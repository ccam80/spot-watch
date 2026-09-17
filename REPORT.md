# Spot placement score log

Generated 2026-09-17 16:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 119 | 0% | 1.7 | 3 (09-17 16:52Z) |
| ap-northeast-1 | 119 | 0% | 1.9 | 2 (09-17 16:52Z) |
| ap-northeast-2 | 119 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 | 119 | 0% | 2.0 | 3 (09-17 16:52Z) |
| ap-southeast-2 | 119 | 0% | 1.0 | 1 (09-17 16:52Z) |
| ap-southeast-3 | 119 | 0% | 2.5 | 3 (09-17 16:52Z) |
| us-east-1 | 119 | 0% | 1.9 | 2 (09-17 16:52Z) |
| us-east-2 | 119 | 0% | 1.7 | 3 (09-17 16:52Z) |
| us-west-2 | 119 | 0% | 1.5 | 1 (09-17 16:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111333333333333333333333333333333333333333333
ap-northeast-1   222211232211233233333333333332233211322122221122
ap-northeast-2   333332333333333333333333333333333333333333333333
ap-south-1       111112113131211113333333133333333311111211221113
ap-southeast-2   111111111111113111111111111111111111111111111111
ap-southeast-3   131331133333333333333333333333131331313313333313
us-east-1        332212211311311332233113232332222221221131121232
us-east-2        331113111111313113333333333333331111111131313333
us-west-2        111111111111111111333133133333331112111211111131
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 64 | 0% | 2.2 | 3 (09-17 16:52Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 107 | 0% | 2.9 | 3 (09-17 16:52Z) |
| ap-northeast-2 apne2-az3 | 106 | 0% | 2.9 | 3 (09-17 16:52Z) |
| ap-northeast-2 apne2-az4 | 116 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 aps1-az1 | 49 | 0% | 1.6 | 1 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 63 | 0% | 2.6 | 3 (09-17 16:52Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 24 | 0% | 1.0 | 1 (09-17 16:52Z) |
| ap-southeast-3 apse3-az3 | 93 | 0% | 2.9 | 3 (09-17 16:52Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 35 | 0% | 1.1 | 1 (09-17 16:52Z) |
| us-east-1 use1-az4 | 22 | 0% | 1.3 | 3 (09-17 11:34Z) |
| us-east-1 use1-az5 | 34 | 0% | 1.4 | 3 (09-17 11:34Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 38 | 0% | 1.6 | 3 (09-17 11:34Z) |
| us-east-2 use2-az2 | 53 | 0% | 1.9 | 3 (09-17 16:52Z) |
| us-east-2 use2-az3 | 62 | 0% | 2.2 | 3 (09-17 16:52Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 24 | 0% | 1.8 | 3 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 60 | 0% | 1.6 | 3 (09-17 11:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 119 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-northeast-1 | 119 | 76% | 7.3 | 9 (09-17 16:52Z) |
| ap-northeast-2 | 119 | 100% | 9.0 | 9 (09-17 16:52Z) |
| ap-south-1 | 119 | 35% | 4.9 | 9 (09-17 16:52Z) |
| ap-southeast-2 | 119 | 8% | 2.6 | 3 (09-17 16:52Z) |
| ap-southeast-3 | 119 | 0% | 2.5 | 3 (09-17 16:52Z) |
| us-east-1 | 119 | 72% | 6.6 | 5 (09-17 16:52Z) |
| us-east-2 | 119 | 74% | 7.2 | 9 (09-17 16:52Z) |
| us-west-2 | 119 | 48% | 5.5 | 4 (09-17 16:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   399922499923499999999999999996499933999249994199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       229995133399399999999999999999999991899992999939
ap-southeast-2   133222223112333333333333223322222222222223322233
ap-southeast-3   131331133333333333333333333333131331313313333313
us-east-1        944569932999923499999999999999943684432493955995
us-east-2        991999923339919199999999999999999999921299999999
us-west-2        513323133234233539999999999999993425433534413994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 38 | 0% | 3.0 | 3 (09-16 01:21Z) |
| ap-northeast-1 apne1-az1 | 61 | 87% | 8.2 | 9 (09-17 16:52Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 80 | 100% | 9.0 | 9 (09-17 16:52Z) |
| ap-northeast-2 apne2-az1 | 110 | 100% | 9.0 | 9 (09-17 16:52Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 109 | 100% | 9.0 | 9 (09-17 16:52Z) |
| ap-northeast-2 apne2-az4 | 43 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 aps1-az1 | 30 | 27% | 4.6 | 9 (09-17 16:52Z) |
| ap-south-1 aps1-az2 | 32 | 0% | 3.0 | 3 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 46 | 61% | 6.7 | 9 (09-17 16:52Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 35 | 0% | 3.0 | 3 (09-17 00:25Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 45 | 100% | 9.0 | 9 (09-17 11:34Z) |
| us-east-1 use1-az4 | 47 | 96% | 8.7 | 9 (09-17 11:34Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 46 | 100% | 9.0 | 9 (09-17 06:03Z) |
| us-east-2 use2-az1 | 47 | 100% | 9.0 | 9 (09-17 16:52Z) |
| us-east-2 use2-az2 | 79 | 97% | 8.8 | 9 (09-17 16:52Z) |
| us-east-2 use2-az3 | 56 | 86% | 8.0 | 9 (09-17 16:52Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 28 | 96% | 8.8 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.715000 | 2026-09-17T16:52:51Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-17T16:52:51Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.799700 | 2026-09-17T16:52:51Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.979200 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589600 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578400 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565200 | 2026-09-17T16:52:51Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742300 | 2026-09-17T16:52:51Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.528700 | 2026-09-17T16:52:51Z |
| ap-south-1 | ap-south-1a | Windows | 0.320800 | 2026-09-17T16:52:51Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.471500 | 2026-09-17T16:52:51Z |
| ap-south-1 | ap-south-1b | Windows | 0.318200 | 2026-09-17T16:52:51Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686000 | 2026-09-17T16:52:51Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.500100 | 2026-09-17T16:52:51Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.894900 | 2026-09-17T16:52:51Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.524400 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.859300 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1a | Windows | 0.343700 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.657500 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1b | Windows | 0.326100 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.544800 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1c | Windows | 0.302700 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.540200 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1d | Windows | 0.312000 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.548100 | 2026-09-17T16:52:51Z |
| us-east-1 | us-east-1f | Windows | 0.320200 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529200 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2a | Windows | 0.639400 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.522400 | 2026-09-17T16:52:51Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.565100 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2a | Windows | 0.341600 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.533200 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2b | Windows | 0.338400 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.534900 | 2026-09-17T16:52:51Z |
| us-west-2 | us-west-2c | Windows | 0.338800 | 2026-09-17T16:52:51Z |
