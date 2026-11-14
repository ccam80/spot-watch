# Spot placement score log

Generated 2026-11-14 03:05 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 533 | 48% | 5.2 | 1 (11-14 03:05Z) |
| ap-northeast-1 | 533 | 16% | 2.7 | 9 (11-14 03:05Z) |
| ap-northeast-2 | 533 | 68% | 7.0 | 1 (11-14 03:05Z) |
| ap-south-1 | 533 | 3% | 1.7 | 1 (11-14 03:05Z) |
| ap-southeast-2 | 533 | 1% | 1.0 | 1 (11-14 03:05Z) |
| ap-southeast-3 | 533 | 24% | 3.1 | 1 (11-14 03:05Z) |
| us-east-1 | 533 | 10% | 2.6 | 2 (11-14 03:05Z) |
| us-east-2 | 533 | 30% | 3.6 | 1 (11-14 03:05Z) |
| us-west-2 | 533 | 9% | 2.1 | 1 (11-14 03:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999991919111129911191999919998199191219111111111
ap-northeast-1   819511911911122112111191999199112111115111211299
ap-northeast-2   999999999929999999999999999999999999919111111111
ap-south-1       116981111112111222221222113119111122111111111111
ap-southeast-2   111111111111171111111111111111111111111111111111
ap-southeast-3   313861811111111113111111111131111111113111111111
us-east-1        129999121123333322322132222223292933224232333442
us-east-2        699999911912111911111119999199991111111111111111
us-west-2        117111211222111911111229221112111112122211121221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
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
| ap-east-1 ape1-az2 | 390 | 66% | 6.6 | 1 (11-13 16:10Z) |
| ap-northeast-1 apne1-az1 | 125 | 10% | 1.9 | 1 (11-14 03:05Z) |
| ap-northeast-1 apne1-az4 | 244 | 26% | 3.5 | 3 (11-14 03:05Z) |
| ap-northeast-2 apne2-az1 | 455 | 63% | 6.6 | 1 (11-13 22:31Z) |
| ap-northeast-2 apne2-az3 | 492 | 68% | 7.0 | 1 (11-14 03:05Z) |
| ap-northeast-2 apne2-az4 | 520 | 70% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 156 | 1% | 1.3 | 1 (11-14 03:05Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 110 | 3% | 1.2 | 1 (11-14 03:05Z) |
| ap-southeast-2 apse2-az2 | 76 | 0% | 1.0 | 1 (11-14 03:05Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 324 | 37% | 4.3 | 1 (11-14 03:05Z) |
| us-east-1 use1-az1 | 112 | 0% | 1.1 | 1 (11-13 22:31Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 170 | 22% | 2.9 | 1 (11-13 22:31Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 130 | 24% | 3.0 | 1 (11-14 03:05Z) |
| us-east-2 use2-az1 | 232 | 42% | 4.5 | 1 (11-14 03:05Z) |
| us-east-2 use2-az2 | 269 | 51% | 5.3 | 1 (11-14 03:05Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 204 | 17% | 2.7 | 1 (11-13 22:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 533 | 71% | 7.3 | 9 (11-14 03:05Z) |
| ap-northeast-1 | 533 | 72% | 7.0 | 9 (11-14 03:05Z) |
| ap-northeast-2 | 533 | 100% | 9.0 | 9 (11-14 03:05Z) |
| ap-south-1 | 533 | 60% | 6.1 | 1 (11-14 03:05Z) |
| ap-southeast-2 | 533 | 26% | 3.6 | 3 (11-14 03:05Z) |
| ap-southeast-3 | 533 | 24% | 3.1 | 1 (11-14 03:05Z) |
| us-east-1 | 533 | 72% | 6.5 | 9 (11-14 03:05Z) |
| us-east-2 | 533 | 68% | 6.7 | 9 (11-14 03:05Z) |
| us-west-2 | 533 | 51% | 5.6 | 2 (11-14 03:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999992999992199199229999999999939229929928942999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999991191129119229921992179119913922911111191111
ap-southeast-2   919911111911191991199999999199119119119919911913
ap-southeast-3   313861811111111113111111111131111111113111111111
us-east-1        999999452346976555795799999999995996699689669789
us-east-2        999999919919912911191199999999991199199199999999
us-west-2        999944924454342949441959559999994943349334341942
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 7 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 344 | 84% | 8.1 | 9 (11-14 03:05Z) |
| ap-east-1 ape1-az2 | 309 | 87% | 8.2 | 9 (11-13 22:31Z) |
| ap-east-1 ape1-az3 | 341 | 87% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az1 | 214 | 95% | 8.7 | 9 (11-13 16:10Z) |
| ap-northeast-1 apne1-az2 | 197 | 86% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az4 | 277 | 99% | 8.9 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az1 | 432 | 100% | 9.0 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az2 | 116 | 86% | 8.1 | 9 (11-13 22:31Z) |
| ap-northeast-2 apne2-az3 | 450 | 100% | 9.0 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az4 | 351 | 87% | 8.2 | 9 (11-14 03:05Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 152 | 91% | 8.4 | 9 (11-13 07:49Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 134 | 93% | 8.5 | 9 (11-13 07:49Z) |
| us-east-2 use2-az1 | 189 | 99% | 8.9 | 9 (11-14 03:05Z) |
| us-east-2 use2-az2 | 209 | 99% | 8.9 | 9 (11-14 03:05Z) |
| us-east-2 use2-az3 | 235 | 97% | 8.7 | 9 (11-14 03:05Z) |
| us-west-2 usw2-az1 | 98 | 98% | 8.8 | 9 (11-13 16:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 138 | 88% | 8.1 | 9 (11-13 16:10Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707000 | 2026-11-14T03:05:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-14T03:05:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.708600 | 2026-11-14T03:05:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584200 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.606100 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.583400 | 2026-11-14T03:05:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-14T03:05:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.627300 | 2026-11-14T03:05:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.391600 | 2026-11-14T03:05:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.596400 | 2026-11-14T03:05:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.379800 | 2026-11-14T03:05:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.621600 | 2026-11-14T03:05:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492300 | 2026-11-14T03:05:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.563500 | 2026-11-14T03:05:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.540900 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.805400 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.758300 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.568100 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.564300 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509000 | 2026-11-14T03:05:44Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548500 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.567900 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549100 | 2026-11-14T03:05:44Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.619700 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2a | Windows | 0.333600 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579900 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2b | Windows | 0.293500 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.597000 | 2026-11-14T03:05:44Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-14T03:05:44Z |
