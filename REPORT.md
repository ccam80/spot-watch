# Spot placement score log

Generated 2026-08-30 21:53 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 17 | 0% | 1.0 | 1 (08-30 21:53Z) |
| ap-northeast-1 | 17 | 0% | 1.9 | 1 (08-30 21:53Z) |
| ap-northeast-2 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-south-1 | 17 | 0% | 2.6 | 3 (08-30 21:53Z) |
| ap-southeast-2 | 17 | 0% | 1.0 | 1 (08-30 21:53Z) |
| ap-southeast-3 | 17 | 0% | 2.5 | 3 (08-30 21:53Z) |
| us-east-1 | 17 | 0% | 1.7 | 1 (08-30 21:53Z) |
| us-east-2 | 17 | 0% | 1.5 | 1 (08-30 21:53Z) |
| us-west-2 | 17 | 0% | 1.6 | 3 (08-30 21:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                       11111111111111111
ap-northeast-1                                  11131133331331311
ap-northeast-2                                  33333333333333333
ap-south-1                                      33313133333331333
ap-southeast-2                                  11111111111111111
ap-southeast-3                                  33333333232321113
us-east-1                                       32333211113111111
us-east-2                                       11111311311113311
us-west-2                                       22122211311111313
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | · | 3 | · | 1 | 3 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | 1 | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 1 | · | 3 | 1 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | 1 | 3 | · | 2 | 1 | 3 |
| us-east-2 | · | 1 | · | 1 | 1 | · | · | · | 3 | · | · | 3 | · | · | 2 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| us-west-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 8 | 0% | 1.0 | 1 (08-30 21:53Z) |
| ap-east-1 ape1-az2 | 1 | 0% | 1.0 | 1 (08-30 18:34Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 12 | 0% | 2.3 | 1 (08-30 21:53Z) |
| ap-northeast-2 apne2-az1 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-northeast-2 apne2-az3 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-northeast-2 apne2-az4 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-south-1 aps1-az1 | 9 | 0% | 2.2 | 1 (08-30 14:23Z) |
| ap-south-1 aps1-az3 | 14 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-southeast-2 apse2-az1 | 1 | 0% | 1.0 | 1 (08-30 18:34Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 1.0 | 1 (08-30 18:34Z) |
| ap-southeast-3 apse3-az1 | 6 | 0% | 1.0 | 1 (08-30 21:53Z) |
| ap-southeast-3 apse3-az3 | 13 | 0% | 2.8 | 3 (08-30 21:53Z) |
| us-east-1 use1-az1 | 2 | 0% | 1.0 | 1 (08-29 22:37Z) |
| us-east-1 use1-az2 | 10 | 0% | 1.2 | 1 (08-30 21:53Z) |
| us-east-1 use1-az4 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-east-1 use1-az5 | 2 | 0% | 2.0 | 1 (08-30 18:34Z) |
| us-east-1 use1-az6 | 9 | 0% | 1.2 | 1 (08-30 14:23Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 6 | 0% | 1.3 | 1 (08-30 08:15Z) |
| us-east-2 use2-az3 | 4 | 0% | 2.8 | 3 (08-30 14:23Z) |
| us-west-2 usw2-az1 | 4 | 0% | 2.0 | 3 (08-30 21:53Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 7 | 0% | 1.6 | 3 (08-30 14:23Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-northeast-1 | 17 | 94% | 8.5 | 9 (08-30 21:53Z) |
| ap-northeast-2 | 17 | 100% | 9.0 | 9 (08-30 21:53Z) |
| ap-south-1 | 17 | 0% | 2.9 | 3 (08-30 21:53Z) |
| ap-southeast-2 | 17 | 59% | 5.7 | 3 (08-30 21:53Z) |
| ap-southeast-3 | 17 | 0% | 2.5 | 3 (08-30 21:53Z) |
| us-east-1 | 17 | 100% | 7.9 | 9 (08-30 21:53Z) |
| us-east-2 | 17 | 65% | 6.4 | 2 (08-30 21:53Z) |
| us-west-2 | 17 | 35% | 4.8 | 9 (08-30 21:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                       33333333333333333
ap-northeast-1                                  99199999999999999
ap-northeast-2                                  99999999999999999
ap-south-1                                      33313333333333333
ap-southeast-2                                  11111197999999993
ap-southeast-3                                  33333333232321113
us-east-1                                       76678758999999999
us-east-2                                       92991929999919922
us-west-2                                       44243921922229999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | · | 9 | · | 1 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | · | 9 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 9 | · | 1 | 7 | · | · | · | 9 | · | · | 5 | · | · | 5 | · | 9 | · | 9 | 9 | · | 2 | 6 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 9 | · | 6 | 8 | · | · | · | 9 | · | · | 8 | · | · | 8 | · | 9 | · | 9 | 9 | · | 8 | 7 | 8 |
| us-east-2 | · | 1 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 2 | 9 | · | 6 | 4 | 1 |
| us-west-2 | · | 2 | · | 2 | 1 | · | · | · | 9 | · | · | 9 | · | · | 6 | · | 2 | · | 9 | 2 | · | 6 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 5 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 14 | 100% | 9.0 | 9 (08-30 21:53Z) |
| ap-northeast-2 apne2-az1 | 16 | 100% | 9.0 | 9 (08-30 21:53Z) |
| ap-northeast-2 apne2-az3 | 16 | 100% | 9.0 | 9 (08-30 21:53Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 8 | 100% | 9.0 | 9 (08-30 21:53Z) |
| us-east-1 use1-az4 | 7 | 100% | 9.0 | 9 (08-30 21:53Z) |
| us-east-1 use1-az5 | 7 | 100% | 9.0 | 9 (08-30 21:53Z) |
| us-east-1 use1-az6 | 9 | 100% | 9.0 | 9 (08-30 21:53Z) |
| us-east-2 use2-az1 | 5 | 100% | 8.8 | 9 (08-30 14:23Z) |
| us-east-2 use2-az2 | 9 | 78% | 7.7 | 9 (08-30 14:23Z) |
| us-east-2 use2-az3 | 7 | 100% | 8.4 | 9 (08-30 08:15Z) |
| us-west-2 usw2-az1 | 4 | 75% | 7.5 | 9 (08-30 21:53Z) |
| us-west-2 usw2-az2 | 5 | 100% | 9.0 | 9 (08-30 21:53Z) |
| us-west-2 usw2-az3 | 5 | 100% | 9.0 | 9 (08-30 21:53Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.776300 | 2026-08-30T21:53:33Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-30T21:53:33Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.839300 | 2026-08-30T21:53:33Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.345400 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.391400 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.346600 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.316200 | 2026-08-30T21:53:33Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-30T21:53:33Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.518000 | 2026-08-30T21:53:33Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-30T21:53:33Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.469000 | 2026-08-30T21:53:33Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-30T21:53:33Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.745900 | 2026-08-30T21:53:33Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.454700 | 2026-08-30T21:53:33Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.847600 | 2026-08-30T21:53:33Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.376600 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.951400 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1a | Windows | 0.346100 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.726100 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1b | Windows | 0.327900 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.621900 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1c | Windows | 0.325400 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.524300 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1d | Windows | 0.327700 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.532900 | 2026-08-30T21:53:33Z |
| us-east-1 | us-east-1f | Windows | 0.324100 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.373100 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.355300 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.347300 | 2026-08-30T21:53:33Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.537400 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.502900 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.504600 | 2026-08-30T21:53:33Z |
| us-west-2 | us-west-2c | Windows | 0.331700 | 2026-08-30T21:53:33Z |
