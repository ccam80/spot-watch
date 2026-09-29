# Spot placement score log

Generated 2026-09-29 19:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 224 | 27% | 3.8 | 9 (09-29 19:21Z) |
| ap-northeast-1 | 224 | 8% | 2.3 | 3 (09-29 19:21Z) |
| ap-northeast-2 | 224 | 32% | 4.9 | 9 (09-29 19:21Z) |
| ap-south-1 | 224 | 3% | 1.9 | 1 (09-29 19:21Z) |
| ap-southeast-2 | 224 | 0% | 1.0 | 1 (09-29 19:21Z) |
| ap-southeast-3 | 224 | 21% | 3.4 | 1 (09-29 19:21Z) |
| us-east-1 | 224 | 6% | 2.3 | 1 (09-29 19:21Z) |
| us-east-2 | 224 | 18% | 3.0 | 9 (09-29 19:21Z) |
| us-west-2 | 224 | 10% | 2.3 | 1 (09-29 19:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        889911399111499999999999999999999999999999999999
ap-northeast-1   444211111111111189899455894122122211121148188213
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       927913441111111112111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   998911111111536878675566888911111111154378876811
us-east-1        229999119999919991111111211111291111122111221111
us-east-2        999999999999999991111111111111111199999991111119
us-west-2        999999999999999911111111111111221111111111222221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 6 | 6 | 3 | 3 | 3 | 6 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 5 | 4 | 2 | 3 | 4 | 7 | 6 | 4 | 5 | 4 | 6 | 4 | 2 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 6 | 4 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 76 | 0% | 1.5 | 1 (09-29 19:21Z) |
| ap-east-1 ape1-az2 | 156 | 38% | 5.0 | 9 (09-29 19:21Z) |
| ap-northeast-1 apne1-az1 | 31 | 0% | 1.3 | 2 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 100 | 10% | 2.7 | 1 (09-29 19:21Z) |
| ap-northeast-2 apne2-az1 | 202 | 32% | 4.9 | 9 (09-29 19:21Z) |
| ap-northeast-2 apne2-az3 | 206 | 34% | 5.0 | 9 (09-29 19:21Z) |
| ap-northeast-2 apne2-az4 | 221 | 32% | 4.9 | 9 (09-29 19:21Z) |
| ap-south-1 aps1-az1 | 66 | 2% | 1.7 | 1 (09-29 13:28Z) |
| ap-south-1 aps1-az3 | 90 | 3% | 2.7 | 1 (09-29 16:27Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 21 | 0% | 1.0 | 1 (09-29 16:27Z) |
| ap-southeast-3 apse3-az1 | 44 | 0% | 1.0 | 1 (09-29 15:24Z) |
| ap-southeast-3 apse3-az3 | 167 | 26% | 4.1 | 1 (09-29 18:29Z) |
| us-east-1 use1-az1 | 31 | 0% | 1.2 | 1 (09-29 18:29Z) |
| us-east-1 use1-az2 | 66 | 3% | 1.5 | 1 (09-29 19:21Z) |
| us-east-1 use1-az4 | 65 | 20% | 3.0 | 1 (09-29 18:29Z) |
| us-east-1 use1-az5 | 66 | 17% | 2.7 | 1 (09-29 14:24Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 85 | 28% | 3.7 | 9 (09-29 19:21Z) |
| us-east-2 use2-az2 | 113 | 32% | 4.1 | 9 (09-29 19:21Z) |
| us-east-2 use2-az3 | 131 | 30% | 4.2 | 9 (09-29 19:21Z) |
| us-west-2 usw2-az1 | 74 | 27% | 3.8 | 1 (09-29 17:20Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 102 | 18% | 3.0 | 1 (09-29 18:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 224 | 32% | 4.9 | 9 (09-29 19:21Z) |
| ap-northeast-1 | 224 | 76% | 7.3 | 9 (09-29 19:21Z) |
| ap-northeast-2 | 224 | 100% | 9.0 | 9 (09-29 19:21Z) |
| ap-south-1 | 224 | 57% | 6.2 | 9 (09-29 19:21Z) |
| ap-southeast-2 | 224 | 17% | 3.3 | 2 (09-29 19:21Z) |
| ap-southeast-3 | 224 | 21% | 3.4 | 1 (09-29 19:21Z) |
| us-east-1 | 224 | 75% | 6.9 | 5 (09-29 19:21Z) |
| us-east-2 | 224 | 74% | 7.2 | 9 (09-29 19:21Z) |
| us-west-2 | 224 | 57% | 6.0 | 3 (09-29 19:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999911111111138999999999999933352223338999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999993211229999999999999999942171115299999
ap-southeast-2   992222222222224279499993221222222222222229592292
ap-southeast-3   998911111111536878675566888911111111154378876811
us-east-1        999999999999999992212344543369895794899594454435
us-east-2        999999999999999999223333223322399999999993343339
us-west-2        999999999999999999994434332244442299224494535553
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 6 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 7 | 6 | 8 | 7 | 5 | 4 | 3 | 5 | 4 | 2 | 6 | 4 | 7 | 7 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 5 | 2 | 3 | 3 | 4 | 6 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 5 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 5 | 6 | 5 | 6 | 6 | 9 | 7 | 7 | 5 | 8 | 7 | 9 | 8 | 6 | 8 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 114 | 53% | 6.2 | 9 (09-29 19:21Z) |
| ap-east-1 ape1-az2 | 88 | 53% | 6.2 | 9 (09-29 18:29Z) |
| ap-east-1 ape1-az3 | 86 | 49% | 5.9 | 9 (09-29 19:21Z) |
| ap-northeast-1 apne1-az1 | 106 | 92% | 8.5 | 9 (09-29 18:29Z) |
| ap-northeast-1 apne1-az2 | 43 | 40% | 5.4 | 9 (09-29 16:27Z) |
| ap-northeast-1 apne1-az4 | 135 | 99% | 8.9 | 9 (09-29 19:21Z) |
| ap-northeast-2 apne2-az1 | 176 | 100% | 9.0 | 9 (09-29 18:29Z) |
| ap-northeast-2 apne2-az2 | 50 | 72% | 7.2 | 9 (09-29 19:21Z) |
| ap-northeast-2 apne2-az3 | 200 | 100% | 9.0 | 9 (09-29 19:21Z) |
| ap-northeast-2 apne2-az4 | 109 | 57% | 6.4 | 9 (09-29 19:21Z) |
| ap-south-1 aps1-az1 | 65 | 66% | 7.0 | 9 (09-29 18:29Z) |
| ap-south-1 aps1-az2 | 77 | 53% | 6.2 | 9 (09-29 19:21Z) |
| ap-south-1 aps1-az3 | 90 | 80% | 7.8 | 9 (09-29 17:20Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 51 | 22% | 4.2 | 8 (09-29 14:24Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 86 | 98% | 8.8 | 9 (09-29 10:24Z) |
| us-east-1 use1-az5 | 47 | 98% | 8.9 | 9 (09-29 03:28Z) |
| us-east-1 use1-az6 | 76 | 96% | 8.7 | 2 (09-29 08:32Z) |
| us-east-2 use2-az1 | 84 | 99% | 8.9 | 9 (09-29 19:21Z) |
| us-east-2 use2-az2 | 117 | 98% | 8.9 | 9 (09-29 19:21Z) |
| us-east-2 use2-az3 | 109 | 93% | 8.5 | 9 (09-29 19:21Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 72 | 99% | 8.9 | 9 (09-29 12:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730200 | 2026-09-29T19:21:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.877800 | 2026-09-29T19:21:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.794200 | 2026-09-29T19:21:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.985100 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594600 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577600 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567100 | 2026-09-29T19:21:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-29T19:21:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.590200 | 2026-09-29T19:21:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.351300 | 2026-09-29T19:21:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.624000 | 2026-09-29T19:21:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.341000 | 2026-09-29T19:21:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.710900 | 2026-09-29T19:21:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-09-29T19:21:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.633400 | 2026-09-29T19:21:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.611600 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1a | Windows | 0.306600 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.462900 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.446300 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395700 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438300 | 2026-09-29T19:21:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530800 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-09-29T19:21:00Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.515700 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2a | Windows | 0.332300 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498300 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2b | Windows | 0.332200 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-29T19:21:00Z |
| us-west-2 | us-west-2c | Windows | 0.331100 | 2026-09-29T19:21:00Z |
