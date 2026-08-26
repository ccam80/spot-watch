"""Render REPORT.md and report/heatmap.svg from data/scores.csv."""

import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORT_DIR = ROOT / "report"
STRIP = 48  # hours shown in the recent timeline


def glyph(score):
    """One character per hourly score: digits, or a dot for no sample."""
    if score is None:
        return "·"
    return str(min(int(score), 9))


def load_scores():
    """Return region-level rows grouped by score set, plus AZ rows."""
    path = DATA / "scores.csv"
    if not path.exists():
        return {}, {}
    region_rows = defaultdict(list)
    az_rows = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            row["score"] = int(row["score"]) if row["score"] else None
            row["time"] = datetime.strptime(
                row["timestamp_utc"], "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc)
            target = region_rows if row["level"] == "region" else az_rows
            target[row["score_set"]].append(row)
    return region_rows, az_rows


def by_region(rows):
    """Map region -> list of (time, score) sorted by time."""
    series = defaultdict(list)
    for row in rows:
        series[row["region"]].append((row["time"], row["score"]))
    for values in series.values():
        values.sort()
    return series


def availability_table(series, threshold):
    """Markdown rows: share of samples at or above the threshold."""
    lines = [
        f"| region | samples | hours ≥ {threshold} | mean score | latest |",
        "|---|---|---|---|---|",
    ]
    for region in sorted(series):
        values = [s for _, s in series[region] if s is not None]
        if not values:
            continue
        share = sum(1 for s in values if s >= threshold) / len(values)
        latest_time, latest = series[region][-1]
        lines.append(
            f"| {region} | {len(values)} | {share:.0%} | "
            f"{sum(values) / len(values):.1f} | {latest} "
            f"({latest_time:%m-%d %H:%M}Z) |"
        )
    return "\n".join(lines)


def hour_of_day_table(series):
    """Markdown rows: mean score per UTC hour for each region."""
    header = "| region | " + " | ".join(f"{h:02d}" for h in range(24)) + " |"
    lines = [header, "|---|" + "---|" * 24]
    for region in sorted(series):
        buckets = defaultdict(list)
        for time, score in series[region]:
            if score is not None:
                buckets[time.hour].append(score)
        cells = []
        for hour in range(24):
            values = buckets.get(hour)
            cells.append(
                f"{sum(values) / len(values):.0f}" if values else "·"
            )
        lines.append(f"| {region} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def timeline(series):
    """Fixed-width strip of the last STRIP hourly scores per region."""
    lines = ["```", f"{'region':16} oldest → newest ({STRIP} h, one char per sample)"]
    for region in sorted(series):
        recent = series[region][-STRIP:]
        strip = "".join(glyph(score) for _, score in recent)
        lines.append(f"{region:16} {strip:>{STRIP}}")
    lines.append("```")
    return "\n".join(lines)


def heatmap_svg(series, path):
    """Region x UTC-hour heatmap of mean scores as a standalone SVG."""
    regions = sorted(series)
    cell, left, top = 22, 130, 30
    width = left + 24 * cell + 10
    height = top + len(regions) * cell + 10
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" font-family="monospace" font-size="11">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
    ]
    for hour in range(24):
        parts.append(
            f'<text x="{left + hour * cell + 4}" y="{top - 8}">{hour:02d}</text>'
        )
    for row, region in enumerate(regions):
        buckets = defaultdict(list)
        for time, score in series[region]:
            if score is not None:
                buckets[time.hour].append(score)
        y = top + row * cell
        parts.append(f'<text x="4" y="{y + 15}">{region}</text>')
        for hour in range(24):
            values = buckets.get(hour)
            if values:
                mean = sum(values) / len(values)
                shade = int(255 - 255 * min(mean, 10) / 10)
                fill = f"rgb({shade},{255 - shade // 2},{shade})"
                label = f"{mean:.0f}"
            else:
                fill, label = "#eeeeee", ""
            x = left + hour * cell
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell - 1}" '
                f'height="{cell - 1}" fill="{fill}"/>'
            )
            if label:
                parts.append(
                    f'<text x="{x + 6}" y="{y + 15}">{label}</text>'
                )
    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts), encoding="utf-8")


def latest_prices():
    """Markdown rows for the newest price sample per region and product."""
    path = DATA / "prices.csv"
    if not path.exists():
        return "_no price samples yet_"
    latest = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = (row["region"], row["az"], row["product"])
            if key not in latest or row["timestamp_utc"] > latest[key]["timestamp_utc"]:
                latest[key] = row
    lines = ["| region | az | product | $/h | sampled |", "|---|---|---|---|---|"]
    for key in sorted(latest):
        row = latest[key]
        lines.append(
            f"| {row['region']} | {row['az']} | {row['product']} | "
            f"{row['spot_price']} | {row['timestamp_utc']} |"
        )
    return "\n".join(lines)


def main():
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    threshold = config["available_score"]
    region_rows, az_rows = load_scores()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    sections = [
        "# Spot placement score log",
        f"Generated {now}. Scores are 1–10; "
        f"a region counts as available at ≥ {threshold}. "
        "The single-type set is scored low by design (EC2 wants three "
        "or more instance types); read it relative to itself over time "
        "and use the trio set as the calibrated reference.",
    ]
    for set_name, types in config["score_sets"].items():
        series = by_region(region_rows.get(set_name, []))
        sections.append(f"## {set_name} ({', '.join(types)})")
        if not series:
            sections.append("_no samples yet_")
            continue
        sections.append(availability_table(series, threshold))
        sections.append(f"### Last {STRIP} samples")
        sections.append(timeline(series))
        sections.append("### Mean score by UTC hour")
        sections.append(hour_of_day_table(series))
        svg = REPORT_DIR / f"heatmap-{set_name}.svg"
        heatmap_svg(series, svg)
        sections.append(f"![{set_name} heatmap](report/heatmap-{set_name}.svg)")
        az_series = defaultdict(list)
        for row in az_rows.get(set_name, []):
            az_series[f"{row['region']} {row['az_id']}"].append(
                (row["time"], row["score"])
            )
        if az_series:
            for values in az_series.values():
                values.sort()
            sections.append("### Best single AZ per sample")
            sections.append(availability_table(az_series, threshold))
    sections.append("## Latest spot prices")
    sections.append(latest_prices())
    (ROOT / "REPORT.md").write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print("REPORT.md written")


if __name__ == "__main__":
    main()
