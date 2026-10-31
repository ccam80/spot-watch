# Spot placement score log

Generated 2026-10-31 13:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 475 | 48% | 5.2 | 9 (10-31 13:12Z) |
| ap-northeast-1 | 475 | 14% | 2.6 | 1 (10-31 13:12Z) |
| ap-northeast-2 | 475 | 67% | 7.0 | 9 (10-31 13:12Z) |
| ap-south-1 | 475 | 2% | 1.7 | 1 (10-31 13:12Z) |
| ap-southeast-2 | 475 | 0% | 1.0 | 1 (10-31 13:12Z) |
| ap-southeast-3 | 475 | 25% | 3.3 | 1 (10-31 13:12Z) |
| us-east-1 | 475 | 10% | 2.6 | 1 (10-31 13:12Z) |
| us-east-2 | 475 | 29% | 3.6 | 1 (10-31 13:12Z) |
| us-west-2 | 475 | 9% | 2.2 | 4 (10-31 13:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        221442121219999999999999999911111199911111999999
ap-northeast-1   211111222211111111111222287111124211144211111211
ap-northeast-2   999999999999999999999999999999999999999119999999
ap-south-1       111111111111111111111122111121111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   123321111111111111111117867511111111111111111551
us-east-1        333322111123333333323322222222211122222222222221
us-east-2        111111111111112899129111111111111111111111199111
us-west-2        111111222222222111221111111111111111111111111194
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 154 | 6% | 1.6 | 1 (10-31 06:19Z) |
| ap-east-1 ape1-az2 | 350 | 65% | 6.6 | 9 (10-31 13:12Z) |
| ap-northeast-1 apne1-az1 | 99 | 4% | 1.4 | 2 (10-31 11:11Z) |
| ap-northeast-1 apne1-az4 | 214 | 25% | 3.5 | 1 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 406 | 60% | 6.4 | 9 (10-31 09:13Z) |
| ap-northeast-2 apne2-az3 | 442 | 67% | 6.9 | 9 (10-31 13:12Z) |
| ap-northeast-2 apne2-az4 | 469 | 67% | 7.0 | 9 (10-31 13:12Z) |
| ap-south-1 aps1-az1 | 136 | 1% | 1.3 | 1 (10-31 13:12Z) |
| ap-south-1 aps1-az3 | 128 | 5% | 2.4 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az1 | 89 | 2% | 1.2 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az2 | 56 | 0% | 1.0 | 1 (10-31 04:15Z) |
| ap-southeast-3 apse3-az1 | 85 | 0% | 1.0 | 1 (10-31 09:13Z) |
| ap-southeast-3 apse3-az3 | 299 | 39% | 4.4 | 1 (10-31 13:12Z) |
| us-east-1 use1-az1 | 97 | 0% | 1.1 | 1 (10-31 13:12Z) |
| us-east-1 use1-az2 | 132 | 2% | 1.3 | 1 (10-31 13:12Z) |
| us-east-1 use1-az4 | 156 | 23% | 3.0 | 1 (10-31 13:12Z) |
| us-east-1 use1-az5 | 154 | 25% | 3.1 | 1 (10-31 12:17Z) |
| us-east-1 use1-az6 | 115 | 23% | 3.0 | 1 (10-31 11:11Z) |
| us-east-2 use2-az1 | 199 | 42% | 4.5 | 1 (10-31 13:12Z) |
| us-east-2 use2-az2 | 242 | 49% | 5.2 | 1 (10-31 11:11Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 148 | 25% | 3.3 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az2 | 116 | 18% | 2.7 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az3 | 191 | 17% | 2.7 | 3 (10-31 13:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 475 | 68% | 7.1 | 9 (10-31 13:12Z) |
| ap-northeast-1 | 475 | 72% | 7.0 | 9 (10-31 13:12Z) |
| ap-northeast-2 | 475 | 100% | 9.0 | 9 (10-31 13:12Z) |
| ap-south-1 | 475 | 61% | 6.3 | 9 (10-31 13:12Z) |
| ap-southeast-2 | 475 | 22% | 3.3 | 9 (10-31 13:12Z) |
| ap-southeast-3 | 475 | 25% | 3.3 | 1 (10-31 13:12Z) |
| us-east-1 | 475 | 70% | 6.4 | 9 (10-31 13:12Z) |
| us-east-2 | 475 | 67% | 6.6 | 9 (10-31 13:12Z) |
| us-west-2 | 475 | 51% | 5.6 | 5 (10-31 13:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999911111111113399999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111299999999991111111122111129999999999997999999
ap-southeast-2   999999111111111111111111111111111199999991113199
ap-southeast-3   123321111111111111111117867511111111111111111551
us-east-1        565556545466666999999999323233343393943999999999
us-east-2        122221212222249999999932222222222222289999999999
us-west-2        993344455344555933559999948443959312112332449995
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 304 | 82% | 7.9 | 9 (10-31 13:12Z) |
| ap-east-1 ape1-az2 | 265 | 85% | 8.1 | 9 (10-31 12:17Z) |
| ap-east-1 ape1-az3 | 294 | 85% | 8.1 | 9 (10-31 11:11Z) |
| ap-northeast-1 apne1-az1 | 201 | 95% | 8.7 | 9 (10-31 13:12Z) |
| ap-northeast-1 apne1-az2 | 169 | 84% | 8.0 | 9 (10-31 12:17Z) |
| ap-northeast-1 apne1-az4 | 252 | 99% | 8.9 | 9 (10-31 13:12Z) |
| ap-northeast-2 apne2-az1 | 390 | 100% | 9.0 | 9 (10-31 13:12Z) |
| ap-northeast-2 apne2-az2 | 99 | 84% | 8.0 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az3 | 414 | 100% | 9.0 | 9 (10-31 12:17Z) |
| ap-northeast-2 apne2-az4 | 312 | 85% | 8.1 | 9 (10-31 13:12Z) |
| ap-south-1 aps1-az1 | 163 | 87% | 8.2 | 9 (10-31 09:13Z) |
| ap-south-1 aps1-az2 | 180 | 79% | 7.7 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az3 | 180 | 89% | 8.3 | 9 (10-31 11:11Z) |
| ap-southeast-2 apse2-az1 | 54 | 81% | 7.9 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 64 | 80% | 7.8 | 9 (10-31 13:12Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 26 | 50% | 5.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az2 | 101 | 100% | 9.0 | 9 (10-31 12:17Z) |
| us-east-1 use1-az4 | 131 | 91% | 8.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az5 | 96 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 165 | 99% | 8.9 | 9 (10-31 13:12Z) |
| us-east-2 use2-az2 | 188 | 99% | 8.9 | 9 (10-31 09:13Z) |
| us-east-2 use2-az3 | 213 | 96% | 8.7 | 9 (10-31 13:12Z) |
| us-west-2 usw2-az1 | 90 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 120 | 89% | 8.2 | 9 (10-31 11:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700400 | 2026-10-31T13:12:18Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T13:12:18Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742400 | 2026-10-31T13:12:18Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.885800 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583700 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591000 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T13:12:18Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T13:12:18Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.639400 | 2026-10-31T13:12:18Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T13:12:18Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.537600 | 2026-10-31T13:12:18Z |
| ap-south-1 | ap-south-1b | Windows | 0.382100 | 2026-10-31T13:12:18Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651700 | 2026-10-31T13:12:18Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T13:12:18Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656000 | 2026-10-31T13:12:18Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.562000 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.575900 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.510500 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.505900 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558300 | 2026-10-31T13:12:18Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559400 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547300 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T13:12:18Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.555400 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2a | Windows | 0.314200 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572600 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2b | Windows | 0.322000 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544600 | 2026-10-31T13:12:18Z |
| us-west-2 | us-west-2c | Windows | 0.313800 | 2026-10-31T13:12:18Z |
