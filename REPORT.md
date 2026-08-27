# Spot placement score log

Generated 2026-08-27 03:05 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 3 | 0% | 1.0 | 1 (08-27 03:05Z) |
| ap-northeast-1 | 3 | 0% | 1.0 | 1 (08-27 03:05Z) |
| ap-northeast-2 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-south-1 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-southeast-2 | 3 | 0% | 1.0 | 1 (08-27 03:05Z) |
| ap-southeast-3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| us-east-1 | 3 | 0% | 2.7 | 3 (08-27 03:05Z) |
| us-east-2 | 3 | 0% | 1.0 | 1 (08-27 03:05Z) |
| us-west-2 | 3 | 0% | 1.7 | 1 (08-27 03:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                     111
ap-northeast-1                                                111
ap-northeast-2                                                333
ap-south-1                                                    333
ap-southeast-2                                                111
ap-southeast-3                                                333
us-east-1                                                     323
us-east-2                                                     111
us-west-2                                                     221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · |
| ap-northeast-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · |
| ap-northeast-2 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| ap-south-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| ap-southeast-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · |
| ap-southeast-3 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| us-east-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 2 | · |
| us-east-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · |
| us-west-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 2 | 2 | · |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-2 apne2-az1 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-northeast-2 apne2-az3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-northeast-2 apne2-az4 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 2.0 | 1 (08-27 03:05Z) |
| ap-south-1 aps1-az3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (08-27 03:05Z) |
| ap-southeast-3 apse3-az3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| us-east-1 use1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-east-1 use1-az4 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-east-1 use1-az6 | 2 | 0% | 1.0 | 1 (08-27 03:05Z) |
| us-east-2 use2-az1 | 1 | 0% | 1.0 | 1 (08-27 03:05Z) |
| us-east-2 use2-az2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-west-2 usw2-az2 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| us-west-2 usw2-az3 | 2 | 0% | 1.0 | 1 (08-27 03:05Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-northeast-1 | 3 | 67% | 6.3 | 1 (08-27 03:05Z) |
| ap-northeast-2 | 3 | 100% | 9.0 | 9 (08-27 03:05Z) |
| ap-south-1 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-southeast-2 | 3 | 0% | 1.0 | 1 (08-27 03:05Z) |
| ap-southeast-3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| us-east-1 | 3 | 100% | 6.3 | 6 (08-27 03:05Z) |
| us-east-2 | 3 | 67% | 6.7 | 9 (08-27 03:05Z) |
| us-west-2 | 3 | 0% | 3.3 | 2 (08-27 03:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                     333
ap-northeast-1                                                991
ap-northeast-2                                                999
ap-south-1                                                    333
ap-southeast-2                                                111
ap-southeast-3                                                333
us-east-1                                                     766
us-east-2                                                     929
us-west-2                                                     442
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| ap-northeast-1 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | 9 | · |
| ap-northeast-2 | · | · | · | 9 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | 9 | · |
| ap-south-1 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| ap-southeast-2 | · | · | · | 1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 1 | · |
| ap-southeast-3 | · | · | · | 3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | 3 | · |
| us-east-1 | · | · | · | 6 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 7 | 6 | · |
| us-east-2 | · | · | · | 9 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | 2 | · |
| us-west-2 | · | · | · | 2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 4 | 4 | · |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 1 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-east-1 ape1-az2 | 2 | 0% | 3.0 | 3 (08-26 22:23Z) |
| ap-east-1 ape1-az3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-northeast-1 apne1-az1 | 2 | 100% | 9.0 | 9 (08-26 22:23Z) |
| ap-northeast-1 apne1-az2 | 2 | 0% | 3.0 | 3 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 2 | 100% | 9.0 | 9 (08-26 22:23Z) |
| ap-northeast-2 apne2-az1 | 3 | 100% | 9.0 | 9 (08-27 03:05Z) |
| ap-northeast-2 apne2-az3 | 3 | 100% | 9.0 | 9 (08-27 03:05Z) |
| ap-northeast-2 apne2-az4 | 1 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-south-1 aps1-az2 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| ap-south-1 aps1-az3 | 2 | 0% | 3.0 | 3 (08-26 22:23Z) |
| ap-southeast-3 apse3-az3 | 3 | 0% | 3.0 | 3 (08-27 03:05Z) |
| us-east-2 use2-az1 | 1 | 100% | 9.0 | 9 (08-27 03:05Z) |
| us-east-2 use2-az2 | 1 | 100% | 9.0 | 9 (08-27 03:05Z) |
| us-east-2 use2-az3 | 1 | 100% | 9.0 | 9 (08-27 03:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.819500 | 2026-08-27T03:05:41Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-27T03:05:41Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.857900 | 2026-08-27T03:05:41Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.329900 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.424300 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.402800 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.357500 | 2026-08-27T03:05:41Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307800 | 2026-08-27T03:05:41Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.516600 | 2026-08-27T03:05:41Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-27T03:05:41Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.477500 | 2026-08-27T03:05:41Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-27T03:05:41Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718100 | 2026-08-27T03:05:41Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.454700 | 2026-08-27T03:05:41Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.826800 | 2026-08-27T03:05:41Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.374900 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.963300 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1a | Windows | 0.352800 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.774900 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1b | Windows | 0.330700 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.673600 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1c | Windows | 0.325200 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.592700 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1d | Windows | 0.328300 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.565200 | 2026-08-27T03:05:41Z |
| us-east-1 | us-east-1f | Windows | 0.324500 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.396200 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.376500 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.349700 | 2026-08-27T03:05:41Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.535000 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.517400 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.515200 | 2026-08-27T03:05:41Z |
| us-west-2 | us-west-2c | Windows | 0.330700 | 2026-08-27T03:05:41Z |
