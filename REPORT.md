# Spot placement score log

Generated 2026-09-25 13:40 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 163 | 6% | 2.4 | 1 (09-25 13:39Z) |
| ap-northeast-1 | 163 | 0% | 1.9 | 3 (09-25 13:39Z) |
| ap-northeast-2 | 163 | 6% | 3.3 | 9 (09-25 13:39Z) |
| ap-south-1 | 163 | 0% | 1.9 | 1 (09-25 13:39Z) |
| ap-southeast-2 | 163 | 0% | 1.0 | 1 (09-25 13:39Z) |
| ap-southeast-3 | 163 | 6% | 2.9 | 9 (09-25 13:39Z) |
| us-east-1 | 163 | 0% | 2.0 | 1 (09-25 13:39Z) |
| us-east-2 | 163 | 2% | 2.0 | 9 (09-25 13:39Z) |
| us-west-2 | 163 | 0% | 1.7 | 1 (09-25 13:39Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333339999999991
ap-northeast-1   112222111221223322312322112122133222233222222113
ap-northeast-2   333333333333333333333333333333333333339999999999
ap-south-1       111333311312113333333333211111111111111111111211
ap-southeast-2   111111111111111111111111111311111111111111111111
ap-southeast-3   331313112333333333331333313331333333339968999519
us-east-1        123223123111213112233333333132122323222212321131
us-east-2        333333313311333312333333133111121131131929112199
us-west-2        113122131112333333333333333121122221322211222211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | · | 1 | 2 | 3 | 2 | 5 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 4 | · | 3 | 3 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 53 | 0% | 1.4 | 1 (09-25 13:39Z) |
| ap-east-1 ape1-az2 | 104 | 9% | 3.0 | 9 (09-25 07:40Z) |
| ap-northeast-1 apne1-az1 | 21 | 0% | 1.2 | 2 (09-25 13:39Z) |
| ap-northeast-1 apne1-az4 | 76 | 0% | 2.1 | 1 (09-25 07:40Z) |
| ap-northeast-2 apne2-az1 | 146 | 7% | 3.4 | 9 (09-25 13:39Z) |
| ap-northeast-2 apne2-az3 | 145 | 7% | 3.3 | 9 (09-25 13:39Z) |
| ap-northeast-2 apne2-az4 | 160 | 6% | 3.4 | 9 (09-25 13:39Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 127 | 7% | 3.3 | 9 (09-25 13:39Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 55 | 0% | 1.3 | 1 (09-25 07:40Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 53 | 4% | 2.1 | 9 (09-25 13:39Z) |
| us-east-2 use2-az2 | 71 | 3% | 2.1 | 9 (09-25 13:39Z) |
| us-east-2 use2-az3 | 90 | 4% | 2.5 | 9 (09-25 13:39Z) |
| us-west-2 usw2-az1 | 49 | 0% | 2.0 | 1 (09-25 13:39Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 163 | 6% | 3.4 | 9 (09-25 13:39Z) |
| ap-northeast-1 | 163 | 79% | 7.6 | 9 (09-25 13:39Z) |
| ap-northeast-2 | 163 | 100% | 9.0 | 9 (09-25 13:39Z) |
| ap-south-1 | 163 | 48% | 5.7 | 9 (09-25 13:39Z) |
| ap-southeast-2 | 163 | 9% | 2.7 | 9 (09-25 13:39Z) |
| ap-southeast-3 | 163 | 6% | 2.9 | 9 (09-25 13:39Z) |
| us-east-1 | 163 | 75% | 6.9 | 3 (09-25 13:39Z) |
| us-east-2 | 163 | 75% | 7.3 | 9 (09-25 13:39Z) |
| us-west-2 | 163 | 55% | 5.8 | 9 (09-25 13:39Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333339999999999
ap-northeast-1   419999339999999999999999999999999999999934999219
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       993999923999999999999999991999249998399992899989
ap-southeast-2   223322223323333333333333223312222222335122992229
ap-southeast-3   331313112333333333331333313331333333339968999519
us-east-1        599569999454999999999999999499944599966699545983
us-east-2        999999999911999919999999999339959999994999234899
us-west-2        399445953345999999999999999431954549955595544599
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 4 | · | 3 | 4 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 3 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 6 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 5 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 61 | 11% | 3.7 | 9 (09-25 13:39Z) |
| ap-east-1 ape1-az2 | 48 | 15% | 3.9 | 9 (09-25 13:39Z) |
| ap-east-1 ape1-az3 | 51 | 14% | 3.8 | 9 (09-25 07:40Z) |
| ap-northeast-1 apne1-az1 | 88 | 91% | 8.4 | 9 (09-25 13:39Z) |
| ap-northeast-1 apne1-az2 | 29 | 10% | 3.6 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az4 | 109 | 100% | 9.0 | 9 (09-24 22:18Z) |
| ap-northeast-2 apne2-az1 | 145 | 100% | 9.0 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az2 | 21 | 38% | 5.3 | 9 (09-25 13:39Z) |
| ap-northeast-2 apne2-az3 | 148 | 100% | 9.0 | 9 (09-25 13:39Z) |
| ap-northeast-2 apne2-az4 | 56 | 16% | 4.0 | 9 (09-25 07:40Z) |
| ap-south-1 aps1-az1 | 52 | 58% | 6.5 | 9 (09-24 22:18Z) |
| ap-south-1 aps1-az2 | 42 | 14% | 3.9 | 9 (09-25 13:39Z) |
| ap-south-1 aps1-az3 | 70 | 74% | 7.5 | 9 (09-25 01:25Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 15 | 20% | 4.2 | 9 (09-25 13:39Z) |
| ap-southeast-3 apse3-az3 | 45 | 11% | 3.7 | 9 (09-25 13:39Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 66 | 97% | 8.8 | 9 (09-25 01:25Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 64 | 100% | 9.0 | 9 (09-25 01:25Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 85 | 91% | 8.4 | 9 (09-25 13:39Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 60 | 98% | 8.9 | 9 (09-25 13:39Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.726300 | 2026-09-25T13:39:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.858900 | 2026-09-25T13:39:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.832400 | 2026-09-25T13:39:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.019200 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591200 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578000 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568200 | 2026-09-25T13:39:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-25T13:39:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.510200 | 2026-09-25T13:39:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.330200 | 2026-09-25T13:39:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.492800 | 2026-09-25T13:39:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.311800 | 2026-09-25T13:39:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.642800 | 2026-09-25T13:39:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515300 | 2026-09-25T13:39:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.750900 | 2026-09-25T13:39:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.729900 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1a | Windows | 0.327000 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.533600 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1b | Windows | 0.290100 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.433000 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.423300 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.427900 | 2026-09-25T13:39:54Z |
| us-east-1 | us-east-1f | Windows | 0.290200 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525300 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2a | Windows | 0.640700 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.526900 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2b | Windows | 0.642400 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513700 | 2026-09-25T13:39:54Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.515700 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2a | Windows | 0.332800 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.487700 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2b | Windows | 0.332700 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486500 | 2026-09-25T13:39:54Z |
| us-west-2 | us-west-2c | Windows | 0.331800 | 2026-09-25T13:39:54Z |
