# Spot placement score log

Generated 2026-09-19 22:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 133 | 0% | 1.8 | 3 (09-19 22:55Z) |
| ap-northeast-1 | 133 | 0% | 1.9 | 2 (09-19 22:55Z) |
| ap-northeast-2 | 133 | 0% | 3.0 | 3 (09-19 22:55Z) |
| ap-south-1 | 133 | 0% | 2.0 | 3 (09-19 22:55Z) |
| ap-southeast-2 | 133 | 0% | 1.0 | 1 (09-19 22:55Z) |
| ap-southeast-3 | 133 | 0% | 2.5 | 3 (09-19 22:55Z) |
| us-east-1 | 133 | 0% | 1.9 | 2 (09-19 22:55Z) |
| us-east-2 | 133 | 0% | 1.8 | 2 (09-19 22:55Z) |
| us-west-2 | 133 | 0% | 1.6 | 3 (09-19 22:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   323333333333333223321132212222112222111221223322
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       111333333313333333331111121122111333311312113333
ap-southeast-2   311111111111111111111111111111111111111111111111
ap-southeast-3   333333333333333313133131331333331313112333333333
us-east-1        133223311323233222222122113112123223123111213112
us-east-2        311333333333333333111111113131333333313311333312
us-west-2        111133313313333333111211121111113122131112333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 38 | 0% | 1.3 | 3 (09-19 22:55Z) |
| ap-east-1 ape1-az2 | 77 | 0% | 2.3 | 3 (09-19 22:55Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 65 | 0% | 2.2 | 3 (09-19 17:57Z) |
| ap-northeast-2 apne2-az1 | 121 | 0% | 2.9 | 3 (09-19 22:55Z) |
| ap-northeast-2 apne2-az3 | 118 | 0% | 2.9 | 3 (09-19 22:55Z) |
| ap-northeast-2 apne2-az4 | 130 | 0% | 3.0 | 3 (09-19 22:55Z) |
| ap-south-1 aps1-az1 | 54 | 0% | 1.7 | 3 (09-19 22:55Z) |
| ap-south-1 aps1-az3 | 72 | 0% | 2.6 | 3 (09-19 22:55Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 103 | 0% | 2.9 | 3 (09-19 22:55Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 39 | 0% | 1.1 | 1 (09-18 21:36Z) |
| us-east-1 use1-az4 | 26 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az5 | 37 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 43 | 0% | 1.7 | 3 (09-19 10:50Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 72 | 0% | 2.3 | 3 (09-19 17:57Z) |
| us-west-2 usw2-az1 | 38 | 0% | 2.0 | 3 (09-19 22:55Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 68 | 0% | 1.7 | 3 (09-19 22:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 133 | 0% | 3.0 | 3 (09-19 22:55Z) |
| ap-northeast-1 | 133 | 77% | 7.4 | 9 (09-19 22:55Z) |
| ap-northeast-2 | 133 | 100% | 9.0 | 9 (09-19 22:55Z) |
| ap-south-1 | 133 | 41% | 5.3 | 9 (09-19 22:55Z) |
| ap-southeast-2 | 133 | 8% | 2.6 | 3 (09-19 22:55Z) |
| ap-southeast-3 | 133 | 0% | 2.5 | 3 (09-19 22:55Z) |
| us-east-1 | 133 | 74% | 6.8 | 9 (09-19 22:55Z) |
| us-east-2 | 133 | 74% | 7.2 | 9 (09-19 22:55Z) |
| us-west-2 | 133 | 50% | 5.6 | 9 (09-19 22:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999649993399924999419999339999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999999189999299993999923999999999
ap-southeast-2   333333333322332222222222222332223322223323333333
ap-southeast-3   333333333333333313133131331333331313112333333333
us-east-1        349999999999999994368443249395599569999454999999
us-east-2        919999999999999999999992129999999999999911999919
us-west-2        353999999999999999342543353441399445953345999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 3 | 4 | 9 | 3 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 3 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 7 | 4 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 68 | 88% | 8.3 | 9 (09-19 20:33Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 89 | 100% | 9.0 | 9 (09-19 22:55Z) |
| ap-northeast-2 apne2-az1 | 122 | 100% | 9.0 | 9 (09-19 22:55Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 121 | 100% | 9.0 | 9 (09-19 22:55Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 40 | 45% | 5.7 | 9 (09-19 20:33Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 54 | 67% | 7.0 | 9 (09-19 22:55Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 53 | 100% | 9.0 | 9 (09-19 22:55Z) |
| us-east-1 use1-az4 | 56 | 96% | 8.8 | 9 (09-19 22:55Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 52 | 100% | 9.0 | 9 (09-19 22:55Z) |
| us-east-2 use2-az1 | 52 | 100% | 9.0 | 9 (09-19 10:50Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 66 | 88% | 8.2 | 9 (09-19 17:57Z) |
| us-west-2 usw2-az1 | 46 | 98% | 8.9 | 9 (09-19 22:55Z) |
| us-west-2 usw2-az2 | 35 | 97% | 8.7 | 9 (09-19 22:55Z) |
| us-west-2 usw2-az3 | 47 | 98% | 8.9 | 9 (09-19 22:55Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.714200 | 2026-09-19T22:55:36Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-19T22:55:36Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.844700 | 2026-09-19T22:55:36Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.025700 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588800 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579500 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565900 | 2026-09-19T22:55:36Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-09-19T22:55:36Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.497500 | 2026-09-19T22:55:36Z |
| ap-south-1 | ap-south-1a | Windows | 0.308300 | 2026-09-19T22:55:36Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.452900 | 2026-09-19T22:55:36Z |
| ap-south-1 | ap-south-1b | Windows | 0.316600 | 2026-09-19T22:55:36Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.687800 | 2026-09-19T22:55:36Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513100 | 2026-09-19T22:55:36Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.847200 | 2026-09-19T22:55:36Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.841000 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1a | Windows | 0.348300 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.624300 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1b | Windows | 0.314100 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.507200 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1c | Windows | 0.293900 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.518800 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1d | Windows | 0.308000 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.511400 | 2026-09-19T22:55:36Z |
| us-east-1 | us-east-1f | Windows | 0.316900 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521600 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2a | Windows | 0.641300 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.521800 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2b | Windows | 0.641700 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514400 | 2026-09-19T22:55:36Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.570800 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2a | Windows | 0.339700 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526000 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2b | Windows | 0.336400 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528100 | 2026-09-19T22:55:36Z |
| us-west-2 | us-west-2c | Windows | 0.336800 | 2026-09-19T22:55:36Z |
