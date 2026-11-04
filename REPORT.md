# Spot placement score log

Generated 2026-11-04 17:07 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 499 | 48% | 5.2 | 2 (11-04 17:07Z) |
| ap-northeast-1 | 499 | 16% | 2.7 | 2 (11-04 17:07Z) |
| ap-northeast-2 | 499 | 68% | 7.0 | 9 (11-04 17:07Z) |
| ap-south-1 | 499 | 3% | 1.7 | 1 (11-04 17:07Z) |
| ap-southeast-2 | 499 | 1% | 1.1 | 7 (11-04 17:07Z) |
| ap-southeast-3 | 499 | 26% | 3.3 | 1 (11-04 17:07Z) |
| us-east-1 | 499 | 10% | 2.6 | 3 (11-04 17:07Z) |
| us-east-2 | 499 | 30% | 3.6 | 1 (11-04 17:07Z) |
| us-west-2 | 499 | 9% | 2.1 | 1 (11-04 17:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999911111199911111999999999111999999999191911112
ap-northeast-1   287111124211144211111211879111478881951191191112
ap-northeast-2   999999999999999119999999999199999999999999992999
ap-south-1       111121111111111111111111111111111111698111111211
ap-southeast-2   111111111111111111111111111111111111111111111117
ap-southeast-3   867511111111111111111551254111839731386181111111
us-east-1        222222211122222222222221221111111112999912112333
us-east-2        111111111111111111199111211199911969999991191211
us-west-2        111111111111111111111194131111111111711121122211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 157 | 6% | 1.6 | 1 (11-03 15:00Z) |
| ap-east-1 ape1-az2 | 368 | 65% | 6.6 | 1 (11-04 09:01Z) |
| ap-northeast-1 apne1-az1 | 109 | 8% | 1.7 | 1 (11-04 01:16Z) |
| ap-northeast-1 apne1-az4 | 224 | 26% | 3.5 | 1 (11-04 09:01Z) |
| ap-northeast-2 apne2-az1 | 428 | 62% | 6.6 | 9 (11-04 17:07Z) |
| ap-northeast-2 apne2-az3 | 465 | 68% | 7.0 | 9 (11-04 17:07Z) |
| ap-northeast-2 apne2-az4 | 492 | 69% | 7.1 | 9 (11-04 17:07Z) |
| ap-south-1 aps1-az1 | 141 | 1% | 1.3 | 1 (11-04 17:07Z) |
| ap-south-1 aps1-az3 | 138 | 7% | 2.4 | 1 (11-04 09:01Z) |
| ap-southeast-2 apse2-az1 | 98 | 3% | 1.3 | 7 (11-04 17:07Z) |
| ap-southeast-2 apse2-az2 | 66 | 0% | 1.0 | 1 (11-04 09:01Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 311 | 39% | 4.4 | 1 (11-04 01:16Z) |
| us-east-1 use1-az1 | 104 | 0% | 1.1 | 1 (11-04 17:07Z) |
| us-east-1 use1-az2 | 136 | 3% | 1.4 | 1 (11-04 17:07Z) |
| us-east-1 use1-az4 | 163 | 23% | 3.0 | 1 (11-04 17:07Z) |
| us-east-1 use1-az5 | 160 | 26% | 3.2 | 1 (11-04 09:01Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 213 | 43% | 4.6 | 1 (11-04 17:07Z) |
| us-east-2 use2-az2 | 255 | 50% | 5.3 | 1 (11-03 20:55Z) |
| us-east-2 use2-az3 | 281 | 47% | 5.1 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 157 | 24% | 3.2 | 1 (11-04 09:01Z) |
| us-west-2 usw2-az2 | 120 | 18% | 2.6 | 1 (11-04 01:16Z) |
| us-west-2 usw2-az3 | 195 | 16% | 2.7 | 1 (11-04 17:07Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 499 | 69% | 7.2 | 9 (11-04 17:07Z) |
| ap-northeast-1 | 499 | 72% | 7.0 | 9 (11-04 17:07Z) |
| ap-northeast-2 | 499 | 100% | 9.0 | 9 (11-04 17:07Z) |
| ap-south-1 | 499 | 62% | 6.3 | 1 (11-04 17:07Z) |
| ap-southeast-2 | 499 | 24% | 3.4 | 9 (11-04 17:07Z) |
| ap-southeast-3 | 499 | 26% | 3.3 | 1 (11-04 17:07Z) |
| us-east-1 | 499 | 70% | 6.4 | 7 (11-04 17:07Z) |
| us-east-2 | 499 | 67% | 6.7 | 1 (11-04 17:07Z) |
| us-west-2 | 499 | 51% | 5.6 | 4 (11-04 17:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999999999999999299999219
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111129999999999997999999999999999999999119112911
ap-southeast-2   111111111199999991113199999999999991991111191119
ap-southeast-3   867511111111111111111551254111839731386181111111
us-east-1        323233343393943999999999993229999999999945234697
us-east-2        222222222222289999999999999299919999999991991991
us-west-2        948443959312112332449995499929999999994492445434
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 322 | 83% | 8.0 | 9 (11-04 17:07Z) |
| ap-east-1 ape1-az2 | 280 | 85% | 8.1 | 9 (11-04 17:07Z) |
| ap-east-1 ape1-az3 | 309 | 86% | 8.1 | 9 (11-04 17:07Z) |
| ap-northeast-1 apne1-az1 | 207 | 95% | 8.7 | 9 (11-04 17:07Z) |
| ap-northeast-1 apne1-az2 | 181 | 85% | 8.1 | 9 (11-04 17:07Z) |
| ap-northeast-1 apne1-az4 | 265 | 99% | 8.9 | 9 (11-04 17:07Z) |
| ap-northeast-2 apne2-az1 | 409 | 100% | 9.0 | 9 (11-04 17:07Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 427 | 100% | 9.0 | 9 (11-04 17:07Z) |
| ap-northeast-2 apne2-az4 | 324 | 85% | 8.1 | 9 (11-04 17:07Z) |
| ap-south-1 aps1-az1 | 173 | 87% | 8.2 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az2 | 184 | 80% | 7.7 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az3 | 193 | 90% | 8.4 | 9 (11-04 01:16Z) |
| ap-southeast-2 apse2-az1 | 61 | 84% | 8.0 | 8 (11-04 17:07Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 104 | 98% | 8.9 | 9 (11-04 09:01Z) |
| us-east-1 use1-az6 | 125 | 92% | 8.4 | 9 (11-04 09:01Z) |
| us-east-2 use2-az1 | 176 | 99% | 8.9 | 9 (11-04 09:01Z) |
| us-east-2 use2-az2 | 193 | 99% | 8.9 | 9 (11-03 06:36Z) |
| us-east-2 use2-az3 | 222 | 96% | 8.7 | 9 (11-04 09:01Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 128 | 88% | 8.2 | 2 (11-04 01:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.720900 | 2026-11-04T17:07:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-04T17:07:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.736500 | 2026-11-04T17:07:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579800 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591700 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571500 | 2026-11-04T17:07:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-04T17:07:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.601500 | 2026-11-04T17:07:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.440100 | 2026-11-04T17:07:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.532000 | 2026-11-04T17:07:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.365800 | 2026-11-04T17:07:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.585900 | 2026-11-04T17:07:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507500 | 2026-11-04T17:07:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.725300 | 2026-11-04T17:07:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.553400 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.510500 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.528800 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.479600 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.458400 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.550000 | 2026-11-04T17:07:24Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550500 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551200 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546900 | 2026-11-04T17:07:24Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.572500 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2a | Windows | 0.306500 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.671200 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2b | Windows | 0.319800 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.611400 | 2026-11-04T17:07:24Z |
| us-west-2 | us-west-2c | Windows | 0.306000 | 2026-11-04T17:07:24Z |
