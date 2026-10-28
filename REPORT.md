# Spot placement score log

Generated 2026-10-28 12:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 402 | 47% | 5.2 | 9 (10-28 12:23Z) |
| ap-northeast-1 | 402 | 16% | 2.8 | 1 (10-28 12:23Z) |
| ap-northeast-2 | 402 | 61% | 6.7 | 9 (10-28 12:23Z) |
| ap-south-1 | 402 | 3% | 1.8 | 1 (10-28 12:23Z) |
| ap-southeast-2 | 402 | 0% | 1.0 | 1 (10-28 12:23Z) |
| ap-southeast-3 | 402 | 27% | 3.5 | 5 (10-28 12:23Z) |
| us-east-1 | 402 | 12% | 2.7 | 3 (10-28 12:23Z) |
| us-east-2 | 402 | 33% | 3.9 | 1 (10-28 12:23Z) |
| us-west-2 | 402 | 11% | 2.3 | 2 (10-28 12:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999991999999999999999999999999999911111199999999
ap-northeast-1   821124999994999919292112211312222221111111111121
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111499911169111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   991191911285874289886127111864885411111111111115
us-east-1        232222322199199399729992192332223331112211122333
us-east-2        111911119999991939919991119611199991119111999911
us-west-2        211221222222211919191112121111111111111112111122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 8 | 4 | 6 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 128 | 7% | 1.7 | 1 (10-28 11:16Z) |
| ap-east-1 ape1-az2 | 302 | 63% | 6.5 | 9 (10-28 12:23Z) |
| ap-northeast-1 apne1-az1 | 70 | 6% | 1.6 | 1 (10-28 08:21Z) |
| ap-northeast-1 apne1-az4 | 183 | 29% | 3.8 | 1 (10-28 12:23Z) |
| ap-northeast-2 apne2-az1 | 350 | 54% | 6.1 | 1 (10-28 12:23Z) |
| ap-northeast-2 apne2-az3 | 371 | 61% | 6.5 | 9 (10-28 12:23Z) |
| ap-northeast-2 apne2-az4 | 398 | 62% | 6.7 | 9 (10-28 12:23Z) |
| ap-south-1 aps1-az1 | 99 | 1% | 1.5 | 1 (10-28 11:16Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 68 | 3% | 1.3 | 1 (10-28 08:21Z) |
| ap-southeast-2 apse2-az2 | 42 | 0% | 1.0 | 1 (10-28 06:26Z) |
| ap-southeast-3 apse3-az1 | 77 | 0% | 1.0 | 1 (10-28 11:16Z) |
| ap-southeast-3 apse3-az3 | 266 | 39% | 4.5 | 5 (10-28 12:23Z) |
| us-east-1 use1-az1 | 76 | 0% | 1.1 | 1 (10-28 06:26Z) |
| us-east-1 use1-az2 | 106 | 3% | 1.4 | 1 (10-28 12:23Z) |
| us-east-1 use1-az4 | 125 | 29% | 3.5 | 1 (10-28 06:26Z) |
| us-east-1 use1-az5 | 132 | 29% | 3.5 | 1 (10-28 12:23Z) |
| us-east-1 use1-az6 | 95 | 28% | 3.4 | 1 (10-28 11:16Z) |
| us-east-2 use2-az1 | 166 | 47% | 5.0 | 9 (10-28 10:17Z) |
| us-east-2 use2-az2 | 215 | 53% | 5.5 | 1 (10-28 11:16Z) |
| us-east-2 use2-az3 | 248 | 49% | 5.3 | 1 (10-28 12:23Z) |
| us-west-2 usw2-az1 | 138 | 26% | 3.4 | 1 (10-28 12:23Z) |
| us-west-2 usw2-az2 | 93 | 22% | 3.0 | 1 (10-28 08:21Z) |
| us-west-2 usw2-az3 | 151 | 21% | 3.1 | 1 (10-28 11:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 402 | 62% | 6.7 | 9 (10-28 12:23Z) |
| ap-northeast-1 | 402 | 72% | 7.0 | 9 (10-28 12:23Z) |
| ap-northeast-2 | 402 | 100% | 9.0 | 9 (10-28 12:23Z) |
| ap-south-1 | 402 | 63% | 6.4 | 1 (10-28 12:23Z) |
| ap-southeast-2 | 402 | 20% | 3.2 | 9 (10-28 12:23Z) |
| ap-southeast-3 | 402 | 27% | 3.5 | 5 (10-28 12:23Z) |
| us-east-1 | 402 | 71% | 6.5 | 4 (10-28 12:23Z) |
| us-east-2 | 402 | 73% | 7.0 | 9 (10-28 12:23Z) |
| us-west-2 | 402 | 51% | 5.7 | 9 (10-28 12:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992399999999999999999199911999999992211111122279
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999919999999999999999919911211999999999911111111
ap-southeast-2   111111111119199999911111111119911111111111119999
ap-southeast-3   991191911285874289886127111864885411111111111115
us-east-1        465645659999999999999994399554457669969654459654
us-east-2        221952269999991989939999999999999999999999999999
us-west-2        333454534599954999993494459113333343333335594399
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 249 | 78% | 7.7 | 9 (10-28 11:16Z) |
| ap-east-1 ape1-az2 | 211 | 81% | 7.8 | 9 (10-28 12:23Z) |
| ap-east-1 ape1-az3 | 224 | 80% | 7.8 | 9 (10-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 126 | 79% | 7.7 | 9 (10-28 12:23Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 322 | 100% | 9.0 | 9 (10-28 11:16Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 346 | 100% | 9.0 | 9 (10-28 12:23Z) |
| ap-northeast-2 apne2-az4 | 250 | 81% | 7.9 | 9 (10-28 12:23Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 37 | 73% | 7.3 | 9 (10-28 12:23Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 48 | 73% | 7.3 | 9 (10-28 12:23Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 116 | 94% | 8.6 | 9 (10-28 09:18Z) |
| us-east-1 use1-az5 | 86 | 98% | 8.8 | 9 (10-28 09:18Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 149 | 99% | 8.9 | 9 (10-28 12:23Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 193 | 96% | 8.7 | 9 (10-28 12:23Z) |
| us-west-2 usw2-az1 | 85 | 98% | 8.8 | 9 (10-28 12:23Z) |
| us-west-2 usw2-az2 | 78 | 96% | 8.7 | 9 (10-28 11:16Z) |
| us-west-2 usw2-az3 | 102 | 92% | 8.5 | 9 (10-28 12:23Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703500 | 2026-10-28T12:23:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T12:23:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790600 | 2026-10-28T12:23:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.973600 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584700 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585700 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-28T12:23:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T12:23:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.571500 | 2026-10-28T12:23:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.456800 | 2026-10-28T12:23:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.625500 | 2026-10-28T12:23:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.402700 | 2026-10-28T12:23:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656200 | 2026-10-28T12:23:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517700 | 2026-10-28T12:23:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660700 | 2026-10-28T12:23:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.592800 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.475100 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524700 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520500 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.542100 | 2026-10-28T12:23:44Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.564600 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547900 | 2026-10-28T12:23:44Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566000 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2a | Windows | 0.319200 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2b | Windows | 0.326800 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.562900 | 2026-10-28T12:23:44Z |
| us-west-2 | us-west-2c | Windows | 0.318800 | 2026-10-28T12:23:44Z |
