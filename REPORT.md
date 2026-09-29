# Spot placement score log

Generated 2026-09-29 21:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 226 | 27% | 3.9 | 9 (09-29 21:21Z) |
| ap-northeast-1 | 226 | 8% | 2.4 | 9 (09-29 21:21Z) |
| ap-northeast-2 | 226 | 32% | 4.9 | 9 (09-29 21:21Z) |
| ap-south-1 | 226 | 3% | 1.9 | 1 (09-29 21:21Z) |
| ap-southeast-2 | 226 | 0% | 1.0 | 1 (09-29 21:21Z) |
| ap-southeast-3 | 226 | 20% | 3.4 | 1 (09-29 21:21Z) |
| us-east-1 | 226 | 6% | 2.3 | 2 (09-29 21:21Z) |
| us-east-2 | 226 | 19% | 3.0 | 6 (09-29 21:21Z) |
| us-west-2 | 226 | 10% | 2.3 | 1 (09-29 21:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        991139911149999999999999999999999999999999999999
ap-northeast-1   421111111111118989945589412212221112114818821379
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       791344111111111211111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   891111111153687867556688891111111115437887681111
us-east-1        999911999991999111111121111129111112211122111112
us-east-2        999999999999999111111111111111119999999111111916
us-west-2        999999999999991111111111111122111111111122222111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 6 | 6 | 3 | 3 | 3 | 6 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 5 | 4 | 2 | 3 | 4 | 7 | 6 | 4 | 5 | 4 | 6 | 4 | 2 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 6 | 4 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 78 | 0% | 1.5 | 2 (09-29 21:21Z) |
| ap-east-1 ape1-az2 | 158 | 39% | 5.0 | 9 (09-29 21:21Z) |
| ap-northeast-1 apne1-az1 | 31 | 0% | 1.3 | 2 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 102 | 12% | 2.8 | 8 (09-29 21:21Z) |
| ap-northeast-2 apne2-az1 | 204 | 33% | 4.9 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az3 | 208 | 35% | 5.0 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az4 | 223 | 33% | 5.0 | 9 (09-29 21:21Z) |
| ap-south-1 aps1-az1 | 66 | 2% | 1.7 | 1 (09-29 13:28Z) |
| ap-south-1 aps1-az3 | 90 | 3% | 2.7 | 1 (09-29 16:27Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 21 | 0% | 1.0 | 1 (09-29 16:27Z) |
| ap-southeast-3 apse3-az1 | 44 | 0% | 1.0 | 1 (09-29 15:24Z) |
| ap-southeast-3 apse3-az3 | 169 | 25% | 4.0 | 1 (09-29 21:21Z) |
| us-east-1 use1-az1 | 32 | 0% | 1.2 | 1 (09-29 21:21Z) |
| us-east-1 use1-az2 | 67 | 3% | 1.5 | 1 (09-29 20:25Z) |
| us-east-1 use1-az4 | 67 | 19% | 2.9 | 1 (09-29 21:21Z) |
| us-east-1 use1-az5 | 66 | 17% | 2.7 | 1 (09-29 14:24Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 86 | 28% | 3.6 | 1 (09-29 20:25Z) |
| us-east-2 use2-az2 | 113 | 32% | 4.1 | 9 (09-29 19:21Z) |
| us-east-2 use2-az3 | 132 | 30% | 4.2 | 4 (09-29 21:21Z) |
| us-west-2 usw2-az1 | 74 | 27% | 3.8 | 1 (09-29 17:20Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 102 | 18% | 3.0 | 1 (09-29 18:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 226 | 32% | 4.9 | 9 (09-29 21:21Z) |
| ap-northeast-1 | 226 | 76% | 7.3 | 9 (09-29 21:21Z) |
| ap-northeast-2 | 226 | 100% | 9.0 | 9 (09-29 21:21Z) |
| ap-south-1 | 226 | 57% | 6.2 | 9 (09-29 21:21Z) |
| ap-southeast-2 | 226 | 17% | 3.3 | 1 (09-29 21:21Z) |
| ap-southeast-3 | 226 | 20% | 3.4 | 1 (09-29 21:21Z) |
| us-east-1 | 226 | 75% | 6.9 | 5 (09-29 21:21Z) |
| us-east-2 | 226 | 74% | 7.2 | 9 (09-29 21:21Z) |
| us-west-2 | 226 | 56% | 5.9 | 2 (09-29 21:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   991111111113899999999999993335222333899999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999321122999999999999999994217111529999999
ap-southeast-2   222222222222427949999322122222222222222959229221
ap-southeast-3   891111111153687867556688891111111115437887681111
us-east-1        999999999999999221234454336989579489959445443595
us-east-2        999999999999999922333322332239999999999334333999
us-west-2        999999999999999999443433224444229922449453555322
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 6 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 7 | 6 | 8 | 7 | 5 | 4 | 3 | 5 | 4 | 2 | 6 | 4 | 7 | 7 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 5 | 2 | 3 | 3 | 4 | 6 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 5 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 5 | 6 | 5 | 6 | 6 | 9 | 7 | 7 | 5 | 8 | 7 | 9 | 8 | 6 | 8 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 53% | 6.2 | 9 (09-29 21:21Z) |
| ap-east-1 ape1-az2 | 89 | 54% | 6.2 | 9 (09-29 20:25Z) |
| ap-east-1 ape1-az3 | 88 | 50% | 6.0 | 9 (09-29 21:21Z) |
| ap-northeast-1 apne1-az1 | 107 | 93% | 8.5 | 9 (09-29 20:25Z) |
| ap-northeast-1 apne1-az2 | 44 | 41% | 5.5 | 9 (09-29 21:21Z) |
| ap-northeast-1 apne1-az4 | 137 | 99% | 8.9 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az1 | 177 | 100% | 9.0 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az2 | 51 | 73% | 7.3 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az3 | 202 | 100% | 9.0 | 9 (09-29 21:21Z) |
| ap-northeast-2 apne2-az4 | 111 | 58% | 6.5 | 9 (09-29 21:21Z) |
| ap-south-1 aps1-az1 | 66 | 67% | 7.0 | 9 (09-29 20:25Z) |
| ap-south-1 aps1-az2 | 79 | 54% | 6.3 | 9 (09-29 21:21Z) |
| ap-south-1 aps1-az3 | 92 | 80% | 7.8 | 9 (09-29 21:21Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730200 | 2026-09-29T21:21:22Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.877800 | 2026-09-29T21:21:22Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.794200 | 2026-09-29T21:21:22Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.985100 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594600 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567100 | 2026-09-29T21:21:22Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-29T21:21:22Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.592900 | 2026-09-29T21:21:22Z |
| ap-south-1 | ap-south-1a | Windows | 0.351300 | 2026-09-29T21:21:22Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.624000 | 2026-09-29T21:21:22Z |
| ap-south-1 | ap-south-1b | Windows | 0.341000 | 2026-09-29T21:21:22Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.710900 | 2026-09-29T21:21:22Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-09-29T21:21:22Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.633400 | 2026-09-29T21:21:22Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.611600 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1a | Windows | 0.306600 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.460500 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.446300 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.399400 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438300 | 2026-09-29T21:21:22Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530800 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-09-29T21:21:22Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513500 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2a | Windows | 0.332300 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.500500 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2b | Windows | 0.332200 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-29T21:21:22Z |
| us-west-2 | us-west-2c | Windows | 0.331100 | 2026-09-29T21:21:22Z |
