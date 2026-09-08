# Spot placement score log

Generated 2026-09-08 09:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 66 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-northeast-1 | 66 | 0% | 1.7 | 1 (09-08 09:34Z) |
| ap-northeast-2 | 66 | 0% | 2.9 | 3 (09-08 09:34Z) |
| ap-south-1 | 66 | 0% | 2.2 | 2 (09-08 09:34Z) |
| ap-southeast-2 | 66 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 | 66 | 0% | 2.5 | 1 (09-08 09:34Z) |
| us-east-1 | 66 | 0% | 1.9 | 3 (09-08 09:34Z) |
| us-east-2 | 66 | 0% | 1.4 | 3 (09-08 09:34Z) |
| us-west-2 | 66 | 0% | 1.5 | 1 (09-08 09:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   131111111113112111122113113333113333312211112221
ap-northeast-2   333333331133333333333333333333333333333333333333
ap-south-1       111311131222133221133322333333233331112111131112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   112333333333333313131313333333311333333331333321
us-east-1        121111111111111122123332113132333323232333232233
us-east-2        111111111131111111111111111113111113311113111333
us-west-2        311111111111112111222222222221111111111111121331
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 2 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 22 | 0% | 1.0 | 1 (09-07 20:30Z) |
| ap-east-1 ape1-az2 | 20 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-northeast-1 apne1-az1 | 12 | 0% | 1.2 | 1 (09-07 10:10Z) |
| ap-northeast-1 apne1-az4 | 37 | 0% | 2.1 | 2 (09-07 20:30Z) |
| ap-northeast-2 apne2-az1 | 62 | 0% | 3.0 | 2 (09-08 09:34Z) |
| ap-northeast-2 apne2-az3 | 59 | 0% | 2.9 | 3 (09-08 04:26Z) |
| ap-northeast-2 apne2-az4 | 65 | 0% | 3.0 | 3 (09-08 09:34Z) |
| ap-south-1 aps1-az1 | 28 | 0% | 1.7 | 1 (09-08 09:34Z) |
| ap-south-1 aps1-az3 | 42 | 0% | 2.6 | 1 (09-07 23:27Z) |
| ap-southeast-2 apse2-az1 | 15 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 14 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 apse3-az3 | 53 | 0% | 2.9 | 2 (09-08 04:26Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 22 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 20 | 0% | 1.3 | 3 (09-08 04:26Z) |
| us-east-1 use1-az6 | 30 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az1 | 14 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az2 | 24 | 0% | 1.5 | 3 (09-08 09:34Z) |
| us-east-2 use2-az3 | 25 | 0% | 1.9 | 3 (09-08 09:34Z) |
| us-west-2 usw2-az1 | 14 | 0% | 1.6 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 33 | 0% | 1.4 | 1 (09-08 09:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 66 | 0% | 3.0 | 3 (09-08 09:34Z) |
| ap-northeast-1 | 66 | 79% | 7.4 | 3 (09-08 09:34Z) |
| ap-northeast-2 | 66 | 100% | 9.0 | 9 (09-08 09:34Z) |
| ap-south-1 | 66 | 0% | 2.8 | 3 (09-08 09:34Z) |
| ap-southeast-2 | 66 | 15% | 2.9 | 1 (09-08 09:34Z) |
| ap-southeast-3 | 66 | 0% | 2.5 | 1 (09-08 09:34Z) |
| us-east-1 | 66 | 76% | 6.7 | 9 (09-08 09:34Z) |
| us-east-2 | 66 | 68% | 6.7 | 9 (09-08 09:34Z) |
| us-west-2 | 66 | 52% | 5.7 | 9 (09-08 09:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   199119999119999219999129999999999999999991299943
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       133311333333333322333333333333333333333333333333
ap-southeast-2   111112311111311113331113313333333333333311131111
ap-southeast-3   112333333333333313131313333333311333333331333321
us-east-1        941191121992113994335654256599599999999999999999
us-east-2        911199999999113993332393382999999999999999999999
us-west-2        991299244929212429443445345449985896999971999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 7 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 19 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 27 | 70% | 7.2 | 9 (09-07 23:27Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 49 | 100% | 9.0 | 9 (09-07 23:27Z) |
| ap-northeast-2 apne2-az1 | 62 | 100% | 9.0 | 9 (09-08 09:34Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 62 | 100% | 9.0 | 9 (09-08 09:34Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 12 | 0% | 3.0 | 3 (09-07 20:30Z) |
| ap-south-1 aps1-az2 | 23 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 27 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az4 | 28 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 30 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-2 use2-az1 | 26 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-2 use2-az2 | 41 | 95% | 8.6 | 9 (09-08 09:34Z) |
| us-east-2 use2-az3 | 21 | 62% | 6.5 | 9 (09-08 09:34Z) |
| us-west-2 usw2-az1 | 25 | 96% | 8.8 | 9 (09-08 09:34Z) |
| us-west-2 usw2-az2 | 17 | 94% | 8.7 | 9 (09-08 04:26Z) |
| us-west-2 usw2-az3 | 25 | 96% | 8.7 | 9 (09-08 09:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.750000 | 2026-09-08T09:34:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-08T09:34:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.786100 | 2026-09-08T09:34:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956200 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597600 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585400 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579400 | 2026-09-08T09:34:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-08T09:34:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548900 | 2026-09-08T09:34:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.325100 | 2026-09-08T09:34:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.493800 | 2026-09-08T09:34:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.327300 | 2026-09-08T09:34:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750500 | 2026-09-08T09:34:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-09-08T09:34:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.911500 | 2026-09-08T09:34:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.408800 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.916300 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1a | Windows | 0.359000 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.680500 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1b | Windows | 0.319800 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.584900 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1c | Windows | 0.315500 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.502700 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1d | Windows | 0.319200 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.530800 | 2026-09-08T09:34:32Z |
| us-east-1 | us-east-1f | Windows | 0.318200 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.522500 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2a | Windows | 0.637700 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525900 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.524500 | 2026-09-08T09:34:32Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579200 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2a | Windows | 0.301500 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.539800 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2b | Windows | 0.311400 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.532200 | 2026-09-08T09:34:32Z |
| us-west-2 | us-west-2c | Windows | 0.335100 | 2026-09-08T09:34:32Z |
