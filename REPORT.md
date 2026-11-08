# Spot placement score log

Generated 2026-11-08 15:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 514 | 49% | 5.2 | 9 (11-08 15:03Z) |
| ap-northeast-1 | 514 | 16% | 2.7 | 9 (11-08 15:03Z) |
| ap-northeast-2 | 514 | 69% | 7.1 | 9 (11-08 15:03Z) |
| ap-south-1 | 514 | 3% | 1.7 | 1 (11-08 15:03Z) |
| ap-southeast-2 | 514 | 1% | 1.1 | 1 (11-08 15:03Z) |
| ap-southeast-3 | 514 | 25% | 3.2 | 3 (11-08 15:03Z) |
| us-east-1 | 514 | 10% | 2.6 | 2 (11-08 15:03Z) |
| us-east-2 | 514 | 30% | 3.7 | 9 (11-08 15:03Z) |
| us-west-2 | 514 | 9% | 2.1 | 1 (11-08 15:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111999999999111999999999191911112991119199991999
ap-northeast-1   211111211879111478881951191191112211211119199919
ap-northeast-2   119999999999199999999999999992999999999999999999
ap-south-1       111111111111111111111698111111211122222122211311
ap-southeast-2   111111111111111111111111111111117111111111111111
ap-southeast-3   111111551254111839731386181111111111311111111113
us-east-1        222222221221111111112999912112333332232213222222
us-east-2        111199111211199911969999991191211191111111999919
us-west-2        111111194131111111111711121122211191111122922111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 4 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 163 | 6% | 1.5 | 1 (11-08 07:12Z) |
| ap-east-1 ape1-az2 | 378 | 66% | 6.7 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az1 | 117 | 10% | 1.9 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az4 | 231 | 27% | 3.5 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az1 | 441 | 63% | 6.6 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az3 | 479 | 69% | 7.0 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az4 | 507 | 70% | 7.2 | 9 (11-08 15:03Z) |
| ap-south-1 aps1-az1 | 150 | 1% | 1.3 | 3 (11-08 00:28Z) |
| ap-south-1 aps1-az3 | 141 | 6% | 2.4 | 1 (11-08 07:12Z) |
| ap-southeast-2 apse2-az1 | 102 | 3% | 1.3 | 1 (11-07 09:56Z) |
| ap-southeast-2 apse2-az2 | 70 | 0% | 1.0 | 1 (11-07 09:56Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 317 | 38% | 4.4 | 3 (11-08 15:03Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 163 | 25% | 3.2 | 1 (11-08 07:12Z) |
| us-east-1 use1-az6 | 124 | 24% | 3.0 | 1 (11-07 20:49Z) |
| us-east-2 use2-az1 | 222 | 43% | 4.6 | 9 (11-08 15:03Z) |
| us-east-2 use2-az2 | 263 | 51% | 5.3 | 9 (11-08 15:03Z) |
| us-east-2 use2-az3 | 291 | 47% | 5.1 | 9 (11-08 15:03Z) |
| us-west-2 usw2-az1 | 161 | 23% | 3.1 | 1 (11-08 07:12Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 514 | 70% | 7.2 | 9 (11-08 15:03Z) |
| ap-northeast-1 | 514 | 73% | 7.0 | 9 (11-08 15:03Z) |
| ap-northeast-2 | 514 | 100% | 9.0 | 9 (11-08 15:03Z) |
| ap-south-1 | 514 | 61% | 6.2 | 1 (11-08 15:03Z) |
| ap-southeast-2 | 514 | 25% | 3.5 | 9 (11-08 15:03Z) |
| ap-southeast-3 | 514 | 25% | 3.2 | 3 (11-08 15:03Z) |
| us-east-1 | 514 | 71% | 6.4 | 9 (11-08 15:03Z) |
| us-east-2 | 514 | 67% | 6.6 | 9 (11-08 15:03Z) |
| us-west-2 | 514 | 52% | 5.7 | 9 (11-08 15:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999299999219919922999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       997999999999999999999999119112911922992199217911
ap-southeast-2   991113199999999999991991111191119199119999999919
ap-southeast-3   111111551254111839731386181111111111311111111113
us-east-1        999999999993229999999999945234697655579579999999
us-east-2        999999999999299919999999991991991291119119999999
us-west-2        332449995499929999999994492445434294944195955999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 328 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-east-1 ape1-az2 | 294 | 86% | 8.2 | 9 (11-08 07:12Z) |
| ap-east-1 ape1-az3 | 324 | 86% | 8.2 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az1 | 210 | 95% | 8.7 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az2 | 189 | 86% | 8.1 | 9 (11-08 15:03Z) |
| ap-northeast-1 apne1-az4 | 269 | 99% | 8.9 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az1 | 418 | 100% | 9.0 | 9 (11-08 15:03Z) |
| ap-northeast-2 apne2-az2 | 111 | 86% | 8.1 | 9 (11-07 20:49Z) |
| ap-northeast-2 apne2-az3 | 434 | 100% | 9.0 | 9 (11-07 02:43Z) |
| ap-northeast-2 apne2-az4 | 335 | 86% | 8.2 | 9 (11-08 00:28Z) |
| ap-south-1 aps1-az1 | 177 | 88% | 8.3 | 9 (11-08 00:28Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 197 | 90% | 8.4 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az1 | 66 | 85% | 8.0 | 9 (11-06 23:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 79 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 110 | 100% | 9.0 | 9 (11-08 00:28Z) |
| us-east-1 use1-az4 | 145 | 92% | 8.4 | 9 (11-08 00:28Z) |
| us-east-1 use1-az5 | 107 | 98% | 8.9 | 9 (11-08 07:12Z) |
| us-east-1 use1-az6 | 129 | 92% | 8.4 | 9 (11-08 07:12Z) |
| us-east-2 use2-az1 | 181 | 99% | 8.9 | 9 (11-08 15:03Z) |
| us-east-2 use2-az2 | 199 | 99% | 8.9 | 9 (11-08 15:03Z) |
| us-east-2 use2-az3 | 227 | 96% | 8.7 | 9 (11-07 20:49Z) |
| us-west-2 usw2-az1 | 95 | 98% | 8.8 | 9 (11-08 07:12Z) |
| us-west-2 usw2-az2 | 93 | 90% | 8.3 | 9 (11-08 15:03Z) |
| us-west-2 usw2-az3 | 133 | 88% | 8.2 | 9 (11-08 07:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718700 | 2026-11-08T15:03:11Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-08T15:03:11Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.723500 | 2026-11-08T15:03:11Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579600 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.592300 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-11-08T15:03:11Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-08T15:03:11Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.561300 | 2026-11-08T15:03:11Z |
| ap-south-1 | ap-south-1a | Windows | 0.420300 | 2026-11-08T15:03:11Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.536800 | 2026-11-08T15:03:11Z |
| ap-south-1 | ap-south-1b | Windows | 0.348400 | 2026-11-08T15:03:11Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.586600 | 2026-11-08T15:03:11Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492700 | 2026-11-08T15:03:11Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.665100 | 2026-11-08T15:03:11Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530500 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.589900 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.566100 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.496400 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.426500 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.466400 | 2026-11-08T15:03:11Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549000 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548200 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546100 | 2026-11-08T15:03:11Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.546400 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2a | Windows | 0.299500 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.660000 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2b | Windows | 0.314000 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.575900 | 2026-11-08T15:03:11Z |
| us-west-2 | us-west-2c | Windows | 0.299200 | 2026-11-08T15:03:11Z |
