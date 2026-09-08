# Spot placement score log

Generated 2026-09-08 21:48 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 69 | 0% | 1.0 | 1 (09-08 21:48Z) |
| ap-northeast-1 | 69 | 0% | 1.7 | 3 (09-08 21:48Z) |
| ap-northeast-2 | 69 | 0% | 2.9 | 3 (09-08 21:48Z) |
| ap-south-1 | 69 | 0% | 2.1 | 1 (09-08 21:48Z) |
| ap-southeast-2 | 69 | 0% | 1.0 | 1 (09-08 21:48Z) |
| ap-southeast-3 | 69 | 0% | 2.5 | 3 (09-08 21:48Z) |
| us-east-1 | 69 | 0% | 1.9 | 2 (09-08 21:48Z) |
| us-east-2 | 69 | 0% | 1.4 | 1 (09-08 21:48Z) |
| us-west-2 | 69 | 0% | 1.5 | 1 (09-08 21:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   111111113112111122113113333113333312211112221123
ap-northeast-2   333331133333333333333333333333333333333333333333
ap-south-1       311131222133221133322333333233331112111131112211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333333313131313333333311333333331333321233
us-east-1        111111111111122123332113132333323232333232233332
us-east-2        111111131111111111111111113111113311113111333311
us-west-2        111111111112111222222222221111111111111121331111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 2 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 23 | 0% | 1.0 | 1 (09-08 21:48Z) |
| ap-east-1 ape1-az2 | 23 | 0% | 1.0 | 1 (09-08 21:48Z) |
| ap-northeast-1 apne1-az1 | 14 | 0% | 1.1 | 1 (09-08 18:34Z) |
| ap-northeast-1 apne1-az4 | 38 | 0% | 2.1 | 2 (09-08 21:48Z) |
| ap-northeast-2 apne2-az1 | 65 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-northeast-2 apne2-az3 | 62 | 0% | 2.9 | 3 (09-08 21:48Z) |
| ap-northeast-2 apne2-az4 | 68 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az1 | 28 | 0% | 1.7 | 1 (09-08 09:34Z) |
| ap-south-1 aps1-az3 | 44 | 0% | 2.5 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 17 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 14 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 apse3-az3 | 56 | 0% | 2.9 | 3 (09-08 21:48Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 22 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 22 | 0% | 1.3 | 1 (09-08 21:48Z) |
| us-east-1 use1-az6 | 30 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az1 | 14 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az2 | 25 | 0% | 1.5 | 3 (09-08 14:27Z) |
| us-east-2 use2-az3 | 28 | 0% | 1.9 | 1 (09-08 21:48Z) |
| us-west-2 usw2-az1 | 15 | 0% | 1.5 | 1 (09-08 21:48Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 33 | 0% | 1.4 | 1 (09-08 09:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 69 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-northeast-1 | 69 | 80% | 7.5 | 9 (09-08 21:48Z) |
| ap-northeast-2 | 69 | 100% | 9.0 | 9 (09-08 21:48Z) |
| ap-south-1 | 69 | 3% | 3.0 | 9 (09-08 21:48Z) |
| ap-southeast-2 | 69 | 14% | 2.9 | 1 (09-08 21:48Z) |
| ap-southeast-3 | 69 | 0% | 2.5 | 3 (09-08 21:48Z) |
| us-east-1 | 69 | 74% | 6.6 | 4 (09-08 21:48Z) |
| us-east-2 | 69 | 70% | 6.8 | 9 (09-08 21:48Z) |
| us-west-2 | 69 | 51% | 5.7 | 4 (09-08 21:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   119999119999219999129999999999999999991299943999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       311333333333322333333333333333333333333333333399
ap-southeast-2   112311111311113331113313333333333333311131111331
ap-southeast-3   333333333333313131313333333311333333331333321233
us-east-1        191121992113994335654256599599999999999999999544
us-east-2        199999999113993332393382999999999999999999999999
us-west-2        299244929212429443445345449985896999971999999944
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 8 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-east-1 ape1-az2 | 20 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-east-1 ape1-az3 | 22 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-northeast-1 apne1-az1 | 30 | 73% | 7.4 | 9 (09-08 21:48Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 52 | 100% | 9.0 | 9 (09-08 21:48Z) |
| ap-northeast-2 apne2-az1 | 65 | 100% | 9.0 | 9 (09-08 21:48Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 65 | 100% | 9.0 | 9 (09-08 21:48Z) |
| ap-northeast-2 apne2-az4 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az1 | 13 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-south-1 aps1-az2 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az3 | 13 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 7 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-southeast-3 apse3-az3 | 22 | 0% | 3.0 | 3 (09-08 21:48Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 27 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az4 | 28 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 30 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-2 use2-az1 | 27 | 100% | 9.0 | 9 (09-08 14:27Z) |
| us-east-2 use2-az2 | 43 | 95% | 8.7 | 9 (09-08 18:34Z) |
| us-east-2 use2-az3 | 24 | 67% | 6.8 | 8 (09-08 21:48Z) |
| us-west-2 usw2-az1 | 26 | 96% | 8.8 | 9 (09-08 14:27Z) |
| us-west-2 usw2-az2 | 17 | 94% | 8.7 | 9 (09-08 04:26Z) |
| us-west-2 usw2-az3 | 26 | 96% | 8.7 | 9 (09-08 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.747400 | 2026-09-08T21:48:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-08T21:48:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.784400 | 2026-09-08T21:48:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956100 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596900 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585200 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578000 | 2026-09-08T21:48:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-08T21:48:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.543900 | 2026-09-08T21:48:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.325100 | 2026-09-08T21:48:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.493300 | 2026-09-08T21:48:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.327000 | 2026-09-08T21:48:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750500 | 2026-09-08T21:48:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509000 | 2026-09-08T21:48:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.899100 | 2026-09-08T21:48:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.407700 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.914800 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1a | Windows | 0.360000 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.699300 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1b | Windows | 0.319800 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.595300 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1c | Windows | 0.316900 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.509200 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1d | Windows | 0.322900 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.555200 | 2026-09-08T21:48:06Z |
| us-east-1 | us-east-1f | Windows | 0.319000 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.541500 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.538200 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.527100 | 2026-09-08T21:48:06Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.577300 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2a | Windows | 0.306600 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.549500 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2b | Windows | 0.313700 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535500 | 2026-09-08T21:48:06Z |
| us-west-2 | us-west-2c | Windows | 0.336100 | 2026-09-08T21:48:06Z |
