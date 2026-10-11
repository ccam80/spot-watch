# Spot placement score log

Generated 2026-10-11 05:37 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 297 | 32% | 4.1 | 2 (10-11 05:37Z) |
| ap-northeast-1 | 297 | 15% | 2.8 | 2 (10-11 05:37Z) |
| ap-northeast-2 | 297 | 47% | 5.8 | 9 (10-11 05:37Z) |
| ap-south-1 | 297 | 2% | 1.8 | 2 (10-11 05:37Z) |
| ap-southeast-2 | 297 | 0% | 1.0 | 1 (10-11 05:37Z) |
| ap-southeast-3 | 297 | 21% | 3.3 | 7 (10-11 05:37Z) |
| us-east-1 | 297 | 10% | 2.6 | 9 (10-11 05:37Z) |
| us-east-2 | 297 | 26% | 3.5 | 9 (10-11 05:37Z) |
| us-west-2 | 297 | 12% | 2.4 | 1 (10-11 05:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111199399119119999812111111111111111111111182292
ap-northeast-1   981212982199999999999911911115119711111191112222
ap-northeast-2   999999999999999999999991499999999999999999199999
ap-south-1       111111112111111111112222222222222211122111111222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111119991141111111111111111111138811111389119997
us-east-1        222119229222331199199999211112111122211323233319
us-east-2        218999999991199999999999111811111111111111118119
us-west-2        121112221212999999991991121121211111111111199991
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
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
| ap-northeast-2 apne2-az1 | 257 | 44% | 5.5 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 269 | 48% | 5.8 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az4 | 294 | 48% | 5.9 | 9 (10-11 05:37Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 30 | 0% | 1.0 | 1 (10-10 08:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 202 | 30% | 4.2 | 7 (10-11 05:37Z) |
| us-east-1 use1-az1 | 55 | 0% | 1.1 | 1 (10-11 05:37Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 94 | 28% | 3.5 | 9 (10-11 05:37Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 118 | 36% | 4.3 | 4 (10-11 05:37Z) |
| us-east-2 use2-az2 | 151 | 43% | 4.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 179 | 41% | 4.8 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 64 | 27% | 3.5 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 297 | 48% | 5.9 | 9 (10-11 05:37Z) |
| ap-northeast-1 | 297 | 73% | 7.2 | 9 (10-11 05:37Z) |
| ap-northeast-2 | 297 | 100% | 9.0 | 9 (10-11 05:37Z) |
| ap-south-1 | 297 | 60% | 6.3 | 9 (10-11 05:37Z) |
| ap-southeast-2 | 297 | 17% | 3.2 | 9 (10-11 05:37Z) |
| ap-southeast-3 | 297 | 21% | 3.3 | 7 (10-11 05:37Z) |
| us-east-1 | 297 | 71% | 6.6 | 9 (10-11 05:37Z) |
| us-east-2 | 297 | 72% | 7.1 | 9 (10-11 05:37Z) |
| us-west-2 | 297 | 53% | 5.7 | 9 (10-11 05:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999224992299999999999991992399139911991199999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999992999999999999999992299299929991999149999999
ap-southeast-2   222222222222222229299922911111119111111118919999
ap-southeast-3   111119991141111111111111111111138811111389119997
us-east-1        344559449855763499999999554533433366354645699829
us-east-2        599999999993999999999999239933212121112121199229
us-west-2        444339344995999999999999432354413233313323399999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 176 | 69% | 7.2 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az2 | 146 | 72% | 7.3 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az3 | 145 | 70% | 7.2 | 9 (10-11 05:37Z) |
| ap-northeast-1 apne1-az1 | 140 | 92% | 8.5 | 9 (10-11 05:37Z) |
| ap-northeast-1 apne1-az2 | 76 | 66% | 6.9 | 9 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 168 | 99% | 8.9 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az1 | 232 | 100% | 9.0 | 9 (10-10 23:28Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 254 | 100% | 9.0 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az4 | 169 | 72% | 7.3 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az1 | 103 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 119 | 85% | 8.1 | 9 (10-10 23:28Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 37 | 65% | 6.8 | 9 (10-11 05:37Z) |
| ap-southeast-3 apse3-az3 | 59 | 27% | 4.5 | 9 (10-10 23:28Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 99 | 95% | 8.6 | 9 (10-10 15:16Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 81 | 95% | 8.7 | 9 (10-10 08:24Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 133 | 94% | 8.6 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az1 | 73 | 97% | 8.8 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 85 | 95% | 8.7 | 9 (10-10 23:28Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710500 | 2026-10-11T05:37:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-11T05:37:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.767000 | 2026-10-11T05:37:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.953000 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597800 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585500 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.576000 | 2026-10-11T05:37:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742400 | 2026-10-11T05:37:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.585300 | 2026-10-11T05:37:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.369300 | 2026-10-11T05:37:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.669200 | 2026-10-11T05:37:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.350700 | 2026-10-11T05:37:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.728200 | 2026-10-11T05:37:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504700 | 2026-10-11T05:37:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.416300 | 2026-10-11T05:37:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.529700 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.481300 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.459000 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395100 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.464300 | 2026-10-11T05:37:06Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534900 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2a | Windows | 0.639900 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528800 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2b | Windows | 0.640100 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516600 | 2026-10-11T05:37:06Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.523600 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2a | Windows | 0.320500 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.486600 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2b | Windows | 0.322500 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.491300 | 2026-10-11T05:37:06Z |
| us-west-2 | us-west-2c | Windows | 0.320300 | 2026-10-11T05:37:06Z |
