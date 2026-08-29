# Spot placement score log

Generated 2026-08-29 19:41 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 11 | 0% | 1.0 | 1 (08-29 19:41Z) |
| ap-northeast-1 | 11 | 0% | 1.9 | 1 (08-29 19:41Z) |
| ap-northeast-2 | 11 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 | 11 | 0% | 2.6 | 3 (08-29 19:41Z) |
| ap-southeast-2 | 11 | 0% | 1.0 | 1 (08-29 19:41Z) |
| ap-southeast-3 | 11 | 0% | 2.8 | 2 (08-29 19:41Z) |
| us-east-1 | 11 | 0% | 2.1 | 3 (08-29 19:41Z) |
| us-east-2 | 11 | 0% | 1.4 | 1 (08-29 19:41Z) |
| us-west-2 | 11 | 0% | 1.6 | 1 (08-29 19:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                             11111111111
ap-northeast-1                                        11131133331
ap-northeast-2                                        33333333333
ap-south-1                                            33313133333
ap-southeast-2                                        11111111111
ap-southeast-3                                        33333333232
us-east-1                                             32333211113
us-east-2                                             11111311311
us-west-2                                             22122211311
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | · | · | · | 1 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-south-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 3 | 1 | · | · | · | · | · | · | 2 | · | · | 3 | · | 1 | · | · | 3 | · | 3 | 2 | 3 |
| us-east-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 3 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| us-west-2 | · | · | · | 1 | 1 | · | · | · | · | · | · | 2 | · | · | 2 | · | 1 | · | · | 1 | · | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 6 | 0% | 2.7 | 3 (08-29 16:40Z) |
| ap-northeast-2 apne2-az1 | 11 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-northeast-2 apne2-az3 | 11 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-northeast-2 apne2-az4 | 11 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az1 | 7 | 0% | 2.3 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 9 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-southeast-3 apse3-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-southeast-3 apse3-az3 | 10 | 0% | 2.9 | 2 (08-29 19:41Z) |
| us-east-1 use1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az2 | 7 | 0% | 1.3 | 3 (08-29 19:41Z) |
| us-east-1 use1-az4 | 2 | 0% | 2.0 | 3 (08-29 19:41Z) |
| us-east-1 use1-az5 | 1 | 0% | 3.0 | 3 (08-29 19:41Z) |
| us-east-1 use1-az6 | 6 | 0% | 1.3 | 3 (08-29 19:41Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 4 | 0% | 1.5 | 1 (08-29 16:40Z) |
| us-east-2 use2-az3 | 2 | 0% | 2.5 | 3 (08-29 11:36Z) |
| us-west-2 usw2-az1 | 1 | 0% | 1.0 | 1 (08-29 04:07Z) |
| us-west-2 usw2-az2 | 2 | 0% | 2.0 | 3 (08-29 11:36Z) |
| us-west-2 usw2-az3 | 5 | 0% | 1.4 | 3 (08-29 11:36Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 11 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-northeast-1 | 11 | 91% | 8.3 | 9 (08-29 19:41Z) |
| ap-northeast-2 | 11 | 100% | 9.0 | 9 (08-29 19:41Z) |
| ap-south-1 | 11 | 0% | 2.8 | 3 (08-29 19:41Z) |
| ap-southeast-2 | 11 | 45% | 4.5 | 9 (08-29 19:41Z) |
| ap-southeast-3 | 11 | 0% | 2.8 | 2 (08-29 19:41Z) |
| us-east-1 | 11 | 100% | 7.4 | 9 (08-29 19:41Z) |
| us-east-2 | 11 | 73% | 7.0 | 9 (08-29 19:41Z) |
| us-west-2 | 11 | 18% | 3.8 | 2 (08-29 19:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                             33333333333
ap-northeast-1                                        99199999999
ap-northeast-2                                        99999999999
ap-south-1                                            33313333333
ap-southeast-2                                        11111197999
ap-southeast-3                                        33333333232
us-east-1                                             76678758999
us-east-2                                             92991929999
us-west-2                                             44243921922
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | · | · | · | 1 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | · | · | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-south-1 | · | · | · | 3 | 3 | · | · | · | · | · | · | 3 | · | · | 1 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | 7 | · | · | · | · | · | · | 5 | · | · | 1 | · | 9 | · | · | 9 | · | 1 | 5 | 1 |
| ap-southeast-3 | · | · | · | 3 | 3 | · | · | · | · | · | · | 2 | · | · | 3 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 6 | 8 | · | · | · | · | · | · | 8 | · | · | 7 | · | 9 | · | · | 9 | · | 7 | 6 | 8 |
| us-east-2 | · | · | · | 9 | 9 | · | · | · | · | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 2 | 1 |
| us-west-2 | · | · | · | 2 | 1 | · | · | · | · | · | · | 9 | · | · | 4 | · | 2 | · | · | 2 | · | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 4 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 8 | 100% | 9.0 | 9 (08-29 19:41Z) |
| ap-northeast-2 apne2-az1 | 10 | 100% | 9.0 | 9 (08-29 19:41Z) |
| ap-northeast-2 apne2-az3 | 10 | 100% | 9.0 | 9 (08-29 19:41Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 3 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-southeast-2 apse2-az1 | 3 | 100% | 8.3 | 9 (08-29 11:36Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 3 | 100% | 9.0 | 9 (08-29 19:41Z) |
| us-east-1 use1-az4 | 3 | 100% | 9.0 | 9 (08-29 19:41Z) |
| us-east-1 use1-az5 | 2 | 100% | 9.0 | 9 (08-29 19:41Z) |
| us-east-1 use1-az6 | 3 | 100% | 9.0 | 9 (08-29 19:41Z) |
| us-east-2 use2-az1 | 2 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-east-2 use2-az2 | 6 | 83% | 8.0 | 4 (08-29 19:41Z) |
| us-east-2 use2-az3 | 5 | 100% | 8.2 | 9 (08-29 11:36Z) |
| us-west-2 usw2-az1 | 1 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-west-2 usw2-az2 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |
| us-west-2 usw2-az3 | 1 | 100% | 9.0 | 9 (08-29 11:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.786200 | 2026-08-29T19:41:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-29T19:41:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.834000 | 2026-08-29T19:41:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.343000 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.400300 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.367200 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.333800 | 2026-08-29T19:41:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-29T19:41:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.506800 | 2026-08-29T19:41:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-29T19:41:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.468300 | 2026-08-29T19:41:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-29T19:41:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.739900 | 2026-08-29T19:41:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.443000 | 2026-08-29T19:41:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.822100 | 2026-08-29T19:41:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377300 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.953300 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1a | Windows | 0.346500 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.736300 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1b | Windows | 0.328600 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.632000 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1c | Windows | 0.325800 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.537200 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1d | Windows | 0.328200 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.535500 | 2026-08-29T19:41:14Z |
| us-east-1 | us-east-1f | Windows | 0.324500 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.372100 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.356100 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.345900 | 2026-08-29T19:41:14Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.528700 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496800 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.497100 | 2026-08-29T19:41:14Z |
| us-west-2 | us-west-2c | Windows | 0.330800 | 2026-08-29T19:41:14Z |
