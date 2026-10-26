# Spot placement score log

Generated 2026-10-26 00:11 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 375 | 45% | 5.0 | 9 (10-26 00:11Z) |
| ap-northeast-1 | 375 | 17% | 2.9 | 2 (10-26 00:11Z) |
| ap-northeast-2 | 375 | 58% | 6.5 | 9 (10-26 00:11Z) |
| ap-south-1 | 375 | 3% | 1.9 | 9 (10-26 00:11Z) |
| ap-southeast-2 | 375 | 1% | 1.1 | 1 (10-26 00:11Z) |
| ap-southeast-3 | 375 | 27% | 3.5 | 6 (10-26 00:11Z) |
| us-east-1 | 375 | 12% | 2.7 | 9 (10-26 00:11Z) |
| us-east-2 | 375 | 32% | 3.9 | 9 (10-26 00:11Z) |
| us-west-2 | 375 | 11% | 2.3 | 1 (10-26 00:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999911199999999999999991999999999999999
ap-northeast-1   241659122219811212111211112821124999994999919292
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222222222111111111111499911169
ap-southeast-2   911111111111111111111111111111111111111111111111
ap-southeast-3   799247488117871136511899115991191911285874289886
us-east-1        219239999991121321121211151232222322199199399729
us-east-2        999991999991199911199111991111911119999991939919
us-west-2        212191192112111111131221951211221222222211919191
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 2 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 277 | 61% | 6.3 | 9 (10-26 00:11Z) |
| ap-northeast-1 apne1-az1 | 62 | 6% | 1.7 | 1 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 174 | 30% | 3.9 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az1 | 326 | 53% | 6.0 | 9 (10-26 00:11Z) |
| ap-northeast-2 apne2-az3 | 346 | 59% | 6.4 | 9 (10-26 00:11Z) |
| ap-northeast-2 apne2-az4 | 371 | 59% | 6.5 | 9 (10-26 00:11Z) |
| ap-south-1 aps1-az1 | 90 | 1% | 1.5 | 1 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 120 | 6% | 2.5 | 9 (10-26 00:11Z) |
| ap-southeast-2 apse2-az1 | 60 | 3% | 1.3 | 1 (10-25 11:16Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 253 | 38% | 4.5 | 6 (10-26 00:11Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 117 | 30% | 3.6 | 9 (10-25 01:06Z) |
| us-east-1 use1-az5 | 120 | 30% | 3.6 | 9 (10-26 00:11Z) |
| us-east-1 use1-az6 | 87 | 28% | 3.4 | 9 (10-26 00:11Z) |
| us-east-2 use2-az1 | 154 | 46% | 4.9 | 9 (10-25 18:58Z) |
| us-east-2 use2-az2 | 199 | 51% | 5.4 | 9 (10-26 00:11Z) |
| us-east-2 use2-az3 | 229 | 48% | 5.3 | 4 (10-26 00:11Z) |
| us-west-2 usw2-az1 | 132 | 27% | 3.5 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az2 | 84 | 24% | 3.2 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az3 | 140 | 22% | 3.3 | 4 (10-25 21:41Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 375 | 59% | 6.6 | 9 (10-26 00:11Z) |
| ap-northeast-1 | 375 | 74% | 7.2 | 9 (10-26 00:11Z) |
| ap-northeast-2 | 375 | 100% | 9.0 | 9 (10-26 00:11Z) |
| ap-south-1 | 375 | 64% | 6.6 | 9 (10-26 00:11Z) |
| ap-southeast-2 | 375 | 20% | 3.2 | 1 (10-26 00:11Z) |
| ap-southeast-3 | 375 | 27% | 3.5 | 6 (10-26 00:11Z) |
| us-east-1 | 375 | 71% | 6.6 | 9 (10-26 00:11Z) |
| us-east-2 | 375 | 71% | 6.9 | 9 (10-26 00:11Z) |
| us-west-2 | 375 | 53% | 5.7 | 3 (10-26 00:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999329912399923999239992399999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999929999222822999929999919999999999999999
ap-southeast-2   999999991119111111111111111111111111119199999911
ap-southeast-3   799247488117871136511899115991191911285874289886
us-east-1        999999999994645634443643392465645659999999999999
us-east-2        999999999992399952999129997221952269999991989939
us-west-2        999999999995343943391453999333454534599954999993
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 4 | 4 | 6 | 4 | 7 | 6 | 8 | 8 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 231 | 77% | 7.6 | 9 (10-25 18:58Z) |
| ap-east-1 ape1-az2 | 194 | 79% | 7.7 | 9 (10-26 00:11Z) |
| ap-east-1 ape1-az3 | 200 | 78% | 7.7 | 9 (10-26 00:11Z) |
| ap-northeast-1 apne1-az1 | 168 | 93% | 8.6 | 9 (10-25 06:03Z) |
| ap-northeast-1 apne1-az2 | 116 | 77% | 7.6 | 9 (10-26 00:11Z) |
| ap-northeast-1 apne1-az4 | 213 | 99% | 8.9 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az1 | 298 | 100% | 9.0 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az2 | 78 | 79% | 7.7 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az3 | 321 | 100% | 9.0 | 9 (10-26 00:11Z) |
| ap-northeast-2 apne2-az4 | 228 | 79% | 7.8 | 9 (10-26 00:11Z) |
| ap-south-1 aps1-az1 | 130 | 83% | 8.0 | 9 (10-25 21:41Z) |
| ap-south-1 aps1-az2 | 145 | 75% | 7.4 | 9 (10-26 00:11Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 111 | 95% | 8.6 | 9 (10-25 21:41Z) |
| us-east-1 use1-az5 | 79 | 97% | 8.8 | 9 (10-25 21:41Z) |
| us-east-1 use1-az6 | 97 | 96% | 8.7 | 9 (10-26 00:11Z) |
| us-east-2 use2-az1 | 127 | 98% | 8.9 | 9 (10-25 16:03Z) |
| us-east-2 use2-az2 | 166 | 99% | 8.9 | 9 (10-24 10:49Z) |
| us-east-2 use2-az3 | 167 | 95% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703100 | 2026-10-26T00:11:25Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-26T00:11:25Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.776400 | 2026-10-26T00:11:25Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.959400 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588600 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585000 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-10-26T00:11:25Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-26T00:11:25Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.535900 | 2026-10-26T00:11:25Z |
| ap-south-1 | ap-south-1a | Windows | 0.431700 | 2026-10-26T00:11:25Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.698100 | 2026-10-26T00:11:25Z |
| ap-south-1 | ap-south-1b | Windows | 0.424200 | 2026-10-26T00:11:25Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.661400 | 2026-10-26T00:11:25Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492500 | 2026-10-26T00:11:25Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.654200 | 2026-10-26T00:11:25Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550000 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.600500 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.444600 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.479000 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500900 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509000 | 2026-10-26T00:11:25Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.556300 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2a | Windows | 0.639800 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548100 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2b | Windows | 0.637900 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-26T00:11:25Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.550900 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2a | Windows | 0.318000 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.570700 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2b | Windows | 0.330700 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.542600 | 2026-10-26T00:11:25Z |
| us-west-2 | us-west-2c | Windows | 0.317700 | 2026-10-26T00:11:25Z |
