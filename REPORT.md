# Spot placement score log

Generated 2026-10-31 14:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 476 | 48% | 5.2 | 9 (10-31 14:12Z) |
| ap-northeast-1 | 476 | 14% | 2.6 | 8 (10-31 14:12Z) |
| ap-northeast-2 | 476 | 67% | 7.0 | 9 (10-31 14:12Z) |
| ap-south-1 | 476 | 2% | 1.7 | 1 (10-31 14:12Z) |
| ap-southeast-2 | 476 | 0% | 1.0 | 1 (10-31 14:12Z) |
| ap-southeast-3 | 476 | 25% | 3.3 | 2 (10-31 14:12Z) |
| us-east-1 | 476 | 10% | 2.6 | 2 (10-31 14:12Z) |
| us-east-2 | 476 | 29% | 3.6 | 2 (10-31 14:12Z) |
| us-west-2 | 476 | 9% | 2.1 | 1 (10-31 14:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        214421212199999999999999999111111999111119999999
ap-northeast-1   111112222111111111112222871111242111442111112118
ap-northeast-2   999999999999999999999999999999999999991199999999
ap-south-1       111111111111111111111221111211111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   233211111111111111111178675111111111111111115512
us-east-1        333221111233333333233222222222111222222222222212
us-east-2        111111111111128991291111111111111111111111991112
us-west-2        111112222222221112211111111111111111111111111941
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 154 | 6% | 1.6 | 1 (10-31 06:19Z) |
| ap-east-1 ape1-az2 | 351 | 65% | 6.6 | 9 (10-31 14:12Z) |
| ap-northeast-1 apne1-az1 | 100 | 5% | 1.5 | 7 (10-31 14:12Z) |
| ap-northeast-1 apne1-az4 | 214 | 25% | 3.5 | 1 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 407 | 60% | 6.4 | 9 (10-31 14:12Z) |
| ap-northeast-2 apne2-az3 | 443 | 67% | 6.9 | 9 (10-31 14:12Z) |
| ap-northeast-2 apne2-az4 | 470 | 67% | 7.0 | 9 (10-31 14:12Z) |
| ap-south-1 aps1-az1 | 137 | 1% | 1.3 | 1 (10-31 14:12Z) |
| ap-south-1 aps1-az3 | 128 | 5% | 2.4 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az1 | 89 | 2% | 1.2 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az2 | 56 | 0% | 1.0 | 1 (10-31 04:15Z) |
| ap-southeast-3 apse3-az1 | 85 | 0% | 1.0 | 1 (10-31 09:13Z) |
| ap-southeast-3 apse3-az3 | 300 | 39% | 4.4 | 2 (10-31 14:12Z) |
| us-east-1 use1-az1 | 97 | 0% | 1.1 | 1 (10-31 13:12Z) |
| us-east-1 use1-az2 | 132 | 2% | 1.3 | 1 (10-31 13:12Z) |
| us-east-1 use1-az4 | 157 | 23% | 3.0 | 1 (10-31 14:12Z) |
| us-east-1 use1-az5 | 154 | 25% | 3.1 | 1 (10-31 12:17Z) |
| us-east-1 use1-az6 | 115 | 23% | 3.0 | 1 (10-31 11:11Z) |
| us-east-2 use2-az1 | 200 | 42% | 4.5 | 1 (10-31 14:12Z) |
| us-east-2 use2-az2 | 242 | 49% | 5.2 | 1 (10-31 11:11Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 148 | 25% | 3.3 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az2 | 116 | 18% | 2.7 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az3 | 192 | 17% | 2.7 | 1 (10-31 14:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 476 | 68% | 7.1 | 9 (10-31 14:12Z) |
| ap-northeast-1 | 476 | 72% | 7.0 | 9 (10-31 14:12Z) |
| ap-northeast-2 | 476 | 100% | 9.0 | 9 (10-31 14:12Z) |
| ap-south-1 | 476 | 62% | 6.3 | 9 (10-31 14:12Z) |
| ap-southeast-2 | 476 | 22% | 3.3 | 9 (10-31 14:12Z) |
| ap-southeast-3 | 476 | 25% | 3.3 | 2 (10-31 14:12Z) |
| us-east-1 | 476 | 70% | 6.4 | 9 (10-31 14:12Z) |
| us-east-2 | 476 | 67% | 6.6 | 9 (10-31 14:12Z) |
| us-west-2 | 476 | 51% | 5.6 | 4 (10-31 14:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999111111111133999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       112999999999911111111221111299999999999979999999
ap-southeast-2   999991111111111111111111111111111999999911131999
ap-southeast-3   233211111111111111111178675111111111111111115512
us-east-1        655565454666669999999993232333433939439999999999
us-east-2        222212122222499999999322222222222222899999999999
us-west-2        933444553445559335599999484439593121123324499954
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 305 | 82% | 7.9 | 9 (10-31 14:12Z) |
| ap-east-1 ape1-az2 | 266 | 85% | 8.1 | 9 (10-31 14:12Z) |
| ap-east-1 ape1-az3 | 294 | 85% | 8.1 | 9 (10-31 11:11Z) |
| ap-northeast-1 apne1-az1 | 201 | 95% | 8.7 | 9 (10-31 13:12Z) |
| ap-northeast-1 apne1-az2 | 170 | 84% | 8.0 | 9 (10-31 14:12Z) |
| ap-northeast-1 apne1-az4 | 252 | 99% | 8.9 | 9 (10-31 13:12Z) |
| ap-northeast-2 apne2-az1 | 390 | 100% | 9.0 | 9 (10-31 13:12Z) |
| ap-northeast-2 apne2-az2 | 100 | 84% | 8.0 | 9 (10-31 14:12Z) |
| ap-northeast-2 apne2-az3 | 414 | 100% | 9.0 | 9 (10-31 12:17Z) |
| ap-northeast-2 apne2-az4 | 312 | 85% | 8.1 | 9 (10-31 13:12Z) |
| ap-south-1 aps1-az1 | 163 | 87% | 8.2 | 9 (10-31 09:13Z) |
| ap-south-1 aps1-az2 | 180 | 79% | 7.7 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az3 | 181 | 89% | 8.3 | 9 (10-31 14:12Z) |
| ap-southeast-2 apse2-az1 | 55 | 82% | 7.9 | 9 (10-31 14:12Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 64 | 80% | 7.8 | 9 (10-31 13:12Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 26 | 50% | 5.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az2 | 102 | 100% | 9.0 | 9 (10-31 14:12Z) |
| us-east-1 use1-az4 | 131 | 91% | 8.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az5 | 97 | 98% | 8.8 | 9 (10-31 14:12Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 166 | 99% | 8.9 | 9 (10-31 14:12Z) |
| us-east-2 use2-az2 | 189 | 99% | 8.9 | 9 (10-31 14:12Z) |
| us-east-2 use2-az3 | 213 | 96% | 8.7 | 9 (10-31 13:12Z) |
| us-west-2 usw2-az1 | 90 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 120 | 89% | 8.2 | 9 (10-31 11:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700400 | 2026-10-31T14:12:34Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T14:12:34Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742400 | 2026-10-31T14:12:34Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.885800 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583700 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591000 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T14:12:34Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T14:12:34Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.639400 | 2026-10-31T14:12:34Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T14:12:34Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.537600 | 2026-10-31T14:12:34Z |
| ap-south-1 | ap-south-1b | Windows | 0.382100 | 2026-10-31T14:12:34Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651700 | 2026-10-31T14:12:34Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T14:12:34Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656000 | 2026-10-31T14:12:34Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.562000 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.575900 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.510500 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.505900 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.551200 | 2026-10-31T14:12:34Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559400 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548000 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T14:12:34Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.555400 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2a | Windows | 0.313700 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572600 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2b | Windows | 0.322000 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544600 | 2026-10-31T14:12:34Z |
| us-west-2 | us-west-2c | Windows | 0.313800 | 2026-10-31T14:12:34Z |
