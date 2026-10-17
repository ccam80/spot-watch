# Spot placement score log

Generated 2026-10-17 04:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 324 | 38% | 4.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 | 324 | 15% | 2.7 | 1 (10-17 04:14Z) |
| ap-northeast-2 | 324 | 52% | 6.1 | 9 (10-17 04:14Z) |
| ap-south-1 | 324 | 2% | 1.8 | 2 (10-17 04:14Z) |
| ap-southeast-2 | 324 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 | 324 | 22% | 3.3 | 5 (10-17 04:14Z) |
| us-east-1 | 324 | 9% | 2.5 | 3 (10-17 04:14Z) |
| us-east-2 | 324 | 27% | 3.6 | 1 (10-17 04:14Z) |
| us-west-2 | 324 | 11% | 2.3 | 1 (10-17 04:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111182292999999999999999999999999999
ap-northeast-1   115119711111191112222119221212111422114211113221
ap-northeast-2   999999999999999199999999999999999999999999999999
ap-south-1       222222211122111111222222222211111222222211122222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111138811111389119997939515112211113115182143875
us-east-1        112111122211323233319223322211333323213231222223
us-east-2        811111111111111118119999991111299111291119991111
us-west-2        121211111111111199991111111111111111112211112221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 8 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 229 | 53% | 5.8 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 152 | 25% | 3.5 | 2 (10-16 17:21Z) |
| ap-northeast-2 apne2-az1 | 283 | 49% | 5.8 | 6 (10-16 23:30Z) |
| ap-northeast-2 apne2-az3 | 296 | 52% | 6.0 | 9 (10-17 04:14Z) |
| ap-northeast-2 apne2-az4 | 321 | 52% | 6.1 | 9 (10-17 04:14Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 111 | 3% | 2.3 | 1 (10-16 17:21Z) |
| ap-southeast-2 apse2-az1 | 51 | 0% | 1.1 | 1 (10-15 18:13Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 218 | 32% | 4.2 | 5 (10-17 04:14Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 91 | 3% | 1.5 | 1 (10-17 04:14Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 101 | 24% | 3.2 | 1 (10-16 17:21Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 127 | 39% | 4.5 | 9 (10-16 07:03Z) |
| us-east-2 use2-az2 | 166 | 44% | 4.9 | 1 (10-17 04:14Z) |
| us-east-2 use2-az3 | 195 | 43% | 4.9 | 1 (10-16 17:21Z) |
| us-west-2 usw2-az1 | 116 | 27% | 3.5 | 1 (10-17 04:14Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 324 | 53% | 6.2 | 9 (10-17 04:14Z) |
| ap-northeast-1 | 324 | 73% | 7.1 | 9 (10-17 04:14Z) |
| ap-northeast-2 | 324 | 100% | 9.0 | 9 (10-17 04:14Z) |
| ap-south-1 | 324 | 61% | 6.4 | 9 (10-17 04:14Z) |
| ap-southeast-2 | 324 | 17% | 3.1 | 9 (10-17 04:14Z) |
| ap-southeast-3 | 324 | 22% | 3.3 | 5 (10-17 04:14Z) |
| us-east-1 | 324 | 70% | 6.5 | 5 (10-17 04:14Z) |
| us-east-2 | 324 | 70% | 6.9 | 3 (10-17 04:14Z) |
| us-west-2 | 324 | 51% | 5.6 | 4 (10-17 04:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399139911991199999999999999239923999219991199999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299929991999149999999999929919991229922999129999
ap-southeast-2   111119111111118919999991111111111181111111111119
ap-southeast-3   111138811111389119997939515112211113115182143875
us-east-1        533433366354645699829999994542666435555467934465
us-east-2        933212121112121199229999991191299112291119993113
us-west-2        354413233313323399999935929944249534335543344544
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 197 | 73% | 7.4 | 9 (10-16 23:30Z) |
| ap-east-1 ape1-az2 | 166 | 75% | 7.5 | 9 (10-17 04:14Z) |
| ap-east-1 ape1-az3 | 167 | 74% | 7.4 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 94 | 71% | 7.3 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az4 | 184 | 98% | 8.9 | 9 (10-16 23:30Z) |
| ap-northeast-2 apne2-az1 | 256 | 100% | 9.0 | 9 (10-17 04:14Z) |
| ap-northeast-2 apne2-az2 | 71 | 79% | 7.7 | 9 (10-17 04:14Z) |
| ap-northeast-2 apne2-az3 | 279 | 100% | 9.0 | 9 (10-17 04:14Z) |
| ap-northeast-2 apne2-az4 | 193 | 76% | 7.5 | 9 (10-17 04:14Z) |
| ap-south-1 aps1-az1 | 114 | 81% | 7.8 | 9 (10-17 04:14Z) |
| ap-south-1 aps1-az2 | 117 | 69% | 7.1 | 9 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 133 | 86% | 8.2 | 9 (10-16 23:30Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 63 | 30% | 4.7 | 4 (10-16 12:19Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 81 | 100% | 9.0 | 9 (10-16 07:03Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 84 | 95% | 8.7 | 9 (10-16 07:03Z) |
| us-east-2 use2-az1 | 107 | 98% | 8.9 | 9 (10-15 07:20Z) |
| us-east-2 use2-az2 | 154 | 99% | 8.9 | 9 (10-16 07:03Z) |
| us-east-2 use2-az3 | 144 | 94% | 8.6 | 7 (10-16 12:19Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711200 | 2026-10-17T04:14:52Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-17T04:14:52Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.760800 | 2026-10-17T04:14:52Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.943800 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587500 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582000 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-10-17T04:14:52Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741400 | 2026-10-17T04:14:52Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.554000 | 2026-10-17T04:14:52Z |
| ap-south-1 | ap-south-1a | Windows | 0.376500 | 2026-10-17T04:14:52Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.694000 | 2026-10-17T04:14:52Z |
| ap-south-1 | ap-south-1b | Windows | 0.328200 | 2026-10-17T04:14:52Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719700 | 2026-10-17T04:14:52Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522700 | 2026-10-17T04:14:52Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.580500 | 2026-10-17T04:14:52Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575600 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.434700 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.515800 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.473900 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.417700 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.463800 | 2026-10-17T04:14:52Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.546700 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2a | Windows | 0.643700 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.537800 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2b | Windows | 0.639800 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.535700 | 2026-10-17T04:14:52Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.524900 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2a | Windows | 0.314800 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499100 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2b | Windows | 0.330400 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.495800 | 2026-10-17T04:14:52Z |
| us-west-2 | us-west-2c | Windows | 0.314500 | 2026-10-17T04:14:52Z |
