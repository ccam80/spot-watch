# Spot placement score log

Generated 2026-10-28 09:18 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 399 | 47% | 5.1 | 9 (10-28 09:18Z) |
| ap-northeast-1 | 399 | 16% | 2.8 | 1 (10-28 09:18Z) |
| ap-northeast-2 | 399 | 61% | 6.6 | 9 (10-28 09:18Z) |
| ap-south-1 | 399 | 3% | 1.8 | 1 (10-28 09:18Z) |
| ap-southeast-2 | 399 | 1% | 1.1 | 1 (10-28 09:18Z) |
| ap-southeast-3 | 399 | 27% | 3.5 | 1 (10-28 09:18Z) |
| us-east-1 | 399 | 12% | 2.7 | 2 (10-28 09:18Z) |
| us-east-2 | 399 | 33% | 3.9 | 9 (10-28 09:18Z) |
| us-west-2 | 399 | 11% | 2.3 | 1 (10-28 09:18Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991999999999999999999999999999911111199999
ap-northeast-1   112821124999994999919292112211312222221111111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222111111111111499911169111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   115991191911285874289886127111864885411111111111
us-east-1        151232222322199199399729992192332223331112211122
us-east-2        991111911119999991939919991119611199991119111999
us-west-2        951211221222222211919191112121111111111111112111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 126 | 7% | 1.7 | 1 (10-28 09:18Z) |
| ap-east-1 ape1-az2 | 299 | 62% | 6.4 | 9 (10-28 09:18Z) |
| ap-northeast-1 apne1-az1 | 70 | 6% | 1.6 | 1 (10-28 08:21Z) |
| ap-northeast-1 apne1-az4 | 181 | 29% | 3.8 | 1 (10-28 05:16Z) |
| ap-northeast-2 apne2-az1 | 349 | 54% | 6.1 | 2 (10-28 08:21Z) |
| ap-northeast-2 apne2-az3 | 368 | 60% | 6.5 | 4 (10-28 09:18Z) |
| ap-northeast-2 apne2-az4 | 395 | 61% | 6.7 | 9 (10-28 09:18Z) |
| ap-south-1 aps1-az1 | 97 | 1% | 1.5 | 1 (10-28 09:18Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 68 | 3% | 1.3 | 1 (10-28 08:21Z) |
| ap-southeast-2 apse2-az2 | 42 | 0% | 1.0 | 1 (10-28 06:26Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 265 | 39% | 4.5 | 1 (10-28 04:19Z) |
| us-east-1 use1-az1 | 76 | 0% | 1.1 | 1 (10-28 06:26Z) |
| us-east-1 use1-az2 | 105 | 3% | 1.4 | 1 (10-28 05:16Z) |
| us-east-1 use1-az4 | 125 | 29% | 3.5 | 1 (10-28 06:26Z) |
| us-east-1 use1-az5 | 131 | 29% | 3.5 | 1 (10-28 08:21Z) |
| us-east-1 use1-az6 | 93 | 29% | 3.5 | 1 (10-28 09:18Z) |
| us-east-2 use2-az1 | 165 | 47% | 5.0 | 9 (10-28 09:18Z) |
| us-east-2 use2-az2 | 213 | 53% | 5.5 | 9 (10-28 09:18Z) |
| us-east-2 use2-az3 | 246 | 49% | 5.3 | 9 (10-28 09:18Z) |
| us-west-2 usw2-az1 | 137 | 26% | 3.5 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az2 | 93 | 22% | 3.0 | 1 (10-28 08:21Z) |
| us-west-2 usw2-az3 | 149 | 21% | 3.1 | 1 (10-28 09:18Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 399 | 62% | 6.7 | 9 (10-28 09:18Z) |
| ap-northeast-1 | 399 | 72% | 7.1 | 2 (10-28 09:18Z) |
| ap-northeast-2 | 399 | 100% | 9.0 | 9 (10-28 09:18Z) |
| ap-south-1 | 399 | 63% | 6.5 | 1 (10-28 09:18Z) |
| ap-southeast-2 | 399 | 19% | 3.2 | 9 (10-28 09:18Z) |
| ap-southeast-3 | 399 | 27% | 3.5 | 1 (10-28 09:18Z) |
| us-east-1 | 399 | 71% | 6.5 | 9 (10-28 09:18Z) |
| us-east-2 | 399 | 72% | 7.0 | 9 (10-28 09:18Z) |
| us-west-2 | 399 | 51% | 5.6 | 4 (10-28 09:18Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   239992399999999999999999199911999999992211111122
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       929999919999999999999999919911211999999999911111
ap-southeast-2   111111111111119199999911111111119911111111111119
ap-southeast-3   115991191911285874289886127111864885411111111111
us-east-1        392465645659999999999999994399554457669969654459
us-east-2        997221952269999991989939999999999999999999999999
us-west-2        999333454534599954999993494459113333343333335594
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 247 | 78% | 7.7 | 9 (10-28 08:21Z) |
| ap-east-1 ape1-az2 | 209 | 80% | 7.8 | 9 (10-28 09:18Z) |
| ap-east-1 ape1-az3 | 222 | 80% | 7.8 | 9 (10-28 09:18Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 320 | 100% | 9.0 | 9 (10-28 09:18Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 343 | 100% | 9.0 | 9 (10-28 09:18Z) |
| ap-northeast-2 apne2-az4 | 247 | 81% | 7.9 | 9 (10-28 09:18Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 36 | 72% | 7.3 | 9 (10-28 09:18Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 116 | 94% | 8.6 | 9 (10-28 09:18Z) |
| us-east-1 use1-az5 | 86 | 98% | 8.8 | 9 (10-28 09:18Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 146 | 99% | 8.9 | 9 (10-28 08:21Z) |
| us-east-2 use2-az2 | 180 | 99% | 8.9 | 9 (10-28 09:18Z) |
| us-east-2 use2-az3 | 190 | 96% | 8.7 | 9 (10-28 09:18Z) |
| us-west-2 usw2-az1 | 84 | 98% | 8.8 | 9 (10-28 08:21Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 100 | 92% | 8.4 | 2 (10-28 07:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703500 | 2026-10-28T09:18:42Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T09:18:42Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790600 | 2026-10-28T09:18:42Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964500 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585000 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570600 | 2026-10-28T09:18:42Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T09:18:42Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.571500 | 2026-10-28T09:18:42Z |
| ap-south-1 | ap-south-1a | Windows | 0.456800 | 2026-10-28T09:18:42Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.632800 | 2026-10-28T09:18:42Z |
| ap-south-1 | ap-south-1b | Windows | 0.402700 | 2026-10-28T09:18:42Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656200 | 2026-10-28T09:18:42Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517700 | 2026-10-28T09:18:42Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660700 | 2026-10-28T09:18:42Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.595800 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.475100 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524700 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520500 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.536800 | 2026-10-28T09:18:42Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.565300 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-28T09:18:42Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566000 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2a | Windows | 0.319200 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2b | Windows | 0.327200 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.562900 | 2026-10-28T09:18:42Z |
| us-west-2 | us-west-2c | Windows | 0.318800 | 2026-10-28T09:18:42Z |
