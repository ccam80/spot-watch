# Spot placement score log

Generated 2026-09-26 17:05 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 169 | 8% | 2.5 | 9 (09-26 17:05Z) |
| ap-northeast-1 | 169 | 1% | 2.0 | 5 (09-26 17:05Z) |
| ap-northeast-2 | 169 | 9% | 3.5 | 9 (09-26 17:05Z) |
| ap-south-1 | 169 | 0% | 1.9 | 4 (09-26 17:05Z) |
| ap-southeast-2 | 169 | 0% | 1.0 | 1 (09-26 17:05Z) |
| ap-southeast-3 | 169 | 8% | 3.0 | 9 (09-26 17:05Z) |
| us-east-1 | 169 | 0% | 2.0 | 2 (09-26 17:05Z) |
| us-east-2 | 169 | 5% | 2.2 | 9 (09-26 17:05Z) |
| us-west-2 | 169 | 2% | 1.8 | 5 (09-26 17:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333339999999991191999
ap-northeast-1   111221223322312322112122133222233222222113432215
ap-northeast-2   333333333333333333333333333333339999999999999999
ap-south-1       311312113333333333211111111111111111111211113114
ap-southeast-2   111111111111111111111311111111111111111111111111
ap-southeast-3   112333333333331333313331333333339968999519891589
us-east-1        123111213112233333333132122323222212321131223322
us-east-2        313311333312333333133111121131131929112199289999
us-west-2        131112333333333333333121122221322211222211121995
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 6 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 4 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 5 | · | 3 | 3 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 2 | · | 1 | 2 | 2 | 2 | 6 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 2 | 4 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 3 | 2 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 1.4 | 1 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 108 | 12% | 3.2 | 9 (09-26 17:05Z) |
| ap-northeast-1 apne1-az1 | 22 | 0% | 1.2 | 2 (09-25 22:14Z) |
| ap-northeast-1 apne1-az4 | 78 | 0% | 2.1 | 3 (09-26 17:05Z) |
| ap-northeast-2 apne2-az1 | 152 | 11% | 3.6 | 9 (09-26 17:05Z) |
| ap-northeast-2 apne2-az3 | 151 | 11% | 3.6 | 9 (09-26 17:05Z) |
| ap-northeast-2 apne2-az4 | 166 | 10% | 3.6 | 9 (09-26 17:05Z) |
| ap-south-1 aps1-az1 | 59 | 0% | 1.7 | 1 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 83 | 0% | 2.5 | 2 (09-26 01:28Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 131 | 10% | 3.4 | 9 (09-26 17:05Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 56 | 0% | 1.3 | 1 (09-25 18:30Z) |
| us-east-1 use1-az4 | 36 | 0% | 1.7 | 1 (09-26 01:28Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 56 | 7% | 2.3 | 9 (09-26 17:05Z) |
| us-east-2 use2-az2 | 76 | 8% | 2.4 | 9 (09-26 17:05Z) |
| us-east-2 use2-az3 | 95 | 9% | 2.8 | 9 (09-26 17:05Z) |
| us-west-2 usw2-az1 | 53 | 6% | 2.3 | 5 (09-26 17:05Z) |
| us-west-2 usw2-az2 | 31 | 6% | 2.4 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az3 | 82 | 2% | 1.9 | 9 (09-26 13:00Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 169 | 9% | 3.6 | 9 (09-26 17:05Z) |
| ap-northeast-1 | 169 | 79% | 7.6 | 9 (09-26 17:05Z) |
| ap-northeast-2 | 169 | 100% | 9.0 | 9 (09-26 17:05Z) |
| ap-south-1 | 169 | 50% | 5.8 | 9 (09-26 17:05Z) |
| ap-southeast-2 | 169 | 12% | 2.9 | 9 (09-26 17:05Z) |
| ap-southeast-3 | 169 | 8% | 3.0 | 9 (09-26 17:05Z) |
| us-east-1 | 169 | 76% | 6.9 | 9 (09-26 17:05Z) |
| us-east-2 | 169 | 76% | 7.3 | 9 (09-26 17:05Z) |
| us-west-2 | 169 | 55% | 5.8 | 9 (09-26 17:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333339999999999999999
ap-northeast-1   339999999999999999999999999999999934999219999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       923999999999999999991999249998399992899989999999
ap-southeast-2   223323333333333333223312222222335122992229999999
ap-southeast-3   112333333333331333313331333333339968999519891589
us-east-1        999454999999999999999499944599966699545983479999
us-east-2        999911999919999999999339959999994999234899999999
us-west-2        953345999999999999999431954549955595544599343999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | · | 3 | 4 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 7 | 3 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 4 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 65 | 17% | 4.0 | 9 (09-26 13:00Z) |
| ap-east-1 ape1-az2 | 51 | 20% | 4.2 | 9 (09-26 13:00Z) |
| ap-east-1 ape1-az3 | 54 | 19% | 4.1 | 9 (09-26 17:05Z) |
| ap-northeast-1 apne1-az1 | 89 | 91% | 8.4 | 9 (09-26 17:05Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 112 | 100% | 9.0 | 9 (09-26 17:05Z) |
| ap-northeast-2 apne2-az1 | 148 | 100% | 9.0 | 9 (09-26 07:34Z) |
| ap-northeast-2 apne2-az2 | 24 | 46% | 5.8 | 9 (09-26 17:05Z) |
| ap-northeast-2 apne2-az3 | 153 | 100% | 9.0 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az4 | 59 | 20% | 4.2 | 9 (09-26 17:05Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 44 | 18% | 4.1 | 9 (09-26 17:05Z) |
| ap-south-1 aps1-az3 | 74 | 76% | 7.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az1 | 18 | 44% | 5.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 18 | 33% | 5.0 | 9 (09-26 17:05Z) |
| ap-southeast-3 apse3-az3 | 46 | 13% | 3.8 | 9 (09-26 17:05Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 63 | 100% | 9.0 | 9 (09-26 13:00Z) |
| us-east-1 use1-az4 | 68 | 97% | 8.8 | 9 (09-26 17:05Z) |
| us-east-1 use1-az5 | 33 | 97% | 8.8 | 9 (09-26 13:00Z) |
| us-east-1 use1-az6 | 65 | 100% | 9.0 | 9 (09-26 07:34Z) |
| us-east-2 use2-az1 | 66 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-east-2 use2-az2 | 99 | 98% | 8.8 | 9 (09-26 01:28Z) |
| us-east-2 use2-az3 | 86 | 91% | 8.4 | 9 (09-25 22:14Z) |
| us-west-2 usw2-az1 | 52 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 61 | 98% | 8.9 | 9 (09-26 17:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727100 | 2026-09-26T17:05:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.852700 | 2026-09-26T17:05:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.826500 | 2026-09-26T17:05:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.995500 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592300 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577900 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568000 | 2026-09-26T17:05:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-09-26T17:05:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.533100 | 2026-09-26T17:05:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.343900 | 2026-09-26T17:05:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.528400 | 2026-09-26T17:05:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.319100 | 2026-09-26T17:05:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653900 | 2026-09-26T17:05:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515300 | 2026-09-26T17:05:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.713700 | 2026-09-26T17:05:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.685800 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1a | Windows | 0.320300 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.503000 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1b | Windows | 0.286000 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.432500 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.409700 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.424600 | 2026-09-26T17:05:35Z |
| us-east-1 | us-east-1f | Windows | 0.286300 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525200 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527200 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2b | Windows | 0.641800 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513400 | 2026-09-26T17:05:35Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513700 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.484800 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2b | Windows | 0.332300 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.484100 | 2026-09-26T17:05:35Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-26T17:05:35Z |
