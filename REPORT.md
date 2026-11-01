# Spot placement score log

Generated 2026-11-01 14:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 488 | 49% | 5.2 | 9 (11-01 14:59Z) |
| ap-northeast-1 | 488 | 15% | 2.7 | 9 (11-01 14:59Z) |
| ap-northeast-2 | 488 | 67% | 7.0 | 9 (11-01 14:59Z) |
| ap-south-1 | 488 | 2% | 1.7 | 6 (11-01 14:59Z) |
| ap-southeast-2 | 488 | 0% | 1.0 | 1 (11-01 14:59Z) |
| ap-southeast-3 | 488 | 26% | 3.3 | 3 (11-01 14:59Z) |
| us-east-1 | 488 | 10% | 2.6 | 9 (11-01 14:59Z) |
| us-east-2 | 488 | 30% | 3.6 | 9 (11-01 14:59Z) |
| us-west-2 | 488 | 9% | 2.1 | 7 (11-01 14:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999111111999111119999999991119999999
ap-northeast-1   111111112222871111242111442111112118791114788819
ap-northeast-2   999999999999999999999999991199999999991999999999
ap-south-1       111111111221111211111111111111111111111111111116
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111178675111111111111111115512541118397313
us-east-1        333333233222222222111222222222222212211111111129
us-east-2        128991291111111111111111111111991112111999119699
us-west-2        221112211111111111111111111111111941311111111117
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 155 | 6% | 1.6 | 1 (10-31 18:15Z) |
| ap-east-1 ape1-az2 | 361 | 66% | 6.6 | 9 (11-01 14:59Z) |
| ap-northeast-1 apne1-az1 | 107 | 8% | 1.7 | 6 (11-01 00:41Z) |
| ap-northeast-1 apne1-az4 | 220 | 25% | 3.5 | 9 (11-01 14:59Z) |
| ap-northeast-2 apne2-az1 | 418 | 61% | 6.5 | 9 (11-01 14:59Z) |
| ap-northeast-2 apne2-az3 | 455 | 68% | 7.0 | 9 (11-01 14:59Z) |
| ap-northeast-2 apne2-az4 | 481 | 68% | 7.1 | 9 (11-01 14:59Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 132 | 5% | 2.3 | 1 (11-01 00:41Z) |
| ap-southeast-2 apse2-az1 | 93 | 2% | 1.2 | 1 (11-01 07:25Z) |
| ap-southeast-2 apse2-az2 | 61 | 0% | 1.0 | 1 (11-01 00:41Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 308 | 39% | 4.4 | 3 (11-01 00:41Z) |
| us-east-1 use1-az1 | 101 | 0% | 1.1 | 1 (11-01 07:25Z) |
| us-east-1 use1-az2 | 134 | 3% | 1.4 | 9 (11-01 14:59Z) |
| us-east-1 use1-az4 | 159 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-1 use1-az5 | 155 | 25% | 3.1 | 1 (10-31 20:13Z) |
| us-east-1 use1-az6 | 119 | 24% | 3.0 | 9 (11-01 14:59Z) |
| us-east-2 use2-az1 | 207 | 42% | 4.6 | 9 (11-01 14:59Z) |
| us-east-2 use2-az2 | 249 | 49% | 5.2 | 9 (11-01 14:59Z) |
| us-east-2 use2-az3 | 276 | 46% | 5.0 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az1 | 152 | 24% | 3.3 | 1 (11-01 00:41Z) |
| us-west-2 usw2-az2 | 118 | 18% | 2.6 | 1 (11-01 07:25Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 488 | 69% | 7.1 | 9 (11-01 14:59Z) |
| ap-northeast-1 | 488 | 72% | 7.0 | 9 (11-01 14:59Z) |
| ap-northeast-2 | 488 | 100% | 9.0 | 9 (11-01 14:59Z) |
| ap-south-1 | 488 | 62% | 6.3 | 9 (11-01 14:59Z) |
| ap-southeast-2 | 488 | 24% | 3.4 | 9 (11-01 14:59Z) |
| ap-southeast-3 | 488 | 26% | 3.3 | 3 (11-01 14:59Z) |
| us-east-1 | 488 | 70% | 6.4 | 9 (11-01 14:59Z) |
| us-east-2 | 488 | 67% | 6.6 | 9 (11-01 14:59Z) |
| us-west-2 | 488 | 52% | 5.7 | 9 (11-01 14:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111111133999999999999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911111111221111299999999999979999999999999999999
ap-southeast-2   111111111111111111111999999911131999999999999919
ap-southeast-3   111111111178675111111111111111115512541118397313
us-east-1        669999999993232333433939439999999999932299999999
us-east-2        499999999322222222222222899999999999992999199999
us-west-2        559335599999484439593121123324499954999299999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 312 | 83% | 8.0 | 9 (11-01 07:25Z) |
| ap-east-1 ape1-az2 | 273 | 85% | 8.1 | 9 (11-01 14:59Z) |
| ap-east-1 ape1-az3 | 299 | 85% | 8.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az1 | 205 | 95% | 8.7 | 9 (11-01 07:25Z) |
| ap-northeast-1 apne1-az2 | 175 | 85% | 8.1 | 9 (11-01 14:59Z) |
| ap-northeast-1 apne1-az4 | 259 | 99% | 8.9 | 9 (11-01 00:41Z) |
| ap-northeast-2 apne2-az1 | 399 | 100% | 9.0 | 9 (11-01 14:59Z) |
| ap-northeast-2 apne2-az2 | 104 | 85% | 8.0 | 9 (10-31 20:13Z) |
| ap-northeast-2 apne2-az3 | 417 | 100% | 9.0 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az4 | 314 | 85% | 8.1 | 9 (10-31 23:11Z) |
| ap-south-1 aps1-az1 | 170 | 87% | 8.2 | 9 (11-01 07:25Z) |
| ap-south-1 aps1-az2 | 182 | 80% | 7.7 | 9 (10-31 23:11Z) |
| ap-south-1 aps1-az3 | 190 | 89% | 8.4 | 9 (11-01 14:59Z) |
| ap-southeast-2 apse2-az1 | 59 | 83% | 7.9 | 9 (11-01 14:59Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 103 | 100% | 9.0 | 9 (10-31 20:13Z) |
| us-east-1 use1-az4 | 137 | 91% | 8.4 | 9 (11-01 07:25Z) |
| us-east-1 use1-az5 | 102 | 98% | 8.9 | 9 (11-01 14:59Z) |
| us-east-1 use1-az6 | 122 | 92% | 8.4 | 9 (11-01 14:59Z) |
| us-east-2 use2-az1 | 170 | 99% | 8.9 | 9 (11-01 14:59Z) |
| us-east-2 use2-az2 | 191 | 99% | 8.9 | 9 (11-01 07:25Z) |
| us-east-2 use2-az3 | 217 | 96% | 8.7 | 9 (10-31 23:11Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 124 | 90% | 8.3 | 9 (11-01 14:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706400 | 2026-11-01T14:59:21Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-01T14:59:21Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742500 | 2026-11-01T14:59:21Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.862900 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.582200 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590700 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571900 | 2026-11-01T14:59:21Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-01T14:59:21Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.631600 | 2026-11-01T14:59:21Z |
| ap-south-1 | ap-south-1a | Windows | 0.465100 | 2026-11-01T14:59:21Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.523100 | 2026-11-01T14:59:21Z |
| ap-south-1 | ap-south-1b | Windows | 0.377500 | 2026-11-01T14:59:21Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.655800 | 2026-11-01T14:59:21Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513300 | 2026-11-01T14:59:21Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655800 | 2026-11-01T14:59:21Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.542600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.562400 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.488900 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.496600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.543500 | 2026-11-01T14:59:21Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.558600 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547100 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2b | Windows | 0.637000 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545700 | 2026-11-01T14:59:21Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553400 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2a | Windows | 0.311700 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.576400 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2b | Windows | 0.319000 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548500 | 2026-11-01T14:59:21Z |
| us-west-2 | us-west-2c | Windows | 0.312300 | 2026-11-01T14:59:21Z |
