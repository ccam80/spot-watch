# Spot placement score log

Generated 2026-09-15 07:38 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 107 | 0% | 1.6 | 3 (09-15 07:38Z) |
| ap-northeast-1 | 107 | 0% | 1.9 | 1 (09-15 07:38Z) |
| ap-northeast-2 | 107 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-south-1 | 107 | 0% | 2.1 | 1 (09-15 07:38Z) |
| ap-southeast-2 | 107 | 0% | 1.0 | 1 (09-15 07:38Z) |
| ap-southeast-3 | 107 | 0% | 2.5 | 1 (09-15 07:38Z) |
| us-east-1 | 107 | 0% | 2.0 | 1 (09-15 07:38Z) |
| us-east-2 | 107 | 0% | 1.7 | 1 (09-15 07:38Z) |
| us-west-2 | 107 | 0% | 1.5 | 2 (09-15 07:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111333333333333333333333333333333
ap-northeast-1   111222112322222211232211233233333333333332233211
ap-northeast-2   333333333333333332333333333333333333333333333333
ap-south-1       113111221111111112113131211113333333133333333311
ap-southeast-2   111111111111111111111111113111111111111111111111
ap-southeast-3   133332123331131331133333333333333333333333131331
us-east-1        323223333211332212211311311332233113232332222221
us-east-2        311133331133331113111111313113333333333333331111
us-west-2        112133111111111111111111111111333133133333331112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 29 | 0% | 1.0 | 1 (09-15 07:38Z) |
| ap-east-1 ape1-az2 | 52 | 0% | 2.0 | 3 (09-15 07:38Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 58 | 0% | 2.3 | 1 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 100 | 0% | 2.9 | 1 (09-15 07:38Z) |
| ap-northeast-2 apne2-az3 | 97 | 0% | 2.9 | 3 (09-15 07:38Z) |
| ap-northeast-2 apne2-az4 | 104 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-south-1 aps1-az1 | 45 | 0% | 1.7 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az3 | 61 | 0% | 2.6 | 3 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 21 | 0% | 1.1 | 1 (09-15 01:24Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 18 | 0% | 1.0 | 1 (09-15 07:38Z) |
| ap-southeast-3 apse3-az3 | 84 | 0% | 2.9 | 3 (09-15 01:24Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 30 | 0% | 1.1 | 1 (09-15 07:38Z) |
| us-east-1 use1-az4 | 17 | 0% | 1.2 | 1 (09-15 01:24Z) |
| us-east-1 use1-az5 | 30 | 0% | 1.3 | 1 (09-15 07:38Z) |
| us-east-1 use1-az6 | 41 | 0% | 1.2 | 1 (09-15 07:38Z) |
| us-east-2 use2-az1 | 32 | 0% | 1.6 | 1 (09-15 01:24Z) |
| us-east-2 use2-az2 | 47 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-east-2 use2-az3 | 52 | 0% | 2.2 | 1 (09-15 07:38Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 22 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 107 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-northeast-1 | 107 | 77% | 7.4 | 3 (09-15 07:38Z) |
| ap-northeast-2 | 107 | 100% | 9.0 | 9 (09-15 07:38Z) |
| ap-south-1 | 107 | 30% | 4.6 | 1 (09-15 07:38Z) |
| ap-southeast-2 | 107 | 9% | 2.7 | 2 (09-15 07:38Z) |
| ap-southeast-3 | 107 | 0% | 2.5 | 1 (09-15 07:38Z) |
| us-east-1 | 107 | 74% | 6.8 | 4 (09-15 07:38Z) |
| us-east-2 | 107 | 74% | 7.1 | 9 (09-15 07:38Z) |
| us-west-2 | 107 | 50% | 5.6 | 5 (09-15 07:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   129994399993399922499923499999999999999996499933
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333339999229995133399399999999999999999999991
ap-southeast-2   113111133111133222223112333333333333223322222222
ap-southeast-3   133332123331131331133333333333333333333333131331
us-east-1        999999954459944569932999923499999999999999943684
us-east-2        999999999999991999923339919199999999999999999999
us-west-2        199999994429513323133234233539999999999999993425
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 7 | · | 1 | 4 | 5 | 4 | 3 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 7 | · | 3 | 4 | 8 | 5 | 1 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | 4 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | 5 | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 41 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-east-1 ape1-az2 | 33 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-east-1 ape1-az3 | 35 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-northeast-1 apne1-az1 | 53 | 85% | 8.1 | 9 (09-14 23:05Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 73 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 98 | 100% | 9.0 | 9 (09-15 07:38Z) |
| ap-northeast-2 apne2-az2 | 10 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 97 | 100% | 9.0 | 9 (09-15 07:38Z) |
| ap-northeast-2 apne2-az4 | 37 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-south-1 aps1-az1 | 23 | 4% | 3.3 | 9 (09-15 01:24Z) |
| ap-south-1 aps1-az2 | 28 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-south-1 aps1-az3 | 37 | 54% | 6.2 | 9 (09-15 01:24Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 31 | 0% | 3.0 | 3 (09-15 01:24Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 45 | 96% | 8.7 | 2 (09-15 07:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 41 | 100% | 9.0 | 9 (09-15 07:38Z) |
| us-east-2 use2-az2 | 72 | 97% | 8.8 | 9 (09-15 07:38Z) |
| us-east-2 use2-az3 | 47 | 83% | 7.9 | 9 (09-15 07:38Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.724400 | 2026-09-15T07:38:39Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-15T07:38:39Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.798300 | 2026-09-15T07:38:39Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.979000 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591300 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579700 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566800 | 2026-09-15T07:38:39Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741600 | 2026-09-15T07:38:39Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.595000 | 2026-09-15T07:38:39Z |
| ap-south-1 | ap-south-1a | Windows | 0.331200 | 2026-09-15T07:38:39Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500900 | 2026-09-15T07:38:39Z |
| ap-south-1 | ap-south-1b | Windows | 0.319600 | 2026-09-15T07:38:39Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.694500 | 2026-09-15T07:38:39Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507300 | 2026-09-15T07:38:39Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.864300 | 2026-09-15T07:38:39Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.488600 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.880300 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1a | Windows | 0.345000 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.670900 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1b | Windows | 0.329300 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.587700 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1c | Windows | 0.308600 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.534500 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1d | Windows | 0.316800 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.575400 | 2026-09-15T07:38:39Z |
| us-east-1 | us-east-1f | Windows | 0.327300 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.528000 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2b | Windows | 0.637200 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517800 | 2026-09-15T07:38:39Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579500 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2a | Windows | 0.346600 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.548600 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2b | Windows | 0.340200 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.543900 | 2026-09-15T07:38:39Z |
| us-west-2 | us-west-2c | Windows | 0.341400 | 2026-09-15T07:38:39Z |
