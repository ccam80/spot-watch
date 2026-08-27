# Spot placement score log

Generated 2026-08-27 23:46 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 5 | 0% | 1.0 | 1 (08-27 23:46Z) |
| ap-northeast-1 | 5 | 0% | 1.4 | 1 (08-27 23:46Z) |
| ap-northeast-2 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-south-1 | 5 | 0% | 2.6 | 3 (08-27 23:46Z) |
| ap-southeast-2 | 5 | 0% | 1.0 | 1 (08-27 23:46Z) |
| ap-southeast-3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| us-east-1 | 5 | 0% | 2.8 | 3 (08-27 23:46Z) |
| us-east-2 | 5 | 0% | 1.0 | 1 (08-27 23:46Z) |
| us-west-2 | 5 | 0% | 1.8 | 2 (08-27 23:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                   11111
ap-northeast-1                                              11131
ap-northeast-2                                              33333
ap-south-1                                                  33313
ap-southeast-2                                              11111
ap-southeast-3                                              33333
us-east-1                                                   32333
us-east-2                                                   11111
us-west-2                                                   22122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 1 | 1 | 1 |
| ap-northeast-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 1 | 1 | 1 |
| ap-northeast-2 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 3 | 3 | 3 |
| ap-south-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 1 | 1 | 1 |
| ap-southeast-3 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 3 | 2 | 3 |
| us-east-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 1 | 1 | 1 |
| us-west-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 2 | · | · | · | · | · | · | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 3 | 0% | 1.0 | 1 (08-27 23:46Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 2 | 0% | 2.0 | 1 (08-27 23:46Z) |
| ap-northeast-2 apne2-az1 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-northeast-2 apne2-az3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-south-1 aps1-az1 | 3 | 0% | 2.3 | 3 (08-27 23:46Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-southeast-3 apse3-az1 | 2 | 0% | 1.0 | 1 (08-27 23:46Z) |
| ap-southeast-3 apse3-az3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| us-east-1 use1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az2 | 3 | 0% | 1.0 | 1 (08-27 23:46Z) |
| us-east-1 use1-az4 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az6 | 3 | 0% | 1.0 | 1 (08-27 14:06Z) |
| us-east-2 use2-az1 | 1 | 0% | 1.0 | 1 (08-27 03:05Z) |
| us-east-2 use2-az2 | 2 | 0% | 1.0 | 1 (08-27 14:06Z) |
| us-west-2 usw2-az2 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-west-2 usw2-az3 | 3 | 0% | 1.0 | 1 (08-27 14:06Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-northeast-1 | 5 | 80% | 7.4 | 9 (08-27 23:46Z) |
| ap-northeast-2 | 5 | 100% | 9.0 | 9 (08-27 23:46Z) |
| ap-south-1 | 5 | 0% | 2.6 | 3 (08-27 23:46Z) |
| ap-southeast-2 | 5 | 0% | 1.0 | 1 (08-27 23:46Z) |
| ap-southeast-3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| us-east-1 | 5 | 100% | 6.8 | 8 (08-27 23:46Z) |
| us-east-2 | 5 | 60% | 6.0 | 1 (08-27 23:46Z) |
| us-west-2 | 5 | 0% | 3.4 | 3 (08-27 23:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                   33333
ap-northeast-1                                              99199
ap-northeast-2                                              99999
ap-south-1                                                  33313
ap-southeast-2                                              11111
ap-southeast-3                                              33333
us-east-1                                                   76678
us-east-2                                                   92991
us-west-2                                                   44243
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 3 | 3 | 3 |
| ap-northeast-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 9 | · | · | · | · | · | · | 9 | 9 | 9 |
| ap-northeast-2 | · | · | · | 9 | · | · | · | · | · | · | · | · | · | · | 9 | · | · | · | · | · | · | 9 | 9 | 9 |
| ap-south-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 3 | 3 | 3 |
| ap-southeast-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | 1 | · | · | · | · | · | · | 1 | 1 | 1 |
| ap-southeast-3 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | 3 | · | · | · | · | · | · | 3 | 3 | 3 |
| us-east-1 | · | · | · | 6 | · | · | · | · | · | · | · | · | · | · | 7 | · | · | · | · | · | · | 7 | 6 | 8 |
| us-east-2 | · | · | · | 9 | · | · | · | · | · | · | · | · | · | · | 9 | · | · | · | · | · | · | 9 | 2 | 1 |
| us-west-2 | · | · | · | 2 | · | · | · | · | · | · | · | · | · | · | 4 | · | · | · | · | · | · | 4 | 4 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 2 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-east-1 ape1-az2 | 3 | 0% | 3.0 | 3 (08-27 14:06Z) |
| ap-east-1 ape1-az3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-northeast-1 apne1-az1 | 4 | 100% | 9.0 | 9 (08-27 23:46Z) |
| ap-northeast-1 apne1-az2 | 4 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-northeast-1 apne1-az4 | 4 | 100% | 9.0 | 9 (08-27 23:46Z) |
| ap-northeast-2 apne2-az1 | 5 | 100% | 9.0 | 9 (08-27 23:46Z) |
| ap-northeast-2 apne2-az3 | 5 | 100% | 9.0 | 9 (08-27 23:46Z) |
| ap-northeast-2 apne2-az4 | 2 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-south-1 aps1-az2 | 4 | 0% | 3.0 | 3 (08-27 23:46Z) |
| ap-south-1 aps1-az3 | 2 | 0% | 3.0 | 3 (08-26 22:23Z) |
| ap-southeast-3 apse3-az3 | 5 | 0% | 3.0 | 3 (08-27 23:46Z) |
| us-east-2 use2-az1 | 1 | 100% | 9.0 | 9 (08-27 03:05Z) |
| us-east-2 use2-az2 | 2 | 100% | 9.0 | 9 (08-27 14:06Z) |
| us-east-2 use2-az3 | 2 | 100% | 9.0 | 9 (08-27 14:06Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.812400 | 2026-08-27T23:46:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-27T23:46:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.848900 | 2026-08-27T23:46:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.329900 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.417700 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.392900 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.354000 | 2026-08-27T23:46:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-27T23:46:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.507400 | 2026-08-27T23:46:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-27T23:46:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.471500 | 2026-08-27T23:46:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-27T23:46:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.724200 | 2026-08-27T23:46:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.444700 | 2026-08-27T23:46:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.809800 | 2026-08-27T23:46:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.376500 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.959500 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1a | Windows | 0.351300 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.760200 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1b | Windows | 0.330300 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.650900 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1c | Windows | 0.325500 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.574500 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1d | Windows | 0.327900 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.554100 | 2026-08-27T23:46:00Z |
| us-east-1 | us-east-1f | Windows | 0.324500 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.385900 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.368700 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.342300 | 2026-08-27T23:46:00Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.530500 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.509300 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.505200 | 2026-08-27T23:46:00Z |
| us-west-2 | us-west-2c | Windows | 0.330900 | 2026-08-27T23:46:00Z |
