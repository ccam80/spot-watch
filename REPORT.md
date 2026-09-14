# Spot placement score log

Generated 2026-09-14 19:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 104 | 0% | 1.5 | 3 (09-14 19:16Z) |
| ap-northeast-1 | 104 | 0% | 2.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 | 104 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-south-1 | 104 | 0% | 2.1 | 3 (09-14 19:16Z) |
| ap-southeast-2 | 104 | 0% | 1.0 | 1 (09-14 19:16Z) |
| ap-southeast-3 | 104 | 0% | 2.5 | 1 (09-14 19:16Z) |
| us-east-1 | 104 | 0% | 2.0 | 2 (09-14 19:16Z) |
| us-east-2 | 104 | 0% | 1.7 | 1 (09-14 19:16Z) |
| us-west-2 | 104 | 0% | 1.5 | 1 (09-14 19:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111333333333333333333333333333
ap-northeast-1   221111222112322222211232211233233333333333332233
ap-northeast-2   333333333333333333332333333333333333333333333333
ap-south-1       211113111221111111112113131211113333333133333333
ap-southeast-2   111111111111111111111111111113111111111111111111
ap-southeast-3   333133332123331131331133333333333333333333333131
us-east-1        233323223333211332212211311311332233113232332222
us-east-2        111311133331133331113111111313113333333333333331
us-west-2        111112133111111111111111111111111333133133333331
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 49 | 0% | 1.9 | 3 (09-14 19:16Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 57 | 0% | 2.3 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az1 | 98 | 0% | 2.9 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 94 | 0% | 2.9 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az4 | 101 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-south-1 aps1-az1 | 44 | 0% | 1.6 | 3 (09-14 19:16Z) |
| ap-south-1 aps1-az3 | 60 | 0% | 2.6 | 3 (09-14 19:16Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 82 | 0% | 2.9 | 3 (09-14 00:58Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 28 | 0% | 1.1 | 1 (09-14 19:16Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 29 | 0% | 1.3 | 3 (09-13 19:23Z) |
| us-east-1 use1-az6 | 39 | 0% | 1.2 | 3 (09-13 19:23Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 46 | 0% | 1.8 | 1 (09-14 19:16Z) |
| us-east-2 use2-az3 | 51 | 0% | 2.3 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 21 | 0% | 1.9 | 3 (09-14 06:08Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 104 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-1 | 104 | 78% | 7.5 | 9 (09-14 19:16Z) |
| ap-northeast-2 | 104 | 100% | 9.0 | 9 (09-14 19:16Z) |
| ap-south-1 | 104 | 29% | 4.6 | 9 (09-14 19:16Z) |
| ap-southeast-2 | 104 | 10% | 2.7 | 2 (09-14 19:16Z) |
| ap-southeast-3 | 104 | 0% | 2.5 | 1 (09-14 19:16Z) |
| us-east-1 | 104 | 74% | 6.8 | 3 (09-14 19:16Z) |
| us-east-2 | 104 | 73% | 7.1 | 9 (09-14 19:16Z) |
| us-west-2 | 104 | 51% | 5.7 | 3 (09-14 19:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999129994399993399922499923499999999999999996499
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333339999229995133399399999999999999999999
ap-southeast-2   331113111133111133222223112333333333333223322222
ap-southeast-3   333133332123331131331133333333333333333333333131
us-east-1        999999999954459944569932999923499999999999999943
us-east-2        999999999999999991999923339919199999999999999999
us-west-2        997199999994429513323133234233539999999999999993
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 6 | · | 3 | 4 | 8 | 5 | · | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 3 |
| ap-southeast-2 | 2 | 6 | · | 1 | 2 | 2 | 2 | · | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 32 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 52 | 85% | 8.1 | 9 (09-14 19:16Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 72 | 100% | 9.0 | 9 (09-14 19:16Z) |
| ap-northeast-2 apne2-az1 | 95 | 100% | 9.0 | 9 (09-14 19:16Z) |
| ap-northeast-2 apne2-az2 | 10 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 94 | 100% | 9.0 | 9 (09-14 19:16Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 22 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 35 | 51% | 6.1 | 9 (09-14 19:16Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 44 | 98% | 8.8 | 9 (09-14 00:58Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 40 | 100% | 9.0 | 9 (09-14 13:55Z) |
| us-east-2 use2-az2 | 69 | 97% | 8.8 | 9 (09-14 19:16Z) |
| us-east-2 use2-az3 | 45 | 82% | 7.8 | 9 (09-14 19:16Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725900 | 2026-09-14T19:16:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-14T19:16:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.796900 | 2026-09-14T19:16:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.977900 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592400 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580500 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567500 | 2026-09-14T19:16:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741500 | 2026-09-14T19:16:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.594800 | 2026-09-14T19:16:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.331200 | 2026-09-14T19:16:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.510200 | 2026-09-14T19:16:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.321700 | 2026-09-14T19:16:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700800 | 2026-09-14T19:16:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509400 | 2026-09-14T19:16:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.849300 | 2026-09-14T19:16:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.481700 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.880100 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1a | Windows | 0.346400 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.673600 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1b | Windows | 0.330100 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.594100 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1c | Windows | 0.310500 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.540500 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1d | Windows | 0.319000 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.585200 | 2026-09-14T19:16:44Z |
| us-east-1 | us-east-1f | Windows | 0.329900 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530400 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531100 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2b | Windows | 0.637300 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.520500 | 2026-09-14T19:16:44Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.588500 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2a | Windows | 0.346100 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.561600 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2b | Windows | 0.340900 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.545600 | 2026-09-14T19:16:44Z |
| us-west-2 | us-west-2c | Windows | 0.342400 | 2026-09-14T19:16:44Z |
