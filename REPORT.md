# Spot placement score log

Generated 2026-09-17 11:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 118 | 0% | 1.7 | 3 (09-17 11:34Z) |
| ap-northeast-1 | 118 | 0% | 1.9 | 2 (09-17 11:34Z) |
| ap-northeast-2 | 118 | 0% | 3.0 | 3 (09-17 11:34Z) |
| ap-south-1 | 118 | 0% | 2.0 | 1 (09-17 11:34Z) |
| ap-southeast-2 | 118 | 0% | 1.0 | 1 (09-17 11:34Z) |
| ap-southeast-3 | 118 | 0% | 2.5 | 1 (09-17 11:34Z) |
| us-east-1 | 118 | 0% | 1.9 | 3 (09-17 11:34Z) |
| us-east-2 | 118 | 0% | 1.7 | 3 (09-17 11:34Z) |
| us-west-2 | 118 | 0% | 1.5 | 3 (09-17 11:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111133333333333333333333333333333333333333333
ap-northeast-1   222221123221123323333333333333223321132212222112
ap-northeast-2   333333233333333333333333333333333333333333333333
ap-south-1       111111211313121111333333313333333331111121122111
ap-southeast-2   111111111111111311111111111111111111111111111111
ap-southeast-3   113133113333333333333333333333313133131331333331
us-east-1        133221221131131133223311323233222222122113112123
us-east-2        333111311111131311333333333333333111111113131333
us-west-2        111111111111111111133313313333333111211121111113
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 63 | 0% | 2.2 | 3 (09-17 11:34Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 106 | 0% | 2.9 | 3 (09-16 18:09Z) |
| ap-northeast-2 apne2-az3 | 105 | 0% | 2.9 | 3 (09-17 11:34Z) |
| ap-northeast-2 apne2-az4 | 115 | 0% | 3.0 | 3 (09-17 11:34Z) |
| ap-south-1 aps1-az1 | 49 | 0% | 1.6 | 1 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 62 | 0% | 2.6 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 23 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-southeast-3 apse3-az3 | 92 | 0% | 2.9 | 3 (09-17 06:03Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 34 | 0% | 1.1 | 1 (09-17 06:03Z) |
| us-east-1 use1-az4 | 22 | 0% | 1.3 | 3 (09-17 11:34Z) |
| us-east-1 use1-az5 | 34 | 0% | 1.4 | 3 (09-17 11:34Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 38 | 0% | 1.6 | 3 (09-17 11:34Z) |
| us-east-2 use2-az2 | 52 | 0% | 1.9 | 3 (09-17 06:03Z) |
| us-east-2 use2-az3 | 61 | 0% | 2.2 | 3 (09-17 11:34Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 24 | 0% | 1.8 | 3 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 60 | 0% | 1.6 | 3 (09-17 11:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 118 | 0% | 3.0 | 3 (09-17 11:34Z) |
| ap-northeast-1 | 118 | 75% | 7.3 | 9 (09-17 11:34Z) |
| ap-northeast-2 | 118 | 100% | 9.0 | 9 (09-17 11:34Z) |
| ap-south-1 | 118 | 35% | 4.9 | 3 (09-17 11:34Z) |
| ap-southeast-2 | 118 | 8% | 2.6 | 3 (09-17 11:34Z) |
| ap-southeast-3 | 118 | 0% | 2.5 | 1 (09-17 11:34Z) |
| us-east-1 | 118 | 72% | 6.7 | 9 (09-17 11:34Z) |
| us-east-2 | 118 | 74% | 7.1 | 9 (09-17 11:34Z) |
| us-west-2 | 118 | 48% | 5.5 | 9 (09-17 11:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   339992249992349999999999999999649993399924999419
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       922999513339939999999999999999999999189999299993
ap-southeast-2   113322222311233333333333322332222222222222332223
ap-southeast-3   113133113333333333333333333333313133131331333331
us-east-1        994456993299992349999999999999994368443249395599
us-east-2        999199992333991919999999999999999999992129999999
us-west-2        951332313323423353999999999999999342543353441399
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 6 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 38 | 0% | 3.0 | 3 (09-16 01:21Z) |
| ap-northeast-1 apne1-az1 | 60 | 87% | 8.2 | 9 (09-17 11:34Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 79 | 100% | 9.0 | 9 (09-16 22:04Z) |
| ap-northeast-2 apne2-az1 | 109 | 100% | 9.0 | 9 (09-17 11:34Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 108 | 100% | 9.0 | 9 (09-17 11:34Z) |
| ap-northeast-2 apne2-az4 | 42 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-south-1 aps1-az1 | 29 | 24% | 4.4 | 9 (09-17 00:25Z) |
| ap-south-1 aps1-az2 | 32 | 0% | 3.0 | 3 (09-16 22:04Z) |
| ap-south-1 aps1-az3 | 45 | 60% | 6.6 | 9 (09-17 06:03Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 35 | 0% | 3.0 | 3 (09-17 00:25Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 45 | 100% | 9.0 | 9 (09-17 11:34Z) |
| us-east-1 use1-az4 | 47 | 96% | 8.7 | 9 (09-17 11:34Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 46 | 100% | 9.0 | 9 (09-17 06:03Z) |
| us-east-2 use2-az1 | 46 | 100% | 9.0 | 9 (09-17 06:03Z) |
| us-east-2 use2-az2 | 78 | 97% | 8.8 | 9 (09-17 11:34Z) |
| us-east-2 use2-az3 | 55 | 85% | 8.0 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 28 | 96% | 8.8 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.715000 | 2026-09-17T11:34:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-17T11:34:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.803200 | 2026-09-17T11:34:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.968800 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589600 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578900 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565700 | 2026-09-17T11:34:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742100 | 2026-09-17T11:34:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.538300 | 2026-09-17T11:34:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.321800 | 2026-09-17T11:34:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.474800 | 2026-09-17T11:34:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.318400 | 2026-09-17T11:34:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686000 | 2026-09-17T11:34:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.500100 | 2026-09-17T11:34:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.901100 | 2026-09-17T11:34:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.524400 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.862600 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1a | Windows | 0.343700 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.660800 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1b | Windows | 0.327100 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.552400 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1c | Windows | 0.302700 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.544000 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1d | Windows | 0.312000 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.548200 | 2026-09-17T11:34:12Z |
| us-east-1 | us-east-1f | Windows | 0.320200 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525000 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2a | Windows | 0.639900 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.519600 | 2026-09-17T11:34:12Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.567400 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2a | Windows | 0.342400 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.533200 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2b | Windows | 0.338400 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.536100 | 2026-09-17T11:34:12Z |
| us-west-2 | us-west-2c | Windows | 0.338600 | 2026-09-17T11:34:12Z |
