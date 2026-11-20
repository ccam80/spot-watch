# Spot placement score log

Generated 2026-11-20 03:02 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 553 | 48% | 5.1 | 1 (11-20 03:02Z) |
| ap-northeast-1 | 553 | 17% | 2.8 | 1 (11-20 03:02Z) |
| ap-northeast-2 | 553 | 69% | 7.0 | 9 (11-20 03:02Z) |
| ap-south-1 | 553 | 3% | 1.7 | 1 (11-20 03:02Z) |
| ap-southeast-2 | 553 | 1% | 1.0 | 1 (11-20 03:02Z) |
| ap-southeast-3 | 553 | 23% | 3.1 | 1 (11-20 03:02Z) |
| us-east-1 | 553 | 12% | 2.7 | 6 (11-20 03:02Z) |
| us-east-2 | 553 | 31% | 3.7 | 1 (11-20 03:02Z) |
| us-west-2 | 553 | 9% | 2.1 | 2 (11-20 03:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199991999819919121911111111199199611391191111111
ap-northeast-1   119199919911211111511121129995999991191211221211
ap-northeast-2   999999999999999991911111111199999999799171691999
ap-south-1       122211311911112211111111111111191111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111113111111111311111111111211311131111111111
us-east-1        213222222329293322423233344223323737465467654656
us-east-2        111999919999111111111111111119919919991119918111
us-west-2        122922111211111212221112122111219111121121212112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 173 | 5% | 1.5 | 1 (11-18 21:51Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 133 | 11% | 2.0 | 1 (11-19 12:52Z) |
| ap-northeast-1 apne1-az4 | 258 | 27% | 3.5 | 1 (11-20 03:02Z) |
| ap-northeast-2 apne2-az1 | 464 | 63% | 6.6 | 8 (11-20 03:02Z) |
| ap-northeast-2 apne2-az3 | 507 | 69% | 7.0 | 9 (11-20 03:02Z) |
| ap-northeast-2 apne2-az4 | 537 | 71% | 7.2 | 9 (11-20 03:02Z) |
| ap-south-1 aps1-az1 | 160 | 1% | 1.3 | 1 (11-19 03:15Z) |
| ap-south-1 aps1-az3 | 162 | 7% | 2.3 | 1 (11-20 03:02Z) |
| ap-southeast-2 apse2-az1 | 113 | 3% | 1.2 | 1 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 81 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az1 | 99 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az3 | 332 | 36% | 4.2 | 1 (11-19 12:52Z) |
| us-east-1 use1-az1 | 120 | 0% | 1.1 | 1 (11-19 12:52Z) |
| us-east-1 use1-az2 | 144 | 3% | 1.4 | 1 (11-18 21:51Z) |
| us-east-1 use1-az4 | 183 | 21% | 2.8 | 2 (11-20 03:02Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 139 | 22% | 2.9 | 2 (11-20 03:02Z) |
| us-east-2 use2-az1 | 242 | 43% | 4.6 | 1 (11-19 03:15Z) |
| us-east-2 use2-az2 | 283 | 51% | 5.3 | 9 (11-19 12:52Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 177 | 21% | 2.9 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az2 | 129 | 16% | 2.5 | 1 (11-19 12:52Z) |
| us-west-2 usw2-az3 | 208 | 16% | 2.6 | 1 (11-19 03:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 553 | 72% | 7.3 | 9 (11-20 03:02Z) |
| ap-northeast-1 | 553 | 72% | 7.0 | 1 (11-20 03:02Z) |
| ap-northeast-2 | 553 | 100% | 9.0 | 9 (11-20 03:02Z) |
| ap-south-1 | 553 | 58% | 6.0 | 1 (11-20 03:02Z) |
| ap-southeast-2 | 553 | 27% | 3.6 | 1 (11-20 03:02Z) |
| ap-southeast-3 | 553 | 23% | 3.1 | 1 (11-20 03:02Z) |
| us-east-1 | 553 | 73% | 6.6 | 8 (11-20 03:02Z) |
| us-east-2 | 553 | 68% | 6.7 | 9 (11-20 03:02Z) |
| us-west-2 | 553 | 51% | 5.6 | 4 (11-20 03:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999993922992992894299999999992292991993991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       199217911991392291111119111111991111111111111111
ap-southeast-2   999999919911911911991991191329999911181911911991
ap-southeast-3   111111113111111111311111111111211311131111111111
us-east-1        579999999999599669968966978999997999998889888888
us-east-2        119999999999119919919999999999999919999589929919
us-west-2        195955999999494334933434194239939991159954535324
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 6 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 357 | 85% | 8.1 | 9 (11-20 03:02Z) |
| ap-east-1 ape1-az2 | 326 | 87% | 8.2 | 9 (11-20 03:02Z) |
| ap-east-1 ape1-az3 | 355 | 88% | 8.3 | 9 (11-20 03:02Z) |
| ap-northeast-1 apne1-az1 | 222 | 95% | 8.7 | 9 (11-19 21:24Z) |
| ap-northeast-1 apne1-az2 | 207 | 87% | 8.2 | 9 (11-19 21:24Z) |
| ap-northeast-1 apne1-az4 | 285 | 99% | 8.9 | 9 (11-19 21:24Z) |
| ap-northeast-2 apne2-az1 | 448 | 100% | 9.0 | 9 (11-20 03:02Z) |
| ap-northeast-2 apne2-az2 | 125 | 87% | 8.2 | 9 (11-19 21:24Z) |
| ap-northeast-2 apne2-az3 | 465 | 100% | 9.0 | 9 (11-20 03:02Z) |
| ap-northeast-2 apne2-az4 | 364 | 87% | 8.2 | 9 (11-20 03:02Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 76 | 87% | 8.2 | 9 (11-19 21:24Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 89 | 84% | 8.0 | 9 (11-19 12:52Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 159 | 91% | 8.4 | 3 (11-20 03:02Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 139 | 93% | 8.5 | 9 (11-18 04:11Z) |
| us-east-2 use2-az1 | 199 | 99% | 8.9 | 9 (11-20 03:02Z) |
| us-east-2 use2-az2 | 219 | 99% | 8.9 | 9 (11-20 03:02Z) |
| us-east-2 use2-az3 | 244 | 97% | 8.8 | 9 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.704600 | 2026-11-20T03:02:04Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-20T03:02:04Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.724800 | 2026-11-20T03:02:04Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.619400 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.632300 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.613100 | 2026-11-20T03:02:04Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-20T03:02:04Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.704300 | 2026-11-20T03:02:04Z |
| ap-south-1 | ap-south-1a | Windows | 0.419900 | 2026-11-20T03:02:04Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.733700 | 2026-11-20T03:02:04Z |
| ap-south-1 | ap-south-1b | Windows | 0.415700 | 2026-11-20T03:02:04Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.648400 | 2026-11-20T03:02:04Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.533500 | 2026-11-20T03:02:04Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.483400 | 2026-11-20T03:02:04Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.549200 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.872900 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.894600 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1b | Windows | 0.291400 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.676300 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.738900 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.632500 | 2026-11-20T03:02:04Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.533100 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.539300 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.531300 | 2026-11-20T03:02:04Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.636300 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2a | Windows | 0.316000 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.704500 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.583900 | 2026-11-20T03:02:04Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-20T03:02:04Z |
