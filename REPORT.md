# Spot placement score log

Generated 2026-11-28 08:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 589 | 45% | 4.9 | 1 (11-28 08:17Z) |
| ap-northeast-1 | 589 | 18% | 2.8 | 2 (11-28 08:17Z) |
| ap-northeast-2 | 589 | 68% | 6.9 | 5 (11-28 08:17Z) |
| ap-south-1 | 589 | 3% | 1.7 | 1 (11-28 08:17Z) |
| ap-southeast-2 | 589 | 1% | 1.0 | 1 (11-28 08:17Z) |
| ap-southeast-3 | 589 | 22% | 2.9 | 1 (11-28 08:17Z) |
| us-east-1 | 589 | 13% | 2.8 | 3 (11-28 08:17Z) |
| us-east-2 | 589 | 29% | 3.5 | 1 (11-28 08:17Z) |
| us-west-2 | 589 | 10% | 2.2 | 1 (11-28 08:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        391191111111111111111111111111911111111191191111
ap-northeast-1   191211221211299999129211111191211161999111112212
ap-northeast-2   799171691999199991111119999911911999899999911115
ap-south-1       111111111111111191121122111121222111111111111111
ap-southeast-2   111111111111111111111111111111111111121111111111
ap-southeast-3   131111111111111111111111111111111111111111113111
us-east-1        465467654656566754465455444535434334333333444333
us-east-2        991119918111111111111111119111111111111111111111
us-west-2        121121212112111521319112121123211333397997999911
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 183 | 5% | 1.5 | 1 (11-28 08:17Z) |
| ap-east-1 ape1-az2 | 407 | 65% | 6.6 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az1 | 148 | 10% | 1.9 | 1 (11-28 07:14Z) |
| ap-northeast-1 apne1-az4 | 278 | 29% | 3.6 | 1 (11-28 07:14Z) |
| ap-northeast-2 apne2-az1 | 486 | 64% | 6.6 | 2 (11-28 08:17Z) |
| ap-northeast-2 apne2-az3 | 531 | 67% | 6.8 | 2 (11-28 08:17Z) |
| ap-northeast-2 apne2-az4 | 560 | 70% | 7.1 | 1 (11-28 07:14Z) |
| ap-south-1 aps1-az1 | 180 | 2% | 1.3 | 1 (11-28 08:17Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 125 | 2% | 1.2 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 110 | 0% | 1.0 | 1 (11-28 08:17Z) |
| ap-southeast-3 apse3-az3 | 343 | 35% | 4.1 | 1 (11-28 07:14Z) |
| us-east-1 use1-az1 | 135 | 0% | 1.0 | 1 (11-28 07:14Z) |
| us-east-1 use1-az2 | 155 | 3% | 1.3 | 1 (11-28 06:21Z) |
| us-east-1 use1-az4 | 209 | 18% | 2.7 | 2 (11-28 08:17Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 157 | 20% | 2.7 | 1 (11-28 08:17Z) |
| us-east-2 use2-az1 | 250 | 42% | 4.5 | 1 (11-28 08:17Z) |
| us-east-2 use2-az2 | 295 | 49% | 5.2 | 1 (11-28 08:17Z) |
| us-east-2 use2-az3 | 317 | 47% | 5.1 | 1 (11-28 06:21Z) |
| us-west-2 usw2-az1 | 191 | 23% | 3.1 | 9 (11-28 06:21Z) |
| us-west-2 usw2-az2 | 147 | 15% | 2.4 | 1 (11-28 07:14Z) |
| us-west-2 usw2-az3 | 230 | 17% | 2.6 | 1 (11-28 08:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 589 | 74% | 7.4 | 9 (11-28 08:17Z) |
| ap-northeast-1 | 589 | 73% | 7.1 | 9 (11-28 08:17Z) |
| ap-northeast-2 | 589 | 100% | 9.0 | 9 (11-28 08:17Z) |
| ap-south-1 | 589 | 58% | 5.9 | 1 (11-28 08:17Z) |
| ap-southeast-2 | 589 | 30% | 3.8 | 9 (11-28 08:17Z) |
| ap-southeast-3 | 589 | 22% | 2.9 | 1 (11-28 08:17Z) |
| us-east-1 | 589 | 74% | 6.7 | 9 (11-28 08:17Z) |
| us-east-2 | 589 | 67% | 6.6 | 9 (11-28 08:17Z) |
| us-west-2 | 589 | 53% | 5.8 | 9 (11-28 08:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   292991993991999999999999291991992999999999999999
ap-northeast-2   999999999999999999999999999999992999999999999999
ap-south-1       111111111111111191121122141151292999999999919681
ap-southeast-2   181911911991199999199919191911991999999999999999
ap-southeast-3   131111111111111111111111111111111111111111113111
us-east-1        998889888888899999899998788878898778878789999999
us-east-2        999589929919932911199493999339929221222111299999
us-west-2        159954535324444995699995969949999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 385 | 86% | 8.2 | 9 (11-28 07:14Z) |
| ap-east-1 ape1-az2 | 344 | 88% | 8.3 | 9 (11-28 08:17Z) |
| ap-east-1 ape1-az3 | 381 | 88% | 8.3 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az1 | 236 | 95% | 8.7 | 9 (11-28 07:14Z) |
| ap-northeast-1 apne1-az2 | 223 | 88% | 8.3 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az4 | 304 | 99% | 8.9 | 9 (11-28 07:14Z) |
| ap-northeast-2 apne2-az1 | 470 | 100% | 9.0 | 9 (11-28 05:14Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 493 | 100% | 9.0 | 9 (11-28 08:17Z) |
| ap-northeast-2 apne2-az4 | 384 | 88% | 8.3 | 9 (11-28 08:17Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 90 | 89% | 8.3 | 9 (11-28 07:14Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 105 | 87% | 8.2 | 9 (11-28 08:17Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 33 | 55% | 5.7 | 9 (11-28 07:14Z) |
| us-east-1 use1-az2 | 128 | 99% | 9.0 | 9 (11-28 08:17Z) |
| us-east-1 use1-az4 | 164 | 90% | 8.3 | 9 (11-28 05:14Z) |
| us-east-1 use1-az5 | 118 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-east-1 use1-az6 | 150 | 93% | 8.5 | 9 (11-28 08:17Z) |
| us-east-2 use2-az1 | 212 | 99% | 8.9 | 9 (11-28 08:17Z) |
| us-east-2 use2-az2 | 227 | 99% | 8.9 | 9 (11-28 08:17Z) |
| us-east-2 use2-az3 | 253 | 97% | 8.8 | 9 (11-28 08:17Z) |
| us-west-2 usw2-az1 | 117 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 111 | 92% | 8.4 | 9 (11-28 08:17Z) |
| us-west-2 usw2-az3 | 162 | 89% | 8.2 | 9 (11-28 05:14Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T08:17:04Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T08:17:04Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731800 | 2026-11-28T08:17:04Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.617700 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.629600 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.614800 | 2026-11-28T08:17:04Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T08:17:04Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.739300 | 2026-11-28T08:17:04Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-11-28T08:17:04Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.685400 | 2026-11-28T08:17:04Z |
| ap-south-1 | ap-south-1b | Windows | 0.395500 | 2026-11-28T08:17:04Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.705400 | 2026-11-28T08:17:04Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499600 | 2026-11-28T08:17:04Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.581900 | 2026-11-28T08:17:04Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519000 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.791200 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.920700 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1b | Windows | 0.344500 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.882800 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1c | Windows | 0.286700 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.874800 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.876900 | 2026-11-28T08:17:04Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545100 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552400 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T08:17:04Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.641400 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2a | Windows | 0.290000 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.908100 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547500 | 2026-11-28T08:17:04Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T08:17:04Z |
