# Spot placement score log

Generated 2026-10-07 16:22 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 282 | 33% | 4.2 | 1 (10-07 16:22Z) |
| ap-northeast-1 | 282 | 16% | 2.8 | 9 (10-07 16:22Z) |
| ap-northeast-2 | 282 | 45% | 5.7 | 9 (10-07 16:22Z) |
| ap-south-1 | 282 | 2% | 1.8 | 2 (10-07 16:22Z) |
| ap-southeast-2 | 282 | 0% | 1.0 | 1 (10-07 16:22Z) |
| ap-southeast-3 | 282 | 20% | 3.2 | 8 (10-07 16:22Z) |
| us-east-1 | 282 | 10% | 2.6 | 1 (10-07 16:22Z) |
| us-east-2 | 282 | 27% | 3.6 | 1 (10-07 16:22Z) |
| us-west-2 | 282 | 11% | 2.4 | 1 (10-07 16:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999989999911111199399119119999812111111111111
ap-northeast-1   222211118991279981212982199999999999911911115119
ap-northeast-2   999999999999999999999999999999999999991499999999
ap-south-1       111111111111111111111112111111111112222222222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111114765161111119991141111111111111111111138
us-east-1        913222222222322222119229222331199199999211112111
us-east-2        999999111118171218999999991199999999999111811111
us-west-2        121122222222222121112221212999999991991121121211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 6 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 6 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 94 | 0% | 1.4 | 1 (10-07 08:33Z) |
| ap-east-1 ape1-az2 | 196 | 47% | 5.5 | 1 (10-07 16:22Z) |
| ap-northeast-1 apne1-az1 | 45 | 9% | 1.8 | 1 (10-07 16:22Z) |
| ap-northeast-1 apne1-az4 | 137 | 26% | 3.6 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az1 | 244 | 41% | 5.4 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az3 | 257 | 46% | 5.7 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az4 | 279 | 46% | 5.7 | 9 (10-07 16:22Z) |
| ap-south-1 aps1-az1 | 73 | 1% | 1.6 | 1 (10-06 10:07Z) |
| ap-south-1 aps1-az3 | 106 | 3% | 2.4 | 1 (10-07 01:27Z) |
| ap-southeast-2 apse2-az1 | 41 | 0% | 1.1 | 1 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 55 | 0% | 1.0 | 1 (10-07 01:27Z) |
| ap-southeast-3 apse3-az3 | 192 | 28% | 4.1 | 8 (10-07 16:22Z) |
| us-east-1 use1-az1 | 43 | 0% | 1.1 | 1 (10-07 16:22Z) |
| us-east-1 use1-az2 | 77 | 4% | 1.6 | 1 (10-07 08:33Z) |
| us-east-1 use1-az4 | 87 | 29% | 3.6 | 1 (10-06 02:54Z) |
| us-east-1 use1-az5 | 90 | 26% | 3.3 | 1 (10-06 21:35Z) |
| us-east-1 use1-az6 | 71 | 21% | 2.9 | 1 (10-07 01:27Z) |
| us-east-2 use2-az1 | 113 | 38% | 4.4 | 2 (10-06 10:07Z) |
| us-east-2 use2-az2 | 149 | 43% | 4.9 | 1 (10-07 08:33Z) |
| us-east-2 use2-az3 | 172 | 41% | 4.9 | 1 (10-07 08:33Z) |
| us-west-2 usw2-az1 | 96 | 29% | 3.8 | 1 (10-07 01:27Z) |
| us-west-2 usw2-az2 | 56 | 25% | 3.4 | 1 (10-07 16:22Z) |
| us-west-2 usw2-az3 | 119 | 21% | 3.2 | 1 (10-07 08:33Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 282 | 46% | 5.7 | 9 (10-07 16:22Z) |
| ap-northeast-1 | 282 | 73% | 7.2 | 9 (10-07 16:22Z) |
| ap-northeast-2 | 282 | 100% | 9.0 | 9 (10-07 16:22Z) |
| ap-south-1 | 282 | 59% | 6.3 | 9 (10-07 16:22Z) |
| ap-southeast-2 | 282 | 16% | 3.1 | 9 (10-07 16:22Z) |
| ap-southeast-3 | 282 | 20% | 3.2 | 8 (10-07 16:22Z) |
| us-east-1 | 282 | 71% | 6.6 | 3 (10-07 16:22Z) |
| us-east-2 | 282 | 75% | 7.3 | 2 (10-07 16:22Z) |
| us-west-2 | 282 | 54% | 5.8 | 3 (10-07 16:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   234437999999999999224992299999999999991992399139
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111992999992999999999999999992299299929
ap-southeast-2   222222222222222222222222222222229299922911111119
ap-southeast-3   111111114765161111119991141111111111111111111138
us-east-1        936554443334433344559449855763499999999554533433
us-east-2        999999832929983599999999993999999999999239933212
us-west-2        253455455444445444339344995999999999999432354413
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 8 | 6 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 165 | 67% | 7.0 | 9 (10-07 16:22Z) |
| ap-east-1 ape1-az2 | 135 | 70% | 7.2 | 9 (10-07 16:22Z) |
| ap-east-1 ape1-az3 | 131 | 66% | 7.0 | 9 (10-07 16:22Z) |
| ap-northeast-1 apne1-az1 | 133 | 92% | 8.5 | 9 (10-07 16:22Z) |
| ap-northeast-1 apne1-az2 | 69 | 62% | 6.7 | 9 (10-07 16:22Z) |
| ap-northeast-1 apne1-az4 | 162 | 99% | 8.9 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az1 | 218 | 100% | 9.0 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az2 | 63 | 78% | 7.6 | 9 (10-06 21:35Z) |
| ap-northeast-2 apne2-az3 | 243 | 100% | 9.0 | 9 (10-07 08:33Z) |
| ap-northeast-2 apne2-az4 | 157 | 70% | 7.2 | 9 (10-07 08:33Z) |
| ap-south-1 aps1-az1 | 94 | 77% | 7.6 | 9 (10-07 16:22Z) |
| ap-south-1 aps1-az2 | 101 | 64% | 6.8 | 9 (10-07 01:27Z) |
| ap-south-1 aps1-az3 | 111 | 84% | 8.0 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 55 | 24% | 4.3 | 3 (10-07 08:33Z) |
| us-east-1 use1-az1 | 15 | 80% | 7.4 | 2 (10-07 08:33Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 96 | 97% | 8.8 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 58 | 98% | 8.9 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 102 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 71 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707900 | 2026-10-07T16:22:16Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-07T16:22:16Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.755200 | 2026-10-07T16:22:16Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938200 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.603000 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578300 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571200 | 2026-10-07T16:22:16Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-10-07T16:22:16Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.644900 | 2026-10-07T16:22:16Z |
| ap-south-1 | ap-south-1a | Windows | 0.383900 | 2026-10-07T16:22:16Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.704400 | 2026-10-07T16:22:16Z |
| ap-south-1 | ap-south-1b | Windows | 0.355500 | 2026-10-07T16:22:16Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719900 | 2026-10-07T16:22:16Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.506000 | 2026-10-07T16:22:16Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.474600 | 2026-10-07T16:22:16Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.589100 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.493400 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.482500 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.415200 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.504600 | 2026-10-07T16:22:16Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532800 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2a | Windows | 0.640400 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527200 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516100 | 2026-10-07T16:22:16Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.528700 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2a | Windows | 0.325600 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.494000 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2b | Windows | 0.327100 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494500 | 2026-10-07T16:22:16Z |
| us-west-2 | us-west-2c | Windows | 0.324400 | 2026-10-07T16:22:16Z |
