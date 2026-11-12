# Spot placement score log

Generated 2026-11-12 02:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 526 | 49% | 5.2 | 1 (11-12 02:52Z) |
| ap-northeast-1 | 526 | 16% | 2.7 | 1 (11-12 02:52Z) |
| ap-northeast-2 | 526 | 69% | 7.1 | 1 (11-12 02:52Z) |
| ap-south-1 | 526 | 3% | 1.7 | 1 (11-12 02:52Z) |
| ap-southeast-2 | 526 | 1% | 1.0 | 1 (11-12 02:52Z) |
| ap-southeast-3 | 526 | 24% | 3.2 | 1 (11-12 02:52Z) |
| us-east-1 | 526 | 10% | 2.6 | 3 (11-12 02:52Z) |
| us-east-2 | 526 | 30% | 3.6 | 1 (11-12 02:52Z) |
| us-west-2 | 526 | 9% | 2.1 | 1 (11-12 02:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111999999999191911112991119199991999819919121911
ap-northeast-1   111478881951191191112211211119199919911211111511
ap-northeast-2   199999999999999992999999999999999999999999991911
ap-south-1       111111111698111111211122222122211311911112211111
ap-southeast-2   111111111111111111117111111111111111111111111111
ap-southeast-3   111839731386181111111111311111111113111111111311
us-east-1        111111112999912112333332232213222222329293322423
us-east-2        199911969999991191211191111111999919999111111111
us-west-2        111111111711121122211191111122922111211111212221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 164 | 5% | 1.5 | 1 (11-11 21:20Z) |
| ap-east-1 ape1-az2 | 386 | 66% | 6.7 | 9 (11-11 14:05Z) |
| ap-northeast-1 apne1-az1 | 122 | 10% | 1.9 | 1 (11-12 02:52Z) |
| ap-northeast-1 apne1-az4 | 239 | 26% | 3.5 | 1 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 451 | 63% | 6.6 | 9 (11-11 14:05Z) |
| ap-northeast-2 apne2-az3 | 487 | 69% | 7.0 | 1 (11-12 02:52Z) |
| ap-northeast-2 apne2-az4 | 518 | 70% | 7.2 | 1 (11-11 21:20Z) |
| ap-south-1 aps1-az1 | 154 | 1% | 1.3 | 1 (11-12 02:52Z) |
| ap-south-1 aps1-az3 | 151 | 7% | 2.3 | 1 (11-11 21:20Z) |
| ap-southeast-2 apse2-az1 | 108 | 3% | 1.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 apse2-az2 | 73 | 0% | 1.0 | 1 (11-12 02:52Z) |
| ap-southeast-3 apse3-az1 | 91 | 0% | 1.0 | 1 (11-11 21:20Z) |
| ap-southeast-3 apse3-az3 | 322 | 38% | 4.3 | 1 (11-12 02:52Z) |
| us-east-1 use1-az1 | 108 | 0% | 1.1 | 1 (11-10 17:42Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 166 | 23% | 3.0 | 3 (11-10 01:27Z) |
| us-east-1 use1-az5 | 169 | 25% | 3.1 | 1 (11-11 21:20Z) |
| us-east-1 use1-az6 | 127 | 24% | 3.1 | 1 (11-12 02:52Z) |
| us-east-2 use2-az1 | 227 | 43% | 4.6 | 1 (11-12 02:52Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 298 | 47% | 5.1 | 1 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 167 | 22% | 3.1 | 1 (11-11 21:20Z) |
| us-west-2 usw2-az2 | 124 | 17% | 2.5 | 1 (11-12 02:52Z) |
| us-west-2 usw2-az3 | 201 | 17% | 2.7 | 1 (11-11 14:05Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 526 | 71% | 7.3 | 9 (11-12 02:52Z) |
| ap-northeast-1 | 526 | 72% | 7.0 | 2 (11-12 02:52Z) |
| ap-northeast-2 | 526 | 100% | 9.0 | 9 (11-12 02:52Z) |
| ap-south-1 | 526 | 61% | 6.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 | 526 | 26% | 3.5 | 1 (11-12 02:52Z) |
| ap-southeast-3 | 526 | 24% | 3.2 | 1 (11-12 02:52Z) |
| us-east-1 | 526 | 71% | 6.5 | 8 (11-12 02:52Z) |
| us-east-2 | 526 | 67% | 6.6 | 9 (11-12 02:52Z) |
| us-west-2 | 526 | 52% | 5.7 | 3 (11-12 02:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999299999219919922999999999993922992992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999119112911922992199217911991392291111
ap-southeast-2   999999991991111191119199119999999919911911911991
ap-southeast-3   111839731386181111111111311111111113111111111311
us-east-1        229999999999945234697655579579999999999599669968
us-east-2        299919999999991991991291119119999999999119919919
us-west-2        929999999994492445434294944195955999999494334933
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 8 | 6 | 6 | 5 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 338 | 84% | 8.0 | 9 (11-12 02:52Z) |
| ap-east-1 ape1-az2 | 303 | 86% | 8.2 | 9 (11-12 02:52Z) |
| ap-east-1 ape1-az3 | 336 | 87% | 8.2 | 9 (11-12 02:52Z) |
| ap-northeast-1 apne1-az1 | 213 | 95% | 8.7 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az2 | 194 | 86% | 8.1 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az4 | 275 | 99% | 8.9 | 9 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 426 | 100% | 9.0 | 9 (11-12 02:52Z) |
| ap-northeast-2 apne2-az2 | 113 | 86% | 8.1 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az3 | 443 | 100% | 9.0 | 8 (11-12 02:52Z) |
| ap-northeast-2 apne2-az4 | 345 | 86% | 8.2 | 9 (11-12 02:52Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 199 | 90% | 8.4 | 9 (11-10 23:11Z) |
| ap-southeast-2 apse2-az1 | 70 | 86% | 8.1 | 9 (11-11 21:20Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 81 | 83% | 7.9 | 1 (11-12 02:52Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 150 | 91% | 8.4 | 2 (11-12 02:52Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 133 | 92% | 8.5 | 9 (11-10 09:39Z) |
| us-east-2 use2-az1 | 184 | 99% | 8.9 | 9 (11-11 05:59Z) |
| us-east-2 use2-az2 | 204 | 99% | 8.9 | 9 (11-12 02:52Z) |
| us-east-2 use2-az3 | 231 | 97% | 8.7 | 9 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710900 | 2026-11-12T02:52:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-12T02:52:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.708500 | 2026-11-12T02:52:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.578400 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.593700 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.575700 | 2026-11-12T02:52:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-12T02:52:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.577800 | 2026-11-12T02:52:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.401300 | 2026-11-12T02:52:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.554700 | 2026-11-12T02:52:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.372300 | 2026-11-12T02:52:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.595200 | 2026-11-12T02:52:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497400 | 2026-11-12T02:52:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.615200 | 2026-11-12T02:52:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.527200 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.726400 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.684900 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.554100 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500800 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.487600 | 2026-11-12T02:52:44Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.551100 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551600 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549600 | 2026-11-12T02:52:44Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566500 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2a | Windows | 0.320100 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.618900 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2b | Windows | 0.302500 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.590800 | 2026-11-12T02:52:44Z |
| us-west-2 | us-west-2c | Windows | 0.285900 | 2026-11-12T02:52:44Z |
