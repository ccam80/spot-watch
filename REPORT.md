# Spot placement score log

Generated 2026-11-26 04:56 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 571 | 46% | 5.0 | 1 (11-26 04:56Z) |
| ap-northeast-1 | 571 | 18% | 2.8 | 1 (11-26 04:56Z) |
| ap-northeast-2 | 571 | 68% | 7.0 | 1 (11-26 04:56Z) |
| ap-south-1 | 571 | 3% | 1.7 | 1 (11-26 04:56Z) |
| ap-southeast-2 | 571 | 1% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 | 571 | 22% | 3.0 | 1 (11-26 04:56Z) |
| us-east-1 | 571 | 13% | 2.8 | 5 (11-26 04:56Z) |
| us-east-2 | 571 | 30% | 3.6 | 1 (11-26 04:56Z) |
| us-west-2 | 571 | 9% | 2.1 | 3 (11-26 04:56Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911111111199199611391191111111111111111111111111
ap-northeast-1   511121129995999991191211221211299999129211111191
ap-northeast-2   911111111199999999799171691999199991111119999911
ap-south-1       111111111111191111111111111111111191121122111121
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   311111111111211311131111111111111111111111111111
us-east-1        423233344223323737465467654656566754465455444535
us-east-2        111111111119919919991119918111111111111111119111
us-west-2        221112122111219111121121212112111521319112121123
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 5 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
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
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 402 | 65% | 6.6 | 1 (11-26 04:56Z) |
| ap-northeast-1 apne1-az1 | 140 | 11% | 1.9 | 1 (11-25 22:26Z) |
| ap-northeast-1 apne1-az4 | 270 | 29% | 3.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az1 | 475 | 63% | 6.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az3 | 520 | 68% | 6.9 | 1 (11-25 22:26Z) |
| ap-northeast-2 apne2-az4 | 551 | 70% | 7.2 | 1 (11-26 04:56Z) |
| ap-south-1 aps1-az1 | 170 | 2% | 1.4 | 1 (11-25 12:40Z) |
| ap-south-1 aps1-az3 | 166 | 7% | 2.3 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az1 | 119 | 3% | 1.2 | 1 (11-26 04:56Z) |
| ap-southeast-2 apse2-az2 | 86 | 0% | 1.0 | 1 (11-25 22:26Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 338 | 36% | 4.2 | 1 (11-25 22:26Z) |
| us-east-1 use1-az1 | 129 | 0% | 1.0 | 1 (11-25 22:26Z) |
| us-east-1 use1-az2 | 148 | 3% | 1.4 | 1 (11-24 17:31Z) |
| us-east-1 use1-az4 | 198 | 19% | 2.8 | 2 (11-26 04:56Z) |
| us-east-1 use1-az5 | 183 | 23% | 3.0 | 1 (11-26 04:56Z) |
| us-east-1 use1-az6 | 148 | 21% | 2.9 | 1 (11-24 17:31Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 288 | 51% | 5.3 | 9 (11-25 02:18Z) |
| us-east-2 use2-az3 | 313 | 48% | 5.1 | 1 (11-26 04:56Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 139 | 15% | 2.4 | 1 (11-25 22:26Z) |
| us-west-2 usw2-az3 | 219 | 16% | 2.6 | 1 (11-25 12:40Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 571 | 73% | 7.4 | 9 (11-26 04:56Z) |
| ap-northeast-1 | 571 | 73% | 7.0 | 1 (11-26 04:56Z) |
| ap-northeast-2 | 571 | 100% | 9.0 | 9 (11-26 04:56Z) |
| ap-south-1 | 571 | 57% | 5.9 | 1 (11-26 04:56Z) |
| ap-southeast-2 | 571 | 28% | 3.7 | 1 (11-26 04:56Z) |
| ap-southeast-3 | 571 | 22% | 3.0 | 1 (11-26 04:56Z) |
| us-east-1 | 571 | 74% | 6.6 | 8 (11-26 04:56Z) |
| us-east-2 | 571 | 68% | 6.7 | 9 (11-26 04:56Z) |
| us-west-2 | 571 | 52% | 5.7 | 9 (11-26 04:56Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992894299999999992292991993991999999999999291991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111119111111991111111111111111111191121122141151
ap-southeast-2   991991191329999911181911911991199999199919191911
ap-southeast-3   311111111111211311131111111111111111111111111111
us-east-1        968966978999997999998889888888899999899998788878
us-east-2        919999999999999919999589929919932911199493999339
us-west-2        933434194239939991159954535324444995699995969949
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 373 | 86% | 8.1 | 9 (11-26 04:56Z) |
| ap-east-1 ape1-az2 | 336 | 88% | 8.3 | 9 (11-26 04:56Z) |
| ap-east-1 ape1-az3 | 370 | 88% | 8.3 | 9 (11-26 04:56Z) |
| ap-northeast-1 apne1-az1 | 229 | 95% | 8.7 | 9 (11-25 22:26Z) |
| ap-northeast-1 apne1-az2 | 216 | 88% | 8.2 | 9 (11-25 22:26Z) |
| ap-northeast-1 apne1-az4 | 294 | 99% | 8.9 | 9 (11-25 22:26Z) |
| ap-northeast-2 apne2-az1 | 460 | 100% | 9.0 | 9 (11-25 22:26Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 482 | 100% | 9.0 | 9 (11-26 04:56Z) |
| ap-northeast-2 apne2-az4 | 377 | 88% | 8.2 | 9 (11-25 22:26Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 202 | 90% | 8.4 | 3 (11-25 22:26Z) |
| ap-southeast-2 apse2-az1 | 83 | 88% | 8.2 | 9 (11-24 17:31Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 96 | 85% | 8.1 | 9 (11-25 12:40Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 162 | 90% | 8.3 | 3 (11-26 04:56Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 206 | 99% | 8.9 | 9 (11-26 04:56Z) |
| us-east-2 use2-az2 | 223 | 99% | 8.9 | 9 (11-25 02:18Z) |
| us-east-2 use2-az3 | 248 | 97% | 8.8 | 9 (11-25 02:18Z) |
| us-west-2 usw2-az1 | 112 | 98% | 8.9 | 9 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 99 | 91% | 8.4 | 9 (11-25 12:40Z) |
| us-west-2 usw2-az3 | 152 | 88% | 8.2 | 2 (11-26 04:56Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708300 | 2026-11-26T04:56:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-26T04:56:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.733600 | 2026-11-26T04:56:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.612000 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.627300 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.609300 | 2026-11-26T04:56:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-26T04:56:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.741700 | 2026-11-26T04:56:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.400700 | 2026-11-26T04:56:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.706400 | 2026-11-26T04:56:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.416800 | 2026-11-26T04:56:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.680900 | 2026-11-26T04:56:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512200 | 2026-11-26T04:56:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.554600 | 2026-11-26T04:56:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.527700 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.827600 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.901700 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1b | Windows | 0.337500 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.838800 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.854400 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.859400 | 2026-11-26T04:56:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.540100 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549700 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549000 | 2026-11-26T04:56:49Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568400 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2a | Windows | 0.296200 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.877400 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.533900 | 2026-11-26T04:56:49Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-26T04:56:49Z |
