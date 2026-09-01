# Spot placement score log

Generated 2026-09-01 06:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 23 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-northeast-1 | 23 | 0% | 1.8 | 1 (09-01 06:12Z) |
| ap-northeast-2 | 23 | 0% | 3.0 | 3 (09-01 06:12Z) |
| ap-south-1 | 23 | 0% | 2.4 | 1 (09-01 06:12Z) |
| ap-southeast-2 | 23 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-southeast-3 | 23 | 0% | 2.3 | 3 (09-01 06:12Z) |
| us-east-1 | 23 | 0% | 1.7 | 1 (09-01 06:12Z) |
| us-east-2 | 23 | 0% | 1.3 | 1 (09-01 06:12Z) |
| us-west-2 | 23 | 0% | 1.7 | 1 (09-01 06:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                 11111111111111111111111
ap-northeast-1                            11131133331331311113111
ap-northeast-2                            33333333333333333333333
ap-south-1                                33313133333331333311131
ap-southeast-2                            11111111111111111111111
ap-southeast-3                            33333333232321113211233
us-east-1                                 32333211113111111312111
us-east-2                                 11111311311113311111111
us-west-2                                 22122211311111313331111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 3 | 3 | 3 | · | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 3 | 3 | 1 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 2 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 1 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | 2 | 1 | · | 1 | 3 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | · | · | 2 | · | · | 2 | 1 | 1 | · | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 9 | 0% | 1.0 | 1 (08-31 15:02Z) |
| ap-east-1 ape1-az2 | 3 | 0% | 1.0 | 1 (08-31 20:47Z) |
| ap-northeast-1 apne1-az1 | 4 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-northeast-1 apne1-az4 | 15 | 0% | 2.2 | 1 (08-31 20:47Z) |
| ap-northeast-2 apne2-az1 | 21 | 0% | 2.9 | 3 (09-01 00:34Z) |
| ap-northeast-2 apne2-az3 | 21 | 0% | 2.8 | 1 (09-01 06:12Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-01 06:12Z) |
| ap-south-1 aps1-az1 | 10 | 0% | 2.1 | 1 (08-31 15:02Z) |
| ap-south-1 aps1-az3 | 18 | 0% | 2.8 | 1 (09-01 06:12Z) |
| ap-southeast-2 apse2-az1 | 5 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-southeast-2 apse2-az2 | 2 | 0% | 1.0 | 1 (08-31 20:47Z) |
| ap-southeast-3 apse3-az1 | 7 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-3 apse3-az3 | 17 | 0% | 2.8 | 3 (09-01 06:12Z) |
| us-east-1 use1-az1 | 5 | 0% | 1.0 | 1 (09-01 06:12Z) |
| us-east-1 use1-az2 | 12 | 0% | 1.2 | 1 (08-31 15:02Z) |
| us-east-1 use1-az4 | 6 | 0% | 1.7 | 1 (09-01 06:12Z) |
| us-east-1 use1-az5 | 6 | 0% | 1.7 | 1 (09-01 06:12Z) |
| us-east-1 use1-az6 | 11 | 0% | 1.4 | 1 (08-31 15:02Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 7 | 0% | 1.3 | 1 (08-31 15:02Z) |
| us-east-2 use2-az3 | 5 | 0% | 2.4 | 1 (08-31 06:58Z) |
| us-west-2 usw2-az1 | 5 | 0% | 2.2 | 3 (08-31 00:28Z) |
| us-west-2 usw2-az2 | 5 | 0% | 1.4 | 1 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 10 | 0% | 1.8 | 1 (08-31 15:02Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 23 | 0% | 3.0 | 3 (09-01 06:12Z) |
| ap-northeast-1 | 23 | 83% | 7.6 | 1 (09-01 06:12Z) |
| ap-northeast-2 | 23 | 100% | 9.0 | 9 (09-01 06:12Z) |
| ap-south-1 | 23 | 0% | 2.7 | 1 (09-01 06:12Z) |
| ap-southeast-2 | 23 | 43% | 4.5 | 1 (09-01 06:12Z) |
| ap-southeast-3 | 23 | 0% | 2.3 | 3 (09-01 06:12Z) |
| us-east-1 | 23 | 87% | 7.3 | 9 (09-01 06:12Z) |
| us-east-2 | 23 | 57% | 5.7 | 9 (09-01 06:12Z) |
| us-west-2 | 23 | 43% | 5.3 | 9 (09-01 06:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                 33333333333333333333333
ap-northeast-1                            99199999999999999919911
ap-northeast-2                            99999999999999999999999
ap-south-1                                33313333333333333313331
ap-southeast-2                            11111197999999993111111
ap-southeast-3                            33333333232321113211233
us-east-1                                 76678758999999999994119
us-east-2                                 92991929999919922191119
us-west-2                                 44243921922229999999129
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 9 | · | 1 | · | 9 | · | · | 9 | · | · | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 7 | · | 1 | · | 9 | · | · | 5 | · | · | 5 | 1 | 9 | · | 9 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 2 | · | 1 | · | · | 2 | · | · | 2 | 1 | 3 | · | 1 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 5 | 9 | · | 6 | 8 | · | 9 | · | 9 | · | · | 8 | · | · | 8 | 4 | 9 | · | 9 | 9 | 1 | 8 | 7 | 8 |
| us-east-2 | 1 | 1 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | 1 | 9 | · | 2 | 9 | 1 | 6 | 4 | 1 |
| us-west-2 | 6 | 2 | · | 2 | 1 | · | 9 | · | 9 | · | · | 9 | · | · | 6 | 9 | 2 | · | 9 | 2 | 1 | 6 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 10 | 0% | 3.0 | 3 (09-01 06:12Z) |
| ap-east-1 ape1-az2 | 8 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-east-1 ape1-az3 | 8 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 7 | 0% | 3.0 | 3 (08-31 20:47Z) |
| ap-northeast-1 apne1-az4 | 17 | 100% | 9.0 | 9 (08-31 20:47Z) |
| ap-northeast-2 apne2-az1 | 22 | 100% | 9.0 | 9 (09-01 06:12Z) |
| ap-northeast-2 apne2-az3 | 22 | 100% | 9.0 | 9 (09-01 06:12Z) |
| ap-northeast-2 apne2-az4 | 8 | 0% | 3.0 | 3 (09-01 06:12Z) |
| ap-south-1 aps1-az1 | 4 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-south-1 aps1-az2 | 10 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-south-1 aps1-az3 | 6 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 7 | 0% | 3.0 | 3 (09-01 00:34Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 9 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az4 | 8 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az5 | 10 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-east-1 use1-az6 | 11 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-east-2 use2-az1 | 7 | 100% | 8.9 | 9 (09-01 06:12Z) |
| us-east-2 use2-az2 | 11 | 82% | 7.9 | 9 (09-01 06:12Z) |
| us-east-2 use2-az3 | 8 | 100% | 8.5 | 9 (08-31 06:58Z) |
| us-west-2 usw2-az1 | 8 | 88% | 8.2 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.782200 | 2026-09-01T06:12:39Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-09-01T06:12:39Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.851300 | 2026-09-01T06:12:39Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.384000 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.370700 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.329800 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.304300 | 2026-09-01T06:12:39Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-09-01T06:12:39Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.538600 | 2026-09-01T06:12:39Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-01T06:12:39Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.469500 | 2026-09-01T06:12:39Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-09-01T06:12:39Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.753200 | 2026-09-01T06:12:39Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.473400 | 2026-09-01T06:12:39Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.884300 | 2026-09-01T06:12:39Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378700 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.942800 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1a | Windows | 0.343200 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.697900 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1b | Windows | 0.326000 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.604400 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1c | Windows | 0.323800 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.510700 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1d | Windows | 0.325900 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.525400 | 2026-09-01T06:12:39Z |
| us-east-1 | us-east-1f | Windows | 0.323400 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.376600 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.362100 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.351800 | 2026-09-01T06:12:39Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563500 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.518400 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.525100 | 2026-09-01T06:12:39Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-01T06:12:39Z |
