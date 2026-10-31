# Spot placement score log

Generated 2026-10-31 10:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 472 | 48% | 5.2 | 9 (10-31 10:12Z) |
| ap-northeast-1 | 472 | 14% | 2.6 | 1 (10-31 10:12Z) |
| ap-northeast-2 | 472 | 67% | 7.0 | 9 (10-31 10:12Z) |
| ap-south-1 | 472 | 2% | 1.7 | 1 (10-31 10:12Z) |
| ap-southeast-2 | 472 | 0% | 1.0 | 1 (10-31 10:12Z) |
| ap-southeast-3 | 472 | 25% | 3.3 | 1 (10-31 10:12Z) |
| us-east-1 | 472 | 10% | 2.6 | 2 (10-31 10:12Z) |
| us-east-2 | 472 | 29% | 3.6 | 9 (10-31 10:12Z) |
| us-west-2 | 472 | 9% | 2.1 | 1 (10-31 10:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111221442121219999999999999999911111199911111999
ap-northeast-1   222211111222211111111111222287111124211144211111
ap-northeast-2   999999999999999999999999999999999999999999119999
ap-south-1       111111111111111111111111122111121111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111123321111111111111111117867511111111111111111
us-east-1        332333322111123333333323322222222211122222222222
us-east-2        111111111111111112899129111111111111111111111199
us-west-2        112111111222222222111221111111111111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
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
| ap-east-1 ape1-az2 | 347 | 65% | 6.6 | 9 (10-31 10:12Z) |
| ap-northeast-1 apne1-az1 | 98 | 4% | 1.4 | 1 (10-31 02:17Z) |
| ap-northeast-1 apne1-az4 | 214 | 25% | 3.5 | 1 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 406 | 60% | 6.4 | 9 (10-31 09:13Z) |
| ap-northeast-2 apne2-az3 | 439 | 67% | 6.9 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az4 | 466 | 67% | 7.0 | 9 (10-31 10:12Z) |
| ap-south-1 aps1-az1 | 134 | 1% | 1.4 | 1 (10-31 08:16Z) |
| ap-south-1 aps1-az3 | 127 | 6% | 2.4 | 1 (10-31 10:12Z) |
| ap-southeast-2 apse2-az1 | 88 | 2% | 1.2 | 1 (10-31 10:12Z) |
| ap-southeast-2 apse2-az2 | 56 | 0% | 1.0 | 1 (10-31 04:15Z) |
| ap-southeast-3 apse3-az1 | 85 | 0% | 1.0 | 1 (10-31 09:13Z) |
| ap-southeast-3 apse3-az3 | 296 | 39% | 4.4 | 1 (10-30 23:11Z) |
| us-east-1 use1-az1 | 96 | 0% | 1.1 | 1 (10-31 09:13Z) |
| us-east-1 use1-az2 | 130 | 2% | 1.4 | 1 (10-31 09:13Z) |
| us-east-1 use1-az4 | 155 | 23% | 3.0 | 1 (10-31 08:16Z) |
| us-east-1 use1-az5 | 153 | 25% | 3.2 | 1 (10-31 10:12Z) |
| us-east-1 use1-az6 | 114 | 24% | 3.0 | 1 (10-31 09:13Z) |
| us-east-2 use2-az1 | 198 | 42% | 4.6 | 9 (10-31 10:12Z) |
| us-east-2 use2-az2 | 241 | 49% | 5.2 | 9 (10-31 10:12Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 147 | 24% | 3.3 | 1 (10-31 07:13Z) |
| us-west-2 usw2-az2 | 115 | 17% | 2.6 | 1 (10-31 07:13Z) |
| us-west-2 usw2-az3 | 188 | 16% | 2.7 | 1 (10-31 08:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 472 | 68% | 7.1 | 9 (10-31 10:12Z) |
| ap-northeast-1 | 472 | 71% | 7.0 | 9 (10-31 10:12Z) |
| ap-northeast-2 | 472 | 100% | 9.0 | 9 (10-31 10:12Z) |
| ap-south-1 | 472 | 61% | 6.2 | 9 (10-31 10:12Z) |
| ap-southeast-2 | 472 | 22% | 3.3 | 3 (10-31 10:12Z) |
| ap-southeast-3 | 472 | 25% | 3.3 | 1 (10-31 10:12Z) |
| us-east-1 | 472 | 69% | 6.4 | 9 (10-31 10:12Z) |
| us-east-2 | 472 | 67% | 6.6 | 9 (10-31 10:12Z) |
| us-west-2 | 472 | 51% | 5.6 | 9 (10-31 10:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999911111111113399999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111299999999991111111122111129999999999997999
ap-southeast-2   999999999111111111111111111111111111199999991113
ap-southeast-3   111123321111111111111111117867511111111111111111
us-east-1        956565556545466666999999999323233343393943999999
us-east-2        299122221212222249999999932222222222222289999999
us-west-2        499993344455344555933559999948443959312112332449
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 4 | 3 | 4 | 3 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 303 | 82% | 7.9 | 9 (10-31 10:12Z) |
| ap-east-1 ape1-az2 | 263 | 84% | 8.1 | 9 (10-31 09:13Z) |
| ap-east-1 ape1-az3 | 293 | 85% | 8.1 | 9 (10-31 10:12Z) |
| ap-northeast-1 apne1-az1 | 200 | 94% | 8.7 | 9 (10-31 10:12Z) |
| ap-northeast-1 apne1-az2 | 167 | 84% | 8.0 | 9 (10-31 08:16Z) |
| ap-northeast-1 apne1-az4 | 251 | 99% | 8.9 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 387 | 100% | 9.0 | 9 (10-31 09:13Z) |
| ap-northeast-2 apne2-az2 | 99 | 84% | 8.0 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az3 | 413 | 100% | 9.0 | 9 (10-31 09:13Z) |
| ap-northeast-2 apne2-az4 | 310 | 85% | 8.1 | 9 (10-31 09:13Z) |
| ap-south-1 aps1-az1 | 163 | 87% | 8.2 | 9 (10-31 09:13Z) |
| ap-south-1 aps1-az2 | 179 | 79% | 7.7 | 9 (10-31 10:12Z) |
| ap-south-1 aps1-az3 | 179 | 89% | 8.3 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az1 | 54 | 81% | 7.9 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 63 | 79% | 7.7 | 9 (10-31 06:19Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 100 | 100% | 9.0 | 9 (10-31 10:12Z) |
| us-east-1 use1-az4 | 130 | 91% | 8.4 | 9 (10-31 09:13Z) |
| us-east-1 use1-az5 | 95 | 98% | 8.8 | 9 (10-30 13:17Z) |
| us-east-1 use1-az6 | 118 | 92% | 8.4 | 9 (10-31 10:12Z) |
| us-east-2 use2-az1 | 162 | 99% | 8.9 | 9 (10-31 10:12Z) |
| us-east-2 use2-az2 | 188 | 99% | 8.9 | 9 (10-31 09:13Z) |
| us-east-2 use2-az3 | 211 | 96% | 8.7 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 119 | 89% | 8.2 | 9 (10-30 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700500 | 2026-10-31T10:12:29Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T10:12:29Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742400 | 2026-10-31T10:12:29Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.896300 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583700 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590800 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T10:12:29Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T10:12:29Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.639400 | 2026-10-31T10:12:29Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T10:12:29Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.543900 | 2026-10-31T10:12:29Z |
| ap-south-1 | ap-south-1b | Windows | 0.382700 | 2026-10-31T10:12:29Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651700 | 2026-10-31T10:12:29Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T10:12:29Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655900 | 2026-10-31T10:12:29Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.564600 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.575900 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.510500 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.505900 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558300 | 2026-10-31T10:12:29Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.557500 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547300 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T10:12:29Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.555400 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2a | Windows | 0.314200 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572400 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2b | Windows | 0.322000 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544600 | 2026-10-31T10:12:29Z |
| us-west-2 | us-west-2c | Windows | 0.313800 | 2026-10-31T10:12:29Z |
