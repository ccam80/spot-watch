# Spot placement score log

Generated 2026-09-05 15:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 49 | 0% | 1.0 | 1 (09-05 15:59Z) |
| ap-northeast-1 | 49 | 0% | 1.7 | 1 (09-05 15:59Z) |
| ap-northeast-2 | 49 | 0% | 2.9 | 3 (09-05 15:59Z) |
| ap-south-1 | 49 | 0% | 2.3 | 2 (09-05 15:59Z) |
| ap-southeast-2 | 49 | 0% | 1.0 | 1 (09-05 15:59Z) |
| ap-southeast-3 | 49 | 0% | 2.5 | 3 (09-05 15:59Z) |
| us-east-1 | 49 | 0% | 1.7 | 3 (09-05 15:59Z) |
| us-east-2 | 49 | 0% | 1.2 | 1 (09-05 15:59Z) |
| us-west-2 | 49 | 0% | 1.6 | 1 (09-05 15:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   113113333133131111311111111131121111221131133331
ap-northeast-2   333333333333333333333333311333333333333333333333
ap-south-1       331313333333133331113111312221332211333223333332
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333323232111321123333333333333131313133333333
us-east-1        233321111311111131211111111111111221233321131323
us-east-2        111131131111331111111111111311111111111111111131
us-west-2        212221131111131333111111111111121112222222222211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 19 | 0% | 1.0 | 1 (09-04 21:23Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 30 | 0% | 2.0 | 3 (09-05 12:37Z) |
| ap-northeast-2 apne2-az1 | 45 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-northeast-2 apne2-az3 | 45 | 0% | 2.9 | 3 (09-05 15:59Z) |
| ap-northeast-2 apne2-az4 | 48 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az1 | 20 | 0% | 1.9 | 1 (09-05 15:59Z) |
| ap-south-1 aps1-az3 | 33 | 0% | 2.7 | 2 (09-05 15:59Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 8 | 0% | 1.0 | 1 (09-05 08:59Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 2.9 | 3 (09-05 15:59Z) |
| us-east-1 use1-az1 | 9 | 0% | 1.0 | 1 (09-05 08:59Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 10 | 0% | 1.4 | 1 (09-05 08:59Z) |
| us-east-1 use1-az5 | 16 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-east-1 use1-az6 | 21 | 0% | 1.2 | 1 (09-05 15:59Z) |
| us-east-2 use2-az1 | 8 | 0% | 1.2 | 1 (09-05 15:59Z) |
| us-east-2 use2-az2 | 15 | 0% | 1.1 | 1 (09-05 15:59Z) |
| us-east-2 use2-az3 | 15 | 0% | 1.7 | 3 (09-05 12:37Z) |
| us-west-2 usw2-az1 | 11 | 0% | 1.5 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 22 | 0% | 1.4 | 1 (09-05 15:59Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 49 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-northeast-1 | 49 | 80% | 7.4 | 9 (09-05 15:59Z) |
| ap-northeast-2 | 49 | 100% | 9.0 | 9 (09-05 15:59Z) |
| ap-south-1 | 49 | 0% | 2.8 | 3 (09-05 15:59Z) |
| ap-southeast-2 | 49 | 20% | 3.1 | 3 (09-05 15:59Z) |
| ap-southeast-3 | 49 | 0% | 2.5 | 3 (09-05 15:59Z) |
| us-east-1 | 49 | 67% | 5.9 | 5 (09-05 15:59Z) |
| us-east-2 | 49 | 57% | 6.0 | 9 (09-05 15:59Z) |
| us-west-2 | 49 | 37% | 4.9 | 9 (09-05 15:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   919999999999999991991199991199992199991299999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       331333333333333331333113333333333223333333333333
ap-southeast-2   111119799999999311111123111113111133311133133333
ap-southeast-3   333333323232111321123333333333333131313133333333
us-east-1        667875899999999999411911219921139943356542565995
us-east-2        299192999991992219111999999991139933323933829999
us-west-2        424392192222999999912992449292124294434453454499
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
| us-east-1 | 4 | 9 | · | 6 | 7 | · | 9 | · | 9 | 8 | · | 8 | 5 | · | 5 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 5 | 9 | 9 | 2 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 6 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 4 | 2 | 2 | 4 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 16 | 50% | 6.0 | 9 (09-05 15:59Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 37 | 100% | 9.0 | 9 (09-05 15:59Z) |
| ap-northeast-2 apne2-az1 | 48 | 100% | 9.0 | 9 (09-05 15:59Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 47 | 100% | 9.0 | 9 (09-05 15:59Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 12 | 100% | 8.9 | 9 (09-05 08:59Z) |
| us-east-1 use1-az4 | 13 | 100% | 9.0 | 9 (09-05 12:37Z) |
| us-east-1 use1-az5 | 16 | 100% | 8.9 | 9 (09-05 12:37Z) |
| us-east-1 use1-az6 | 13 | 100% | 9.0 | 9 (09-05 08:59Z) |
| us-east-2 use2-az1 | 15 | 100% | 8.9 | 9 (09-05 15:59Z) |
| us-east-2 use2-az2 | 25 | 92% | 8.4 | 9 (09-05 15:59Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 14 | 93% | 8.6 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az2 | 11 | 100% | 9.0 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az3 | 15 | 93% | 8.5 | 9 (09-05 15:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.754000 | 2026-09-05T15:59:34Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-05T15:59:34Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783300 | 2026-09-05T15:59:34Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.925800 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.577600 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.571400 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.575800 | 2026-09-05T15:59:34Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-05T15:59:34Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.559500 | 2026-09-05T15:59:34Z |
| ap-south-1 | ap-south-1a | Windows | 0.314600 | 2026-09-05T15:59:34Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500000 | 2026-09-05T15:59:34Z |
| ap-south-1 | ap-south-1b | Windows | 0.318600 | 2026-09-05T15:59:34Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747200 | 2026-09-05T15:59:34Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.481200 | 2026-09-05T15:59:34Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.937100 | 2026-09-05T15:59:34Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.379500 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.915800 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1a | Windows | 0.332900 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.667100 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1b | Windows | 0.318800 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.564300 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1c | Windows | 0.315600 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.469300 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1d | Windows | 0.316800 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.505100 | 2026-09-05T15:59:34Z |
| us-east-1 | us-east-1f | Windows | 0.315800 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.467100 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.473500 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.465000 | 2026-09-05T15:59:34Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559800 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2a | Windows | 0.290900 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.518000 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2b | Windows | 0.294500 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.519300 | 2026-09-05T15:59:34Z |
| us-west-2 | us-west-2c | Windows | 0.333400 | 2026-09-05T15:59:34Z |
