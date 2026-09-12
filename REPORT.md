# Spot placement score log

Generated 2026-09-12 05:42 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 89 | 0% | 1.3 | 3 (09-12 05:42Z) |
| ap-northeast-1 | 89 | 0% | 1.8 | 3 (09-12 05:42Z) |
| ap-northeast-2 | 89 | 0% | 2.9 | 3 (09-12 05:42Z) |
| ap-south-1 | 89 | 0% | 2.0 | 3 (09-12 05:42Z) |
| ap-southeast-2 | 89 | 0% | 1.0 | 1 (09-12 05:42Z) |
| ap-southeast-3 | 89 | 0% | 2.5 | 3 (09-12 05:42Z) |
| us-east-1 | 89 | 0% | 1.9 | 2 (09-12 05:42Z) |
| us-east-2 | 89 | 0% | 1.5 | 3 (09-12 05:42Z) |
| us-west-2 | 89 | 0% | 1.4 | 1 (09-12 05:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111333333333333
ap-northeast-1   311333311333331221111222112322222211232211233233
ap-northeast-2   333333333333333333333333333333333332333333333333
ap-south-1       233333323333111211113111221111111112113131211113
ap-southeast-2   111111111111111111111111111111111111111111113111
ap-southeast-3   333333331133333333133332123331131331133333333333
us-east-1        211313233332323233323223333211332212211311311332
us-east-2        111111311111331111311133331133331113111111313113
us-west-2        222222111111111111112133111111111111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 1.6 | 3 (09-12 05:42Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 45 | 0% | 2.2 | 3 (09-12 05:42Z) |
| ap-northeast-2 apne2-az1 | 84 | 0% | 2.9 | 3 (09-12 05:42Z) |
| ap-northeast-2 apne2-az3 | 81 | 0% | 2.9 | 3 (09-12 05:42Z) |
| ap-northeast-2 apne2-az4 | 87 | 0% | 3.0 | 3 (09-12 05:42Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 48 | 0% | 2.5 | 3 (09-12 05:42Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 72 | 0% | 2.9 | 3 (09-12 05:42Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 15 | 0% | 1.3 | 1 (09-11 22:30Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 26 | 0% | 1.3 | 3 (09-12 05:42Z) |
| us-east-2 use2-az2 | 37 | 0% | 1.6 | 3 (09-12 05:42Z) |
| us-east-2 use2-az3 | 39 | 0% | 2.1 | 3 (09-12 05:42Z) |
| us-west-2 usw2-az1 | 18 | 0% | 1.4 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az2 | 14 | 0% | 1.3 | 1 (09-11 00:59Z) |
| us-west-2 usw2-az3 | 45 | 0% | 1.3 | 1 (09-12 01:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 89 | 0% | 3.0 | 3 (09-12 05:42Z) |
| ap-northeast-1 | 89 | 75% | 7.3 | 9 (09-12 05:42Z) |
| ap-northeast-2 | 89 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-south-1 | 89 | 17% | 3.8 | 9 (09-12 05:42Z) |
| ap-southeast-2 | 89 | 11% | 2.7 | 3 (09-12 05:42Z) |
| ap-southeast-3 | 89 | 0% | 2.5 | 3 (09-12 05:42Z) |
| us-east-1 | 89 | 72% | 6.5 | 9 (09-12 05:42Z) |
| us-east-2 | 89 | 69% | 6.8 | 9 (09-12 05:42Z) |
| us-west-2 | 89 | 44% | 5.2 | 9 (09-12 05:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999999129994399993399922499923499999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333333333339999229995133399399999
ap-southeast-2   331333333333333331113111133111133222223112333333
ap-southeast-3   333333331133333333133332123331131331133333333333
us-east-1        425659959999999999999999954459944569932999923499
us-east-2        338299999999999999999999999999991999923339919199
us-west-2        534544998589699997199999994429513323133234233539
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 4 | 5 | 1 | · | 9 | 3 | 2 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 1 | · | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 1 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 5 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 6 | 1 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 3 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 2 | 5 | 4 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 41 | 80% | 7.8 | 9 (09-12 05:42Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 63 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az1 | 85 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 85 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 22 | 23% | 4.4 | 9 (09-12 01:03Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 31 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-1 use1-az4 | 34 | 97% | 8.8 | 9 (09-12 05:42Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 38 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az1 | 36 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az2 | 54 | 96% | 8.7 | 9 (09-12 05:42Z) |
| us-east-2 use2-az3 | 37 | 78% | 7.6 | 9 (09-12 05:42Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.739100 | 2026-09-12T05:42:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.841000 | 2026-09-12T05:42:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790300 | 2026-09-12T05:42:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.972200 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594300 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581300 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-09-12T05:42:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-12T05:42:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.539600 | 2026-09-12T05:42:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.319800 | 2026-09-12T05:42:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.492900 | 2026-09-12T05:42:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.324400 | 2026-09-12T05:42:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750200 | 2026-09-12T05:42:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502000 | 2026-09-12T05:42:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.840000 | 2026-09-12T05:42:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.435700 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.901600 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1a | Windows | 0.358500 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.713800 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1b | Windows | 0.326900 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.606200 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1c | Windows | 0.317200 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.539800 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1d | Windows | 0.323400 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.598000 | 2026-09-12T05:42:24Z |
| us-east-1 | us-east-1f | Windows | 0.318700 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.544200 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2a | Windows | 0.643800 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536300 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526600 | 2026-09-12T05:42:24Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.585200 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2a | Windows | 0.326300 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562400 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2b | Windows | 0.332900 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548400 | 2026-09-12T05:42:24Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-12T05:42:24Z |
