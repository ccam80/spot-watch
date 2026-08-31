# Spot placement score log

Generated 2026-08-31 15:02 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 20 | 0% | 1.0 | 1 (08-31 15:02Z) |
| ap-northeast-1 | 20 | 0% | 1.9 | 3 (08-31 15:02Z) |
| ap-northeast-2 | 20 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-south-1 | 20 | 0% | 2.5 | 1 (08-31 15:02Z) |
| ap-southeast-2 | 20 | 0% | 1.0 | 1 (08-31 15:02Z) |
| ap-southeast-3 | 20 | 0% | 2.3 | 1 (08-31 15:02Z) |
| us-east-1 | 20 | 0% | 1.8 | 2 (08-31 15:02Z) |
| us-east-2 | 20 | 0% | 1.4 | 1 (08-31 15:02Z) |
| us-west-2 | 20 | 0% | 1.8 | 1 (08-31 15:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                    11111111111111111111
ap-northeast-1                               11131133331331311113
ap-northeast-2                               33333333333333333333
ap-south-1                                   33313133333331333311
ap-southeast-2                               11111111111111111111
ap-southeast-3                               33333333232321113211
us-east-1                                    32333211113111111312
us-east-2                                    11111311311113311111
us-west-2                                    22122211311111313331
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 3 | 3 | 3 | · | 1 | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | 3 | 1 | · | 3 | 1 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 2 | 1 | · | 1 | 3 | · | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| us-west-2 | 3 | 1 | · | 1 | 1 | · | 3 | · | 1 | · | · | 2 | · | · | 2 | 1 | 1 | · | 1 | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 9 | 0% | 1.0 | 1 (08-31 15:02Z) |
| ap-east-1 ape1-az2 | 2 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-northeast-1 apne1-az1 | 2 | 0% | 1.0 | 1 (08-31 00:28Z) |
| ap-northeast-1 apne1-az4 | 14 | 0% | 2.3 | 3 (08-31 15:02Z) |
| ap-northeast-2 apne2-az1 | 19 | 0% | 2.9 | 3 (08-31 15:02Z) |
| ap-northeast-2 apne2-az3 | 18 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-northeast-2 apne2-az4 | 20 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-south-1 aps1-az1 | 10 | 0% | 2.1 | 1 (08-31 15:02Z) |
| ap-south-1 aps1-az3 | 15 | 0% | 3.0 | 3 (08-31 00:28Z) |
| ap-southeast-2 apse2-az1 | 2 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 1.0 | 1 (08-30 18:34Z) |
| ap-southeast-3 apse3-az1 | 7 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-3 apse3-az3 | 14 | 0% | 2.8 | 2 (08-31 00:28Z) |
| us-east-1 use1-az1 | 3 | 0% | 1.0 | 1 (08-31 00:28Z) |
| us-east-1 use1-az2 | 12 | 0% | 1.2 | 1 (08-31 15:02Z) |
| us-east-1 use1-az4 | 4 | 0% | 2.0 | 3 (08-31 00:28Z) |
| us-east-1 use1-az5 | 4 | 0% | 2.0 | 1 (08-31 06:58Z) |
| us-east-1 use1-az6 | 11 | 0% | 1.4 | 1 (08-31 15:02Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 7 | 0% | 1.3 | 1 (08-31 15:02Z) |
| us-east-2 use2-az3 | 5 | 0% | 2.4 | 1 (08-31 06:58Z) |
| us-west-2 usw2-az1 | 5 | 0% | 2.2 | 3 (08-31 00:28Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 10 | 0% | 1.8 | 1 (08-31 15:02Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 20 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-northeast-1 | 20 | 90% | 8.2 | 9 (08-31 15:02Z) |
| ap-northeast-2 | 20 | 100% | 9.0 | 9 (08-31 15:02Z) |
| ap-south-1 | 20 | 0% | 2.8 | 3 (08-31 15:02Z) |
| ap-southeast-2 | 20 | 50% | 5.0 | 1 (08-31 15:02Z) |
| ap-southeast-3 | 20 | 0% | 2.3 | 1 (08-31 15:02Z) |
| us-east-1 | 20 | 95% | 7.8 | 4 (08-31 15:02Z) |
| us-east-2 | 20 | 60% | 6.0 | 1 (08-31 15:02Z) |
| us-west-2 | 20 | 45% | 5.5 | 9 (08-31 15:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                    33333333333333333333
ap-northeast-1                               99199999999999999919
ap-northeast-2                               99999999999999999999
ap-south-1                                   33313333333333333313
ap-southeast-2                               11111197999999993111
ap-southeast-3                               33333333232321113211
us-east-1                                    76678758999999999994
us-east-2                                    92991929999919922191
us-west-2                                    44243921922229999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | 9 | 9 | · | 1 | 9 | · | 1 | · | 9 | · | · | 9 | · | · | 9 | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 7 | · | 1 | · | 9 | · | · | 5 | · | · | 5 | 1 | 9 | · | 9 | 9 | · | 2 | 6 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | 9 | 9 | · | 6 | 8 | · | 9 | · | 9 | · | · | 8 | · | · | 8 | 4 | 9 | · | 9 | 9 | · | 8 | 7 | 8 |
| us-east-2 | 1 | 1 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | 1 | 9 | · | 2 | 9 | · | 6 | 4 | 1 |
| us-west-2 | 9 | 2 | · | 2 | 1 | · | 9 | · | 9 | · | · | 9 | · | · | 6 | 9 | 2 | · | 9 | 2 | · | 6 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 7 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-east-1 ape1-az2 | 6 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 16 | 100% | 9.0 | 9 (08-31 15:02Z) |
| ap-northeast-2 apne2-az1 | 19 | 100% | 9.0 | 9 (08-31 15:02Z) |
| ap-northeast-2 apne2-az3 | 19 | 100% | 9.0 | 9 (08-31 15:02Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 3 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-south-1 aps1-az2 | 8 | 0% | 3.0 | 3 (08-31 15:02Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 9 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az4 | 8 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az5 | 9 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-east-1 use1-az6 | 11 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-east-2 use2-az1 | 6 | 100% | 8.8 | 9 (08-31 06:58Z) |
| us-east-2 use2-az2 | 10 | 80% | 7.8 | 9 (08-31 06:58Z) |
| us-east-2 use2-az3 | 8 | 100% | 8.5 | 9 (08-31 06:58Z) |
| us-west-2 usw2-az1 | 7 | 86% | 8.1 | 9 (08-31 15:02Z) |
| us-west-2 usw2-az2 | 8 | 100% | 9.0 | 9 (08-31 15:02Z) |
| us-west-2 usw2-az3 | 8 | 100% | 9.0 | 9 (08-31 15:02Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.777900 | 2026-08-31T15:02:27Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-31T15:02:27Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.843400 | 2026-08-31T15:02:27Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.373100 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.383600 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.338300 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.305500 | 2026-08-31T15:02:27Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-31T15:02:27Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.524900 | 2026-08-31T15:02:27Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-31T15:02:27Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.469400 | 2026-08-31T15:02:27Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-31T15:02:27Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.749000 | 2026-08-31T15:02:27Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.466300 | 2026-08-31T15:02:27Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.863900 | 2026-08-31T15:02:27Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378000 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.941900 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1a | Windows | 0.346600 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.713300 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1b | Windows | 0.327900 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.614500 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1c | Windows | 0.325200 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.525700 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1d | Windows | 0.327500 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.536600 | 2026-08-31T15:02:27Z |
| us-east-1 | us-east-1f | Windows | 0.323500 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.374000 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.356500 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.347800 | 2026-08-31T15:02:27Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.547300 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.507500 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.509600 | 2026-08-31T15:02:27Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-08-31T15:02:27Z |
