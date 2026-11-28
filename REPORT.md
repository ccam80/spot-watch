# Spot placement score log

Generated 2026-11-28 15:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 596 | 46% | 4.9 | 9 (11-28 15:12Z) |
| ap-northeast-1 | 596 | 18% | 2.9 | 9 (11-28 15:12Z) |
| ap-northeast-2 | 596 | 67% | 6.9 | 1 (11-28 15:12Z) |
| ap-south-1 | 596 | 3% | 1.6 | 2 (11-28 15:12Z) |
| ap-southeast-2 | 596 | 1% | 1.1 | 1 (11-28 15:12Z) |
| ap-southeast-3 | 596 | 22% | 3.0 | 7 (11-28 15:12Z) |
| us-east-1 | 596 | 13% | 2.8 | 2 (11-28 15:12Z) |
| us-east-2 | 596 | 29% | 3.5 | 2 (11-28 15:12Z) |
| us-west-2 | 596 | 11% | 2.3 | 9 (11-28 15:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111119111111111911911111199999
ap-northeast-1   212112999991292111111912111619991111122121233999
ap-northeast-2   919991999911111199999119119998999999111151192111
ap-south-1       111111111911211221111212221111111111111111111112
ap-southeast-2   111111111111111111111111111111211111111111125591
ap-southeast-3   111111111111111111111111111111111111131111386687
us-east-1        546565667544654554445354343343333334443334233452
us-east-2        181111111111111111191111111111111111111111142272
us-west-2        121121115213191121211232113333979979999112999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 7 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 186 | 5% | 1.5 | 1 (11-28 12:18Z) |
| ap-east-1 ape1-az2 | 412 | 66% | 6.6 | 9 (11-28 15:12Z) |
| ap-northeast-1 apne1-az1 | 152 | 10% | 2.0 | 4 (11-28 15:12Z) |
| ap-northeast-1 apne1-az4 | 281 | 30% | 3.7 | 9 (11-28 15:12Z) |
| ap-northeast-2 apne2-az1 | 486 | 64% | 6.6 | 2 (11-28 08:17Z) |
| ap-northeast-2 apne2-az3 | 533 | 67% | 6.8 | 9 (11-28 11:12Z) |
| ap-northeast-2 apne2-az4 | 561 | 70% | 7.1 | 9 (11-28 11:12Z) |
| ap-south-1 aps1-az1 | 184 | 2% | 1.3 | 1 (11-28 15:12Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 130 | 4% | 1.3 | 9 (11-28 14:12Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 111 | 0% | 1.0 | 1 (11-28 10:12Z) |
| ap-southeast-3 apse3-az3 | 349 | 36% | 4.2 | 7 (11-28 15:12Z) |
| us-east-1 use1-az1 | 135 | 0% | 1.0 | 1 (11-28 07:14Z) |
| us-east-1 use1-az2 | 158 | 3% | 1.3 | 1 (11-28 13:12Z) |
| us-east-1 use1-az4 | 215 | 18% | 2.7 | 2 (11-28 14:12Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 162 | 19% | 2.7 | 1 (11-28 15:12Z) |
| us-east-2 use2-az1 | 253 | 41% | 4.5 | 1 (11-28 15:12Z) |
| us-east-2 use2-az2 | 298 | 49% | 5.1 | 2 (11-28 11:12Z) |
| us-east-2 use2-az3 | 319 | 47% | 5.0 | 2 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 197 | 25% | 3.3 | 9 (11-28 15:12Z) |
| us-west-2 usw2-az2 | 148 | 16% | 2.4 | 6 (11-28 15:12Z) |
| us-west-2 usw2-az3 | 237 | 19% | 2.8 | 9 (11-28 15:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 596 | 74% | 7.5 | 9 (11-28 15:12Z) |
| ap-northeast-1 | 596 | 73% | 7.1 | 9 (11-28 15:12Z) |
| ap-northeast-2 | 596 | 100% | 9.0 | 9 (11-28 15:12Z) |
| ap-south-1 | 596 | 57% | 5.8 | 4 (11-28 15:12Z) |
| ap-southeast-2 | 596 | 31% | 3.9 | 9 (11-28 15:12Z) |
| ap-southeast-3 | 596 | 22% | 3.0 | 7 (11-28 15:12Z) |
| us-east-1 | 596 | 75% | 6.7 | 9 (11-28 15:12Z) |
| us-east-2 | 596 | 67% | 6.6 | 9 (11-28 15:12Z) |
| us-west-2 | 596 | 54% | 5.8 | 9 (11-28 15:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   939919999999999992919919929999999999999999999999
ap-northeast-2   999999999999999999999999929999999999999999999999
ap-south-1       111111111911211221411512929999999999196811111124
ap-southeast-2   119911999991999191919119919999999999999999999999
ap-southeast-3   111111111111111111111111111111111111131111386687
us-east-1        888888999998999987888788987788787899999999999999
us-east-2        299199329111994939993399292212221112999999999999
us-west-2        353244449956999959699499999999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 389 | 86% | 8.2 | 9 (11-28 13:12Z) |
| ap-east-1 ape1-az2 | 347 | 88% | 8.3 | 9 (11-28 15:12Z) |
| ap-east-1 ape1-az3 | 384 | 89% | 8.3 | 9 (11-28 15:12Z) |
| ap-northeast-1 apne1-az1 | 239 | 95% | 8.7 | 9 (11-28 13:12Z) |
| ap-northeast-1 apne1-az2 | 224 | 88% | 8.3 | 9 (11-28 13:12Z) |
| ap-northeast-1 apne1-az4 | 309 | 99% | 8.9 | 9 (11-28 13:12Z) |
| ap-northeast-2 apne2-az1 | 473 | 100% | 9.0 | 9 (11-28 13:12Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 497 | 100% | 9.0 | 9 (11-28 15:12Z) |
| ap-northeast-2 apne2-az4 | 386 | 88% | 8.3 | 9 (11-28 14:12Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 92 | 89% | 8.3 | 9 (11-28 15:12Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 109 | 87% | 8.2 | 9 (11-28 14:12Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 36 | 58% | 6.0 | 9 (11-28 13:12Z) |
| us-east-1 use1-az2 | 133 | 99% | 9.0 | 9 (11-28 15:12Z) |
| us-east-1 use1-az4 | 168 | 90% | 8.3 | 9 (11-28 15:12Z) |
| us-east-1 use1-az5 | 119 | 98% | 8.9 | 9 (11-28 15:12Z) |
| us-east-1 use1-az6 | 154 | 94% | 8.5 | 9 (11-28 14:12Z) |
| us-east-2 use2-az1 | 216 | 99% | 8.9 | 9 (11-28 14:12Z) |
| us-east-2 use2-az2 | 229 | 99% | 8.9 | 9 (11-28 15:12Z) |
| us-east-2 use2-az3 | 257 | 97% | 8.8 | 9 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 118 | 98% | 8.9 | 9 (11-28 15:12Z) |
| us-west-2 usw2-az2 | 115 | 92% | 8.4 | 9 (11-28 14:12Z) |
| us-west-2 usw2-az3 | 165 | 89% | 8.2 | 9 (11-28 15:12Z) |
| us-west-2 usw2-az4 | 1 | 100% | 9.0 | 9 (11-28 12:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T15:12:59Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T15:12:59Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732400 | 2026-11-28T15:12:59Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.620900 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.630300 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.621200 | 2026-11-28T15:12:59Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T15:12:59Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.728000 | 2026-11-28T15:12:59Z |
| ap-south-1 | ap-south-1a | Windows | 0.386000 | 2026-11-28T15:12:59Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.681100 | 2026-11-28T15:12:59Z |
| ap-south-1 | ap-south-1b | Windows | 0.394600 | 2026-11-28T15:12:59Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.705400 | 2026-11-28T15:12:59Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.498100 | 2026-11-28T15:12:59Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.584000 | 2026-11-28T15:12:59Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519000 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.785900 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.922300 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1b | Windows | 0.347600 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.890300 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1c | Windows | 0.287000 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.878600 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.877200 | 2026-11-28T15:12:59Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548800 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.554100 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T15:12:59Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.643100 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2a | Windows | 0.291000 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.906000 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548300 | 2026-11-28T15:12:59Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T15:12:59Z |
