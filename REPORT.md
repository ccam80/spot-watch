# Spot placement score log

Generated 2026-11-03 20:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 496 | 49% | 5.2 | 1 (11-03 20:55Z) |
| ap-northeast-1 | 496 | 16% | 2.7 | 1 (11-03 20:55Z) |
| ap-northeast-2 | 496 | 68% | 7.0 | 2 (11-03 20:55Z) |
| ap-south-1 | 496 | 3% | 1.7 | 1 (11-03 20:55Z) |
| ap-southeast-2 | 496 | 0% | 1.0 | 1 (11-03 20:55Z) |
| ap-southeast-3 | 496 | 26% | 3.3 | 1 (11-03 20:55Z) |
| us-east-1 | 496 | 10% | 2.6 | 2 (11-03 20:55Z) |
| us-east-2 | 496 | 30% | 3.7 | 1 (11-03 20:55Z) |
| us-west-2 | 496 | 9% | 2.1 | 2 (11-03 20:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999911111199911111999999999111999999999191911
ap-northeast-1   222287111124211144211111211879111478881951191191
ap-northeast-2   999999999999999999119999999999199999999999999992
ap-south-1       122111121111111111111111111111111111111698111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   117867511111111111111111551254111839731386181111
us-east-1        322222222211122222222222221221111111112999912112
us-east-2        111111111111111111111199111211199911969999991191
us-west-2        111111111111111111111111194131111111111711121122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 157 | 6% | 1.6 | 1 (11-03 15:00Z) |
| ap-east-1 ape1-az2 | 366 | 66% | 6.6 | 9 (11-03 06:36Z) |
| ap-northeast-1 apne1-az1 | 108 | 8% | 1.7 | 1 (11-02 23:26Z) |
| ap-northeast-1 apne1-az4 | 223 | 26% | 3.5 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az1 | 425 | 62% | 6.5 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az3 | 463 | 68% | 7.0 | 1 (11-03 20:55Z) |
| ap-northeast-2 apne2-az4 | 489 | 69% | 7.1 | 2 (11-03 20:55Z) |
| ap-south-1 aps1-az1 | 140 | 1% | 1.3 | 1 (11-03 20:55Z) |
| ap-south-1 aps1-az3 | 136 | 7% | 2.4 | 1 (11-03 15:00Z) |
| ap-southeast-2 apse2-az1 | 95 | 2% | 1.2 | 1 (11-03 06:36Z) |
| ap-southeast-2 apse2-az2 | 64 | 0% | 1.0 | 1 (11-03 15:00Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 310 | 39% | 4.4 | 1 (11-02 23:26Z) |
| us-east-1 use1-az1 | 102 | 0% | 1.1 | 1 (11-02 23:26Z) |
| us-east-1 use1-az2 | 135 | 3% | 1.4 | 1 (11-03 20:55Z) |
| us-east-1 use1-az4 | 162 | 23% | 3.0 | 1 (11-03 20:55Z) |
| us-east-1 use1-az5 | 159 | 26% | 3.2 | 1 (11-03 06:36Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 212 | 43% | 4.6 | 1 (11-03 20:55Z) |
| us-east-2 use2-az2 | 255 | 50% | 5.3 | 1 (11-03 20:55Z) |
| us-east-2 use2-az3 | 281 | 47% | 5.1 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 156 | 24% | 3.2 | 1 (11-03 20:55Z) |
| us-west-2 usw2-az2 | 119 | 18% | 2.6 | 1 (11-02 23:26Z) |
| us-west-2 usw2-az3 | 194 | 16% | 2.7 | 1 (11-03 20:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 496 | 69% | 7.1 | 9 (11-03 20:55Z) |
| ap-northeast-1 | 496 | 73% | 7.0 | 9 (11-03 20:55Z) |
| ap-northeast-2 | 496 | 100% | 9.0 | 9 (11-03 20:55Z) |
| ap-south-1 | 496 | 62% | 6.3 | 2 (11-03 20:55Z) |
| ap-southeast-2 | 496 | 24% | 3.4 | 1 (11-03 20:55Z) |
| ap-southeast-3 | 496 | 26% | 3.3 | 1 (11-03 20:55Z) |
| us-east-1 | 496 | 70% | 6.4 | 4 (11-03 20:55Z) |
| us-east-2 | 496 | 67% | 6.7 | 1 (11-03 20:55Z) |
| us-west-2 | 496 | 52% | 5.6 | 5 (11-03 20:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399999999999999999999999999999999999999999299999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       122111129999999999997999999999999999999999119112
ap-southeast-2   111111111111199999991113199999999999991991111191
ap-southeast-3   117867511111111111111111551254111839731386181111
us-east-1        999323233343393943999999999993229999999999945234
us-east-2        932222222222222289999999999999299919999999991991
us-west-2        999948443959312112332449995499929999999994492445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 319 | 83% | 8.0 | 9 (11-03 20:55Z) |
| ap-east-1 ape1-az2 | 277 | 85% | 8.1 | 9 (11-03 20:55Z) |
| ap-east-1 ape1-az3 | 306 | 86% | 8.1 | 9 (11-03 20:55Z) |
| ap-northeast-1 apne1-az1 | 206 | 95% | 8.7 | 9 (11-03 20:55Z) |
| ap-northeast-1 apne1-az2 | 180 | 85% | 8.1 | 9 (11-03 20:55Z) |
| ap-northeast-1 apne1-az4 | 264 | 99% | 8.9 | 9 (11-03 20:55Z) |
| ap-northeast-2 apne2-az1 | 406 | 100% | 9.0 | 9 (11-03 20:55Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 424 | 100% | 9.0 | 9 (11-03 20:55Z) |
| ap-northeast-2 apne2-az4 | 321 | 85% | 8.1 | 9 (11-03 20:55Z) |
| ap-south-1 aps1-az1 | 172 | 87% | 8.2 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az2 | 183 | 80% | 7.7 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az3 | 192 | 90% | 8.4 | 9 (11-02 23:26Z) |
| ap-southeast-2 apse2-az1 | 60 | 83% | 8.0 | 9 (11-03 15:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 103 | 98% | 8.9 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 124 | 92% | 8.4 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 175 | 99% | 8.9 | 9 (11-03 06:36Z) |
| us-east-2 use2-az2 | 193 | 99% | 8.9 | 9 (11-03 06:36Z) |
| us-east-2 use2-az3 | 221 | 96% | 8.7 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 127 | 89% | 8.2 | 2 (11-03 20:55Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722800 | 2026-11-03T20:55:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-03T20:55:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732400 | 2026-11-03T20:55:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579700 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590700 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-11-03T20:55:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-03T20:55:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.621400 | 2026-11-03T20:55:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.446300 | 2026-11-03T20:55:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.517200 | 2026-11-03T20:55:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.370900 | 2026-11-03T20:55:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.601100 | 2026-11-03T20:55:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508700 | 2026-11-03T20:55:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.723700 | 2026-11-03T20:55:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.552300 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.503100 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.541800 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.483900 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.490800 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.564800 | 2026-11-03T20:55:44Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549900 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550200 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547100 | 2026-11-03T20:55:44Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.588400 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2a | Windows | 0.308800 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.637500 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2b | Windows | 0.321700 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.593000 | 2026-11-03T20:55:44Z |
| us-west-2 | us-west-2c | Windows | 0.308200 | 2026-11-03T20:55:44Z |
