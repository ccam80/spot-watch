# Spot placement score log

Generated 2026-09-23 20:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 154 | 1% | 2.0 | 9 (09-23 20:14Z) |
| ap-northeast-1 | 154 | 0% | 1.9 | 3 (09-23 20:14Z) |
| ap-northeast-2 | 154 | 1% | 3.0 | 9 (09-23 20:14Z) |
| ap-south-1 | 154 | 0% | 2.0 | 1 (09-23 20:14Z) |
| ap-southeast-2 | 154 | 0% | 1.0 | 1 (09-23 20:14Z) |
| ap-southeast-3 | 154 | 1% | 2.6 | 9 (09-23 20:14Z) |
| us-east-1 | 154 | 0% | 2.0 | 2 (09-23 20:14Z) |
| us-east-2 | 154 | 0% | 1.8 | 1 (09-23 20:14Z) |
| us-west-2 | 154 | 0% | 1.7 | 2 (09-23 20:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333339
ap-northeast-1   132212222112222111221223322312322112122133222233
ap-northeast-2   333333333333333333333333333333333333333333333339
ap-south-1       111121122111333311312113333333333211111111111111
ap-southeast-2   111111111111111111111111111111111111311111111111
ap-southeast-3   131331333331313112333333333331333313331333333339
us-east-1        122113112123223123111213112233333333132122323222
us-east-2        111113131333333313311333312333333133111121131131
us-west-2        211121111113122131112333333333333333121122221322
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 44 | 0% | 1.5 | 1 (09-23 20:14Z) |
| ap-east-1 ape1-az2 | 96 | 1% | 2.5 | 9 (09-23 20:14Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 69 | 0% | 2.2 | 1 (09-23 20:14Z) |
| ap-northeast-2 apne2-az1 | 137 | 1% | 3.0 | 9 (09-23 20:14Z) |
| ap-northeast-2 apne2-az3 | 136 | 1% | 3.0 | 9 (09-23 20:14Z) |
| ap-northeast-2 apne2-az4 | 151 | 1% | 3.0 | 9 (09-23 20:14Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 31 | 0% | 1.0 | 1 (09-23 16:48Z) |
| ap-southeast-3 apse3-az3 | 119 | 1% | 2.9 | 9 (09-23 20:14Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 54 | 0% | 1.3 | 1 (09-23 20:14Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 47 | 0% | 1.6 | 1 (09-23 16:48Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 51 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-east-2 use2-az2 | 63 | 0% | 2.0 | 1 (09-23 20:14Z) |
| us-east-2 use2-az3 | 83 | 0% | 2.3 | 3 (09-23 16:48Z) |
| us-west-2 usw2-az1 | 47 | 0% | 2.1 | 1 (09-23 20:14Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 154 | 1% | 3.0 | 9 (09-23 20:14Z) |
| ap-northeast-1 | 154 | 80% | 7.6 | 9 (09-23 20:14Z) |
| ap-northeast-2 | 154 | 100% | 9.0 | 9 (09-23 20:14Z) |
| ap-south-1 | 154 | 46% | 5.6 | 9 (09-23 20:14Z) |
| ap-southeast-2 | 154 | 7% | 2.6 | 5 (09-23 20:14Z) |
| ap-southeast-3 | 154 | 1% | 2.6 | 9 (09-23 20:14Z) |
| us-east-1 | 154 | 75% | 6.9 | 6 (09-23 20:14Z) |
| us-east-2 | 154 | 76% | 7.3 | 4 (09-23 20:14Z) |
| us-west-2 | 154 | 54% | 5.8 | 5 (09-23 20:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333339
ap-northeast-1   399924999419999339999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       189999299993999923999999999999999991999249998399
ap-southeast-2   222222332223322223323333333333333223312222222335
ap-southeast-3   131331333331313112333333333331333313331333333339
us-east-1        443249395599569999454999999999999999499944599966
us-east-2        992129999999999999911999919999999999339959999994
us-west-2        543353441399445953345999999999999999431954549955
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 5 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 5 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-east-1 ape1-az2 | 42 | 2% | 3.1 | 9 (09-23 20:14Z) |
| ap-east-1 ape1-az3 | 45 | 2% | 3.1 | 9 (09-23 20:14Z) |
| ap-northeast-1 apne1-az1 | 83 | 90% | 8.4 | 9 (09-23 16:48Z) |
| ap-northeast-1 apne1-az2 | 27 | 4% | 3.2 | 9 (09-23 20:14Z) |
| ap-northeast-1 apne1-az4 | 106 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az1 | 140 | 100% | 9.0 | 9 (09-23 20:14Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 140 | 100% | 9.0 | 9 (09-23 20:14Z) |
| ap-northeast-2 apne2-az4 | 48 | 2% | 3.1 | 9 (09-23 20:14Z) |
| ap-south-1 aps1-az1 | 50 | 56% | 6.4 | 9 (09-23 20:14Z) |
| ap-south-1 aps1-az2 | 37 | 3% | 3.2 | 9 (09-23 20:14Z) |
| ap-south-1 aps1-az3 | 67 | 73% | 7.4 | 9 (09-23 20:14Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 41 | 2% | 3.1 | 9 (09-23 20:14Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 30 | 97% | 8.8 | 9 (09-23 00:22Z) |
| us-east-1 use1-az6 | 62 | 100% | 9.0 | 9 (09-23 11:25Z) |
| us-east-2 use2-az1 | 61 | 98% | 8.9 | 9 (09-23 00:22Z) |
| us-east-2 use2-az2 | 97 | 98% | 8.8 | 9 (09-23 16:48Z) |
| us-east-2 use2-az3 | 81 | 90% | 8.3 | 9 (09-23 16:48Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727600 | 2026-09-23T20:14:28Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.865900 | 2026-09-23T20:14:28Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.851700 | 2026-09-23T20:14:28Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.032700 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591900 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579400 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568500 | 2026-09-23T20:14:28Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-23T20:14:28Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.485300 | 2026-09-23T20:14:28Z |
| ap-south-1 | ap-south-1a | Windows | 0.334200 | 2026-09-23T20:14:28Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.453700 | 2026-09-23T20:14:28Z |
| ap-south-1 | ap-south-1b | Windows | 0.307100 | 2026-09-23T20:14:28Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653300 | 2026-09-23T20:14:28Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.524700 | 2026-09-23T20:14:28Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.772200 | 2026-09-23T20:14:28Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.777700 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1a | Windows | 0.340900 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.581200 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1b | Windows | 0.293000 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.463100 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1c | Windows | 0.286700 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.455200 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1d | Windows | 0.291400 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.442200 | 2026-09-23T20:14:28Z |
| us-east-1 | us-east-1f | Windows | 0.298400 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525700 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523600 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.510600 | 2026-09-23T20:14:28Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.517500 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2a | Windows | 0.334700 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.483000 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2b | Windows | 0.333400 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.487200 | 2026-09-23T20:14:28Z |
| us-west-2 | us-west-2c | Windows | 0.333500 | 2026-09-23T20:14:28Z |
