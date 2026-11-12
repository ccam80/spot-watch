# Spot placement score log

Generated 2026-11-12 18:50 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 528 | 49% | 5.2 | 1 (11-12 18:50Z) |
| ap-northeast-1 | 528 | 16% | 2.7 | 2 (11-12 18:50Z) |
| ap-northeast-2 | 528 | 69% | 7.1 | 1 (11-12 18:50Z) |
| ap-south-1 | 528 | 3% | 1.7 | 1 (11-12 18:50Z) |
| ap-southeast-2 | 528 | 1% | 1.0 | 1 (11-12 18:50Z) |
| ap-southeast-3 | 528 | 24% | 3.1 | 1 (11-12 18:50Z) |
| us-east-1 | 528 | 10% | 2.6 | 3 (11-12 18:50Z) |
| us-east-2 | 528 | 30% | 3.6 | 1 (11-12 18:50Z) |
| us-west-2 | 528 | 9% | 2.1 | 1 (11-12 18:50Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199999999919191111299111919999199981991912191111
ap-northeast-1   147888195119119111221121111919991991121111151112
ap-northeast-2   999999999999999299999999999999999999999999191111
ap-south-1       111111169811111121112222212221131191111221111111
ap-southeast-2   111111111111111111711111111111111111111111111111
ap-southeast-3   183973138618111111111131111111111311111111131111
us-east-1        111111299991211233333223221322222232929332242323
us-east-2        991196999999119121119111111199991999911111111111
us-west-2        111111171112112221119111112292211121111121222111
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
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 166 | 5% | 1.5 | 1 (11-12 18:50Z) |
| ap-east-1 ape1-az2 | 388 | 66% | 6.6 | 1 (11-12 18:50Z) |
| ap-northeast-1 apne1-az1 | 122 | 10% | 1.9 | 1 (11-12 02:52Z) |
| ap-northeast-1 apne1-az4 | 240 | 26% | 3.5 | 1 (11-12 18:50Z) |
| ap-northeast-2 apne2-az1 | 453 | 63% | 6.6 | 1 (11-12 18:50Z) |
| ap-northeast-2 apne2-az3 | 488 | 69% | 7.0 | 1 (11-12 10:55Z) |
| ap-northeast-2 apne2-az4 | 519 | 70% | 7.2 | 1 (11-12 18:50Z) |
| ap-south-1 aps1-az1 | 154 | 1% | 1.3 | 1 (11-12 02:52Z) |
| ap-south-1 aps1-az3 | 152 | 7% | 2.3 | 1 (11-12 18:50Z) |
| ap-southeast-2 apse2-az1 | 108 | 3% | 1.2 | 1 (11-12 02:52Z) |
| ap-southeast-2 apse2-az2 | 74 | 0% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 apse3-az1 | 92 | 0% | 1.0 | 1 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 322 | 38% | 4.3 | 1 (11-12 02:52Z) |
| us-east-1 use1-az1 | 109 | 0% | 1.1 | 1 (11-12 10:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 167 | 23% | 3.0 | 1 (11-12 10:55Z) |
| us-east-1 use1-az5 | 170 | 25% | 3.1 | 1 (11-12 18:50Z) |
| us-east-1 use1-az6 | 128 | 24% | 3.0 | 1 (11-12 10:55Z) |
| us-east-2 use2-az1 | 228 | 43% | 4.6 | 1 (11-12 10:55Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 299 | 47% | 5.1 | 1 (11-12 18:50Z) |
| us-west-2 usw2-az1 | 168 | 22% | 3.0 | 1 (11-12 18:50Z) |
| us-west-2 usw2-az2 | 124 | 17% | 2.5 | 1 (11-12 02:52Z) |
| us-west-2 usw2-az3 | 202 | 17% | 2.7 | 1 (11-12 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 528 | 71% | 7.3 | 9 (11-12 18:50Z) |
| ap-northeast-1 | 528 | 72% | 7.0 | 9 (11-12 18:50Z) |
| ap-northeast-2 | 528 | 100% | 9.0 | 9 (11-12 18:50Z) |
| ap-south-1 | 528 | 61% | 6.2 | 1 (11-12 18:50Z) |
| ap-southeast-2 | 528 | 26% | 3.6 | 9 (11-12 18:50Z) |
| ap-southeast-3 | 528 | 24% | 3.1 | 1 (11-12 18:50Z) |
| us-east-1 | 528 | 71% | 6.5 | 6 (11-12 18:50Z) |
| us-east-2 | 528 | 67% | 6.6 | 9 (11-12 18:50Z) |
| us-west-2 | 528 | 51% | 5.6 | 3 (11-12 18:50Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999929999921991992299999999999392299299289
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999911911291192299219921791199139229111111
ap-southeast-2   999999199111119111919911999999991991191191199199
ap-southeast-3   183973138618111111111131111111111311111111131111
us-east-1        999999999994523469765557957999999999959966996896
us-east-2        991999999999199199129111911999999999911991991999
us-west-2        999999999449244543429494419595599999949433493343
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
| ap-east-1 ape1-az1 | 339 | 84% | 8.0 | 9 (11-12 10:55Z) |
| ap-east-1 ape1-az2 | 305 | 87% | 8.2 | 9 (11-12 18:50Z) |
| ap-east-1 ape1-az3 | 337 | 87% | 8.2 | 9 (11-12 18:50Z) |
| ap-northeast-1 apne1-az1 | 213 | 95% | 8.7 | 9 (11-11 21:20Z) |
| ap-northeast-1 apne1-az2 | 195 | 86% | 8.2 | 9 (11-12 18:50Z) |
| ap-northeast-1 apne1-az4 | 275 | 99% | 8.9 | 9 (11-11 21:20Z) |
| ap-northeast-2 apne2-az1 | 428 | 100% | 9.0 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az2 | 115 | 86% | 8.1 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az3 | 445 | 100% | 9.0 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az4 | 347 | 86% | 8.2 | 9 (11-12 18:50Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 199 | 90% | 8.4 | 9 (11-10 23:11Z) |
| ap-southeast-2 apse2-az1 | 71 | 86% | 8.1 | 9 (11-12 10:55Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 151 | 91% | 8.4 | 9 (11-12 10:55Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 133 | 92% | 8.5 | 9 (11-10 09:39Z) |
| us-east-2 use2-az1 | 185 | 99% | 8.9 | 9 (11-12 18:50Z) |
| us-east-2 use2-az2 | 205 | 99% | 8.9 | 9 (11-12 10:55Z) |
| us-east-2 use2-az3 | 232 | 97% | 8.7 | 9 (11-12 18:50Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708600 | 2026-11-12T18:50:10Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-12T18:50:10Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.706700 | 2026-11-12T18:50:10Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.576200 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.595300 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.581000 | 2026-11-12T18:50:10Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-12T18:50:10Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.583100 | 2026-11-12T18:50:10Z |
| ap-south-1 | ap-south-1a | Windows | 0.397500 | 2026-11-12T18:50:10Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.562600 | 2026-11-12T18:50:10Z |
| ap-south-1 | ap-south-1b | Windows | 0.373500 | 2026-11-12T18:50:10Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.590800 | 2026-11-12T18:50:10Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492500 | 2026-11-12T18:50:10Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.606100 | 2026-11-12T18:50:10Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.512200 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.743100 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.708700 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.565000 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.515400 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.499000 | 2026-11-12T18:50:10Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550200 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552000 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549300 | 2026-11-12T18:50:10Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.585400 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2a | Windows | 0.325700 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.603500 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2b | Windows | 0.298700 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.602300 | 2026-11-12T18:50:10Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-12T18:50:10Z |
