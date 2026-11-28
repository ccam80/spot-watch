# Spot placement score log

Generated 2026-11-28 20:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 601 | 46% | 5.0 | 9 (11-28 20:13Z) |
| ap-northeast-1 | 601 | 19% | 2.9 | 9 (11-28 20:13Z) |
| ap-northeast-2 | 601 | 68% | 6.9 | 9 (11-28 20:13Z) |
| ap-south-1 | 601 | 3% | 1.7 | 9 (11-28 20:13Z) |
| ap-southeast-2 | 601 | 1% | 1.1 | 7 (11-28 20:13Z) |
| ap-southeast-3 | 601 | 23% | 3.0 | 8 (11-28 20:13Z) |
| us-east-1 | 601 | 13% | 2.8 | 4 (11-28 20:13Z) |
| us-east-2 | 601 | 28% | 3.5 | 2 (11-28 20:13Z) |
| us-west-2 | 601 | 11% | 2.3 | 3 (11-28 20:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111911111111191191111119999999999
ap-northeast-1   299999129211111191211161999111112212123399999199
ap-northeast-2   199991111119999911911999899999911115119211199999
ap-south-1       111191121122111121222111111111111111111111211199
ap-southeast-2   111111111111111111111111121111111111112559113247
ap-southeast-3   111111111111111111111111111111113111138668783268
us-east-1        566754465455444535434334333333444333423345244444
us-east-2        111111111111119111111111111111111111114227222222
us-west-2        111521319112121123211333397997999911299999991113
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 7 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 187 | 5% | 1.5 | 1 (11-28 18:15Z) |
| ap-east-1 ape1-az2 | 417 | 66% | 6.6 | 9 (11-28 20:13Z) |
| ap-northeast-1 apne1-az1 | 156 | 10% | 2.0 | 3 (11-28 20:13Z) |
| ap-northeast-1 apne1-az4 | 286 | 30% | 3.8 | 9 (11-28 20:13Z) |
| ap-northeast-2 apne2-az1 | 487 | 64% | 6.6 | 9 (11-28 16:14Z) |
| ap-northeast-2 apne2-az3 | 538 | 67% | 6.8 | 9 (11-28 20:13Z) |
| ap-northeast-2 apne2-az4 | 566 | 70% | 7.1 | 9 (11-28 20:13Z) |
| ap-south-1 aps1-az1 | 186 | 3% | 1.4 | 9 (11-28 20:13Z) |
| ap-south-1 aps1-az3 | 172 | 8% | 2.3 | 9 (11-28 20:13Z) |
| ap-southeast-2 apse2-az1 | 134 | 4% | 1.4 | 7 (11-28 20:13Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 112 | 0% | 1.0 | 1 (11-28 18:15Z) |
| ap-southeast-3 apse3-az3 | 354 | 36% | 4.2 | 8 (11-28 20:13Z) |
| us-east-1 use1-az1 | 136 | 0% | 1.0 | 1 (11-28 17:11Z) |
| us-east-1 use1-az2 | 158 | 3% | 1.3 | 1 (11-28 13:12Z) |
| us-east-1 use1-az4 | 219 | 17% | 2.7 | 2 (11-28 19:11Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 162 | 19% | 2.7 | 1 (11-28 15:12Z) |
| us-east-2 use2-az1 | 253 | 41% | 4.5 | 1 (11-28 15:12Z) |
| us-east-2 use2-az2 | 299 | 49% | 5.1 | 1 (11-28 18:15Z) |
| us-east-2 use2-az3 | 319 | 47% | 5.0 | 2 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 199 | 26% | 3.3 | 2 (11-28 20:13Z) |
| us-west-2 usw2-az2 | 148 | 16% | 2.4 | 6 (11-28 15:12Z) |
| us-west-2 usw2-az3 | 239 | 19% | 2.8 | 1 (11-28 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 601 | 75% | 7.5 | 9 (11-28 20:13Z) |
| ap-northeast-1 | 601 | 74% | 7.1 | 9 (11-28 20:13Z) |
| ap-northeast-2 | 601 | 100% | 9.0 | 9 (11-28 20:13Z) |
| ap-south-1 | 601 | 57% | 5.9 | 9 (11-28 20:13Z) |
| ap-southeast-2 | 601 | 31% | 3.9 | 9 (11-28 20:13Z) |
| ap-southeast-3 | 601 | 23% | 3.0 | 8 (11-28 20:13Z) |
| us-east-1 | 601 | 75% | 6.7 | 9 (11-28 20:13Z) |
| us-east-2 | 601 | 67% | 6.6 | 5 (11-28 20:13Z) |
| us-west-2 | 601 | 54% | 5.8 | 9 (11-28 20:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999291991992999999999999999999999999999
ap-northeast-2   999999999999999999992999999999999999999999999999
ap-south-1       111191121122141151292999999999919681111112413999
ap-southeast-2   199999199919191911991999999999999999999999999999
ap-southeast-3   111111111111111111111111111111113111138668783268
us-east-1        899999899998788878898778878789999999999999999999
us-east-2        932911199493999339929221222111299999999999999995
us-west-2        444995699995969949999999999999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 6 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 6 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 393 | 86% | 8.2 | 9 (11-28 20:13Z) |
| ap-east-1 ape1-az2 | 349 | 88% | 8.3 | 9 (11-28 20:13Z) |
| ap-east-1 ape1-az3 | 386 | 89% | 8.3 | 9 (11-28 18:15Z) |
| ap-northeast-1 apne1-az1 | 241 | 95% | 8.7 | 9 (11-28 20:13Z) |
| ap-northeast-1 apne1-az2 | 226 | 88% | 8.3 | 9 (11-28 18:15Z) |
| ap-northeast-1 apne1-az4 | 313 | 99% | 8.9 | 9 (11-28 20:13Z) |
| ap-northeast-2 apne2-az1 | 476 | 100% | 9.0 | 9 (11-28 19:11Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 500 | 100% | 9.0 | 9 (11-28 19:11Z) |
| ap-northeast-2 apne2-az4 | 389 | 88% | 8.3 | 9 (11-28 20:13Z) |
| ap-south-1 aps1-az1 | 189 | 88% | 8.3 | 9 (11-28 19:11Z) |
| ap-south-1 aps1-az2 | 192 | 81% | 7.8 | 9 (11-28 20:13Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 93 | 89% | 8.3 | 9 (11-28 20:13Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 111 | 87% | 8.2 | 9 (11-28 19:11Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 37 | 59% | 6.1 | 9 (11-28 17:11Z) |
| us-east-1 use1-az2 | 137 | 99% | 9.0 | 9 (11-28 20:13Z) |
| us-east-1 use1-az4 | 169 | 90% | 8.3 | 9 (11-28 17:11Z) |
| us-east-1 use1-az5 | 119 | 98% | 8.9 | 9 (11-28 15:12Z) |
| us-east-1 use1-az6 | 158 | 94% | 8.5 | 9 (11-28 20:13Z) |
| us-east-2 use2-az1 | 216 | 99% | 8.9 | 9 (11-28 14:12Z) |
| us-east-2 use2-az2 | 229 | 99% | 8.9 | 9 (11-28 15:12Z) |
| us-east-2 use2-az3 | 261 | 97% | 8.8 | 9 (11-28 19:11Z) |
| us-west-2 usw2-az1 | 119 | 98% | 8.9 | 9 (11-28 20:13Z) |
| us-west-2 usw2-az2 | 117 | 92% | 8.5 | 9 (11-28 17:11Z) |
| us-west-2 usw2-az3 | 168 | 89% | 8.2 | 9 (11-28 19:11Z) |
| us-west-2 usw2-az4 | 1 | 100% | 9.0 | 9 (11-28 12:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712000 | 2026-11-28T20:13:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T20:13:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731800 | 2026-11-28T20:13:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.620900 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.628800 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.621200 | 2026-11-28T20:13:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T20:13:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.715500 | 2026-11-28T20:13:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.384000 | 2026-11-28T20:13:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.675900 | 2026-11-28T20:13:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.394600 | 2026-11-28T20:13:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.707000 | 2026-11-28T20:13:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.498100 | 2026-11-28T20:13:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.584000 | 2026-11-28T20:13:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.516700 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.782200 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.922300 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1b | Windows | 0.350900 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.893900 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1c | Windows | 0.287400 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.878600 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.881200 | 2026-11-28T20:13:24Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548800 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.562100 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T20:13:24Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.643100 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2a | Windows | 0.289600 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.905700 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.550000 | 2026-11-28T20:13:24Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T20:13:24Z |
