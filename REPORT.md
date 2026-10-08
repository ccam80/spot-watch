# Spot placement score log

Generated 2026-10-08 22:01 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 287 | 32% | 4.1 | 1 (10-08 22:00Z) |
| ap-northeast-1 | 287 | 16% | 2.8 | 1 (10-08 22:00Z) |
| ap-northeast-2 | 287 | 46% | 5.7 | 9 (10-08 22:00Z) |
| ap-south-1 | 287 | 2% | 1.8 | 2 (10-08 22:00Z) |
| ap-southeast-2 | 287 | 0% | 1.0 | 1 (10-08 22:00Z) |
| ap-southeast-3 | 287 | 20% | 3.2 | 1 (10-08 22:00Z) |
| us-east-1 | 287 | 10% | 2.5 | 1 (10-08 22:00Z) |
| us-east-2 | 287 | 26% | 3.5 | 1 (10-08 22:00Z) |
| us-west-2 | 287 | 11% | 2.4 | 1 (10-08 22:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        998999991111119939911911999981211111111111111111
ap-northeast-1   111899127998121298219999999999991191111511971111
ap-northeast-2   999999999999999999999999999999999149999999999999
ap-south-1       111111111111111111211111111111222222222222221112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111476516111111999114111111111111111111113881111
us-east-1        222222232222211922922233119919999921111211112221
us-east-2        911111817121899999999119999999999911181111111111
us-west-2        222222222212111222121299999999199112112121111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 6 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 6 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 95 | 0% | 1.4 | 1 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 200 | 46% | 5.4 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 47 | 9% | 1.8 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 139 | 26% | 3.6 | 1 (10-08 08:51Z) |
| ap-northeast-2 apne2-az1 | 249 | 43% | 5.4 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 261 | 47% | 5.8 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az4 | 284 | 46% | 5.8 | 9 (10-08 22:00Z) |
| ap-south-1 aps1-az1 | 73 | 1% | 1.6 | 1 (10-06 10:07Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 44 | 0% | 1.1 | 1 (10-08 22:00Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 56 | 0% | 1.0 | 1 (10-08 08:51Z) |
| ap-southeast-3 apse3-az3 | 195 | 28% | 4.0 | 1 (10-08 22:00Z) |
| us-east-1 use1-az1 | 46 | 0% | 1.1 | 1 (10-08 22:00Z) |
| us-east-1 use1-az2 | 78 | 4% | 1.6 | 1 (10-07 21:56Z) |
| us-east-1 use1-az4 | 89 | 28% | 3.5 | 1 (10-08 22:00Z) |
| us-east-1 use1-az5 | 92 | 25% | 3.3 | 1 (10-08 16:24Z) |
| us-east-1 use1-az6 | 72 | 21% | 2.9 | 1 (10-08 08:51Z) |
| us-east-2 use2-az1 | 113 | 38% | 4.4 | 2 (10-06 10:07Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 174 | 41% | 4.8 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az1 | 99 | 28% | 3.7 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az2 | 58 | 24% | 3.4 | 1 (10-08 22:00Z) |
| us-west-2 usw2-az3 | 120 | 21% | 3.2 | 1 (10-08 08:51Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 287 | 47% | 5.8 | 9 (10-08 22:00Z) |
| ap-northeast-1 | 287 | 73% | 7.1 | 9 (10-08 22:00Z) |
| ap-northeast-2 | 287 | 100% | 9.0 | 9 (10-08 22:00Z) |
| ap-south-1 | 287 | 60% | 6.3 | 9 (10-08 22:00Z) |
| ap-southeast-2 | 287 | 16% | 3.1 | 1 (10-08 22:00Z) |
| ap-southeast-3 | 287 | 20% | 3.2 | 1 (10-08 22:00Z) |
| us-east-1 | 287 | 71% | 6.6 | 5 (10-08 22:00Z) |
| us-east-2 | 287 | 74% | 7.2 | 1 (10-08 22:00Z) |
| us-west-2 | 287 | 53% | 5.7 | 1 (10-08 22:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   799999999999922499229999999999999199239913991199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111199299999299999999999999999229929992999199
ap-southeast-2   222222222222222222222222222929992291111111911111
ap-southeast-3   111476516111111999114111111111111111111113881111
us-east-1        444333443334455944985576349999999955453343336635
us-east-2        983292998359999999999399999999999923993321212111
us-west-2        545544444544433934499599999999999943235441323331
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 5 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 170 | 68% | 7.1 | 9 (10-08 22:00Z) |
| ap-east-1 ape1-az2 | 140 | 71% | 7.2 | 9 (10-08 22:00Z) |
| ap-east-1 ape1-az3 | 136 | 68% | 7.1 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 136 | 92% | 8.5 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az2 | 71 | 63% | 6.8 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 164 | 99% | 8.9 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az1 | 223 | 100% | 9.0 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 247 | 100% | 9.0 | 9 (10-08 16:24Z) |
| ap-northeast-2 apne2-az4 | 161 | 71% | 7.2 | 9 (10-08 16:24Z) |
| ap-south-1 aps1-az1 | 97 | 77% | 7.6 | 9 (10-08 22:00Z) |
| ap-south-1 aps1-az2 | 103 | 65% | 6.9 | 9 (10-08 01:50Z) |
| ap-south-1 aps1-az3 | 114 | 84% | 8.1 | 9 (10-08 22:00Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 55 | 24% | 4.3 | 3 (10-07 08:33Z) |
| us-east-1 use1-az1 | 17 | 71% | 6.8 | 2 (10-08 08:51Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 97 | 96% | 8.7 | 2 (10-08 08:51Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 102 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707000 | 2026-10-08T22:00:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-08T22:00:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.759100 | 2026-10-08T22:00:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.942100 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.603600 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579700 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574300 | 2026-10-08T22:00:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743000 | 2026-10-08T22:00:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.629700 | 2026-10-08T22:00:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.381500 | 2026-10-08T22:00:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.688600 | 2026-10-08T22:00:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.353700 | 2026-10-08T22:00:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718200 | 2026-10-08T22:00:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503700 | 2026-10-08T22:00:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.446200 | 2026-10-08T22:00:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.569400 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.489800 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.481000 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.411400 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.491800 | 2026-10-08T22:00:54Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534400 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529200 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517200 | 2026-10-08T22:00:54Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.529700 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2a | Windows | 0.323500 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491800 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2b | Windows | 0.325500 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.496900 | 2026-10-08T22:00:54Z |
| us-west-2 | us-west-2c | Windows | 0.323500 | 2026-10-08T22:00:54Z |
