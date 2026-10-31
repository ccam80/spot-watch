# Spot placement score log

Generated 2026-10-31 12:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 474 | 48% | 5.2 | 9 (10-31 12:17Z) |
| ap-northeast-1 | 474 | 14% | 2.6 | 1 (10-31 12:17Z) |
| ap-northeast-2 | 474 | 67% | 7.0 | 9 (10-31 12:17Z) |
| ap-south-1 | 474 | 2% | 1.7 | 1 (10-31 12:17Z) |
| ap-southeast-2 | 474 | 0% | 1.0 | 1 (10-31 12:17Z) |
| ap-southeast-3 | 474 | 26% | 3.3 | 5 (10-31 12:17Z) |
| us-east-1 | 474 | 10% | 2.6 | 2 (10-31 12:17Z) |
| us-east-2 | 474 | 29% | 3.6 | 1 (10-31 12:17Z) |
| us-west-2 | 474 | 9% | 2.1 | 9 (10-31 12:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        122144212121999999999999999991111119991111199999
ap-northeast-1   221111122221111111111122228711112421114421111121
ap-northeast-2   999999999999999999999999999999999999999911999999
ap-south-1       111111111111111111111112211112111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   112332111111111111111111786751111111111111111155
us-east-1        233332211112333333332332222222221112222222222222
us-east-2        111111111111111289912911111111111111111111119911
us-west-2        211111122222222211122111111111111111111111111119
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
| ap-east-1 ape1-az2 | 349 | 65% | 6.6 | 9 (10-31 12:17Z) |
| ap-northeast-1 apne1-az1 | 99 | 4% | 1.4 | 2 (10-31 11:11Z) |
| ap-northeast-1 apne1-az4 | 214 | 25% | 3.5 | 1 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 406 | 60% | 6.4 | 9 (10-31 09:13Z) |
| ap-northeast-2 apne2-az3 | 441 | 67% | 6.9 | 9 (10-31 12:17Z) |
| ap-northeast-2 apne2-az4 | 468 | 67% | 7.0 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az1 | 135 | 1% | 1.3 | 1 (10-31 11:11Z) |
| ap-south-1 aps1-az3 | 128 | 5% | 2.4 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az1 | 89 | 2% | 1.2 | 1 (10-31 12:17Z) |
| ap-southeast-2 apse2-az2 | 56 | 0% | 1.0 | 1 (10-31 04:15Z) |
| ap-southeast-3 apse3-az1 | 85 | 0% | 1.0 | 1 (10-31 09:13Z) |
| ap-southeast-3 apse3-az3 | 298 | 39% | 4.4 | 5 (10-31 12:17Z) |
| us-east-1 use1-az1 | 96 | 0% | 1.1 | 1 (10-31 09:13Z) |
| us-east-1 use1-az2 | 131 | 2% | 1.4 | 1 (10-31 11:11Z) |
| us-east-1 use1-az4 | 155 | 23% | 3.0 | 1 (10-31 08:16Z) |
| us-east-1 use1-az5 | 154 | 25% | 3.1 | 1 (10-31 12:17Z) |
| us-east-1 use1-az6 | 115 | 23% | 3.0 | 1 (10-31 11:11Z) |
| us-east-2 use2-az1 | 198 | 42% | 4.6 | 9 (10-31 10:12Z) |
| us-east-2 use2-az2 | 242 | 49% | 5.2 | 1 (10-31 11:11Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 148 | 25% | 3.3 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az2 | 116 | 18% | 2.7 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az3 | 190 | 17% | 2.7 | 9 (10-31 12:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 474 | 68% | 7.1 | 9 (10-31 12:17Z) |
| ap-northeast-1 | 474 | 72% | 7.0 | 9 (10-31 12:17Z) |
| ap-northeast-2 | 474 | 100% | 9.0 | 9 (10-31 12:17Z) |
| ap-south-1 | 474 | 61% | 6.3 | 9 (10-31 12:17Z) |
| ap-southeast-2 | 474 | 22% | 3.3 | 9 (10-31 12:17Z) |
| ap-southeast-3 | 474 | 26% | 3.3 | 5 (10-31 12:17Z) |
| us-east-1 | 474 | 70% | 6.4 | 9 (10-31 12:17Z) |
| us-east-2 | 474 | 67% | 6.6 | 9 (10-31 12:17Z) |
| us-west-2 | 474 | 51% | 5.6 | 9 (10-31 12:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999991111111111339999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111129999999999111111112211112999999999999799999
ap-southeast-2   999999911111111111111111111111111119999999111319
ap-southeast-3   112332111111111111111111786751111111111111111155
us-east-1        656555654546666699999999932323334339394399999999
us-east-2        912222121222224999999993222222222222228999999999
us-west-2        999334445534455593355999994844395931211233244999
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
| ap-east-1 ape1-az1 | 303 | 82% | 7.9 | 9 (10-31 10:12Z) |
| ap-east-1 ape1-az2 | 265 | 85% | 8.1 | 9 (10-31 12:17Z) |
| ap-east-1 ape1-az3 | 294 | 85% | 8.1 | 9 (10-31 11:11Z) |
| ap-northeast-1 apne1-az1 | 200 | 94% | 8.7 | 9 (10-31 10:12Z) |
| ap-northeast-1 apne1-az2 | 169 | 84% | 8.0 | 9 (10-31 12:17Z) |
| ap-northeast-1 apne1-az4 | 251 | 99% | 8.9 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az1 | 389 | 100% | 9.0 | 9 (10-31 12:17Z) |
| ap-northeast-2 apne2-az2 | 99 | 84% | 8.0 | 9 (10-31 10:12Z) |
| ap-northeast-2 apne2-az3 | 414 | 100% | 9.0 | 9 (10-31 12:17Z) |
| ap-northeast-2 apne2-az4 | 311 | 85% | 8.1 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az1 | 163 | 87% | 8.2 | 9 (10-31 09:13Z) |
| ap-south-1 aps1-az2 | 180 | 79% | 7.7 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az3 | 180 | 89% | 8.3 | 9 (10-31 11:11Z) |
| ap-southeast-2 apse2-az1 | 54 | 81% | 7.9 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 63 | 79% | 7.7 | 9 (10-31 06:19Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 101 | 100% | 9.0 | 9 (10-31 12:17Z) |
| us-east-1 use1-az4 | 130 | 91% | 8.4 | 9 (10-31 09:13Z) |
| us-east-1 use1-az5 | 96 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 164 | 99% | 8.9 | 9 (10-31 12:17Z) |
| us-east-2 use2-az2 | 188 | 99% | 8.9 | 9 (10-31 09:13Z) |
| us-east-2 use2-az3 | 212 | 96% | 8.7 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az1 | 90 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 120 | 89% | 8.2 | 9 (10-31 11:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700500 | 2026-10-31T12:17:52Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T12:17:52Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742400 | 2026-10-31T12:17:52Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.896300 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583700 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591000 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T12:17:52Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T12:17:52Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.639400 | 2026-10-31T12:17:52Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T12:17:52Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.537600 | 2026-10-31T12:17:52Z |
| ap-south-1 | ap-south-1b | Windows | 0.382700 | 2026-10-31T12:17:52Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651700 | 2026-10-31T12:17:52Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T12:17:52Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656000 | 2026-10-31T12:17:52Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.562000 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.575900 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.510500 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.505900 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558300 | 2026-10-31T12:17:52Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.557500 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547300 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T12:17:52Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.555400 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2a | Windows | 0.314200 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572600 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2b | Windows | 0.322000 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544600 | 2026-10-31T12:17:52Z |
| us-west-2 | us-west-2c | Windows | 0.313800 | 2026-10-31T12:17:52Z |
