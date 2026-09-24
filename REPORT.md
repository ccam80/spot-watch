# Spot placement score log

Generated 2026-09-24 09:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 157 | 3% | 2.2 | 9 (09-24 09:55Z) |
| ap-northeast-1 | 157 | 0% | 1.9 | 2 (09-24 09:55Z) |
| ap-northeast-2 | 157 | 3% | 3.1 | 9 (09-24 09:55Z) |
| ap-south-1 | 157 | 0% | 2.0 | 1 (09-24 09:55Z) |
| ap-southeast-2 | 157 | 0% | 1.0 | 1 (09-24 09:55Z) |
| ap-southeast-3 | 157 | 3% | 2.7 | 8 (09-24 09:55Z) |
| us-east-1 | 157 | 0% | 2.0 | 2 (09-24 09:55Z) |
| us-east-2 | 157 | 1% | 1.9 | 9 (09-24 09:55Z) |
| us-west-2 | 157 | 0% | 1.7 | 1 (09-24 09:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333339999
ap-northeast-1   212222112222111221223322312322112122133222233222
ap-northeast-2   333333333333333333333333333333333333333333339999
ap-south-1       121122111333311312113333333333211111111111111111
ap-southeast-2   111111111111111111111111111111111311111111111111
ap-southeast-3   331333331313112333333333331333313331333333339968
us-east-1        113112123223123111213112233333333132122323222212
us-east-2        113131333333313311333312333333133111121131131929
us-west-2        121111113122131112333333333333333121122221322211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 47 | 0% | 1.4 | 1 (09-24 09:55Z) |
| ap-east-1 ape1-az2 | 99 | 4% | 2.7 | 9 (09-24 09:55Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 71 | 0% | 2.2 | 1 (09-24 04:37Z) |
| ap-northeast-2 apne2-az1 | 140 | 3% | 3.1 | 9 (09-24 09:55Z) |
| ap-northeast-2 apne2-az3 | 139 | 3% | 3.1 | 9 (09-24 09:55Z) |
| ap-northeast-2 apne2-az4 | 154 | 3% | 3.1 | 9 (09-24 09:55Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 34 | 0% | 1.0 | 1 (09-24 09:55Z) |
| ap-southeast-3 apse3-az3 | 122 | 3% | 3.1 | 8 (09-24 09:55Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 54 | 0% | 1.3 | 1 (09-23 20:14Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 48 | 0% | 1.5 | 1 (09-23 23:37Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 52 | 2% | 1.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 65 | 2% | 2.1 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 86 | 2% | 2.4 | 9 (09-24 09:55Z) |
| us-west-2 usw2-az1 | 47 | 0% | 2.1 | 1 (09-23 20:14Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 157 | 3% | 3.2 | 9 (09-24 09:55Z) |
| ap-northeast-1 | 157 | 79% | 7.6 | 4 (09-24 09:55Z) |
| ap-northeast-2 | 157 | 100% | 9.0 | 9 (09-24 09:55Z) |
| ap-south-1 | 157 | 46% | 5.6 | 2 (09-24 09:55Z) |
| ap-southeast-2 | 157 | 7% | 2.6 | 2 (09-24 09:55Z) |
| ap-southeast-3 | 157 | 3% | 2.7 | 8 (09-24 09:55Z) |
| us-east-1 | 157 | 76% | 6.9 | 9 (09-24 09:55Z) |
| us-east-2 | 157 | 76% | 7.3 | 9 (09-24 09:55Z) |
| us-west-2 | 157 | 55% | 5.8 | 5 (09-24 09:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333339999
ap-northeast-1   924999419999339999999999999999999999999999999934
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999299993999923999999999999999991999249998399992
ap-southeast-2   222332223322223323333333333333223312222222335122
ap-southeast-3   331333331313112333333333331333313331333333339968
us-east-1        249395599569999454999999999999999499944599966699
us-east-2        129999999999999911999919999999999339959999994999
us-west-2        353441399445953345999999999999999431954549955595
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 57 | 5% | 3.3 | 9 (09-24 09:55Z) |
| ap-east-1 ape1-az2 | 44 | 7% | 3.4 | 9 (09-24 09:55Z) |
| ap-east-1 ape1-az3 | 47 | 6% | 3.4 | 9 (09-24 09:55Z) |
| ap-northeast-1 apne1-az1 | 84 | 90% | 8.4 | 9 (09-23 23:37Z) |
| ap-northeast-1 apne1-az2 | 27 | 4% | 3.2 | 9 (09-23 20:14Z) |
| ap-northeast-1 apne1-az4 | 106 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az1 | 142 | 100% | 9.0 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az2 | 15 | 13% | 3.8 | 9 (09-24 09:55Z) |
| ap-northeast-2 apne2-az3 | 143 | 100% | 9.0 | 9 (09-24 09:55Z) |
| ap-northeast-2 apne2-az4 | 51 | 8% | 3.5 | 9 (09-24 09:55Z) |
| ap-south-1 aps1-az1 | 51 | 57% | 6.4 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az2 | 38 | 5% | 3.3 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az3 | 68 | 74% | 7.4 | 9 (09-24 04:37Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 42 | 5% | 3.3 | 9 (09-23 23:37Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 63 | 100% | 9.0 | 9 (09-24 04:37Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 83 | 90% | 8.3 | 9 (09-24 09:55Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727600 | 2026-09-24T09:55:02Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.867900 | 2026-09-24T09:55:02Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.843600 | 2026-09-24T09:55:02Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.024500 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591800 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578800 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568600 | 2026-09-24T09:55:02Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-24T09:55:02Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.489400 | 2026-09-24T09:55:02Z |
| ap-south-1 | ap-south-1a | Windows | 0.332300 | 2026-09-24T09:55:02Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.472800 | 2026-09-24T09:55:02Z |
| ap-south-1 | ap-south-1b | Windows | 0.307000 | 2026-09-24T09:55:02Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.643100 | 2026-09-24T09:55:02Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523100 | 2026-09-24T09:55:02Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.758600 | 2026-09-24T09:55:02Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.570600 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.758100 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1a | Windows | 0.337600 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.561800 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1b | Windows | 0.292100 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.451100 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.443400 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1d | Windows | 0.289700 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.433400 | 2026-09-24T09:55:02Z |
| us-east-1 | us-east-1f | Windows | 0.296700 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524800 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524600 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.510700 | 2026-09-24T09:55:02Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.517400 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2a | Windows | 0.333900 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.482900 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2b | Windows | 0.333400 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-24T09:55:02Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-24T09:55:02Z |
