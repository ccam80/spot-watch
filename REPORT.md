# Spot placement score log

Generated 2026-09-21 06:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 141 | 0% | 1.9 | 3 (09-21 06:13Z) |
| ap-northeast-1 | 141 | 0% | 1.9 | 1 (09-21 06:13Z) |
| ap-northeast-2 | 141 | 0% | 3.0 | 3 (09-21 06:13Z) |
| ap-south-1 | 141 | 0% | 2.1 | 1 (09-21 06:13Z) |
| ap-southeast-2 | 141 | 0% | 1.0 | 1 (09-21 06:13Z) |
| ap-southeast-3 | 141 | 0% | 2.5 | 1 (09-21 06:13Z) |
| us-east-1 | 141 | 0% | 2.0 | 3 (09-21 06:13Z) |
| us-east-2 | 141 | 0% | 1.8 | 3 (09-21 06:13Z) |
| us-west-2 | 141 | 0% | 1.7 | 3 (09-21 06:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333333322332113221222211222211122122332231232211
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       331333333333111112112211133331131211333333333321
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333331313313133133333131311233333333333133331
us-east-1        132323322222212211311212322312311121311223333333
us-east-2        333333333311111111313133333331331133331233333313
us-west-2        331333333311121112111111312213111233333333333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 42 | 0% | 1.5 | 3 (09-21 00:10Z) |
| ap-east-1 ape1-az2 | 83 | 0% | 2.4 | 3 (09-21 06:13Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 124 | 0% | 2.9 | 3 (09-20 18:43Z) |
| ap-northeast-2 apne2-az3 | 123 | 0% | 2.9 | 3 (09-20 21:28Z) |
| ap-northeast-2 apne2-az4 | 138 | 0% | 3.0 | 3 (09-21 06:13Z) |
| ap-south-1 aps1-az1 | 55 | 0% | 1.7 | 3 (09-20 18:43Z) |
| ap-south-1 aps1-az3 | 78 | 0% | 2.6 | 3 (09-20 21:28Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 106 | 0% | 2.9 | 3 (09-21 00:10Z) |
| us-east-1 use1-az1 | 17 | 0% | 1.4 | 3 (09-20 21:28Z) |
| us-east-1 use1-az2 | 46 | 0% | 1.4 | 3 (09-21 06:13Z) |
| us-east-1 use1-az4 | 32 | 0% | 1.7 | 3 (09-21 06:13Z) |
| us-east-1 use1-az5 | 41 | 0% | 1.6 | 3 (09-21 06:13Z) |
| us-east-1 use1-az6 | 47 | 0% | 1.3 | 3 (09-21 06:13Z) |
| us-east-2 use2-az1 | 47 | 0% | 1.8 | 3 (09-21 06:13Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 75 | 0% | 2.3 | 3 (09-21 06:13Z) |
| us-west-2 usw2-az1 | 43 | 0% | 2.1 | 3 (09-21 06:13Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 75 | 0% | 1.8 | 3 (09-21 06:13Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 141 | 0% | 3.0 | 3 (09-21 06:13Z) |
| ap-northeast-1 | 141 | 78% | 7.5 | 9 (09-21 06:13Z) |
| ap-northeast-2 | 141 | 100% | 9.0 | 9 (09-21 06:13Z) |
| ap-south-1 | 141 | 44% | 5.5 | 9 (09-21 06:13Z) |
| ap-southeast-2 | 141 | 7% | 2.6 | 2 (09-21 06:13Z) |
| ap-southeast-3 | 141 | 0% | 2.5 | 1 (09-21 06:13Z) |
| us-east-1 | 141 | 75% | 6.9 | 9 (09-21 06:13Z) |
| us-east-2 | 141 | 76% | 7.3 | 9 (09-21 06:13Z) |
| us-west-2 | 141 | 53% | 5.8 | 9 (09-21 06:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999964999339992499941999933999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999918999929999399992399999999999999999
ap-southeast-2   332233222222222222233222332222332333333333333322
ap-southeast-3   333333331313313133133333131311233333333333133331
us-east-1        999999999436844324939559956999945499999999999999
us-east-2        999999999999999212999999999999991199991999999999
us-west-2        999999999934254335344139944595334599999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 7 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 6 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 72 | 89% | 8.3 | 9 (09-21 00:10Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 95 | 100% | 9.0 | 9 (09-21 06:13Z) |
| ap-northeast-2 apne2-az1 | 127 | 100% | 9.0 | 9 (09-21 06:13Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 127 | 100% | 9.0 | 9 (09-21 06:13Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 43 | 49% | 5.9 | 9 (09-21 00:10Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 59 | 69% | 7.2 | 9 (09-21 00:10Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 60 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-1 use1-az4 | 61 | 97% | 8.8 | 9 (09-21 00:10Z) |
| us-east-1 use1-az5 | 28 | 96% | 8.8 | 9 (09-21 06:13Z) |
| us-east-1 use1-az6 | 57 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-2 use2-az1 | 56 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-2 use2-az2 | 88 | 98% | 8.8 | 9 (09-20 21:28Z) |
| us-east-2 use2-az3 | 73 | 89% | 8.3 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az1 | 49 | 98% | 8.9 | 9 (09-21 00:10Z) |
| us-west-2 usw2-az2 | 40 | 98% | 8.8 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az3 | 54 | 98% | 8.9 | 9 (09-21 06:13Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.720700 | 2026-09-21T06:13:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-21T06:13:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.846700 | 2026-09-21T06:13:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.028700 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590700 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580000 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566600 | 2026-09-21T06:13:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742900 | 2026-09-21T06:13:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.482500 | 2026-09-21T06:13:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-21T06:13:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.446600 | 2026-09-21T06:13:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.314100 | 2026-09-21T06:13:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.691500 | 2026-09-21T06:13:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.528100 | 2026-09-21T06:13:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.827200 | 2026-09-21T06:13:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.838900 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1a | Windows | 0.361200 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.623100 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1b | Windows | 0.305700 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.507800 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1c | Windows | 0.290400 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500300 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1d | Windows | 0.304000 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.481500 | 2026-09-21T06:13:05Z |
| us-east-1 | us-east-1f | Windows | 0.310900 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524700 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2a | Windows | 0.642000 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524500 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2b | Windows | 0.642000 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516100 | 2026-09-21T06:13:05Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.555400 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2a | Windows | 0.338500 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.509600 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2b | Windows | 0.335800 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.517100 | 2026-09-21T06:13:05Z |
| us-west-2 | us-west-2c | Windows | 0.336300 | 2026-09-21T06:13:05Z |
