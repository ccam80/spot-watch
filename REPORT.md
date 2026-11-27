# Spot placement score log

Generated 2026-11-27 08:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 574 | 46% | 5.0 | 1 (11-27 08:12Z) |
| ap-northeast-1 | 574 | 18% | 2.8 | 1 (11-27 08:12Z) |
| ap-northeast-2 | 574 | 68% | 7.0 | 1 (11-27 08:12Z) |
| ap-south-1 | 574 | 3% | 1.7 | 2 (11-27 08:12Z) |
| ap-southeast-2 | 574 | 1% | 1.0 | 1 (11-27 08:12Z) |
| ap-southeast-3 | 574 | 22% | 3.0 | 1 (11-27 08:12Z) |
| us-east-1 | 574 | 13% | 2.8 | 4 (11-27 08:12Z) |
| us-east-2 | 574 | 30% | 3.6 | 1 (11-27 08:12Z) |
| us-west-2 | 574 | 9% | 2.1 | 1 (11-27 08:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111199199611391191111111111111111111111111911
ap-northeast-1   121129995999991191211221211299999129211111191211
ap-northeast-2   111111199999999799171691999199991111119999911911
ap-south-1       111111111191111111111111111111191121122111121222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111211311131111111111111111111111111111111
us-east-1        233344223323737465467654656566754465455444535434
us-east-2        111111119919919991119918111111111111111119111111
us-west-2        112122111219111121121212112111521319112121123211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 177 | 5% | 1.5 | 1 (11-27 08:12Z) |
| ap-east-1 ape1-az2 | 403 | 66% | 6.6 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 141 | 11% | 1.9 | 1 (11-26 23:45Z) |
| ap-northeast-1 apne1-az4 | 270 | 29% | 3.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az1 | 475 | 63% | 6.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az3 | 523 | 68% | 6.9 | 1 (11-27 08:12Z) |
| ap-northeast-2 apne2-az4 | 553 | 70% | 7.1 | 1 (11-26 23:45Z) |
| ap-south-1 aps1-az1 | 172 | 2% | 1.4 | 1 (11-27 08:12Z) |
| ap-south-1 aps1-az3 | 167 | 7% | 2.3 | 1 (11-26 23:45Z) |
| ap-southeast-2 apse2-az1 | 121 | 2% | 1.2 | 1 (11-27 08:12Z) |
| ap-southeast-2 apse2-az2 | 87 | 0% | 1.0 | 1 (11-26 23:45Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 339 | 36% | 4.2 | 1 (11-26 23:45Z) |
| us-east-1 use1-az1 | 130 | 0% | 1.0 | 1 (11-26 23:45Z) |
| us-east-1 use1-az2 | 150 | 3% | 1.4 | 1 (11-27 08:12Z) |
| us-east-1 use1-az4 | 199 | 19% | 2.8 | 1 (11-26 15:01Z) |
| us-east-1 use1-az5 | 185 | 23% | 3.0 | 1 (11-27 08:12Z) |
| us-east-1 use1-az6 | 150 | 21% | 2.8 | 1 (11-27 08:12Z) |
| us-east-2 use2-az1 | 246 | 42% | 4.5 | 1 (11-26 15:01Z) |
| us-east-2 use2-az2 | 289 | 51% | 5.2 | 1 (11-27 08:12Z) |
| us-east-2 use2-az3 | 314 | 47% | 5.1 | 1 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 140 | 15% | 2.4 | 1 (11-26 23:45Z) |
| us-west-2 usw2-az3 | 221 | 16% | 2.6 | 1 (11-27 08:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 574 | 73% | 7.4 | 9 (11-27 08:12Z) |
| ap-northeast-1 | 574 | 72% | 7.0 | 2 (11-27 08:12Z) |
| ap-northeast-2 | 574 | 100% | 9.0 | 2 (11-27 08:12Z) |
| ap-south-1 | 574 | 57% | 5.9 | 2 (11-27 08:12Z) |
| ap-southeast-2 | 574 | 28% | 3.7 | 1 (11-27 08:12Z) |
| ap-southeast-3 | 574 | 22% | 3.0 | 1 (11-27 08:12Z) |
| us-east-1 | 574 | 74% | 6.6 | 8 (11-27 08:12Z) |
| us-east-2 | 574 | 68% | 6.7 | 9 (11-27 08:12Z) |
| us-west-2 | 574 | 52% | 5.7 | 9 (11-27 08:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   894299999999992292991993991999999999999291991992
ap-northeast-2   999999999999999999999999999999999999999999999992
ap-south-1       119111111991111111111111111111191121122141151292
ap-southeast-2   991191329999911181911911991199999199919191911991
ap-southeast-3   111111111211311131111111111111111111111111111111
us-east-1        966978999997999998889888888899999899998788878898
us-east-2        999999999999919999589929919932911199493999339929
us-west-2        434194239939991159954535324444995699995969949999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 376 | 86% | 8.1 | 9 (11-27 08:12Z) |
| ap-east-1 ape1-az2 | 337 | 88% | 8.3 | 9 (11-27 08:12Z) |
| ap-east-1 ape1-az3 | 373 | 88% | 8.3 | 9 (11-27 08:12Z) |
| ap-northeast-1 apne1-az1 | 229 | 95% | 8.7 | 9 (11-25 22:26Z) |
| ap-northeast-1 apne1-az2 | 218 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-northeast-1 apne1-az4 | 296 | 99% | 8.9 | 9 (11-26 23:45Z) |
| ap-northeast-2 apne2-az1 | 461 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 483 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az4 | 378 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 189 | 80% | 7.8 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az3 | 203 | 90% | 8.4 | 9 (11-26 23:45Z) |
| ap-southeast-2 apse2-az1 | 84 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 96 | 85% | 8.1 | 9 (11-25 12:40Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 163 | 90% | 8.3 | 2 (11-27 08:12Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 145 | 93% | 8.5 | 9 (11-26 23:45Z) |
| us-east-2 use2-az1 | 208 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az2 | 225 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az3 | 250 | 97% | 8.8 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 113 | 98% | 8.9 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az2 | 101 | 91% | 8.4 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az3 | 154 | 88% | 8.2 | 9 (11-27 08:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708000 | 2026-11-27T08:12:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-27T08:12:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731700 | 2026-11-27T08:12:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.610300 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626500 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.607600 | 2026-11-27T08:12:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-27T08:12:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.778900 | 2026-11-27T08:12:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.392000 | 2026-11-27T08:12:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.692300 | 2026-11-27T08:12:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.402400 | 2026-11-27T08:12:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700800 | 2026-11-27T08:12:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.506600 | 2026-11-27T08:12:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.569800 | 2026-11-27T08:12:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.521900 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.795200 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.905700 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1b | Windows | 0.341800 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.878600 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.861400 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.867100 | 2026-11-27T08:12:05Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542700 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552700 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547100 | 2026-11-27T08:12:05Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.621100 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2a | Windows | 0.291000 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906200 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535800 | 2026-11-27T08:12:05Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-27T08:12:05Z |
