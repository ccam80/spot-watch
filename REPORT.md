# Spot placement score log

Generated 2026-11-28 14:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 595 | 46% | 4.9 | 9 (11-28 14:12Z) |
| ap-northeast-1 | 595 | 18% | 2.9 | 9 (11-28 14:12Z) |
| ap-northeast-2 | 595 | 68% | 6.9 | 1 (11-28 14:12Z) |
| ap-south-1 | 595 | 3% | 1.6 | 1 (11-28 14:12Z) |
| ap-southeast-2 | 595 | 1% | 1.1 | 9 (11-28 14:12Z) |
| ap-southeast-3 | 595 | 22% | 3.0 | 8 (11-28 14:12Z) |
| us-east-1 | 595 | 13% | 2.8 | 5 (11-28 14:12Z) |
| us-east-2 | 595 | 29% | 3.5 | 7 (11-28 14:12Z) |
| us-west-2 | 595 | 11% | 2.2 | 9 (11-28 14:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111911111111191191111119999
ap-northeast-1   221211299999129211111191211161999111112212123399
ap-northeast-2   691999199991111119999911911999899999911115119211
ap-south-1       111111111191121122111121222111111111111111111111
ap-southeast-2   111111111111111111111111111111121111111111112559
ap-southeast-3   111111111111111111111111111111111111113111138668
us-east-1        654656566754465455444535434334333333444333423345
us-east-2        918111111111111111119111111111111111111111114227
us-west-2        212112111521319112121123211333397997999911299999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 7 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 186 | 5% | 1.5 | 1 (11-28 12:18Z) |
| ap-east-1 ape1-az2 | 411 | 66% | 6.6 | 9 (11-28 14:12Z) |
| ap-northeast-1 apne1-az1 | 151 | 10% | 1.9 | 4 (11-28 14:12Z) |
| ap-northeast-1 apne1-az4 | 280 | 29% | 3.7 | 9 (11-28 14:12Z) |
| ap-northeast-2 apne2-az1 | 486 | 64% | 6.6 | 2 (11-28 08:17Z) |
| ap-northeast-2 apne2-az3 | 533 | 67% | 6.8 | 9 (11-28 11:12Z) |
| ap-northeast-2 apne2-az4 | 561 | 70% | 7.1 | 9 (11-28 11:12Z) |
| ap-south-1 aps1-az1 | 183 | 2% | 1.3 | 1 (11-28 12:18Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 130 | 4% | 1.3 | 9 (11-28 14:12Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 111 | 0% | 1.0 | 1 (11-28 10:12Z) |
| ap-southeast-3 apse3-az3 | 348 | 36% | 4.2 | 8 (11-28 14:12Z) |
| us-east-1 use1-az1 | 135 | 0% | 1.0 | 1 (11-28 07:14Z) |
| us-east-1 use1-az2 | 158 | 3% | 1.3 | 1 (11-28 13:12Z) |
| us-east-1 use1-az4 | 215 | 18% | 2.7 | 2 (11-28 14:12Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 161 | 19% | 2.7 | 2 (11-28 13:12Z) |
| us-east-2 use2-az1 | 252 | 41% | 4.5 | 3 (11-28 14:12Z) |
| us-east-2 use2-az2 | 298 | 49% | 5.1 | 2 (11-28 11:12Z) |
| us-east-2 use2-az3 | 319 | 47% | 5.0 | 2 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 196 | 25% | 3.3 | 9 (11-28 14:12Z) |
| us-west-2 usw2-az2 | 147 | 15% | 2.4 | 1 (11-28 07:14Z) |
| us-west-2 usw2-az3 | 236 | 18% | 2.7 | 6 (11-28 14:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 595 | 74% | 7.5 | 9 (11-28 14:12Z) |
| ap-northeast-1 | 595 | 73% | 7.1 | 9 (11-28 14:12Z) |
| ap-northeast-2 | 595 | 100% | 9.0 | 9 (11-28 14:12Z) |
| ap-south-1 | 595 | 57% | 5.9 | 2 (11-28 14:12Z) |
| ap-southeast-2 | 595 | 31% | 3.9 | 9 (11-28 14:12Z) |
| ap-southeast-3 | 595 | 22% | 3.0 | 8 (11-28 14:12Z) |
| us-east-1 | 595 | 75% | 6.7 | 9 (11-28 14:12Z) |
| us-east-2 | 595 | 67% | 6.6 | 9 (11-28 14:12Z) |
| us-west-2 | 595 | 54% | 5.8 | 9 (11-28 14:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   993991999999999999291991992999999999999999999999
ap-northeast-2   999999999999999999999999992999999999999999999999
ap-south-1       111111111191121122141151292999999999919681111112
ap-southeast-2   911991199999199919191911991999999999999999999999
ap-southeast-3   111111111111111111111111111111111111113111138668
us-east-1        888888899999899998788878898778878789999999999999
us-east-2        929919932911199493999339929221222111299999999999
us-west-2        535324444995699995969949999999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 389 | 86% | 8.2 | 9 (11-28 13:12Z) |
| ap-east-1 ape1-az2 | 346 | 88% | 8.3 | 9 (11-28 14:12Z) |
| ap-east-1 ape1-az3 | 383 | 89% | 8.3 | 9 (11-28 11:12Z) |
| ap-northeast-1 apne1-az1 | 239 | 95% | 8.7 | 9 (11-28 13:12Z) |
| ap-northeast-1 apne1-az2 | 224 | 88% | 8.3 | 9 (11-28 13:12Z) |
| ap-northeast-1 apne1-az4 | 309 | 99% | 8.9 | 9 (11-28 13:12Z) |
| ap-northeast-2 apne2-az1 | 473 | 100% | 9.0 | 9 (11-28 13:12Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 496 | 100% | 9.0 | 9 (11-28 14:12Z) |
| ap-northeast-2 apne2-az4 | 386 | 88% | 8.3 | 9 (11-28 14:12Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 91 | 89% | 8.3 | 9 (11-28 09:14Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 109 | 87% | 8.2 | 9 (11-28 14:12Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 36 | 58% | 6.0 | 9 (11-28 13:12Z) |
| us-east-1 use1-az2 | 132 | 99% | 9.0 | 9 (11-28 14:12Z) |
| us-east-1 use1-az4 | 167 | 90% | 8.3 | 9 (11-28 13:12Z) |
| us-east-1 use1-az5 | 118 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-east-1 use1-az6 | 154 | 94% | 8.5 | 9 (11-28 14:12Z) |
| us-east-2 use2-az1 | 216 | 99% | 8.9 | 9 (11-28 14:12Z) |
| us-east-2 use2-az2 | 228 | 99% | 8.9 | 9 (11-28 14:12Z) |
| us-east-2 use2-az3 | 257 | 97% | 8.8 | 9 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 117 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 115 | 92% | 8.4 | 9 (11-28 14:12Z) |
| us-west-2 usw2-az3 | 164 | 89% | 8.2 | 9 (11-28 13:12Z) |
| us-west-2 usw2-az4 | 1 | 100% | 9.0 | 9 (11-28 12:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T14:12:47Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T14:12:47Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732400 | 2026-11-28T14:12:47Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.620000 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.630300 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.620300 | 2026-11-28T14:12:47Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T14:12:47Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.728000 | 2026-11-28T14:12:47Z |
| ap-south-1 | ap-south-1a | Windows | 0.386000 | 2026-11-28T14:12:47Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.685400 | 2026-11-28T14:12:47Z |
| ap-south-1 | ap-south-1b | Windows | 0.394600 | 2026-11-28T14:12:47Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.705400 | 2026-11-28T14:12:47Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499600 | 2026-11-28T14:12:47Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.583200 | 2026-11-28T14:12:47Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519000 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.785900 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.922300 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1b | Windows | 0.347600 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.890300 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1c | Windows | 0.287000 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.878600 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.877200 | 2026-11-28T14:12:47Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548800 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.554100 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T14:12:47Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.643100 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2a | Windows | 0.291000 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906000 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548300 | 2026-11-28T14:12:47Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T14:12:47Z |
