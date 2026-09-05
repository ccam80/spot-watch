# Spot placement score log

Generated 2026-09-05 21:09 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 51 | 0% | 1.0 | 1 (09-05 21:09Z) |
| ap-northeast-1 | 51 | 0% | 1.7 | 3 (09-05 21:09Z) |
| ap-northeast-2 | 51 | 0% | 2.9 | 3 (09-05 21:09Z) |
| ap-south-1 | 51 | 0% | 2.3 | 3 (09-05 21:09Z) |
| ap-southeast-2 | 51 | 0% | 1.0 | 1 (09-05 21:09Z) |
| ap-southeast-3 | 51 | 0% | 2.5 | 1 (09-05 21:09Z) |
| us-east-1 | 51 | 0% | 1.7 | 3 (09-05 21:09Z) |
| us-east-2 | 51 | 0% | 1.2 | 1 (09-05 21:09Z) |
| us-west-2 | 51 | 0% | 1.5 | 1 (09-05 21:09Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   311333313313111131111111113112111122113113333113
ap-northeast-2   333333333333333333333331133333333333333333333333
ap-south-1       131333333313333111311131222133221133322333333233
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333332323211132112333333333333313131313333333311
us-east-1        332111131111113121111111111111122123332113132333
us-east-2        113113111133111111111111131111111111111111113111
us-west-2        222113111113133311111111111112111222222222221111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 20 | 0% | 1.0 | 1 (09-05 18:11Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 31 | 0% | 2.0 | 3 (09-05 21:09Z) |
| ap-northeast-2 apne2-az1 | 47 | 0% | 3.0 | 3 (09-05 21:09Z) |
| ap-northeast-2 apne2-az3 | 47 | 0% | 2.9 | 3 (09-05 21:09Z) |
| ap-northeast-2 apne2-az4 | 50 | 0% | 3.0 | 3 (09-05 21:09Z) |
| ap-south-1 aps1-az1 | 22 | 0% | 1.8 | 1 (09-05 21:09Z) |
| ap-south-1 aps1-az3 | 35 | 0% | 2.7 | 3 (09-05 21:09Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 8 | 0% | 1.0 | 1 (09-05 08:59Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 2.9 | 3 (09-05 15:59Z) |
| us-east-1 use1-az1 | 9 | 0% | 1.0 | 1 (09-05 08:59Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 10 | 0% | 1.4 | 1 (09-05 08:59Z) |
| us-east-1 use1-az5 | 16 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-east-1 use1-az6 | 23 | 0% | 1.2 | 1 (09-05 21:09Z) |
| us-east-2 use2-az1 | 10 | 0% | 1.2 | 1 (09-05 21:09Z) |
| us-east-2 use2-az2 | 17 | 0% | 1.1 | 1 (09-05 21:09Z) |
| us-east-2 use2-az3 | 15 | 0% | 1.7 | 3 (09-05 12:37Z) |
| us-west-2 usw2-az1 | 11 | 0% | 1.5 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 24 | 0% | 1.3 | 1 (09-05 21:09Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 51 | 0% | 3.0 | 3 (09-05 21:09Z) |
| ap-northeast-1 | 51 | 80% | 7.5 | 9 (09-05 21:09Z) |
| ap-northeast-2 | 51 | 100% | 9.0 | 9 (09-05 21:09Z) |
| ap-south-1 | 51 | 0% | 2.8 | 3 (09-05 21:09Z) |
| ap-southeast-2 | 51 | 20% | 3.1 | 3 (09-05 21:09Z) |
| ap-southeast-3 | 51 | 0% | 2.5 | 1 (09-05 21:09Z) |
| us-east-1 | 51 | 69% | 6.0 | 9 (09-05 21:09Z) |
| us-east-2 | 51 | 59% | 6.1 | 9 (09-05 21:09Z) |
| us-west-2 | 51 | 39% | 5.0 | 5 (09-05 21:09Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999199119999119999219999129999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       133333333333333133311333333333322333333333333333
ap-southeast-2   111979999999931111112311111311113331113313333333
ap-southeast-3   333332323211132112333333333333313131313333333311
us-east-1        787589999999999941191121992113994335654256599599
us-east-2        919299999199221911199999999113993332393382999999
us-west-2        439219222299999991299244929212429443445345449985
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 2 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 6 | 1 | · | 5 | 2 | · | 3 | 2 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 7 | · | 9 | · | 9 | 8 | · | 8 | 5 | · | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 6 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 5 | 2 | 2 | 4 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 18 | 56% | 6.3 | 9 (09-05 21:09Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 39 | 100% | 9.0 | 9 (09-05 21:09Z) |
| ap-northeast-2 apne2-az1 | 50 | 100% | 9.0 | 9 (09-05 21:09Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 49 | 100% | 9.0 | 9 (09-05 21:09Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 14 | 100% | 8.9 | 9 (09-05 21:09Z) |
| us-east-1 use1-az4 | 15 | 100% | 9.0 | 9 (09-05 21:09Z) |
| us-east-1 use1-az5 | 18 | 100% | 8.9 | 9 (09-05 21:09Z) |
| us-east-1 use1-az6 | 15 | 100% | 9.0 | 9 (09-05 21:09Z) |
| us-east-2 use2-az1 | 17 | 100% | 8.9 | 9 (09-05 21:09Z) |
| us-east-2 use2-az2 | 27 | 93% | 8.4 | 9 (09-05 21:09Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 14 | 93% | 8.6 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az2 | 11 | 100% | 9.0 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az3 | 15 | 93% | 8.5 | 9 (09-05 15:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.752900 | 2026-09-05T21:09:10Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-05T21:09:10Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.780400 | 2026-09-05T21:09:10Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.932200 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.577600 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.571700 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.580100 | 2026-09-05T21:09:10Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-05T21:09:10Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.555500 | 2026-09-05T21:09:10Z |
| ap-south-1 | ap-south-1a | Windows | 0.316000 | 2026-09-05T21:09:10Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.496400 | 2026-09-05T21:09:10Z |
| ap-south-1 | ap-south-1b | Windows | 0.320200 | 2026-09-05T21:09:10Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747100 | 2026-09-05T21:09:10Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.479700 | 2026-09-05T21:09:10Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.934800 | 2026-09-05T21:09:10Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.379300 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.915800 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1a | Windows | 0.332600 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.667100 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1b | Windows | 0.318800 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.559800 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1c | Windows | 0.315200 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.468400 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1d | Windows | 0.316200 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.504400 | 2026-09-05T21:09:10Z |
| us-east-1 | us-east-1f | Windows | 0.315200 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.469100 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.482600 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.476200 | 2026-09-05T21:09:10Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556500 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2a | Windows | 0.291600 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.518000 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2b | Windows | 0.296800 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.519300 | 2026-09-05T21:09:10Z |
| us-west-2 | us-west-2c | Windows | 0.333400 | 2026-09-05T21:09:10Z |
