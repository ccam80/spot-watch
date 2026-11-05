# Spot placement score log

Generated 2026-11-05 15:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 502 | 49% | 5.2 | 1 (11-05 15:23Z) |
| ap-northeast-1 | 502 | 16% | 2.7 | 1 (11-05 15:23Z) |
| ap-northeast-2 | 502 | 68% | 7.1 | 9 (11-05 15:23Z) |
| ap-south-1 | 502 | 3% | 1.7 | 2 (11-05 15:23Z) |
| ap-southeast-2 | 502 | 1% | 1.1 | 1 (11-05 15:23Z) |
| ap-southeast-3 | 502 | 25% | 3.2 | 1 (11-05 15:23Z) |
| us-east-1 | 502 | 10% | 2.6 | 2 (11-05 15:23Z) |
| us-east-2 | 502 | 30% | 3.6 | 1 (11-05 15:23Z) |
| us-west-2 | 502 | 9% | 2.1 | 1 (11-05 15:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911111199911111999999999111999999999191911112991
ap-northeast-1   111124211144211111211879111478881951191191112211
ap-northeast-2   999999999999119999999999199999999999999992999999
ap-south-1       121111111111111111111111111111111698111111211122
ap-southeast-2   111111111111111111111111111111111111111111117111
ap-southeast-3   511111111111111111551254111839731386181111111111
us-east-1        222211122222222222221221111111112999912112333332
us-east-2        111111111111111199111211199911969999991191211191
us-west-2        111111111111111111194131111111111711121122211191
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 160 | 6% | 1.6 | 1 (11-05 15:23Z) |
| ap-east-1 ape1-az2 | 370 | 66% | 6.6 | 9 (11-05 06:32Z) |
| ap-northeast-1 apne1-az1 | 109 | 8% | 1.7 | 1 (11-04 01:16Z) |
| ap-northeast-1 apne1-az4 | 225 | 26% | 3.5 | 1 (11-05 06:32Z) |
| ap-northeast-2 apne2-az1 | 431 | 62% | 6.6 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az3 | 467 | 68% | 7.0 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az4 | 495 | 69% | 7.1 | 9 (11-05 15:23Z) |
| ap-south-1 aps1-az1 | 143 | 1% | 1.3 | 1 (11-05 15:23Z) |
| ap-south-1 aps1-az3 | 138 | 7% | 2.4 | 1 (11-04 09:01Z) |
| ap-southeast-2 apse2-az1 | 98 | 3% | 1.3 | 7 (11-04 17:07Z) |
| ap-southeast-2 apse2-az2 | 66 | 0% | 1.0 | 1 (11-04 09:01Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 311 | 39% | 4.4 | 1 (11-04 01:16Z) |
| us-east-1 use1-az1 | 104 | 0% | 1.1 | 1 (11-04 17:07Z) |
| us-east-1 use1-az2 | 138 | 3% | 1.4 | 1 (11-05 15:23Z) |
| us-east-1 use1-az4 | 164 | 23% | 3.0 | 1 (11-04 23:34Z) |
| us-east-1 use1-az5 | 161 | 25% | 3.2 | 1 (11-05 06:32Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 216 | 42% | 4.6 | 1 (11-05 15:23Z) |
| us-east-2 use2-az2 | 257 | 50% | 5.3 | 1 (11-05 15:23Z) |
| us-east-2 use2-az3 | 282 | 47% | 5.1 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az1 | 157 | 24% | 3.2 | 1 (11-04 09:01Z) |
| us-west-2 usw2-az2 | 120 | 18% | 2.6 | 1 (11-04 01:16Z) |
| us-west-2 usw2-az3 | 198 | 17% | 2.7 | 1 (11-05 15:23Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 502 | 70% | 7.2 | 9 (11-05 15:23Z) |
| ap-northeast-1 | 502 | 72% | 7.0 | 9 (11-05 15:23Z) |
| ap-northeast-2 | 502 | 100% | 9.0 | 9 (11-05 15:23Z) |
| ap-south-1 | 502 | 62% | 6.3 | 2 (11-05 15:23Z) |
| ap-southeast-2 | 502 | 24% | 3.4 | 9 (11-05 15:23Z) |
| ap-southeast-3 | 502 | 25% | 3.2 | 1 (11-05 15:23Z) |
| us-east-1 | 502 | 70% | 6.4 | 5 (11-05 15:23Z) |
| us-east-2 | 502 | 67% | 6.6 | 1 (11-05 15:23Z) |
| us-west-2 | 502 | 51% | 5.6 | 4 (11-05 15:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999999999999299999219919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       129999999999997999999999999999999999119112911922
ap-southeast-2   111111199999991113199999999999991991111191119199
ap-southeast-3   511111111111111111551254111839731386181111111111
us-east-1        233343393943999999999993229999999999945234697655
us-east-2        222222222289999999999999299919999999991991991291
us-west-2        443959312112332449995499929999999994492445434294
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 325 | 83% | 8.0 | 9 (11-05 15:23Z) |
| ap-east-1 ape1-az2 | 283 | 86% | 8.1 | 9 (11-05 15:23Z) |
| ap-east-1 ape1-az3 | 312 | 86% | 8.2 | 9 (11-05 15:23Z) |
| ap-northeast-1 apne1-az1 | 208 | 95% | 8.7 | 9 (11-05 15:23Z) |
| ap-northeast-1 apne1-az2 | 183 | 85% | 8.1 | 9 (11-05 15:23Z) |
| ap-northeast-1 apne1-az4 | 267 | 99% | 8.9 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az1 | 411 | 100% | 9.0 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 429 | 100% | 9.0 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az4 | 326 | 86% | 8.1 | 9 (11-05 06:32Z) |
| ap-south-1 aps1-az1 | 174 | 87% | 8.2 | 9 (11-04 23:34Z) |
| ap-south-1 aps1-az2 | 184 | 80% | 7.7 | 9 (11-04 01:16Z) |
| ap-south-1 aps1-az3 | 194 | 90% | 8.4 | 9 (11-04 23:34Z) |
| ap-southeast-2 apse2-az1 | 63 | 84% | 8.0 | 9 (11-05 15:23Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 73 | 82% | 7.9 | 9 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 104 | 98% | 8.9 | 9 (11-04 09:01Z) |
| us-east-1 use1-az6 | 125 | 92% | 8.4 | 9 (11-04 09:01Z) |
| us-east-2 use2-az1 | 177 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az2 | 194 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az3 | 223 | 96% | 8.7 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 89 | 90% | 8.3 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az3 | 129 | 88% | 8.2 | 9 (11-05 06:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718000 | 2026-11-05T15:23:19Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-05T15:23:19Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.735500 | 2026-11-05T15:23:19Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580700 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.593500 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573000 | 2026-11-05T15:23:19Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-05T15:23:19Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.600200 | 2026-11-05T15:23:19Z |
| ap-south-1 | ap-south-1a | Windows | 0.432900 | 2026-11-05T15:23:19Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.545900 | 2026-11-05T15:23:19Z |
| ap-south-1 | ap-south-1b | Windows | 0.361000 | 2026-11-05T15:23:19Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.582900 | 2026-11-05T15:23:19Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507500 | 2026-11-05T15:23:19Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.731700 | 2026-11-05T15:23:19Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.554600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.524300 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.505000 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.481500 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.449200 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.528600 | 2026-11-05T15:23:19Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550400 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551600 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548300 | 2026-11-05T15:23:19Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.562800 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2a | Windows | 0.304200 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.685500 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2b | Windows | 0.318200 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.605100 | 2026-11-05T15:23:19Z |
| us-west-2 | us-west-2c | Windows | 0.303900 | 2026-11-05T15:23:19Z |
