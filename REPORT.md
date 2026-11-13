# Spot placement score log

Generated 2026-11-13 00:11 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 529 | 49% | 5.2 | 1 (11-13 00:11Z) |
| ap-northeast-1 | 529 | 16% | 2.7 | 1 (11-13 00:11Z) |
| ap-northeast-2 | 529 | 69% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 | 529 | 3% | 1.7 | 1 (11-13 00:11Z) |
| ap-southeast-2 | 529 | 1% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 | 529 | 24% | 3.1 | 1 (11-13 00:11Z) |
| us-east-1 | 529 | 10% | 2.6 | 3 (11-13 00:11Z) |
| us-east-2 | 529 | 30% | 3.6 | 1 (11-13 00:11Z) |
| us-west-2 | 529 | 9% | 2.1 | 2 (11-13 00:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999191911112991119199991999819919121911111
ap-northeast-1   478881951191191112211211119199919911211111511121
ap-northeast-2   999999999999992999999999999999999999999991911111
ap-south-1       111111698111111211122222122211311911112211111111
ap-southeast-2   111111111111111117111111111111111111111111111111
ap-southeast-3   839731386181111111111311111111113111111111311111
us-east-1        111112999912112333332232213222222329293322423233
us-east-2        911969999991191211191111111999919999111111111111
us-west-2        111111711121122211191111122922111211111212221112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 167 | 5% | 1.5 | 1 (11-13 00:11Z) |
| ap-east-1 ape1-az2 | 389 | 66% | 6.6 | 1 (11-13 00:11Z) |
| ap-northeast-1 apne1-az1 | 122 | 10% | 1.9 | 1 (11-12 02:52Z) |
| ap-northeast-1 apne1-az4 | 241 | 26% | 3.5 | 1 (11-13 00:11Z) |
| ap-northeast-2 apne2-az1 | 454 | 63% | 6.6 | 1 (11-13 00:11Z) |
| ap-northeast-2 apne2-az3 | 488 | 69% | 7.0 | 1 (11-12 10:55Z) |
| ap-northeast-2 apne2-az4 | 520 | 70% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 154 | 1% | 1.3 | 1 (11-12 02:52Z) |
| ap-south-1 aps1-az3 | 153 | 7% | 2.3 | 1 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 108 | 3% | 1.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 apse2-az2 | 74 | 0% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 322 | 38% | 4.3 | 1 (11-12 02:52Z) |
| us-east-1 use1-az1 | 109 | 0% | 1.1 | 1 (11-12 10:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 167 | 23% | 3.0 | 1 (11-12 10:55Z) |
| us-east-1 use1-az5 | 171 | 25% | 3.1 | 1 (11-13 00:11Z) |
| us-east-1 use1-az6 | 128 | 24% | 3.0 | 1 (11-12 10:55Z) |
| us-east-2 use2-az1 | 228 | 43% | 4.6 | 1 (11-12 10:55Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 124 | 17% | 2.5 | 1 (11-12 02:52Z) |
| us-west-2 usw2-az3 | 202 | 17% | 2.7 | 1 (11-12 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 529 | 71% | 7.3 | 9 (11-13 00:11Z) |
| ap-northeast-1 | 529 | 72% | 7.0 | 4 (11-13 00:11Z) |
| ap-northeast-2 | 529 | 100% | 9.0 | 9 (11-13 00:11Z) |
| ap-south-1 | 529 | 61% | 6.2 | 9 (11-13 00:11Z) |
| ap-southeast-2 | 529 | 26% | 3.6 | 1 (11-13 00:11Z) |
| ap-southeast-3 | 529 | 24% | 3.1 | 1 (11-13 00:11Z) |
| us-east-1 | 529 | 71% | 6.5 | 6 (11-13 00:11Z) |
| us-east-2 | 529 | 67% | 6.6 | 9 (11-13 00:11Z) |
| us-west-2 | 529 | 51% | 5.6 | 4 (11-13 00:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999299999219919922999999999993922992992894
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999119112911922992199217911991392291111119
ap-southeast-2   999991991111191119199119999999919911911911991991
ap-southeast-3   839731386181111111111311111111113111111111311111
us-east-1        999999999945234697655579579999999999599669968966
us-east-2        919999999991991991291119119999999999119919919999
us-west-2        999999994492445434294944195955999999494334933434
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 8 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 340 | 84% | 8.0 | 9 (11-13 00:11Z) |
| ap-east-1 ape1-az2 | 306 | 87% | 8.2 | 9 (11-13 00:11Z) |
| ap-east-1 ape1-az3 | 338 | 87% | 8.2 | 9 (11-13 00:11Z) |
| ap-northeast-1 apne1-az1 | 213 | 95% | 8.7 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az2 | 195 | 86% | 8.2 | 9 (11-12 18:50Z) |
| ap-northeast-1 apne1-az4 | 275 | 99% | 8.9 | 9 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 429 | 100% | 9.0 | 9 (11-13 00:11Z) |
| ap-northeast-2 apne2-az2 | 115 | 86% | 8.1 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az3 | 446 | 100% | 9.0 | 9 (11-13 00:11Z) |
| ap-northeast-2 apne2-az4 | 348 | 86% | 8.2 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 71 | 86% | 8.1 | 9 (11-12 10:55Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 151 | 91% | 8.4 | 9 (11-12 10:55Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 133 | 92% | 8.5 | 9 (11-10 09:39Z) |
| us-east-2 use2-az1 | 186 | 99% | 8.9 | 5 (11-13 00:11Z) |
| us-east-2 use2-az2 | 206 | 99% | 8.9 | 7 (11-13 00:11Z) |
| us-east-2 use2-az3 | 232 | 97% | 8.7 | 9 (11-12 18:50Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707600 | 2026-11-13T00:11:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-13T00:11:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.707700 | 2026-11-13T00:11:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.578200 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.597300 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.581700 | 2026-11-13T00:11:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-13T00:11:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.589300 | 2026-11-13T00:11:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.397500 | 2026-11-13T00:11:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.562300 | 2026-11-13T00:11:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.373500 | 2026-11-13T00:11:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.592700 | 2026-11-13T00:11:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.491300 | 2026-11-13T00:11:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.597000 | 2026-11-13T00:11:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.512200 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.750400 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.723900 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.568000 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520900 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.505800 | 2026-11-13T00:11:12Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550100 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551800 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548800 | 2026-11-13T00:11:12Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.594400 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2a | Windows | 0.325700 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.603500 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2b | Windows | 0.297300 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.602400 | 2026-11-13T00:11:12Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-13T00:11:12Z |
