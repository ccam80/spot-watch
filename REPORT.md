# Spot placement score log

Generated 2026-10-31 01:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 463 | 48% | 5.2 | 9 (10-31 01:14Z) |
| ap-northeast-1 | 463 | 14% | 2.7 | 1 (10-31 01:14Z) |
| ap-northeast-2 | 463 | 66% | 7.0 | 9 (10-31 01:14Z) |
| ap-south-1 | 463 | 2% | 1.7 | 1 (10-31 01:14Z) |
| ap-southeast-2 | 463 | 0% | 1.0 | 1 (10-31 01:14Z) |
| ap-southeast-3 | 463 | 26% | 3.3 | 1 (10-31 01:14Z) |
| us-east-1 | 463 | 10% | 2.6 | 2 (10-31 01:14Z) |
| us-east-2 | 463 | 29% | 3.6 | 1 (10-31 01:14Z) |
| us-west-2 | 463 | 9% | 2.2 | 1 (10-31 01:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999997111111221442121219999999999999999911111199
ap-northeast-1   111111111222211111222211111111111222287111124211
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111122111121111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111123321111111111111111117867511111111
us-east-1        112222333332333322111123333333323322222222211122
us-east-2        111114111111111111111111112899129111111111111111
us-west-2        122222211112111111222222222111221111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 151 | 6% | 1.6 | 1 (10-31 01:14Z) |
| ap-east-1 ape1-az2 | 342 | 64% | 6.5 | 9 (10-31 01:14Z) |
| ap-northeast-1 apne1-az1 | 97 | 4% | 1.4 | 1 (10-30 23:11Z) |
| ap-northeast-1 apne1-az4 | 208 | 26% | 3.5 | 1 (10-31 00:33Z) |
| ap-northeast-2 apne2-az1 | 401 | 60% | 6.4 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az3 | 432 | 66% | 6.9 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az4 | 459 | 67% | 7.0 | 9 (10-31 01:14Z) |
| ap-south-1 aps1-az1 | 131 | 1% | 1.4 | 1 (10-30 23:11Z) |
| ap-south-1 aps1-az3 | 125 | 6% | 2.4 | 1 (10-31 00:33Z) |
| ap-southeast-2 apse2-az1 | 86 | 2% | 1.2 | 1 (10-30 22:12Z) |
| ap-southeast-2 apse2-az2 | 55 | 0% | 1.0 | 1 (10-31 00:33Z) |
| ap-southeast-3 apse3-az1 | 81 | 0% | 1.0 | 1 (10-31 01:14Z) |
| ap-southeast-3 apse3-az3 | 296 | 39% | 4.4 | 1 (10-30 23:11Z) |
| us-east-1 use1-az1 | 90 | 0% | 1.1 | 1 (10-31 01:14Z) |
| us-east-1 use1-az2 | 124 | 2% | 1.4 | 1 (10-31 01:14Z) |
| us-east-1 use1-az4 | 151 | 24% | 3.1 | 1 (10-30 23:11Z) |
| us-east-1 use1-az5 | 151 | 25% | 3.2 | 1 (10-31 00:33Z) |
| us-east-1 use1-az6 | 109 | 25% | 3.1 | 1 (10-31 01:14Z) |
| us-east-2 use2-az1 | 191 | 42% | 4.6 | 1 (10-31 01:14Z) |
| us-east-2 use2-az2 | 237 | 49% | 5.2 | 1 (10-30 20:12Z) |
| us-east-2 use2-az3 | 271 | 45% | 5.0 | 1 (10-30 22:12Z) |
| us-west-2 usw2-az1 | 146 | 25% | 3.3 | 1 (10-31 00:33Z) |
| us-west-2 usw2-az2 | 113 | 18% | 2.6 | 1 (10-30 22:12Z) |
| us-west-2 usw2-az3 | 183 | 17% | 2.7 | 1 (10-30 23:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 463 | 67% | 7.0 | 9 (10-31 01:14Z) |
| ap-northeast-1 | 463 | 71% | 6.9 | 9 (10-31 01:14Z) |
| ap-northeast-2 | 463 | 100% | 9.0 | 9 (10-31 01:14Z) |
| ap-south-1 | 463 | 60% | 6.2 | 9 (10-31 01:14Z) |
| ap-southeast-2 | 463 | 21% | 3.2 | 9 (10-31 01:14Z) |
| ap-southeast-3 | 463 | 26% | 3.3 | 1 (10-31 01:14Z) |
| us-east-1 | 463 | 69% | 6.3 | 3 (10-31 01:14Z) |
| us-east-2 | 463 | 66% | 6.6 | 2 (10-31 01:14Z) |
| us-west-2 | 463 | 51% | 5.6 | 2 (10-31 01:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111111111999999999999911111111113399999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       997111111111111299999999991111111122111129999999
ap-southeast-2   111111143999999999111111111111111111111111111199
ap-southeast-3   111111111111123321111111111111111117867511111111
us-east-1        466665779956565556545466666999999999323233343393
us-east-2        522229922299122221212222249999999932222222222222
us-west-2        355999554499993344455344555933559999948443959312
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 298 | 82% | 7.9 | 9 (10-31 01:14Z) |
| ap-east-1 ape1-az2 | 258 | 84% | 8.0 | 9 (10-31 01:14Z) |
| ap-east-1 ape1-az3 | 284 | 85% | 8.1 | 9 (10-31 00:33Z) |
| ap-northeast-1 apne1-az1 | 198 | 94% | 8.6 | 9 (10-31 00:33Z) |
| ap-northeast-1 apne1-az2 | 163 | 83% | 8.0 | 9 (10-31 00:33Z) |
| ap-northeast-1 apne1-az4 | 247 | 99% | 8.9 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az1 | 381 | 100% | 9.0 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az2 | 96 | 83% | 7.9 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az3 | 406 | 100% | 9.0 | 9 (10-31 00:33Z) |
| ap-northeast-2 apne2-az4 | 304 | 85% | 8.1 | 9 (10-31 01:14Z) |
| ap-south-1 aps1-az1 | 160 | 86% | 8.2 | 9 (10-31 01:14Z) |
| ap-south-1 aps1-az2 | 171 | 78% | 7.6 | 9 (10-31 00:33Z) |
| ap-south-1 aps1-az3 | 178 | 89% | 8.3 | 9 (10-31 01:14Z) |
| ap-southeast-2 apse2-az1 | 53 | 81% | 7.8 | 9 (10-31 01:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 60 | 78% | 7.7 | 9 (10-31 01:14Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 97 | 100% | 9.0 | 9 (10-30 10:16Z) |
| us-east-1 use1-az4 | 127 | 91% | 8.3 | 9 (10-30 11:13Z) |
| us-east-1 use1-az5 | 95 | 98% | 8.8 | 9 (10-30 13:17Z) |
| us-east-1 use1-az6 | 114 | 91% | 8.4 | 9 (10-30 11:13Z) |
| us-east-2 use2-az1 | 158 | 99% | 8.9 | 9 (10-30 11:13Z) |
| us-east-2 use2-az2 | 185 | 99% | 8.9 | 9 (10-30 08:21Z) |
| us-east-2 use2-az3 | 205 | 96% | 8.7 | 9 (10-30 11:13Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 119 | 89% | 8.2 | 9 (10-30 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700500 | 2026-10-31T01:14:51Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T01:14:51Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.744000 | 2026-10-31T01:14:51Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.908200 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584400 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590200 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T01:14:51Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T01:14:51Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.617700 | 2026-10-31T01:14:51Z |
| ap-south-1 | ap-south-1a | Windows | 0.463000 | 2026-10-31T01:14:51Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.558800 | 2026-10-31T01:14:51Z |
| ap-south-1 | ap-south-1b | Windows | 0.384300 | 2026-10-31T01:14:51Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652100 | 2026-10-31T01:14:51Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515500 | 2026-10-31T01:14:51Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656800 | 2026-10-31T01:14:51Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.571800 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.553500 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.515700 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.509500 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.560500 | 2026-10-31T01:14:51Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554800 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547800 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2b | Windows | 0.637300 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T01:14:51Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556800 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2a | Windows | 0.315200 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572900 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2b | Windows | 0.323000 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547300 | 2026-10-31T01:14:51Z |
| us-west-2 | us-west-2c | Windows | 0.315600 | 2026-10-31T01:14:51Z |
