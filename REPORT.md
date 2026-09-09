# Spot placement score log

Generated 2026-09-09 04:36 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 71 | 0% | 1.0 | 1 (09-09 04:36Z) |
| ap-northeast-1 | 71 | 0% | 1.7 | 2 (09-09 04:36Z) |
| ap-northeast-2 | 71 | 0% | 2.9 | 3 (09-09 04:36Z) |
| ap-south-1 | 71 | 0% | 2.1 | 1 (09-09 04:36Z) |
| ap-southeast-2 | 71 | 0% | 1.0 | 1 (09-09 04:36Z) |
| ap-southeast-3 | 71 | 0% | 2.5 | 1 (09-09 04:36Z) |
| us-east-1 | 71 | 0% | 1.9 | 1 (09-09 04:36Z) |
| us-east-2 | 71 | 0% | 1.4 | 3 (09-09 04:36Z) |
| us-west-2 | 71 | 0% | 1.5 | 1 (09-09 04:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   111111311211112211311333311333331221111222112322
ap-northeast-2   333113333333333333333333333333333333333333333333
ap-south-1       113122213322113332233333323333111211113111221111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333331313131333333331133333333133332123331
us-east-1        111111111112212333211313233332323233323223333211
us-east-2        111113111111111111111111311111331111311133331133
us-west-2        111111111211122222222222111111111111112133111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 24 | 0% | 1.0 | 1 (09-09 04:36Z) |
| ap-east-1 ape1-az2 | 24 | 0% | 1.0 | 1 (09-09 04:36Z) |
| ap-northeast-1 apne1-az1 | 14 | 0% | 1.1 | 1 (09-08 18:34Z) |
| ap-northeast-1 apne1-az4 | 39 | 0% | 2.1 | 1 (09-09 04:36Z) |
| ap-northeast-2 apne2-az1 | 67 | 0% | 2.9 | 1 (09-09 04:36Z) |
| ap-northeast-2 apne2-az3 | 63 | 0% | 2.9 | 3 (09-09 00:06Z) |
| ap-northeast-2 apne2-az4 | 70 | 0% | 3.0 | 3 (09-09 04:36Z) |
| ap-south-1 aps1-az1 | 29 | 0% | 1.7 | 1 (09-09 00:06Z) |
| ap-south-1 aps1-az3 | 44 | 0% | 2.5 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 17 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 14 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 apse3-az3 | 57 | 0% | 2.9 | 3 (09-09 00:06Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 23 | 0% | 1.1 | 1 (09-09 04:36Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 23 | 0% | 1.3 | 1 (09-09 04:36Z) |
| us-east-1 use1-az6 | 31 | 0% | 1.1 | 1 (09-09 00:06Z) |
| us-east-2 use2-az1 | 15 | 0% | 1.1 | 1 (09-09 00:06Z) |
| us-east-2 use2-az2 | 27 | 0% | 1.6 | 3 (09-09 04:36Z) |
| us-east-2 use2-az3 | 30 | 0% | 2.0 | 3 (09-09 04:36Z) |
| us-west-2 usw2-az1 | 16 | 0% | 1.5 | 1 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 34 | 0% | 1.4 | 1 (09-09 00:06Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 71 | 0% | 3.0 | 3 (09-09 04:36Z) |
| ap-northeast-1 | 71 | 79% | 7.5 | 3 (09-09 04:36Z) |
| ap-northeast-2 | 71 | 100% | 9.0 | 9 (09-09 04:36Z) |
| ap-south-1 | 71 | 6% | 3.2 | 9 (09-09 04:36Z) |
| ap-southeast-2 | 71 | 14% | 2.8 | 1 (09-09 04:36Z) |
| ap-southeast-3 | 71 | 0% | 2.5 | 1 (09-09 04:36Z) |
| us-east-1 | 71 | 75% | 6.6 | 9 (09-09 04:36Z) |
| us-east-2 | 71 | 70% | 6.9 | 9 (09-09 04:36Z) |
| us-west-2 | 71 | 51% | 5.7 | 9 (09-09 04:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999911999921999912999999999999999999129994399993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       133333333332233333333333333333333333333333339999
ap-southeast-2   231111131111333111331333333333333331113111133111
ap-southeast-3   333333333331313131333333331133333333133332123331
us-east-1        112199211399433565425659959999999999999999954459
us-east-2        999999911399333239338299999999999999999999999999
us-west-2        924492921242944344534544998589699997199999994429
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 7 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 4 | 3 | · | 3 | 4 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 6 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 8 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-east-1 ape1-az2 | 21 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-east-1 ape1-az3 | 22 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-northeast-1 apne1-az1 | 30 | 73% | 7.4 | 9 (09-08 21:48Z) |
| ap-northeast-1 apne1-az2 | 17 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-northeast-1 apne1-az4 | 52 | 100% | 9.0 | 9 (09-08 21:48Z) |
| ap-northeast-2 apne2-az1 | 67 | 100% | 9.0 | 9 (09-09 04:36Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 67 | 100% | 9.0 | 9 (09-09 04:36Z) |
| ap-northeast-2 apne2-az4 | 25 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-south-1 aps1-az1 | 14 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-south-1 aps1-az2 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az3 | 14 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 7 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-southeast-3 apse3-az3 | 23 | 0% | 3.0 | 3 (09-09 00:06Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 28 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az4 | 29 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 31 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-2 use2-az1 | 27 | 100% | 9.0 | 9 (09-08 14:27Z) |
| us-east-2 use2-az2 | 45 | 96% | 8.7 | 9 (09-09 04:36Z) |
| us-east-2 use2-az3 | 26 | 69% | 7.0 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.747700 | 2026-09-09T04:36:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-09T04:36:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.784400 | 2026-09-09T04:36:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956100 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596300 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585200 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578000 | 2026-09-09T04:36:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-09T04:36:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.546400 | 2026-09-09T04:36:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.325200 | 2026-09-09T04:36:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.492400 | 2026-09-09T04:36:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.327300 | 2026-09-09T04:36:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.755900 | 2026-09-09T04:36:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-09-09T04:36:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.893800 | 2026-09-09T04:36:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.408900 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.913100 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1a | Windows | 0.358000 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.707900 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1b | Windows | 0.320100 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.608700 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1c | Windows | 0.317000 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520600 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1d | Windows | 0.323600 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.556000 | 2026-09-09T04:36:44Z |
| us-east-1 | us-east-1f | Windows | 0.319000 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.547000 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.539300 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.534000 | 2026-09-09T04:36:44Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.578400 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2a | Windows | 0.306600 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.553300 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2b | Windows | 0.313800 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.536800 | 2026-09-09T04:36:44Z |
| us-west-2 | us-west-2c | Windows | 0.339400 | 2026-09-09T04:36:44Z |
