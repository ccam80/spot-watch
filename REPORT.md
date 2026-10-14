# Spot placement score log

Generated 2026-10-14 01:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 308 | 34% | 4.3 | 9 (10-14 01:49Z) |
| ap-northeast-1 | 308 | 15% | 2.8 | 1 (10-14 01:49Z) |
| ap-northeast-2 | 308 | 49% | 5.9 | 9 (10-14 01:49Z) |
| ap-south-1 | 308 | 2% | 1.8 | 1 (10-14 01:49Z) |
| ap-southeast-2 | 308 | 0% | 1.0 | 1 (10-14 01:49Z) |
| ap-southeast-3 | 308 | 22% | 3.3 | 1 (10-14 01:49Z) |
| us-east-1 | 308 | 9% | 2.5 | 3 (10-14 01:49Z) |
| us-east-2 | 308 | 27% | 3.6 | 9 (10-14 01:49Z) |
| us-west-2 | 308 | 12% | 2.4 | 1 (10-14 01:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911999981211111111111111111111118229299999999999
ap-northeast-1   999999999991191111511971111119111222211922121211
ap-northeast-2   999999999999149999999999999999919999999999999999
ap-south-1       111111111222222222222221112211111122222222221111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111111111113881111138911999793951511221
us-east-1        233119919999921111211112221132323331922332221133
us-east-2        119999999999911181111111111111111811999999111129
us-west-2        299999999199112112121111111111119999111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 5 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 107 | 8% | 1.8 | 5 (10-13 17:32Z) |
| ap-east-1 ape1-az2 | 213 | 49% | 5.6 | 9 (10-14 01:49Z) |
| ap-northeast-1 apne1-az1 | 52 | 8% | 1.8 | 1 (10-13 17:32Z) |
| ap-northeast-1 apne1-az4 | 147 | 26% | 3.6 | 1 (10-14 01:49Z) |
| ap-northeast-2 apne2-az1 | 268 | 47% | 5.7 | 9 (10-14 01:49Z) |
| ap-northeast-2 apne2-az3 | 280 | 50% | 5.9 | 9 (10-14 01:49Z) |
| ap-northeast-2 apne2-az4 | 305 | 50% | 6.0 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az1 | 80 | 1% | 1.6 | 1 (10-13 09:19Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 48 | 0% | 1.1 | 1 (10-13 01:16Z) |
| ap-southeast-2 apse2-az2 | 32 | 0% | 1.0 | 1 (10-13 01:16Z) |
| ap-southeast-3 apse3-az1 | 58 | 0% | 1.0 | 1 (10-12 18:57Z) |
| ap-southeast-3 apse3-az3 | 209 | 31% | 4.2 | 2 (10-13 22:38Z) |
| us-east-1 use1-az1 | 60 | 0% | 1.1 | 1 (10-13 17:32Z) |
| us-east-1 use1-az2 | 81 | 4% | 1.6 | 1 (10-13 22:38Z) |
| us-east-1 use1-az4 | 97 | 27% | 3.4 | 1 (10-13 17:32Z) |
| us-east-1 use1-az5 | 97 | 25% | 3.2 | 1 (10-14 01:49Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 125 | 38% | 4.4 | 8 (10-14 01:49Z) |
| us-east-2 use2-az2 | 156 | 45% | 5.0 | 9 (10-14 01:49Z) |
| us-east-2 use2-az3 | 186 | 42% | 4.9 | 9 (10-14 01:49Z) |
| us-west-2 usw2-az1 | 105 | 30% | 3.8 | 1 (10-14 01:49Z) |
| us-west-2 usw2-az2 | 66 | 26% | 3.4 | 1 (10-13 17:32Z) |
| us-west-2 usw2-az3 | 126 | 22% | 3.3 | 1 (10-13 09:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 308 | 50% | 6.0 | 9 (10-14 01:49Z) |
| ap-northeast-1 | 308 | 73% | 7.2 | 2 (10-14 01:49Z) |
| ap-northeast-2 | 308 | 100% | 9.0 | 9 (10-14 01:49Z) |
| ap-south-1 | 308 | 61% | 6.4 | 9 (10-14 01:49Z) |
| ap-southeast-2 | 308 | 17% | 3.2 | 1 (10-14 01:49Z) |
| ap-southeast-3 | 308 | 22% | 3.3 | 1 (10-14 01:49Z) |
| us-east-1 | 308 | 71% | 6.6 | 6 (10-14 01:49Z) |
| us-east-2 | 308 | 72% | 7.0 | 9 (10-14 01:49Z) |
| us-west-2 | 308 | 52% | 5.7 | 4 (10-14 01:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999199239913991199119999999999999923992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999229929992999199914999999999992991999
ap-southeast-2   222222929992291111111911111111891999999111111111
ap-southeast-3   111111111111111111113881111138911999793951511221
us-east-1        576349999999955453343336635464569982999999454266
us-east-2        399999999999923993321212111212119922999999119129
us-west-2        599999999999943235441323331332339999993592994424
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 6 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 8 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 183 | 70% | 7.2 | 9 (10-14 01:49Z) |
| ap-east-1 ape1-az2 | 153 | 73% | 7.4 | 9 (10-14 01:49Z) |
| ap-east-1 ape1-az3 | 153 | 71% | 7.3 | 9 (10-14 01:49Z) |
| ap-northeast-1 apne1-az1 | 145 | 92% | 8.5 | 9 (10-13 22:38Z) |
| ap-northeast-1 apne1-az2 | 83 | 69% | 7.1 | 9 (10-13 22:38Z) |
| ap-northeast-1 apne1-az4 | 175 | 98% | 8.9 | 9 (10-13 22:38Z) |
| ap-northeast-2 apne2-az1 | 242 | 100% | 9.0 | 9 (10-13 22:38Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 263 | 100% | 9.0 | 9 (10-14 01:49Z) |
| ap-northeast-2 apne2-az4 | 177 | 73% | 7.4 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az1 | 109 | 80% | 7.8 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az2 | 109 | 67% | 7.0 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az3 | 126 | 86% | 8.2 | 9 (10-14 01:49Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 19 | 63% | 6.3 | 2 (10-13 09:19Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 105 | 98% | 8.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az2 | 150 | 99% | 8.9 | 9 (10-14 01:49Z) |
| us-east-2 use2-az3 | 139 | 94% | 8.6 | 9 (10-14 01:49Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.716900 | 2026-10-14T01:49:17Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-14T01:49:17Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.754700 | 2026-10-14T01:49:17Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938400 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591300 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586800 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.576200 | 2026-10-14T01:49:17Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742000 | 2026-10-14T01:49:17Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.547100 | 2026-10-14T01:49:17Z |
| ap-south-1 | ap-south-1a | Windows | 0.386800 | 2026-10-14T01:49:17Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.701900 | 2026-10-14T01:49:17Z |
| ap-south-1 | ap-south-1b | Windows | 0.336100 | 2026-10-14T01:49:17Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.724100 | 2026-10-14T01:49:17Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.519400 | 2026-10-14T01:49:17Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.494300 | 2026-10-14T01:49:17Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.622700 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.489900 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.490100 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.491400 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.425300 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.476200 | 2026-10-14T01:49:17Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.541400 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2a | Windows | 0.643900 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531800 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.525600 | 2026-10-14T01:49:17Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.538800 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2a | Windows | 0.317200 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499500 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2b | Windows | 0.333300 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.505700 | 2026-10-14T01:49:17Z |
| us-west-2 | us-west-2c | Windows | 0.317300 | 2026-10-14T01:49:17Z |
