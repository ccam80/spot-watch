# Spot placement score log

Generated 2026-09-08 18:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 68 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-northeast-1 | 68 | 0% | 1.7 | 2 (09-08 18:34Z) |
| ap-northeast-2 | 68 | 0% | 2.9 | 3 (09-08 18:34Z) |
| ap-south-1 | 68 | 0% | 2.1 | 1 (09-08 18:34Z) |
| ap-southeast-2 | 68 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-southeast-3 | 68 | 0% | 2.5 | 3 (09-08 18:34Z) |
| us-east-1 | 68 | 0% | 1.9 | 3 (09-08 18:34Z) |
| us-east-2 | 68 | 0% | 1.4 | 1 (09-08 18:34Z) |
| us-west-2 | 68 | 0% | 1.5 | 1 (09-08 18:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   111111111311211112211311333311333331221111222112
ap-northeast-2   333333113333333333333333333333333333333333333333
ap-south-1       131113122213322113332233333323333111211113111221
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   233333333333331313131333333331133333333133332123
us-east-1        111111111111112212333211313233332323233323223333
us-east-2        111111113111111111111111111311111331111311133331
us-west-2        111111111111211122222222222111111111111112133111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 2 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 22 | 0% | 1.0 | 1 (09-07 20:30Z) |
| ap-east-1 ape1-az2 | 22 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-northeast-1 apne1-az1 | 14 | 0% | 1.1 | 1 (09-08 18:34Z) |
| ap-northeast-1 apne1-az4 | 37 | 0% | 2.1 | 2 (09-07 20:30Z) |
| ap-northeast-2 apne2-az1 | 64 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-northeast-2 apne2-az3 | 61 | 0% | 2.9 | 3 (09-08 18:34Z) |
| ap-northeast-2 apne2-az4 | 67 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-south-1 aps1-az1 | 28 | 0% | 1.7 | 1 (09-08 09:34Z) |
| ap-south-1 aps1-az3 | 44 | 0% | 2.5 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 17 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 14 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 apse3-az3 | 55 | 0% | 2.9 | 3 (09-08 18:34Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 22 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 21 | 0% | 1.3 | 1 (09-08 18:34Z) |
| us-east-1 use1-az6 | 30 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az1 | 14 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az2 | 25 | 0% | 1.5 | 3 (09-08 14:27Z) |
| us-east-2 use2-az3 | 27 | 0% | 1.9 | 1 (09-08 18:34Z) |
| us-west-2 usw2-az1 | 14 | 0% | 1.6 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 33 | 0% | 1.4 | 1 (09-08 09:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 68 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-northeast-1 | 68 | 79% | 7.5 | 9 (09-08 18:34Z) |
| ap-northeast-2 | 68 | 100% | 9.0 | 9 (09-08 18:34Z) |
| ap-south-1 | 68 | 1% | 2.9 | 9 (09-08 18:34Z) |
| ap-southeast-2 | 68 | 15% | 2.9 | 3 (09-08 18:34Z) |
| ap-southeast-3 | 68 | 0% | 2.5 | 3 (09-08 18:34Z) |
| us-east-1 | 68 | 75% | 6.6 | 4 (09-08 18:34Z) |
| us-east-2 | 68 | 69% | 6.8 | 9 (09-08 18:34Z) |
| us-west-2 | 68 | 51% | 5.7 | 4 (09-08 18:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   911999911999921999912999999999999999999129994399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       331133333333332233333333333333333333333333333339
ap-southeast-2   111231111131111333111331333333333333331113111133
ap-southeast-3   233333333333331313131333333331133333333133332123
us-east-1        119112199211399433565425659959999999999999999954
us-east-2        119999999911399333239338299999999999999999999999
us-west-2        129924492921242944344534544998589699997199999994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 8 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 20 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 29 | 72% | 7.3 | 9 (09-08 18:34Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 51 | 100% | 9.0 | 9 (09-08 18:34Z) |
| ap-northeast-2 apne2-az1 | 64 | 100% | 9.0 | 9 (09-08 18:34Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 64 | 100% | 9.0 | 9 (09-08 18:34Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 13 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-south-1 aps1-az2 | 23 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-south-1 aps1-az3 | 13 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 7 | 0% | 3.0 | 3 (09-08 18:34Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 27 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az4 | 28 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 30 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-2 use2-az1 | 27 | 100% | 9.0 | 9 (09-08 14:27Z) |
| us-east-2 use2-az2 | 43 | 95% | 8.7 | 9 (09-08 18:34Z) |
| us-east-2 use2-az3 | 23 | 65% | 6.7 | 9 (09-08 18:34Z) |
| us-west-2 usw2-az1 | 26 | 96% | 8.8 | 9 (09-08 14:27Z) |
| us-west-2 usw2-az2 | 17 | 94% | 8.7 | 9 (09-08 04:26Z) |
| us-west-2 usw2-az3 | 26 | 96% | 8.7 | 9 (09-08 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.747400 | 2026-09-08T18:34:15Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-08T18:34:15Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.784700 | 2026-09-08T18:34:15Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.953100 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597300 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585700 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578800 | 2026-09-08T18:34:15Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-08T18:34:15Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.543900 | 2026-09-08T18:34:15Z |
| ap-south-1 | ap-south-1a | Windows | 0.325000 | 2026-09-08T18:34:15Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.493300 | 2026-09-08T18:34:15Z |
| ap-south-1 | ap-south-1b | Windows | 0.327000 | 2026-09-08T18:34:15Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750500 | 2026-09-08T18:34:15Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-09-08T18:34:15Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.899100 | 2026-09-08T18:34:15Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.407700 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.918300 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1a | Windows | 0.357800 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.699300 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1b | Windows | 0.319800 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.592100 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1c | Windows | 0.315700 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.509200 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1d | Windows | 0.321900 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.555200 | 2026-09-08T18:34:15Z |
| us-east-1 | us-east-1f | Windows | 0.318400 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.541500 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.538200 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526100 | 2026-09-08T18:34:15Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.577300 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2a | Windows | 0.303800 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.543100 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2b | Windows | 0.313400 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.534200 | 2026-09-08T18:34:15Z |
| us-west-2 | us-west-2c | Windows | 0.335400 | 2026-09-08T18:34:15Z |
