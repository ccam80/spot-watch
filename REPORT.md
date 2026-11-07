# Spot placement score log

Generated 2026-11-07 16:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 510 | 49% | 5.2 | 9 (11-07 16:21Z) |
| ap-northeast-1 | 510 | 16% | 2.7 | 9 (11-07 16:21Z) |
| ap-northeast-2 | 510 | 69% | 7.1 | 9 (11-07 16:21Z) |
| ap-south-1 | 510 | 3% | 1.7 | 1 (11-07 16:21Z) |
| ap-southeast-2 | 510 | 1% | 1.1 | 1 (11-07 16:21Z) |
| ap-southeast-3 | 510 | 25% | 3.2 | 1 (11-07 16:21Z) |
| us-east-1 | 510 | 10% | 2.6 | 2 (11-07 16:21Z) |
| us-east-2 | 510 | 30% | 3.6 | 9 (11-07 16:21Z) |
| us-west-2 | 510 | 9% | 2.1 | 2 (11-07 16:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        991111199999999911199999999919191111299111919999
ap-northeast-1   114421111121187911147888195119119111221121111919
ap-northeast-2   999911999999999919999999999999999299999999999999
ap-south-1       111111111111111111111111169811111121112222212221
ap-southeast-2   111111111111111111111111111111111111711111111111
ap-southeast-3   111111111155125411183973138618111111111131111111
us-east-1        222222222222122111111111299991211233333223221322
us-east-2        111111119911121119991196999999119121119111111199
us-west-2        111111111119413111111111171112112221119111112292
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 162 | 6% | 1.5 | 1 (11-07 09:56Z) |
| ap-east-1 ape1-az2 | 375 | 66% | 6.7 | 9 (11-07 16:21Z) |
| ap-northeast-1 apne1-az1 | 114 | 9% | 1.8 | 9 (11-07 16:21Z) |
| ap-northeast-1 apne1-az4 | 227 | 26% | 3.5 | 9 (11-07 16:21Z) |
| ap-northeast-2 apne2-az1 | 437 | 63% | 6.6 | 9 (11-07 16:21Z) |
| ap-northeast-2 apne2-az3 | 475 | 69% | 7.0 | 9 (11-07 16:21Z) |
| ap-northeast-2 apne2-az4 | 503 | 69% | 7.1 | 9 (11-07 16:21Z) |
| ap-south-1 aps1-az1 | 148 | 1% | 1.3 | 1 (11-07 02:43Z) |
| ap-south-1 aps1-az3 | 140 | 6% | 2.4 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az1 | 102 | 3% | 1.3 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az2 | 70 | 0% | 1.0 | 1 (11-07 09:56Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 316 | 38% | 4.4 | 1 (11-07 02:43Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 162 | 25% | 3.2 | 1 (11-06 23:00Z) |
| us-east-1 use1-az6 | 123 | 24% | 3.1 | 1 (11-07 02:43Z) |
| us-east-2 use2-az1 | 219 | 42% | 4.6 | 9 (11-07 16:21Z) |
| us-east-2 use2-az2 | 260 | 50% | 5.3 | 9 (11-07 16:21Z) |
| us-east-2 use2-az3 | 287 | 47% | 5.1 | 9 (11-07 16:21Z) |
| us-west-2 usw2-az1 | 160 | 23% | 3.1 | 1 (11-07 16:21Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 510 | 70% | 7.2 | 9 (11-07 16:21Z) |
| ap-northeast-1 | 510 | 72% | 7.0 | 9 (11-07 16:21Z) |
| ap-northeast-2 | 510 | 100% | 9.0 | 9 (11-07 16:21Z) |
| ap-south-1 | 510 | 62% | 6.3 | 1 (11-07 16:21Z) |
| ap-southeast-2 | 510 | 25% | 3.5 | 9 (11-07 16:21Z) |
| ap-southeast-3 | 510 | 25% | 3.2 | 1 (11-07 16:21Z) |
| us-east-1 | 510 | 70% | 6.4 | 9 (11-07 16:21Z) |
| us-east-2 | 510 | 67% | 6.6 | 9 (11-07 16:21Z) |
| us-west-2 | 510 | 51% | 5.6 | 5 (11-07 16:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999929999921991992299999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999799999999999999999999911911291192299219921
ap-southeast-2   999999111319999999999999199111119111919911999999
ap-southeast-3   111111111155125411183973138618111111111131111111
us-east-1        394399999999999322999999999994523469765557957999
us-east-2        228999999999999929991999999999199199129111911999
us-west-2        211233244999549992999999999449244543429494419595
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 327 | 83% | 8.0 | 9 (11-06 10:43Z) |
| ap-east-1 ape1-az2 | 291 | 86% | 8.2 | 9 (11-07 16:21Z) |
| ap-east-1 ape1-az3 | 320 | 86% | 8.2 | 9 (11-07 16:21Z) |
| ap-northeast-1 apne1-az1 | 209 | 95% | 8.7 | 9 (11-05 21:55Z) |
| ap-northeast-1 apne1-az2 | 187 | 86% | 8.1 | 9 (11-07 02:43Z) |
| ap-northeast-1 apne1-az4 | 268 | 99% | 8.9 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az1 | 416 | 100% | 9.0 | 9 (11-07 16:21Z) |
| ap-northeast-2 apne2-az2 | 110 | 85% | 8.1 | 9 (11-07 09:56Z) |
| ap-northeast-2 apne2-az3 | 434 | 100% | 9.0 | 9 (11-07 02:43Z) |
| ap-northeast-2 apne2-az4 | 333 | 86% | 8.2 | 9 (11-07 16:21Z) |
| ap-south-1 aps1-az1 | 176 | 88% | 8.2 | 9 (11-06 23:00Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 197 | 90% | 8.4 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az1 | 66 | 85% | 8.0 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 77 | 83% | 8.0 | 9 (11-07 16:21Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 108 | 100% | 9.0 | 9 (11-07 16:21Z) |
| us-east-1 use1-az4 | 143 | 92% | 8.4 | 9 (11-07 16:21Z) |
| us-east-1 use1-az5 | 106 | 98% | 8.9 | 9 (11-07 02:43Z) |
| us-east-1 use1-az6 | 127 | 92% | 8.4 | 9 (11-07 02:43Z) |
| us-east-2 use2-az1 | 179 | 99% | 8.9 | 9 (11-07 16:21Z) |
| us-east-2 use2-az2 | 196 | 99% | 8.9 | 9 (11-07 16:21Z) |
| us-east-2 use2-az3 | 226 | 96% | 8.7 | 9 (11-07 16:21Z) |
| us-west-2 usw2-az1 | 93 | 98% | 8.8 | 9 (11-07 09:56Z) |
| us-west-2 usw2-az2 | 90 | 90% | 8.3 | 9 (11-07 09:56Z) |
| us-west-2 usw2-az3 | 131 | 88% | 8.1 | 9 (11-07 09:56Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718400 | 2026-11-07T16:21:01Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-07T16:21:01Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731200 | 2026-11-07T16:21:01Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580200 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.592400 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574200 | 2026-11-07T16:21:01Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-07T16:21:01Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.576100 | 2026-11-07T16:21:01Z |
| ap-south-1 | ap-south-1a | Windows | 0.429100 | 2026-11-07T16:21:01Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.545000 | 2026-11-07T16:21:01Z |
| ap-south-1 | ap-south-1b | Windows | 0.348400 | 2026-11-07T16:21:01Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.583100 | 2026-11-07T16:21:01Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.489000 | 2026-11-07T16:21:01Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.685300 | 2026-11-07T16:21:01Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.527900 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.575300 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.539300 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.490600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.416700 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.486600 | 2026-11-07T16:21:01Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548900 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548500 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546400 | 2026-11-07T16:21:01Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.551700 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2a | Windows | 0.301300 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.676600 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2b | Windows | 0.315700 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.587400 | 2026-11-07T16:21:01Z |
| us-west-2 | us-west-2c | Windows | 0.301000 | 2026-11-07T16:21:01Z |
