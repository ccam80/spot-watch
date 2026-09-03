# Spot placement score log

Generated 2026-09-03 18:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 37 | 0% | 1.0 | 1 (09-03 18:33Z) |
| ap-northeast-1 | 37 | 0% | 1.6 | 1 (09-03 18:33Z) |
| ap-northeast-2 | 37 | 0% | 2.9 | 3 (09-03 18:33Z) |
| ap-south-1 | 37 | 0% | 2.2 | 1 (09-03 18:33Z) |
| ap-southeast-2 | 37 | 0% | 1.0 | 1 (09-03 18:33Z) |
| ap-southeast-3 | 37 | 0% | 2.5 | 1 (09-03 18:33Z) |
| us-east-1 | 37 | 0% | 1.5 | 1 (09-03 18:33Z) |
| us-east-2 | 37 | 0% | 1.3 | 1 (09-03 18:33Z) |
| us-west-2 | 37 | 0% | 1.5 | 2 (09-03 18:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                   1111111111111111111111111111111111111
ap-northeast-1              1113113333133131111311111111131121111
ap-northeast-2              3333333333333333333333333311333333333
ap-south-1                  3331313333333133331113111312221332211
ap-southeast-2              1111111111111111111111111111111111111
ap-southeast-3              3333333323232111321123333333333333131
us-east-1                   3233321111311111131211111111111111221
us-east-2                   1111131131111331111111111111311111111
us-west-2                   2212221131111131333111111111111121112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 2 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | 2 | · | 3 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 17 | 0% | 1.0 | 1 (09-03 18:33Z) |
| ap-east-1 ape1-az2 | 10 | 0% | 1.0 | 1 (09-03 18:33Z) |
| ap-northeast-1 apne1-az1 | 7 | 0% | 1.3 | 1 (09-03 00:06Z) |
| ap-northeast-1 apne1-az4 | 23 | 0% | 1.9 | 1 (09-03 18:33Z) |
| ap-northeast-2 apne2-az1 | 33 | 0% | 2.9 | 3 (09-03 18:33Z) |
| ap-northeast-2 apne2-az3 | 33 | 0% | 2.9 | 3 (09-03 18:33Z) |
| ap-northeast-2 apne2-az4 | 36 | 0% | 2.9 | 3 (09-03 18:33Z) |
| ap-south-1 aps1-az1 | 13 | 0% | 1.8 | 1 (09-03 09:40Z) |
| ap-south-1 aps1-az3 | 22 | 0% | 2.7 | 3 (09-03 00:06Z) |
| ap-southeast-2 apse2-az1 | 8 | 0% | 1.0 | 1 (09-03 04:19Z) |
| ap-southeast-2 apse2-az2 | 5 | 0% | 1.0 | 1 (09-03 14:26Z) |
| ap-southeast-3 apse3-az1 | 12 | 0% | 1.0 | 1 (09-03 09:40Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 2.9 | 3 (09-03 14:26Z) |
| us-east-1 use1-az1 | 7 | 0% | 1.0 | 1 (09-03 14:26Z) |
| us-east-1 use1-az2 | 19 | 0% | 1.1 | 1 (09-03 18:33Z) |
| us-east-1 use1-az4 | 8 | 0% | 1.5 | 1 (09-03 14:26Z) |
| us-east-1 use1-az5 | 12 | 0% | 1.3 | 1 (09-03 18:33Z) |
| us-east-1 use1-az6 | 17 | 0% | 1.2 | 1 (09-03 14:26Z) |
| us-east-2 use2-az1 | 4 | 0% | 1.5 | 1 (09-03 09:40Z) |
| us-east-2 use2-az2 | 12 | 0% | 1.2 | 1 (09-03 09:40Z) |
| us-east-2 use2-az3 | 11 | 0% | 1.8 | 1 (09-03 18:33Z) |
| us-west-2 usw2-az1 | 9 | 0% | 1.7 | 1 (09-03 18:33Z) |
| us-west-2 usw2-az2 | 7 | 0% | 1.3 | 1 (09-03 04:19Z) |
| us-west-2 usw2-az3 | 16 | 0% | 1.5 | 1 (09-03 14:26Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 37 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-northeast-1 | 37 | 78% | 7.3 | 9 (09-03 18:33Z) |
| ap-northeast-2 | 37 | 100% | 9.0 | 9 (09-03 18:33Z) |
| ap-south-1 | 37 | 0% | 2.7 | 3 (09-03 18:33Z) |
| ap-southeast-2 | 37 | 27% | 3.4 | 3 (09-03 18:33Z) |
| ap-southeast-3 | 37 | 0% | 2.5 | 1 (09-03 18:33Z) |
| us-east-1 | 37 | 65% | 6.0 | 3 (09-03 18:33Z) |
| us-east-2 | 37 | 59% | 6.0 | 3 (09-03 18:33Z) |
| us-west-2 | 37 | 38% | 5.0 | 4 (09-03 18:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                   3333333333333333333333333333333333333
ap-northeast-1              9919999999999999991991199991199992199
ap-northeast-2              9999999999999999999999999999999999999
ap-south-1                  3331333333333333331333113333333333223
ap-southeast-2              1111119799999999311111123111113111133
ap-southeast-3              3333333323232111321123333333333333131
us-east-1                   7667875899999999999411911219921139943
us-east-2                   9299192999991992219111999999991139933
us-west-2                   4424392192222999999912992449292124294
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 2 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 4 | 1 | 9 | 3 | 5 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 9 | · | 9 | · | 9 | 9 | · | 8 | 1 | · | 6 | 4 | 9 | 1 | 4 | 9 | 2 | 6 | 7 | 4 |
| us-east-2 | 2 | 1 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 8 | 1 | 9 | 9 | 2 | 9 | 5 | 4 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 9 | 2 | · | 9 | 9 | · | 8 | 9 | 2 | 2 | 5 | 2 | 2 | 5 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 20 | 0% | 3.0 | 3 (09-03 14:26Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-east-1 ape1-az3 | 14 | 0% | 3.0 | 3 (09-03 14:26Z) |
| ap-northeast-1 apne1-az1 | 8 | 50% | 6.0 | 3 (09-03 18:33Z) |
| ap-northeast-1 apne1-az2 | 13 | 0% | 3.0 | 3 (09-03 14:26Z) |
| ap-northeast-1 apne1-az4 | 27 | 100% | 9.0 | 9 (09-03 18:33Z) |
| ap-northeast-2 apne2-az1 | 36 | 100% | 9.0 | 9 (09-03 18:33Z) |
| ap-northeast-2 apne2-az2 | 2 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-northeast-2 apne2-az3 | 36 | 100% | 9.0 | 9 (09-03 18:33Z) |
| ap-northeast-2 apne2-az4 | 18 | 0% | 3.0 | 3 (09-03 14:26Z) |
| ap-south-1 aps1-az1 | 6 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-south-1 aps1-az2 | 16 | 0% | 3.0 | 3 (09-02 21:46Z) |
| ap-south-1 aps1-az3 | 9 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-southeast-2 apse2-az1 | 6 | 50% | 5.7 | 3 (09-03 18:33Z) |
| ap-southeast-2 apse2-az3 | 2 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-southeast-3 apse3-az3 | 17 | 0% | 3.0 | 3 (09-03 14:26Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 11 | 100% | 8.9 | 8 (09-03 04:19Z) |
| us-east-1 use1-az4 | 11 | 100% | 9.0 | 9 (09-03 09:40Z) |
| us-east-1 use1-az5 | 14 | 100% | 8.9 | 8 (09-03 09:40Z) |
| us-east-1 use1-az6 | 12 | 100% | 9.0 | 9 (09-03 04:19Z) |
| us-east-2 use2-az1 | 11 | 100% | 8.9 | 9 (09-02 14:23Z) |
| us-east-2 use2-az2 | 20 | 90% | 8.2 | 9 (09-03 09:40Z) |
| us-east-2 use2-az3 | 13 | 62% | 6.4 | 3 (09-03 09:40Z) |
| us-west-2 usw2-az1 | 12 | 92% | 8.5 | 9 (09-03 14:26Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 12 | 100% | 9.0 | 9 (09-02 14:23Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.742500 | 2026-09-03T18:33:53Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-09-03T18:33:53Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.824400 | 2026-09-03T18:33:53Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.382300 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.340100 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.286000 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.261700 | 2026-09-03T18:33:53Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-09-03T18:33:53Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.539900 | 2026-09-03T18:33:53Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-03T18:33:53Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.477500 | 2026-09-03T18:33:53Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-09-03T18:33:53Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747100 | 2026-09-03T18:33:53Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.476900 | 2026-09-03T18:33:53Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.925500 | 2026-09-03T18:33:53Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377200 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.932700 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1a | Windows | 0.333900 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.700800 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1b | Windows | 0.320600 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.578400 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1c | Windows | 0.317800 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.480300 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1d | Windows | 0.318700 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.517700 | 2026-09-03T18:33:53Z |
| us-east-1 | us-east-1f | Windows | 0.317100 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.369800 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.359400 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.352400 | 2026-09-03T18:33:53Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563300 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.524900 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527600 | 2026-09-03T18:33:53Z |
| us-west-2 | us-west-2c | Windows | 0.332000 | 2026-09-03T18:33:53Z |
