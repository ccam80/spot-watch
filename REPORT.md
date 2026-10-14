# Spot placement score log

Generated 2026-10-14 22:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 312 | 35% | 4.3 | 9 (10-14 22:14Z) |
| ap-northeast-1 | 312 | 15% | 2.8 | 2 (10-14 22:14Z) |
| ap-northeast-2 | 312 | 50% | 6.0 | 9 (10-14 22:14Z) |
| ap-south-1 | 312 | 2% | 1.8 | 2 (10-14 22:14Z) |
| ap-southeast-2 | 312 | 0% | 1.0 | 1 (10-14 22:14Z) |
| ap-southeast-3 | 312 | 21% | 3.3 | 3 (10-14 22:14Z) |
| us-east-1 | 312 | 9% | 2.6 | 3 (10-14 22:14Z) |
| us-east-2 | 312 | 27% | 3.6 | 1 (10-14 22:14Z) |
| us-west-2 | 312 | 12% | 2.4 | 1 (10-14 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999812111111111111111111111182292999999999999999
ap-northeast-1   999999911911115119711111191112222119221212111422
ap-northeast-2   999999991499999999999999999199999999999999999999
ap-south-1       111112222222222222211122111111222222222211111222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111111138811111389119997939515112211113
us-east-1        199199999211112111122211323233319223322211333323
us-east-2        999999999111811111111111111118119999991111299111
us-west-2        999991991121121211111111111199991111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 5 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 108 | 8% | 1.8 | 1 (10-14 18:31Z) |
| ap-east-1 ape1-az2 | 217 | 50% | 5.6 | 9 (10-14 22:14Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 147 | 26% | 3.6 | 1 (10-14 01:49Z) |
| ap-northeast-2 apne2-az1 | 272 | 47% | 5.7 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az3 | 284 | 51% | 6.0 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az4 | 309 | 50% | 6.0 | 9 (10-14 22:14Z) |
| ap-south-1 aps1-az1 | 83 | 1% | 1.6 | 1 (10-14 18:31Z) |
| ap-south-1 aps1-az3 | 109 | 3% | 2.4 | 1 (10-14 22:14Z) |
| ap-southeast-2 apse2-az1 | 49 | 0% | 1.1 | 1 (10-14 13:38Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 59 | 0% | 1.0 | 1 (10-14 18:31Z) |
| ap-southeast-3 apse3-az3 | 210 | 30% | 4.2 | 3 (10-14 22:14Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 83 | 4% | 1.5 | 1 (10-14 22:14Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 97 | 25% | 3.2 | 1 (10-14 01:49Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 126 | 39% | 4.4 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 158 | 44% | 4.9 | 1 (10-14 22:14Z) |
| us-east-2 use2-az3 | 188 | 43% | 4.9 | 1 (10-14 22:14Z) |
| us-west-2 usw2-az1 | 107 | 29% | 3.7 | 1 (10-14 22:14Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 312 | 51% | 6.1 | 9 (10-14 22:14Z) |
| ap-northeast-1 | 312 | 73% | 7.2 | 9 (10-14 22:14Z) |
| ap-northeast-2 | 312 | 100% | 9.0 | 9 (10-14 22:14Z) |
| ap-south-1 | 312 | 61% | 6.3 | 9 (10-14 22:14Z) |
| ap-southeast-2 | 312 | 17% | 3.2 | 1 (10-14 22:14Z) |
| ap-southeast-3 | 312 | 21% | 3.3 | 3 (10-14 22:14Z) |
| us-east-1 | 312 | 71% | 6.5 | 5 (10-14 22:14Z) |
| us-east-2 | 312 | 71% | 7.0 | 2 (10-14 22:14Z) |
| us-west-2 | 312 | 52% | 5.7 | 4 (10-14 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999991992399139911991199999999999999239923999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999992299299929991999149999999999929919991229
ap-southeast-2   229299922911111119111111118919999991111111111181
ap-southeast-3   111111111111111138811111389119997939515112211113
us-east-1        499999999554533433366354645699829999994542666435
us-east-2        999999999239933212121112121199229999991191299112
us-west-2        999999999432354413233313323399999935929944249534
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 187 | 71% | 7.3 | 9 (10-14 22:14Z) |
| ap-east-1 ape1-az2 | 156 | 74% | 7.4 | 9 (10-14 18:31Z) |
| ap-east-1 ape1-az3 | 157 | 72% | 7.3 | 9 (10-14 22:14Z) |
| ap-northeast-1 apne1-az1 | 148 | 93% | 8.5 | 9 (10-14 22:14Z) |
| ap-northeast-1 apne1-az2 | 86 | 70% | 7.2 | 9 (10-14 22:14Z) |
| ap-northeast-1 apne1-az4 | 178 | 98% | 8.9 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az1 | 246 | 100% | 9.0 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az2 | 68 | 78% | 7.6 | 9 (10-14 18:31Z) |
| ap-northeast-2 apne2-az3 | 267 | 100% | 9.0 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az4 | 181 | 74% | 7.4 | 9 (10-14 22:14Z) |
| ap-south-1 aps1-az1 | 109 | 80% | 7.8 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az2 | 110 | 67% | 7.0 | 9 (10-14 22:14Z) |
| ap-south-1 aps1-az3 | 127 | 86% | 8.2 | 9 (10-14 22:14Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 20 | 60% | 6.0 | 2 (10-14 07:30Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 106 | 98% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 151 | 99% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az3 | 140 | 94% | 8.6 | 9 (10-14 07:30Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.715900 | 2026-10-14T22:14:30Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-14T22:14:30Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.756800 | 2026-10-14T22:14:30Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938700 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590800 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586400 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-10-14T22:14:30Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741700 | 2026-10-14T22:14:30Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.552200 | 2026-10-14T22:14:30Z |
| ap-south-1 | ap-south-1a | Windows | 0.381500 | 2026-10-14T22:14:30Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.703400 | 2026-10-14T22:14:30Z |
| ap-south-1 | ap-south-1b | Windows | 0.332900 | 2026-10-14T22:14:30Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.724900 | 2026-10-14T22:14:30Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.526000 | 2026-10-14T22:14:30Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.512900 | 2026-10-14T22:14:30Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.616800 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.474100 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.504500 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.469100 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.420000 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.467900 | 2026-10-14T22:14:30Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542100 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.532400 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2b | Windows | 0.640600 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.525200 | 2026-10-14T22:14:30Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.533700 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2a | Windows | 0.316500 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496600 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2b | Windows | 0.332000 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.498000 | 2026-10-14T22:14:30Z |
| us-west-2 | us-west-2c | Windows | 0.316000 | 2026-10-14T22:14:30Z |
