# Spot placement score log

Generated 2026-09-17 23:31 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 121 | 0% | 1.7 | 3 (09-17 23:31Z) |
| ap-northeast-1 | 121 | 0% | 1.9 | 2 (09-17 23:31Z) |
| ap-northeast-2 | 121 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-south-1 | 121 | 0% | 2.0 | 3 (09-17 23:31Z) |
| ap-southeast-2 | 121 | 0% | 1.0 | 1 (09-17 23:31Z) |
| ap-southeast-3 | 121 | 0% | 2.5 | 3 (09-17 23:31Z) |
| us-east-1 | 121 | 0% | 2.0 | 3 (09-17 23:31Z) |
| us-east-2 | 121 | 0% | 1.7 | 3 (09-17 23:31Z) |
| us-west-2 | 121 | 0% | 1.5 | 2 (09-17 23:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111133333333333333333333333333333333333333333333
ap-northeast-1   221123221123323333333333333223321132212222112222
ap-northeast-2   333233333333333333333333333333333333333333333333
ap-south-1       111211313121111333333313333333331111121122111333
ap-southeast-2   111111111111311111111111111111111111111111111111
ap-southeast-3   133113333333333333333333333313133131331333331313
us-east-1        221221131131133223311323233222222122113112123223
us-east-2        111311111131311333333333333333111111113131333333
us-west-2        111111111111111133313313333333111211121111113122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 66 | 0% | 2.2 | 3 (09-17 23:31Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 109 | 0% | 2.9 | 3 (09-17 23:31Z) |
| ap-northeast-2 apne2-az3 | 107 | 0% | 2.9 | 3 (09-17 20:14Z) |
| ap-northeast-2 apne2-az4 | 118 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-south-1 aps1-az1 | 51 | 0% | 1.7 | 3 (09-17 23:31Z) |
| ap-south-1 aps1-az3 | 65 | 0% | 2.6 | 3 (09-17 23:31Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 24 | 0% | 1.0 | 1 (09-17 16:52Z) |
| ap-southeast-3 apse3-az3 | 94 | 0% | 2.9 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 35 | 0% | 1.1 | 1 (09-17 16:52Z) |
| us-east-1 use1-az4 | 24 | 0% | 1.3 | 3 (09-17 23:31Z) |
| us-east-1 use1-az5 | 35 | 0% | 1.4 | 3 (09-17 23:31Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 39 | 0% | 1.6 | 1 (09-17 20:14Z) |
| us-east-2 use2-az2 | 55 | 0% | 1.9 | 3 (09-17 23:31Z) |
| us-east-2 use2-az3 | 64 | 0% | 2.3 | 3 (09-17 23:31Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 24 | 0% | 1.8 | 3 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 60 | 0% | 1.6 | 3 (09-17 11:34Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 121 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-northeast-1 | 121 | 76% | 7.4 | 9 (09-17 23:31Z) |
| ap-northeast-2 | 121 | 100% | 9.0 | 9 (09-17 23:31Z) |
| ap-south-1 | 121 | 36% | 5.0 | 9 (09-17 23:31Z) |
| ap-southeast-2 | 121 | 8% | 2.6 | 2 (09-17 23:31Z) |
| ap-southeast-3 | 121 | 0% | 2.5 | 3 (09-17 23:31Z) |
| us-east-1 | 121 | 73% | 6.7 | 9 (09-17 23:31Z) |
| us-east-2 | 121 | 74% | 7.2 | 9 (09-17 23:31Z) |
| us-west-2 | 121 | 48% | 5.5 | 5 (09-17 23:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   992249992349999999999999999649993399924999419999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999513339939999999999999999999999189999299993999
ap-southeast-2   322222311233333333333322332222222222222332223322
ap-southeast-3   133113333333333333333333333313133131331333331313
us-east-1        456993299992349999999999999994368443249395599569
us-east-2        199992333991919999999999999999999992129999999999
us-west-2        332313323423353999999999999999342543353441399445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 4 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 4 | 8 | 7 | 7 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 40 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-northeast-1 apne1-az1 | 62 | 87% | 8.2 | 9 (09-17 20:14Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 81 | 100% | 9.0 | 9 (09-17 20:14Z) |
| ap-northeast-2 apne2-az1 | 112 | 100% | 9.0 | 9 (09-17 23:31Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 111 | 100% | 9.0 | 9 (09-17 23:31Z) |
| ap-northeast-2 apne2-az4 | 43 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 aps1-az1 | 32 | 31% | 4.9 | 9 (09-17 23:31Z) |
| ap-south-1 aps1-az2 | 33 | 0% | 3.0 | 3 (09-17 20:14Z) |
| ap-south-1 aps1-az3 | 48 | 62% | 6.8 | 9 (09-17 23:31Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 36 | 0% | 3.0 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 45 | 100% | 9.0 | 9 (09-17 11:34Z) |
| us-east-1 use1-az4 | 48 | 96% | 8.7 | 9 (09-17 23:31Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 46 | 100% | 9.0 | 9 (09-17 06:03Z) |
| us-east-2 use2-az1 | 48 | 100% | 9.0 | 9 (09-17 23:31Z) |
| us-east-2 use2-az2 | 81 | 98% | 8.8 | 9 (09-17 23:31Z) |
| us-east-2 use2-az3 | 58 | 86% | 8.1 | 9 (09-17 23:31Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 28 | 96% | 8.8 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712600 | 2026-09-17T23:31:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-17T23:31:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.809700 | 2026-09-17T23:31:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.992700 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589500 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578700 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565100 | 2026-09-17T23:31:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742300 | 2026-09-17T23:31:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.523900 | 2026-09-17T23:31:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.320300 | 2026-09-17T23:31:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.468900 | 2026-09-17T23:31:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.318400 | 2026-09-17T23:31:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686500 | 2026-09-17T23:31:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507100 | 2026-09-17T23:31:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.882800 | 2026-09-17T23:31:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530200 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.855600 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1a | Windows | 0.344300 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.657500 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1b | Windows | 0.325600 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.538600 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1c | Windows | 0.300600 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.539200 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1d | Windows | 0.310200 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.548100 | 2026-09-17T23:31:05Z |
| us-east-1 | us-east-1f | Windows | 0.319800 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529200 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2a | Windows | 0.639400 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529900 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.522400 | 2026-09-17T23:31:05Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.564300 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2a | Windows | 0.341500 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.530500 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2b | Windows | 0.338300 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.533600 | 2026-09-17T23:31:05Z |
| us-west-2 | us-west-2c | Windows | 0.338800 | 2026-09-17T23:31:05Z |
