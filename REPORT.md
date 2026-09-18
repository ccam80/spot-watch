# Spot placement score log

Generated 2026-09-18 04:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 122 | 0% | 1.7 | 3 (09-18 04:33Z) |
| ap-northeast-1 | 122 | 0% | 1.9 | 1 (09-18 04:33Z) |
| ap-northeast-2 | 122 | 0% | 3.0 | 3 (09-18 04:33Z) |
| ap-south-1 | 122 | 0% | 2.0 | 3 (09-18 04:33Z) |
| ap-southeast-2 | 122 | 0% | 1.0 | 1 (09-18 04:33Z) |
| ap-southeast-3 | 122 | 0% | 2.5 | 1 (09-18 04:33Z) |
| us-east-1 | 122 | 0% | 1.9 | 1 (09-18 04:33Z) |
| us-east-2 | 122 | 0% | 1.7 | 3 (09-18 04:33Z) |
| us-west-2 | 122 | 0% | 1.5 | 1 (09-18 04:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111333333333333333333333333333333333333333333333
ap-northeast-1   211232211233233333333333332233211322122221122221
ap-northeast-2   332333333333333333333333333333333333333333333333
ap-south-1       112113131211113333333133333333311111211221113333
ap-southeast-2   111111111113111111111111111111111111111111111111
ap-southeast-3   331133333333333333333333333131331313313333313131
us-east-1        212211311311332233113232332222221221131121232231
us-east-2        113111111313113333333333333331111111131313333333
us-west-2        111111111111111333133133333331112111211111131221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 67 | 0% | 2.2 | 3 (09-18 04:33Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 110 | 0% | 2.9 | 3 (09-18 04:33Z) |
| ap-northeast-2 apne2-az3 | 108 | 0% | 2.9 | 3 (09-18 04:33Z) |
| ap-northeast-2 apne2-az4 | 119 | 0% | 3.0 | 3 (09-18 04:33Z) |
| ap-south-1 aps1-az1 | 51 | 0% | 1.7 | 3 (09-17 23:31Z) |
| ap-south-1 aps1-az3 | 66 | 0% | 2.6 | 3 (09-18 04:33Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 25 | 0% | 1.0 | 1 (09-18 04:33Z) |
| ap-southeast-3 apse3-az3 | 94 | 0% | 2.9 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 36 | 0% | 1.1 | 1 (09-18 04:33Z) |
| us-east-1 use1-az4 | 24 | 0% | 1.3 | 3 (09-17 23:31Z) |
| us-east-1 use1-az5 | 35 | 0% | 1.4 | 3 (09-17 23:31Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 40 | 0% | 1.6 | 3 (09-18 04:33Z) |
| us-east-2 use2-az2 | 56 | 0% | 1.9 | 3 (09-18 04:33Z) |
| us-east-2 use2-az3 | 65 | 0% | 2.3 | 3 (09-18 04:33Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 24 | 0% | 1.8 | 3 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 60 | 0% | 1.6 | 3 (09-17 11:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 122 | 0% | 3.0 | 3 (09-18 04:33Z) |
| ap-northeast-1 | 122 | 75% | 7.3 | 3 (09-18 04:33Z) |
| ap-northeast-2 | 122 | 100% | 9.0 | 9 (09-18 04:33Z) |
| ap-south-1 | 122 | 37% | 5.0 | 9 (09-18 04:33Z) |
| ap-southeast-2 | 122 | 8% | 2.6 | 2 (09-18 04:33Z) |
| ap-southeast-3 | 122 | 0% | 2.5 | 1 (09-18 04:33Z) |
| us-east-1 | 122 | 73% | 6.7 | 9 (09-18 04:33Z) |
| us-east-2 | 122 | 75% | 7.2 | 9 (09-18 04:33Z) |
| us-west-2 | 122 | 48% | 5.5 | 9 (09-18 04:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   922499923499999999999999996499933999249994199993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       995133399399999999999999999999991899992999939999
ap-southeast-2   222223112333333333333223322222222222223322233222
ap-southeast-3   331133333333333333333333333131331313313333313131
us-east-1        569932999923499999999999999943684432493955995699
us-east-2        999923339919199999999999999999999921299999999999
us-west-2        323133234233539999999999999993425433534413994459
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 4 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 4 | 8 | 7 | 7 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 40 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-northeast-1 apne1-az1 | 62 | 87% | 8.2 | 9 (09-17 20:14Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 81 | 100% | 9.0 | 9 (09-17 20:14Z) |
| ap-northeast-2 apne2-az1 | 113 | 100% | 9.0 | 9 (09-18 04:33Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 112 | 100% | 9.0 | 9 (09-18 04:33Z) |
| ap-northeast-2 apne2-az4 | 43 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 aps1-az1 | 33 | 33% | 5.0 | 9 (09-18 04:33Z) |
| ap-south-1 aps1-az2 | 33 | 0% | 3.0 | 3 (09-17 20:14Z) |
| ap-south-1 aps1-az3 | 49 | 63% | 6.8 | 9 (09-18 04:33Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 36 | 0% | 3.0 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 46 | 100% | 9.0 | 9 (09-18 04:33Z) |
| us-east-1 use1-az4 | 49 | 96% | 8.7 | 9 (09-18 04:33Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 47 | 100% | 9.0 | 9 (09-18 04:33Z) |
| us-east-2 use2-az1 | 49 | 100% | 9.0 | 9 (09-18 04:33Z) |
| us-east-2 use2-az2 | 82 | 98% | 8.8 | 9 (09-18 04:33Z) |
| us-east-2 use2-az3 | 59 | 86% | 8.1 | 9 (09-18 04:33Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 28 | 96% | 8.8 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712600 | 2026-09-18T04:33:55Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-18T04:33:55Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.809700 | 2026-09-18T04:33:55Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.992700 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589800 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579100 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565200 | 2026-09-18T04:33:55Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742400 | 2026-09-18T04:33:55Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.518200 | 2026-09-18T04:33:55Z |
| ap-south-1 | ap-south-1a | Windows | 0.319100 | 2026-09-18T04:33:55Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.468900 | 2026-09-18T04:33:55Z |
| ap-south-1 | ap-south-1b | Windows | 0.318400 | 2026-09-18T04:33:55Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686600 | 2026-09-18T04:33:55Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507100 | 2026-09-18T04:33:55Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.882800 | 2026-09-18T04:33:55Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.546400 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.855600 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1a | Windows | 0.344300 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.650600 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1b | Windows | 0.324300 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.538600 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1c | Windows | 0.300500 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.542800 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1d | Windows | 0.310300 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.538700 | 2026-09-18T04:33:55Z |
| us-east-1 | us-east-1f | Windows | 0.319500 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.531000 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2a | Windows | 0.639800 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529900 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2b | Windows | 0.637700 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.521600 | 2026-09-18T04:33:55Z |
| us-east-2 | us-east-2c | Windows | 0.638400 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.564300 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2a | Windows | 0.341500 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.530500 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2b | Windows | 0.338300 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.533600 | 2026-09-18T04:33:55Z |
| us-west-2 | us-west-2c | Windows | 0.338400 | 2026-09-18T04:33:55Z |
