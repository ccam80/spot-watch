# Spot placement score log

Generated 2026-11-08 19:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 515 | 49% | 5.3 | 8 (11-08 19:34Z) |
| ap-northeast-1 | 515 | 16% | 2.8 | 9 (11-08 19:34Z) |
| ap-northeast-2 | 515 | 69% | 7.1 | 9 (11-08 19:34Z) |
| ap-south-1 | 515 | 3% | 1.7 | 9 (11-08 19:34Z) |
| ap-southeast-2 | 515 | 1% | 1.1 | 1 (11-08 19:34Z) |
| ap-southeast-3 | 515 | 25% | 3.2 | 1 (11-08 19:34Z) |
| us-east-1 | 515 | 10% | 2.6 | 3 (11-08 19:34Z) |
| us-east-2 | 515 | 30% | 3.7 | 9 (11-08 19:34Z) |
| us-west-2 | 515 | 9% | 2.1 | 2 (11-08 19:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119999999991119999999991919111129911191999919998
ap-northeast-1   111112118791114788819511911911122112111191999199
ap-northeast-2   199999999991999999999999999929999999999999999999
ap-south-1       111111111111111111116981111112111222221222113119
ap-southeast-2   111111111111111111111111111111171111111111111111
ap-southeast-3   111115512541118397313861811111111113111111111131
us-east-1        222222212211111111129999121123333322322132222223
us-east-2        111991112111999119699999911912111911111119999199
us-west-2        111111941311111111117111211222111911111229221112
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
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 163 | 6% | 1.5 | 1 (11-08 07:12Z) |
| ap-east-1 ape1-az2 | 379 | 66% | 6.7 | 8 (11-08 19:34Z) |
| ap-northeast-1 apne1-az1 | 117 | 10% | 1.9 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az4 | 232 | 27% | 3.6 | 9 (11-08 19:34Z) |
| ap-northeast-2 apne2-az1 | 442 | 63% | 6.6 | 9 (11-08 19:34Z) |
| ap-northeast-2 apne2-az3 | 480 | 69% | 7.0 | 9 (11-08 19:34Z) |
| ap-northeast-2 apne2-az4 | 508 | 70% | 7.2 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az1 | 151 | 1% | 1.4 | 5 (11-08 19:34Z) |
| ap-south-1 aps1-az3 | 142 | 7% | 2.4 | 8 (11-08 19:34Z) |
| ap-southeast-2 apse2-az1 | 102 | 3% | 1.3 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az2 | 70 | 0% | 1.0 | 1 (11-07 09:56Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 317 | 38% | 4.4 | 3 (11-08 15:03Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 163 | 25% | 3.2 | 1 (11-08 07:12Z) |
| us-east-1 use1-az6 | 124 | 24% | 3.0 | 1 (11-07 20:49Z) |
| us-east-2 use2-az1 | 223 | 43% | 4.6 | 9 (11-08 19:34Z) |
| us-east-2 use2-az2 | 264 | 51% | 5.3 | 9 (11-08 19:34Z) |
| us-east-2 use2-az3 | 292 | 47% | 5.1 | 9 (11-08 19:34Z) |
| us-west-2 usw2-az1 | 161 | 23% | 3.1 | 1 (11-08 07:12Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 515 | 70% | 7.2 | 9 (11-08 19:34Z) |
| ap-northeast-1 | 515 | 73% | 7.0 | 9 (11-08 19:34Z) |
| ap-northeast-2 | 515 | 100% | 9.0 | 9 (11-08 19:34Z) |
| ap-south-1 | 515 | 62% | 6.3 | 9 (11-08 19:34Z) |
| ap-southeast-2 | 515 | 26% | 3.5 | 9 (11-08 19:34Z) |
| ap-southeast-3 | 515 | 25% | 3.2 | 1 (11-08 19:34Z) |
| us-east-1 | 515 | 71% | 6.4 | 9 (11-08 19:34Z) |
| us-east-2 | 515 | 67% | 6.6 | 9 (11-08 19:34Z) |
| us-west-2 | 515 | 52% | 5.7 | 9 (11-08 19:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999992999992199199229999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       979999999999999999999991191129119229921992179119
ap-southeast-2   911131999999999999919911111911191991199999999199
ap-southeast-3   111115512541118397313861811111111113111111111131
us-east-1        999999999932299999999999452346976555795799999999
us-east-2        999999999992999199999999919919912911191199999999
us-west-2        324499954999299999999944924454342949441959559999
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
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 328 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-east-1 ape1-az2 | 295 | 86% | 8.2 | 9 (11-08 19:34Z) |
| ap-east-1 ape1-az3 | 325 | 86% | 8.2 | 9 (11-08 19:34Z) |
| ap-northeast-1 apne1-az1 | 210 | 95% | 8.7 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az2 | 189 | 86% | 8.1 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az4 | 269 | 99% | 8.9 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az1 | 418 | 100% | 9.0 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az2 | 112 | 86% | 8.1 | 9 (11-08 19:34Z) |
| ap-northeast-2 apne2-az3 | 434 | 100% | 9.0 | 9 (11-07 02:43Z) |
| ap-northeast-2 apne2-az4 | 336 | 86% | 8.2 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 197 | 90% | 8.4 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az1 | 66 | 85% | 8.0 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 79 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 111 | 100% | 9.0 | 9 (11-08 19:34Z) |
| us-east-1 use1-az4 | 145 | 92% | 8.4 | 9 (11-08 00:28Z) |
| us-east-1 use1-az5 | 107 | 98% | 8.9 | 9 (11-08 07:12Z) |
| us-east-1 use1-az6 | 129 | 92% | 8.4 | 9 (11-08 07:12Z) |
| us-east-2 use2-az1 | 181 | 99% | 8.9 | 9 (11-08 15:03Z) |
| us-east-2 use2-az2 | 200 | 99% | 8.9 | 9 (11-08 19:34Z) |
| us-east-2 use2-az3 | 227 | 96% | 8.7 | 9 (11-07 20:49Z) |
| us-west-2 usw2-az1 | 96 | 98% | 8.8 | 9 (11-08 19:34Z) |
| us-west-2 usw2-az2 | 94 | 90% | 8.3 | 9 (11-08 19:34Z) |
| us-west-2 usw2-az3 | 134 | 88% | 8.2 | 9 (11-08 19:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718800 | 2026-11-08T19:34:36Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-08T19:34:36Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.723500 | 2026-11-08T19:34:36Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.578300 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.592100 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-11-08T19:34:36Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-08T19:34:36Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.554600 | 2026-11-08T19:34:36Z |
| ap-south-1 | ap-south-1a | Windows | 0.420300 | 2026-11-08T19:34:36Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.536800 | 2026-11-08T19:34:36Z |
| ap-south-1 | ap-south-1b | Windows | 0.348400 | 2026-11-08T19:34:36Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.588000 | 2026-11-08T19:34:36Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.494900 | 2026-11-08T19:34:36Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.662400 | 2026-11-08T19:34:36Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530500 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.589900 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.578100 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.496400 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.427500 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.466400 | 2026-11-08T19:34:36Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549000 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548200 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546100 | 2026-11-08T19:34:36Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.546400 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2a | Windows | 0.299200 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.660000 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2b | Windows | 0.313500 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.575900 | 2026-11-08T19:34:36Z |
| us-west-2 | us-west-2c | Windows | 0.298900 | 2026-11-08T19:34:36Z |
