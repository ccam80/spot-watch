# Spot placement score log

Generated 2026-09-01 23:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 27 | 0% | 1.0 | 1 (09-01 23:15Z) |
| ap-northeast-1 | 27 | 0% | 1.7 | 1 (09-01 23:15Z) |
| ap-northeast-2 | 27 | 0% | 2.9 | 1 (09-01 23:15Z) |
| ap-south-1 | 27 | 0% | 2.3 | 1 (09-01 23:15Z) |
| ap-southeast-2 | 27 | 0% | 1.0 | 1 (09-01 23:15Z) |
| ap-southeast-3 | 27 | 0% | 2.4 | 3 (09-01 23:15Z) |
| us-east-1 | 27 | 0% | 1.6 | 1 (09-01 23:15Z) |
| us-east-2 | 27 | 0% | 1.3 | 1 (09-01 23:15Z) |
| us-west-2 | 27 | 0% | 1.6 | 1 (09-01 23:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                             111111111111111111111111111
ap-northeast-1                        111311333313313111131111111
ap-northeast-2                        333333333333333333333333331
ap-south-1                            333131333333313333111311131
ap-southeast-2                        111111111111111111111111111
ap-southeast-3                        333333332323211132112333333
us-east-1                             323332111131111113121111111
us-east-2                             111113113111133111111111111
us-west-2                             221222113111113133311111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 3 | · | 1 | · | 1 | · | · | 2 | 1 | · | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 1 | · | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 3 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | · | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 2 | · | 1 | · | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 1 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 1 | · | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | · | · | 3 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | · | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 13 | 0% | 1.0 | 1 (09-01 23:15Z) |
| ap-east-1 ape1-az2 | 3 | 0% | 1.0 | 1 (08-31 20:47Z) |
| ap-northeast-1 apne1-az1 | 4 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-northeast-1 apne1-az4 | 18 | 0% | 2.0 | 1 (09-01 23:15Z) |
| ap-northeast-2 apne2-az1 | 24 | 0% | 2.9 | 3 (09-01 20:58Z) |
| ap-northeast-2 apne2-az3 | 24 | 0% | 2.8 | 3 (09-01 20:58Z) |
| ap-northeast-2 apne2-az4 | 27 | 0% | 2.9 | 1 (09-01 23:15Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 2.0 | 1 (09-01 23:15Z) |
| ap-south-1 aps1-az3 | 19 | 0% | 2.8 | 3 (09-01 20:58Z) |
| ap-southeast-2 apse2-az1 | 5 | 0% | 1.0 | 1 (09-01 06:12Z) |
| ap-southeast-2 apse2-az2 | 2 | 0% | 1.0 | 1 (08-31 20:47Z) |
| ap-southeast-3 apse3-az1 | 10 | 0% | 1.0 | 1 (09-01 23:15Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 2.8 | 3 (09-01 23:15Z) |
| us-east-1 use1-az1 | 5 | 0% | 1.0 | 1 (09-01 06:12Z) |
| us-east-1 use1-az2 | 15 | 0% | 1.1 | 1 (09-01 23:15Z) |
| us-east-1 use1-az4 | 6 | 0% | 1.7 | 1 (09-01 06:12Z) |
| us-east-1 use1-az5 | 7 | 0% | 1.6 | 1 (09-01 12:31Z) |
| us-east-1 use1-az6 | 13 | 0% | 1.3 | 1 (09-01 23:15Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 9 | 0% | 1.2 | 1 (09-01 23:15Z) |
| us-east-2 use2-az3 | 6 | 0% | 2.2 | 1 (09-01 12:31Z) |
| us-west-2 usw2-az1 | 8 | 0% | 1.8 | 1 (09-01 23:15Z) |
| us-west-2 usw2-az2 | 5 | 0% | 1.4 | 1 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 12 | 0% | 1.7 | 1 (09-01 17:18Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 27 | 0% | 3.0 | 3 (09-01 23:15Z) |
| ap-northeast-1 | 27 | 85% | 7.8 | 9 (09-01 23:15Z) |
| ap-northeast-2 | 27 | 100% | 9.0 | 9 (09-01 23:15Z) |
| ap-south-1 | 27 | 0% | 2.7 | 3 (09-01 23:15Z) |
| ap-southeast-2 | 27 | 37% | 4.1 | 1 (09-01 23:15Z) |
| ap-southeast-3 | 27 | 0% | 2.4 | 3 (09-01 23:15Z) |
| us-east-1 | 27 | 74% | 6.4 | 1 (09-01 23:15Z) |
| us-east-2 | 27 | 63% | 6.2 | 9 (09-01 23:15Z) |
| us-west-2 | 27 | 41% | 5.2 | 4 (09-01 23:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                             333333333333333333333333333
ap-northeast-1                        991999999999999999199119999
ap-northeast-2                        999999999999999999999999999
ap-south-1                            333133333333333333133311333
ap-southeast-2                        111111979999999931111112311
ap-southeast-3                        333333332323211132112333333
us-east-1                             766787589999999999941191121
us-east-2                             929919299999199221911199999
us-west-2                             442439219222299999991299244
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | · | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 9 | · | 1 | · | 9 | · | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | · | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 7 | · | 1 | · | 9 | · | · | 5 | 2 | · | 5 | 1 | 9 | 3 | 9 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 2 | 2 | · | 3 | 3 | · | 2 | · | 1 | · | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 1 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 5 | 9 | · | 6 | 8 | · | 9 | · | 9 | · | · | 8 | 1 | · | 8 | 4 | 9 | 1 | 9 | 9 | 2 | 8 | 7 | 4 |
| us-east-2 | 1 | 1 | · | 9 | 9 | · | 9 | · | 9 | · | · | 9 | 9 | · | 9 | 1 | 9 | 9 | 2 | 9 | 5 | 6 | 4 | 5 |
| us-west-2 | 6 | 2 | · | 2 | 1 | · | 9 | · | 9 | · | · | 9 | 9 | · | 6 | 9 | 2 | 2 | 9 | 2 | 2 | 6 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 14 | 0% | 3.0 | 3 (09-01 23:15Z) |
| ap-east-1 ape1-az2 | 9 | 0% | 3.0 | 3 (09-01 12:31Z) |
| ap-east-1 ape1-az3 | 9 | 0% | 3.0 | 3 (09-01 20:58Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 10 | 0% | 3.0 | 3 (09-01 23:15Z) |
| ap-northeast-1 apne1-az4 | 21 | 100% | 9.0 | 9 (09-01 23:15Z) |
| ap-northeast-2 apne2-az1 | 26 | 100% | 9.0 | 9 (09-01 23:15Z) |
| ap-northeast-2 apne2-az3 | 26 | 100% | 9.0 | 9 (09-01 23:15Z) |
| ap-northeast-2 apne2-az4 | 12 | 0% | 3.0 | 3 (09-01 23:15Z) |
| ap-south-1 aps1-az1 | 4 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-south-1 aps1-az2 | 13 | 0% | 3.0 | 3 (09-01 23:15Z) |
| ap-south-1 aps1-az3 | 6 | 0% | 3.0 | 3 (09-01 00:34Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 10 | 0% | 3.0 | 3 (09-01 23:15Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 9 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az4 | 8 | 100% | 9.0 | 9 (08-31 00:28Z) |
| us-east-1 use1-az5 | 10 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-east-1 use1-az6 | 11 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-east-2 use2-az1 | 8 | 100% | 8.9 | 9 (09-01 12:31Z) |
| us-east-2 use2-az2 | 15 | 87% | 8.0 | 6 (09-01 23:15Z) |
| us-east-2 use2-az3 | 10 | 80% | 7.4 | 3 (09-01 23:15Z) |
| us-west-2 usw2-az1 | 9 | 89% | 8.3 | 9 (09-01 12:31Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 10 | 100% | 9.0 | 9 (09-01 12:31Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.769300 | 2026-09-01T23:15:26Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-09-01T23:15:26Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.843400 | 2026-09-01T23:15:26Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.377300 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.363800 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.313900 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.290600 | 2026-09-01T23:15:26Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-09-01T23:15:26Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.534700 | 2026-09-01T23:15:26Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-01T23:15:26Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.473500 | 2026-09-01T23:15:26Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-09-01T23:15:26Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.748000 | 2026-09-01T23:15:26Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.473400 | 2026-09-01T23:15:26Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.892900 | 2026-09-01T23:15:26Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.379600 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.942700 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1a | Windows | 0.343000 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.710500 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1b | Windows | 0.325900 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.603500 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1c | Windows | 0.322900 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.498200 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1d | Windows | 0.324200 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.528300 | 2026-09-01T23:15:26Z |
| us-east-1 | us-east-1f | Windows | 0.321700 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.375700 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.363900 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.356100 | 2026-09-01T23:15:26Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.569200 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.530300 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.531900 | 2026-09-01T23:15:26Z |
| us-west-2 | us-west-2c | Windows | 0.332300 | 2026-09-01T23:15:26Z |
