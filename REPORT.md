# Spot placement score log

Generated 2026-11-28 10:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 591 | 45% | 4.9 | 1 (11-28 10:12Z) |
| ap-northeast-1 | 591 | 18% | 2.8 | 2 (11-28 10:12Z) |
| ap-northeast-2 | 591 | 68% | 6.9 | 1 (11-28 10:12Z) |
| ap-south-1 | 591 | 3% | 1.7 | 1 (11-28 10:12Z) |
| ap-southeast-2 | 591 | 1% | 1.0 | 1 (11-28 10:12Z) |
| ap-southeast-3 | 591 | 22% | 2.9 | 3 (11-28 10:12Z) |
| us-east-1 | 591 | 13% | 2.8 | 2 (11-28 10:12Z) |
| us-east-2 | 591 | 29% | 3.5 | 1 (11-28 10:12Z) |
| us-west-2 | 591 | 10% | 2.2 | 9 (11-28 10:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119111111111111111111111111191111111119119111111
ap-northeast-1   121122121129999912921111119121116199911111221212
ap-northeast-2   917169199919999111111999991191199989999991111511
ap-south-1       111111111111119112112211112122211111111111111111
ap-southeast-2   111111111111111111111111111111111112111111111111
ap-southeast-3   111111111111111111111111111111111111111111311113
us-east-1        546765465656675446545544453543433433333344433342
us-east-2        111991811111111111111111911111111111111111111111
us-west-2        112121211211152131911212112321133339799799991129
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 5 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 7 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 185 | 5% | 1.5 | 1 (11-28 10:12Z) |
| ap-east-1 ape1-az2 | 407 | 65% | 6.6 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az1 | 148 | 10% | 1.9 | 1 (11-28 07:14Z) |
| ap-northeast-1 apne1-az4 | 278 | 29% | 3.6 | 1 (11-28 07:14Z) |
| ap-northeast-2 apne2-az1 | 486 | 64% | 6.6 | 2 (11-28 08:17Z) |
| ap-northeast-2 apne2-az3 | 532 | 67% | 6.8 | 1 (11-28 09:14Z) |
| ap-northeast-2 apne2-az4 | 560 | 70% | 7.1 | 1 (11-28 07:14Z) |
| ap-south-1 aps1-az1 | 182 | 2% | 1.3 | 1 (11-28 10:12Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 126 | 2% | 1.2 | 1 (11-28 09:14Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 111 | 0% | 1.0 | 1 (11-28 10:12Z) |
| ap-southeast-3 apse3-az3 | 344 | 35% | 4.1 | 3 (11-28 10:12Z) |
| us-east-1 use1-az1 | 135 | 0% | 1.0 | 1 (11-28 07:14Z) |
| us-east-1 use1-az2 | 156 | 3% | 1.3 | 1 (11-28 09:14Z) |
| us-east-1 use1-az4 | 211 | 18% | 2.7 | 2 (11-28 10:12Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 159 | 19% | 2.7 | 1 (11-28 10:12Z) |
| us-east-2 use2-az1 | 251 | 41% | 4.5 | 1 (11-28 10:12Z) |
| us-east-2 use2-az2 | 297 | 49% | 5.1 | 1 (11-28 10:12Z) |
| us-east-2 use2-az3 | 318 | 47% | 5.0 | 1 (11-28 09:14Z) |
| us-west-2 usw2-az1 | 192 | 23% | 3.2 | 9 (11-28 10:12Z) |
| us-west-2 usw2-az2 | 147 | 15% | 2.4 | 1 (11-28 07:14Z) |
| us-west-2 usw2-az3 | 232 | 17% | 2.6 | 9 (11-28 10:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 591 | 74% | 7.4 | 9 (11-28 10:12Z) |
| ap-northeast-1 | 591 | 73% | 7.1 | 9 (11-28 10:12Z) |
| ap-northeast-2 | 591 | 100% | 9.0 | 9 (11-28 10:12Z) |
| ap-south-1 | 591 | 57% | 5.9 | 1 (11-28 10:12Z) |
| ap-southeast-2 | 591 | 30% | 3.8 | 9 (11-28 10:12Z) |
| ap-southeast-3 | 591 | 22% | 2.9 | 3 (11-28 10:12Z) |
| us-east-1 | 591 | 74% | 6.7 | 9 (11-28 10:12Z) |
| us-east-2 | 591 | 67% | 6.6 | 9 (11-28 10:12Z) |
| us-west-2 | 591 | 54% | 5.8 | 9 (11-28 10:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   299199399199999999999929199199299999999999999999
ap-northeast-2   999999999999999999999999999999299999999999999999
ap-south-1       111111111111119112112214115129299999999991968111
ap-southeast-2   191191199119999919991919191199199999999999999999
ap-southeast-3   111111111111111111111111111111111111111111311113
us-east-1        888988888889999989999878887889877887878999999999
us-east-2        958992991993291119949399933992922122211129999999
us-west-2        995453532444499569999596994999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 387 | 86% | 8.2 | 9 (11-28 10:12Z) |
| ap-east-1 ape1-az2 | 345 | 88% | 8.3 | 9 (11-28 09:14Z) |
| ap-east-1 ape1-az3 | 382 | 88% | 8.3 | 9 (11-28 10:12Z) |
| ap-northeast-1 apne1-az1 | 237 | 95% | 8.7 | 9 (11-28 09:14Z) |
| ap-northeast-1 apne1-az2 | 223 | 88% | 8.3 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az4 | 306 | 99% | 8.9 | 9 (11-28 10:12Z) |
| ap-northeast-2 apne2-az1 | 471 | 100% | 9.0 | 9 (11-28 10:12Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 494 | 100% | 9.0 | 9 (11-28 10:12Z) |
| ap-northeast-2 apne2-az4 | 385 | 88% | 8.3 | 9 (11-28 09:14Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 91 | 89% | 8.3 | 9 (11-28 09:14Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 105 | 87% | 8.2 | 9 (11-28 08:17Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 34 | 56% | 5.8 | 9 (11-28 09:14Z) |
| us-east-1 use1-az2 | 130 | 99% | 9.0 | 9 (11-28 10:12Z) |
| us-east-1 use1-az4 | 164 | 90% | 8.3 | 9 (11-28 05:14Z) |
| us-east-1 use1-az5 | 118 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-east-1 use1-az6 | 152 | 93% | 8.5 | 9 (11-28 10:12Z) |
| us-east-2 use2-az1 | 214 | 99% | 8.9 | 9 (11-28 10:12Z) |
| us-east-2 use2-az2 | 227 | 99% | 8.9 | 9 (11-28 08:17Z) |
| us-east-2 use2-az3 | 254 | 97% | 8.8 | 9 (11-28 10:12Z) |
| us-west-2 usw2-az1 | 117 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 112 | 92% | 8.4 | 9 (11-28 10:12Z) |
| us-west-2 usw2-az3 | 162 | 89% | 8.2 | 9 (11-28 05:14Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T10:12:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T10:12:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731800 | 2026-11-28T10:12:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.620000 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.629600 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.614800 | 2026-11-28T10:12:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T10:12:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.739300 | 2026-11-28T10:12:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-11-28T10:12:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.685400 | 2026-11-28T10:12:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.395500 | 2026-11-28T10:12:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.705400 | 2026-11-28T10:12:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499600 | 2026-11-28T10:12:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.581900 | 2026-11-28T10:12:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519000 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.791200 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.920700 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1b | Windows | 0.344500 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.882800 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1c | Windows | 0.286700 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.874800 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.876900 | 2026-11-28T10:12:54Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545100 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552400 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T10:12:54Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.641400 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2a | Windows | 0.290000 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.908100 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547500 | 2026-11-28T10:12:54Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T10:12:54Z |
