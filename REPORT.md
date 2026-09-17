# Spot placement score log

Generated 2026-09-17 00:25 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 116 | 0% | 1.7 | 3 (09-17 00:25Z) |
| ap-northeast-1 | 116 | 0% | 1.9 | 1 (09-17 00:25Z) |
| ap-northeast-2 | 116 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-south-1 | 116 | 0% | 2.0 | 1 (09-17 00:25Z) |
| ap-southeast-2 | 116 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-southeast-3 | 116 | 0% | 2.5 | 3 (09-17 00:25Z) |
| us-east-1 | 116 | 0% | 1.9 | 1 (09-17 00:25Z) |
| us-east-2 | 116 | 0% | 1.7 | 3 (09-17 00:25Z) |
| us-west-2 | 116 | 0% | 1.5 | 1 (09-17 00:25Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111333333333333333333333333333333333333333
ap-northeast-1   322222211232211233233333333333332233211322122221
ap-northeast-2   333333332333333333333333333333333333333333333333
ap-south-1       111111112113131211113333333133333333311111211221
ap-southeast-2   111111111111111113111111111111111111111111111111
ap-southeast-3   331131331133333333333333333333333131331313313333
us-east-1        211332212211311311332233113232332222221221131121
us-east-2        133331113111111313113333333333333331111111131313
us-west-2        111111111111111111111333133133333331112111211111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 61 | 0% | 2.1 | 3 (09-17 00:25Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 106 | 0% | 2.9 | 3 (09-16 18:09Z) |
| ap-northeast-2 apne2-az3 | 103 | 0% | 2.9 | 3 (09-16 22:04Z) |
| ap-northeast-2 apne2-az4 | 113 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-south-1 aps1-az1 | 49 | 0% | 1.6 | 1 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 62 | 0% | 2.6 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 23 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-southeast-3 apse3-az3 | 91 | 0% | 2.9 | 3 (09-17 00:25Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 33 | 0% | 1.1 | 1 (09-17 00:25Z) |
| us-east-1 use1-az4 | 20 | 0% | 1.2 | 1 (09-16 13:26Z) |
| us-east-1 use1-az5 | 33 | 0% | 1.3 | 1 (09-17 00:25Z) |
| us-east-1 use1-az6 | 43 | 0% | 1.2 | 1 (09-15 18:07Z) |
| us-east-2 use2-az1 | 36 | 0% | 1.6 | 3 (09-16 18:09Z) |
| us-east-2 use2-az2 | 51 | 0% | 1.8 | 3 (09-17 00:25Z) |
| us-east-2 use2-az3 | 59 | 0% | 2.2 | 3 (09-17 00:25Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 23 | 0% | 1.8 | 1 (09-15 13:28Z) |
| us-west-2 usw2-az3 | 59 | 0% | 1.5 | 1 (09-16 22:04Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 116 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-northeast-1 | 116 | 76% | 7.4 | 4 (09-17 00:25Z) |
| ap-northeast-2 | 116 | 100% | 9.0 | 9 (09-17 00:25Z) |
| ap-south-1 | 116 | 34% | 4.9 | 9 (09-17 00:25Z) |
| ap-southeast-2 | 116 | 9% | 2.6 | 2 (09-17 00:25Z) |
| ap-southeast-3 | 116 | 0% | 2.5 | 3 (09-17 00:25Z) |
| us-east-1 | 116 | 72% | 6.6 | 5 (09-17 00:25Z) |
| us-east-2 | 116 | 73% | 7.1 | 9 (09-17 00:25Z) |
| us-west-2 | 116 | 47% | 5.4 | 3 (09-17 00:25Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   993399922499923499999999999999996499933999249994
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999229995133399399999999999999999999991899992999
ap-southeast-2   111133222223112333333333333223322222222222223322
ap-southeast-3   331131331133333333333333333333333131331313313333
us-east-1        459944569932999923499999999999999943684432493955
us-east-2        999991999923339919199999999999999999999921299999
us-west-2        429513323133234233539999999999999993425433534413
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 4 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 5 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 6 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 38 | 0% | 3.0 | 3 (09-16 01:21Z) |
| ap-northeast-1 apne1-az1 | 59 | 86% | 8.2 | 9 (09-16 22:04Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 79 | 100% | 9.0 | 9 (09-16 22:04Z) |
| ap-northeast-2 apne2-az1 | 107 | 100% | 9.0 | 9 (09-17 00:25Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 106 | 100% | 9.0 | 9 (09-17 00:25Z) |
| ap-northeast-2 apne2-az4 | 42 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-south-1 aps1-az1 | 29 | 24% | 4.4 | 9 (09-17 00:25Z) |
| ap-south-1 aps1-az2 | 32 | 0% | 3.0 | 3 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 44 | 59% | 6.6 | 9 (09-17 00:25Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 35 | 0% | 3.0 | 3 (09-17 00:25Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 45 | 96% | 8.7 | 2 (09-15 07:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 45 | 100% | 9.0 | 9 (09-16 07:37Z) |
| us-east-2 use2-az1 | 45 | 100% | 9.0 | 9 (09-17 00:25Z) |
| us-east-2 use2-az2 | 77 | 97% | 8.8 | 9 (09-17 00:25Z) |
| us-east-2 use2-az3 | 53 | 85% | 8.0 | 9 (09-17 00:25Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.717100 | 2026-09-17T00:25:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-17T00:25:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.803300 | 2026-09-17T00:25:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.986200 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589800 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579000 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566000 | 2026-09-17T00:25:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742100 | 2026-09-17T00:25:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.553800 | 2026-09-17T00:25:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.325200 | 2026-09-17T00:25:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.475500 | 2026-09-17T00:25:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.319000 | 2026-09-17T00:25:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.685300 | 2026-09-17T00:25:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497800 | 2026-09-17T00:25:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.884500 | 2026-09-17T00:25:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.499000 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.870000 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1a | Windows | 0.344600 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.671200 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1b | Windows | 0.327800 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.556700 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1c | Windows | 0.304400 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.546000 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1d | Windows | 0.313000 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.553600 | 2026-09-17T00:25:49Z |
| us-east-1 | us-east-1f | Windows | 0.321700 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526000 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2a | Windows | 0.639800 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527700 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.518800 | 2026-09-17T00:25:49Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568100 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2a | Windows | 0.344200 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.534400 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2b | Windows | 0.338200 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.536500 | 2026-09-17T00:25:49Z |
| us-west-2 | us-west-2c | Windows | 0.338600 | 2026-09-17T00:25:49Z |
