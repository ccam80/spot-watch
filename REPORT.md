# Spot placement score log

Generated 2026-09-05 04:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 46 | 0% | 1.0 | 1 (09-05 04:17Z) |
| ap-northeast-1 | 46 | 0% | 1.6 | 3 (09-05 04:17Z) |
| ap-northeast-2 | 46 | 0% | 2.9 | 3 (09-05 04:17Z) |
| ap-south-1 | 46 | 0% | 2.3 | 3 (09-05 04:17Z) |
| ap-southeast-2 | 46 | 0% | 1.0 | 1 (09-05 04:17Z) |
| ap-southeast-3 | 46 | 0% | 2.5 | 3 (09-05 04:17Z) |
| us-east-1 | 46 | 0% | 1.6 | 1 (09-05 04:17Z) |
| us-east-2 | 46 | 0% | 1.2 | 1 (09-05 04:17Z) |
| us-west-2 | 46 | 0% | 1.6 | 2 (09-05 04:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1          1111111111111111111111111111111111111111111111
ap-northeast-1     1113113333133131111311111111131121111221131133
ap-northeast-2     3333333333333333333333333311333333333333333333
ap-south-1         3331313333333133331113111312221332211333223333
ap-southeast-2     1111111111111111111111111111111111111111111111
ap-southeast-3     3333333323232111321123333333333333131313133333
us-east-1          3233321111311111131211111111111111221233321131
us-east-2          1111131131111331111111111111311111111111111111
us-west-2          2212221131111131333111111111111121112222222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | 2 | · | 3 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 19 | 0% | 1.0 | 1 (09-04 21:23Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 28 | 0% | 1.9 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az1 | 42 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 42 | 0% | 2.9 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az1 | 18 | 0% | 1.9 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 30 | 0% | 2.7 | 3 (09-05 04:17Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 7 | 0% | 1.0 | 1 (09-04 23:58Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 37 | 0% | 2.8 | 3 (09-05 04:17Z) |
| us-east-1 use1-az1 | 8 | 0% | 1.0 | 1 (09-04 23:58Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 9 | 0% | 1.4 | 1 (09-04 23:58Z) |
| us-east-1 use1-az5 | 16 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-east-1 use1-az6 | 19 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-east-2 use2-az1 | 7 | 0% | 1.3 | 1 (09-05 04:17Z) |
| us-east-2 use2-az2 | 14 | 0% | 1.1 | 1 (09-05 04:17Z) |
| us-east-2 use2-az3 | 14 | 0% | 1.6 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az1 | 11 | 0% | 1.5 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 19 | 0% | 1.4 | 1 (09-05 04:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 46 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-1 | 46 | 78% | 7.3 | 9 (09-05 04:17Z) |
| ap-northeast-2 | 46 | 100% | 9.0 | 9 (09-05 04:17Z) |
| ap-south-1 | 46 | 0% | 2.8 | 3 (09-05 04:17Z) |
| ap-southeast-2 | 46 | 22% | 3.2 | 3 (09-05 04:17Z) |
| ap-southeast-3 | 46 | 0% | 2.5 | 3 (09-05 04:17Z) |
| us-east-1 | 46 | 65% | 5.7 | 5 (09-05 04:17Z) |
| us-east-2 | 46 | 54% | 5.8 | 9 (09-05 04:17Z) |
| us-west-2 | 46 | 35% | 4.8 | 4 (09-05 04:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1          3333333333333333333333333333333333333333333333
ap-northeast-1     9919999999999999991991199991199992199991299999
ap-northeast-2     9999999999999999999999999999999999999999999999
ap-south-1         3331333333333333331333113333333333223333333333
ap-southeast-2     1111119799999999311111123111113111133311133133
ap-southeast-3     3333333323232111321123333333333333131313133333
us-east-1          7667875899999999999411911219921139943356542565
us-east-2          9299192999991992219111999999991139933323933829
us-west-2          4424392192222999999912992449292124294434453454
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 3 | 1 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 7 | · | 9 | · | 9 | 8 | · | 8 | 1 | · | 5 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 1 | 9 | 9 | 2 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 9 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 4 | 2 | 2 | 4 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 13 | 38% | 5.3 | 9 (09-05 04:17Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 34 | 100% | 9.0 | 9 (09-05 04:17Z) |
| ap-northeast-2 apne2-az1 | 45 | 100% | 9.0 | 9 (09-05 04:17Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 45 | 100% | 9.0 | 9 (09-05 04:17Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 10 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 11 | 100% | 8.9 | 8 (09-03 04:19Z) |
| us-east-1 use1-az4 | 11 | 100% | 9.0 | 9 (09-03 09:40Z) |
| us-east-1 use1-az5 | 14 | 100% | 8.9 | 8 (09-03 09:40Z) |
| us-east-1 use1-az6 | 12 | 100% | 9.0 | 9 (09-03 04:19Z) |
| us-east-2 use2-az1 | 12 | 100% | 8.9 | 9 (09-05 04:17Z) |
| us-east-2 use2-az2 | 22 | 91% | 8.3 | 9 (09-05 04:17Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 12 | 92% | 8.5 | 9 (09-03 14:26Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 13 | 92% | 8.5 | 2 (09-04 09:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.755200 | 2026-09-05T04:17:42Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-05T04:17:42Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.796100 | 2026-09-05T04:17:42Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.914500 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.565700 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.556700 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565700 | 2026-09-05T04:17:42Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-05T04:17:42Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.557600 | 2026-09-05T04:17:42Z |
| ap-south-1 | ap-south-1a | Windows | 0.314300 | 2026-09-05T04:17:42Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.502100 | 2026-09-05T04:17:42Z |
| ap-south-1 | ap-south-1b | Windows | 0.317000 | 2026-09-05T04:17:42Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747300 | 2026-09-05T04:17:42Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.470000 | 2026-09-05T04:17:42Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.933500 | 2026-09-05T04:17:42Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.379600 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.920700 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1a | Windows | 0.333100 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.675600 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1b | Windows | 0.319400 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.569300 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1c | Windows | 0.317000 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.471900 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1d | Windows | 0.317200 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.505200 | 2026-09-05T04:17:42Z |
| us-east-1 | us-east-1f | Windows | 0.315900 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.462500 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.462600 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.454400 | 2026-09-05T04:17:42Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561400 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2a | Windows | 0.288600 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.519800 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2b | Windows | 0.291000 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.521500 | 2026-09-05T04:17:42Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-05T04:17:42Z |
