# Spot placement score log

Generated 2026-11-06 17:54 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 506 | 48% | 5.2 | 1 (11-06 17:54Z) |
| ap-northeast-1 | 506 | 15% | 2.7 | 1 (11-06 17:54Z) |
| ap-northeast-2 | 506 | 68% | 7.1 | 9 (11-06 17:54Z) |
| ap-south-1 | 506 | 3% | 1.7 | 1 (11-06 17:54Z) |
| ap-southeast-2 | 506 | 1% | 1.1 | 1 (11-06 17:54Z) |
| ap-southeast-3 | 506 | 25% | 3.2 | 1 (11-06 17:54Z) |
| us-east-1 | 506 | 10% | 2.6 | 2 (11-06 17:54Z) |
| us-east-2 | 506 | 30% | 3.6 | 1 (11-06 17:54Z) |
| us-west-2 | 506 | 9% | 2.1 | 1 (11-06 17:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111999111119999999991119999999991919111129911191
ap-northeast-1   242111442111112118791114788819511911911122112111
ap-northeast-2   999999991199999999991999999999999999929999999999
ap-south-1       111111111111111111111111111116981111112111222221
ap-southeast-2   111111111111111111111111111111111111111171111111
ap-southeast-3   111111111111115512541118397313861811111111113111
us-east-1        111222222222222212211111111129999121123333322322
us-east-2        111111111111991112111999119699999911912111911111
us-west-2        111111111111111941311111111117111211222111911111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 160 | 6% | 1.6 | 1 (11-05 15:23Z) |
| ap-east-1 ape1-az2 | 371 | 66% | 6.6 | 9 (11-06 10:43Z) |
| ap-northeast-1 apne1-az1 | 112 | 8% | 1.7 | 1 (11-06 17:54Z) |
| ap-northeast-1 apne1-az4 | 225 | 26% | 3.5 | 1 (11-05 06:32Z) |
| ap-northeast-2 apne2-az1 | 434 | 62% | 6.6 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az3 | 471 | 68% | 7.0 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az4 | 499 | 69% | 7.1 | 9 (11-06 17:54Z) |
| ap-south-1 aps1-az1 | 147 | 1% | 1.3 | 1 (11-06 17:54Z) |
| ap-south-1 aps1-az3 | 138 | 7% | 2.4 | 1 (11-04 09:01Z) |
| ap-southeast-2 apse2-az1 | 101 | 3% | 1.3 | 1 (11-06 17:54Z) |
| ap-southeast-2 apse2-az2 | 69 | 0% | 1.0 | 1 (11-06 17:54Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 315 | 38% | 4.4 | 1 (11-06 17:54Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 161 | 25% | 3.2 | 1 (11-05 06:32Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 217 | 42% | 4.5 | 1 (11-05 21:55Z) |
| us-east-2 use2-az2 | 257 | 50% | 5.3 | 1 (11-05 15:23Z) |
| us-east-2 use2-az3 | 285 | 47% | 5.1 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az1 | 157 | 24% | 3.2 | 1 (11-04 09:01Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 199 | 17% | 2.7 | 1 (11-05 21:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 506 | 70% | 7.2 | 9 (11-06 17:54Z) |
| ap-northeast-1 | 506 | 72% | 7.0 | 9 (11-06 17:54Z) |
| ap-northeast-2 | 506 | 100% | 9.0 | 9 (11-06 17:54Z) |
| ap-south-1 | 506 | 62% | 6.3 | 1 (11-06 17:54Z) |
| ap-southeast-2 | 506 | 25% | 3.5 | 9 (11-06 17:54Z) |
| ap-southeast-3 | 506 | 25% | 3.2 | 1 (11-06 17:54Z) |
| us-east-1 | 506 | 70% | 6.4 | 5 (11-06 17:54Z) |
| us-east-2 | 506 | 67% | 6.6 | 1 (11-06 17:54Z) |
| us-west-2 | 506 | 51% | 5.6 | 1 (11-06 17:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999999992999992199199229
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999979999999999999999999991191129119229921
ap-southeast-2   111999999911131999999999999919911111911191991199
ap-southeast-3   111111111111115512541118397313861811111111113111
us-east-1        433939439999999999932299999999999452346976555795
us-east-2        222222899999999999992999199999999919919912911191
us-west-2        593121123324499954999299999999944924454342949441
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 5 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 327 | 83% | 8.0 | 9 (11-06 10:43Z) |
| ap-east-1 ape1-az2 | 287 | 86% | 8.1 | 9 (11-06 17:54Z) |
| ap-east-1 ape1-az3 | 316 | 86% | 8.2 | 9 (11-06 17:54Z) |
| ap-northeast-1 apne1-az1 | 209 | 95% | 8.7 | 9 (11-05 21:55Z) |
| ap-northeast-1 apne1-az2 | 185 | 85% | 8.1 | 9 (11-06 17:54Z) |
| ap-northeast-1 apne1-az4 | 268 | 99% | 8.9 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az1 | 414 | 100% | 9.0 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az2 | 108 | 85% | 8.0 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az3 | 432 | 100% | 9.0 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az4 | 330 | 86% | 8.1 | 9 (11-06 17:54Z) |
| ap-south-1 aps1-az1 | 175 | 87% | 8.2 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 196 | 90% | 8.4 | 9 (11-06 02:17Z) |
| ap-southeast-2 apse2-az1 | 65 | 85% | 8.0 | 9 (11-06 17:54Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 74 | 82% | 7.9 | 9 (11-06 17:54Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 106 | 100% | 9.0 | 9 (11-06 10:43Z) |
| us-east-1 use1-az4 | 141 | 91% | 8.4 | 9 (11-06 10:43Z) |
| us-east-1 use1-az5 | 105 | 98% | 8.9 | 9 (11-06 10:43Z) |
| us-east-1 use1-az6 | 126 | 92% | 8.4 | 9 (11-06 10:43Z) |
| us-east-2 use2-az1 | 177 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az2 | 194 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az3 | 224 | 96% | 8.7 | 9 (11-06 10:43Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 89 | 90% | 8.3 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az3 | 130 | 88% | 8.1 | 2 (11-06 02:17Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718800 | 2026-11-06T17:54:09Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-06T17:54:09Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.733700 | 2026-11-06T17:54:09Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580700 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.594000 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574100 | 2026-11-06T17:54:09Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-06T17:54:09Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.592600 | 2026-11-06T17:54:09Z |
| ap-south-1 | ap-south-1a | Windows | 0.430400 | 2026-11-06T17:54:09Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.552600 | 2026-11-06T17:54:09Z |
| ap-south-1 | ap-south-1b | Windows | 0.355200 | 2026-11-06T17:54:09Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.582800 | 2026-11-06T17:54:09Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.494900 | 2026-11-06T17:54:09Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.715700 | 2026-11-06T17:54:09Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542200 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.551300 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.515000 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.488200 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.419800 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.513300 | 2026-11-06T17:54:09Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549300 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550600 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547100 | 2026-11-06T17:54:09Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553900 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2a | Windows | 0.302700 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.683800 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2b | Windows | 0.316900 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.579400 | 2026-11-06T17:54:09Z |
| us-west-2 | us-west-2c | Windows | 0.302300 | 2026-11-06T17:54:09Z |
