# Spot placement score log

Generated 2026-08-30 08:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 14 | 0% | 1.0 | 1 (08-30 08:15Z) |
| ap-northeast-1 | 14 | 0% | 2.0 | 1 (08-30 08:15Z) |
| ap-northeast-2 | 14 | 0% | 3.0 | 3 (08-30 08:15Z) |
| ap-south-1 | 14 | 0% | 2.6 | 1 (08-30 08:15Z) |
| ap-southeast-2 | 14 | 0% | 1.0 | 1 (08-30 08:15Z) |
| ap-southeast-3 | 14 | 0% | 2.6 | 1 (08-30 08:15Z) |
| us-east-1 | 14 | 0% | 1.9 | 1 (08-30 08:15Z) |
| us-east-2 | 14 | 0% | 1.4 | 3 (08-30 08:15Z) |
| us-west-2 | 14 | 0% | 1.5 | 1 (08-30 08:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                          11111111111111
ap-northeast-1                                     11131133331331
ap-northeast-2                                     33333333333333
ap-south-1                                         33313133333331
ap-southeast-2                                     11111111111111
ap-southeast-3                                     33333333232321
us-east-1                                          32333211113111
us-east-2                                          11111311311113
us-west-2                                          22122211311111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | · | 3 | · | 1 | 3 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | · | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 1 | · | 3 | 1 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 1 | · | · | 3 | · | 3 | 1 | 3 |
| us-east-2 | · | 1 | · | 1 | 1 | · | · | · | 3 | · | · | 3 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| us-west-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | · | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 7 | 0% | 1.0 | 1 (08-30 08:15Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 9 | 0% | 2.6 | 1 (08-30 08:15Z) |
| ap-northeast-2 apne2-az1 | 14 | 0% | 3.0 | 3 (08-30 08:15Z) |
| ap-northeast-2 apne2-az3 | 14 | 0% | 3.0 | 3 (08-30 08:15Z) |
| ap-northeast-2 apne2-az4 | 14 | 0% | 3.0 | 3 (08-30 08:15Z) |
| ap-south-1 aps1-az1 | 8 | 0% | 2.4 | 3 (08-29 22:37Z) |
| ap-south-1 aps1-az3 | 11 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-southeast-3 apse3-az3 | 12 | 0% | 2.8 | 2 (08-30 01:12Z) |
| us-east-1 use1-az1 | 2 | 0% | 1.0 | 1 (08-29 22:37Z) |
| us-east-1 use1-az2 | 9 | 0% | 1.2 | 1 (08-30 08:15Z) |
| us-east-1 use1-az4 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-east-1 use1-az5 | 1 | 0% | 3.0 | 3 (08-29 19:41Z) |
| us-east-1 use1-az6 | 8 | 0% | 1.2 | 1 (08-30 08:15Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 6 | 0% | 1.3 | 1 (08-30 08:15Z) |
| us-east-2 use2-az3 | 3 | 0% | 2.7 | 3 (08-30 08:15Z) |
| us-west-2 usw2-az1 | 1 | 0% | 1.0 | 1 (08-29 04:07Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 6 | 0% | 1.3 | 1 (08-30 08:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 14 | 0% | 3.0 | 3 (08-30 08:15Z) |
| ap-northeast-1 | 14 | 93% | 8.4 | 9 (08-30 08:15Z) |
| ap-northeast-2 | 14 | 100% | 9.0 | 9 (08-30 08:15Z) |
| ap-south-1 | 14 | 0% | 2.9 | 3 (08-30 08:15Z) |
| ap-southeast-2 | 14 | 57% | 5.4 | 9 (08-30 08:15Z) |
| ap-southeast-3 | 14 | 0% | 2.6 | 1 (08-30 08:15Z) |
| us-east-1 | 14 | 100% | 7.7 | 9 (08-30 08:15Z) |
| us-east-2 | 14 | 71% | 6.9 | 9 (08-30 08:15Z) |
| us-west-2 | 14 | 21% | 3.9 | 9 (08-30 08:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                          33333333333333
ap-northeast-1                                     99199999999999
ap-northeast-2                                     99999999999999
ap-south-1                                         33313333333333
ap-southeast-2                                     11111197999999
ap-southeast-3                                     33333333232321
us-east-1                                          76678758999999
us-east-2                                          92991929999919
us-west-2                                          44243921922229
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | · | 9 | · | 1 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | · | 9 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 9 | · | 1 | 7 | · | · | · | 9 | · | · | 5 | · | · | 1 | · | 9 | · | · | 9 | · | 1 | 6 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 9 | · | 6 | 8 | · | · | · | 9 | · | · | 8 | · | · | 7 | · | 9 | · | · | 9 | · | 7 | 7 | 8 |
| us-east-2 | · | 1 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 4 | 1 |
| us-west-2 | · | 2 | · | 2 | 1 | · | · | · | 9 | · | · | 9 | · | · | 4 | · | 2 | · | · | 2 | · | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 5 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 11 | 100% | 9.0 | 9 (08-30 08:15Z) |
| ap-northeast-2 apne2-az1 | 13 | 100% | 9.0 | 9 (08-30 08:15Z) |
| ap-northeast-2 apne2-az3 | 13 | 100% | 9.0 | 9 (08-30 08:15Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 6 | 100% | 9.0 | 9 (08-30 08:15Z) |
| us-east-1 use1-az4 | 5 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az5 | 4 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az6 | 6 | 100% | 9.0 | 9 (08-30 08:15Z) |
| us-east-2 use2-az1 | 4 | 100% | 8.8 | 9 (08-30 08:15Z) |
| us-east-2 use2-az2 | 8 | 75% | 7.5 | 9 (08-30 08:15Z) |
| us-east-2 use2-az3 | 7 | 100% | 8.4 | 9 (08-30 08:15Z) |
| us-west-2 usw2-az1 | 1 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-west-2 usw2-az2 | 2 | 100% | 9.0 | 9 (08-30 08:15Z) |
| us-west-2 usw2-az3 | 2 | 100% | 9.0 | 9 (08-30 08:15Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.779600 | 2026-08-30T08:15:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-30T08:15:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.833900 | 2026-08-30T08:15:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.345100 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.392600 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.358100 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.326500 | 2026-08-30T08:15:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-30T08:15:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.514500 | 2026-08-30T08:15:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-30T08:15:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.467000 | 2026-08-30T08:15:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-30T08:15:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.738000 | 2026-08-30T08:15:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.447700 | 2026-08-30T08:15:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.837100 | 2026-08-30T08:15:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.376800 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.952200 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1a | Windows | 0.345600 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.730900 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1b | Windows | 0.328000 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.629400 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1c | Windows | 0.325200 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.527300 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1d | Windows | 0.327900 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.533000 | 2026-08-30T08:15:12Z |
| us-east-1 | us-east-1f | Windows | 0.324200 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.370700 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.355500 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.347000 | 2026-08-30T08:15:12Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.528700 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498400 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.500900 | 2026-08-30T08:15:12Z |
| us-west-2 | us-west-2c | Windows | 0.330900 | 2026-08-30T08:15:12Z |
