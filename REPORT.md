# Spot placement score log

Generated 2026-10-25 01:06 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 369 | 44% | 5.0 | 9 (10-25 01:06Z) |
| ap-northeast-1 | 369 | 17% | 2.9 | 9 (10-25 01:06Z) |
| ap-northeast-2 | 369 | 58% | 6.4 | 9 (10-25 01:06Z) |
| ap-south-1 | 369 | 2% | 1.8 | 9 (10-25 01:06Z) |
| ap-southeast-2 | 369 | 1% | 1.1 | 1 (10-25 01:06Z) |
| ap-southeast-3 | 369 | 26% | 3.5 | 4 (10-25 01:06Z) |
| us-east-1 | 369 | 11% | 2.7 | 9 (10-25 01:06Z) |
| us-east-2 | 369 | 31% | 3.8 | 1 (10-25 01:06Z) |
| us-west-2 | 369 | 11% | 2.3 | 1 (10-25 01:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999911199999999999999991999999999
ap-northeast-1   221293241659122219811212111211112821124999994999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222222222222222111111111111499
ap-southeast-2   111911911111111111111111111111111111111111111111
ap-southeast-3   875186799247488117871136511899115991191911285874
us-east-1        223332219239999991121321121211151232222322199199
us-east-2        111619999991999991199911199111991111911119999991
us-west-2        221121212191192112111111131221951211221222222211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 6 | 5 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 271 | 60% | 6.3 | 9 (10-25 01:06Z) |
| ap-northeast-1 apne1-az1 | 61 | 7% | 1.7 | 1 (10-24 00:37Z) |
| ap-northeast-1 apne1-az4 | 171 | 29% | 3.8 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az1 | 321 | 53% | 6.0 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az3 | 340 | 58% | 6.4 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az4 | 366 | 58% | 6.5 | 9 (10-25 01:06Z) |
| ap-south-1 aps1-az1 | 89 | 1% | 1.5 | 1 (10-23 22:05Z) |
| ap-south-1 aps1-az3 | 118 | 4% | 2.4 | 9 (10-25 01:06Z) |
| ap-southeast-2 apse2-az1 | 59 | 3% | 1.3 | 1 (10-24 00:37Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 248 | 37% | 4.5 | 4 (10-25 01:06Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 117 | 30% | 3.6 | 9 (10-25 01:06Z) |
| us-east-1 use1-az5 | 117 | 29% | 3.5 | 9 (10-25 01:06Z) |
| us-east-1 use1-az6 | 85 | 26% | 3.3 | 9 (10-25 01:06Z) |
| us-east-2 use2-az1 | 152 | 45% | 4.9 | 9 (10-24 23:07Z) |
| us-east-2 use2-az2 | 195 | 50% | 5.3 | 9 (10-24 23:07Z) |
| us-east-2 use2-az3 | 224 | 48% | 5.3 | 9 (10-24 23:07Z) |
| us-west-2 usw2-az1 | 130 | 26% | 3.5 | 1 (10-22 15:10Z) |
| us-west-2 usw2-az2 | 81 | 22% | 3.1 | 1 (10-24 00:37Z) |
| us-west-2 usw2-az3 | 136 | 21% | 3.2 | 1 (10-24 05:43Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 369 | 59% | 6.5 | 9 (10-25 01:06Z) |
| ap-northeast-1 | 369 | 73% | 7.2 | 9 (10-25 01:06Z) |
| ap-northeast-2 | 369 | 100% | 9.0 | 9 (10-25 01:06Z) |
| ap-south-1 | 369 | 63% | 6.5 | 9 (10-25 01:06Z) |
| ap-southeast-2 | 369 | 19% | 3.2 | 9 (10-25 01:06Z) |
| ap-southeast-3 | 369 | 26% | 3.5 | 4 (10-25 01:06Z) |
| us-east-1 | 369 | 70% | 6.5 | 9 (10-25 01:06Z) |
| us-east-2 | 369 | 70% | 6.9 | 1 (10-25 01:06Z) |
| us-west-2 | 369 | 52% | 5.7 | 4 (10-25 01:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999329912399923999239992399999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999929999222822999929999919999999999
ap-southeast-2   119999999999991119111111111111111111111111119199
ap-southeast-3   875186799247488117871136511899115991191911285874
us-east-1        465999999999999994645634443643392465645659999999
us-east-2        113999999999999992399952999129997221952269999991
us-west-2        544399999999999995343943391453999333454534599954
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 229 | 76% | 7.6 | 9 (10-25 01:06Z) |
| ap-east-1 ape1-az2 | 191 | 79% | 7.7 | 9 (10-24 20:42Z) |
| ap-east-1 ape1-az3 | 199 | 78% | 7.7 | 9 (10-25 01:06Z) |
| ap-northeast-1 apne1-az1 | 167 | 93% | 8.6 | 9 (10-24 23:07Z) |
| ap-northeast-1 apne1-az2 | 113 | 76% | 7.5 | 9 (10-25 01:06Z) |
| ap-northeast-1 apne1-az4 | 211 | 99% | 8.9 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az1 | 294 | 100% | 9.0 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az2 | 77 | 79% | 7.7 | 9 (10-24 10:49Z) |
| ap-northeast-2 apne2-az3 | 317 | 100% | 9.0 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az4 | 225 | 79% | 7.7 | 9 (10-25 01:06Z) |
| ap-south-1 aps1-az1 | 128 | 83% | 8.0 | 9 (10-24 23:07Z) |
| ap-south-1 aps1-az2 | 141 | 74% | 7.4 | 9 (10-25 01:06Z) |
| ap-south-1 aps1-az3 | 152 | 88% | 8.3 | 9 (10-24 23:07Z) |
| ap-southeast-2 apse2-az1 | 32 | 69% | 7.1 | 9 (10-24 18:04Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 45 | 71% | 7.2 | 9 (10-24 23:07Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 90 | 100% | 9.0 | 9 (10-25 01:06Z) |
| us-east-1 use1-az4 | 109 | 94% | 8.6 | 9 (10-24 23:07Z) |
| us-east-1 use1-az5 | 76 | 97% | 8.8 | 9 (10-24 23:07Z) |
| us-east-1 use1-az6 | 94 | 96% | 8.7 | 9 (10-25 01:06Z) |
| us-east-2 use2-az1 | 126 | 98% | 8.9 | 9 (10-24 14:27Z) |
| us-east-2 use2-az2 | 166 | 99% | 8.9 | 9 (10-24 10:49Z) |
| us-east-2 use2-az3 | 165 | 95% | 8.7 | 9 (10-24 23:07Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 75 | 96% | 8.7 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az3 | 94 | 94% | 8.6 | 2 (10-23 04:37Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710900 | 2026-10-25T01:06:26Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-25T01:06:26Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.752800 | 2026-10-25T01:06:26Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.937900 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588400 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582800 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568200 | 2026-10-25T01:06:26Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-25T01:06:26Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.534700 | 2026-10-25T01:06:26Z |
| ap-south-1 | ap-south-1a | Windows | 0.405200 | 2026-10-25T01:06:26Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.709700 | 2026-10-25T01:06:26Z |
| ap-south-1 | ap-south-1b | Windows | 0.392600 | 2026-10-25T01:06:26Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.667900 | 2026-10-25T01:06:26Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.470600 | 2026-10-25T01:06:26Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655900 | 2026-10-25T01:06:26Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.543400 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.591500 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.439300 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.486200 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.501900 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.518000 | 2026-10-25T01:06:26Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.573100 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550000 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2b | Windows | 0.638100 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546500 | 2026-10-25T01:06:26Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.549700 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2a | Windows | 0.317000 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.567600 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2b | Windows | 0.330400 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.539100 | 2026-10-25T01:06:26Z |
| us-west-2 | us-west-2c | Windows | 0.316700 | 2026-10-25T01:06:26Z |
