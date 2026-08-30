# Spot placement score log

Generated 2026-08-30 14:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 15 | 0% | 1.0 | 1 (08-30 14:23Z) |
| ap-northeast-1 | 15 | 0% | 2.1 | 3 (08-30 14:23Z) |
| ap-northeast-2 | 15 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-south-1 | 15 | 0% | 2.6 | 3 (08-30 14:23Z) |
| ap-southeast-2 | 15 | 0% | 1.0 | 1 (08-30 14:23Z) |
| ap-southeast-3 | 15 | 0% | 2.5 | 1 (08-30 14:23Z) |
| us-east-1 | 15 | 0% | 1.8 | 1 (08-30 14:23Z) |
| us-east-2 | 15 | 0% | 1.5 | 3 (08-30 14:23Z) |
| us-west-2 | 15 | 0% | 1.6 | 3 (08-30 14:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                         111111111111111
ap-northeast-1                                    111311333313313
ap-northeast-2                                    333333333333333
ap-south-1                                        333131333333313
ap-southeast-2                                    111111111111111
ap-southeast-3                                    333333332323211
us-east-1                                         323332111131111
us-east-2                                         111113113111133
us-west-2                                         221222113111113
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-northeast-1 | · | 3 | · | 1 | 3 | · | · | · | 1 | · | · | 2 | · | · | 3 | · | 3 | · | · | 1 | · | 1 | 2 | 1 |
| ap-northeast-2 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 1 | · | · | 1 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 1 | · | 3 | 1 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | · | 3 | · | 3 | 1 | 3 |
| us-east-2 | · | 1 | · | 1 | 1 | · | · | · | 3 | · | · | 3 | · | · | 2 | · | 1 | · | · | 1 | · | 1 | 1 | 1 |
| us-west-2 | · | 1 | · | 1 | 1 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 1 | · | · | 1 | · | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 7 | 0% | 1.0 | 1 (08-30 08:15Z) |
| ap-northeast-1 apne1-az1 | 1 | 0% | 1.0 | 1 (08-26 22:23Z) |
| ap-northeast-1 apne1-az4 | 10 | 0% | 2.6 | 3 (08-30 14:23Z) |
| ap-northeast-2 apne2-az1 | 15 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-northeast-2 apne2-az3 | 15 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-northeast-2 apne2-az4 | 15 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-south-1 aps1-az1 | 9 | 0% | 2.2 | 1 (08-30 14:23Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-southeast-3 apse3-az1 | 5 | 0% | 1.0 | 1 (08-29 04:07Z) |
| ap-southeast-3 apse3-az3 | 12 | 0% | 2.8 | 2 (08-30 01:12Z) |
| us-east-1 use1-az1 | 2 | 0% | 1.0 | 1 (08-29 22:37Z) |
| us-east-1 use1-az2 | 9 | 0% | 1.2 | 1 (08-30 08:15Z) |
| us-east-1 use1-az4 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-east-1 use1-az5 | 1 | 0% | 3.0 | 3 (08-29 19:41Z) |
| us-east-1 use1-az6 | 9 | 0% | 1.2 | 1 (08-30 14:23Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 6 | 0% | 1.3 | 1 (08-30 08:15Z) |
| us-east-2 use2-az3 | 4 | 0% | 2.8 | 3 (08-30 14:23Z) |
| us-west-2 usw2-az1 | 2 | 0% | 2.0 | 3 (08-30 14:23Z) |
| us-west-2 usw2-az2 | 3 | 0% | 1.7 | 1 (08-29 22:37Z) |
| us-west-2 usw2-az3 | 7 | 0% | 1.6 | 3 (08-30 14:23Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 15 | 0% | 3.0 | 3 (08-30 14:23Z) |
| ap-northeast-1 | 15 | 93% | 8.5 | 9 (08-30 14:23Z) |
| ap-northeast-2 | 15 | 100% | 9.0 | 9 (08-30 14:23Z) |
| ap-south-1 | 15 | 0% | 2.9 | 3 (08-30 14:23Z) |
| ap-southeast-2 | 15 | 60% | 5.7 | 9 (08-30 14:23Z) |
| ap-southeast-3 | 15 | 0% | 2.5 | 1 (08-30 14:23Z) |
| us-east-1 | 15 | 100% | 7.8 | 9 (08-30 14:23Z) |
| us-east-2 | 15 | 73% | 7.0 | 9 (08-30 14:23Z) |
| us-west-2 | 15 | 27% | 4.3 | 9 (08-30 14:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                         333333333333333
ap-northeast-1                                    991999999999999
ap-northeast-2                                    999999999999999
ap-south-1                                        333133333333333
ap-southeast-2                                    111111979999999
ap-southeast-3                                    333333332323211
us-east-1                                         766787589999999
us-east-2                                         929919299999199
us-west-2                                         442439219222299
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 3 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-northeast-1 | · | 9 | · | 1 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-northeast-2 | · | 9 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 9 | 9 |
| ap-south-1 | · | 3 | · | 3 | 3 | · | · | · | 3 | · | · | 3 | · | · | 2 | · | 3 | · | · | 3 | · | 3 | 3 | 3 |
| ap-southeast-2 | · | 9 | · | 1 | 7 | · | · | · | 9 | · | · | 5 | · | · | 5 | · | 9 | · | · | 9 | · | 1 | 6 | 1 |
| ap-southeast-3 | · | 2 | · | 3 | 3 | · | · | · | 1 | · | · | 2 | · | · | 2 | · | 3 | · | · | 2 | · | 3 | 3 | 3 |
| us-east-1 | · | 9 | · | 6 | 8 | · | · | · | 9 | · | · | 8 | · | · | 8 | · | 9 | · | · | 9 | · | 7 | 7 | 8 |
| us-east-2 | · | 1 | · | 9 | 9 | · | · | · | 9 | · | · | 9 | · | · | 9 | · | 9 | · | · | 9 | · | 9 | 4 | 1 |
| us-west-2 | · | 2 | · | 2 | 1 | · | · | · | 9 | · | · | 9 | · | · | 6 | · | 2 | · | · | 2 | · | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 6 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-east-1 ape1-az2 | 5 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-east-1 ape1-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 5 | 80% | 7.8 | 3 (08-28 22:13Z) |
| ap-northeast-1 apne1-az2 | 6 | 0% | 3.0 | 3 (08-29 04:07Z) |
| ap-northeast-1 apne1-az4 | 12 | 100% | 9.0 | 9 (08-30 14:23Z) |
| ap-northeast-2 apne2-az1 | 14 | 100% | 9.0 | 9 (08-30 14:23Z) |
| ap-northeast-2 apne2-az3 | 14 | 100% | 9.0 | 9 (08-30 14:23Z) |
| ap-northeast-2 apne2-az4 | 5 | 0% | 3.0 | 3 (08-29 16:40Z) |
| ap-south-1 aps1-az1 | 2 | 0% | 3.0 | 3 (08-28 22:13Z) |
| ap-south-1 aps1-az2 | 7 | 0% | 3.0 | 3 (08-29 19:41Z) |
| ap-south-1 aps1-az3 | 4 | 0% | 3.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-3 apse3-az3 | 6 | 0% | 3.0 | 3 (08-28 11:16Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 6 | 100% | 9.0 | 9 (08-30 08:15Z) |
| us-east-1 use1-az4 | 5 | 100% | 9.0 | 9 (08-30 01:12Z) |
| us-east-1 use1-az5 | 5 | 100% | 9.0 | 9 (08-30 14:23Z) |
| us-east-1 use1-az6 | 7 | 100% | 9.0 | 9 (08-30 14:23Z) |
| us-east-2 use2-az1 | 5 | 100% | 8.8 | 9 (08-30 14:23Z) |
| us-east-2 use2-az2 | 9 | 78% | 7.7 | 9 (08-30 14:23Z) |
| us-east-2 use2-az3 | 7 | 100% | 8.4 | 9 (08-30 08:15Z) |
| us-west-2 usw2-az1 | 2 | 50% | 6.0 | 9 (08-30 14:23Z) |
| us-west-2 usw2-az2 | 3 | 100% | 9.0 | 9 (08-30 14:23Z) |
| us-west-2 usw2-az3 | 3 | 100% | 9.0 | 9 (08-30 14:23Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.779000 | 2026-08-30T14:23:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-08-30T14:23:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.835000 | 2026-08-30T14:23:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.345000 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.394300 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.356800 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.324500 | 2026-08-30T14:23:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-08-30T14:23:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.515800 | 2026-08-30T14:23:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-08-30T14:23:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.470900 | 2026-08-30T14:23:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-08-30T14:23:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.737700 | 2026-08-30T14:23:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.447700 | 2026-08-30T14:23:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.836700 | 2026-08-30T14:23:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.376000 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.951800 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1a | Windows | 0.345600 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.729000 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1b | Windows | 0.327800 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.623100 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1c | Windows | 0.325200 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.525100 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1d | Windows | 0.327800 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.533000 | 2026-08-30T14:23:46Z |
| us-east-1 | us-east-1f | Windows | 0.324000 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.370400 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.354500 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.346800 | 2026-08-30T14:23:46Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.536500 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.502000 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.501900 | 2026-08-30T14:23:46Z |
| us-west-2 | us-west-2c | Windows | 0.331300 | 2026-08-30T14:23:46Z |
