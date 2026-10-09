# Spot placement score log

Generated 2026-10-09 02:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 288 | 32% | 4.1 | 1 (10-09 02:03Z) |
| ap-northeast-1 | 288 | 16% | 2.8 | 1 (10-09 02:03Z) |
| ap-northeast-2 | 288 | 46% | 5.8 | 9 (10-09 02:03Z) |
| ap-south-1 | 288 | 2% | 1.8 | 2 (10-09 02:03Z) |
| ap-southeast-2 | 288 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 | 288 | 20% | 3.2 | 1 (10-09 02:03Z) |
| us-east-1 | 288 | 10% | 2.5 | 1 (10-09 02:03Z) |
| us-east-2 | 288 | 26% | 3.5 | 1 (10-09 02:03Z) |
| us-west-2 | 288 | 11% | 2.4 | 1 (10-09 02:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        989999911111199399119119999812111111111111111111
ap-northeast-1   118991279981212982199999999999911911115119711111
ap-northeast-2   999999999999999999999999999999991499999999999999
ap-south-1       111111111111111112111111111112222222222222211122
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   114765161111119991141111111111111111111138811111
us-east-1        222222322222119229222331199199999211112111122211
us-east-2        111118171218999999991199999999999111811111111111
us-west-2        222222222121112221212999999991991121121211111111
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
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 6 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 95 | 0% | 1.4 | 1 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 200 | 46% | 5.4 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 47 | 9% | 1.8 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 139 | 26% | 3.6 | 1 (10-08 08:51Z) |
| ap-northeast-2 apne2-az1 | 250 | 43% | 5.4 | 9 (10-09 02:03Z) |
| ap-northeast-2 apne2-az3 | 262 | 47% | 5.8 | 9 (10-09 02:03Z) |
| ap-northeast-2 apne2-az4 | 285 | 47% | 5.8 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az1 | 74 | 1% | 1.6 | 1 (10-09 02:03Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 44 | 0% | 1.1 | 1 (10-08 22:00Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 195 | 28% | 4.0 | 1 (10-08 22:00Z) |
| us-east-1 use1-az1 | 47 | 0% | 1.1 | 1 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 4% | 1.6 | 1 (10-09 02:03Z) |
| us-east-1 use1-az4 | 89 | 28% | 3.5 | 1 (10-08 22:00Z) |
| us-east-1 use1-az5 | 92 | 25% | 3.3 | 1 (10-08 16:24Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 114 | 38% | 4.3 | 1 (10-09 02:03Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 174 | 41% | 4.8 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az1 | 99 | 28% | 3.7 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az2 | 58 | 24% | 3.4 | 1 (10-08 22:00Z) |
| us-west-2 usw2-az3 | 121 | 21% | 3.2 | 1 (10-09 02:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 288 | 47% | 5.8 | 9 (10-09 02:03Z) |
| ap-northeast-1 | 288 | 73% | 7.1 | 1 (10-09 02:03Z) |
| ap-northeast-2 | 288 | 100% | 9.0 | 9 (10-09 02:03Z) |
| ap-south-1 | 288 | 60% | 6.3 | 9 (10-09 02:03Z) |
| ap-southeast-2 | 288 | 16% | 3.1 | 1 (10-09 02:03Z) |
| ap-southeast-3 | 288 | 20% | 3.2 | 1 (10-09 02:03Z) |
| us-east-1 | 288 | 70% | 6.6 | 4 (10-09 02:03Z) |
| us-east-2 | 288 | 73% | 7.1 | 2 (10-09 02:03Z) |
| us-west-2 | 288 | 52% | 5.7 | 3 (10-09 02:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999224992299999999999991992399139911991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111992999992999999999999999992299299929991999
ap-southeast-2   222222222222222222222222229299922911111119111111
ap-southeast-3   114765161111119991141111111111111111111138811111
us-east-1        443334433344559449855763499999999554533433366354
us-east-2        832929983599999999993999999999999239933212121112
us-west-2        455444445444339344995999999999999432354413233313
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
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
| ap-east-1 ape1-az1 | 171 | 68% | 7.1 | 9 (10-09 02:03Z) |
| ap-east-1 ape1-az2 | 141 | 71% | 7.3 | 9 (10-09 02:03Z) |
| ap-east-1 ape1-az3 | 137 | 68% | 7.1 | 9 (10-09 02:03Z) |
| ap-northeast-1 apne1-az1 | 136 | 92% | 8.5 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az2 | 71 | 63% | 6.8 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 164 | 99% | 8.9 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az1 | 224 | 100% | 9.0 | 9 (10-09 02:03Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 248 | 100% | 9.0 | 9 (10-09 02:03Z) |
| ap-northeast-2 apne2-az4 | 162 | 71% | 7.3 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az1 | 98 | 78% | 7.7 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az2 | 104 | 65% | 6.9 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az3 | 115 | 84% | 8.1 | 9 (10-09 02:03Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 55 | 24% | 4.3 | 3 (10-07 08:33Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706300 | 2026-10-09T02:03:23Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-09T02:03:23Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.761100 | 2026-10-09T02:03:23Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.942100 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.600500 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579700 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574300 | 2026-10-09T02:03:23Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742900 | 2026-10-09T02:03:23Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.620200 | 2026-10-09T02:03:23Z |
| ap-south-1 | ap-south-1a | Windows | 0.378500 | 2026-10-09T02:03:23Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.688600 | 2026-10-09T02:03:23Z |
| ap-south-1 | ap-south-1b | Windows | 0.353700 | 2026-10-09T02:03:23Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718200 | 2026-10-09T02:03:23Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503700 | 2026-10-09T02:03:23Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.440400 | 2026-10-09T02:03:23Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.569400 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.489000 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.481000 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.411100 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.491800 | 2026-10-09T02:03:23Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534500 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529000 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517200 | 2026-10-09T02:03:23Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.529700 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2a | Windows | 0.323100 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491400 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2b | Windows | 0.325500 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.496800 | 2026-10-09T02:03:23Z |
| us-west-2 | us-west-2c | Windows | 0.322900 | 2026-10-09T02:03:23Z |
