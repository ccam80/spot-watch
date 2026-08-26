"""Append one sample of Spot placement scores and prices to data/."""

import csv
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RAW = ROOT / "raw"
SCORE_COLUMNS = [
    "timestamp_utc", "score_set", "instance_types", "level", "region",
    "az_id", "score",
]
PRICE_COLUMNS = [
    "timestamp_utc", "region", "az", "instance_type", "product",
    "spot_price", "price_timestamp_utc",
]


def append_rows(path, columns, rows):
    """Append rows to a CSV, writing the header when the file is new."""
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        if new_file:
            writer.writeheader()
        writer.writerows(rows)


def placement_scores(ec2, config, stamp):
    """Return score rows for every configured set at both levels."""
    rows = []
    raw = {}
    for set_name, types in config["score_sets"].items():
        for level, single_az in (("region", False), ("az", True)):
            response = ec2.get_spot_placement_scores(
                InstanceTypes=types,
                TargetCapacity=config["target_capacity"],
                TargetCapacityUnitType="units",
                SingleAvailabilityZone=single_az,
                RegionNames=config["regions"],
                MaxResults=100,
            )
            raw[f"{set_name}:{level}"] = response
            for entry in response.get("SpotPlacementScores", []):
                rows.append({
                    "timestamp_utc": stamp,
                    "score_set": set_name,
                    "instance_types": "|".join(types),
                    "level": level,
                    "region": entry.get("Region", ""),
                    "az_id": entry.get("AvailabilityZoneId", ""),
                    "score": entry.get("Score", ""),
                })
    return rows, raw


def spot_prices(session, config, stamp, now):
    """Return the latest spot price per AZ and product in each region."""
    rows = []
    raw = {}
    for region in config["regions"]:
        ec2 = session.client("ec2", region_name=region)
        try:
            response = ec2.describe_spot_price_history(
                InstanceTypes=config["price_instance_types"],
                ProductDescriptions=config["price_products"],
                StartTime=now - timedelta(hours=6),
                EndTime=now,
            )
        except Exception as error:  # a region denied by policy is skipped
            print(f"{region} price history skipped: {error}", file=sys.stderr)
            continue
        raw[region] = response
        latest = {}
        for entry in response.get("SpotPriceHistory", []):
            key = (
                entry["AvailabilityZone"], entry["InstanceType"],
                entry["ProductDescription"],
            )
            if key not in latest or entry["Timestamp"] > latest[key]["Timestamp"]:
                latest[key] = entry
        for (az, instance_type, product), entry in sorted(latest.items()):
            rows.append({
                "timestamp_utc": stamp,
                "region": region,
                "az": az,
                "instance_type": instance_type,
                "product": product,
                "spot_price": entry["SpotPrice"],
                "price_timestamp_utc": entry["Timestamp"].strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
            })
    return rows, raw


def main():
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).replace(microsecond=0)
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    session = boto3.session.Session()
    home = session.client(
        "ec2", region_name=os.environ.get("AWS_REGION", "us-east-2")
    )

    score_rows, score_raw = placement_scores(home, config, stamp)
    append_rows(DATA / "scores.csv", SCORE_COLUMNS, score_rows)
    print(f"{len(score_rows)} score rows at {stamp}")

    price_rows, price_raw = spot_prices(session, config, stamp, now)
    if price_rows:
        append_rows(DATA / "prices.csv", PRICE_COLUMNS, price_rows)
    print(f"{len(price_rows)} price rows at {stamp}")

    for response in list(score_raw.values()) + list(price_raw.values()):
        response.pop("ResponseMetadata", None)
    RAW.mkdir(exist_ok=True)
    (RAW / f"{stamp.replace(':', '')}.json").write_text(
        json.dumps({"scores": score_raw, "prices": price_raw},
                   default=str, indent=1),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
