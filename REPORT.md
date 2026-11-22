# Spot placement score log

Generated 2026-11-22 11:09 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 561 | 47% | 5.1 | 1 (11-22 11:09Z) |
| ap-northeast-1 | 561 | 18% | 2.8 | 2 (11-22 11:09Z) |
| ap-northeast-2 | 561 | 68% | 7.0 | 1 (11-22 11:09Z) |
| ap-south-1 | 561 | 3% | 1.7 | 2 (11-22 11:09Z) |
| ap-southeast-2 | 561 | 1% | 1.0 | 1 (11-22 11:09Z) |
| ap-southeast-3 | 561 | 23% | 3.0 | 1 (11-22 11:09Z) |
| us-east-1 | 561 | 13% | 2.8 | 6 (11-22 11:09Z) |
| us-east-2 | 561 | 30% | 3.6 | 1 (11-22 11:09Z) |
| us-west-2 | 561 | 9% | 2.1 | 1 (11-22 11:09Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        981991912191111111119919961139119111111111111111
ap-northeast-1   991121111151112112999599999119121122121129999912
ap-northeast-2   999999999191111111119999999979917169199919999111
ap-south-1       191111221111111111111119111111111111111111119112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   311111111131111111111121131113111111111111111111
us-east-1        232929332242323334422332373746546765465656675446
us-east-2        999911111111111111111991991999111991811111111111
us-west-2        121111121222111212211121911112112121211211152131
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
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 135 | 11% | 2.0 | 1 (11-21 01:25Z) |
| ap-northeast-1 apne1-az4 | 265 | 28% | 3.6 | 2 (11-22 11:09Z) |
| ap-northeast-2 apne2-az1 | 469 | 63% | 6.6 | 1 (11-22 11:09Z) |
| ap-northeast-2 apne2-az3 | 512 | 69% | 7.0 | 9 (11-21 17:22Z) |
| ap-northeast-2 apne2-az4 | 541 | 71% | 7.2 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az1 | 167 | 2% | 1.4 | 1 (11-22 11:09Z) |
| ap-south-1 aps1-az3 | 163 | 7% | 2.3 | 8 (11-21 17:22Z) |
| ap-southeast-2 apse2-az1 | 114 | 3% | 1.2 | 1 (11-20 11:24Z) |
| ap-southeast-2 apse2-az2 | 82 | 0% | 1.0 | 1 (11-21 01:25Z) |
| ap-southeast-3 apse3-az1 | 102 | 0% | 1.0 | 1 (11-22 11:09Z) |
| ap-southeast-3 apse3-az3 | 334 | 36% | 4.2 | 1 (11-21 01:25Z) |
| us-east-1 use1-az1 | 123 | 0% | 1.0 | 1 (11-21 09:39Z) |
| us-east-1 use1-az2 | 147 | 3% | 1.4 | 1 (11-22 11:09Z) |
| us-east-1 use1-az4 | 190 | 20% | 2.8 | 2 (11-22 11:09Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 147 | 21% | 2.9 | 2 (11-22 11:09Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 286 | 51% | 5.3 | 1 (11-22 11:09Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 179 | 21% | 2.9 | 1 (11-22 11:09Z) |
| us-west-2 usw2-az2 | 133 | 16% | 2.4 | 1 (11-21 09:39Z) |
| us-west-2 usw2-az3 | 215 | 16% | 2.6 | 1 (11-22 11:09Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 561 | 73% | 7.4 | 9 (11-22 11:09Z) |
| ap-northeast-1 | 561 | 73% | 7.0 | 9 (11-22 11:09Z) |
| ap-northeast-2 | 561 | 100% | 9.0 | 9 (11-22 11:09Z) |
| ap-south-1 | 561 | 58% | 5.9 | 2 (11-22 11:09Z) |
| ap-southeast-2 | 561 | 28% | 3.7 | 9 (11-22 11:09Z) |
| ap-southeast-3 | 561 | 23% | 3.0 | 1 (11-22 11:09Z) |
| us-east-1 | 561 | 73% | 6.6 | 9 (11-22 11:09Z) |
| us-east-2 | 561 | 68% | 6.7 | 9 (11-22 11:09Z) |
| us-west-2 | 561 | 51% | 5.6 | 9 (11-22 11:09Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999392299299289429999999999229299199399199999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       199139229111111911111199111111111111111111119112
ap-southeast-2   991191191199199119132999991118191191199119999919
ap-southeast-3   311111111131111111111121131113111111111111111111
us-east-1        999959966996896697899999799999888988888889999989
us-east-2        999911991991999999999999991999958992991993291119
us-west-2        999949433493343419423993999115995453532444499569
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
| ap-east-1 ape1-az1 | 364 | 85% | 8.1 | 9 (11-22 11:09Z) |
| ap-east-1 ape1-az2 | 331 | 88% | 8.3 | 9 (11-22 03:03Z) |
| ap-east-1 ape1-az3 | 361 | 88% | 8.3 | 9 (11-22 11:09Z) |
| ap-northeast-1 apne1-az1 | 226 | 95% | 8.7 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az2 | 213 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az4 | 290 | 99% | 8.9 | 9 (11-22 11:09Z) |
| ap-northeast-2 apne2-az1 | 454 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az2 | 128 | 88% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 472 | 100% | 9.0 | 9 (11-22 11:09Z) |
| ap-northeast-2 apne2-az4 | 370 | 87% | 8.2 | 9 (11-22 11:09Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 79 | 87% | 8.2 | 9 (11-21 23:05Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 93 | 85% | 8.1 | 9 (11-22 11:09Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 120 | 99% | 8.9 | 9 (11-22 11:09Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 115 | 98% | 8.9 | 9 (11-21 23:05Z) |
| us-east-1 use1-az6 | 143 | 93% | 8.5 | 9 (11-22 11:09Z) |
| us-east-2 use2-az1 | 201 | 99% | 8.9 | 9 (11-22 11:09Z) |
| us-east-2 use2-az2 | 220 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az3 | 245 | 97% | 8.8 | 9 (11-21 09:39Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 145 | 88% | 8.2 | 9 (11-21 17:22Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706700 | 2026-11-22T11:09:29Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-22T11:09:29Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.723600 | 2026-11-22T11:09:29Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.598800 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.617200 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.593100 | 2026-11-22T11:09:29Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-22T11:09:29Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.695800 | 2026-11-22T11:09:29Z |
| ap-south-1 | ap-south-1a | Windows | 0.420900 | 2026-11-22T11:09:29Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.772600 | 2026-11-22T11:09:29Z |
| ap-south-1 | ap-south-1b | Windows | 0.424700 | 2026-11-22T11:09:29Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.628200 | 2026-11-22T11:09:29Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.533900 | 2026-11-22T11:09:29Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.518000 | 2026-11-22T11:09:29Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550000 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.860000 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.893100 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1b | Windows | 0.311100 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.749700 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.800800 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.717700 | 2026-11-22T11:09:29Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530600 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536300 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.527400 | 2026-11-22T11:09:29Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.589800 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2a | Windows | 0.305000 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.760500 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526900 | 2026-11-22T11:09:29Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-22T11:09:29Z |
