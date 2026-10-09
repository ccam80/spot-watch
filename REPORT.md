# Spot placement score log

Generated 2026-10-09 21:36 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 291 | 32% | 4.1 | 1 (10-09 21:36Z) |
| ap-northeast-1 | 291 | 16% | 2.8 | 1 (10-09 21:36Z) |
| ap-northeast-2 | 291 | 47% | 5.8 | 9 (10-09 21:36Z) |
| ap-south-1 | 291 | 2% | 1.8 | 1 (10-09 21:36Z) |
| ap-southeast-2 | 291 | 0% | 1.0 | 1 (10-09 21:36Z) |
| ap-southeast-3 | 291 | 20% | 3.2 | 9 (10-09 21:36Z) |
| us-east-1 | 291 | 10% | 2.5 | 3 (10-09 21:36Z) |
| us-east-2 | 291 | 26% | 3.5 | 1 (10-09 21:36Z) |
| us-west-2 | 291 | 11% | 2.4 | 1 (10-09 21:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999911111199399119119999812111111111111111111111
ap-northeast-1   991279981212982199999999999911911115119711111191
ap-northeast-2   999999999999999999999999999991499999999999999999
ap-south-1       111111111111112111111111112222222222222211122111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   765161111119991141111111111111111111138811111389
us-east-1        222322222119229222331199199999211112111122211323
us-east-2        118171218999999991199999999999111811111111111111
us-west-2        222222121112221212999999991991121121211111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 95 | 0% | 1.4 | 1 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 200 | 46% | 5.4 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 49 | 8% | 1.8 | 1 (10-09 21:36Z) |
| ap-northeast-1 apne1-az4 | 140 | 26% | 3.7 | 9 (10-09 16:07Z) |
| ap-northeast-2 apne2-az1 | 253 | 43% | 5.5 | 9 (10-09 21:36Z) |
| ap-northeast-2 apne2-az3 | 265 | 48% | 5.8 | 8 (10-09 21:36Z) |
| ap-northeast-2 apne2-az4 | 288 | 47% | 5.8 | 8 (10-09 21:36Z) |
| ap-south-1 aps1-az1 | 75 | 1% | 1.6 | 1 (10-09 08:55Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 46 | 0% | 1.1 | 1 (10-09 21:36Z) |
| ap-southeast-2 apse2-az2 | 29 | 0% | 1.0 | 1 (10-09 08:55Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 198 | 28% | 4.1 | 9 (10-09 21:36Z) |
| us-east-1 use1-az1 | 50 | 0% | 1.1 | 1 (10-09 21:36Z) |
| us-east-1 use1-az2 | 79 | 4% | 1.6 | 1 (10-09 02:03Z) |
| us-east-1 use1-az4 | 91 | 27% | 3.5 | 1 (10-09 21:36Z) |
| us-east-1 use1-az5 | 92 | 25% | 3.3 | 1 (10-08 16:24Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 116 | 37% | 4.3 | 1 (10-09 21:36Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 175 | 41% | 4.8 | 1 (10-09 08:55Z) |
| us-west-2 usw2-az1 | 99 | 28% | 3.7 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az2 | 61 | 23% | 3.2 | 1 (10-09 21:36Z) |
| us-west-2 usw2-az3 | 121 | 21% | 3.2 | 1 (10-09 02:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 291 | 47% | 5.8 | 9 (10-09 21:36Z) |
| ap-northeast-1 | 291 | 73% | 7.1 | 9 (10-09 21:36Z) |
| ap-northeast-2 | 291 | 100% | 9.0 | 9 (10-09 21:36Z) |
| ap-south-1 | 291 | 59% | 6.3 | 9 (10-09 21:36Z) |
| ap-southeast-2 | 291 | 16% | 3.1 | 8 (10-09 21:36Z) |
| ap-southeast-3 | 291 | 20% | 3.2 | 9 (10-09 21:36Z) |
| us-east-1 | 291 | 70% | 6.6 | 5 (10-09 21:36Z) |
| us-east-2 | 291 | 73% | 7.1 | 1 (10-09 21:36Z) |
| us-west-2 | 291 | 52% | 5.7 | 3 (10-09 21:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999224992299999999999991992399139911991199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111992999992999999999999999992299299929991999149
ap-southeast-2   222222222222222222222229299922911111119111111118
ap-southeast-3   765161111119991141111111111111111111138811111389
us-east-1        334433344559449855763499999999554533433366354645
us-east-2        929983599999999993999999999999239933212121112121
us-west-2        444445444339344995999999999999432354413233313323
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 5 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 174 | 69% | 7.1 | 9 (10-09 21:36Z) |
| ap-east-1 ape1-az2 | 143 | 71% | 7.3 | 9 (10-09 16:07Z) |
| ap-east-1 ape1-az3 | 140 | 69% | 7.1 | 9 (10-09 21:36Z) |
| ap-northeast-1 apne1-az1 | 138 | 92% | 8.5 | 9 (10-09 21:36Z) |
| ap-northeast-1 apne1-az2 | 73 | 64% | 6.9 | 9 (10-09 21:36Z) |
| ap-northeast-1 apne1-az4 | 166 | 99% | 8.9 | 9 (10-09 21:36Z) |
| ap-northeast-2 apne2-az1 | 227 | 100% | 9.0 | 9 (10-09 21:36Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 250 | 100% | 9.0 | 9 (10-09 16:07Z) |
| ap-northeast-2 apne2-az4 | 165 | 72% | 7.3 | 9 (10-09 21:36Z) |
| ap-south-1 aps1-az1 | 98 | 78% | 7.7 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az2 | 105 | 66% | 6.9 | 9 (10-09 21:36Z) |
| ap-south-1 aps1-az3 | 116 | 84% | 8.1 | 9 (10-09 21:36Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 58 | 26% | 4.5 | 9 (10-09 21:36Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 98 | 95% | 8.6 | 2 (10-09 08:55Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 80 | 95% | 8.7 | 2 (10-09 08:55Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707400 | 2026-10-09T21:36:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-09T21:36:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.761100 | 2026-10-09T21:36:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.944100 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.600200 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581700 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574500 | 2026-10-09T21:36:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-10-09T21:36:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.611700 | 2026-10-09T21:36:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.374500 | 2026-10-09T21:36:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.680100 | 2026-10-09T21:36:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.352700 | 2026-10-09T21:36:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.716500 | 2026-10-09T21:36:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-10-09T21:36:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.435800 | 2026-10-09T21:36:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574100 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.558600 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.484500 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.475200 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.402000 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.480700 | 2026-10-09T21:36:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534800 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529400 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517400 | 2026-10-09T21:36:49Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.527300 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2a | Windows | 0.321700 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.490200 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2b | Windows | 0.324200 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.493700 | 2026-10-09T21:36:49Z |
| us-west-2 | us-west-2c | Windows | 0.322000 | 2026-10-09T21:36:49Z |
