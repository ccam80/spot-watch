# Spot placement score log

Generated 2026-09-07 16:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 62 | 0% | 1.0 | 1 (09-07 16:24Z) |
| ap-northeast-1 | 62 | 0% | 1.7 | 1 (09-07 16:24Z) |
| ap-northeast-2 | 62 | 0% | 2.9 | 3 (09-07 16:24Z) |
| ap-south-1 | 62 | 0% | 2.2 | 3 (09-07 16:24Z) |
| ap-southeast-2 | 62 | 0% | 1.0 | 1 (09-07 16:24Z) |
| ap-southeast-3 | 62 | 0% | 2.5 | 3 (09-07 16:24Z) |
| us-east-1 | 62 | 0% | 1.9 | 3 (09-07 16:24Z) |
| us-east-2 | 62 | 0% | 1.3 | 1 (09-07 16:24Z) |
| us-west-2 | 62 | 0% | 1.5 | 2 (09-07 16:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   311113111111111311211112211311333311333331221111
ap-northeast-2   333333333333113333333333333333333333333333333333
ap-south-1       333311131113122213322113332233333323333111211113
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   113211233333333333331313131333333331133333333133
us-east-1        111312111111111111112212333211313233332323233323
us-east-2        311111111111113111111111111111111311111331111311
us-west-2        313331111111111111211122222222222111111111111112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 21 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-east-1 ape1-az2 | 19 | 0% | 1.0 | 1 (09-07 10:10Z) |
| ap-northeast-1 apne1-az1 | 12 | 0% | 1.2 | 1 (09-07 10:10Z) |
| ap-northeast-1 apne1-az4 | 36 | 0% | 2.1 | 1 (09-07 16:24Z) |
| ap-northeast-2 apne2-az1 | 58 | 0% | 3.0 | 3 (09-07 16:24Z) |
| ap-northeast-2 apne2-az3 | 58 | 0% | 2.9 | 3 (09-07 16:24Z) |
| ap-northeast-2 apne2-az4 | 61 | 0% | 3.0 | 3 (09-07 16:24Z) |
| ap-south-1 aps1-az1 | 25 | 0% | 1.8 | 3 (09-07 16:24Z) |
| ap-south-1 aps1-az3 | 41 | 0% | 2.6 | 3 (09-07 16:24Z) |
| ap-southeast-2 apse2-az1 | 14 | 0% | 1.0 | 1 (09-07 10:10Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 50 | 0% | 2.9 | 3 (09-07 16:24Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 21 | 0% | 1.1 | 1 (09-05 23:49Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 19 | 0% | 1.2 | 1 (09-07 16:24Z) |
| us-east-1 use1-az6 | 28 | 0% | 1.1 | 1 (09-06 23:47Z) |
| us-east-2 use2-az1 | 11 | 0% | 1.2 | 1 (09-06 21:17Z) |
| us-east-2 use2-az2 | 21 | 0% | 1.4 | 3 (09-07 04:26Z) |
| us-east-2 use2-az3 | 22 | 0% | 1.8 | 1 (09-07 16:24Z) |
| us-west-2 usw2-az1 | 13 | 0% | 1.5 | 1 (09-07 16:24Z) |
| us-west-2 usw2-az2 | 10 | 0% | 1.2 | 1 (09-07 04:26Z) |
| us-west-2 usw2-az3 | 29 | 0% | 1.3 | 1 (09-06 23:47Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 62 | 0% | 3.0 | 3 (09-07 16:24Z) |
| ap-northeast-1 | 62 | 81% | 7.5 | 9 (09-07 16:24Z) |
| ap-northeast-2 | 62 | 100% | 9.0 | 9 (09-07 16:24Z) |
| ap-south-1 | 62 | 0% | 2.8 | 3 (09-07 16:24Z) |
| ap-southeast-2 | 62 | 16% | 3.0 | 3 (09-07 16:24Z) |
| ap-southeast-3 | 62 | 0% | 2.5 | 3 (09-07 16:24Z) |
| us-east-1 | 62 | 74% | 6.5 | 9 (09-07 16:24Z) |
| us-east-2 | 62 | 66% | 6.6 | 9 (09-07 16:24Z) |
| us-west-2 | 62 | 48% | 5.5 | 9 (09-07 16:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999919911999911999921999912999999999999999999129
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333313331133333333332233333333333333333333333333
ap-southeast-2   993111111231111131111333111331333333333333331113
ap-southeast-3   113211233333333333331313131333333331133333333133
us-east-1        999994119112199211399433565425659959999999999999
us-east-2        922191119999999911399333239338299999999999999999
us-west-2        999999129924492921242944344534544998589699997199
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 2 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 6 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 6 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 4 | 9 | 9 | 9 | 9 | 7 | 9 | 7 | 2 | 5 | 6 | 2 | 5 | 3 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 19 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 25 | 68% | 7.1 | 9 (09-07 16:24Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 47 | 100% | 9.0 | 9 (09-07 16:24Z) |
| ap-northeast-2 apne2-az1 | 58 | 100% | 9.0 | 9 (09-07 10:10Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 59 | 100% | 9.0 | 9 (09-07 16:24Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 23 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 24 | 100% | 9.0 | 9 (09-07 16:24Z) |
| us-east-1 use1-az4 | 25 | 100% | 9.0 | 9 (09-07 16:24Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 26 | 100% | 9.0 | 9 (09-07 16:24Z) |
| us-east-2 use2-az1 | 24 | 100% | 9.0 | 9 (09-07 10:10Z) |
| us-east-2 use2-az2 | 38 | 95% | 8.6 | 9 (09-07 16:24Z) |
| us-east-2 use2-az3 | 18 | 56% | 6.1 | 3 (09-07 04:26Z) |
| us-west-2 usw2-az1 | 21 | 95% | 8.7 | 9 (09-07 16:24Z) |
| us-west-2 usw2-az2 | 15 | 93% | 8.7 | 9 (09-07 16:24Z) |
| us-west-2 usw2-az3 | 21 | 95% | 8.7 | 9 (09-07 16:24Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.750100 | 2026-09-07T16:24:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-07T16:24:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.784900 | 2026-09-07T16:24:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.958200 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597700 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585100 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579700 | 2026-09-07T16:24:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-07T16:24:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.553000 | 2026-09-07T16:24:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.325600 | 2026-09-07T16:24:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.488300 | 2026-09-07T16:24:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.326900 | 2026-09-07T16:24:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.751300 | 2026-09-07T16:24:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503100 | 2026-09-07T16:24:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.914000 | 2026-09-07T16:24:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.402900 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.918500 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1a | Windows | 0.343800 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.660800 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1b | Windows | 0.318500 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.567900 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1c | Windows | 0.315300 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.478200 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1d | Windows | 0.317700 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.517200 | 2026-09-07T16:24:49Z |
| us-east-1 | us-east-1f | Windows | 0.317000 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.517000 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2a | Windows | 0.637400 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.514100 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2b | Windows | 0.636800 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515800 | 2026-09-07T16:24:49Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568500 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2a | Windows | 0.298000 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.525300 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2b | Windows | 0.308400 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526000 | 2026-09-07T16:24:49Z |
| us-west-2 | us-west-2c | Windows | 0.335200 | 2026-09-07T16:24:49Z |
