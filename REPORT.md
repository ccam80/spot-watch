# Spot placement score log

Generated 2026-10-11 18:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 299 | 32% | 4.1 | 9 (10-11 18:00Z) |
| ap-northeast-1 | 299 | 15% | 2.8 | 1 (10-11 18:00Z) |
| ap-northeast-2 | 299 | 48% | 5.8 | 9 (10-11 18:00Z) |
| ap-south-1 | 299 | 2% | 1.8 | 2 (10-11 18:00Z) |
| ap-southeast-2 | 299 | 0% | 1.0 | 1 (10-11 18:00Z) |
| ap-southeast-3 | 299 | 21% | 3.3 | 3 (10-11 18:00Z) |
| us-east-1 | 299 | 10% | 2.6 | 2 (10-11 18:00Z) |
| us-east-2 | 299 | 27% | 3.5 | 9 (10-11 18:00Z) |
| us-west-2 | 299 | 12% | 2.4 | 1 (10-11 18:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119939911911999981211111111111111111111118229299
ap-northeast-1   121298219999999999991191111511971111119111222211
ap-northeast-2   999999999999999999999149999999999999999919999999
ap-south-1       111111211111111111222222222222221112211111122222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111999114111111111111111111113881111138911999793
us-east-1        211922922233119919999921111211112221132323331922
us-east-2        899999999119999999999911181111111111111111811999
us-west-2        111222121299999999199112112121111111111119999111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 100 | 3% | 1.6 | 7 (10-11 18:00Z) |
| ap-east-1 ape1-az2 | 204 | 47% | 5.4 | 9 (10-11 18:00Z) |
| ap-northeast-1 apne1-az1 | 50 | 8% | 1.8 | 1 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 143 | 26% | 3.6 | 1 (10-11 12:40Z) |
| ap-northeast-2 apne2-az1 | 259 | 45% | 5.6 | 9 (10-11 18:00Z) |
| ap-northeast-2 apne2-az3 | 271 | 49% | 5.8 | 9 (10-11 18:00Z) |
| ap-northeast-2 apne2-az4 | 296 | 48% | 5.9 | 9 (10-11 18:00Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 30 | 0% | 1.0 | 1 (10-10 08:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 204 | 30% | 4.2 | 3 (10-11 18:00Z) |
| us-east-1 use1-az1 | 56 | 0% | 1.1 | 1 (10-11 18:00Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 94 | 28% | 3.5 | 9 (10-11 05:37Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 120 | 38% | 4.3 | 9 (10-11 18:00Z) |
| us-east-2 use2-az2 | 153 | 44% | 4.9 | 6 (10-11 18:00Z) |
| us-east-2 use2-az3 | 181 | 41% | 4.8 | 9 (10-11 18:00Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 64 | 27% | 3.5 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 299 | 49% | 5.9 | 9 (10-11 18:00Z) |
| ap-northeast-1 | 299 | 74% | 7.2 | 9 (10-11 18:00Z) |
| ap-northeast-2 | 299 | 100% | 9.0 | 9 (10-11 18:00Z) |
| ap-south-1 | 299 | 61% | 6.4 | 9 (10-11 18:00Z) |
| ap-southeast-2 | 299 | 18% | 3.2 | 9 (10-11 18:00Z) |
| ap-southeast-3 | 299 | 21% | 3.3 | 3 (10-11 18:00Z) |
| us-east-1 | 299 | 71% | 6.6 | 9 (10-11 18:00Z) |
| us-east-2 | 299 | 72% | 7.1 | 9 (10-11 18:00Z) |
| us-west-2 | 299 | 53% | 5.7 | 3 (10-11 18:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   922499229999999999999199239913991199119999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999299999999999999999229929992999199914999999999
ap-southeast-2   222222222222222929992291111111911111111891999999
ap-southeast-3   111999114111111111111111111113881111138911999793
us-east-1        455944985576349999999955453343336635464569982999
us-east-2        999999999399999999999923993321212111212119922999
us-west-2        433934499599999999999943235441323331332339999993
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 177 | 69% | 7.2 | 9 (10-11 18:00Z) |
| ap-east-1 ape1-az2 | 147 | 72% | 7.3 | 9 (10-11 18:00Z) |
| ap-east-1 ape1-az3 | 145 | 70% | 7.2 | 9 (10-11 05:37Z) |
| ap-northeast-1 apne1-az1 | 141 | 92% | 8.5 | 9 (10-11 12:40Z) |
| ap-northeast-1 apne1-az2 | 77 | 66% | 7.0 | 9 (10-11 18:00Z) |
| ap-northeast-1 apne1-az4 | 169 | 99% | 8.9 | 9 (10-11 18:00Z) |
| ap-northeast-2 apne2-az1 | 234 | 100% | 9.0 | 9 (10-11 18:00Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 255 | 100% | 9.0 | 9 (10-11 18:00Z) |
| ap-northeast-2 apne2-az4 | 169 | 72% | 7.3 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az1 | 104 | 79% | 7.7 | 9 (10-11 12:40Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 121 | 85% | 8.1 | 9 (10-11 18:00Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 60 | 28% | 4.6 | 9 (10-11 12:40Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 100 | 95% | 8.7 | 9 (10-11 12:40Z) |
| us-east-1 use1-az5 | 61 | 97% | 8.8 | 9 (10-11 18:00Z) |
| us-east-1 use1-az6 | 82 | 95% | 8.7 | 9 (10-11 18:00Z) |
| us-east-2 use2-az1 | 104 | 98% | 8.9 | 9 (10-11 18:00Z) |
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 134 | 94% | 8.6 | 9 (10-11 12:40Z) |
| us-west-2 usw2-az1 | 73 | 97% | 8.8 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 86 | 95% | 8.7 | 9 (10-11 12:40Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712300 | 2026-10-11T18:00:42Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-11T18:00:42Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.768000 | 2026-10-11T18:00:42Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.951000 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.600100 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586800 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578500 | 2026-10-11T18:00:42Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742300 | 2026-10-11T18:00:42Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.570300 | 2026-10-11T18:00:42Z |
| ap-south-1 | ap-south-1a | Windows | 0.366100 | 2026-10-11T18:00:42Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.661700 | 2026-10-11T18:00:42Z |
| ap-south-1 | ap-south-1b | Windows | 0.350200 | 2026-10-11T18:00:42Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.722100 | 2026-10-11T18:00:42Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507000 | 2026-10-11T18:00:42Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.416300 | 2026-10-11T18:00:42Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.525900 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.480300 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.457800 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.394900 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.453000 | 2026-10-11T18:00:42Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.536000 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2a | Windows | 0.640000 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529300 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2b | Windows | 0.640100 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.518100 | 2026-10-11T18:00:42Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.522700 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2a | Windows | 0.320300 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.489100 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2b | Windows | 0.321100 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.497100 | 2026-10-11T18:00:42Z |
| us-west-2 | us-west-2c | Windows | 0.319700 | 2026-10-11T18:00:42Z |
