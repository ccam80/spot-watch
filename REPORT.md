# Spot placement score log

Generated 2026-11-07 20:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 511 | 49% | 5.2 | 1 (11-07 20:49Z) |
| ap-northeast-1 | 511 | 16% | 2.7 | 9 (11-07 20:49Z) |
| ap-northeast-2 | 511 | 69% | 7.1 | 9 (11-07 20:49Z) |
| ap-south-1 | 511 | 3% | 1.7 | 1 (11-07 20:49Z) |
| ap-southeast-2 | 511 | 1% | 1.1 | 1 (11-07 20:49Z) |
| ap-southeast-3 | 511 | 25% | 3.2 | 1 (11-07 20:49Z) |
| us-east-1 | 511 | 10% | 2.6 | 2 (11-07 20:49Z) |
| us-east-2 | 511 | 30% | 3.6 | 9 (11-07 20:49Z) |
| us-west-2 | 511 | 9% | 2.1 | 2 (11-07 20:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911111999999999111999999999191911112991119199991
ap-northeast-1   144211111211879111478881951191191112211211119199
ap-northeast-2   999119999999999199999999999999992999999999999999
ap-south-1       111111111111111111111111698111111211122222122211
ap-southeast-2   111111111111111111111111111111111117111111111111
ap-southeast-3   111111111551254111839731386181111111111311111111
us-east-1        222222222221221111111112999912112333332232213222
us-east-2        111111199111211199911969999991191211191111111999
us-west-2        111111111194131111111111711121122211191111122922
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
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
| ap-northeast-1 apne1-az1 | 115 | 9% | 1.8 | 2 (11-07 20:49Z) |
| ap-northeast-1 apne1-az4 | 228 | 26% | 3.5 | 9 (11-07 20:49Z) |
| ap-northeast-2 apne2-az1 | 438 | 63% | 6.6 | 9 (11-07 20:49Z) |
| ap-northeast-2 apne2-az3 | 476 | 69% | 7.0 | 9 (11-07 20:49Z) |
| ap-northeast-2 apne2-az4 | 504 | 69% | 7.1 | 9 (11-07 20:49Z) |
| ap-south-1 aps1-az1 | 149 | 1% | 1.3 | 1 (11-07 20:49Z) |
| ap-south-1 aps1-az3 | 140 | 6% | 2.4 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az1 | 102 | 3% | 1.3 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az2 | 70 | 0% | 1.0 | 1 (11-07 09:56Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 316 | 38% | 4.4 | 1 (11-07 02:43Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 162 | 25% | 3.2 | 1 (11-06 23:00Z) |
| us-east-1 use1-az6 | 124 | 24% | 3.0 | 1 (11-07 20:49Z) |
| us-east-2 use2-az1 | 220 | 42% | 4.6 | 8 (11-07 20:49Z) |
| us-east-2 use2-az2 | 261 | 51% | 5.3 | 9 (11-07 20:49Z) |
| us-east-2 use2-az3 | 288 | 47% | 5.1 | 9 (11-07 20:49Z) |
| us-west-2 usw2-az1 | 160 | 23% | 3.1 | 1 (11-07 16:21Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 511 | 70% | 7.2 | 9 (11-07 20:49Z) |
| ap-northeast-1 | 511 | 72% | 7.0 | 9 (11-07 20:49Z) |
| ap-northeast-2 | 511 | 100% | 9.0 | 9 (11-07 20:49Z) |
| ap-south-1 | 511 | 62% | 6.3 | 7 (11-07 20:49Z) |
| ap-southeast-2 | 511 | 25% | 3.5 | 9 (11-07 20:49Z) |
| ap-southeast-3 | 511 | 25% | 3.2 | 1 (11-07 20:49Z) |
| us-east-1 | 511 | 70% | 6.4 | 9 (11-07 20:49Z) |
| us-east-2 | 511 | 67% | 6.6 | 9 (11-07 20:49Z) |
| us-west-2 | 511 | 51% | 5.6 | 5 (11-07 20:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999299999219919922999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999997999999999999999999999119112911922992199217
ap-southeast-2   999991113199999999999991991111191119199119999999
ap-southeast-3   111111111551254111839731386181111111111311111111
us-east-1        943999999999993229999999999945234697655579579999
us-east-2        289999999999999299919999999991991991291119119999
us-west-2        112332449995499929999999994492445434294944195955
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
| ap-east-1 ape1-az2 | 292 | 86% | 8.2 | 9 (11-07 20:49Z) |
| ap-east-1 ape1-az3 | 321 | 86% | 8.2 | 9 (11-07 20:49Z) |
| ap-northeast-1 apne1-az1 | 209 | 95% | 8.7 | 9 (11-05 21:55Z) |
| ap-northeast-1 apne1-az2 | 187 | 86% | 8.1 | 9 (11-07 02:43Z) |
| ap-northeast-1 apne1-az4 | 268 | 99% | 8.9 | 9 (11-06 17:54Z) |
| ap-northeast-2 apne2-az1 | 416 | 100% | 9.0 | 9 (11-07 16:21Z) |
| ap-northeast-2 apne2-az2 | 111 | 86% | 8.1 | 9 (11-07 20:49Z) |
| ap-northeast-2 apne2-az3 | 434 | 100% | 9.0 | 9 (11-07 02:43Z) |
| ap-northeast-2 apne2-az4 | 334 | 86% | 8.2 | 9 (11-07 20:49Z) |
| ap-south-1 aps1-az1 | 176 | 88% | 8.2 | 9 (11-06 23:00Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 197 | 90% | 8.4 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az1 | 66 | 85% | 8.0 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 78 | 83% | 8.0 | 9 (11-07 20:49Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 109 | 100% | 9.0 | 9 (11-07 20:49Z) |
| us-east-1 use1-az4 | 144 | 92% | 8.4 | 9 (11-07 20:49Z) |
| us-east-1 use1-az5 | 106 | 98% | 8.9 | 9 (11-07 02:43Z) |
| us-east-1 use1-az6 | 128 | 92% | 8.4 | 9 (11-07 20:49Z) |
| us-east-2 use2-az1 | 179 | 99% | 8.9 | 9 (11-07 16:21Z) |
| us-east-2 use2-az2 | 197 | 99% | 8.9 | 9 (11-07 20:49Z) |
| us-east-2 use2-az3 | 227 | 96% | 8.7 | 9 (11-07 20:49Z) |
| us-west-2 usw2-az1 | 93 | 98% | 8.8 | 9 (11-07 09:56Z) |
| us-west-2 usw2-az2 | 90 | 90% | 8.3 | 9 (11-07 09:56Z) |
| us-west-2 usw2-az3 | 131 | 88% | 8.1 | 9 (11-07 09:56Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718400 | 2026-11-07T20:49:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-07T20:49:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731000 | 2026-11-07T20:49:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580400 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.592200 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574100 | 2026-11-07T20:49:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-07T20:49:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.573300 | 2026-11-07T20:49:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.426600 | 2026-11-07T20:49:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.545000 | 2026-11-07T20:49:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.348400 | 2026-11-07T20:49:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.583100 | 2026-11-07T20:49:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.490400 | 2026-11-07T20:49:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.681200 | 2026-11-07T20:49:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.527900 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.575300 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.550300 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.490800 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.416700 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.486600 | 2026-11-07T20:49:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548900 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548500 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546700 | 2026-11-07T20:49:45Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.550200 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2a | Windows | 0.300900 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.669600 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2b | Windows | 0.315200 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.587400 | 2026-11-07T20:49:45Z |
| us-west-2 | us-west-2c | Windows | 0.300400 | 2026-11-07T20:49:45Z |
