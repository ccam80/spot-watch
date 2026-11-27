# Spot placement score log

Generated 2026-11-27 22:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 579 | 46% | 4.9 | 1 (11-27 22:14Z) |
| ap-northeast-1 | 579 | 18% | 2.8 | 9 (11-27 22:14Z) |
| ap-northeast-2 | 579 | 68% | 7.0 | 9 (11-27 22:14Z) |
| ap-south-1 | 579 | 3% | 1.7 | 1 (11-27 22:14Z) |
| ap-southeast-2 | 579 | 1% | 1.0 | 2 (11-27 22:14Z) |
| ap-southeast-3 | 579 | 22% | 3.0 | 1 (11-27 22:14Z) |
| us-east-1 | 579 | 13% | 2.8 | 3 (11-27 22:14Z) |
| us-east-2 | 579 | 29% | 3.5 | 1 (11-27 22:14Z) |
| us-west-2 | 579 | 9% | 2.1 | 9 (11-27 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119919961139119111111111111111111111111191111111
ap-northeast-1   999599999119121122121129999912921111119121116199
ap-northeast-2   119999999979917169199919999111111999991191199989
ap-south-1       111119111111111111111111119112112211112122211111
ap-southeast-2   111111111111111111111111111111111111111111111112
ap-southeast-3   111121131113111111111111111111111111111111111111
us-east-1        422332373746546765465656675446545544453543433433
us-east-2        111991991999111991811111111111111111911111111111
us-west-2        211121911112112121211211152131911212112321133339
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 178 | 5% | 1.5 | 1 (11-27 19:11Z) |
| ap-east-1 ape1-az2 | 404 | 65% | 6.6 | 1 (11-27 22:14Z) |
| ap-northeast-1 apne1-az1 | 145 | 10% | 1.9 | 4 (11-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 274 | 29% | 3.7 | 9 (11-27 22:14Z) |
| ap-northeast-2 apne2-az1 | 479 | 63% | 6.6 | 9 (11-27 22:14Z) |
| ap-northeast-2 apne2-az3 | 526 | 68% | 6.9 | 3 (11-27 21:12Z) |
| ap-northeast-2 apne2-az4 | 557 | 70% | 7.1 | 1 (11-27 22:14Z) |
| ap-south-1 aps1-az1 | 173 | 2% | 1.4 | 1 (11-27 19:11Z) |
| ap-south-1 aps1-az3 | 169 | 7% | 2.3 | 1 (11-27 21:12Z) |
| ap-southeast-2 apse2-az1 | 124 | 2% | 1.2 | 2 (11-27 22:14Z) |
| ap-southeast-2 apse2-az2 | 90 | 0% | 1.0 | 1 (11-27 21:12Z) |
| ap-southeast-3 apse3-az1 | 105 | 0% | 1.0 | 1 (11-27 22:14Z) |
| ap-southeast-3 apse3-az3 | 340 | 36% | 4.2 | 1 (11-27 20:14Z) |
| us-east-1 use1-az1 | 133 | 0% | 1.0 | 1 (11-27 21:12Z) |
| us-east-1 use1-az2 | 151 | 3% | 1.4 | 1 (11-27 19:11Z) |
| us-east-1 use1-az4 | 200 | 19% | 2.8 | 1 (11-27 19:11Z) |
| us-east-1 use1-az5 | 190 | 22% | 2.9 | 1 (11-27 22:14Z) |
| us-east-1 use1-az6 | 151 | 21% | 2.8 | 1 (11-27 19:11Z) |
| us-east-2 use2-az1 | 247 | 42% | 4.5 | 1 (11-27 19:11Z) |
| us-east-2 use2-az2 | 289 | 51% | 5.2 | 1 (11-27 08:12Z) |
| us-east-2 use2-az3 | 315 | 47% | 5.1 | 1 (11-27 22:14Z) |
| us-west-2 usw2-az1 | 185 | 21% | 3.0 | 9 (11-27 22:14Z) |
| us-west-2 usw2-az2 | 143 | 15% | 2.3 | 1 (11-27 21:12Z) |
| us-west-2 usw2-az3 | 222 | 16% | 2.6 | 1 (11-27 19:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 579 | 74% | 7.4 | 9 (11-27 22:14Z) |
| ap-northeast-1 | 579 | 73% | 7.1 | 9 (11-27 22:14Z) |
| ap-northeast-2 | 579 | 100% | 9.0 | 9 (11-27 22:14Z) |
| ap-south-1 | 579 | 57% | 5.9 | 9 (11-27 22:14Z) |
| ap-southeast-2 | 579 | 29% | 3.7 | 9 (11-27 22:14Z) |
| ap-southeast-3 | 579 | 22% | 3.0 | 1 (11-27 22:14Z) |
| us-east-1 | 579 | 74% | 6.6 | 7 (11-27 22:14Z) |
| us-east-2 | 579 | 67% | 6.6 | 2 (11-27 22:14Z) |
| us-west-2 | 579 | 53% | 5.7 | 9 (11-27 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999229299199399199999999999929199199299999
ap-northeast-2   999999999999999999999999999999999999999999299999
ap-south-1       111199111111111111111111119112112214115129299999
ap-southeast-2   132999991118191191199119999919991919191199199999
ap-southeast-3   111121131113111111111111111111111111111111111111
us-east-1        899999799999888988888889999989999878887889877887
us-east-2        999999991999958992991993291119949399933992922122
us-west-2        423993999115995453532444499569999596994999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 380 | 86% | 8.1 | 9 (11-27 22:14Z) |
| ap-east-1 ape1-az2 | 339 | 88% | 8.3 | 9 (11-27 21:12Z) |
| ap-east-1 ape1-az3 | 375 | 88% | 8.3 | 9 (11-27 21:12Z) |
| ap-northeast-1 apne1-az1 | 233 | 95% | 8.7 | 9 (11-27 22:14Z) |
| ap-northeast-1 apne1-az2 | 221 | 88% | 8.2 | 9 (11-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 299 | 99% | 8.9 | 9 (11-27 22:14Z) |
| ap-northeast-2 apne2-az1 | 465 | 100% | 9.0 | 9 (11-27 22:14Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 485 | 100% | 9.0 | 9 (11-27 21:12Z) |
| ap-northeast-2 apne2-az4 | 380 | 88% | 8.3 | 9 (11-27 21:12Z) |
| ap-south-1 aps1-az1 | 184 | 88% | 8.3 | 9 (11-27 22:14Z) |
| ap-south-1 aps1-az2 | 190 | 81% | 7.8 | 9 (11-27 21:12Z) |
| ap-south-1 aps1-az3 | 207 | 90% | 8.4 | 9 (11-27 22:14Z) |
| ap-southeast-2 apse2-az1 | 86 | 88% | 8.3 | 9 (11-27 20:14Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 99 | 86% | 8.1 | 9 (11-27 22:14Z) |
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
| us-west-2 usw2-az1 | 115 | 98% | 8.9 | 9 (11-27 21:12Z) |
| us-west-2 usw2-az2 | 105 | 91% | 8.4 | 9 (11-27 22:14Z) |
| us-west-2 usw2-az3 | 158 | 89% | 8.2 | 9 (11-27 22:14Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707800 | 2026-11-27T22:14:01Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-27T22:14:01Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.730900 | 2026-11-27T22:14:01Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.612900 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626900 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.611600 | 2026-11-27T22:14:01Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-27T22:14:01Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.753900 | 2026-11-27T22:14:01Z |
| ap-south-1 | ap-south-1a | Windows | 0.389500 | 2026-11-27T22:14:01Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.691400 | 2026-11-27T22:14:01Z |
| ap-south-1 | ap-south-1b | Windows | 0.399400 | 2026-11-27T22:14:01Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.701100 | 2026-11-27T22:14:01Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504900 | 2026-11-27T22:14:01Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.576400 | 2026-11-27T22:14:01Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.520300 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.792800 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.913200 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881000 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.870300 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.875200 | 2026-11-27T22:14:01Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545200 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.553700 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549200 | 2026-11-27T22:14:01Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.640600 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2a | Windows | 0.289500 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906600 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-11-27T22:14:01Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-27T22:14:01Z |
