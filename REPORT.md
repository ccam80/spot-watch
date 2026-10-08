# Spot placement score log

Generated 2026-10-08 08:51 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 285 | 33% | 4.2 | 1 (10-08 08:51Z) |
| ap-northeast-1 | 285 | 16% | 2.8 | 1 (10-08 08:51Z) |
| ap-northeast-2 | 285 | 46% | 5.7 | 9 (10-08 08:51Z) |
| ap-south-1 | 285 | 2% | 1.8 | 1 (10-08 08:51Z) |
| ap-southeast-2 | 285 | 0% | 1.0 | 1 (10-08 08:51Z) |
| ap-southeast-3 | 285 | 20% | 3.2 | 1 (10-08 08:51Z) |
| us-east-1 | 285 | 10% | 2.6 | 2 (10-08 08:51Z) |
| us-east-2 | 285 | 27% | 3.5 | 1 (10-08 08:51Z) |
| us-west-2 | 285 | 11% | 2.4 | 1 (10-08 08:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999989999911111199399119119999812111111111111111
ap-northeast-1   211118991279981212982199999999999911911115119711
ap-northeast-2   999999999999999999999999999999999991499999999999
ap-south-1       111111111111111111112111111111112222222222222211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111114765161111119991141111111111111111111138811
us-east-1        222222222322222119229222331199199999211112111122
us-east-2        999111118171218999999991199999999999111811111111
us-west-2        122222222222121112221212999999991991121121211111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 6 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 6 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 95 | 0% | 1.4 | 1 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 198 | 46% | 5.4 | 1 (10-08 01:50Z) |
| ap-northeast-1 apne1-az1 | 46 | 9% | 1.8 | 1 (10-08 01:50Z) |
| ap-northeast-1 apne1-az4 | 139 | 26% | 3.6 | 1 (10-08 08:51Z) |
| ap-northeast-2 apne2-az1 | 247 | 42% | 5.4 | 9 (10-08 08:51Z) |
| ap-northeast-2 apne2-az3 | 259 | 47% | 5.7 | 9 (10-08 01:50Z) |
| ap-northeast-2 apne2-az4 | 282 | 46% | 5.8 | 9 (10-08 08:51Z) |
| ap-south-1 aps1-az1 | 73 | 1% | 1.6 | 1 (10-06 10:07Z) |
| ap-south-1 aps1-az3 | 107 | 3% | 2.4 | 1 (10-08 08:51Z) |
| ap-southeast-2 apse2-az1 | 42 | 0% | 1.1 | 1 (10-08 01:50Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 56 | 0% | 1.0 | 1 (10-08 08:51Z) |
| ap-southeast-3 apse3-az3 | 194 | 28% | 4.1 | 1 (10-08 01:50Z) |
| us-east-1 use1-az1 | 44 | 0% | 1.1 | 1 (10-08 01:50Z) |
| us-east-1 use1-az2 | 78 | 4% | 1.6 | 1 (10-07 21:56Z) |
| us-east-1 use1-az4 | 88 | 28% | 3.5 | 1 (10-08 01:50Z) |
| us-east-1 use1-az5 | 91 | 25% | 3.3 | 1 (10-07 21:56Z) |
| us-east-1 use1-az6 | 72 | 21% | 2.9 | 1 (10-08 08:51Z) |
| us-east-2 use2-az1 | 113 | 38% | 4.4 | 2 (10-06 10:07Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 173 | 41% | 4.8 | 1 (10-07 21:56Z) |
| us-west-2 usw2-az1 | 98 | 29% | 3.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 57 | 25% | 3.4 | 1 (10-08 01:50Z) |
| us-west-2 usw2-az3 | 120 | 21% | 3.2 | 1 (10-08 08:51Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 285 | 46% | 5.8 | 9 (10-08 08:51Z) |
| ap-northeast-1 | 285 | 73% | 7.1 | 1 (10-08 08:51Z) |
| ap-northeast-2 | 285 | 100% | 9.0 | 9 (10-08 08:51Z) |
| ap-south-1 | 285 | 59% | 6.3 | 1 (10-08 08:51Z) |
| ap-southeast-2 | 285 | 16% | 3.1 | 1 (10-08 08:51Z) |
| ap-southeast-3 | 285 | 20% | 3.2 | 1 (10-08 08:51Z) |
| us-east-1 | 285 | 71% | 6.6 | 6 (10-08 08:51Z) |
| us-east-2 | 285 | 74% | 7.2 | 1 (10-08 08:51Z) |
| us-west-2 | 285 | 53% | 5.8 | 3 (10-08 08:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   437999999999999224992299999999999991992399139911
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111992999992999999999999999992299299929991
ap-southeast-2   222222222222222222222222222229299922911111119111
ap-southeast-3   111114765161111119991141111111111111111111138811
us-east-1        554443334433344559449855763499999999554533433366
us-east-2        999832929983599999999993999999999999239933212121
us-west-2        455455444445444339344995999999999999432354413233
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 5 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 168 | 68% | 7.1 | 9 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 138 | 70% | 7.2 | 9 (10-08 08:51Z) |
| ap-east-1 ape1-az3 | 134 | 67% | 7.0 | 9 (10-08 08:51Z) |
| ap-northeast-1 apne1-az1 | 134 | 92% | 8.5 | 9 (10-07 21:56Z) |
| ap-northeast-1 apne1-az2 | 70 | 63% | 6.8 | 9 (10-07 21:56Z) |
| ap-northeast-1 apne1-az4 | 162 | 99% | 8.9 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az1 | 221 | 100% | 9.0 | 9 (10-08 08:51Z) |
| ap-northeast-2 apne2-az2 | 63 | 78% | 7.6 | 9 (10-06 21:35Z) |
| ap-northeast-2 apne2-az3 | 246 | 100% | 9.0 | 9 (10-08 08:51Z) |
| ap-northeast-2 apne2-az4 | 160 | 71% | 7.2 | 9 (10-08 08:51Z) |
| ap-south-1 aps1-az1 | 96 | 77% | 7.6 | 9 (10-08 01:50Z) |
| ap-south-1 aps1-az2 | 103 | 65% | 6.9 | 9 (10-08 01:50Z) |
| ap-south-1 aps1-az3 | 112 | 84% | 8.0 | 9 (10-08 01:50Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 55 | 24% | 4.3 | 3 (10-07 08:33Z) |
| us-east-1 use1-az1 | 17 | 71% | 6.8 | 2 (10-08 08:51Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 97 | 96% | 8.7 | 2 (10-08 08:51Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 102 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707700 | 2026-10-08T08:51:17Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-08T08:51:17Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.756100 | 2026-10-08T08:51:17Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.939100 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.604100 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578800 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-10-08T08:51:17Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-10-08T08:51:17Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.632000 | 2026-10-08T08:51:17Z |
| ap-south-1 | ap-south-1a | Windows | 0.385200 | 2026-10-08T08:51:17Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.697800 | 2026-10-08T08:51:17Z |
| ap-south-1 | ap-south-1b | Windows | 0.354600 | 2026-10-08T08:51:17Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718600 | 2026-10-08T08:51:17Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.505400 | 2026-10-08T08:51:17Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.458500 | 2026-10-08T08:51:17Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.581700 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.492400 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.479400 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.413700 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.503800 | 2026-10-08T08:51:17Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.533900 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2a | Windows | 0.640600 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516400 | 2026-10-08T08:51:17Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.530700 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2a | Windows | 0.323700 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.492300 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2b | Windows | 0.326000 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494300 | 2026-10-08T08:51:17Z |
| us-west-2 | us-west-2c | Windows | 0.323600 | 2026-10-08T08:51:17Z |
