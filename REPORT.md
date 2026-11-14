# Spot placement score log

Generated 2026-11-14 16:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 535 | 48% | 5.2 | 9 (11-14 16:59Z) |
| ap-northeast-1 | 535 | 17% | 2.8 | 5 (11-14 16:59Z) |
| ap-northeast-2 | 535 | 68% | 7.0 | 9 (11-14 16:59Z) |
| ap-south-1 | 535 | 3% | 1.7 | 1 (11-14 16:59Z) |
| ap-southeast-2 | 535 | 1% | 1.0 | 1 (11-14 16:59Z) |
| ap-southeast-3 | 535 | 24% | 3.1 | 1 (11-14 16:59Z) |
| us-east-1 | 535 | 10% | 2.6 | 3 (11-14 16:59Z) |
| us-east-2 | 535 | 30% | 3.6 | 9 (11-14 16:59Z) |
| us-west-2 | 535 | 9% | 2.1 | 1 (11-14 16:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999191911112991119199991999819919121911111111199
ap-northeast-1   951191191112211211119199919911211111511121129995
ap-northeast-2   999999992999999999999999999999999991911111111199
ap-south-1       698111111211122222122211311911112211111111111111
ap-southeast-2   111111111117111111111111111111111111111111111111
ap-southeast-3   386181111111111311111111113111111111311111111111
us-east-1        999912112333332232213222222329293322423233344223
us-east-2        999991191211191111111999919999111111111111111119
us-west-2        711121122211191111122922111211111212221112122111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 168 | 5% | 1.5 | 1 (11-13 07:49Z) |
| ap-east-1 ape1-az2 | 392 | 66% | 6.6 | 9 (11-14 16:59Z) |
| ap-northeast-1 apne1-az1 | 126 | 10% | 1.9 | 1 (11-14 10:14Z) |
| ap-northeast-1 apne1-az4 | 246 | 26% | 3.5 | 3 (11-14 16:59Z) |
| ap-northeast-2 apne2-az1 | 456 | 63% | 6.6 | 9 (11-14 16:59Z) |
| ap-northeast-2 apne2-az3 | 494 | 69% | 7.0 | 9 (11-14 16:59Z) |
| ap-northeast-2 apne2-az4 | 522 | 70% | 7.1 | 9 (11-14 16:59Z) |
| ap-south-1 aps1-az1 | 156 | 1% | 1.3 | 1 (11-14 03:05Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 110 | 3% | 1.2 | 1 (11-14 03:05Z) |
| ap-southeast-2 apse2-az2 | 77 | 0% | 1.0 | 1 (11-14 10:14Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 326 | 37% | 4.3 | 1 (11-14 16:59Z) |
| us-east-1 use1-az1 | 112 | 0% | 1.1 | 1 (11-13 22:31Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 170 | 22% | 2.9 | 1 (11-13 22:31Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 132 | 23% | 3.0 | 1 (11-14 16:59Z) |
| us-east-2 use2-az1 | 234 | 42% | 4.5 | 9 (11-14 16:59Z) |
| us-east-2 use2-az2 | 271 | 51% | 5.3 | 9 (11-14 16:59Z) |
| us-east-2 use2-az3 | 301 | 47% | 5.1 | 9 (11-14 16:59Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 204 | 17% | 2.7 | 1 (11-13 22:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 535 | 71% | 7.3 | 9 (11-14 16:59Z) |
| ap-northeast-1 | 535 | 72% | 7.0 | 9 (11-14 16:59Z) |
| ap-northeast-2 | 535 | 100% | 9.0 | 9 (11-14 16:59Z) |
| ap-south-1 | 535 | 60% | 6.1 | 1 (11-14 16:59Z) |
| ap-southeast-2 | 535 | 26% | 3.6 | 9 (11-14 16:59Z) |
| ap-southeast-3 | 535 | 24% | 3.1 | 1 (11-14 16:59Z) |
| us-east-1 | 535 | 72% | 6.5 | 9 (11-14 16:59Z) |
| us-east-2 | 535 | 68% | 6.7 | 9 (11-14 16:59Z) |
| us-west-2 | 535 | 51% | 5.6 | 9 (11-14 16:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999299999219919922999999999993922992992894299999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999119112911922992199217911991392291111119111111
ap-southeast-2   991111191119199119999999919911911911991991191329
ap-southeast-3   386181111111111311111111113111111111311111111111
us-east-1        999945234697655579579999999999599669968966978999
us-east-2        999991991991291119119999999999119919919999999999
us-west-2        994492445434294944195955999999494334933434194239
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 7 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 344 | 84% | 8.1 | 9 (11-14 03:05Z) |
| ap-east-1 ape1-az2 | 310 | 87% | 8.2 | 9 (11-14 10:14Z) |
| ap-east-1 ape1-az3 | 341 | 87% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az1 | 216 | 95% | 8.7 | 9 (11-14 16:59Z) |
| ap-northeast-1 apne1-az2 | 197 | 86% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az4 | 277 | 99% | 8.9 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az1 | 433 | 100% | 9.0 | 9 (11-14 10:14Z) |
| ap-northeast-2 apne2-az2 | 118 | 86% | 8.1 | 9 (11-14 16:59Z) |
| ap-northeast-2 apne2-az3 | 450 | 100% | 9.0 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az4 | 352 | 87% | 8.2 | 9 (11-14 16:59Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 84 | 83% | 8.0 | 9 (11-14 16:59Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 115 | 99% | 8.9 | 9 (11-14 16:59Z) |
| us-east-1 use1-az4 | 154 | 92% | 8.4 | 9 (11-14 16:59Z) |
| us-east-1 use1-az5 | 110 | 98% | 8.9 | 9 (11-14 16:59Z) |
| us-east-1 use1-az6 | 134 | 93% | 8.5 | 9 (11-13 07:49Z) |
| us-east-2 use2-az1 | 189 | 99% | 8.9 | 9 (11-14 03:05Z) |
| us-east-2 use2-az2 | 210 | 99% | 8.9 | 9 (11-14 10:14Z) |
| us-east-2 use2-az3 | 236 | 97% | 8.8 | 9 (11-14 10:14Z) |
| us-west-2 usw2-az1 | 99 | 98% | 8.8 | 9 (11-14 16:59Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 139 | 88% | 8.1 | 9 (11-14 16:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706700 | 2026-11-14T16:59:20Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-14T16:59:20Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.709400 | 2026-11-14T16:59:20Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593100 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.608900 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.593000 | 2026-11-14T16:59:20Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-14T16:59:20Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.654300 | 2026-11-14T16:59:20Z |
| ap-south-1 | ap-south-1a | Windows | 0.386700 | 2026-11-14T16:59:20Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.615500 | 2026-11-14T16:59:20Z |
| ap-south-1 | ap-south-1b | Windows | 0.378000 | 2026-11-14T16:59:20Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.632000 | 2026-11-14T16:59:20Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502500 | 2026-11-14T16:59:20Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.549600 | 2026-11-14T16:59:20Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.832000 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.777300 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.567600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.573600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.508100 | 2026-11-14T16:59:20Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548100 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.581500 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548900 | 2026-11-14T16:59:20Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.637700 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2a | Windows | 0.332600 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.570400 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2b | Windows | 0.289600 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.593700 | 2026-11-14T16:59:20Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-14T16:59:20Z |
