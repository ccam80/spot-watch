# Spot placement score log

Generated 2026-10-27 10:26 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 381 | 46% | 5.1 | 9 (10-27 10:26Z) |
| ap-northeast-1 | 381 | 17% | 2.9 | 1 (10-27 10:26Z) |
| ap-northeast-2 | 381 | 59% | 6.5 | 9 (10-27 10:26Z) |
| ap-south-1 | 381 | 3% | 1.8 | 1 (10-27 10:26Z) |
| ap-southeast-2 | 381 | 1% | 1.1 | 1 (10-27 10:26Z) |
| ap-southeast-3 | 381 | 27% | 3.5 | 1 (10-27 10:26Z) |
| us-east-1 | 381 | 13% | 2.8 | 2 (10-27 10:26Z) |
| us-east-2 | 381 | 32% | 3.9 | 9 (10-27 10:26Z) |
| us-west-2 | 381 | 11% | 2.3 | 1 (10-27 10:26Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999911199999999999999991999999999999999999999
ap-northeast-1   122219811212111211112821124999994999919292112211
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222111111111111499911169111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   488117871136511899115991191911285874289886127111
us-east-1        999991121321121211151232222322199199399729992192
us-east-2        999991199911199111991111911119999991939919991119
us-west-2        192112111111131221951211221222222211919191112121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 5 | 3 | 3 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 124 | 7% | 1.7 | 1 (10-26 23:47Z) |
| ap-east-1 ape1-az2 | 283 | 61% | 6.4 | 9 (10-27 10:26Z) |
| ap-northeast-1 apne1-az1 | 63 | 6% | 1.7 | 1 (10-27 10:26Z) |
| ap-northeast-1 apne1-az4 | 176 | 30% | 3.9 | 1 (10-26 23:47Z) |
| ap-northeast-2 apne2-az1 | 332 | 54% | 6.1 | 9 (10-27 10:26Z) |
| ap-northeast-2 apne2-az3 | 352 | 59% | 6.5 | 9 (10-27 10:26Z) |
| ap-northeast-2 apne2-az4 | 377 | 59% | 6.5 | 9 (10-27 10:26Z) |
| ap-south-1 aps1-az1 | 90 | 1% | 1.5 | 1 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 62 | 3% | 1.3 | 1 (10-27 10:26Z) |
| ap-southeast-2 apse2-az2 | 39 | 0% | 1.0 | 1 (10-27 04:53Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 255 | 38% | 4.5 | 7 (10-26 19:12Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 100 | 3% | 1.5 | 1 (10-26 19:12Z) |
| us-east-1 use1-az4 | 119 | 30% | 3.6 | 1 (10-27 04:53Z) |
| us-east-1 use1-az5 | 124 | 31% | 3.7 | 9 (10-27 04:53Z) |
| us-east-1 use1-az6 | 90 | 30% | 3.5 | 9 (10-27 04:53Z) |
| us-east-2 use2-az1 | 158 | 47% | 5.0 | 8 (10-27 10:26Z) |
| us-east-2 use2-az2 | 202 | 51% | 5.4 | 9 (10-27 10:26Z) |
| us-east-2 use2-az3 | 233 | 49% | 5.3 | 9 (10-27 10:26Z) |
| us-west-2 usw2-az1 | 134 | 27% | 3.5 | 1 (10-26 23:47Z) |
| us-west-2 usw2-az2 | 85 | 24% | 3.2 | 1 (10-27 10:26Z) |
| us-west-2 usw2-az3 | 141 | 22% | 3.2 | 1 (10-27 04:53Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 381 | 60% | 6.6 | 9 (10-27 10:26Z) |
| ap-northeast-1 | 381 | 73% | 7.2 | 1 (10-27 10:26Z) |
| ap-northeast-2 | 381 | 100% | 9.0 | 9 (10-27 10:26Z) |
| ap-south-1 | 381 | 64% | 6.5 | 1 (10-27 10:26Z) |
| ap-southeast-2 | 381 | 19% | 3.2 | 1 (10-27 10:26Z) |
| ap-southeast-3 | 381 | 27% | 3.5 | 1 (10-27 10:26Z) |
| us-east-1 | 381 | 71% | 6.6 | 9 (10-27 10:26Z) |
| us-east-2 | 381 | 71% | 6.9 | 9 (10-27 10:26Z) |
| us-west-2 | 381 | 53% | 5.8 | 9 (10-27 10:26Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999329912399923999239992399999999999999999199911
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999929999222822999929999919999999999999999919911
ap-southeast-2   991119111111111111111111111111119199999911111111
ap-southeast-3   488117871136511899115991191911285874289886127111
us-east-1        999994645634443643392465645659999999999999994399
us-east-2        999992399952999129997221952269999991989939999999
us-west-2        999995343943391453999333454534599954999993494459
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 8 | 8 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 234 | 77% | 7.6 | 9 (10-27 10:26Z) |
| ap-east-1 ape1-az2 | 196 | 79% | 7.7 | 9 (10-26 23:47Z) |
| ap-east-1 ape1-az3 | 206 | 79% | 7.7 | 9 (10-27 10:26Z) |
| ap-northeast-1 apne1-az1 | 169 | 93% | 8.6 | 9 (10-26 19:12Z) |
| ap-northeast-1 apne1-az2 | 119 | 77% | 7.6 | 9 (10-26 23:47Z) |
| ap-northeast-1 apne1-az4 | 213 | 99% | 8.9 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az1 | 303 | 100% | 9.0 | 9 (10-27 10:26Z) |
| ap-northeast-2 apne2-az2 | 79 | 80% | 7.7 | 9 (10-26 19:12Z) |
| ap-northeast-2 apne2-az3 | 327 | 100% | 9.0 | 9 (10-27 10:26Z) |
| ap-northeast-2 apne2-az4 | 233 | 80% | 7.8 | 9 (10-27 10:26Z) |
| ap-south-1 aps1-az1 | 132 | 83% | 8.0 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az2 | 148 | 76% | 7.5 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 114 | 95% | 8.6 | 9 (10-27 10:26Z) |
| us-east-1 use1-az5 | 82 | 98% | 8.8 | 9 (10-27 10:26Z) |
| us-east-1 use1-az6 | 101 | 96% | 8.7 | 9 (10-27 10:26Z) |
| us-east-2 use2-az1 | 132 | 98% | 8.9 | 9 (10-27 10:26Z) |
| us-east-2 use2-az2 | 168 | 99% | 8.9 | 9 (10-27 04:53Z) |
| us-east-2 use2-az3 | 173 | 95% | 8.7 | 9 (10-27 10:26Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703300 | 2026-10-27T10:26:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-27T10:26:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.774500 | 2026-10-27T10:26:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.963600 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.586200 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-27T10:26:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-27T10:26:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.558000 | 2026-10-27T10:26:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.446800 | 2026-10-27T10:26:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.655200 | 2026-10-27T10:26:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.409900 | 2026-10-27T10:26:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.661600 | 2026-10-27T10:26:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510900 | 2026-10-27T10:26:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.661200 | 2026-10-27T10:26:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556900 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.599600 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.460500 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.489900 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.524700 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.537200 | 2026-10-27T10:26:05Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.561300 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548600 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547500 | 2026-10-27T10:26:05Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.564700 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2a | Windows | 0.320000 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.577500 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2b | Windows | 0.327200 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.561500 | 2026-10-27T10:26:05Z |
| us-west-2 | us-west-2c | Windows | 0.319500 | 2026-10-27T10:26:05Z |
