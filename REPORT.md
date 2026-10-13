# Spot placement score log

Generated 2026-10-13 17:32 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 306 | 34% | 4.2 | 9 (10-13 17:32Z) |
| ap-northeast-1 | 306 | 15% | 2.8 | 2 (10-13 17:32Z) |
| ap-northeast-2 | 306 | 49% | 5.9 | 9 (10-13 17:32Z) |
| ap-south-1 | 306 | 2% | 1.8 | 1 (10-13 17:32Z) |
| ap-southeast-2 | 306 | 0% | 1.0 | 1 (10-13 17:32Z) |
| ap-southeast-3 | 306 | 22% | 3.3 | 2 (10-13 17:32Z) |
| us-east-1 | 306 | 9% | 2.5 | 1 (10-13 17:32Z) |
| us-east-2 | 306 | 27% | 3.5 | 1 (10-13 17:32Z) |
| us-west-2 | 306 | 12% | 2.4 | 1 (10-13 17:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119119999812111111111111111111111182292999999999
ap-northeast-1   199999999999911911115119711111191112222119221212
ap-northeast-2   999999999999991499999999999999999199999999999999
ap-south-1       111111111112222222222222211122111111222222222211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   141111111111111111111138811111389119997939515112
us-east-1        222331199199999211112111122211323233319223322211
us-east-2        991199999999999111811111111111111118119999991111
us-west-2        212999999991991121121211111111111199991111111111
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
| ap-east-1 ape1-az2 | 211 | 49% | 5.5 | 9 (10-13 17:32Z) |
| ap-northeast-1 apne1-az1 | 52 | 8% | 1.8 | 1 (10-13 17:32Z) |
| ap-northeast-1 apne1-az4 | 145 | 26% | 3.6 | 1 (10-12 01:14Z) |
| ap-northeast-2 apne2-az1 | 266 | 46% | 5.7 | 9 (10-13 17:32Z) |
| ap-northeast-2 apne2-az3 | 278 | 50% | 5.9 | 9 (10-13 17:32Z) |
| ap-northeast-2 apne2-az4 | 303 | 50% | 5.9 | 9 (10-13 17:32Z) |
| ap-south-1 aps1-az1 | 80 | 1% | 1.6 | 1 (10-13 09:19Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 48 | 0% | 1.1 | 1 (10-13 01:16Z) |
| ap-southeast-2 apse2-az2 | 32 | 0% | 1.0 | 1 (10-13 01:16Z) |
| ap-southeast-3 apse3-az1 | 58 | 0% | 1.0 | 1 (10-12 18:57Z) |
| ap-southeast-3 apse3-az3 | 208 | 31% | 4.2 | 2 (10-13 17:32Z) |
| us-east-1 use1-az1 | 60 | 0% | 1.1 | 1 (10-13 17:32Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 97 | 27% | 3.4 | 1 (10-13 17:32Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 124 | 38% | 4.4 | 1 (10-13 09:19Z) |
| us-east-2 use2-az2 | 155 | 45% | 4.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az3 | 184 | 42% | 4.9 | 9 (10-12 09:04Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 66 | 26% | 3.4 | 1 (10-13 17:32Z) |
| us-west-2 usw2-az3 | 126 | 22% | 3.3 | 1 (10-13 09:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 306 | 50% | 6.0 | 9 (10-13 17:32Z) |
| ap-northeast-1 | 306 | 74% | 7.2 | 9 (10-13 17:32Z) |
| ap-northeast-2 | 306 | 100% | 9.0 | 9 (10-13 17:32Z) |
| ap-south-1 | 306 | 61% | 6.4 | 9 (10-13 17:32Z) |
| ap-southeast-2 | 306 | 17% | 3.2 | 1 (10-13 17:32Z) |
| ap-southeast-3 | 306 | 22% | 3.3 | 2 (10-13 17:32Z) |
| us-east-1 | 306 | 71% | 6.6 | 2 (10-13 17:32Z) |
| us-east-2 | 306 | 72% | 7.0 | 1 (10-13 17:32Z) |
| us-west-2 | 306 | 53% | 5.7 | 4 (10-13 17:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   299999999999991992399139911991199999999999999239
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999992299299929991999149999999999929919
ap-southeast-2   222222229299922911111119111111118919999991111111
ap-southeast-3   141111111111111111111138811111389119997939515112
us-east-1        855763499999999554533433366354645699829999994542
us-east-2        993999999999999239933212121112121199229999991191
us-west-2        995999999999999432354413233313323399999935929944
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
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 181 | 70% | 7.2 | 9 (10-13 17:32Z) |
| ap-east-1 ape1-az2 | 151 | 73% | 7.4 | 9 (10-13 09:19Z) |
| ap-east-1 ape1-az3 | 151 | 71% | 7.3 | 9 (10-13 17:32Z) |
| ap-northeast-1 apne1-az1 | 144 | 92% | 8.5 | 9 (10-13 17:32Z) |
| ap-northeast-1 apne1-az2 | 82 | 68% | 7.1 | 9 (10-13 17:32Z) |
| ap-northeast-1 apne1-az4 | 174 | 98% | 8.9 | 9 (10-13 17:32Z) |
| ap-northeast-2 apne2-az1 | 241 | 100% | 9.0 | 9 (10-13 17:32Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 261 | 100% | 9.0 | 9 (10-13 17:32Z) |
| ap-northeast-2 apne2-az4 | 175 | 73% | 7.4 | 9 (10-13 17:32Z) |
| ap-south-1 aps1-az1 | 108 | 80% | 7.8 | 9 (10-13 17:32Z) |
| ap-south-1 aps1-az2 | 107 | 66% | 7.0 | 9 (10-12 18:57Z) |
| ap-south-1 aps1-az3 | 125 | 86% | 8.1 | 9 (10-13 17:32Z) |
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
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 138 | 94% | 8.6 | 9 (10-13 09:19Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.717400 | 2026-10-13T17:32:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-13T17:32:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.758500 | 2026-10-13T17:32:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.940800 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592300 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.587400 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.576800 | 2026-10-13T17:32:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742100 | 2026-10-13T17:32:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.547600 | 2026-10-13T17:32:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.386800 | 2026-10-13T17:32:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.696300 | 2026-10-13T17:32:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.338800 | 2026-10-13T17:32:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.723200 | 2026-10-13T17:32:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.519400 | 2026-10-13T17:32:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.471700 | 2026-10-13T17:32:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.615900 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.498500 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.484500 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.481300 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.412000 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.473500 | 2026-10-13T17:32:50Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.540900 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2a | Windows | 0.643900 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531700 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.525400 | 2026-10-13T17:32:50Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.540700 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2a | Windows | 0.317500 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.508300 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2b | Windows | 0.333400 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.511700 | 2026-10-13T17:32:50Z |
| us-west-2 | us-west-2c | Windows | 0.317300 | 2026-10-13T17:32:50Z |
