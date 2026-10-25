# Spot placement score log

Generated 2026-10-25 21:41 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 374 | 45% | 5.0 | 9 (10-25 21:41Z) |
| ap-northeast-1 | 374 | 17% | 2.9 | 9 (10-25 21:41Z) |
| ap-northeast-2 | 374 | 58% | 6.5 | 9 (10-25 21:41Z) |
| ap-south-1 | 374 | 3% | 1.8 | 6 (10-25 21:41Z) |
| ap-southeast-2 | 374 | 1% | 1.1 | 1 (10-25 21:41Z) |
| ap-southeast-3 | 374 | 27% | 3.5 | 8 (10-25 21:41Z) |
| us-east-1 | 374 | 12% | 2.7 | 2 (10-25 21:41Z) |
| us-east-2 | 374 | 32% | 3.8 | 1 (10-25 21:41Z) |
| us-west-2 | 374 | 11% | 2.3 | 9 (10-25 21:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999991119999999999999999199999999999999
ap-northeast-1   324165912221981121211121111282112499999499991929
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222222222211111111111149991116
ap-southeast-2   191111111111111111111111111111111111111111111111
ap-southeast-3   679924748811787113651189911599119191128587428988
us-east-1        221923999999112132112121115123222232219919939972
us-east-2        999999199999119991119911199111191111999999193991
us-west-2        121219119211211111113122195121122122222221191919
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
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 2 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 276 | 61% | 6.3 | 9 (10-25 21:41Z) |
| ap-northeast-1 apne1-az1 | 62 | 6% | 1.7 | 1 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 174 | 30% | 3.9 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az1 | 325 | 53% | 6.0 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az3 | 345 | 59% | 6.4 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az4 | 370 | 59% | 6.5 | 9 (10-25 21:41Z) |
| ap-south-1 aps1-az1 | 90 | 1% | 1.5 | 1 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 119 | 5% | 2.4 | 6 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 60 | 3% | 1.3 | 1 (10-25 11:16Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 252 | 38% | 4.5 | 8 (10-25 21:41Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 117 | 30% | 3.6 | 9 (10-25 01:06Z) |
| us-east-1 use1-az5 | 119 | 29% | 3.6 | 9 (10-25 16:03Z) |
| us-east-1 use1-az6 | 86 | 27% | 3.3 | 6 (10-25 18:58Z) |
| us-east-2 use2-az1 | 154 | 46% | 4.9 | 9 (10-25 18:58Z) |
| us-east-2 use2-az2 | 198 | 51% | 5.3 | 9 (10-25 18:58Z) |
| us-east-2 use2-az3 | 228 | 49% | 5.3 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az1 | 132 | 27% | 3.5 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az2 | 84 | 24% | 3.2 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az3 | 140 | 22% | 3.3 | 4 (10-25 21:41Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 374 | 59% | 6.5 | 9 (10-25 21:41Z) |
| ap-northeast-1 | 374 | 74% | 7.2 | 9 (10-25 21:41Z) |
| ap-northeast-2 | 374 | 100% | 9.0 | 9 (10-25 21:41Z) |
| ap-south-1 | 374 | 64% | 6.6 | 9 (10-25 21:41Z) |
| ap-southeast-2 | 374 | 20% | 3.2 | 1 (10-25 21:41Z) |
| ap-southeast-3 | 374 | 27% | 3.5 | 8 (10-25 21:41Z) |
| us-east-1 | 374 | 71% | 6.6 | 9 (10-25 21:41Z) |
| us-east-2 | 374 | 71% | 6.9 | 3 (10-25 21:41Z) |
| us-west-2 | 374 | 53% | 5.8 | 9 (10-25 21:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999932991239992399923999239999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999992999922282299992999991999999999999999
ap-southeast-2   999999999111911111111111111111111111111919999991
ap-southeast-3   679924748811787113651189911599119191128587428988
us-east-1        999999999999464563444364339246564565999999999999
us-east-2        999999999999239995299912999722195226999999198993
us-west-2        999999999999534394339145399933345453459995499999
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
| ap-east-1 ape1-az2 | 193 | 79% | 7.7 | 9 (10-25 21:41Z) |
| ap-east-1 ape1-az3 | 199 | 78% | 7.7 | 9 (10-25 01:06Z) |
| ap-northeast-1 apne1-az1 | 168 | 93% | 8.6 | 9 (10-25 06:03Z) |
| ap-northeast-1 apne1-az2 | 115 | 77% | 7.6 | 9 (10-25 18:58Z) |
| ap-northeast-1 apne1-az4 | 213 | 99% | 8.9 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az1 | 298 | 100% | 9.0 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az2 | 78 | 79% | 7.7 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az3 | 320 | 100% | 9.0 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az4 | 227 | 79% | 7.8 | 9 (10-25 18:58Z) |
| ap-south-1 aps1-az1 | 130 | 83% | 8.0 | 9 (10-25 21:41Z) |
| ap-south-1 aps1-az2 | 144 | 75% | 7.4 | 9 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 93 | 100% | 9.0 | 9 (10-25 21:41Z) |
| us-east-1 use1-az4 | 111 | 95% | 8.6 | 9 (10-25 21:41Z) |
| us-east-1 use1-az5 | 79 | 97% | 8.8 | 9 (10-25 21:41Z) |
| us-east-1 use1-az6 | 96 | 96% | 8.7 | 9 (10-25 16:03Z) |
| us-east-2 use2-az1 | 127 | 98% | 8.9 | 9 (10-25 16:03Z) |
| us-east-2 use2-az2 | 166 | 99% | 8.9 | 9 (10-24 10:49Z) |
| us-east-2 use2-az3 | 167 | 95% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az1 | 82 | 98% | 8.8 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 97 | 94% | 8.6 | 9 (10-25 21:41Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.705200 | 2026-10-25T21:41:15Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-25T21:41:15Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.776400 | 2026-10-25T21:41:15Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.959400 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588600 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585000 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-10-25T21:41:15Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-25T21:41:15Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.532700 | 2026-10-25T21:41:15Z |
| ap-south-1 | ap-south-1a | Windows | 0.431700 | 2026-10-25T21:41:15Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.698100 | 2026-10-25T21:41:15Z |
| ap-south-1 | ap-south-1b | Windows | 0.412800 | 2026-10-25T21:41:15Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.668200 | 2026-10-25T21:41:15Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.477600 | 2026-10-25T21:41:15Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.654200 | 2026-10-25T21:41:15Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550000 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.597200 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.444600 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.479000 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.506300 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.518100 | 2026-10-25T21:41:15Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.556300 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2a | Windows | 0.640000 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548100 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2b | Windows | 0.637900 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-25T21:41:15Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.549100 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2a | Windows | 0.317400 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.566600 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2b | Windows | 0.330700 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.542600 | 2026-10-25T21:41:15Z |
| us-west-2 | us-west-2c | Windows | 0.317200 | 2026-10-25T21:41:15Z |
