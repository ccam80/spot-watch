# Spot placement score log

Generated 2026-11-27 20:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 577 | 46% | 5.0 | 1 (11-27 20:14Z) |
| ap-northeast-1 | 577 | 18% | 2.8 | 1 (11-27 20:14Z) |
| ap-northeast-2 | 577 | 68% | 7.0 | 9 (11-27 20:14Z) |
| ap-south-1 | 577 | 3% | 1.7 | 1 (11-27 20:14Z) |
| ap-southeast-2 | 577 | 1% | 1.0 | 1 (11-27 20:14Z) |
| ap-southeast-3 | 577 | 22% | 3.0 | 1 (11-27 20:14Z) |
| us-east-1 | 577 | 13% | 2.8 | 4 (11-27 20:14Z) |
| us-east-2 | 577 | 29% | 3.6 | 1 (11-27 20:14Z) |
| us-west-2 | 577 | 9% | 2.1 | 3 (11-27 20:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111199199611391191111111111111111111111111911111
ap-northeast-1   129995999991191211221211299999129211111191211161
ap-northeast-2   111199999999799171691999199991111119999911911999
ap-south-1       111111191111111111111111111191121122111121222111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111211311131111111111111111111111111111111111
us-east-1        344223323737465467654656566754465455444535434334
us-east-2        111119919919991119918111111111111111119111111111
us-west-2        122111219111121121212112111521319112121123211333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
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
| ap-east-1 ape1-az2 | 403 | 66% | 6.6 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 143 | 10% | 1.9 | 1 (11-27 20:14Z) |
| ap-northeast-1 apne1-az4 | 272 | 29% | 3.6 | 1 (11-27 20:14Z) |
| ap-northeast-2 apne2-az1 | 478 | 63% | 6.6 | 9 (11-27 20:14Z) |
| ap-northeast-2 apne2-az3 | 525 | 68% | 6.9 | 1 (11-27 20:14Z) |
| ap-northeast-2 apne2-az4 | 555 | 70% | 7.1 | 1 (11-27 20:14Z) |
| ap-south-1 aps1-az1 | 173 | 2% | 1.4 | 1 (11-27 19:11Z) |
| ap-south-1 aps1-az3 | 168 | 7% | 2.3 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az1 | 122 | 2% | 1.2 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az2 | 89 | 0% | 1.0 | 1 (11-27 20:14Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 340 | 36% | 4.2 | 1 (11-27 20:14Z) |
| us-east-1 use1-az1 | 132 | 0% | 1.0 | 1 (11-27 20:14Z) |
| us-east-1 use1-az2 | 151 | 3% | 1.4 | 1 (11-27 19:11Z) |
| us-east-1 use1-az4 | 200 | 19% | 2.8 | 1 (11-27 19:11Z) |
| us-east-1 use1-az5 | 188 | 22% | 2.9 | 1 (11-27 20:14Z) |
| us-east-1 use1-az6 | 151 | 21% | 2.8 | 1 (11-27 19:11Z) |
| us-east-2 use2-az1 | 247 | 42% | 4.5 | 1 (11-27 19:11Z) |
| us-east-2 use2-az2 | 289 | 51% | 5.2 | 1 (11-27 08:12Z) |
| us-east-2 use2-az3 | 314 | 47% | 5.1 | 1 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 142 | 15% | 2.4 | 1 (11-27 20:14Z) |
| us-west-2 usw2-az3 | 222 | 16% | 2.6 | 1 (11-27 19:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 577 | 73% | 7.4 | 9 (11-27 20:14Z) |
| ap-northeast-1 | 577 | 73% | 7.0 | 9 (11-27 20:14Z) |
| ap-northeast-2 | 577 | 100% | 9.0 | 9 (11-27 20:14Z) |
| ap-south-1 | 577 | 57% | 5.9 | 9 (11-27 20:14Z) |
| ap-southeast-2 | 577 | 29% | 3.7 | 9 (11-27 20:14Z) |
| ap-southeast-3 | 577 | 22% | 3.0 | 1 (11-27 20:14Z) |
| us-east-1 | 577 | 74% | 6.6 | 8 (11-27 20:14Z) |
| us-east-2 | 577 | 67% | 6.6 | 1 (11-27 20:14Z) |
| us-west-2 | 577 | 53% | 5.7 | 9 (11-27 20:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   299999999992292991993991999999999999291991992999
ap-northeast-2   999999999999999999999999999999999999999999992999
ap-south-1       111111991111111111111111111191121122141151292999
ap-southeast-2   191329999911181911911991199999199919191911991999
ap-southeast-3   111111211311131111111111111111111111111111111111
us-east-1        978999997999998889888888899999899998788878898778
us-east-2        999999999919999589929919932911199493999339929221
us-west-2        194239939991159954535324444995699995969949999999
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
| ap-east-1 ape1-az1 | 379 | 86% | 8.1 | 9 (11-27 20:14Z) |
| ap-east-1 ape1-az2 | 338 | 88% | 8.3 | 9 (11-27 20:14Z) |
| ap-east-1 ape1-az3 | 374 | 88% | 8.3 | 9 (11-27 19:11Z) |
| ap-northeast-1 apne1-az1 | 232 | 95% | 8.7 | 9 (11-27 20:14Z) |
| ap-northeast-1 apne1-az2 | 220 | 88% | 8.2 | 9 (11-27 19:11Z) |
| ap-northeast-1 apne1-az4 | 298 | 99% | 8.9 | 9 (11-27 20:14Z) |
| ap-northeast-2 apne2-az1 | 463 | 100% | 9.0 | 9 (11-27 19:11Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 484 | 100% | 9.0 | 9 (11-27 19:11Z) |
| ap-northeast-2 apne2-az4 | 379 | 88% | 8.3 | 9 (11-27 20:14Z) |
| ap-south-1 aps1-az1 | 182 | 88% | 8.3 | 9 (11-27 20:14Z) |
| ap-south-1 aps1-az2 | 189 | 80% | 7.8 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az3 | 206 | 90% | 8.4 | 9 (11-27 20:14Z) |
| ap-southeast-2 apse2-az1 | 86 | 88% | 8.3 | 9 (11-27 20:14Z) |
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
| us-west-2 usw2-az1 | 114 | 98% | 8.9 | 9 (11-27 20:14Z) |
| us-west-2 usw2-az2 | 103 | 91% | 8.4 | 9 (11-27 19:11Z) |
| us-west-2 usw2-az3 | 156 | 88% | 8.2 | 9 (11-27 20:14Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707800 | 2026-11-27T20:14:31Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-27T20:14:31Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.730900 | 2026-11-27T20:14:31Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.611800 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626900 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612000 | 2026-11-27T20:14:31Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-27T20:14:31Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.753900 | 2026-11-27T20:14:31Z |
| ap-south-1 | ap-south-1a | Windows | 0.390800 | 2026-11-27T20:14:31Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.691400 | 2026-11-27T20:14:31Z |
| ap-south-1 | ap-south-1b | Windows | 0.399400 | 2026-11-27T20:14:31Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.701100 | 2026-11-27T20:14:31Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504900 | 2026-11-27T20:14:31Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.574400 | 2026-11-27T20:14:31Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.520300 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.792800 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.910500 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881000 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.870300 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.872400 | 2026-11-27T20:14:31Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545200 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.553700 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549200 | 2026-11-27T20:14:31Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.635800 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2a | Windows | 0.289500 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906600 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-11-27T20:14:31Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-27T20:14:31Z |
