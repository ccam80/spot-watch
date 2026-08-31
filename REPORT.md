# Spot placement score log

Generated 2026-08-31 06:58 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 19 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-northeast-1 | 19 | 0% | 1.8 | 1 (08-31 06:58Z) |
| ap-northeast-2 | 19 | 0% | 3.0 | 3 (08-31 06:58Z) |
| ap-south-1 | 19 | 0% | 2.6 | 1 (08-31 06:58Z) |
| ap-southeast-2 | 19 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-3 | 19 | 0% | 2.4 | 1 (08-31 06:58Z) |
| us-east-1 | 19 | 0% | 1.7 | 1 (08-31 06:58Z) |
| us-east-2 | 19 | 0% | 1.4 | 1 (08-31 06:58Z) |
| us-west-2 | 19 | 0% | 1.8 | 3 (08-31 06:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                     1111111111111111111
ap-northeast-1                                1113113333133131111
ap-northeast-2                                3333333333333333333
ap-south-1                                    3331313333333133331
ap-southeast-2                                1111111111111111111
ap-southeast-3                                3333333323232111321
us-east-1                                     3233321111311111131
us-east-2                                     1111131131111331111
us-west-2                                     2212221131111131333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | 1 | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | 3 | 1 | · | 3 | 1 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | 1 | 3 | · | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 |
| us-west-2 | 3 | 1 | · | 1 | 1 | · | 3 | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 8 | 0% | 1.0 | 1 (08-30 21:53Z) |
| ap-east-1 ape1-az2 | 2 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-northeast-1 apne1-az1 | 2 | 0% | 1.0 | 1 (08-31 00:28Z) |
| ap-northeast-1 apne1-az4 | 13 | 0% | 2.2 | 1 (08-31 06:58Z) |
| ap-northeast-2 apne2-az1 | 18 | 0% | 2.9 | 1 (08-31 06:58Z) |
| ap-northeast-2 apne2-az3 | 17 | 0% | 3.0 | 3 (08-30 21:53Z) |
| ap-northeast-2 apne2-az4 | 19 | 0% | 3.0 | 3 (08-31 06:58Z) |
| ap-south-1 aps1-az1 | 9 | 0% | 2.2 | 1 (08-30 14:23Z) |
| ap-south-1 aps1-az3 | 15 | 0% | 3.0 | 3 (08-31 00:28Z) |
| ap-southeast-2 apse2-az1 | 2 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 1.0 | 1 (08-30 18:34Z) |
| ap-southeast-3 apse3-az1 | 7 | 0% | 1.0 | 1 (08-31 06:58Z) |
| ap-southeast-3 apse3-az3 | 14 | 0% | 2.8 | 2 (08-31 00:28Z) |
| us-east-1 use1-az1 | 3 | 0% | 1.0 | 1 (08-31 00:28Z) |
| us-east-1 use1-az2 | 11 | 0% | 1.2 | 1 (08-31 06:58Z) |
| us-east-1 use1-az4 | 4 | 0% | 2.0 | 3 (08-31 00:28Z) |
| us-east-1 use1-az5 | 4 | 0% | 2.0 | 1 (08-31 06:58Z) |
| us-east-1 use1-az6 | 10 | 0% | 1.4 | 3 (08-31 00:28Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 6 | 0% | 1.3 | 1 (08-30 08:15Z) |
| us-east-2 use2-az3 | 5 | 0% | 2.4 | 1 (08-31 06:58Z) |
| us-west-2 usw2-az1 | 5 | 0% | 2.2 | 3 (08-31 00:28Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 9 | 0% | 1.9 | 3 (08-31 06:58Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 19 | 0% | 3.0 | 3 (08-31 06:58Z) |
| ap-northeast-1 | 19 | 89% | 8.2 | 1 (08-31 06:58Z) |
| ap-northeast-2 | 19 | 100% | 9.0 | 9 (08-31 06:58Z) |
| ap-south-1 | 19 | 0% | 2.8 | 1 (08-31 06:58Z) |
| ap-southeast-2 | 19 | 53% | 5.2 | 1 (08-31 06:58Z) |
| ap-southeast-3 | 19 | 0% | 2.4 | 1 (08-31 06:58Z) |
| us-east-1 | 19 | 100% | 8.1 | 9 (08-31 06:58Z) |
| us-east-2 | 19 | 63% | 6.3 | 9 (08-31 06:58Z) |
| us-west-2 | 19 | 42% | 5.3 | 9 (08-31 06:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                     3333333333333333333
ap-northeast-1                                9919999999999999991
ap-northeast-2                                9999999999999999999
ap-south-1                                    3331333333333333331
ap-southeast-2                                1111119799999999311
ap-southeast-3                                3333333323232111321
us-east-1                                     7667875899999999999
us-east-2                                     9299192999991992219
us-west-2                                     4424392192222999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | 9 | 9 | · | 1 | 9 | · | 1 | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | · | · | 3 | · | · | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 7 | · | 1 | · | 9 | · | · | 5 | · | · | 5 | · | 9 | · | 9 | 9 | · | 2 | 6 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | 1 | 2 | · | 3 | 3 | 3 |
| us-east-1 | 9 | 9 | · | 6 | 8 | · | 9 | · | 9 | · | · | 8 | · | · | 8 | · | 9 | · | 9 | 9 | · | 8 | 7 | 8 |
| us-east-2 | 1 | 1 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | 2 | 9 | · | 6 | 4 | 1 |
| us-west-2 | 9 | 2 | · | 2 | 1 | · | 9 | · | 9 | · | · | 9 | · | · | 6 | · | 2 | · | 9 | 2 | · | 6 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 5 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 15 | 100% | 9.0 | 9 (08-31 00:28Z) |
| ap-northeast-2 apne2-az1 | 18 | 100% | 9.0 | 9 (08-31 06:58Z) |
| ap-northeast-2 apne2-az3 | 18 | 100% | 9.0 | 9 (08-31 06:58Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
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
| us-west-2 usw2-az1 | 6 | 83% | 8.0 | 9 (08-31 06:58Z) |
| us-west-2 usw2-az2 | 7 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-west-2 usw2-az3 | 7 | 100% | 9.0 | 9 (08-31 06:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.776700 | 2026-08-31T06:58:18Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-31T06:58:18Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.839300 | 2026-08-31T06:58:18Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.360400 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.388700 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.346000 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.306400 | 2026-08-31T06:58:18Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-31T06:58:18Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.522300 | 2026-08-31T06:58:18Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-31T06:58:18Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.467200 | 2026-08-31T06:58:18Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-31T06:58:18Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747800 | 2026-08-31T06:58:18Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.457000 | 2026-08-31T06:58:18Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.855700 | 2026-08-31T06:58:18Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377300 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.947200 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1a | Windows | 0.345100 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.715800 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1b | Windows | 0.327800 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.614600 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1c | Windows | 0.325300 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.515700 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1d | Windows | 0.327500 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.529200 | 2026-08-31T06:58:18Z |
| us-east-1 | us-east-1f | Windows | 0.324100 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.372700 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.354800 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.348700 | 2026-08-31T06:58:18Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.545400 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.506600 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.506400 | 2026-08-31T06:58:18Z |
| us-west-2 | us-west-2c | Windows | 0.331900 | 2026-08-31T06:58:18Z |
