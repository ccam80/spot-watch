# Spot placement score log

Generated 2026-09-06 19:05 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 57 | 0% | 1.0 | 1 (09-06 19:05Z) |
| ap-northeast-1 | 57 | 0% | 1.8 | 2 (09-06 19:05Z) |
| ap-northeast-2 | 57 | 0% | 2.9 | 3 (09-06 19:05Z) |
| ap-south-1 | 57 | 0% | 2.3 | 2 (09-06 19:05Z) |
| ap-southeast-2 | 57 | 0% | 1.0 | 1 (09-06 19:05Z) |
| ap-southeast-3 | 57 | 0% | 2.5 | 3 (09-06 19:05Z) |
| us-east-1 | 57 | 0% | 1.8 | 2 (09-06 19:05Z) |
| us-east-2 | 57 | 0% | 1.3 | 1 (09-06 19:05Z) |
| us-west-2 | 57 | 0% | 1.5 | 1 (09-06 19:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   313313111131111111113112111122113113333113333312
ap-northeast-2   333333333333333331133333333333333333333333333333
ap-south-1       333313333111311131222133221133322333333233331112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   323211132112333333333333313131313333333311333333
us-east-1        131111113121111111111111122123332113132333323232
us-east-2        111133111111111111131111111111111111113111113311
us-west-2        111113133311111111111112111222222222221111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | · | 2 | 2 | 3 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 21 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-east-1 ape1-az2 | 16 | 0% | 1.0 | 1 (09-06 19:05Z) |
| ap-northeast-1 apne1-az1 | 11 | 0% | 1.2 | 1 (09-06 09:20Z) |
| ap-northeast-1 apne1-az4 | 35 | 0% | 2.1 | 3 (09-06 13:37Z) |
| ap-northeast-2 apne2-az1 | 53 | 0% | 3.0 | 3 (09-06 19:05Z) |
| ap-northeast-2 apne2-az3 | 53 | 0% | 2.9 | 3 (09-06 19:05Z) |
| ap-northeast-2 apne2-az4 | 56 | 0% | 3.0 | 3 (09-06 19:05Z) |
| ap-south-1 aps1-az1 | 23 | 0% | 1.8 | 1 (09-05 23:49Z) |
| ap-south-1 aps1-az3 | 38 | 0% | 2.7 | 1 (09-06 13:37Z) |
| ap-southeast-2 apse2-az1 | 12 | 0% | 1.0 | 1 (09-06 13:37Z) |
| ap-southeast-2 apse2-az2 | 11 | 0% | 1.0 | 1 (09-06 19:05Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 46 | 0% | 2.9 | 3 (09-06 19:05Z) |
| us-east-1 use1-az1 | 11 | 0% | 1.0 | 1 (09-06 19:05Z) |
| us-east-1 use1-az2 | 21 | 0% | 1.1 | 1 (09-05 23:49Z) |
| us-east-1 use1-az4 | 12 | 0% | 1.3 | 1 (09-06 19:05Z) |
| us-east-1 use1-az5 | 17 | 0% | 1.2 | 1 (09-06 04:28Z) |
| us-east-1 use1-az6 | 26 | 0% | 1.2 | 1 (09-06 19:05Z) |
| us-east-2 use2-az1 | 10 | 0% | 1.2 | 1 (09-05 21:09Z) |
| us-east-2 use2-az2 | 19 | 0% | 1.3 | 3 (09-06 13:37Z) |
| us-east-2 use2-az3 | 18 | 0% | 1.8 | 3 (09-06 13:37Z) |
| us-west-2 usw2-az1 | 12 | 0% | 1.5 | 1 (09-06 04:28Z) |
| us-west-2 usw2-az2 | 9 | 0% | 1.2 | 1 (09-06 09:20Z) |
| us-west-2 usw2-az3 | 27 | 0% | 1.3 | 1 (09-06 19:05Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 57 | 0% | 3.0 | 3 (09-06 19:05Z) |
| ap-northeast-1 | 57 | 82% | 7.6 | 9 (09-06 19:05Z) |
| ap-northeast-2 | 57 | 100% | 9.0 | 9 (09-06 19:05Z) |
| ap-south-1 | 57 | 0% | 2.8 | 3 (09-06 19:05Z) |
| ap-southeast-2 | 57 | 18% | 3.1 | 3 (09-06 19:05Z) |
| ap-southeast-3 | 57 | 0% | 2.5 | 3 (09-06 19:05Z) |
| us-east-1 | 57 | 72% | 6.3 | 9 (09-06 19:05Z) |
| us-east-2 | 57 | 63% | 6.4 | 9 (09-06 19:05Z) |
| us-west-2 | 57 | 46% | 5.4 | 9 (09-06 19:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999199119999119999219999129999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333133311333333333322333333333333333333333
ap-southeast-2   999999931111112311111311113331113313333333333333
ap-southeast-3   323211132112333333333333313131313333333311333333
us-east-1        999999999941191121992113994335654256599599999999
us-east-2        999199221911199999999113993332393382999999999999
us-west-2        222299999991299244929212429443445345449985896999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 3 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 6 | 2 | · | 5 | 2 | 3 | 3 | 2 | 6 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 6 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 5 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 4 | · | 9 | 9 | 9 | 7 | 9 | 6 | 2 | 5 | 6 | 2 | 4 | 3 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 22 | 64% | 6.8 | 9 (09-06 19:05Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 44 | 100% | 9.0 | 9 (09-06 19:05Z) |
| ap-northeast-2 apne2-az1 | 54 | 100% | 9.0 | 9 (09-06 19:05Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 54 | 100% | 9.0 | 9 (09-06 19:05Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 19 | 100% | 8.9 | 9 (09-06 19:05Z) |
| us-east-1 use1-az4 | 21 | 100% | 9.0 | 9 (09-06 19:05Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 21 | 100% | 9.0 | 9 (09-06 19:05Z) |
| us-east-2 use2-az1 | 21 | 100% | 9.0 | 9 (09-06 13:37Z) |
| us-east-2 use2-az2 | 33 | 94% | 8.5 | 9 (09-06 19:05Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 18 | 94% | 8.7 | 9 (09-06 19:05Z) |
| us-west-2 usw2-az2 | 12 | 100% | 9.0 | 9 (09-06 04:28Z) |
| us-west-2 usw2-az3 | 19 | 95% | 8.6 | 9 (09-06 19:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.752000 | 2026-09-06T19:05:04Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-06T19:05:04Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.781400 | 2026-09-06T19:05:04Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.941700 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.598500 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.584000 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579500 | 2026-09-06T19:05:04Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-06T19:05:04Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.550300 | 2026-09-06T19:05:04Z |
| ap-south-1 | ap-south-1a | Windows | 0.325700 | 2026-09-06T19:05:04Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.486700 | 2026-09-06T19:05:04Z |
| ap-south-1 | ap-south-1b | Windows | 0.325000 | 2026-09-06T19:05:04Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.734600 | 2026-09-06T19:05:04Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.484400 | 2026-09-06T19:05:04Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.920300 | 2026-09-06T19:05:04Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.389000 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.912200 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1a | Windows | 0.335100 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.654400 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1b | Windows | 0.318100 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.555200 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1c | Windows | 0.315000 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.468500 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1d | Windows | 0.316100 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.502800 | 2026-09-06T19:05:04Z |
| us-east-1 | us-east-1f | Windows | 0.314800 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.497600 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.496300 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.500800 | 2026-09-06T19:05:04Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.552100 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2a | Windows | 0.296800 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.516200 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2b | Windows | 0.303200 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.515400 | 2026-09-06T19:05:04Z |
| us-west-2 | us-west-2c | Windows | 0.334500 | 2026-09-06T19:05:04Z |
