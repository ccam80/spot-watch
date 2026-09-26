# Spot placement score log

Generated 2026-09-26 01:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 166 | 6% | 2.4 | 1 (09-26 01:28Z) |
| ap-northeast-1 | 166 | 0% | 2.0 | 2 (09-26 01:28Z) |
| ap-northeast-2 | 166 | 8% | 3.4 | 9 (09-26 01:28Z) |
| ap-south-1 | 166 | 0% | 1.9 | 3 (09-26 01:28Z) |
| ap-southeast-2 | 166 | 0% | 1.0 | 1 (09-26 01:28Z) |
| ap-southeast-3 | 166 | 7% | 2.9 | 1 (09-26 01:28Z) |
| us-east-1 | 166 | 0% | 2.0 | 3 (09-26 01:28Z) |
| us-east-2 | 166 | 4% | 2.0 | 9 (09-26 01:28Z) |
| us-west-2 | 166 | 0% | 1.7 | 1 (09-26 01:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333339999999991191
ap-northeast-1   222111221223322312322112122133222233222222113432
ap-northeast-2   333333333333333333333333333333333339999999999999
ap-south-1       333311312113333333333211111111111111111111211113
ap-southeast-2   111111111111111111111111311111111111111111111111
ap-southeast-3   313112333333333331333313331333333339968999519891
us-east-1        223123111213112233333333132122323222212321131223
us-east-2        333313311333312333333133111121131131929112199289
us-west-2        122131112333333333333333121122221322211222211121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 5 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 5 | · | 3 | 3 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 2 | · | 1 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 1.4 | 1 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 105 | 10% | 3.1 | 9 (09-25 22:14Z) |
| ap-northeast-1 apne1-az1 | 22 | 0% | 1.2 | 2 (09-25 22:14Z) |
| ap-northeast-1 apne1-az4 | 77 | 0% | 2.1 | 1 (09-25 18:30Z) |
| ap-northeast-2 apne2-az1 | 149 | 9% | 3.5 | 9 (09-26 01:28Z) |
| ap-northeast-2 apne2-az3 | 148 | 9% | 3.4 | 9 (09-26 01:28Z) |
| ap-northeast-2 apne2-az4 | 163 | 8% | 3.5 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az1 | 59 | 0% | 1.7 | 1 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 83 | 0% | 2.5 | 2 (09-26 01:28Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 129 | 9% | 3.3 | 9 (09-25 22:14Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 56 | 0% | 1.3 | 1 (09-25 18:30Z) |
| us-east-1 use1-az4 | 36 | 0% | 1.7 | 1 (09-26 01:28Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 54 | 4% | 2.0 | 1 (09-26 01:28Z) |
| us-east-2 use2-az2 | 73 | 4% | 2.2 | 9 (09-26 01:28Z) |
| us-east-2 use2-az3 | 92 | 7% | 2.6 | 9 (09-26 01:28Z) |
| us-west-2 usw2-az1 | 50 | 0% | 2.0 | 1 (09-25 18:30Z) |
| us-west-2 usw2-az2 | 29 | 0% | 2.0 | 1 (09-25 22:14Z) |
| us-west-2 usw2-az3 | 80 | 0% | 1.8 | 1 (09-26 01:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 166 | 8% | 3.5 | 9 (09-26 01:28Z) |
| ap-northeast-1 | 166 | 79% | 7.6 | 9 (09-26 01:28Z) |
| ap-northeast-2 | 166 | 100% | 9.0 | 9 (09-26 01:28Z) |
| ap-south-1 | 166 | 49% | 5.8 | 9 (09-26 01:28Z) |
| ap-southeast-2 | 166 | 10% | 2.8 | 9 (09-26 01:28Z) |
| ap-southeast-3 | 166 | 7% | 2.9 | 1 (09-26 01:28Z) |
| us-east-1 | 166 | 75% | 6.9 | 9 (09-26 01:28Z) |
| us-east-2 | 166 | 76% | 7.3 | 9 (09-26 01:28Z) |
| us-west-2 | 166 | 54% | 5.8 | 3 (09-26 01:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333339999999999999
ap-northeast-1   999339999999999999999999999999999999934999219999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999923999999999999999991999249998399992899989999
ap-southeast-2   322223323333333333333223312222222335122992229999
ap-southeast-3   313112333333333331333313331333333339968999519891
us-east-1        569999454999999999999999499944599966699545983479
us-east-2        999999911999919999999999339959999994999234899999
us-west-2        445953345999999999999999431954549955595544599343
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | · | 3 | 4 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 3 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 6 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 5 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 63 | 14% | 3.9 | 9 (09-26 01:28Z) |
| ap-east-1 ape1-az2 | 50 | 18% | 4.1 | 9 (09-26 01:28Z) |
| ap-east-1 ape1-az3 | 52 | 15% | 3.9 | 9 (09-25 18:30Z) |
| ap-northeast-1 apne1-az1 | 88 | 91% | 8.4 | 9 (09-25 13:39Z) |
| ap-northeast-1 apne1-az2 | 31 | 16% | 4.0 | 9 (09-25 22:14Z) |
| ap-northeast-1 apne1-az4 | 110 | 100% | 9.0 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az1 | 147 | 100% | 9.0 | 9 (09-25 22:14Z) |
| ap-northeast-2 apne2-az2 | 22 | 41% | 5.5 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az3 | 151 | 100% | 9.0 | 9 (09-26 01:28Z) |
| ap-northeast-2 apne2-az4 | 58 | 19% | 4.1 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 43 | 16% | 4.0 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 72 | 75% | 7.5 | 9 (09-25 22:14Z) |
| ap-southeast-2 apse2-az1 | 16 | 38% | 5.1 | 9 (09-26 01:28Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 17 | 29% | 4.8 | 9 (09-25 22:14Z) |
| ap-southeast-3 apse3-az3 | 45 | 11% | 3.7 | 9 (09-25 13:39Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 67 | 97% | 8.8 | 9 (09-26 01:28Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 64 | 100% | 9.0 | 9 (09-25 01:25Z) |
| us-east-2 use2-az1 | 64 | 98% | 8.9 | 9 (09-26 01:28Z) |
| us-east-2 use2-az2 | 99 | 98% | 8.8 | 9 (09-26 01:28Z) |
| us-east-2 use2-az3 | 86 | 91% | 8.4 | 9 (09-25 22:14Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 60 | 98% | 8.9 | 9 (09-25 13:39Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727100 | 2026-09-26T01:28:17Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.854900 | 2026-09-26T01:28:17Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.828400 | 2026-09-26T01:28:17Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.009400 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591400 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577700 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568000 | 2026-09-26T01:28:17Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-26T01:28:17Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.527700 | 2026-09-26T01:28:17Z |
| ap-south-1 | ap-south-1a | Windows | 0.337600 | 2026-09-26T01:28:17Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.512500 | 2026-09-26T01:28:17Z |
| ap-south-1 | ap-south-1b | Windows | 0.312900 | 2026-09-26T01:28:17Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.649100 | 2026-09-26T01:28:17Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.516400 | 2026-09-26T01:28:17Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.729200 | 2026-09-26T01:28:17Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.707000 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1a | Windows | 0.325400 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.519400 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1b | Windows | 0.289900 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.433000 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.422700 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.427300 | 2026-09-26T01:28:17Z |
| us-east-1 | us-east-1f | Windows | 0.289700 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525900 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.526800 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2b | Windows | 0.642300 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513500 | 2026-09-26T01:28:17Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513800 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2a | Windows | 0.332600 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.485300 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2b | Windows | 0.332400 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.484700 | 2026-09-26T01:28:17Z |
| us-west-2 | us-west-2c | Windows | 0.331500 | 2026-09-26T01:28:17Z |
