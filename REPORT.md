# Spot placement score log

Generated 2026-10-10 15:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 294 | 32% | 4.1 | 2 (10-10 15:16Z) |
| ap-northeast-1 | 294 | 16% | 2.8 | 2 (10-10 15:16Z) |
| ap-northeast-2 | 294 | 47% | 5.8 | 9 (10-10 15:16Z) |
| ap-south-1 | 294 | 2% | 1.8 | 1 (10-10 15:16Z) |
| ap-southeast-2 | 294 | 0% | 1.0 | 1 (10-10 15:16Z) |
| ap-southeast-3 | 294 | 20% | 3.2 | 9 (10-10 15:16Z) |
| us-east-1 | 294 | 10% | 2.5 | 3 (10-10 15:16Z) |
| us-east-2 | 294 | 26% | 3.5 | 8 (10-10 15:16Z) |
| us-west-2 | 294 | 12% | 2.4 | 9 (10-10 15:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911111199399119119999812111111111111111111111182
ap-northeast-1   279981212982199999999999911911115119711111191112
ap-northeast-2   999999999999999999999999991499999999999999999199
ap-south-1       111111111112111111111112222222222222211122111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   161111119991141111111111111111111138811111389119
us-east-1        322222119229222331199199999211112111122211323233
us-east-2        171218999999991199999999999111811111111111111118
us-west-2        222121112221212999999991991121121211111111111199
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 4 | 2 | 3 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 96 | 0% | 1.4 | 1 (10-10 01:42Z) |
| ap-east-1 ape1-az2 | 201 | 46% | 5.4 | 8 (10-10 08:24Z) |
| ap-northeast-1 apne1-az1 | 49 | 8% | 1.8 | 1 (10-09 21:36Z) |
| ap-northeast-1 apne1-az4 | 141 | 26% | 3.7 | 1 (10-10 01:42Z) |
| ap-northeast-2 apne2-az1 | 254 | 44% | 5.5 | 9 (10-10 15:16Z) |
| ap-northeast-2 apne2-az3 | 267 | 48% | 5.8 | 5 (10-10 15:16Z) |
| ap-northeast-2 apne2-az4 | 291 | 47% | 5.8 | 9 (10-10 15:16Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 30 | 0% | 1.0 | 1 (10-10 08:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 199 | 29% | 4.1 | 9 (10-10 15:16Z) |
| us-east-1 use1-az1 | 53 | 0% | 1.1 | 1 (10-10 15:16Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 93 | 27% | 3.4 | 1 (10-10 15:16Z) |
| us-east-1 use1-az5 | 93 | 25% | 3.3 | 1 (10-10 08:24Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 117 | 37% | 4.3 | 1 (10-10 01:42Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 177 | 41% | 4.8 | 8 (10-10 15:16Z) |
| us-west-2 usw2-az1 | 101 | 30% | 3.8 | 9 (10-10 15:16Z) |
| us-west-2 usw2-az2 | 63 | 25% | 3.4 | 8 (10-10 15:16Z) |
| us-west-2 usw2-az3 | 123 | 21% | 3.2 | 9 (10-10 15:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 294 | 48% | 5.9 | 9 (10-10 15:16Z) |
| ap-northeast-1 | 294 | 73% | 7.1 | 9 (10-10 15:16Z) |
| ap-northeast-2 | 294 | 100% | 9.0 | 9 (10-10 15:16Z) |
| ap-south-1 | 294 | 60% | 6.3 | 9 (10-10 15:16Z) |
| ap-southeast-2 | 294 | 16% | 3.1 | 9 (10-10 15:16Z) |
| ap-southeast-3 | 294 | 20% | 3.2 | 9 (10-10 15:16Z) |
| us-east-1 | 294 | 71% | 6.6 | 9 (10-10 15:16Z) |
| us-east-2 | 294 | 72% | 7.1 | 9 (10-10 15:16Z) |
| us-west-2 | 294 | 52% | 5.7 | 9 (10-10 15:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999224992299999999999991992399139911991199999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992999992999999999999999992299299929991999149999
ap-southeast-2   222222222222222222229299922911111119111111118919
ap-southeast-3   161111119991141111111111111111111138811111389119
us-east-1        433344559449855763499999999554533433366354645699
us-east-2        983599999999993999999999999239933212121112121199
us-west-2        445444339344995999999999999432354413233313323399
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 69% | 7.1 | 9 (10-10 01:42Z) |
| ap-east-1 ape1-az2 | 145 | 72% | 7.3 | 9 (10-10 15:16Z) |
| ap-east-1 ape1-az3 | 143 | 69% | 7.2 | 9 (10-10 15:16Z) |
| ap-northeast-1 apne1-az1 | 138 | 92% | 8.5 | 9 (10-09 21:36Z) |
| ap-northeast-1 apne1-az2 | 74 | 65% | 6.9 | 9 (10-10 01:42Z) |
| ap-northeast-1 apne1-az4 | 167 | 99% | 8.9 | 9 (10-10 01:42Z) |
| ap-northeast-2 apne2-az1 | 230 | 100% | 9.0 | 9 (10-10 15:16Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 253 | 100% | 9.0 | 9 (10-10 15:16Z) |
| ap-northeast-2 apne2-az4 | 168 | 72% | 7.3 | 9 (10-10 15:16Z) |
| ap-south-1 aps1-az1 | 100 | 78% | 7.7 | 9 (10-10 08:24Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 117 | 85% | 8.1 | 9 (10-10 01:42Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 34 | 62% | 6.6 | 9 (10-10 15:16Z) |
| ap-southeast-3 apse3-az3 | 58 | 26% | 4.5 | 9 (10-09 21:36Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 99 | 95% | 8.6 | 9 (10-10 15:16Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 81 | 95% | 8.7 | 9 (10-10 08:24Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 148 | 99% | 8.9 | 9 (10-10 08:24Z) |
| us-east-2 use2-az3 | 132 | 94% | 8.6 | 9 (10-10 15:16Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 67 | 96% | 8.7 | 9 (10-10 15:16Z) |
| us-west-2 usw2-az3 | 84 | 95% | 8.7 | 9 (10-10 15:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708300 | 2026-10-10T15:16:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-10T15:16:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.769000 | 2026-10-10T15:16:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.952000 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.598600 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.584800 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574800 | 2026-10-10T15:16:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742600 | 2026-10-10T15:16:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.604600 | 2026-10-10T15:16:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.371100 | 2026-10-10T15:16:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.678600 | 2026-10-10T15:16:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.351900 | 2026-10-10T15:16:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.716200 | 2026-10-10T15:16:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504700 | 2026-10-10T15:16:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.418100 | 2026-10-10T15:16:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574800 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.535900 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.481600 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.462800 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.396000 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.468700 | 2026-10-10T15:16:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535300 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2a | Windows | 0.639900 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529900 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2b | Windows | 0.640000 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517200 | 2026-10-10T15:16:49Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.525200 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2a | Windows | 0.320900 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.487300 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2b | Windows | 0.322800 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.492200 | 2026-10-10T15:16:49Z |
| us-west-2 | us-west-2c | Windows | 0.320500 | 2026-10-10T15:16:49Z |
