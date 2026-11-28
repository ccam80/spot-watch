# Spot placement score log

Generated 2026-11-28 02:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 583 | 46% | 4.9 | 1 (11-28 02:18Z) |
| ap-northeast-1 | 583 | 18% | 2.9 | 1 (11-28 02:18Z) |
| ap-northeast-2 | 583 | 68% | 7.0 | 9 (11-28 02:18Z) |
| ap-south-1 | 583 | 3% | 1.7 | 1 (11-28 02:18Z) |
| ap-southeast-2 | 583 | 1% | 1.0 | 1 (11-28 02:18Z) |
| ap-southeast-3 | 583 | 22% | 3.0 | 1 (11-28 02:18Z) |
| us-east-1 | 583 | 13% | 2.8 | 3 (11-28 02:18Z) |
| us-east-2 | 583 | 29% | 3.5 | 1 (11-28 02:18Z) |
| us-west-2 | 583 | 9% | 2.1 | 7 (11-28 02:18Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199611391191111111111111111111111111911111111191
ap-northeast-1   999991191211221211299999129211111191211161999111
ap-northeast-2   999999799171691999199991111119999911911999899999
ap-south-1       191111111111111111111191121122111121222111111111
ap-southeast-2   111111111111111111111111111111111111111111121111
ap-southeast-3   211311131111111111111111111111111111111111111111
us-east-1        323737465467654656566754465455444535434334333333
us-east-2        919919991119918111111111111111119111111111111111
us-west-2        219111121121212112111521319112121123211333397997
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 180 | 5% | 1.5 | 1 (11-28 01:15Z) |
| ap-east-1 ape1-az2 | 406 | 65% | 6.6 | 9 (11-28 01:15Z) |
| ap-northeast-1 apne1-az1 | 147 | 10% | 1.9 | 1 (11-28 02:18Z) |
| ap-northeast-1 apne1-az4 | 277 | 29% | 3.6 | 1 (11-28 01:15Z) |
| ap-northeast-2 apne2-az1 | 483 | 64% | 6.6 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 528 | 68% | 6.9 | 1 (11-28 02:18Z) |
| ap-northeast-2 apne2-az4 | 559 | 70% | 7.1 | 9 (11-28 01:15Z) |
| ap-south-1 aps1-az1 | 175 | 2% | 1.4 | 1 (11-28 02:18Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 125 | 2% | 1.2 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az2 | 90 | 0% | 1.0 | 1 (11-27 21:12Z) |
| ap-southeast-3 apse3-az1 | 108 | 0% | 1.0 | 1 (11-28 01:15Z) |
| ap-southeast-3 apse3-az3 | 341 | 35% | 4.1 | 1 (11-28 02:18Z) |
| us-east-1 use1-az1 | 134 | 0% | 1.0 | 1 (11-28 02:18Z) |
| us-east-1 use1-az2 | 151 | 3% | 1.4 | 1 (11-27 19:11Z) |
| us-east-1 use1-az4 | 203 | 19% | 2.7 | 1 (11-28 02:18Z) |
| us-east-1 use1-az5 | 191 | 22% | 2.9 | 1 (11-28 00:33Z) |
| us-east-1 use1-az6 | 152 | 20% | 2.8 | 1 (11-27 23:12Z) |
| us-east-2 use2-az1 | 247 | 42% | 4.5 | 1 (11-27 19:11Z) |
| us-east-2 use2-az2 | 291 | 50% | 5.2 | 1 (11-28 01:15Z) |
| us-east-2 use2-az3 | 316 | 47% | 5.1 | 1 (11-28 00:33Z) |
| us-west-2 usw2-az1 | 187 | 21% | 3.0 | 2 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 144 | 15% | 2.3 | 1 (11-28 02:18Z) |
| us-west-2 usw2-az3 | 225 | 16% | 2.6 | 1 (11-28 02:18Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 583 | 74% | 7.4 | 9 (11-28 02:18Z) |
| ap-northeast-1 | 583 | 73% | 7.1 | 9 (11-28 02:18Z) |
| ap-northeast-2 | 583 | 100% | 9.0 | 9 (11-28 02:18Z) |
| ap-south-1 | 583 | 57% | 5.9 | 9 (11-28 02:18Z) |
| ap-southeast-2 | 583 | 29% | 3.8 | 9 (11-28 02:18Z) |
| ap-southeast-3 | 583 | 22% | 3.0 | 1 (11-28 02:18Z) |
| us-east-1 | 583 | 74% | 6.6 | 9 (11-28 02:18Z) |
| us-east-2 | 583 | 67% | 6.6 | 1 (11-28 02:18Z) |
| us-west-2 | 583 | 53% | 5.7 | 9 (11-28 02:18Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999992292991993991999999999999291991992999999999
ap-northeast-2   999999999999999999999999999999999999992999999999
ap-south-1       991111111111111111111191121122141151292999999999
ap-southeast-2   999911181911911991199999199919191911991999999999
ap-southeast-3   211311131111111111111111111111111111111111111111
us-east-1        997999998889888888899999899998788878898778878789
us-east-2        999919999589929919932911199493999339929221222111
us-west-2        939991159954535324444995699995969949999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 382 | 86% | 8.2 | 9 (11-28 01:15Z) |
| ap-east-1 ape1-az2 | 341 | 88% | 8.3 | 9 (11-28 02:18Z) |
| ap-east-1 ape1-az3 | 379 | 88% | 8.3 | 9 (11-28 02:18Z) |
| ap-northeast-1 apne1-az1 | 234 | 95% | 8.7 | 9 (11-27 23:12Z) |
| ap-northeast-1 apne1-az2 | 222 | 88% | 8.3 | 9 (11-27 23:12Z) |
| ap-northeast-1 apne1-az4 | 300 | 99% | 8.9 | 9 (11-28 01:15Z) |
| ap-northeast-2 apne2-az1 | 467 | 100% | 9.0 | 9 (11-28 01:15Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 489 | 100% | 9.0 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az4 | 381 | 88% | 8.3 | 9 (11-28 01:15Z) |
| ap-south-1 aps1-az1 | 187 | 88% | 8.3 | 9 (11-28 02:18Z) |
| ap-south-1 aps1-az2 | 190 | 81% | 7.8 | 9 (11-27 21:12Z) |
| ap-south-1 aps1-az3 | 210 | 90% | 8.4 | 9 (11-28 02:18Z) |
| ap-southeast-2 apse2-az1 | 89 | 89% | 8.3 | 9 (11-28 02:18Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 102 | 86% | 8.1 | 9 (11-28 01:15Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 163 | 90% | 8.3 | 2 (11-27 08:12Z) |
| us-east-1 use1-az5 | 118 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-east-1 use1-az6 | 145 | 93% | 8.5 | 9 (11-26 23:45Z) |
| us-east-2 use2-az1 | 208 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az2 | 225 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az3 | 250 | 97% | 8.8 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 117 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 107 | 92% | 8.4 | 9 (11-28 01:15Z) |
| us-west-2 usw2-az3 | 161 | 89% | 8.2 | 9 (11-28 02:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707800 | 2026-11-28T02:18:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T02:18:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.730900 | 2026-11-28T02:18:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.612900 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.627600 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.611600 | 2026-11-28T02:18:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T02:18:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.753900 | 2026-11-28T02:18:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.389500 | 2026-11-28T02:18:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.687300 | 2026-11-28T02:18:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.398600 | 2026-11-28T02:18:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.702500 | 2026-11-28T02:18:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502100 | 2026-11-28T02:18:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.576400 | 2026-11-28T02:18:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519700 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.791200 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.917300 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881500 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1c | Windows | 0.286600 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.870300 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.875200 | 2026-11-28T02:18:54Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545100 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.553700 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548500 | 2026-11-28T02:18:54Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.640600 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2a | Windows | 0.289500 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.908100 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-11-28T02:18:54Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T02:18:54Z |
