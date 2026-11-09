# Spot placement score log

Generated 2026-11-09 17:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 518 | 49% | 5.3 | 9 (11-09 17:23Z) |
| ap-northeast-1 | 518 | 16% | 2.7 | 2 (11-09 17:23Z) |
| ap-northeast-2 | 518 | 69% | 7.1 | 9 (11-09 17:23Z) |
| ap-south-1 | 518 | 3% | 1.7 | 1 (11-09 17:23Z) |
| ap-southeast-2 | 518 | 1% | 1.1 | 1 (11-09 17:23Z) |
| ap-southeast-3 | 518 | 25% | 3.2 | 1 (11-09 17:23Z) |
| us-east-1 | 518 | 10% | 2.6 | 2 (11-09 17:23Z) |
| us-east-2 | 518 | 31% | 3.7 | 1 (11-09 17:23Z) |
| us-west-2 | 518 | 9% | 2.1 | 1 (11-09 17:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991119999999991919111129911191999919998199
ap-northeast-1   112118791114788819511911911122112111191999199112
ap-northeast-2   999999991999999999999999929999999999999999999999
ap-south-1       111111111111111116981111112111222221222113119111
ap-southeast-2   111111111111111111111111111171111111111111111111
ap-southeast-3   115512541118397313861811111111113111111111131111
us-east-1        222212211111111129999121123333322322132222223292
us-east-2        991112111999119699999911912111911111119999199991
us-west-2        111941311111111117111211222111911111229221112111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 163 | 6% | 1.5 | 1 (11-08 07:12Z) |
| ap-east-1 ape1-az2 | 381 | 67% | 6.7 | 9 (11-09 17:23Z) |
| ap-northeast-1 apne1-az1 | 119 | 10% | 1.9 | 1 (11-09 06:07Z) |
| ap-northeast-1 apne1-az4 | 233 | 27% | 3.6 | 1 (11-09 17:23Z) |
| ap-northeast-2 apne2-az1 | 445 | 63% | 6.6 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az3 | 482 | 69% | 7.0 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az4 | 511 | 70% | 7.2 | 9 (11-09 17:23Z) |
| ap-south-1 aps1-az1 | 151 | 1% | 1.4 | 5 (11-08 19:34Z) |
| ap-south-1 aps1-az3 | 145 | 7% | 2.4 | 1 (11-09 17:23Z) |
| ap-southeast-2 apse2-az1 | 103 | 3% | 1.3 | 1 (11-09 17:23Z) |
| ap-southeast-2 apse2-az2 | 71 | 0% | 1.0 | 1 (11-09 06:07Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 319 | 38% | 4.3 | 1 (11-09 06:07Z) |
| us-east-1 use1-az1 | 107 | 0% | 1.1 | 1 (11-09 06:07Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 164 | 25% | 3.2 | 1 (11-09 17:23Z) |
| us-east-1 use1-az6 | 124 | 24% | 3.0 | 1 (11-07 20:49Z) |
| us-east-2 use2-az1 | 225 | 43% | 4.6 | 1 (11-09 06:07Z) |
| us-east-2 use2-az2 | 265 | 51% | 5.3 | 9 (11-08 23:39Z) |
| us-east-2 use2-az3 | 295 | 47% | 5.1 | 1 (11-09 17:23Z) |
| us-west-2 usw2-az1 | 162 | 23% | 3.1 | 1 (11-09 17:23Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 518 | 70% | 7.2 | 9 (11-09 17:23Z) |
| ap-northeast-1 | 518 | 73% | 7.0 | 9 (11-09 17:23Z) |
| ap-northeast-2 | 518 | 100% | 9.0 | 9 (11-09 17:23Z) |
| ap-south-1 | 518 | 61% | 6.2 | 3 (11-09 17:23Z) |
| ap-southeast-2 | 518 | 26% | 3.5 | 9 (11-09 17:23Z) |
| ap-southeast-3 | 518 | 25% | 3.2 | 1 (11-09 17:23Z) |
| us-east-1 | 518 | 71% | 6.4 | 5 (11-09 17:23Z) |
| us-east-2 | 518 | 67% | 6.6 | 1 (11-09 17:23Z) |
| us-west-2 | 518 | 52% | 5.7 | 4 (11-09 17:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999992999992199199229999999999939
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999991191129119229921992179119913
ap-southeast-2   131999999999999919911111911191991199999999199119
ap-southeast-3   115512541118397313861811111111113111111111131111
us-east-1        999999932299999999999452346976555795799999999995
us-east-2        999999992999199999999919919912911191199999999991
us-west-2        499954999299999999944924454342949441959559999994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 330 | 84% | 8.0 | 9 (11-09 17:23Z) |
| ap-east-1 ape1-az2 | 296 | 86% | 8.2 | 9 (11-09 06:07Z) |
| ap-east-1 ape1-az3 | 328 | 87% | 8.2 | 9 (11-09 17:23Z) |
| ap-northeast-1 apne1-az1 | 211 | 95% | 8.7 | 9 (11-09 17:23Z) |
| ap-northeast-1 apne1-az2 | 190 | 86% | 8.1 | 9 (11-09 17:23Z) |
| ap-northeast-1 apne1-az4 | 271 | 99% | 8.9 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az1 | 419 | 100% | 9.0 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az2 | 113 | 86% | 8.1 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az3 | 435 | 100% | 9.0 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az4 | 339 | 86% | 8.2 | 9 (11-09 17:23Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 197 | 90% | 8.4 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az1 | 67 | 85% | 8.1 | 9 (11-09 17:23Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 79 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 112 | 100% | 9.0 | 9 (11-09 06:07Z) |
| us-east-1 use1-az4 | 147 | 92% | 8.4 | 9 (11-09 06:07Z) |
| us-east-1 use1-az5 | 107 | 98% | 8.9 | 9 (11-08 07:12Z) |
| us-east-1 use1-az6 | 131 | 92% | 8.5 | 9 (11-09 06:07Z) |
| us-east-2 use2-az1 | 182 | 99% | 8.9 | 9 (11-08 23:39Z) |
| us-east-2 use2-az2 | 201 | 99% | 8.9 | 9 (11-09 06:07Z) |
| us-east-2 use2-az3 | 228 | 96% | 8.7 | 9 (11-08 23:39Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 96 | 91% | 8.3 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az3 | 136 | 88% | 8.2 | 9 (11-09 06:07Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711300 | 2026-11-09T17:23:41Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-09T17:23:41Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.713700 | 2026-11-09T17:23:41Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.578000 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.592500 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573300 | 2026-11-09T17:23:41Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-09T17:23:41Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548200 | 2026-11-09T17:23:41Z |
| ap-south-1 | ap-south-1a | Windows | 0.414100 | 2026-11-09T17:23:41Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.548500 | 2026-11-09T17:23:41Z |
| ap-south-1 | ap-south-1b | Windows | 0.355900 | 2026-11-09T17:23:41Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.594600 | 2026-11-09T17:23:41Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.498400 | 2026-11-09T17:23:41Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.643700 | 2026-11-09T17:23:41Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530500 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.622200 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.597300 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.499000 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.432000 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.449200 | 2026-11-09T17:23:41Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549300 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549200 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546700 | 2026-11-09T17:23:41Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.543100 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2a | Windows | 0.308100 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.646100 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2b | Windows | 0.311000 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.568100 | 2026-11-09T17:23:41Z |
| us-west-2 | us-west-2c | Windows | 0.296800 | 2026-11-09T17:23:41Z |
