# Spot placement score log

Generated 2026-10-10 23:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 296 | 32% | 4.1 | 9 (10-10 23:28Z) |
| ap-northeast-1 | 296 | 16% | 2.8 | 2 (10-10 23:28Z) |
| ap-northeast-2 | 296 | 47% | 5.8 | 9 (10-10 23:28Z) |
| ap-south-1 | 296 | 2% | 1.8 | 2 (10-10 23:28Z) |
| ap-southeast-2 | 296 | 0% | 1.0 | 1 (10-10 23:28Z) |
| ap-southeast-3 | 296 | 21% | 3.3 | 9 (10-10 23:28Z) |
| us-east-1 | 296 | 9% | 2.5 | 1 (10-10 23:28Z) |
| us-east-2 | 296 | 26% | 3.5 | 1 (10-10 23:28Z) |
| us-west-2 | 296 | 12% | 2.4 | 9 (10-10 23:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111119939911911999981211111111111111111111118229
ap-northeast-1   998121298219999999999991191111511971111119111222
ap-northeast-2   999999999999999999999999149999999999999999919999
ap-south-1       111111111211111111111222222222222221112211111122
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111999114111111111111111111113881111138911999
us-east-1        222211922922233119919999921111211112221132323331
us-east-2        121899999999119999999999911181111111111111111811
us-west-2        212111222121299999999199112112121111111111119999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 4 | 2 | 3 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 98 | 1% | 1.5 | 7 (10-10 23:28Z) |
| ap-east-1 ape1-az2 | 202 | 47% | 5.4 | 9 (10-10 23:28Z) |
| ap-northeast-1 apne1-az1 | 50 | 8% | 1.8 | 1 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 142 | 26% | 3.6 | 1 (10-10 20:01Z) |
| ap-northeast-2 apne2-az1 | 256 | 44% | 5.5 | 9 (10-10 23:28Z) |
| ap-northeast-2 apne2-az3 | 268 | 48% | 5.8 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az4 | 293 | 48% | 5.8 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 30 | 0% | 1.0 | 1 (10-10 08:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 201 | 29% | 4.2 | 9 (10-10 23:28Z) |
| us-east-1 use1-az1 | 54 | 0% | 1.1 | 1 (10-10 23:28Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 93 | 27% | 3.4 | 1 (10-10 15:16Z) |
| us-east-1 use1-az5 | 94 | 24% | 3.2 | 1 (10-10 20:01Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 117 | 37% | 4.3 | 1 (10-10 01:42Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 178 | 40% | 4.8 | 1 (10-10 20:01Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 64 | 27% | 3.5 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 296 | 48% | 5.9 | 9 (10-10 23:28Z) |
| ap-northeast-1 | 296 | 73% | 7.1 | 9 (10-10 23:28Z) |
| ap-northeast-2 | 296 | 100% | 9.0 | 9 (10-10 23:28Z) |
| ap-south-1 | 296 | 60% | 6.3 | 9 (10-10 23:28Z) |
| ap-southeast-2 | 296 | 17% | 3.2 | 9 (10-10 23:28Z) |
| ap-southeast-3 | 296 | 21% | 3.3 | 9 (10-10 23:28Z) |
| us-east-1 | 296 | 71% | 6.6 | 2 (10-10 23:28Z) |
| us-east-2 | 296 | 72% | 7.0 | 2 (10-10 23:28Z) |
| us-west-2 | 296 | 52% | 5.7 | 9 (10-10 23:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999922499229999999999999199239913991199119999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299999299999999999999999229929992999199914999999
ap-southeast-2   222222222222222222929992291111111911111111891999
ap-southeast-3   111111999114111111111111111111113881111138911999
us-east-1        334455944985576349999999955453343336635464569982
us-east-2        359999999999399999999999923993321212111212119922
us-west-2        544433934499599999999999943235441323331332339999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 176 | 69% | 7.2 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az2 | 146 | 72% | 7.3 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az3 | 144 | 69% | 7.2 | 9 (10-10 23:28Z) |
| ap-northeast-1 apne1-az1 | 139 | 92% | 8.5 | 9 (10-10 20:01Z) |
| ap-northeast-1 apne1-az2 | 76 | 66% | 6.9 | 9 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 168 | 99% | 8.9 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az1 | 232 | 100% | 9.0 | 9 (10-10 23:28Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 254 | 100% | 9.0 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az4 | 169 | 72% | 7.3 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az1 | 102 | 78% | 7.7 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 119 | 85% | 8.1 | 9 (10-10 23:28Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 36 | 64% | 6.8 | 9 (10-10 23:28Z) |
| ap-southeast-3 apse3-az3 | 59 | 27% | 4.5 | 9 (10-10 23:28Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 99 | 95% | 8.6 | 9 (10-10 15:16Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 81 | 95% | 8.7 | 9 (10-10 08:24Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 148 | 99% | 8.9 | 9 (10-10 08:24Z) |
| us-east-2 use2-az3 | 132 | 94% | 8.6 | 9 (10-10 15:16Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 68 | 96% | 8.7 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 85 | 95% | 8.7 | 9 (10-10 23:28Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-10-10T23:28:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-10T23:28:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.769000 | 2026-10-10T23:28:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.953000 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596900 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.584900 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574900 | 2026-10-10T23:28:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742500 | 2026-10-10T23:28:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.598700 | 2026-10-10T23:28:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.370400 | 2026-10-10T23:28:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.677700 | 2026-10-10T23:28:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.350800 | 2026-10-10T23:28:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.720300 | 2026-10-10T23:28:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504700 | 2026-10-10T23:28:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.416300 | 2026-10-10T23:28:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574100 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.532600 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.481700 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.459300 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395300 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.464300 | 2026-10-10T23:28:37Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534900 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2a | Windows | 0.639900 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529900 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2b | Windows | 0.640100 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517700 | 2026-10-10T23:28:37Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.525200 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2a | Windows | 0.320700 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.486600 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2b | Windows | 0.322600 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.492600 | 2026-10-10T23:28:37Z |
| us-west-2 | us-west-2c | Windows | 0.320400 | 2026-10-10T23:28:37Z |
