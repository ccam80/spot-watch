# Spot placement score log

Generated 2026-11-16 01:54 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 541 | 48% | 5.2 | 1 (11-16 01:54Z) |
| ap-northeast-1 | 541 | 17% | 2.8 | 1 (11-16 01:54Z) |
| ap-northeast-2 | 541 | 69% | 7.0 | 9 (11-16 01:54Z) |
| ap-south-1 | 541 | 3% | 1.7 | 1 (11-16 01:54Z) |
| ap-southeast-2 | 541 | 1% | 1.0 | 1 (11-16 01:54Z) |
| ap-southeast-3 | 541 | 24% | 3.1 | 1 (11-16 01:54Z) |
| us-east-1 | 541 | 10% | 2.7 | 7 (11-16 01:54Z) |
| us-east-2 | 541 | 30% | 3.6 | 9 (11-16 01:54Z) |
| us-west-2 | 541 | 9% | 2.1 | 1 (11-16 01:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911112991119199991999819919121911111111199199611
ap-northeast-1   191112211211119199919911211111511121129995999991
ap-northeast-2   992999999999999999999999999991911111111199999999
ap-south-1       111211122222122211311911112211111111111111191111
ap-southeast-2   111117111111111111111111111111111111111111111111
ap-southeast-3   111111111311111111113111111111311111111111211311
us-east-1        112333332232213222222329293322423233344223323737
us-east-2        191211191111111999919999111111111111111119919919
us-west-2        122211191111122922111211111212221112122111219111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 169 | 5% | 1.5 | 1 (11-16 01:54Z) |
| ap-east-1 ape1-az2 | 395 | 66% | 6.6 | 6 (11-15 16:59Z) |
| ap-northeast-1 apne1-az1 | 130 | 11% | 2.0 | 3 (11-15 21:41Z) |
| ap-northeast-1 apne1-az4 | 251 | 28% | 3.6 | 9 (11-15 21:41Z) |
| ap-northeast-2 apne2-az1 | 461 | 63% | 6.6 | 2 (11-16 01:54Z) |
| ap-northeast-2 apne2-az3 | 500 | 69% | 7.0 | 1 (11-16 01:54Z) |
| ap-northeast-2 apne2-az4 | 528 | 70% | 7.2 | 9 (11-16 01:54Z) |
| ap-south-1 aps1-az1 | 157 | 1% | 1.4 | 3 (11-15 01:47Z) |
| ap-south-1 aps1-az3 | 156 | 7% | 2.3 | 1 (11-16 01:54Z) |
| ap-southeast-2 apse2-az1 | 111 | 3% | 1.2 | 1 (11-15 21:41Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 329 | 37% | 4.2 | 1 (11-15 21:41Z) |
| us-east-1 use1-az1 | 116 | 0% | 1.1 | 1 (11-16 01:54Z) |
| us-east-1 use1-az2 | 141 | 3% | 1.4 | 1 (11-16 01:54Z) |
| us-east-1 use1-az4 | 173 | 22% | 2.9 | 1 (11-16 01:54Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 132 | 23% | 3.0 | 1 (11-14 16:59Z) |
| us-east-2 use2-az1 | 237 | 43% | 4.6 | 9 (11-16 01:54Z) |
| us-east-2 use2-az2 | 275 | 51% | 5.3 | 9 (11-16 01:54Z) |
| us-east-2 use2-az3 | 304 | 47% | 5.1 | 9 (11-15 16:59Z) |
| us-west-2 usw2-az1 | 170 | 22% | 3.0 | 1 (11-15 16:59Z) |
| us-west-2 usw2-az2 | 126 | 17% | 2.5 | 1 (11-15 21:41Z) |
| us-west-2 usw2-az3 | 205 | 17% | 2.7 | 1 (11-15 09:13Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 541 | 72% | 7.3 | 9 (11-16 01:54Z) |
| ap-northeast-1 | 541 | 72% | 7.0 | 2 (11-16 01:54Z) |
| ap-northeast-2 | 541 | 100% | 9.0 | 9 (11-16 01:54Z) |
| ap-south-1 | 541 | 60% | 6.1 | 1 (11-16 01:54Z) |
| ap-southeast-2 | 541 | 27% | 3.6 | 1 (11-16 01:54Z) |
| ap-southeast-3 | 541 | 24% | 3.1 | 1 (11-16 01:54Z) |
| us-east-1 | 541 | 72% | 6.5 | 9 (11-16 01:54Z) |
| us-east-2 | 541 | 68% | 6.7 | 9 (11-16 01:54Z) |
| us-west-2 | 541 | 51% | 5.6 | 1 (11-16 01:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999219919922999999999993922992992894299999999992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       112911922992199217911991392291111119111111991111
ap-southeast-2   191119199119999999919911911911991991191329999911
ap-southeast-3   111111111311111111113111111111311111111111211311
us-east-1        234697655579579999999999599669968966978999997999
us-east-2        991991291119119999999999119919919999999999999919
us-west-2        445434294944195955999999494334933434194239939991
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 7 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 346 | 84% | 8.1 | 9 (11-16 01:54Z) |
| ap-east-1 ape1-az2 | 315 | 87% | 8.2 | 9 (11-16 01:54Z) |
| ap-east-1 ape1-az3 | 346 | 87% | 8.2 | 9 (11-16 01:54Z) |
| ap-northeast-1 apne1-az1 | 217 | 95% | 8.7 | 9 (11-15 21:41Z) |
| ap-northeast-1 apne1-az2 | 202 | 87% | 8.2 | 9 (11-15 21:41Z) |
| ap-northeast-1 apne1-az4 | 279 | 99% | 8.9 | 9 (11-15 21:41Z) |
| ap-northeast-2 apne2-az1 | 439 | 100% | 9.0 | 9 (11-16 01:54Z) |
| ap-northeast-2 apne2-az2 | 119 | 87% | 8.1 | 9 (11-15 21:41Z) |
| ap-northeast-2 apne2-az3 | 453 | 100% | 9.0 | 9 (11-15 21:41Z) |
| ap-northeast-2 apne2-az4 | 353 | 87% | 8.2 | 9 (11-15 01:47Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 87 | 84% | 8.0 | 9 (11-15 16:59Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 117 | 99% | 8.9 | 9 (11-16 01:54Z) |
| us-east-1 use1-az4 | 156 | 92% | 8.4 | 9 (11-16 01:54Z) |
| us-east-1 use1-az5 | 113 | 98% | 8.9 | 9 (11-16 01:54Z) |
| us-east-1 use1-az6 | 138 | 93% | 8.5 | 9 (11-16 01:54Z) |
| us-east-2 use2-az1 | 193 | 99% | 8.9 | 9 (11-16 01:54Z) |
| us-east-2 use2-az2 | 211 | 99% | 8.9 | 9 (11-16 01:54Z) |
| us-east-2 use2-az3 | 238 | 97% | 8.8 | 9 (11-15 09:13Z) |
| us-west-2 usw2-az1 | 103 | 98% | 8.9 | 9 (11-15 21:41Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 142 | 88% | 8.2 | 9 (11-15 21:41Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703600 | 2026-11-16T01:54:39Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-16T01:54:39Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.717900 | 2026-11-16T01:54:39Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.606700 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.619900 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.606000 | 2026-11-16T01:54:39Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-16T01:54:39Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.681000 | 2026-11-16T01:54:39Z |
| ap-south-1 | ap-south-1a | Windows | 0.400600 | 2026-11-16T01:54:39Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.644300 | 2026-11-16T01:54:39Z |
| ap-south-1 | ap-south-1b | Windows | 0.403100 | 2026-11-16T01:54:39Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.639500 | 2026-11-16T01:54:39Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.520700 | 2026-11-16T01:54:39Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.521800 | 2026-11-16T01:54:39Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.872200 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.825100 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.585300 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.594000 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.516300 | 2026-11-16T01:54:39Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548200 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.584300 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.550200 | 2026-11-16T01:54:39Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.678500 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2a | Windows | 0.335700 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.560100 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2b | Windows | 0.285600 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.626400 | 2026-11-16T01:54:39Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-16T01:54:39Z |
