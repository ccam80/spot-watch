# Spot placement score log

Generated 2026-08-29 16:40 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 10 | 0% | 1.0 | 1 (08-29 16:40Z) |
| ap-northeast-1 | 10 | 0% | 2.0 | 3 (08-29 16:40Z) |
| ap-northeast-2 | 10 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 | 10 | 0% | 2.6 | 3 (08-29 16:40Z) |
| ap-southeast-2 | 10 | 0% | 1.0 | 1 (08-29 16:40Z) |
| ap-southeast-3 | 10 | 0% | 2.9 | 3 (08-29 16:40Z) |
| us-east-1 | 10 | 0% | 2.0 | 1 (08-29 16:40Z) |
| us-east-2 | 10 | 0% | 1.4 | 1 (08-29 16:40Z) |
| us-west-2 | 10 | 0% | 1.7 | 1 (08-29 16:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                              1111111111
ap-northeast-1                                         1113113333
ap-northeast-2                                         3333333333
ap-south-1                                             3331313333
ap-southeast-2                                         1111111111
ap-southeast-3                                         3333333323
us-east-1                                              3233321111
us-east-2                                              1111131131
us-west-2                                              2212221131
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | · | · | 1 | 1 | 1 |
| ap-northeast-1 | · | · | · | 1 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | · | · | 1 | 2 | 1 |
| ap-northeast-2 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| ap-south-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 1 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | · | · | 1 | 1 | 1 |
| ap-southeast-3 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 3 | 1 | · | · | · | · | · | · | 2 | · | · | 3 | · | 1 | · | · | · | · | 3 | 2 | 3 |
| us-east-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 3 | · | · | 1 | · | 1 | · | · | · | · | 1 | 1 | 1 |
| us-west-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 2 | · | · | 2 | · | 1 | · | · | · | · | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 6 | 0% | 2.7 | 3 (08-29 16:40Z) |
| ap-northeast-2 apne2-az1 | 10 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-northeast-2 apne2-az3 | 10 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-northeast-2 apne2-az4 | 10 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 6 | 0% | 2.2 | 2 (08-29 16:40Z) |
| ap-south-1 aps1-az3 | 8 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-southeast-3 apse3-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-southeast-3 apse3-az3 | 9 | 0% | 3.0 | 3 (08-29 16:40Z) |
| us-east-1 use1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az2 | 6 | 0% | 1.0 | 1 (08-29 16:40Z) |
| us-east-1 use1-az4 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az6 | 5 | 0% | 1.0 | 1 (08-29 16:40Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 4 | 0% | 1.5 | 1 (08-29 16:40Z) |
| us-east-2 use2-az3 | 2 | 0% | 2.5 | 3 (08-29 11:36Z) |
| us-west-2 usw2-az1 | 1 | 0% | 1.0 | 1 (08-29 04:07Z) |
| us-west-2 usw2-az2 | 2 | 0% | 2.0 | 3 (08-29 11:36Z) |
| us-west-2 usw2-az3 | 5 | 0% | 1.4 | 3 (08-29 11:36Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 10 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-northeast-1 | 10 | 90% | 8.2 | 9 (08-29 16:40Z) |
| ap-northeast-2 | 10 | 100% | 9.0 | 9 (08-29 16:40Z) |
| ap-south-1 | 10 | 0% | 2.8 | 3 (08-29 16:40Z) |
| ap-southeast-2 | 10 | 40% | 4.0 | 9 (08-29 16:40Z) |
| ap-southeast-3 | 10 | 0% | 2.9 | 3 (08-29 16:40Z) |
| us-east-1 | 10 | 100% | 7.2 | 9 (08-29 16:40Z) |
| us-east-2 | 10 | 70% | 6.8 | 9 (08-29 16:40Z) |
| us-west-2 | 10 | 20% | 4.0 | 2 (08-29 16:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                              3333333333
ap-northeast-1                                         9919999999
ap-northeast-2                                         9999999999
ap-south-1                                             3331333333
ap-southeast-2                                         1111119799
ap-southeast-3                                         3333333323
us-east-1                                              7667875899
us-east-2                                              9299192999
us-west-2                                              4424392192
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| ap-northeast-1 | · | · | · | 1 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | · | · | 9 | 9 | 9 |
| ap-northeast-2 | · | · | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | · | · | 9 | 9 | 9 |
| ap-south-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 1 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | 7 | · | · | · | · | · | · | 5 | · | · | 1 | · | 9 | · | · | · | · | 1 | 5 | 1 |
| ap-southeast-3 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | · | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 6 | 8 | · | · | · | · | · | · | 8 | · | · | 7 | · | 9 | · | · | · | · | 7 | 6 | 8 |
| us-east-2 | · | · | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | · | · | 9 | 2 | 1 |
| us-west-2 | · | · | · | 2 | 1 | · | · | · | · | · | · | 9 | · | · | 4 | · | 2 | · | · | · | · | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 4 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 7 | 100% | 9.0 | 9 (08-29 16:40Z) |
| ap-northeast-2 apne2-az1 | 9 | 100% | 9.0 | 9 (08-29 16:40Z) |
| ap-northeast-2 apne2-az3 | 9 | 100% | 9.0 | 9 (08-29 16:40Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-south-1 aps1-az3 | 3 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-southeast-2 apse2-az1 | 3 | 100% | 8.3 | 9 (08-29 11:36Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-east-1 use1-az2 | 2 | 100% | 9.0 | 9 (08-29 16:40Z) |
| us-east-1 use1-az4 | 2 | 100% | 9.0 | 9 (08-29 16:40Z) |
| us-east-1 use1-az5 | 1 | 100% | 9.0 | 9 (08-29 16:40Z) |
| us-east-1 use1-az6 | 2 | 100% | 9.0 | 9 (08-29 16:40Z) |
| us-east-2 use2-az1 | 2 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-east-2 use2-az2 | 5 | 100% | 8.8 | 8 (08-29 16:40Z) |
| us-east-2 use2-az3 | 5 | 100% | 8.2 | 9 (08-29 11:36Z) |
| us-west-2 usw2-az1 | 1 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-west-2 usw2-az2 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-west-2 usw2-az3 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.789500 | 2026-08-29T16:40:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-29T16:40:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.834000 | 2026-08-29T16:40:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.340800 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.400300 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.367200 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.340300 | 2026-08-29T16:40:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-29T16:40:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.506800 | 2026-08-29T16:40:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-29T16:40:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.469900 | 2026-08-29T16:40:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-29T16:40:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.739900 | 2026-08-29T16:40:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.443000 | 2026-08-29T16:40:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.822100 | 2026-08-29T16:40:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377300 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.953300 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1a | Windows | 0.346700 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.736300 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1b | Windows | 0.328600 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.632700 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1c | Windows | 0.325800 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.537200 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1d | Windows | 0.328200 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.535500 | 2026-08-29T16:40:12Z |
| us-east-1 | us-east-1f | Windows | 0.324500 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.372700 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.356100 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.345900 | 2026-08-29T16:40:12Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.524200 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496800 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.497100 | 2026-08-29T16:40:12Z |
| us-west-2 | us-west-2c | Windows | 0.330500 | 2026-08-29T16:40:12Z |
