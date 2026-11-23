# Spot placement score log

Generated 2026-11-23 08:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 564 | 47% | 5.0 | 1 (11-23 08:55Z) |
| ap-northeast-1 | 564 | 18% | 2.8 | 1 (11-23 08:55Z) |
| ap-northeast-2 | 564 | 68% | 7.0 | 1 (11-23 08:55Z) |
| ap-south-1 | 564 | 3% | 1.7 | 2 (11-23 08:55Z) |
| ap-southeast-2 | 564 | 1% | 1.0 | 1 (11-23 08:55Z) |
| ap-southeast-3 | 564 | 23% | 3.0 | 1 (11-23 08:55Z) |
| us-east-1 | 564 | 13% | 2.8 | 5 (11-23 08:55Z) |
| us-east-2 | 564 | 30% | 3.6 | 1 (11-23 08:55Z) |
| us-west-2 | 564 | 9% | 2.1 | 1 (11-23 08:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        991912191111111119919961139119111111111111111111
ap-northeast-1   121111151112112999599999119121122121129999912921
ap-northeast-2   999999191111111119999999979917169199919999111111
ap-south-1       111221111111111111119111111111111111111119112112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111131111111111121131113111111111111111111111
us-east-1        929332242323334422332373746546765465656675446545
us-east-2        911111111111111111991991999111991811111111111111
us-west-2        111121222111212211121911112112121211211152131911
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
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 400 | 66% | 6.6 | 1 (11-23 00:46Z) |
| ap-northeast-1 apne1-az1 | 136 | 11% | 2.0 | 1 (11-23 08:55Z) |
| ap-northeast-1 apne1-az4 | 267 | 28% | 3.6 | 1 (11-23 00:46Z) |
| ap-northeast-2 apne2-az1 | 470 | 63% | 6.6 | 1 (11-23 00:46Z) |
| ap-northeast-2 apne2-az3 | 514 | 68% | 6.9 | 1 (11-23 08:55Z) |
| ap-northeast-2 apne2-az4 | 544 | 70% | 7.2 | 1 (11-23 08:55Z) |
| ap-south-1 aps1-az1 | 167 | 2% | 1.4 | 1 (11-22 11:09Z) |
| ap-south-1 aps1-az3 | 166 | 7% | 2.3 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az1 | 117 | 3% | 1.2 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az2 | 84 | 0% | 1.0 | 1 (11-23 08:55Z) |
| ap-southeast-3 apse3-az1 | 103 | 0% | 1.0 | 1 (11-23 00:46Z) |
| ap-southeast-3 apse3-az3 | 334 | 36% | 4.2 | 1 (11-21 01:25Z) |
| us-east-1 use1-az1 | 125 | 0% | 1.0 | 1 (11-23 08:55Z) |
| us-east-1 use1-az2 | 147 | 3% | 1.4 | 1 (11-22 11:09Z) |
| us-east-1 use1-az4 | 191 | 20% | 2.8 | 2 (11-23 08:55Z) |
| us-east-1 use1-az5 | 179 | 23% | 3.0 | 1 (11-23 08:55Z) |
| us-east-1 use1-az6 | 147 | 21% | 2.9 | 2 (11-22 11:09Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 286 | 51% | 5.3 | 1 (11-22 11:09Z) |
| us-east-2 use2-az3 | 311 | 48% | 5.1 | 1 (11-23 00:46Z) |
| us-west-2 usw2-az1 | 181 | 21% | 3.0 | 1 (11-23 00:46Z) |
| us-west-2 usw2-az2 | 135 | 16% | 2.4 | 1 (11-23 08:55Z) |
| us-west-2 usw2-az3 | 216 | 16% | 2.6 | 9 (11-22 19:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 564 | 73% | 7.4 | 9 (11-23 08:55Z) |
| ap-northeast-1 | 564 | 73% | 7.1 | 9 (11-23 08:55Z) |
| ap-northeast-2 | 564 | 100% | 9.0 | 9 (11-23 08:55Z) |
| ap-south-1 | 564 | 57% | 5.9 | 2 (11-23 08:55Z) |
| ap-southeast-2 | 564 | 28% | 3.7 | 1 (11-23 08:55Z) |
| ap-southeast-3 | 564 | 23% | 3.0 | 1 (11-23 08:55Z) |
| us-east-1 | 564 | 73% | 6.6 | 9 (11-23 08:55Z) |
| us-east-2 | 564 | 68% | 6.7 | 9 (11-23 08:55Z) |
| us-west-2 | 564 | 52% | 5.6 | 9 (11-23 08:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   392299299289429999999999229299199399199999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       139229111111911111199111111111111111111119112112
ap-southeast-2   191191199199119132999991118191191199119999919991
ap-southeast-3   111111131111111111121131113111111111111111111111
us-east-1        959966996896697899999799999888988888889999989999
us-east-2        911991991999999999999991999958992991993291119949
us-west-2        949433493343419423993999115995453532444499569999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 366 | 85% | 8.1 | 9 (11-23 08:55Z) |
| ap-east-1 ape1-az2 | 334 | 88% | 8.3 | 9 (11-23 08:55Z) |
| ap-east-1 ape1-az3 | 363 | 88% | 8.3 | 9 (11-23 08:55Z) |
| ap-northeast-1 apne1-az1 | 226 | 95% | 8.7 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az2 | 213 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az4 | 290 | 99% | 8.9 | 9 (11-22 11:09Z) |
| ap-northeast-2 apne2-az1 | 454 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az2 | 128 | 88% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 475 | 100% | 9.0 | 9 (11-23 08:55Z) |
| ap-northeast-2 apne2-az4 | 372 | 87% | 8.2 | 9 (11-23 00:46Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 81 | 88% | 8.2 | 9 (11-23 00:46Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 94 | 85% | 8.1 | 9 (11-22 19:28Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 202 | 99% | 8.9 | 9 (11-23 08:55Z) |
| us-east-2 use2-az2 | 221 | 99% | 8.9 | 9 (11-23 08:55Z) |
| us-east-2 use2-az3 | 246 | 97% | 8.8 | 9 (11-23 08:55Z) |
| us-west-2 usw2-az1 | 108 | 98% | 8.9 | 9 (11-23 08:55Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 148 | 89% | 8.2 | 9 (11-23 08:55Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.705100 | 2026-11-23T08:55:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-23T08:55:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.724800 | 2026-11-23T08:55:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594600 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.617500 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.592200 | 2026-11-23T08:55:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-23T08:55:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.726700 | 2026-11-23T08:55:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.419600 | 2026-11-23T08:55:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.755600 | 2026-11-23T08:55:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.420900 | 2026-11-23T08:55:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.636100 | 2026-11-23T08:55:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.526700 | 2026-11-23T08:55:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.524900 | 2026-11-23T08:55:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.541200 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.857700 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.895800 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1b | Windows | 0.314600 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.765100 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.815300 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.760400 | 2026-11-23T08:55:50Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529900 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.537400 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.528000 | 2026-11-23T08:55:50Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556600 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2a | Windows | 0.304200 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.797100 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.530600 | 2026-11-23T08:55:50Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-23T08:55:50Z |
