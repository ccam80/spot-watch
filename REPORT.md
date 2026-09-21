# Spot placement score log

Generated 2026-09-21 13:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 142 | 0% | 1.9 | 3 (09-21 13:58Z) |
| ap-northeast-1 | 142 | 0% | 1.9 | 2 (09-21 13:58Z) |
| ap-northeast-2 | 142 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-south-1 | 142 | 0% | 2.1 | 1 (09-21 13:58Z) |
| ap-southeast-2 | 142 | 0% | 1.0 | 1 (09-21 13:58Z) |
| ap-southeast-3 | 142 | 0% | 2.5 | 3 (09-21 13:58Z) |
| us-east-1 | 142 | 0% | 2.0 | 3 (09-21 13:58Z) |
| us-east-2 | 142 | 0% | 1.8 | 3 (09-21 13:58Z) |
| us-west-2 | 142 | 0% | 1.7 | 3 (09-21 13:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333333223321132212222112222111221223322312322112
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       313333333331111121122111333311312113333333333211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333313133131331333331313112333333333331333313
us-east-1        323233222222122113112123223123111213112233333333
us-east-2        333333333111111113131333333313311333312333333133
us-west-2        313333333111211121111113122131112333333333333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 84 | 0% | 2.4 | 3 (09-21 13:58Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 125 | 0% | 2.9 | 3 (09-21 13:58Z) |
| ap-northeast-2 apne2-az3 | 124 | 0% | 2.9 | 3 (09-21 13:58Z) |
| ap-northeast-2 apne2-az4 | 139 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-south-1 aps1-az1 | 55 | 0% | 1.7 | 3 (09-20 18:43Z) |
| ap-south-1 aps1-az3 | 78 | 0% | 2.6 | 3 (09-20 21:28Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 27 | 0% | 1.0 | 1 (09-21 13:58Z) |
| ap-southeast-3 apse3-az3 | 107 | 0% | 2.9 | 3 (09-21 13:58Z) |
| us-east-1 use1-az1 | 17 | 0% | 1.4 | 3 (09-20 21:28Z) |
| us-east-1 use1-az2 | 47 | 0% | 1.4 | 1 (09-21 13:58Z) |
| us-east-1 use1-az4 | 32 | 0% | 1.7 | 3 (09-21 06:13Z) |
| us-east-1 use1-az5 | 41 | 0% | 1.6 | 3 (09-21 06:13Z) |
| us-east-1 use1-az6 | 47 | 0% | 1.3 | 3 (09-21 06:13Z) |
| us-east-2 use2-az1 | 47 | 0% | 1.8 | 3 (09-21 06:13Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 76 | 0% | 2.3 | 3 (09-21 13:58Z) |
| us-west-2 usw2-az1 | 44 | 0% | 2.1 | 3 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 75 | 0% | 1.8 | 3 (09-21 06:13Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 142 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-northeast-1 | 142 | 78% | 7.5 | 9 (09-21 13:58Z) |
| ap-northeast-2 | 142 | 100% | 9.0 | 9 (09-21 13:58Z) |
| ap-south-1 | 142 | 44% | 5.4 | 1 (09-21 13:58Z) |
| ap-southeast-2 | 142 | 7% | 2.6 | 3 (09-21 13:58Z) |
| ap-southeast-3 | 142 | 0% | 2.5 | 3 (09-21 13:58Z) |
| us-east-1 | 142 | 75% | 6.9 | 9 (09-21 13:58Z) |
| us-east-2 | 142 | 76% | 7.3 | 9 (09-21 13:58Z) |
| us-west-2 | 142 | 54% | 5.8 | 9 (09-21 13:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999649993399924999419999339999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999189999299993999923999999999999999991
ap-southeast-2   322332222222222222332223322223323333333333333223
ap-southeast-3   333333313133131331333331313112333333333331333313
us-east-1        999999994368443249395599569999454999999999999999
us-east-2        999999999999992129999999999999911999919999999999
us-west-2        999999999342543353441399445953345999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 7 | 5 | 3 | 3 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 51 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 73 | 89% | 8.3 | 9 (09-21 13:58Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 96 | 100% | 9.0 | 9 (09-21 13:58Z) |
| ap-northeast-2 apne2-az1 | 128 | 100% | 9.0 | 9 (09-21 13:58Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 128 | 100% | 9.0 | 9 (09-21 13:58Z) |
| ap-northeast-2 apne2-az4 | 46 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-south-1 aps1-az1 | 43 | 49% | 5.9 | 9 (09-21 00:10Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 59 | 69% | 7.2 | 9 (09-21 00:10Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 60 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-1 use1-az4 | 61 | 97% | 8.8 | 9 (09-21 00:10Z) |
| us-east-1 use1-az5 | 28 | 96% | 8.8 | 9 (09-21 06:13Z) |
| us-east-1 use1-az6 | 57 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-2 use2-az1 | 56 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-2 use2-az2 | 89 | 98% | 8.8 | 9 (09-21 13:58Z) |
| us-east-2 use2-az3 | 74 | 89% | 8.3 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az1 | 50 | 98% | 8.9 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 40 | 98% | 8.8 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az3 | 55 | 98% | 8.9 | 9 (09-21 13:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.723000 | 2026-09-21T13:58:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-21T13:58:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.846700 | 2026-09-21T13:58:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.027700 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590900 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579700 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566700 | 2026-09-21T13:58:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742900 | 2026-09-21T13:58:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.482200 | 2026-09-21T13:58:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-21T13:58:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.446400 | 2026-09-21T13:58:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.313100 | 2026-09-21T13:58:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.691200 | 2026-09-21T13:58:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.528100 | 2026-09-21T13:58:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.815300 | 2026-09-21T13:58:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.831800 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1a | Windows | 0.361200 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.621400 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1b | Windows | 0.305200 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.505900 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1c | Windows | 0.289700 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.494300 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1d | Windows | 0.303900 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.480000 | 2026-09-21T13:58:58Z |
| us-east-1 | us-east-1f | Windows | 0.309200 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525300 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2a | Windows | 0.642000 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524500 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2b | Windows | 0.641800 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-09-21T13:58:58Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.547400 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2a | Windows | 0.337700 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.502800 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2b | Windows | 0.335700 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.505800 | 2026-09-21T13:58:58Z |
| us-west-2 | us-west-2c | Windows | 0.336100 | 2026-09-21T13:58:58Z |
