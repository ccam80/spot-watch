# Spot placement score log

Generated 2026-11-24 17:31 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 567 | 47% | 5.0 | 1 (11-24 17:31Z) |
| ap-northeast-1 | 567 | 18% | 2.8 | 1 (11-24 17:31Z) |
| ap-northeast-2 | 567 | 68% | 7.0 | 9 (11-24 17:31Z) |
| ap-south-1 | 567 | 3% | 1.7 | 1 (11-24 17:31Z) |
| ap-southeast-2 | 567 | 1% | 1.0 | 1 (11-24 17:31Z) |
| ap-southeast-3 | 567 | 23% | 3.0 | 1 (11-24 17:31Z) |
| us-east-1 | 567 | 13% | 2.8 | 4 (11-24 17:31Z) |
| us-east-2 | 567 | 30% | 3.6 | 1 (11-24 17:31Z) |
| us-west-2 | 567 | 9% | 2.1 | 2 (11-24 17:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        912191111111119919961139119111111111111111111111
ap-northeast-1   111151112112999599999119121122121129999912921111
ap-northeast-2   999191111111119999999979917169199919999111111999
ap-south-1       221111111111111119111111111111111111119112112211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111131111111111121131113111111111111111111111111
us-east-1        332242323334422332373746546765465656675446545544
us-east-2        111111111111111991991999111991811111111111111111
us-west-2        121222111212211121911112112121211211152131911212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
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
| ap-northeast-1 apne1-az1 | 138 | 11% | 1.9 | 1 (11-24 05:56Z) |
| ap-northeast-1 apne1-az4 | 267 | 28% | 3.6 | 1 (11-23 00:46Z) |
| ap-northeast-2 apne2-az1 | 473 | 63% | 6.6 | 9 (11-24 17:31Z) |
| ap-northeast-2 apne2-az3 | 517 | 68% | 6.9 | 9 (11-24 17:31Z) |
| ap-northeast-2 apne2-az4 | 547 | 71% | 7.2 | 9 (11-24 17:31Z) |
| ap-south-1 aps1-az1 | 169 | 2% | 1.4 | 1 (11-24 17:31Z) |
| ap-south-1 aps1-az3 | 166 | 7% | 2.3 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az1 | 117 | 3% | 1.2 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az2 | 85 | 0% | 1.0 | 1 (11-24 05:56Z) |
| ap-southeast-3 apse3-az1 | 103 | 0% | 1.0 | 1 (11-23 00:46Z) |
| ap-southeast-3 apse3-az3 | 336 | 36% | 4.2 | 1 (11-24 05:56Z) |
| us-east-1 use1-az1 | 127 | 0% | 1.0 | 1 (11-24 05:56Z) |
| us-east-1 use1-az2 | 148 | 3% | 1.4 | 1 (11-24 17:31Z) |
| us-east-1 use1-az4 | 194 | 20% | 2.8 | 2 (11-24 17:31Z) |
| us-east-1 use1-az5 | 180 | 23% | 3.0 | 1 (11-24 05:56Z) |
| us-east-1 use1-az6 | 148 | 21% | 2.9 | 1 (11-24 17:31Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 287 | 51% | 5.2 | 1 (11-24 17:31Z) |
| us-east-2 use2-az3 | 311 | 48% | 5.1 | 1 (11-23 00:46Z) |
| us-west-2 usw2-az1 | 182 | 21% | 3.0 | 1 (11-24 17:31Z) |
| us-west-2 usw2-az2 | 137 | 15% | 2.4 | 1 (11-24 05:56Z) |
| us-west-2 usw2-az3 | 218 | 16% | 2.6 | 1 (11-24 17:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 567 | 73% | 7.4 | 9 (11-24 17:31Z) |
| ap-northeast-1 | 567 | 73% | 7.0 | 9 (11-24 17:31Z) |
| ap-northeast-2 | 567 | 100% | 9.0 | 9 (11-24 17:31Z) |
| ap-south-1 | 567 | 57% | 5.9 | 4 (11-24 17:31Z) |
| ap-southeast-2 | 567 | 28% | 3.7 | 9 (11-24 17:31Z) |
| ap-southeast-3 | 567 | 23% | 3.0 | 1 (11-24 17:31Z) |
| us-east-1 | 567 | 73% | 6.6 | 8 (11-24 17:31Z) |
| us-east-2 | 567 | 68% | 6.7 | 9 (11-24 17:31Z) |
| us-west-2 | 567 | 52% | 5.7 | 6 (11-24 17:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   299299289429999999999229299199399199999999999929
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       229111111911111199111111111111111111119112112214
ap-southeast-2   191199199119132999991118191191199119999919991919
ap-southeast-3   111131111111111121131113111111111111111111111111
us-east-1        966996896697899999799999888988888889999989999878
us-east-2        991991999999999999991999958992991993291119949399
us-west-2        433493343419423993999115995453532444499569999596
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 369 | 85% | 8.1 | 9 (11-24 17:31Z) |
| ap-east-1 ape1-az2 | 334 | 88% | 8.3 | 9 (11-23 08:55Z) |
| ap-east-1 ape1-az3 | 366 | 88% | 8.3 | 9 (11-24 17:31Z) |
| ap-northeast-1 apne1-az1 | 228 | 95% | 8.7 | 9 (11-24 17:31Z) |
| ap-northeast-1 apne1-az2 | 215 | 87% | 8.2 | 9 (11-24 17:31Z) |
| ap-northeast-1 apne1-az4 | 292 | 99% | 8.9 | 9 (11-24 17:31Z) |
| ap-northeast-2 apne2-az1 | 457 | 100% | 9.0 | 9 (11-24 17:31Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 478 | 100% | 9.0 | 9 (11-24 17:31Z) |
| ap-northeast-2 apne2-az4 | 374 | 87% | 8.2 | 9 (11-24 05:56Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 83 | 88% | 8.2 | 9 (11-24 17:31Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 95 | 85% | 8.1 | 9 (11-24 17:31Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 204 | 99% | 8.9 | 9 (11-24 17:31Z) |
| us-east-2 use2-az2 | 222 | 99% | 8.9 | 9 (11-24 05:56Z) |
| us-east-2 use2-az3 | 247 | 97% | 8.8 | 9 (11-24 05:56Z) |
| us-west-2 usw2-az1 | 109 | 98% | 8.9 | 9 (11-24 05:56Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 149 | 89% | 8.2 | 9 (11-24 05:56Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707500 | 2026-11-24T17:31:48Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-24T17:31:48Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.735700 | 2026-11-24T17:31:48Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.610800 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.628400 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.607300 | 2026-11-24T17:31:48Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-24T17:31:48Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.761500 | 2026-11-24T17:31:48Z |
| ap-south-1 | ap-south-1a | Windows | 0.411100 | 2026-11-24T17:31:48Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.756700 | 2026-11-24T17:31:48Z |
| ap-south-1 | ap-south-1b | Windows | 0.429500 | 2026-11-24T17:31:48Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.658400 | 2026-11-24T17:31:48Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.518400 | 2026-11-24T17:31:48Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.544300 | 2026-11-24T17:31:48Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.533100 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.846100 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.897400 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1b | Windows | 0.320400 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.820200 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.843200 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.809700 | 2026-11-24T17:31:48Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532500 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545300 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.535900 | 2026-11-24T17:31:48Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.549600 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2a | Windows | 0.303500 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.834700 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.529300 | 2026-11-24T17:31:48Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-24T17:31:48Z |
