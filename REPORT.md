# Spot placement score log

Generated 2026-11-22 03:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 560 | 47% | 5.1 | 1 (11-22 03:03Z) |
| ap-northeast-1 | 560 | 18% | 2.8 | 1 (11-22 03:03Z) |
| ap-northeast-2 | 560 | 69% | 7.0 | 1 (11-22 03:03Z) |
| ap-south-1 | 560 | 3% | 1.7 | 1 (11-22 03:03Z) |
| ap-southeast-2 | 560 | 1% | 1.0 | 1 (11-22 03:03Z) |
| ap-southeast-3 | 560 | 23% | 3.0 | 1 (11-22 03:03Z) |
| us-east-1 | 560 | 12% | 2.8 | 4 (11-22 03:03Z) |
| us-east-2 | 560 | 30% | 3.6 | 1 (11-22 03:03Z) |
| us-west-2 | 560 | 9% | 2.1 | 3 (11-22 03:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        998199191219111111111991996113911911111111111111
ap-northeast-1   199112111115111211299959999911912112212112999991
ap-northeast-2   999999999919111111111999999997991716919991999911
ap-south-1       119111122111111111111111911111111111111111111911
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   131111111113111111111112113111311111111111111111
us-east-1        223292933224232333442233237374654676546565667544
us-east-2        199991111111111111111199199199911199181111111111
us-west-2        112111112122211121221112191111211212121121115213
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 135 | 11% | 2.0 | 1 (11-21 01:25Z) |
| ap-northeast-1 apne1-az4 | 264 | 28% | 3.6 | 1 (11-22 03:03Z) |
| ap-northeast-2 apne2-az1 | 468 | 63% | 6.6 | 1 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 512 | 69% | 7.0 | 9 (11-21 17:22Z) |
| ap-northeast-2 apne2-az4 | 541 | 71% | 7.2 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az1 | 166 | 2% | 1.4 | 1 (11-22 03:03Z) |
| ap-south-1 aps1-az3 | 163 | 7% | 2.3 | 8 (11-21 17:22Z) |
| ap-southeast-2 apse2-az1 | 114 | 3% | 1.2 | 1 (11-20 11:24Z) |
| ap-southeast-2 apse2-az2 | 82 | 0% | 1.0 | 1 (11-21 01:25Z) |
| ap-southeast-3 apse3-az1 | 101 | 0% | 1.0 | 1 (11-22 03:03Z) |
| ap-southeast-3 apse3-az3 | 334 | 36% | 4.2 | 1 (11-21 01:25Z) |
| us-east-1 use1-az1 | 123 | 0% | 1.0 | 1 (11-21 09:39Z) |
| us-east-1 use1-az2 | 146 | 3% | 1.4 | 1 (11-22 03:03Z) |
| us-east-1 use1-az4 | 189 | 20% | 2.8 | 2 (11-21 23:05Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 146 | 21% | 2.9 | 2 (11-22 03:03Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 285 | 51% | 5.3 | 1 (11-22 03:03Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 178 | 21% | 3.0 | 4 (11-21 09:39Z) |
| us-west-2 usw2-az2 | 133 | 16% | 2.4 | 1 (11-21 09:39Z) |
| us-west-2 usw2-az3 | 214 | 16% | 2.6 | 1 (11-22 03:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 560 | 73% | 7.4 | 9 (11-22 03:03Z) |
| ap-northeast-1 | 560 | 72% | 7.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 | 560 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-south-1 | 560 | 58% | 5.9 | 1 (11-22 03:03Z) |
| ap-southeast-2 | 560 | 28% | 3.6 | 1 (11-22 03:03Z) |
| ap-southeast-3 | 560 | 23% | 3.0 | 1 (11-22 03:03Z) |
| us-east-1 | 560 | 73% | 6.6 | 8 (11-22 03:03Z) |
| us-east-2 | 560 | 68% | 6.7 | 1 (11-22 03:03Z) |
| us-west-2 | 560 | 51% | 5.6 | 6 (11-22 03:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999939229929928942999999999922929919939919999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       119913922911111191111119911111111111111111111911
ap-southeast-2   199119119119919911913299999111819119119911999991
ap-southeast-3   131111111113111111111112113111311111111111111111
us-east-1        999995996699689669789999979999988898888888999998
us-east-2        999991199199199999999999999199995899299199329111
us-west-2        999994943349334341942399399911599545353244449956
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 363 | 85% | 8.1 | 9 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 331 | 88% | 8.3 | 9 (11-22 03:03Z) |
| ap-east-1 ape1-az3 | 360 | 88% | 8.3 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az1 | 226 | 95% | 8.7 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az2 | 213 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az4 | 289 | 99% | 8.9 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az1 | 454 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az2 | 128 | 88% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 471 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az4 | 369 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 79 | 87% | 8.2 | 9 (11-21 23:05Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 92 | 85% | 8.0 | 9 (11-21 17:22Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 119 | 99% | 8.9 | 9 (11-21 17:22Z) |
| us-east-1 use1-az4 | 160 | 91% | 8.4 | 9 (11-21 09:39Z) |
| us-east-1 use1-az5 | 115 | 98% | 8.9 | 9 (11-21 23:05Z) |
| us-east-1 use1-az6 | 142 | 93% | 8.5 | 9 (11-21 23:05Z) |
| us-east-2 use2-az1 | 200 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az2 | 220 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az3 | 245 | 97% | 8.8 | 9 (11-21 09:39Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 145 | 88% | 8.2 | 9 (11-21 17:22Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706800 | 2026-11-22T03:03:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-22T03:03:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.725900 | 2026-11-22T03:03:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.599900 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.620300 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.596300 | 2026-11-22T03:03:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-22T03:03:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.683000 | 2026-11-22T03:03:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.422200 | 2026-11-22T03:03:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.771100 | 2026-11-22T03:03:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.424700 | 2026-11-22T03:03:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.626600 | 2026-11-22T03:03:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.534300 | 2026-11-22T03:03:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.510100 | 2026-11-22T03:03:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550200 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.860900 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.893100 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1b | Windows | 0.307100 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.737400 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.797000 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.696400 | 2026-11-22T03:03:37Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530600 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536300 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.527900 | 2026-11-22T03:03:37Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.598400 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2a | Windows | 0.306800 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.746900 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.536600 | 2026-11-22T03:03:37Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-22T03:03:37Z |
