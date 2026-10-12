# Spot placement score log

Generated 2026-10-12 09:04 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 302 | 33% | 4.2 | 9 (10-12 09:04Z) |
| ap-northeast-1 | 302 | 16% | 2.8 | 2 (10-12 09:04Z) |
| ap-northeast-2 | 302 | 48% | 5.9 | 9 (10-12 09:04Z) |
| ap-south-1 | 302 | 2% | 1.8 | 2 (10-12 09:04Z) |
| ap-southeast-2 | 302 | 0% | 1.0 | 1 (10-12 09:04Z) |
| ap-southeast-3 | 302 | 22% | 3.3 | 1 (10-12 09:04Z) |
| us-east-1 | 302 | 10% | 2.6 | 2 (10-12 09:04Z) |
| us-east-2 | 302 | 27% | 3.6 | 9 (10-12 09:04Z) |
| us-west-2 | 302 | 12% | 2.4 | 1 (10-12 09:04Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        939911911999981211111111111111111111118229299999
ap-northeast-1   298219999999999991191111511971111119111222211922
ap-northeast-2   999999999999999999149999999999999999919999999999
ap-south-1       111211111111111222222222222221112211111122222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   999114111111111111111111113881111138911999793951
us-east-1        922922233119919999921111211112221132323331922332
us-east-2        999999119999999999911181111111111111111811999999
us-west-2        222121299999999199112112121111111111119999111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 5 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 103 | 6% | 1.7 | 5 (10-12 09:04Z) |
| ap-east-1 ape1-az2 | 207 | 48% | 5.5 | 9 (10-12 09:04Z) |
| ap-northeast-1 apne1-az1 | 51 | 8% | 1.8 | 1 (10-12 09:04Z) |
| ap-northeast-1 apne1-az4 | 145 | 26% | 3.6 | 1 (10-12 01:14Z) |
| ap-northeast-2 apne2-az1 | 262 | 45% | 5.6 | 9 (10-12 09:04Z) |
| ap-northeast-2 apne2-az3 | 274 | 49% | 5.9 | 9 (10-12 09:04Z) |
| ap-northeast-2 apne2-az4 | 299 | 49% | 5.9 | 9 (10-12 09:04Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 31 | 0% | 1.0 | 1 (10-12 09:04Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 206 | 31% | 4.2 | 5 (10-12 01:14Z) |
| us-east-1 use1-az1 | 57 | 0% | 1.1 | 1 (10-12 09:04Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 95 | 27% | 3.4 | 1 (10-12 09:04Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 122 | 39% | 4.4 | 9 (10-12 01:14Z) |
| us-east-2 use2-az2 | 155 | 45% | 4.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az3 | 184 | 42% | 4.9 | 9 (10-12 09:04Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 64 | 27% | 3.5 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 302 | 49% | 6.0 | 9 (10-12 09:04Z) |
| ap-northeast-1 | 302 | 74% | 7.2 | 9 (10-12 09:04Z) |
| ap-northeast-2 | 302 | 100% | 9.0 | 9 (10-12 09:04Z) |
| ap-south-1 | 302 | 61% | 6.4 | 2 (10-12 09:04Z) |
| ap-southeast-2 | 302 | 18% | 3.2 | 1 (10-12 09:04Z) |
| ap-southeast-3 | 302 | 22% | 3.3 | 1 (10-12 09:04Z) |
| us-east-1 | 302 | 71% | 6.6 | 9 (10-12 09:04Z) |
| us-east-2 | 302 | 73% | 7.1 | 9 (10-12 09:04Z) |
| us-west-2 | 302 | 53% | 5.7 | 2 (10-12 09:04Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   499229999999999999199239913991199119999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299999999999999999229929992999199914999999999992
ap-southeast-2   222222222222929992291111111911111111891999999111
ap-southeast-3   999114111111111111111111113881111138911999793951
us-east-1        944985576349999999955453343336635464569982999999
us-east-2        999999399999999999923993321212111212119922999999
us-west-2        934499599999999999943235441323331332339999993592
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 178 | 70% | 7.2 | 9 (10-12 09:04Z) |
| ap-east-1 ape1-az2 | 148 | 72% | 7.3 | 9 (10-12 09:04Z) |
| ap-east-1 ape1-az3 | 148 | 70% | 7.2 | 9 (10-12 09:04Z) |
| ap-northeast-1 apne1-az1 | 143 | 92% | 8.5 | 9 (10-12 09:04Z) |
| ap-northeast-1 apne1-az2 | 80 | 68% | 7.0 | 9 (10-12 09:04Z) |
| ap-northeast-1 apne1-az4 | 171 | 99% | 8.9 | 9 (10-12 09:04Z) |
| ap-northeast-2 apne2-az1 | 237 | 100% | 9.0 | 9 (10-12 09:04Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 257 | 100% | 9.0 | 9 (10-12 09:04Z) |
| ap-northeast-2 apne2-az4 | 171 | 73% | 7.4 | 9 (10-12 09:04Z) |
| ap-south-1 aps1-az1 | 105 | 79% | 7.7 | 9 (10-11 21:50Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 123 | 85% | 8.1 | 9 (10-12 01:14Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 105 | 98% | 8.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 137 | 94% | 8.6 | 9 (10-12 09:04Z) |
| us-west-2 usw2-az1 | 73 | 97% | 8.8 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 86 | 95% | 8.7 | 9 (10-11 12:40Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.716300 | 2026-10-12T09:04:42Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-12T09:04:42Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.774200 | 2026-10-12T09:04:42Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.957100 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596100 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.587800 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579200 | 2026-10-12T09:04:42Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742300 | 2026-10-12T09:04:42Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.554200 | 2026-10-12T09:04:42Z |
| ap-south-1 | ap-south-1a | Windows | 0.361000 | 2026-10-12T09:04:42Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.671700 | 2026-10-12T09:04:42Z |
| ap-south-1 | ap-south-1b | Windows | 0.347800 | 2026-10-12T09:04:42Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.723600 | 2026-10-12T09:04:42Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.518400 | 2026-10-12T09:04:42Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.442600 | 2026-10-12T09:04:42Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.585400 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.523900 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.484100 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.463300 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.400900 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.461300 | 2026-10-12T09:04:42Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.536200 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529900 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.520900 | 2026-10-12T09:04:42Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.533600 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2a | Windows | 0.319500 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.494700 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2b | Windows | 0.323000 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.499800 | 2026-10-12T09:04:42Z |
| us-west-2 | us-west-2c | Windows | 0.319100 | 2026-10-12T09:04:42Z |
