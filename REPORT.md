# Spot placement score log

Generated 2026-11-16 20:20 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 543 | 48% | 5.2 | 9 (11-16 20:20Z) |
| ap-northeast-1 | 543 | 17% | 2.8 | 9 (11-16 20:20Z) |
| ap-northeast-2 | 543 | 69% | 7.1 | 9 (11-16 20:20Z) |
| ap-south-1 | 543 | 3% | 1.7 | 1 (11-16 20:20Z) |
| ap-southeast-2 | 543 | 1% | 1.0 | 1 (11-16 20:20Z) |
| ap-southeast-3 | 543 | 24% | 3.1 | 3 (11-16 20:20Z) |
| us-east-1 | 543 | 10% | 2.7 | 6 (11-16 20:20Z) |
| us-east-2 | 543 | 31% | 3.7 | 9 (11-16 20:20Z) |
| us-west-2 | 543 | 9% | 2.1 | 2 (11-16 20:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111299111919999199981991912191111111119919961139
ap-northeast-1   111221121111919991991121111151112112999599999119
ap-northeast-2   299999999999999999999999999191111111119999999979
ap-south-1       121112222212221131191111221111111111111119111111
ap-southeast-2   111711111111111111111111111111111111111111111111
ap-southeast-3   111111131111111111311111111131111111111121131113
us-east-1        233333223221322222232929332242323334422332373746
us-east-2        121119111111199991999911111111111111111991991999
us-west-2        221119111112292211121111121222111212211121911112
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
| ap-east-1 ape1-az2 | 397 | 66% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az1 | 131 | 11% | 2.0 | 5 (11-16 20:20Z) |
| ap-northeast-1 apne1-az4 | 252 | 28% | 3.6 | 3 (11-16 20:20Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 501 | 69% | 7.0 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az4 | 530 | 70% | 7.2 | 9 (11-16 20:20Z) |
| ap-south-1 aps1-az1 | 158 | 1% | 1.3 | 1 (11-16 09:29Z) |
| ap-south-1 aps1-az3 | 156 | 7% | 2.3 | 1 (11-16 01:54Z) |
| ap-southeast-2 apse2-az1 | 111 | 3% | 1.2 | 1 (11-15 21:41Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 94 | 0% | 1.0 | 1 (11-16 20:20Z) |
| ap-southeast-3 apse3-az3 | 330 | 37% | 4.2 | 3 (11-16 20:20Z) |
| us-east-1 use1-az1 | 116 | 0% | 1.1 | 1 (11-16 01:54Z) |
| us-east-1 use1-az2 | 143 | 3% | 1.4 | 1 (11-16 20:20Z) |
| us-east-1 use1-az4 | 174 | 22% | 2.9 | 1 (11-16 09:29Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 133 | 23% | 3.0 | 1 (11-16 09:29Z) |
| us-east-2 use2-az1 | 238 | 43% | 4.6 | 9 (11-16 09:29Z) |
| us-east-2 use2-az2 | 277 | 51% | 5.3 | 3 (11-16 20:20Z) |
| us-east-2 use2-az3 | 305 | 48% | 5.1 | 9 (11-16 09:29Z) |
| us-west-2 usw2-az1 | 170 | 22% | 3.0 | 1 (11-15 16:59Z) |
| us-west-2 usw2-az2 | 126 | 17% | 2.5 | 1 (11-15 21:41Z) |
| us-west-2 usw2-az3 | 206 | 17% | 2.7 | 1 (11-16 09:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 543 | 72% | 7.3 | 9 (11-16 20:20Z) |
| ap-northeast-1 | 543 | 72% | 7.0 | 9 (11-16 20:20Z) |
| ap-northeast-2 | 543 | 100% | 9.0 | 9 (11-16 20:20Z) |
| ap-south-1 | 543 | 59% | 6.1 | 1 (11-16 20:20Z) |
| ap-southeast-2 | 543 | 27% | 3.6 | 8 (11-16 20:20Z) |
| ap-southeast-3 | 543 | 24% | 3.1 | 3 (11-16 20:20Z) |
| us-east-1 | 543 | 72% | 6.5 | 9 (11-16 20:20Z) |
| us-east-2 | 543 | 68% | 6.7 | 9 (11-16 20:20Z) |
| us-west-2 | 543 | 51% | 5.6 | 5 (11-16 20:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   921991992299999999999392299299289429999999999229
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       291192299219921791199139229111111911111199111111
ap-southeast-2   111919911999999991991191191199199119132999991118
ap-southeast-3   111111131111111111311111111131111111111121131113
us-east-1        469765557957999999999959966996896697899999799999
us-east-2        199129111911999999999911991991999999999999991999
us-west-2        543429494419595599999949433493343419423993999115
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
| ap-east-1 ape1-az1 | 348 | 84% | 8.1 | 9 (11-16 20:20Z) |
| ap-east-1 ape1-az2 | 317 | 87% | 8.2 | 9 (11-16 20:20Z) |
| ap-east-1 ape1-az3 | 347 | 87% | 8.2 | 9 (11-16 09:29Z) |
| ap-northeast-1 apne1-az1 | 218 | 95% | 8.7 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az2 | 203 | 87% | 8.2 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az4 | 280 | 99% | 8.9 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az1 | 440 | 100% | 9.0 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az2 | 120 | 87% | 8.1 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 455 | 100% | 9.0 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az4 | 355 | 87% | 8.2 | 9 (11-16 20:20Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 87 | 84% | 8.0 | 9 (11-15 16:59Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 157 | 92% | 8.4 | 9 (11-16 09:29Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 138 | 93% | 8.5 | 9 (11-16 01:54Z) |
| us-east-2 use2-az1 | 193 | 99% | 8.9 | 9 (11-16 01:54Z) |
| us-east-2 use2-az2 | 213 | 99% | 8.9 | 9 (11-16 20:20Z) |
| us-east-2 use2-az3 | 239 | 97% | 8.8 | 9 (11-16 09:29Z) |
| us-west-2 usw2-az1 | 103 | 98% | 8.9 | 9 (11-15 21:41Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 142 | 88% | 8.2 | 9 (11-15 21:41Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.701500 | 2026-11-16T20:20:12Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-16T20:20:12Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.718600 | 2026-11-16T20:20:12Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.609100 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.621500 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.607700 | 2026-11-16T20:20:12Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-16T20:20:12Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.676400 | 2026-11-16T20:20:12Z |
| ap-south-1 | ap-south-1a | Windows | 0.400100 | 2026-11-16T20:20:12Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.643500 | 2026-11-16T20:20:12Z |
| ap-south-1 | ap-south-1b | Windows | 0.401800 | 2026-11-16T20:20:12Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.649000 | 2026-11-16T20:20:12Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523600 | 2026-11-16T20:20:12Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.499900 | 2026-11-16T20:20:12Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.872100 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.859500 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.607000 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.615300 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.524600 | 2026-11-16T20:20:12Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.538800 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.572700 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.540200 | 2026-11-16T20:20:12Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.694600 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2a | Windows | 0.331700 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.597200 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.626200 | 2026-11-16T20:20:12Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-16T20:20:12Z |
