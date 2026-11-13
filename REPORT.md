# Spot placement score log

Generated 2026-11-13 07:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 530 | 48% | 5.2 | 1 (11-13 07:49Z) |
| ap-northeast-1 | 530 | 16% | 2.7 | 1 (11-13 07:49Z) |
| ap-northeast-2 | 530 | 68% | 7.1 | 1 (11-13 07:49Z) |
| ap-south-1 | 530 | 3% | 1.7 | 1 (11-13 07:49Z) |
| ap-southeast-2 | 530 | 1% | 1.0 | 1 (11-13 07:49Z) |
| ap-southeast-3 | 530 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 | 530 | 10% | 2.6 | 3 (11-13 07:49Z) |
| us-east-2 | 530 | 30% | 3.6 | 1 (11-13 07:49Z) |
| us-west-2 | 530 | 9% | 2.1 | 1 (11-13 07:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991919111129911191999919998199191219111111
ap-northeast-1   788819511911911122112111191999199112111115111211
ap-northeast-2   999999999999929999999999999999999999999919111111
ap-south-1       111116981111112111222221222113119111122111111111
ap-southeast-2   111111111111111171111111111111111111111111111111
ap-southeast-3   397313861811111111113111111111131111111113111111
us-east-1        111129999121123333322322132222223292933224232333
us-east-2        119699999911912111911111119999199991111111111111
us-west-2        111117111211222111911111229221112111112122211121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 168 | 5% | 1.5 | 1 (11-13 07:49Z) |
| ap-east-1 ape1-az2 | 389 | 66% | 6.6 | 1 (11-13 00:11Z) |
| ap-northeast-1 apne1-az1 | 122 | 10% | 1.9 | 1 (11-12 02:52Z) |
| ap-northeast-1 apne1-az4 | 242 | 26% | 3.5 | 1 (11-13 07:49Z) |
| ap-northeast-2 apne2-az1 | 454 | 63% | 6.6 | 1 (11-13 00:11Z) |
| ap-northeast-2 apne2-az3 | 489 | 69% | 7.0 | 1 (11-13 07:49Z) |
| ap-northeast-2 apne2-az4 | 520 | 70% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 154 | 1% | 1.3 | 1 (11-12 02:52Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 108 | 3% | 1.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 apse2-az2 | 74 | 0% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 322 | 38% | 4.3 | 1 (11-12 02:52Z) |
| us-east-1 use1-az1 | 110 | 0% | 1.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 168 | 23% | 3.0 | 1 (11-13 07:49Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 128 | 24% | 3.0 | 1 (11-12 10:55Z) |
| us-east-2 use2-az1 | 229 | 42% | 4.6 | 1 (11-13 07:49Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 124 | 17% | 2.5 | 1 (11-12 02:52Z) |
| us-west-2 usw2-az3 | 203 | 17% | 2.7 | 1 (11-13 07:49Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 530 | 71% | 7.3 | 9 (11-13 07:49Z) |
| ap-northeast-1 | 530 | 72% | 7.0 | 2 (11-13 07:49Z) |
| ap-northeast-2 | 530 | 100% | 9.0 | 9 (11-13 07:49Z) |
| ap-south-1 | 530 | 61% | 6.2 | 1 (11-13 07:49Z) |
| ap-southeast-2 | 530 | 26% | 3.6 | 1 (11-13 07:49Z) |
| ap-southeast-3 | 530 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 | 530 | 72% | 6.5 | 9 (11-13 07:49Z) |
| us-east-2 | 530 | 67% | 6.6 | 9 (11-13 07:49Z) |
| us-west-2 | 530 | 51% | 5.6 | 1 (11-13 07:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999992999992199199229999999999939229929928942
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999991191129119229921992179119913922911111191
ap-southeast-2   999919911111911191991199999999199119119119919911
ap-southeast-3   397313861811111111113111111111131111111113111111
us-east-1        999999999452346976555795799999999995996699689669
us-east-2        199999999919919912911191199999999991199199199999
us-west-2        999999944924454342949441959559999994943349334341
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
| ap-east-1 ape1-az1 | 341 | 84% | 8.0 | 9 (11-13 07:49Z) |
| ap-east-1 ape1-az2 | 307 | 87% | 8.2 | 9 (11-13 07:49Z) |
| ap-east-1 ape1-az3 | 339 | 87% | 8.2 | 9 (11-13 07:49Z) |
| ap-northeast-1 apne1-az1 | 213 | 95% | 8.7 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az2 | 195 | 86% | 8.2 | 9 (11-12 18:50Z) |
| ap-northeast-1 apne1-az4 | 275 | 99% | 8.9 | 9 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 430 | 100% | 9.0 | 8 (11-13 07:49Z) |
| ap-northeast-2 apne2-az2 | 115 | 86% | 8.1 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az3 | 447 | 100% | 9.0 | 8 (11-13 07:49Z) |
| ap-northeast-2 apne2-az4 | 348 | 86% | 8.2 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 71 | 86% | 8.1 | 9 (11-12 10:55Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 152 | 91% | 8.4 | 9 (11-13 07:49Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 134 | 93% | 8.5 | 9 (11-13 07:49Z) |
| us-east-2 use2-az1 | 187 | 99% | 8.9 | 9 (11-13 07:49Z) |
| us-east-2 use2-az2 | 207 | 99% | 8.9 | 9 (11-13 07:49Z) |
| us-east-2 use2-az3 | 233 | 97% | 8.7 | 9 (11-13 07:49Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707500 | 2026-11-13T07:49:53Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-13T07:49:53Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.707800 | 2026-11-13T07:49:53Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580600 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.598500 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.582700 | 2026-11-13T07:49:53Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-13T07:49:53Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.601200 | 2026-11-13T07:49:53Z |
| ap-south-1 | ap-south-1a | Windows | 0.393600 | 2026-11-13T07:49:53Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.563800 | 2026-11-13T07:49:53Z |
| ap-south-1 | ap-south-1b | Windows | 0.374800 | 2026-11-13T07:49:53Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.595300 | 2026-11-13T07:49:53Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.491100 | 2026-11-13T07:49:53Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.588200 | 2026-11-13T07:49:53Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.538600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.750400 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.727900 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.566600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.530400 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.511400 | 2026-11-13T07:49:53Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549400 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551800 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548400 | 2026-11-13T07:49:53Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.613600 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2a | Windows | 0.327100 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.600100 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2b | Windows | 0.297100 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.603000 | 2026-11-13T07:49:53Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-13T07:49:53Z |
