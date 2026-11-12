# Spot placement score log

Generated 2026-11-12 10:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 527 | 49% | 5.2 | 1 (11-12 10:55Z) |
| ap-northeast-1 | 527 | 16% | 2.7 | 1 (11-12 10:55Z) |
| ap-northeast-2 | 527 | 69% | 7.1 | 1 (11-12 10:55Z) |
| ap-south-1 | 527 | 3% | 1.7 | 1 (11-12 10:55Z) |
| ap-southeast-2 | 527 | 1% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 | 527 | 24% | 3.2 | 1 (11-12 10:55Z) |
| us-east-1 | 527 | 10% | 2.6 | 2 (11-12 10:55Z) |
| us-east-2 | 527 | 30% | 3.6 | 1 (11-12 10:55Z) |
| us-west-2 | 527 | 9% | 2.1 | 1 (11-12 10:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119999999991919111129911191999919998199191219111
ap-northeast-1   114788819511911911122112111191999199112111115111
ap-northeast-2   999999999999999929999999999999999999999999919111
ap-south-1       111111116981111112111222221222113119111122111111
ap-southeast-2   111111111111111111171111111111111111111111111111
ap-southeast-3   118397313861811111111113111111111131111111113111
us-east-1        111111129999121123333322322132222223292933224232
us-east-2        999119699999911912111911111119999199991111111111
us-west-2        111111117111211222111911111229221112111112122211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 165 | 5% | 1.5 | 1 (11-12 10:55Z) |
| ap-east-1 ape1-az2 | 387 | 66% | 6.6 | 1 (11-12 10:55Z) |
| ap-northeast-1 apne1-az1 | 122 | 10% | 1.9 | 1 (11-12 02:52Z) |
| ap-northeast-1 apne1-az4 | 239 | 26% | 3.5 | 1 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 452 | 63% | 6.6 | 1 (11-12 10:55Z) |
| ap-northeast-2 apne2-az3 | 488 | 69% | 7.0 | 1 (11-12 10:55Z) |
| ap-northeast-2 apne2-az4 | 518 | 70% | 7.2 | 1 (11-11 21:20Z) |
| ap-south-1 aps1-az1 | 154 | 1% | 1.3 | 1 (11-12 02:52Z) |
| ap-south-1 aps1-az3 | 151 | 7% | 2.3 | 1 (11-11 21:20Z) |
| ap-southeast-2 apse2-az1 | 108 | 3% | 1.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 apse2-az2 | 74 | 0% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 apse3-az1 | 91 | 0% | 1.0 | 1 (11-11 21:20Z) |
| ap-southeast-3 apse3-az3 | 322 | 38% | 4.3 | 1 (11-12 02:52Z) |
| us-east-1 use1-az1 | 109 | 0% | 1.1 | 1 (11-12 10:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 167 | 23% | 3.0 | 1 (11-12 10:55Z) |
| us-east-1 use1-az5 | 169 | 25% | 3.1 | 1 (11-11 21:20Z) |
| us-east-1 use1-az6 | 128 | 24% | 3.0 | 1 (11-12 10:55Z) |
| us-east-2 use2-az1 | 228 | 43% | 4.6 | 1 (11-12 10:55Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 298 | 47% | 5.1 | 1 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 167 | 22% | 3.1 | 1 (11-11 21:20Z) |
| us-west-2 usw2-az2 | 124 | 17% | 2.5 | 1 (11-12 02:52Z) |
| us-west-2 usw2-az3 | 202 | 17% | 2.7 | 1 (11-12 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 527 | 71% | 7.3 | 9 (11-12 10:55Z) |
| ap-northeast-1 | 527 | 72% | 7.0 | 8 (11-12 10:55Z) |
| ap-northeast-2 | 527 | 100% | 9.0 | 9 (11-12 10:55Z) |
| ap-south-1 | 527 | 61% | 6.2 | 1 (11-12 10:55Z) |
| ap-southeast-2 | 527 | 26% | 3.6 | 9 (11-12 10:55Z) |
| ap-southeast-3 | 527 | 24% | 3.2 | 1 (11-12 10:55Z) |
| us-east-1 | 527 | 71% | 6.5 | 9 (11-12 10:55Z) |
| us-east-2 | 527 | 67% | 6.6 | 9 (11-12 10:55Z) |
| us-west-2 | 527 | 51% | 5.7 | 4 (11-12 10:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999992999992199199229999999999939229929928
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999991191129119229921992179119913922911111
ap-southeast-2   999999919911111911191991199999999199119119119919
ap-southeast-3   118397313861811111111113111111111131111111113111
us-east-1        299999999999452346976555795799999999995996699689
us-east-2        999199999999919919912911191199999999991199199199
us-west-2        299999999944924454342949441959559999994943349334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 8 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 339 | 84% | 8.0 | 9 (11-12 10:55Z) |
| ap-east-1 ape1-az2 | 304 | 87% | 8.2 | 9 (11-12 10:55Z) |
| ap-east-1 ape1-az3 | 336 | 87% | 8.2 | 9 (11-12 02:52Z) |
| ap-northeast-1 apne1-az1 | 213 | 95% | 8.7 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az2 | 194 | 86% | 8.1 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az4 | 275 | 99% | 8.9 | 9 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 427 | 100% | 9.0 | 9 (11-12 10:55Z) |
| ap-northeast-2 apne2-az2 | 114 | 86% | 8.1 | 9 (11-12 10:55Z) |
| ap-northeast-2 apne2-az3 | 444 | 100% | 9.0 | 9 (11-12 10:55Z) |
| ap-northeast-2 apne2-az4 | 346 | 86% | 8.2 | 9 (11-12 10:55Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 199 | 90% | 8.4 | 9 (11-10 23:11Z) |
| ap-southeast-2 apse2-az1 | 71 | 86% | 8.1 | 9 (11-12 10:55Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 82 | 83% | 7.9 | 9 (11-12 10:55Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 151 | 91% | 8.4 | 9 (11-12 10:55Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 133 | 92% | 8.5 | 9 (11-10 09:39Z) |
| us-east-2 use2-az1 | 184 | 99% | 8.9 | 9 (11-11 05:59Z) |
| us-east-2 use2-az2 | 205 | 99% | 8.9 | 9 (11-12 10:55Z) |
| us-east-2 use2-az3 | 231 | 97% | 8.7 | 9 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708600 | 2026-11-12T10:55:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-12T10:55:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.706200 | 2026-11-12T10:55:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.577000 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.594000 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.580500 | 2026-11-12T10:55:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-12T10:55:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.579500 | 2026-11-12T10:55:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.398800 | 2026-11-12T10:55:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.565700 | 2026-11-12T10:55:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.374800 | 2026-11-12T10:55:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.590800 | 2026-11-12T10:55:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492600 | 2026-11-12T10:55:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.606200 | 2026-11-12T10:55:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519200 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.739000 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.686300 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.564200 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.508100 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.499000 | 2026-11-12T10:55:05Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550300 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551800 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549500 | 2026-11-12T10:55:05Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.573300 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2a | Windows | 0.321100 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.615600 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2b | Windows | 0.299500 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.602100 | 2026-11-12T10:55:05Z |
| us-west-2 | us-west-2c | Windows | 0.285100 | 2026-11-12T10:55:05Z |
