# Spot placement score log

Generated 2026-11-02 05:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 491 | 49% | 5.3 | 1 (11-02 05:51Z) |
| ap-northeast-1 | 491 | 15% | 2.7 | 1 (11-02 05:51Z) |
| ap-northeast-2 | 491 | 68% | 7.0 | 9 (11-02 05:51Z) |
| ap-south-1 | 491 | 3% | 1.7 | 1 (11-02 05:51Z) |
| ap-southeast-2 | 491 | 0% | 1.0 | 1 (11-02 05:51Z) |
| ap-southeast-3 | 491 | 26% | 3.3 | 1 (11-02 05:51Z) |
| us-east-1 | 491 | 11% | 2.6 | 9 (11-02 05:51Z) |
| us-east-2 | 491 | 30% | 3.6 | 9 (11-02 05:51Z) |
| us-west-2 | 491 | 9% | 2.1 | 1 (11-02 05:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999111111999111119999999991119999999991
ap-northeast-1   111112222871111242111442111112118791114788819511
ap-northeast-2   999999999999999999999991199999999991999999999999
ap-south-1       111111221111211111111111111111111111111111116981
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111178675111111111111111115512541118397313861
us-east-1        333233222222222111222222222222212211111111129999
us-east-2        991291111111111111111111111991112111999119699999
us-west-2        112211111111111111111111111111941311111111117111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 155 | 6% | 1.6 | 1 (10-31 18:15Z) |
| ap-east-1 ape1-az2 | 363 | 66% | 6.6 | 9 (11-01 23:31Z) |
| ap-northeast-1 apne1-az1 | 107 | 8% | 1.7 | 6 (11-01 00:41Z) |
| ap-northeast-1 apne1-az4 | 220 | 25% | 3.5 | 9 (11-01 14:59Z) |
| ap-northeast-2 apne2-az1 | 421 | 62% | 6.5 | 9 (11-02 05:51Z) |
| ap-northeast-2 apne2-az3 | 458 | 68% | 7.0 | 9 (11-02 05:51Z) |
| ap-northeast-2 apne2-az4 | 484 | 68% | 7.1 | 9 (11-02 05:51Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 134 | 7% | 2.4 | 8 (11-01 23:31Z) |
| ap-southeast-2 apse2-az1 | 93 | 2% | 1.2 | 1 (11-01 07:25Z) |
| ap-southeast-2 apse2-az2 | 61 | 0% | 1.0 | 1 (11-01 00:41Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 308 | 39% | 4.4 | 3 (11-01 00:41Z) |
| us-east-1 use1-az1 | 101 | 0% | 1.1 | 1 (11-01 07:25Z) |
| us-east-1 use1-az2 | 134 | 3% | 1.4 | 9 (11-01 14:59Z) |
| us-east-1 use1-az4 | 161 | 24% | 3.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 158 | 26% | 3.2 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 121 | 25% | 3.1 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 210 | 43% | 4.6 | 9 (11-02 05:51Z) |
| us-east-2 use2-az2 | 252 | 50% | 5.2 | 9 (11-02 05:51Z) |
| us-east-2 use2-az3 | 279 | 47% | 5.1 | 9 (11-02 05:51Z) |
| us-west-2 usw2-az1 | 153 | 24% | 3.2 | 1 (11-02 05:51Z) |
| us-west-2 usw2-az2 | 118 | 18% | 2.6 | 1 (11-01 07:25Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 491 | 69% | 7.1 | 9 (11-02 05:51Z) |
| ap-northeast-1 | 491 | 72% | 7.0 | 2 (11-02 05:51Z) |
| ap-northeast-2 | 491 | 100% | 9.0 | 9 (11-02 05:51Z) |
| ap-south-1 | 491 | 63% | 6.3 | 1 (11-02 05:51Z) |
| ap-southeast-2 | 491 | 24% | 3.4 | 1 (11-02 05:51Z) |
| ap-southeast-3 | 491 | 26% | 3.3 | 1 (11-02 05:51Z) |
| us-east-1 | 491 | 70% | 6.4 | 9 (11-02 05:51Z) |
| us-east-2 | 491 | 67% | 6.7 | 9 (11-02 05:51Z) |
| us-west-2 | 491 | 52% | 5.7 | 4 (11-02 05:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111133999999999999999999999999999999999999999992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111221111299999999999979999999999999999999991
ap-southeast-2   111111111111111111999999911131999999999999919911
ap-southeast-3   111111178675111111111111111115512541118397313861
us-east-1        999999993232333433939439999999999932299999999999
us-east-2        999999322222222222222899999999999992999199999999
us-west-2        335599999484439593121123324499954999299999999944
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 314 | 83% | 8.0 | 9 (11-02 05:51Z) |
| ap-east-1 ape1-az2 | 274 | 85% | 8.1 | 9 (11-02 05:51Z) |
| ap-east-1 ape1-az3 | 301 | 85% | 8.1 | 9 (11-01 23:31Z) |
| ap-northeast-1 apne1-az1 | 205 | 95% | 8.7 | 9 (11-01 07:25Z) |
| ap-northeast-1 apne1-az2 | 176 | 85% | 8.1 | 9 (11-01 23:31Z) |
| ap-northeast-1 apne1-az4 | 260 | 99% | 8.9 | 9 (11-01 19:33Z) |
| ap-northeast-2 apne2-az1 | 401 | 100% | 9.0 | 9 (11-02 05:51Z) |
| ap-northeast-2 apne2-az2 | 105 | 85% | 8.0 | 9 (11-01 19:33Z) |
| ap-northeast-2 apne2-az3 | 419 | 100% | 9.0 | 9 (11-01 23:31Z) |
| ap-northeast-2 apne2-az4 | 316 | 85% | 8.1 | 9 (11-02 05:51Z) |
| ap-south-1 aps1-az1 | 171 | 87% | 8.2 | 9 (11-01 23:31Z) |
| ap-south-1 aps1-az2 | 182 | 80% | 7.7 | 9 (10-31 23:11Z) |
| ap-south-1 aps1-az3 | 191 | 90% | 8.4 | 9 (11-01 23:31Z) |
| ap-southeast-2 apse2-az1 | 59 | 83% | 7.9 | 9 (11-01 14:59Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 103 | 98% | 8.9 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 124 | 92% | 8.4 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 173 | 99% | 8.9 | 9 (11-02 05:51Z) |
| us-east-2 use2-az2 | 192 | 99% | 8.9 | 9 (11-02 05:51Z) |
| us-east-2 use2-az3 | 218 | 96% | 8.7 | 9 (11-01 23:31Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 125 | 90% | 8.3 | 9 (11-01 19:33Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.717300 | 2026-11-02T05:51:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-02T05:51:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.733700 | 2026-11-02T05:51:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.581400 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591700 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572500 | 2026-11-02T05:51:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-02T05:51:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.639400 | 2026-11-02T05:51:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.461900 | 2026-11-02T05:51:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.511400 | 2026-11-02T05:51:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.376900 | 2026-11-02T05:51:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651100 | 2026-11-02T05:51:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515600 | 2026-11-02T05:51:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.679200 | 2026-11-02T05:51:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.536000 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.556100 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.498200 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.499200 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.554200 | 2026-11-02T05:51:58Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.581600 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551000 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548800 | 2026-11-02T05:51:58Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.554900 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2a | Windows | 0.310900 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.591900 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2b | Windows | 0.317400 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.550300 | 2026-11-02T05:51:58Z |
| us-west-2 | us-west-2c | Windows | 0.309900 | 2026-11-02T05:51:58Z |
