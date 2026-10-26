# Spot placement score log

Generated 2026-10-26 12:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 377 | 45% | 5.0 | 9 (10-26 12:49Z) |
| ap-northeast-1 | 377 | 17% | 2.9 | 1 (10-26 12:49Z) |
| ap-northeast-2 | 377 | 59% | 6.5 | 9 (10-26 12:49Z) |
| ap-south-1 | 377 | 3% | 1.8 | 1 (10-26 12:49Z) |
| ap-southeast-2 | 377 | 1% | 1.1 | 1 (10-26 12:49Z) |
| ap-southeast-3 | 377 | 27% | 3.5 | 2 (10-26 12:49Z) |
| us-east-1 | 377 | 12% | 2.8 | 9 (10-26 12:49Z) |
| us-east-2 | 377 | 32% | 3.9 | 9 (10-26 12:49Z) |
| us-west-2 | 377 | 11% | 2.3 | 1 (10-26 12:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999991119999999999999999199999999999999999
ap-northeast-1   165912221981121211121111282112499999499991929211
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222222211111111111149991116911
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   924748811787113651189911599119191128587428988612
us-east-1        923999999112132112121115123222232219919939972999
us-east-2        999199999119991119911199111191111999999193991999
us-west-2        219119211211111113122195121122122222221191919111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 279 | 61% | 6.4 | 9 (10-26 12:49Z) |
| ap-northeast-1 apne1-az1 | 62 | 6% | 1.7 | 1 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 174 | 30% | 3.9 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az1 | 328 | 53% | 6.0 | 4 (10-26 12:49Z) |
| ap-northeast-2 apne2-az3 | 348 | 59% | 6.4 | 9 (10-26 12:49Z) |
| ap-northeast-2 apne2-az4 | 373 | 59% | 6.5 | 9 (10-26 12:49Z) |
| ap-south-1 aps1-az1 | 90 | 1% | 1.5 | 1 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 120 | 6% | 2.5 | 9 (10-26 00:11Z) |
| ap-southeast-2 apse2-az1 | 61 | 3% | 1.3 | 1 (10-26 12:49Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 254 | 38% | 4.5 | 2 (10-26 12:49Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 118 | 31% | 3.6 | 9 (10-26 06:02Z) |
| us-east-1 use1-az5 | 121 | 31% | 3.7 | 9 (10-26 06:02Z) |
| us-east-1 use1-az6 | 89 | 29% | 3.5 | 9 (10-26 12:49Z) |
| us-east-2 use2-az1 | 156 | 47% | 5.0 | 9 (10-26 12:49Z) |
| us-east-2 use2-az2 | 201 | 51% | 5.4 | 9 (10-26 12:49Z) |
| us-east-2 use2-az3 | 231 | 49% | 5.3 | 9 (10-26 12:49Z) |
| us-west-2 usw2-az1 | 132 | 27% | 3.5 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az2 | 84 | 24% | 3.2 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az3 | 140 | 22% | 3.3 | 4 (10-25 21:41Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 377 | 59% | 6.6 | 9 (10-26 12:49Z) |
| ap-northeast-1 | 377 | 74% | 7.2 | 9 (10-26 12:49Z) |
| ap-northeast-2 | 377 | 100% | 9.0 | 9 (10-26 12:49Z) |
| ap-south-1 | 377 | 64% | 6.5 | 1 (10-26 12:49Z) |
| ap-southeast-2 | 377 | 20% | 3.2 | 1 (10-26 12:49Z) |
| ap-southeast-3 | 377 | 27% | 3.5 | 2 (10-26 12:49Z) |
| us-east-1 | 377 | 71% | 6.6 | 9 (10-26 12:49Z) |
| us-east-2 | 377 | 71% | 6.9 | 9 (10-26 12:49Z) |
| us-west-2 | 377 | 53% | 5.8 | 9 (10-26 12:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999932991239992399923999239999999999999999919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999992999922282299992999991999999999999999991
ap-southeast-2   999999111911111111111111111111111111919999991111
ap-southeast-3   924748811787113651189911599119191128587428988612
us-east-1        999999999464563444364339246564565999999999999999
us-east-2        999999999239995299912999722195226999999198993999
us-west-2        999999999534394339145399933345453459995499999349
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 8 | 8 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 232 | 77% | 7.6 | 9 (10-26 12:49Z) |
| ap-east-1 ape1-az2 | 194 | 79% | 7.7 | 9 (10-26 00:11Z) |
| ap-east-1 ape1-az3 | 202 | 78% | 7.7 | 9 (10-26 12:49Z) |
| ap-northeast-1 apne1-az1 | 168 | 93% | 8.6 | 9 (10-25 06:03Z) |
| ap-northeast-1 apne1-az2 | 117 | 77% | 7.6 | 9 (10-26 12:49Z) |
| ap-northeast-1 apne1-az4 | 213 | 99% | 8.9 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az1 | 300 | 100% | 9.0 | 9 (10-26 12:49Z) |
| ap-northeast-2 apne2-az2 | 78 | 79% | 7.7 | 9 (10-25 21:41Z) |
| ap-northeast-2 apne2-az3 | 323 | 100% | 9.0 | 9 (10-26 12:49Z) |
| ap-northeast-2 apne2-az4 | 229 | 79% | 7.8 | 9 (10-26 12:49Z) |
| ap-south-1 aps1-az1 | 131 | 83% | 8.0 | 9 (10-26 06:02Z) |
| ap-south-1 aps1-az2 | 146 | 75% | 7.5 | 9 (10-26 06:02Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 113 | 95% | 8.6 | 9 (10-26 12:49Z) |
| us-east-1 use1-az5 | 80 | 98% | 8.8 | 9 (10-26 06:02Z) |
| us-east-1 use1-az6 | 99 | 96% | 8.7 | 9 (10-26 12:49Z) |
| us-east-2 use2-az1 | 129 | 98% | 8.9 | 9 (10-26 12:49Z) |
| us-east-2 use2-az2 | 166 | 99% | 8.9 | 9 (10-24 10:49Z) |
| us-east-2 use2-az3 | 169 | 95% | 8.7 | 9 (10-26 12:49Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703200 | 2026-10-26T12:49:29Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-26T12:49:29Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.776500 | 2026-10-26T12:49:29Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.958400 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587700 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.584900 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-10-26T12:49:29Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-26T12:49:29Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.536600 | 2026-10-26T12:49:29Z |
| ap-south-1 | ap-south-1a | Windows | 0.431900 | 2026-10-26T12:49:29Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.680900 | 2026-10-26T12:49:29Z |
| ap-south-1 | ap-south-1b | Windows | 0.418000 | 2026-10-26T12:49:29Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.675300 | 2026-10-26T12:49:29Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501700 | 2026-10-26T12:49:29Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660700 | 2026-10-26T12:49:29Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.553400 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.592600 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.446400 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.475500 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.499300 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.514900 | 2026-10-26T12:49:29Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.553300 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2a | Windows | 0.639700 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547800 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545600 | 2026-10-26T12:49:29Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553900 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2a | Windows | 0.319500 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.580600 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2b | Windows | 0.328800 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547500 | 2026-10-26T12:49:29Z |
| us-west-2 | us-west-2c | Windows | 0.318400 | 2026-10-26T12:49:29Z |
