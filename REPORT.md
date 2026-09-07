# Spot placement score log

Generated 2026-09-07 23:27 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 64 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-northeast-1 | 64 | 0% | 1.7 | 2 (09-07 23:27Z) |
| ap-northeast-2 | 64 | 0% | 2.9 | 3 (09-07 23:27Z) |
| ap-south-1 | 64 | 0% | 2.2 | 1 (09-07 23:27Z) |
| ap-southeast-2 | 64 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-southeast-3 | 64 | 0% | 2.5 | 3 (09-07 23:27Z) |
| us-east-1 | 64 | 0% | 1.9 | 2 (09-07 23:27Z) |
| us-east-2 | 64 | 0% | 1.3 | 3 (09-07 23:27Z) |
| us-west-2 | 64 | 0% | 1.5 | 3 (09-07 23:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   111311111111131121111221131133331133333122111122
ap-northeast-2   333333333311333333333333333333333333333333333333
ap-south-1       331113111312221332211333223333332333311121111311
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   321123333333333333131313133333333113333333313333
us-east-1        131211111111111111221233321131323333232323332322
us-east-2        111111111111311111111111111111131111133111131113
us-west-2        333111111111111121112222222222211111111111111213
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 22 | 0% | 1.0 | 1 (09-07 20:30Z) |
| ap-east-1 ape1-az2 | 20 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-northeast-1 apne1-az1 | 12 | 0% | 1.2 | 1 (09-07 10:10Z) |
| ap-northeast-1 apne1-az4 | 37 | 0% | 2.1 | 2 (09-07 20:30Z) |
| ap-northeast-2 apne2-az1 | 60 | 0% | 3.0 | 3 (09-07 23:27Z) |
| ap-northeast-2 apne2-az3 | 58 | 0% | 2.9 | 3 (09-07 16:24Z) |
| ap-northeast-2 apne2-az4 | 63 | 0% | 3.0 | 3 (09-07 23:27Z) |
| ap-south-1 aps1-az1 | 26 | 0% | 1.8 | 1 (09-07 20:30Z) |
| ap-south-1 aps1-az3 | 42 | 0% | 2.6 | 1 (09-07 23:27Z) |
| ap-southeast-2 apse2-az1 | 15 | 0% | 1.0 | 1 (09-07 23:27Z) |
| ap-southeast-2 apse2-az2 | 13 | 0% | 1.0 | 1 (09-07 04:26Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 52 | 0% | 2.9 | 3 (09-07 23:27Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 21 | 0% | 1.1 | 1 (09-05 23:49Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 19 | 0% | 1.2 | 1 (09-07 16:24Z) |
| us-east-1 use1-az6 | 29 | 0% | 1.1 | 1 (09-07 20:30Z) |
| us-east-2 use2-az1 | 12 | 0% | 1.2 | 1 (09-07 20:30Z) |
| us-east-2 use2-az2 | 22 | 0% | 1.4 | 1 (09-07 20:30Z) |
| us-east-2 use2-az3 | 23 | 0% | 1.8 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az1 | 14 | 0% | 1.6 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az2 | 11 | 0% | 1.4 | 3 (09-07 23:27Z) |
| us-west-2 usw2-az3 | 31 | 0% | 1.3 | 3 (09-07 23:27Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 64 | 0% | 3.0 | 3 (09-07 23:27Z) |
| ap-northeast-1 | 64 | 81% | 7.5 | 9 (09-07 23:27Z) |
| ap-northeast-2 | 64 | 100% | 9.0 | 9 (09-07 23:27Z) |
| ap-south-1 | 64 | 0% | 2.8 | 3 (09-07 23:27Z) |
| ap-southeast-2 | 64 | 16% | 3.0 | 1 (09-07 23:27Z) |
| ap-southeast-3 | 64 | 0% | 2.5 | 3 (09-07 23:27Z) |
| us-east-1 | 64 | 75% | 6.6 | 9 (09-07 23:27Z) |
| us-east-2 | 64 | 67% | 6.7 | 9 (09-07 23:27Z) |
| us-west-2 | 64 | 50% | 5.6 | 9 (09-07 23:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   991991199991199992199991299999999999999999912999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       331333113333333333223333333333333333333333333333
ap-southeast-2   311111123111113111133311133133333333333333111311
ap-southeast-3   321123333333333333131313133333333113333333313333
us-east-1        999411911219921139943356542565995999999999999999
us-east-2        219111999999991139933323933829999999999999999999
us-west-2        999912992449292124294434453454499858969999719999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 2 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 4 | 9 | 9 | 9 | 9 | 7 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

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
| ap-northeast-2 apne2-az1 | 60 | 100% | 9.0 | 9 (09-07 23:27Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 60 | 100% | 9.0 | 9 (09-07 20:30Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 12 | 0% | 3.0 | 3 (09-07 20:30Z) |
| ap-south-1 aps1-az2 | 23 | 0% | 3.0 | 3 (09-07 04:26Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 25 | 100% | 9.0 | 9 (09-07 23:27Z) |
| us-east-1 use1-az4 | 26 | 100% | 9.0 | 9 (09-07 23:27Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 28 | 100% | 9.0 | 9 (09-07 23:27Z) |
| us-east-2 use2-az1 | 24 | 100% | 9.0 | 9 (09-07 10:10Z) |
| us-east-2 use2-az2 | 40 | 95% | 8.6 | 9 (09-07 23:27Z) |
| us-east-2 use2-az3 | 19 | 58% | 6.3 | 9 (09-07 23:27Z) |
| us-west-2 usw2-az1 | 23 | 96% | 8.7 | 9 (09-07 23:27Z) |
| us-west-2 usw2-az2 | 16 | 94% | 8.7 | 9 (09-07 20:30Z) |
| us-west-2 usw2-az3 | 23 | 96% | 8.7 | 9 (09-07 23:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.749600 | 2026-09-07T23:27:18Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-07T23:27:18Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.786100 | 2026-09-07T23:27:18Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.954100 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.597700 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585500 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579900 | 2026-09-07T23:27:18Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-07T23:27:18Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548800 | 2026-09-07T23:27:18Z |
| ap-south-1 | ap-south-1a | Windows | 0.325500 | 2026-09-07T23:27:18Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.487400 | 2026-09-07T23:27:18Z |
| ap-south-1 | ap-south-1b | Windows | 0.327300 | 2026-09-07T23:27:18Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.752800 | 2026-09-07T23:27:18Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-09-07T23:27:18Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.910300 | 2026-09-07T23:27:18Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.404100 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.914600 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1a | Windows | 0.351400 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.679300 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1b | Windows | 0.319600 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.584600 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1c | Windows | 0.315400 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.486900 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1d | Windows | 0.318500 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.522300 | 2026-09-07T23:27:18Z |
| us-east-1 | us-east-1f | Windows | 0.317000 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521700 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2a | Windows | 0.637400 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.517100 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2b | Windows | 0.636800 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.522600 | 2026-09-07T23:27:18Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.577900 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2a | Windows | 0.299000 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.528200 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2b | Windows | 0.309300 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526000 | 2026-09-07T23:27:18Z |
| us-west-2 | us-west-2c | Windows | 0.335100 | 2026-09-07T23:27:18Z |
