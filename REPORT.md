# Spot placement score log

Generated 2026-11-27 19:11 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 576 | 46% | 5.0 | 1 (11-27 19:11Z) |
| ap-northeast-1 | 576 | 18% | 2.8 | 6 (11-27 19:11Z) |
| ap-northeast-2 | 576 | 68% | 7.0 | 9 (11-27 19:11Z) |
| ap-south-1 | 576 | 3% | 1.7 | 1 (11-27 19:11Z) |
| ap-southeast-2 | 576 | 1% | 1.0 | 1 (11-27 19:11Z) |
| ap-southeast-3 | 576 | 22% | 3.0 | 1 (11-27 19:11Z) |
| us-east-1 | 576 | 13% | 2.8 | 3 (11-27 19:11Z) |
| us-east-2 | 576 | 30% | 3.6 | 1 (11-27 19:11Z) |
| us-west-2 | 576 | 9% | 2.1 | 3 (11-27 19:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111119919961139119111111111111111111111111191111
ap-northeast-1   112999599999119121122121129999912921111119121116
ap-northeast-2   111119999999979917169199919999111111999991191199
ap-south-1       111111119111111111111111111119112112211112122211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111121131113111111111111111111111111111111111
us-east-1        334422332373746546765465656675446545544453543433
us-east-2        111111991991999111991811111111111111111911111111
us-west-2        212211121911112112121211211152131911212112321133
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 178 | 5% | 1.5 | 1 (11-27 19:11Z) |
| ap-east-1 ape1-az2 | 403 | 66% | 6.6 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 142 | 11% | 1.9 | 1 (11-27 18:52Z) |
| ap-northeast-1 apne1-az4 | 271 | 29% | 3.6 | 6 (11-27 19:11Z) |
| ap-northeast-2 apne2-az1 | 477 | 63% | 6.6 | 9 (11-27 19:11Z) |
| ap-northeast-2 apne2-az3 | 524 | 68% | 6.9 | 1 (11-27 18:52Z) |
| ap-northeast-2 apne2-az4 | 554 | 70% | 7.1 | 1 (11-27 18:52Z) |
| ap-south-1 aps1-az1 | 173 | 2% | 1.4 | 1 (11-27 19:11Z) |
| ap-south-1 aps1-az3 | 168 | 7% | 2.3 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az1 | 122 | 2% | 1.2 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az2 | 88 | 0% | 1.0 | 1 (11-27 18:52Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 339 | 36% | 4.2 | 1 (11-26 23:45Z) |
| us-east-1 use1-az1 | 131 | 0% | 1.0 | 1 (11-27 18:52Z) |
| us-east-1 use1-az2 | 151 | 3% | 1.4 | 1 (11-27 19:11Z) |
| us-east-1 use1-az4 | 200 | 19% | 2.8 | 1 (11-27 19:11Z) |
| us-east-1 use1-az5 | 187 | 22% | 2.9 | 1 (11-27 19:11Z) |
| us-east-1 use1-az6 | 151 | 21% | 2.8 | 1 (11-27 19:11Z) |
| us-east-2 use2-az1 | 247 | 42% | 4.5 | 1 (11-27 19:11Z) |
| us-east-2 use2-az2 | 289 | 51% | 5.2 | 1 (11-27 08:12Z) |
| us-east-2 use2-az3 | 314 | 47% | 5.1 | 1 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 141 | 15% | 2.4 | 1 (11-27 18:52Z) |
| us-west-2 usw2-az3 | 222 | 16% | 2.6 | 1 (11-27 19:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 576 | 73% | 7.4 | 9 (11-27 19:11Z) |
| ap-northeast-1 | 576 | 73% | 7.0 | 9 (11-27 19:11Z) |
| ap-northeast-2 | 576 | 100% | 9.0 | 9 (11-27 19:11Z) |
| ap-south-1 | 576 | 57% | 5.9 | 9 (11-27 19:11Z) |
| ap-southeast-2 | 576 | 28% | 3.7 | 9 (11-27 19:11Z) |
| ap-southeast-3 | 576 | 22% | 3.0 | 1 (11-27 19:11Z) |
| us-east-1 | 576 | 74% | 6.6 | 7 (11-27 19:11Z) |
| us-east-2 | 576 | 67% | 6.6 | 2 (11-27 19:11Z) |
| us-west-2 | 576 | 52% | 5.7 | 9 (11-27 19:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   429999999999229299199399199999999999929199199299
ap-northeast-2   999999999999999999999999999999999999999999999299
ap-south-1       911111199111111111111111111119112112214115129299
ap-southeast-2   119132999991118191191199119999919991919191199199
ap-southeast-3   111111121131113111111111111111111111111111111111
us-east-1        697899999799999888988888889999989999878887889877
us-east-2        999999999991999958992991993291119949399933992922
us-west-2        419423993999115995453532444499569999596994999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 378 | 86% | 8.1 | 9 (11-27 19:11Z) |
| ap-east-1 ape1-az2 | 337 | 88% | 8.3 | 9 (11-27 08:12Z) |
| ap-east-1 ape1-az3 | 374 | 88% | 8.3 | 9 (11-27 19:11Z) |
| ap-northeast-1 apne1-az1 | 231 | 95% | 8.7 | 9 (11-27 19:11Z) |
| ap-northeast-1 apne1-az2 | 220 | 88% | 8.2 | 9 (11-27 19:11Z) |
| ap-northeast-1 apne1-az4 | 297 | 99% | 8.9 | 9 (11-27 18:52Z) |
| ap-northeast-2 apne2-az1 | 463 | 100% | 9.0 | 9 (11-27 19:11Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 484 | 100% | 9.0 | 9 (11-27 19:11Z) |
| ap-northeast-2 apne2-az4 | 378 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az1 | 181 | 88% | 8.3 | 9 (11-27 18:52Z) |
| ap-south-1 aps1-az2 | 189 | 80% | 7.8 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az3 | 205 | 90% | 8.4 | 9 (11-27 19:11Z) |
| ap-southeast-2 apse2-az1 | 85 | 88% | 8.3 | 9 (11-27 19:11Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 98 | 86% | 8.1 | 9 (11-27 19:11Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 163 | 90% | 8.3 | 2 (11-27 08:12Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 145 | 93% | 8.5 | 9 (11-26 23:45Z) |
| us-east-2 use2-az1 | 208 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az2 | 225 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az3 | 250 | 97% | 8.8 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 113 | 98% | 8.9 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az2 | 103 | 91% | 8.4 | 9 (11-27 19:11Z) |
| us-west-2 usw2-az3 | 155 | 88% | 8.2 | 9 (11-27 18:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707800 | 2026-11-27T19:11:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-27T19:11:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.730900 | 2026-11-27T19:11:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.611800 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626900 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612000 | 2026-11-27T19:11:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-27T19:11:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.764300 | 2026-11-27T19:11:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.390800 | 2026-11-27T19:11:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.698400 | 2026-11-27T19:11:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.400400 | 2026-11-27T19:11:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700800 | 2026-11-27T19:11:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504900 | 2026-11-27T19:11:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.574400 | 2026-11-27T19:11:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.520300 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.792800 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.910500 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881000 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.870300 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.872400 | 2026-11-27T19:11:06Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545200 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.554600 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549200 | 2026-11-27T19:11:06Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.635800 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2a | Windows | 0.290100 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906600 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-11-27T19:11:06Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-27T19:11:06Z |
