# Spot placement score log

Generated 2026-09-28 01:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 181 | 13% | 2.8 | 1 (09-28 01:03Z) |
| ap-northeast-1 | 181 | 3% | 2.1 | 1 (09-28 01:03Z) |
| ap-northeast-2 | 181 | 15% | 3.9 | 9 (09-28 01:03Z) |
| ap-south-1 | 181 | 3% | 2.1 | 1 (09-28 01:03Z) |
| ap-southeast-2 | 181 | 0% | 1.0 | 1 (09-28 01:03Z) |
| ap-southeast-3 | 181 | 13% | 3.3 | 1 (09-28 01:03Z) |
| us-east-1 | 181 | 2% | 2.2 | 9 (09-28 01:03Z) |
| us-east-2 | 181 | 12% | 2.6 | 9 (09-28 01:03Z) |
| us-west-2 | 181 | 6% | 2.1 | 9 (09-28 01:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333339999999991191999199999988991
ap-northeast-1   312322112122133222233222222113432215553166444421
ap-northeast-2   333333333333333333339999999999999999999999999999
ap-south-1       333333211111111111111111111211113114111159992791
ap-southeast-2   111111111311111111111111111111111111111111111111
ap-southeast-3   331333313331333333339968999519891589999286999891
us-east-1        233333333132122323222212321131223322392332222999
us-east-2        333333133111121131131929112199289999999999999999
us-west-2        333333333121122221322211222211121995192991299999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | · | 1 | 2 | 3 | 2 | 6 | 4 | 2 | 2 | 2 | 1 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | · | 3 | 3 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 2 | 3 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 6 | 4 | 3 | 2 | 2 | 2 | 5 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 3 | 4 | 1 | 2 | 2 | 1 | 4 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 55 | 0% | 1.4 | 3 (09-27 01:21Z) |
| ap-east-1 ape1-az2 | 118 | 19% | 3.7 | 9 (09-27 23:19Z) |
| ap-northeast-1 apne1-az1 | 23 | 0% | 1.3 | 2 (09-26 19:48Z) |
| ap-northeast-1 apne1-az4 | 80 | 0% | 2.1 | 3 (09-27 18:17Z) |
| ap-northeast-2 apne2-az1 | 163 | 17% | 3.9 | 9 (09-27 23:19Z) |
| ap-northeast-2 apne2-az3 | 163 | 17% | 4.0 | 9 (09-28 01:03Z) |
| ap-northeast-2 apne2-az4 | 178 | 16% | 3.9 | 9 (09-28 01:03Z) |
| ap-south-1 aps1-az1 | 60 | 2% | 1.8 | 7 (09-27 19:17Z) |
| ap-south-1 aps1-az3 | 86 | 3% | 2.7 | 8 (09-27 20:21Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 140 | 16% | 3.8 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 57 | 0% | 1.3 | 1 (09-26 19:48Z) |
| us-east-1 use1-az4 | 41 | 10% | 2.4 | 9 (09-28 01:03Z) |
| us-east-1 use1-az5 | 53 | 6% | 1.9 | 9 (09-28 01:03Z) |
| us-east-1 use1-az6 | 49 | 2% | 1.5 | 9 (09-28 01:03Z) |
| us-east-2 use2-az1 | 63 | 17% | 2.9 | 9 (09-27 23:19Z) |
| us-east-2 use2-az2 | 87 | 20% | 3.3 | 9 (09-28 01:03Z) |
| us-east-2 use2-az3 | 106 | 19% | 3.5 | 9 (09-28 01:03Z) |
| us-west-2 usw2-az1 | 61 | 18% | 3.2 | 9 (09-28 01:03Z) |
| us-west-2 usw2-az2 | 36 | 19% | 3.3 | 9 (09-28 01:03Z) |
| us-west-2 usw2-az3 | 88 | 9% | 2.4 | 9 (09-28 01:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 181 | 15% | 3.9 | 9 (09-28 01:03Z) |
| ap-northeast-1 | 181 | 80% | 7.7 | 1 (09-28 01:03Z) |
| ap-northeast-2 | 181 | 100% | 9.0 | 9 (09-28 01:03Z) |
| ap-south-1 | 181 | 54% | 6.1 | 9 (09-28 01:03Z) |
| ap-southeast-2 | 181 | 16% | 3.2 | 2 (09-28 01:03Z) |
| ap-southeast-3 | 181 | 13% | 3.3 | 1 (09-28 01:03Z) |
| us-east-1 | 181 | 77% | 7.0 | 9 (09-28 01:03Z) |
| us-east-2 | 181 | 78% | 7.4 | 9 (09-28 01:03Z) |
| us-west-2 | 181 | 58% | 6.0 | 9 (09-28 01:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333339999999999999999999999999999
ap-northeast-1   999999999999999999999934999219999999999999999991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999991999249998399992899989999999999999999999
ap-southeast-2   333333223312222222335122992229999999999999999222
ap-southeast-3   331333313331333333339968999519891589999286999891
us-east-1        999999999499944599966699545983479999999999999999
us-east-2        999999999339959999994999234899999999999999999999
us-west-2        999999999431954549955595544599343999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | · | 3 | 4 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 7 | 5 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | 4 | 7 | 2 | 2 | 3 | 2 | 5 | 4 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | · | 2 | 6 | 7 | 9 | 6 | 7 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 77 | 30% | 4.8 | 9 (09-28 01:03Z) |
| ap-east-1 ape1-az2 | 56 | 27% | 4.6 | 9 (09-27 22:21Z) |
| ap-east-1 ape1-az3 | 58 | 24% | 4.4 | 9 (09-28 01:03Z) |
| ap-northeast-1 apne1-az1 | 92 | 91% | 8.5 | 9 (09-27 18:17Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 117 | 100% | 9.0 | 9 (09-27 23:19Z) |
| ap-northeast-2 apne2-az1 | 149 | 100% | 9.0 | 9 (09-28 01:03Z) |
| ap-northeast-2 apne2-az2 | 29 | 55% | 6.3 | 9 (09-27 23:19Z) |
| ap-northeast-2 apne2-az3 | 161 | 100% | 9.0 | 9 (09-28 01:03Z) |
| ap-northeast-2 apne2-az4 | 67 | 30% | 4.8 | 9 (09-28 01:03Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 55 | 35% | 5.1 | 9 (09-28 01:03Z) |
| ap-south-1 aps1-az3 | 76 | 76% | 7.6 | 9 (09-28 01:03Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 22 | 45% | 5.7 | 9 (09-27 18:17Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 70 | 100% | 9.0 | 9 (09-27 23:19Z) |
| us-east-1 use1-az4 | 73 | 97% | 8.8 | 9 (09-27 20:21Z) |
| us-east-1 use1-az5 | 39 | 97% | 8.8 | 9 (09-28 01:03Z) |
| us-east-1 use1-az6 | 69 | 100% | 9.0 | 9 (09-28 01:03Z) |
| us-east-2 use2-az1 | 69 | 99% | 8.9 | 9 (09-27 23:19Z) |
| us-east-2 use2-az2 | 102 | 98% | 8.9 | 9 (09-27 22:21Z) |
| us-east-2 use2-az3 | 91 | 91% | 8.4 | 9 (09-27 23:19Z) |
| us-west-2 usw2-az1 | 57 | 98% | 8.9 | 9 (09-27 22:21Z) |
| us-west-2 usw2-az2 | 49 | 98% | 8.8 | 9 (09-28 01:03Z) |
| us-west-2 usw2-az3 | 62 | 98% | 8.9 | 9 (09-27 13:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730200 | 2026-09-28T01:03:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.872800 | 2026-09-28T01:03:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.825700 | 2026-09-28T01:03:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.008700 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593300 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578100 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568100 | 2026-09-28T01:03:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T01:03:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.549500 | 2026-09-28T01:03:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.346400 | 2026-09-28T01:03:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.572000 | 2026-09-28T01:03:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.327900 | 2026-09-28T01:03:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.693300 | 2026-09-28T01:03:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.506800 | 2026-09-28T01:03:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.664900 | 2026-09-28T01:03:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.650100 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1a | Windows | 0.311900 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.483500 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.430700 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.391800 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.422000 | 2026-09-28T01:03:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525600 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524400 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.512900 | 2026-09-28T01:03:45Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.506000 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2a | Windows | 0.333000 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.486900 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2b | Windows | 0.332900 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.482100 | 2026-09-28T01:03:45Z |
| us-west-2 | us-west-2c | Windows | 0.331900 | 2026-09-28T01:03:45Z |
