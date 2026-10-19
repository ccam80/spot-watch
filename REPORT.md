# Spot placement score log

Generated 2026-10-19 15:31 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 339 | 40% | 4.7 | 9 (10-19 15:31Z) |
| ap-northeast-1 | 339 | 15% | 2.8 | 9 (10-19 15:31Z) |
| ap-northeast-2 | 339 | 54% | 6.2 | 9 (10-19 15:31Z) |
| ap-south-1 | 339 | 2% | 1.8 | 2 (10-19 15:31Z) |
| ap-southeast-2 | 339 | 1% | 1.1 | 1 (10-19 15:31Z) |
| ap-southeast-3 | 339 | 24% | 3.4 | 7 (10-19 15:31Z) |
| us-east-1 | 339 | 11% | 2.7 | 1 (10-19 15:31Z) |
| us-east-2 | 339 | 30% | 3.7 | 1 (10-19 15:31Z) |
| us-west-2 | 339 | 11% | 2.3 | 2 (10-19 15:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        182292999999999999999999999999999999999999999999
ap-northeast-1   112222119221212111422114211113221293241659122219
ap-northeast-2   199999999999999999999999999999999999999999999999
ap-south-1       111222222222211111222222211122222222222222222222
ap-southeast-2   111111111111111111111111111111111911911111111111
ap-southeast-3   119997939515112211113115182143875186799247488117
us-east-1        233319223322211333323213231222223332219239999991
us-east-2        118119999991111299111291119991111619999991999991
us-west-2        199991111111111111111112211112221121212191192112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 117 | 8% | 1.7 | 1 (10-19 15:31Z) |
| ap-east-1 ape1-az2 | 244 | 56% | 6.0 | 9 (10-19 15:31Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 158 | 26% | 3.6 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az1 | 294 | 50% | 5.9 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az3 | 311 | 54% | 6.2 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az4 | 336 | 54% | 6.2 | 9 (10-19 15:31Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 70 | 0% | 1.0 | 1 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 229 | 34% | 4.3 | 7 (10-19 15:31Z) |
| us-east-1 use1-az1 | 65 | 0% | 1.1 | 1 (10-19 07:40Z) |
| us-east-1 use1-az2 | 94 | 3% | 1.5 | 1 (10-19 15:31Z) |
| us-east-1 use1-az4 | 104 | 31% | 3.7 | 9 (10-19 01:08Z) |
| us-east-1 use1-az5 | 110 | 28% | 3.5 | 8 (10-19 07:40Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 136 | 43% | 4.7 | 9 (10-19 07:40Z) |
| us-east-2 use2-az2 | 177 | 47% | 5.1 | 9 (10-19 07:40Z) |
| us-east-2 use2-az3 | 208 | 45% | 5.1 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az1 | 121 | 27% | 3.6 | 1 (10-19 15:31Z) |
| us-west-2 usw2-az2 | 72 | 25% | 3.3 | 1 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 339 | 55% | 6.3 | 9 (10-19 15:31Z) |
| ap-northeast-1 | 339 | 74% | 7.2 | 9 (10-19 15:31Z) |
| ap-northeast-2 | 339 | 100% | 9.0 | 9 (10-19 15:31Z) |
| ap-south-1 | 339 | 62% | 6.4 | 9 (10-19 15:31Z) |
| ap-southeast-2 | 339 | 20% | 3.3 | 9 (10-19 15:31Z) |
| ap-southeast-3 | 339 | 24% | 3.4 | 7 (10-19 15:31Z) |
| us-east-1 | 339 | 71% | 6.6 | 4 (10-19 15:31Z) |
| us-east-2 | 339 | 71% | 6.9 | 2 (10-19 15:31Z) |
| us-west-2 | 339 | 53% | 5.8 | 5 (10-19 15:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999239923999219991199999999999999999329
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999929919991229922999129999999999999999929
ap-southeast-2   919999991111111111181111111111119999999999991119
ap-southeast-3   119997939515112211113115182143875186799247488117
us-east-1        699829999994542666435555467934465999999999999994
us-east-2        199229999991191299112291119993113999999999999992
us-west-2        399999935929944249534335543344544399999999999995
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 6 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 207 | 74% | 7.4 | 9 (10-19 07:40Z) |
| ap-east-1 ape1-az2 | 172 | 76% | 7.6 | 9 (10-19 15:31Z) |
| ap-east-1 ape1-az3 | 174 | 75% | 7.5 | 9 (10-19 15:31Z) |
| ap-northeast-1 apne1-az1 | 156 | 93% | 8.6 | 9 (10-19 15:31Z) |
| ap-northeast-1 apne1-az2 | 98 | 72% | 7.3 | 9 (10-18 18:01Z) |
| ap-northeast-1 apne1-az4 | 193 | 98% | 8.9 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az1 | 264 | 100% | 9.0 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 292 | 100% | 9.0 | 9 (10-19 15:31Z) |
| ap-northeast-2 apne2-az4 | 202 | 77% | 7.6 | 9 (10-19 15:31Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 123 | 71% | 7.2 | 9 (10-19 15:31Z) |
| ap-south-1 aps1-az3 | 139 | 86% | 8.2 | 9 (10-19 15:31Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 115 | 98% | 8.9 | 9 (10-19 07:40Z) |
| us-east-2 use2-az2 | 158 | 99% | 8.9 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 152 | 95% | 8.6 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az1 | 79 | 97% | 8.8 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az2 | 74 | 96% | 8.7 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708100 | 2026-10-19T15:31:25Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-19T15:31:25Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.766300 | 2026-10-19T15:31:25Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947200 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584600 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581200 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566700 | 2026-10-19T15:31:25Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-10-19T15:31:25Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.554800 | 2026-10-19T15:31:25Z |
| ap-south-1 | ap-south-1a | Windows | 0.388200 | 2026-10-19T15:31:25Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.738800 | 2026-10-19T15:31:25Z |
| ap-south-1 | ap-south-1b | Windows | 0.359300 | 2026-10-19T15:31:25Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.701000 | 2026-10-19T15:31:25Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508900 | 2026-10-19T15:31:25Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.662800 | 2026-10-19T15:31:25Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558800 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.444600 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.531200 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.520500 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.447000 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.499700 | 2026-10-19T15:31:25Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550500 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2a | Windows | 0.643400 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.543900 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2b | Windows | 0.639400 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.542000 | 2026-10-19T15:31:25Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.530800 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2a | Windows | 0.315700 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.517100 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2b | Windows | 0.327300 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.504600 | 2026-10-19T15:31:25Z |
| us-west-2 | us-west-2c | Windows | 0.315200 | 2026-10-19T15:31:25Z |
