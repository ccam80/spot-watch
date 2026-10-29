# Spot placement score log

Generated 2026-10-29 18:20 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 432 | 47% | 5.1 | 4 (10-29 18:20Z) |
| ap-northeast-1 | 432 | 15% | 2.7 | 1 (10-29 18:20Z) |
| ap-northeast-2 | 432 | 64% | 6.8 | 9 (10-29 18:20Z) |
| ap-south-1 | 432 | 3% | 1.7 | 1 (10-29 18:20Z) |
| ap-southeast-2 | 432 | 0% | 1.0 | 1 (10-29 18:20Z) |
| ap-southeast-3 | 432 | 26% | 3.4 | 2 (10-29 18:20Z) |
| us-east-1 | 432 | 11% | 2.7 | 2 (10-29 18:20Z) |
| us-east-2 | 432 | 31% | 3.7 | 1 (10-29 18:20Z) |
| us-west-2 | 432 | 10% | 2.2 | 1 (10-29 18:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999911111199999999999999111111199999711111122144
ap-northeast-1   222221111111111121112122223222111111111122221111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   885411111111111115688863112111111111111111112332
us-east-1        223331112211122333331111111111111222233333233332
us-east-2        199991119111999911111111111111111111411111111111
us-west-2        111111111112111122222222222222112222221111211111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 3 | 4 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 142 | 6% | 1.6 | 1 (10-29 17:15Z) |
| ap-east-1 ape1-az2 | 316 | 64% | 6.5 | 4 (10-29 18:20Z) |
| ap-northeast-1 apne1-az1 | 84 | 5% | 1.5 | 1 (10-29 18:20Z) |
| ap-northeast-1 apne1-az4 | 196 | 27% | 3.6 | 1 (10-29 17:15Z) |
| ap-northeast-2 apne2-az1 | 374 | 57% | 6.2 | 9 (10-29 18:20Z) |
| ap-northeast-2 apne2-az3 | 401 | 64% | 6.7 | 9 (10-29 18:20Z) |
| ap-northeast-2 apne2-az4 | 428 | 64% | 6.8 | 9 (10-29 18:20Z) |
| ap-south-1 aps1-az1 | 119 | 1% | 1.4 | 1 (10-29 18:20Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 75 | 3% | 1.3 | 1 (10-29 16:18Z) |
| ap-southeast-2 apse2-az2 | 45 | 0% | 1.0 | 1 (10-29 08:21Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 283 | 39% | 4.5 | 2 (10-29 18:20Z) |
| us-east-1 use1-az1 | 82 | 0% | 1.1 | 1 (10-29 16:18Z) |
| us-east-1 use1-az2 | 115 | 3% | 1.4 | 1 (10-29 13:17Z) |
| us-east-1 use1-az4 | 139 | 26% | 3.2 | 1 (10-29 18:20Z) |
| us-east-1 use1-az5 | 139 | 27% | 3.4 | 1 (10-29 13:17Z) |
| us-east-1 use1-az6 | 104 | 26% | 3.2 | 1 (10-29 17:15Z) |
| us-east-2 use2-az1 | 179 | 44% | 4.7 | 1 (10-29 18:20Z) |
| us-east-2 use2-az2 | 228 | 50% | 5.2 | 1 (10-29 17:15Z) |
| us-east-2 use2-az3 | 258 | 47% | 5.1 | 1 (10-29 13:17Z) |
| us-west-2 usw2-az1 | 139 | 26% | 3.4 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az2 | 101 | 20% | 2.8 | 1 (10-29 16:18Z) |
| us-west-2 usw2-az3 | 172 | 18% | 2.8 | 1 (10-29 18:20Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 432 | 65% | 6.9 | 9 (10-29 18:20Z) |
| ap-northeast-1 | 432 | 72% | 7.0 | 9 (10-29 18:20Z) |
| ap-northeast-2 | 432 | 100% | 9.0 | 9 (10-29 18:20Z) |
| ap-south-1 | 432 | 61% | 6.3 | 9 (10-29 18:20Z) |
| ap-southeast-2 | 432 | 22% | 3.3 | 9 (10-29 18:20Z) |
| ap-southeast-3 | 432 | 26% | 3.4 | 2 (10-29 18:20Z) |
| us-east-1 | 432 | 70% | 6.4 | 5 (10-29 18:20Z) |
| us-east-2 | 432 | 69% | 6.8 | 2 (10-29 18:20Z) |
| us-west-2 | 432 | 51% | 5.6 | 4 (10-29 18:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999992211111122279999999999993111111111199999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999911111111111112999999999711111111111129
ap-southeast-2   911111111111119999999999911111111111114399999999
ap-southeast-3   885411111111111115688863112111111111111111112332
us-east-1        457669969654459654352221112224446666577995656555
us-east-2        999999999999999999912222222222252222992229912222
us-west-2        333343333335594399459554444444335599955449999334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 6 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 273 | 80% | 7.8 | 9 (10-29 17:15Z) |
| ap-east-1 ape1-az2 | 234 | 82% | 7.9 | 9 (10-29 18:20Z) |
| ap-east-1 ape1-az3 | 254 | 83% | 8.0 | 9 (10-29 18:20Z) |
| ap-northeast-1 apne1-az1 | 185 | 94% | 8.6 | 9 (10-29 18:20Z) |
| ap-northeast-1 apne1-az2 | 145 | 81% | 7.9 | 9 (10-29 18:20Z) |
| ap-northeast-1 apne1-az4 | 232 | 99% | 8.9 | 9 (10-29 17:15Z) |
| ap-northeast-2 apne2-az1 | 350 | 100% | 9.0 | 9 (10-29 18:20Z) |
| ap-northeast-2 apne2-az2 | 88 | 82% | 7.8 | 9 (10-29 18:20Z) |
| ap-northeast-2 apne2-az3 | 376 | 100% | 9.0 | 9 (10-29 18:20Z) |
| ap-northeast-2 apne2-az4 | 277 | 83% | 8.0 | 9 (10-29 18:20Z) |
| ap-south-1 aps1-az1 | 146 | 85% | 8.1 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az2 | 158 | 77% | 7.5 | 2 (10-29 04:19Z) |
| ap-south-1 aps1-az3 | 170 | 88% | 8.3 | 3 (10-29 04:19Z) |
| ap-southeast-2 apse2-az1 | 51 | 80% | 7.8 | 9 (10-29 18:20Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 120 | 91% | 8.4 | 2 (10-29 10:16Z) |
| us-east-1 use1-az5 | 88 | 98% | 8.8 | 9 (10-29 11:15Z) |
| us-east-1 use1-az6 | 108 | 92% | 8.4 | 7 (10-29 11:15Z) |
| us-east-2 use2-az1 | 152 | 99% | 8.9 | 9 (10-29 12:24Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 198 | 96% | 8.7 | 9 (10-29 13:17Z) |
| us-west-2 usw2-az1 | 88 | 98% | 8.8 | 9 (10-29 14:17Z) |
| us-west-2 usw2-az2 | 81 | 93% | 8.5 | 2 (10-29 06:26Z) |
| us-west-2 usw2-az3 | 113 | 89% | 8.3 | 9 (10-29 15:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702000 | 2026-10-29T18:20:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T18:20:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.761200 | 2026-10-29T18:20:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956300 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585200 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.588500 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570700 | 2026-10-29T18:20:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-29T18:20:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.589400 | 2026-10-29T18:20:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.461900 | 2026-10-29T18:20:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.589800 | 2026-10-29T18:20:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.393800 | 2026-10-29T18:20:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652900 | 2026-10-29T18:20:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522300 | 2026-10-29T18:20:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-29T18:20:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559200 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.573800 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.517100 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.527300 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.518000 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.567700 | 2026-10-29T18:20:12Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559900 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548100 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2b | Windows | 0.637500 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547300 | 2026-10-29T18:20:12Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.562000 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2a | Windows | 0.318000 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2b | Windows | 0.325300 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.560100 | 2026-10-29T18:20:12Z |
| us-west-2 | us-west-2c | Windows | 0.317700 | 2026-10-29T18:20:12Z |
