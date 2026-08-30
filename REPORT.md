# Spot placement score log

Generated 2026-08-30 01:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 13 | 0% | 1.0 | 1 (08-30 01:12Z) |
| ap-northeast-1 | 13 | 0% | 2.1 | 3 (08-30 01:12Z) |
| ap-northeast-2 | 13 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-south-1 | 13 | 0% | 2.7 | 3 (08-30 01:12Z) |
| ap-southeast-2 | 13 | 0% | 1.0 | 1 (08-30 01:12Z) |
| ap-southeast-3 | 13 | 0% | 2.8 | 2 (08-30 01:12Z) |
| us-east-1 | 13 | 0% | 1.9 | 1 (08-30 01:12Z) |
| us-east-2 | 13 | 0% | 1.3 | 1 (08-30 01:12Z) |
| us-west-2 | 13 | 0% | 1.5 | 1 (08-30 01:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                           1111111111111
ap-northeast-1                                      1113113333133
ap-northeast-2                                      3333333333333
ap-south-1                                          3331313333333
ap-southeast-2                                      1111111111111
ap-southeast-3                                      3333333323232
us-east-1                                           3233321111311
us-east-2                                           1111131131111
us-west-2                                           2212221131111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 1 | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | · | 3 | · | 1 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | · | 3 | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 1 | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 1 | · | 3 | 1 | · | · | · | · | · | · | 2 | · | · | 3 | · | 1 | · | · | 3 | · | 3 | 1 | 3 |
| us-east-2 | · | 1 | · | 1 | 1 | · | · | · | · | · | · | 3 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| us-west-2 | · | 1 | · | 1 | 1 | · | · | · | · | · | · | 2 | · | · | 2 | · | 1 | · | · | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 1.0 | 1 (08-30 01:12Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 8 | 0% | 2.8 | 3 (08-30 01:12Z) |
| ap-northeast-2 apne2-az1 | 13 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-northeast-2 apne2-az3 | 13 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-northeast-2 apne2-az4 | 13 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-south-1 aps1-az1 | 8 | 0% | 2.4 | 3 (08-29 22:37Z) |
| ap-south-1 aps1-az3 | 11 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-southeast-3 apse3-az3 | 12 | 0% | 2.8 | 2 (08-30 01:12Z) |
| us-east-1 use1-az1 | 2 | 0% | 1.0 | 1 (08-29 22:37Z) |
| us-east-1 use1-az2 | 8 | 0% | 1.2 | 1 (08-30 01:12Z) |
| us-east-1 use1-az4 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-east-1 use1-az5 | 1 | 0% | 3.0 | 3 (08-29 19:41Z) |
| us-east-1 use1-az6 | 7 | 0% | 1.3 | 1 (08-30 01:12Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 5 | 0% | 1.4 | 1 (08-30 01:12Z) |
| us-east-2 use2-az3 | 2 | 0% | 2.5 | 3 (08-29 11:36Z) |
| us-west-2 usw2-az1 | 1 | 0% | 1.0 | 1 (08-29 04:07Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 5 | 0% | 1.4 | 3 (08-29 11:36Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 13 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-northeast-1 | 13 | 92% | 8.4 | 9 (08-30 01:12Z) |
| ap-northeast-2 | 13 | 100% | 9.0 | 9 (08-30 01:12Z) |
| ap-south-1 | 13 | 0% | 2.8 | 3 (08-30 01:12Z) |
| ap-southeast-2 | 13 | 54% | 5.2 | 9 (08-30 01:12Z) |
| ap-southeast-3 | 13 | 0% | 2.8 | 2 (08-30 01:12Z) |
| us-east-1 | 13 | 100% | 7.6 | 9 (08-30 01:12Z) |
| us-east-2 | 13 | 69% | 6.7 | 1 (08-30 01:12Z) |
| us-west-2 | 13 | 15% | 3.5 | 2 (08-30 01:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                           3333333333333
ap-northeast-1                                      9919999999999
ap-northeast-2                                      9999999999999
ap-south-1                                          3331333333333
ap-southeast-2                                      1111119799999
ap-southeast-3                                      3333333323232
us-east-1                                           7667875899999
us-east-2                                           9299192999991
us-west-2                                           4424392192222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 3 | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | · | 9 | · | 1 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | · | 9 | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 9 | · | 1 | 7 | · | · | · | · | · | · | 5 | · | · | 1 | · | 9 | · | · | 9 | · | 1 | 6 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 9 | · | 6 | 8 | · | · | · | · | · | · | 8 | · | · | 7 | · | 9 | · | · | 9 | · | 7 | 7 | 8 |
| us-east-2 | · | 1 | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 4 | 1 |
| us-west-2 | · | 2 | · | 2 | 1 | · | · | · | · | · | · | 9 | · | · | 4 | · | 2 | · | · | 2 | · | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 5 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 10 | 100% | 9.0 | 9 (08-30 01:12Z) |
| ap-northeast-2 apne2-az1 | 12 | 100% | 9.0 | 9 (08-30 01:12Z) |
| ap-northeast-2 apne2-az3 | 12 | 100% | 9.0 | 9 (08-30 01:12Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 5 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az4 | 5 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az5 | 4 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az6 | 5 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-2 use2-az1 | 3 | 100% | 8.7 | 8 (08-29 22:37Z) |
| us-east-2 use2-az2 | 7 | 71% | 7.3 | 3 (08-29 22:37Z) |
| us-east-2 use2-az3 | 6 | 100% | 8.3 | 9 (08-29 22:37Z) |
| us-west-2 usw2-az1 | 1 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-west-2 usw2-az2 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-west-2 usw2-az3 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.781700 | 2026-08-30T01:12:39Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-30T01:12:39Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.833800 | 2026-08-30T01:12:39Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.343000 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.392600 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.358900 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.328100 | 2026-08-30T01:12:39Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-30T01:12:39Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.506300 | 2026-08-30T01:12:39Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-30T01:12:39Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.468300 | 2026-08-30T01:12:39Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-30T01:12:39Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.741400 | 2026-08-30T01:12:39Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.444200 | 2026-08-30T01:12:39Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.825700 | 2026-08-30T01:12:39Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377300 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.953300 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1a | Windows | 0.345500 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.733700 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1b | Windows | 0.328300 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.631200 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1c | Windows | 0.325700 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.529400 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1d | Windows | 0.328000 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.535700 | 2026-08-30T01:12:39Z |
| us-east-1 | us-east-1f | Windows | 0.324200 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.372100 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.356100 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.347600 | 2026-08-30T01:12:39Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.528700 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498700 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.501300 | 2026-08-30T01:12:39Z |
| us-west-2 | us-west-2c | Windows | 0.330900 | 2026-08-30T01:12:39Z |
