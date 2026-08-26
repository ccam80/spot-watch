# Spot placement score log

Generated 2026-08-26 21:31 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-northeast-1 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-northeast-2 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-south-1 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-southeast-2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-southeast-3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| us-east-1 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| us-east-2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-west-2 | 1 | 0% | 2.0 | 2 (08-26 21:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                       1
ap-northeast-1                                                  1
ap-northeast-2                                                  3
ap-south-1                                                      3
ap-southeast-2                                                  1
ap-southeast-3                                                  3
us-east-1                                                       3
us-east-2                                                       1
us-west-2                                                       2
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | · | · |
| ap-northeast-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | · | · |
| ap-northeast-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| ap-south-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| ap-southeast-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | · | · |
| ap-southeast-3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| us-east-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| us-east-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | · | · |
| us-west-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 2 | · | · |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-northeast-2 apne2-az1 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-northeast-2 apne2-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-northeast-2 apne2-az4 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-south-1 aps1-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-southeast-3 apse3-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| us-east-1 use1-az2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-east-1 use1-az6 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-east-2 use2-az2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| us-west-2 usw2-az3 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-northeast-1 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-northeast-2 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-south-1 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-southeast-2 | 1 | 0% | 1.0 | 1 (08-26 21:31Z) |
| ap-southeast-3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| us-east-1 | 1 | 100% | 7.0 | 7 (08-26 21:31Z) |
| us-east-2 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| us-west-2 | 1 | 0% | 4.0 | 4 (08-26 21:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                                                       3
ap-northeast-1                                                  9
ap-northeast-2                                                  9
ap-south-1                                                      3
ap-southeast-2                                                  1
ap-southeast-3                                                  3
us-east-1                                                       7
us-east-2                                                       9
us-west-2                                                       4
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| ap-northeast-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | · | · |
| ap-northeast-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | · | · |
| ap-south-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| ap-southeast-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | · | · |
| ap-southeast-3 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 3 | · | · |
| us-east-1 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 7 | · | · |
| us-east-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 9 | · | · |
| us-west-2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 4 | · | · |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az2 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-east-1 ape1-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-northeast-1 apne1-az1 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-northeast-1 apne1-az2 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-northeast-1 apne1-az4 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-northeast-2 apne2-az1 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-northeast-2 apne2-az3 | 1 | 100% | 9.0 | 9 (08-26 21:31Z) |
| ap-south-1 aps1-az2 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-south-1 aps1-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |
| ap-southeast-3 apse3-az3 | 1 | 0% | 3.0 | 3 (08-26 21:31Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.717100 | 2026-08-26T21:31:26Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.455600 | 2026-08-26T21:31:26Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.818000 | 2026-08-26T21:31:26Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.374600 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.399700 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.376500 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.354600 | 2026-08-26T21:31:26Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-08-26T21:31:26Z |
