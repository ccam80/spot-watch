# Spot placement score log

Generated 2026-09-08 14:27 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 67 | 0% | 1.0 | 1 (09-08 14:27Z) |
| ap-northeast-1 | 67 | 0% | 1.7 | 1 (09-08 14:27Z) |
| ap-northeast-2 | 67 | 0% | 2.9 | 3 (09-08 14:27Z) |
| ap-south-1 | 67 | 0% | 2.1 | 2 (09-08 14:27Z) |
| ap-southeast-2 | 67 | 0% | 1.0 | 1 (09-08 14:27Z) |
| ap-southeast-3 | 67 | 0% | 2.5 | 2 (09-08 14:27Z) |
| us-east-1 | 67 | 0% | 1.9 | 3 (09-08 14:27Z) |
| us-east-2 | 67 | 0% | 1.4 | 3 (09-08 14:27Z) |
| us-west-2 | 67 | 0% | 1.5 | 1 (09-08 14:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   311111111131121111221131133331133333122111122211
ap-northeast-2   333333311333333333333333333333333333333333333333
ap-south-1       113111312221332211333223333332333311121111311122
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   123333333333333131313133333333113333333313333212
us-east-1        211111111111111221233321131323333232323332322333
us-east-2        111111111311111111111111111131111133111131113333
us-west-2        111111111111121112222222222211111111111111213311
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
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 2 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 22 | 0% | 1.0 | 1 (09-07 20:30Z) |
| ap-east-1 ape1-az2 | 21 | 0% | 1.0 | 1 (09-08 14:27Z) |
| ap-northeast-1 apne1-az1 | 13 | 0% | 1.2 | 1 (09-08 14:27Z) |
| ap-northeast-1 apne1-az4 | 37 | 0% | 2.1 | 2 (09-07 20:30Z) |
| ap-northeast-2 apne2-az1 | 63 | 0% | 3.0 | 3 (09-08 14:27Z) |
| ap-northeast-2 apne2-az3 | 60 | 0% | 2.9 | 3 (09-08 14:27Z) |
| ap-northeast-2 apne2-az4 | 66 | 0% | 3.0 | 3 (09-08 14:27Z) |
| ap-south-1 aps1-az1 | 28 | 0% | 1.7 | 1 (09-08 09:34Z) |
| ap-south-1 aps1-az3 | 43 | 0% | 2.6 | 1 (09-08 14:27Z) |
| ap-southeast-2 apse2-az1 | 16 | 0% | 1.0 | 1 (09-08 14:27Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 14 | 0% | 1.0 | 1 (09-08 09:34Z) |
| ap-southeast-3 apse3-az3 | 54 | 0% | 2.9 | 2 (09-08 14:27Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 22 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 20 | 0% | 1.3 | 3 (09-08 04:26Z) |
| us-east-1 use1-az6 | 30 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az1 | 14 | 0% | 1.1 | 1 (09-08 09:34Z) |
| us-east-2 use2-az2 | 25 | 0% | 1.5 | 3 (09-08 14:27Z) |
| us-east-2 use2-az3 | 26 | 0% | 2.0 | 3 (09-08 14:27Z) |
| us-west-2 usw2-az1 | 14 | 0% | 1.6 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 33 | 0% | 1.4 | 1 (09-08 09:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 67 | 0% | 3.0 | 3 (09-08 14:27Z) |
| ap-northeast-1 | 67 | 79% | 7.4 | 9 (09-08 14:27Z) |
| ap-northeast-2 | 67 | 100% | 9.0 | 9 (09-08 14:27Z) |
| ap-south-1 | 67 | 0% | 2.9 | 3 (09-08 14:27Z) |
| ap-southeast-2 | 67 | 15% | 2.9 | 3 (09-08 14:27Z) |
| ap-southeast-3 | 67 | 0% | 2.5 | 2 (09-08 14:27Z) |
| us-east-1 | 67 | 76% | 6.6 | 5 (09-08 14:27Z) |
| us-east-2 | 67 | 69% | 6.8 | 9 (09-08 14:27Z) |
| us-west-2 | 67 | 52% | 5.7 | 9 (09-08 14:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   991199991199992199991299999999999999999912999439
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333113333333333223333333333333333333333333333333
ap-southeast-2   111123111113111133311133133333333333333111311113
ap-southeast-3   123333333333333131313133333333113333333313333212
us-east-1        411911219921139943356542565995999999999999999995
us-east-2        111999999991139933323933829999999999999999999999
us-west-2        912992449292124294434453454499858969999719999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
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
| ap-east-1 ape1-az2 | 19 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 28 | 71% | 7.2 | 8 (09-08 14:27Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 50 | 100% | 9.0 | 9 (09-08 14:27Z) |
| ap-northeast-2 apne2-az1 | 63 | 100% | 9.0 | 9 (09-08 14:27Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 63 | 100% | 9.0 | 9 (09-08 14:27Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 12 | 0% | 3.0 | 3 (09-07 20:30Z) |
| ap-south-1 aps1-az2 | 23 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 6 | 0% | 3.0 | 3 (09-08 14:27Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 27 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az4 | 28 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 30 | 100% | 9.0 | 9 (09-08 09:34Z) |
| us-east-2 use2-az1 | 27 | 100% | 9.0 | 9 (09-08 14:27Z) |
| us-east-2 use2-az2 | 42 | 95% | 8.6 | 9 (09-08 14:27Z) |
| us-east-2 use2-az3 | 22 | 64% | 6.6 | 9 (09-08 14:27Z) |
| us-west-2 usw2-az1 | 26 | 96% | 8.8 | 9 (09-08 14:27Z) |
| us-west-2 usw2-az2 | 17 | 94% | 8.7 | 9 (09-08 04:26Z) |
| us-west-2 usw2-az3 | 26 | 96% | 8.7 | 9 (09-08 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.747400 | 2026-09-08T14:27:27Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-08T14:27:27Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.784700 | 2026-09-08T14:27:27Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.953100 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597300 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578800 | 2026-09-08T14:27:27Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-08T14:27:27Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548900 | 2026-09-08T14:27:27Z |
| ap-south-1 | ap-south-1a | Windows | 0.325100 | 2026-09-08T14:27:27Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.493600 | 2026-09-08T14:27:27Z |
| ap-south-1 | ap-south-1b | Windows | 0.327000 | 2026-09-08T14:27:27Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750600 | 2026-09-08T14:27:27Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-09-08T14:27:27Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.899100 | 2026-09-08T14:27:27Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.404900 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.918300 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1a | Windows | 0.357800 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.691000 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1b | Windows | 0.319800 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.592100 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1c | Windows | 0.315700 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.502700 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1d | Windows | 0.320100 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.551600 | 2026-09-08T14:27:27Z |
| us-east-1 | us-east-1f | Windows | 0.318400 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530300 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2a | Windows | 0.637700 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525900 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526100 | 2026-09-08T14:27:27Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579200 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2a | Windows | 0.301600 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.543100 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2b | Windows | 0.313400 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.534200 | 2026-09-08T14:27:27Z |
| us-west-2 | us-west-2c | Windows | 0.335200 | 2026-09-08T14:27:27Z |
