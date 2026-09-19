# Spot placement score log

Generated 2026-09-19 20:33 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 132 | 0% | 1.8 | 3 (09-19 20:33Z) |
| ap-northeast-1 | 132 | 0% | 1.9 | 2 (09-19 20:33Z) |
| ap-northeast-2 | 132 | 0% | 3.0 | 3 (09-19 20:33Z) |
| ap-south-1 | 132 | 0% | 2.0 | 3 (09-19 20:33Z) |
| ap-southeast-2 | 132 | 0% | 1.0 | 1 (09-19 20:33Z) |
| ap-southeast-3 | 132 | 0% | 2.5 | 3 (09-19 20:33Z) |
| us-east-1 | 132 | 0% | 1.9 | 1 (09-19 20:33Z) |
| us-east-2 | 132 | 0% | 1.8 | 1 (09-19 20:33Z) |
| us-west-2 | 132 | 0% | 1.6 | 3 (09-19 20:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   332333333333333322332113221222211222211122122332
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       111133333331333333333111112112211133331131211333
ap-southeast-2   131111111111111111111111111111111111111111111111
ap-southeast-3   333333333333333331313313133133333131311233333333
us-east-1        113322331132323322222212211311212322312311121311
us-east-2        131133333333333333311111111313133333331331133331
us-west-2        111113331331333333311121112111111312213111233333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 37 | 0% | 1.3 | 3 (09-19 20:33Z) |
| ap-east-1 ape1-az2 | 76 | 0% | 2.3 | 3 (09-19 20:33Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 65 | 0% | 2.2 | 3 (09-19 17:57Z) |
| ap-northeast-2 apne2-az1 | 120 | 0% | 2.9 | 3 (09-19 20:33Z) |
| ap-northeast-2 apne2-az3 | 117 | 0% | 2.9 | 3 (09-19 20:33Z) |
| ap-northeast-2 apne2-az4 | 129 | 0% | 3.0 | 3 (09-19 20:33Z) |
| ap-south-1 aps1-az1 | 53 | 0% | 1.7 | 2 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 71 | 0% | 2.6 | 3 (09-19 20:33Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 102 | 0% | 2.9 | 3 (09-19 20:33Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 39 | 0% | 1.1 | 1 (09-18 21:36Z) |
| us-east-1 use1-az4 | 26 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az5 | 37 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 43 | 0% | 1.7 | 3 (09-19 10:50Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 72 | 0% | 2.3 | 3 (09-19 17:57Z) |
| us-west-2 usw2-az1 | 37 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 67 | 0% | 1.7 | 3 (09-19 20:33Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 132 | 0% | 3.0 | 3 (09-19 20:33Z) |
| ap-northeast-1 | 132 | 77% | 7.4 | 9 (09-19 20:33Z) |
| ap-northeast-2 | 132 | 100% | 9.0 | 9 (09-19 20:33Z) |
| ap-south-1 | 132 | 40% | 5.2 | 9 (09-19 20:33Z) |
| ap-southeast-2 | 132 | 8% | 2.6 | 3 (09-19 20:33Z) |
| ap-southeast-3 | 132 | 0% | 2.5 | 3 (09-19 20:33Z) |
| us-east-1 | 132 | 73% | 6.7 | 9 (09-19 20:33Z) |
| us-east-2 | 132 | 74% | 7.2 | 1 (09-19 20:33Z) |
| us-west-2 | 132 | 50% | 5.6 | 9 (09-19 20:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999964999339992499941999933999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999999918999929999399992399999999
ap-southeast-2   333333333332233222222222222233222332222332333333
ap-southeast-3   333333333333333331313313133133333131311233333333
us-east-1        234999999999999999436844324939559956999945499999
us-east-2        191999999999999999999999212999999999999991199991
us-west-2        335399999999999999934254335344139944595334599999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 3 | 4 | 9 | 3 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 3 | 6 | 7 | 6 | 6 | 5 | 5 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 6 | 5 | 6 | 5 | 6 | 6 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 7 | 4 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 68 | 88% | 8.3 | 9 (09-19 20:33Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 88 | 100% | 9.0 | 9 (09-19 20:33Z) |
| ap-northeast-2 apne2-az1 | 121 | 100% | 9.0 | 9 (09-19 20:33Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 120 | 100% | 9.0 | 9 (09-19 14:20Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 40 | 45% | 5.7 | 9 (09-19 20:33Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 53 | 66% | 7.0 | 9 (09-19 20:33Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 52 | 100% | 9.0 | 9 (09-19 20:33Z) |
| us-east-1 use1-az4 | 55 | 96% | 8.7 | 9 (09-19 20:33Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 51 | 100% | 9.0 | 9 (09-19 14:20Z) |
| us-east-2 use2-az1 | 52 | 100% | 9.0 | 9 (09-19 10:50Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 66 | 88% | 8.2 | 9 (09-19 17:57Z) |
| us-west-2 usw2-az1 | 45 | 98% | 8.9 | 9 (09-19 20:33Z) |
| us-west-2 usw2-az2 | 34 | 97% | 8.7 | 9 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 46 | 98% | 8.8 | 9 (09-19 20:33Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712700 | 2026-09-19T20:33:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-19T20:33:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.844700 | 2026-09-19T20:33:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.025700 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588600 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579200 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565900 | 2026-09-19T20:33:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-09-19T20:33:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.497500 | 2026-09-19T20:33:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.308300 | 2026-09-19T20:33:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.452900 | 2026-09-19T20:33:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.316600 | 2026-09-19T20:33:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.687800 | 2026-09-19T20:33:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513100 | 2026-09-19T20:33:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.847200 | 2026-09-19T20:33:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.841000 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1a | Windows | 0.348300 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.624300 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1b | Windows | 0.314100 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.507100 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1c | Windows | 0.294700 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.518800 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1d | Windows | 0.309100 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.511400 | 2026-09-19T20:33:05Z |
| us-east-1 | us-east-1f | Windows | 0.316900 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521600 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.521800 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2b | Windows | 0.641700 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515600 | 2026-09-19T20:33:05Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.570800 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2a | Windows | 0.339700 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526000 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2b | Windows | 0.336400 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527700 | 2026-09-19T20:33:05Z |
| us-west-2 | us-west-2c | Windows | 0.336800 | 2026-09-19T20:33:05Z |
