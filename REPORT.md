# Spot placement score log

Generated 2026-11-04 01:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 497 | 49% | 5.2 | 1 (11-04 01:16Z) |
| ap-northeast-1 | 497 | 16% | 2.7 | 1 (11-04 01:16Z) |
| ap-northeast-2 | 497 | 68% | 7.0 | 9 (11-04 01:16Z) |
| ap-south-1 | 497 | 3% | 1.7 | 2 (11-04 01:16Z) |
| ap-southeast-2 | 497 | 0% | 1.0 | 1 (11-04 01:16Z) |
| ap-southeast-3 | 497 | 26% | 3.3 | 1 (11-04 01:16Z) |
| us-east-1 | 497 | 10% | 2.6 | 3 (11-04 01:16Z) |
| us-east-2 | 497 | 30% | 3.6 | 2 (11-04 01:16Z) |
| us-west-2 | 497 | 9% | 2.1 | 2 (11-04 01:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999111111999111119999999991119999999991919111
ap-northeast-1   222871111242111442111112118791114788819511911911
ap-northeast-2   999999999999999991199999999991999999999999999929
ap-south-1       221111211111111111111111111111111111116981111112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   178675111111111111111115512541118397313861811111
us-east-1        222222222111222222222222212211111111129999121123
us-east-2        111111111111111111111991112111999119699999911912
us-west-2        111111111111111111111111941311111111117111211222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
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
| ap-east-1 ape1-az2 | 367 | 66% | 6.6 | 1 (11-04 01:16Z) |
| ap-northeast-1 apne1-az1 | 109 | 8% | 1.7 | 1 (11-04 01:16Z) |
| ap-northeast-1 apne1-az4 | 223 | 26% | 3.5 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az1 | 426 | 62% | 6.5 | 9 (11-04 01:16Z) |
| ap-northeast-2 apne2-az3 | 463 | 68% | 7.0 | 1 (11-03 20:55Z) |
| ap-northeast-2 apne2-az4 | 490 | 69% | 7.1 | 5 (11-04 01:16Z) |
| ap-south-1 aps1-az1 | 140 | 1% | 1.3 | 1 (11-03 20:55Z) |
| ap-south-1 aps1-az3 | 137 | 7% | 2.4 | 2 (11-04 01:16Z) |
| ap-southeast-2 apse2-az1 | 96 | 2% | 1.2 | 1 (11-04 01:16Z) |
| ap-southeast-2 apse2-az2 | 65 | 0% | 1.0 | 1 (11-04 01:16Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 311 | 39% | 4.4 | 1 (11-04 01:16Z) |
| us-east-1 use1-az1 | 103 | 0% | 1.1 | 1 (11-04 01:16Z) |
| us-east-1 use1-az2 | 135 | 3% | 1.4 | 1 (11-03 20:55Z) |
| us-east-1 use1-az4 | 162 | 23% | 3.0 | 1 (11-03 20:55Z) |
| us-east-1 use1-az5 | 159 | 26% | 3.2 | 1 (11-03 06:36Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 212 | 43% | 4.6 | 1 (11-03 20:55Z) |
| us-east-2 use2-az2 | 255 | 50% | 5.3 | 1 (11-03 20:55Z) |
| us-east-2 use2-az3 | 281 | 47% | 5.1 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 156 | 24% | 3.2 | 1 (11-03 20:55Z) |
| us-west-2 usw2-az2 | 120 | 18% | 2.6 | 1 (11-04 01:16Z) |
| us-west-2 usw2-az3 | 194 | 16% | 2.7 | 1 (11-03 20:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 497 | 69% | 7.2 | 9 (11-04 01:16Z) |
| ap-northeast-1 | 497 | 72% | 7.0 | 2 (11-04 01:16Z) |
| ap-northeast-2 | 497 | 100% | 9.0 | 9 (11-04 01:16Z) |
| ap-south-1 | 497 | 62% | 6.3 | 9 (11-04 01:16Z) |
| ap-southeast-2 | 497 | 24% | 3.4 | 1 (11-04 01:16Z) |
| ap-southeast-3 | 497 | 26% | 3.3 | 1 (11-04 01:16Z) |
| us-east-1 | 497 | 70% | 6.4 | 6 (11-04 01:16Z) |
| us-east-2 | 497 | 67% | 6.7 | 9 (11-04 01:16Z) |
| us-west-2 | 497 | 52% | 5.6 | 4 (11-04 01:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999999999999999992999992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       221111299999999999979999999999999999999991191129
ap-southeast-2   111111111111999999911131999999999999919911111911
ap-southeast-3   178675111111111111111115512541118397313861811111
us-east-1        993232333433939439999999999932299999999999452346
us-east-2        322222222222222899999999999992999199999999919919
us-west-2        999484439593121123324499954999299999999944924454
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
| ap-east-1 ape1-az1 | 320 | 83% | 8.0 | 9 (11-04 01:16Z) |
| ap-east-1 ape1-az2 | 278 | 85% | 8.1 | 9 (11-04 01:16Z) |
| ap-east-1 ape1-az3 | 307 | 86% | 8.1 | 9 (11-04 01:16Z) |
| ap-northeast-1 apne1-az1 | 206 | 95% | 8.7 | 9 (11-03 20:55Z) |
| ap-northeast-1 apne1-az2 | 180 | 85% | 8.1 | 9 (11-03 20:55Z) |
| ap-northeast-1 apne1-az4 | 264 | 99% | 8.9 | 9 (11-03 20:55Z) |
| ap-northeast-2 apne2-az1 | 407 | 100% | 9.0 | 9 (11-04 01:16Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 425 | 100% | 9.0 | 9 (11-04 01:16Z) |
| ap-northeast-2 apne2-az4 | 322 | 85% | 8.1 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az1 | 173 | 87% | 8.2 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az2 | 184 | 80% | 7.7 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az3 | 193 | 90% | 8.4 | 9 (11-04 01:16Z) |
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
| us-west-2 usw2-az3 | 128 | 88% | 8.2 | 2 (11-04 01:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722400 | 2026-11-04T01:16:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-04T01:16:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.735600 | 2026-11-04T01:16:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579500 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590700 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-11-04T01:16:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-04T01:16:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.621400 | 2026-11-04T01:16:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.441700 | 2026-11-04T01:16:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.520100 | 2026-11-04T01:16:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.368300 | 2026-11-04T01:16:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.591500 | 2026-11-04T01:16:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508700 | 2026-11-04T01:16:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.723700 | 2026-11-04T01:16:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.552300 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.502200 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.541800 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.485500 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.482300 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.556900 | 2026-11-04T01:16:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549300 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2a | Windows | 0.638100 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549700 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546400 | 2026-11-04T01:16:00Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.586800 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2a | Windows | 0.308000 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.641300 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2b | Windows | 0.321300 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.597500 | 2026-11-04T01:16:00Z |
| us-west-2 | us-west-2c | Windows | 0.307400 | 2026-11-04T01:16:00Z |
