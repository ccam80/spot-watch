# Spot placement score log

Generated 2026-11-22 19:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 562 | 47% | 5.1 | 1 (11-22 19:28Z) |
| ap-northeast-1 | 562 | 18% | 2.9 | 9 (11-22 19:28Z) |
| ap-northeast-2 | 562 | 68% | 7.0 | 1 (11-22 19:28Z) |
| ap-south-1 | 562 | 3% | 1.7 | 1 (11-22 19:28Z) |
| ap-southeast-2 | 562 | 1% | 1.0 | 1 (11-22 19:28Z) |
| ap-southeast-3 | 562 | 23% | 3.0 | 1 (11-22 19:28Z) |
| us-east-1 | 562 | 13% | 2.8 | 5 (11-22 19:28Z) |
| us-east-2 | 562 | 30% | 3.6 | 1 (11-22 19:28Z) |
| us-west-2 | 562 | 9% | 2.1 | 9 (11-22 19:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        819919121911111111199199611391191111111111111111
ap-northeast-1   911211111511121129995999991191211221211299999129
ap-northeast-2   999999991911111111199999999799171691999199991111
ap-south-1       911112211111111111111191111111111111111111191121
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111311111111111211311131111111111111111111
us-east-1        329293322423233344223323737465467654656566754465
us-east-2        999111111111111111119919919991119918111111111111
us-west-2        211111212221112122111219111121121212112111521319
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
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 135 | 11% | 2.0 | 1 (11-21 01:25Z) |
| ap-northeast-1 apne1-az4 | 266 | 29% | 3.6 | 9 (11-22 19:28Z) |
| ap-northeast-2 apne2-az1 | 469 | 63% | 6.6 | 1 (11-22 11:09Z) |
| ap-northeast-2 apne2-az3 | 513 | 68% | 6.9 | 1 (11-22 19:28Z) |
| ap-northeast-2 apne2-az4 | 542 | 71% | 7.2 | 1 (11-22 19:28Z) |
| ap-south-1 aps1-az1 | 167 | 2% | 1.4 | 1 (11-22 11:09Z) |
| ap-south-1 aps1-az3 | 164 | 7% | 2.3 | 1 (11-22 19:28Z) |
| ap-southeast-2 apse2-az1 | 115 | 3% | 1.2 | 1 (11-22 19:28Z) |
| ap-southeast-2 apse2-az2 | 83 | 0% | 1.0 | 1 (11-22 19:28Z) |
| ap-southeast-3 apse3-az1 | 102 | 0% | 1.0 | 1 (11-22 11:09Z) |
| ap-southeast-3 apse3-az3 | 334 | 36% | 4.2 | 1 (11-21 01:25Z) |
| us-east-1 use1-az1 | 124 | 0% | 1.0 | 1 (11-22 19:28Z) |
| us-east-1 use1-az2 | 147 | 3% | 1.4 | 1 (11-22 11:09Z) |
| us-east-1 use1-az4 | 190 | 20% | 2.8 | 2 (11-22 11:09Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 147 | 21% | 2.9 | 2 (11-22 11:09Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 286 | 51% | 5.3 | 1 (11-22 11:09Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 180 | 21% | 3.0 | 9 (11-22 19:28Z) |
| us-west-2 usw2-az2 | 134 | 16% | 2.4 | 1 (11-22 19:28Z) |
| us-west-2 usw2-az3 | 216 | 16% | 2.6 | 9 (11-22 19:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 562 | 73% | 7.4 | 9 (11-22 19:28Z) |
| ap-northeast-1 | 562 | 73% | 7.0 | 9 (11-22 19:28Z) |
| ap-northeast-2 | 562 | 100% | 9.0 | 9 (11-22 19:28Z) |
| ap-south-1 | 562 | 58% | 5.9 | 1 (11-22 19:28Z) |
| ap-southeast-2 | 562 | 28% | 3.7 | 9 (11-22 19:28Z) |
| ap-southeast-3 | 562 | 23% | 3.0 | 1 (11-22 19:28Z) |
| us-east-1 | 562 | 73% | 6.6 | 9 (11-22 19:28Z) |
| us-east-2 | 562 | 68% | 6.7 | 9 (11-22 19:28Z) |
| us-west-2 | 562 | 51% | 5.6 | 9 (11-22 19:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   993922992992894299999999992292991993991999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       991392291111119111111991111111111111111111191121
ap-southeast-2   911911911991991191329999911181911911991199999199
ap-southeast-3   111111111311111111111211311131111111111111111111
us-east-1        999599669968966978999997999998889888888899999899
us-east-2        999119919919999999999999919999589929919932911199
us-west-2        999494334933434194239939991159954535324444995699
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
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 364 | 85% | 8.1 | 9 (11-22 11:09Z) |
| ap-east-1 ape1-az2 | 332 | 88% | 8.3 | 9 (11-22 19:28Z) |
| ap-east-1 ape1-az3 | 362 | 88% | 8.3 | 9 (11-22 19:28Z) |
| ap-northeast-1 apne1-az1 | 226 | 95% | 8.7 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az2 | 213 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az4 | 290 | 99% | 8.9 | 9 (11-22 11:09Z) |
| ap-northeast-2 apne2-az1 | 454 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az2 | 128 | 88% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 473 | 100% | 9.0 | 9 (11-22 19:28Z) |
| ap-northeast-2 apne2-az4 | 371 | 87% | 8.2 | 9 (11-22 19:28Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 80 | 88% | 8.2 | 9 (11-22 19:28Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 94 | 85% | 8.1 | 9 (11-22 19:28Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 121 | 99% | 9.0 | 9 (11-22 19:28Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 116 | 98% | 8.9 | 9 (11-22 19:28Z) |
| us-east-1 use1-az6 | 143 | 93% | 8.5 | 9 (11-22 11:09Z) |
| us-east-2 use2-az1 | 201 | 99% | 8.9 | 9 (11-22 11:09Z) |
| us-east-2 use2-az2 | 220 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az3 | 245 | 97% | 8.8 | 9 (11-21 09:39Z) |
| us-west-2 usw2-az1 | 106 | 98% | 8.9 | 9 (11-22 19:28Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 146 | 88% | 8.2 | 9 (11-22 19:28Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.704500 | 2026-11-22T19:28:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-22T19:28:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.724000 | 2026-11-22T19:28:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.615200 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.589500 | 2026-11-22T19:28:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-22T19:28:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.709300 | 2026-11-22T19:28:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.423400 | 2026-11-22T19:28:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.768400 | 2026-11-22T19:28:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.424700 | 2026-11-22T19:28:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.635800 | 2026-11-22T19:28:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.532000 | 2026-11-22T19:28:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.519900 | 2026-11-22T19:28:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.547400 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.858800 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.893300 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1b | Windows | 0.311200 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.751200 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.802200 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.742500 | 2026-11-22T19:28:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.528900 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536200 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.527000 | 2026-11-22T19:28:32Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579400 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2a | Windows | 0.304600 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.792700 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526200 | 2026-11-22T19:28:32Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-22T19:28:32Z |
