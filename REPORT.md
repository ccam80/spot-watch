# Spot placement score log

Generated 2026-11-11 05:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 523 | 49% | 5.2 | 1 (11-11 05:59Z) |
| ap-northeast-1 | 523 | 16% | 2.7 | 1 (11-11 05:59Z) |
| ap-northeast-2 | 523 | 69% | 7.1 | 1 (11-11 05:59Z) |
| ap-south-1 | 523 | 3% | 1.7 | 1 (11-11 05:59Z) |
| ap-southeast-2 | 523 | 1% | 1.0 | 1 (11-11 05:59Z) |
| ap-southeast-3 | 523 | 24% | 3.2 | 1 (11-11 05:59Z) |
| us-east-1 | 523 | 10% | 2.6 | 2 (11-11 05:59Z) |
| us-east-2 | 523 | 30% | 3.7 | 1 (11-11 05:59Z) |
| us-west-2 | 523 | 9% | 2.1 | 2 (11-11 05:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999111999999999191911112991119199991999819919121
ap-northeast-1   879111478881951191191112211211119199919911211111
ap-northeast-2   999199999999999999992999999999999999999999999991
ap-south-1       111111111111698111111211122222122211311911112211
ap-southeast-2   111111111111111111111117111111111111111111111111
ap-southeast-3   254111839731386181111111111311111111113111111111
us-east-1        221111111112999912112333332232213222222329293322
us-east-2        211199911969999991191211191111111999919999111111
us-west-2        131111111111711121122211191111122922111211111212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
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
| ap-east-1 ape1-az1 | 163 | 6% | 1.5 | 1 (11-08 07:12Z) |
| ap-east-1 ape1-az2 | 385 | 66% | 6.7 | 1 (11-11 05:59Z) |
| ap-northeast-1 apne1-az1 | 120 | 10% | 1.9 | 1 (11-10 17:42Z) |
| ap-northeast-1 apne1-az4 | 238 | 26% | 3.5 | 1 (11-11 05:59Z) |
| ap-northeast-2 apne2-az1 | 450 | 63% | 6.6 | 1 (11-11 05:59Z) |
| ap-northeast-2 apne2-az3 | 485 | 69% | 7.0 | 9 (11-10 23:11Z) |
| ap-northeast-2 apne2-az4 | 516 | 70% | 7.2 | 1 (11-11 05:59Z) |
| ap-south-1 aps1-az1 | 151 | 1% | 1.4 | 5 (11-08 19:34Z) |
| ap-south-1 aps1-az3 | 150 | 7% | 2.3 | 1 (11-11 05:59Z) |
| ap-southeast-2 apse2-az1 | 106 | 3% | 1.2 | 1 (11-11 05:59Z) |
| ap-southeast-2 apse2-az2 | 72 | 0% | 1.0 | 1 (11-10 17:42Z) |
| ap-southeast-3 apse3-az1 | 90 | 0% | 1.0 | 1 (11-11 05:59Z) |
| ap-southeast-3 apse3-az3 | 320 | 38% | 4.3 | 1 (11-10 17:42Z) |
| us-east-1 use1-az1 | 108 | 0% | 1.1 | 1 (11-10 17:42Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 166 | 23% | 3.0 | 3 (11-10 01:27Z) |
| us-east-1 use1-az5 | 168 | 25% | 3.1 | 1 (11-11 05:59Z) |
| us-east-1 use1-az6 | 125 | 25% | 3.1 | 9 (11-10 01:27Z) |
| us-east-2 use2-az1 | 226 | 43% | 4.6 | 1 (11-10 17:42Z) |
| us-east-2 use2-az2 | 265 | 51% | 5.3 | 9 (11-08 23:39Z) |
| us-east-2 use2-az3 | 298 | 47% | 5.1 | 1 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 166 | 22% | 3.1 | 1 (11-11 05:59Z) |
| us-west-2 usw2-az2 | 123 | 17% | 2.6 | 1 (11-06 17:54Z) |
| us-west-2 usw2-az3 | 200 | 17% | 2.7 | 9 (11-07 09:56Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 523 | 71% | 7.2 | 9 (11-11 05:59Z) |
| ap-northeast-1 | 523 | 72% | 7.0 | 2 (11-11 05:59Z) |
| ap-northeast-2 | 523 | 100% | 9.0 | 9 (11-11 05:59Z) |
| ap-south-1 | 523 | 61% | 6.2 | 1 (11-11 05:59Z) |
| ap-southeast-2 | 523 | 26% | 3.5 | 1 (11-11 05:59Z) |
| ap-southeast-3 | 523 | 24% | 3.2 | 1 (11-11 05:59Z) |
| us-east-1 | 523 | 71% | 6.5 | 9 (11-11 05:59Z) |
| us-east-2 | 523 | 67% | 6.6 | 9 (11-11 05:59Z) |
| us-west-2 | 523 | 52% | 5.7 | 4 (11-11 05:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999299999219919922999999999993922992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999119112911922992199217911991392291
ap-southeast-2   999999999991991111191119199119999999919911911911
ap-southeast-3   254111839731386181111111111311111111113111111111
us-east-1        993229999999999945234697655579579999999999599669
us-east-2        999299919999999991991991291119119999999999119919
us-west-2        499929999999994492445434294944195955999999494334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 6 | 5 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 335 | 84% | 8.0 | 9 (11-11 05:59Z) |
| ap-east-1 ape1-az2 | 301 | 86% | 8.2 | 9 (11-11 05:59Z) |
| ap-east-1 ape1-az3 | 333 | 87% | 8.2 | 9 (11-11 05:59Z) |
| ap-northeast-1 apne1-az1 | 211 | 95% | 8.7 | 9 (11-09 17:23Z) |
| ap-northeast-1 apne1-az2 | 192 | 86% | 8.1 | 9 (11-10 23:11Z) |
| ap-northeast-1 apne1-az4 | 273 | 99% | 8.9 | 9 (11-10 23:11Z) |
| ap-northeast-2 apne2-az1 | 423 | 100% | 9.0 | 9 (11-11 05:59Z) |
| ap-northeast-2 apne2-az2 | 113 | 86% | 8.1 | 9 (11-09 17:23Z) |
| ap-northeast-2 apne2-az3 | 440 | 100% | 9.0 | 9 (11-11 05:59Z) |
| ap-northeast-2 apne2-az4 | 343 | 86% | 8.2 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az1 | 178 | 88% | 8.3 | 9 (11-08 19:34Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 199 | 90% | 8.4 | 9 (11-10 23:11Z) |
| ap-southeast-2 apse2-az1 | 68 | 85% | 8.1 | 9 (11-10 17:42Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 79 | 84% | 8.0 | 9 (11-08 15:03Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 149 | 92% | 8.4 | 9 (11-11 05:59Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 133 | 92% | 8.5 | 9 (11-10 09:39Z) |
| us-east-2 use2-az1 | 184 | 99% | 8.9 | 9 (11-11 05:59Z) |
| us-east-2 use2-az2 | 203 | 99% | 8.9 | 9 (11-11 05:59Z) |
| us-east-2 use2-az3 | 231 | 97% | 8.7 | 9 (11-11 05:59Z) |
| us-west-2 usw2-az1 | 97 | 98% | 8.8 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az2 | 96 | 91% | 8.3 | 9 (11-09 06:07Z) |
| us-west-2 usw2-az3 | 137 | 88% | 8.1 | 2 (11-11 05:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710800 | 2026-11-11T05:59:01Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-11T05:59:01Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.711600 | 2026-11-11T05:59:01Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.578300 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.593100 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574700 | 2026-11-11T05:59:01Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-11T05:59:01Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.588300 | 2026-11-11T05:59:01Z |
| ap-south-1 | ap-south-1a | Windows | 0.405900 | 2026-11-11T05:59:01Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.562900 | 2026-11-11T05:59:01Z |
| ap-south-1 | ap-south-1b | Windows | 0.377400 | 2026-11-11T05:59:01Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.595800 | 2026-11-11T05:59:01Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501200 | 2026-11-11T05:59:01Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.631800 | 2026-11-11T05:59:01Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530000 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.689800 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.651100 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.536300 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.477300 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.485100 | 2026-11-11T05:59:01Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.551800 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2a | Windows | 0.636900 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552000 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.550000 | 2026-11-11T05:59:01Z |
| us-east-2 | us-east-2c | Windows | 0.636900 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563900 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2a | Windows | 0.314900 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.635300 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2b | Windows | 0.306600 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.578700 | 2026-11-11T05:59:01Z |
| us-west-2 | us-west-2c | Windows | 0.290700 | 2026-11-11T05:59:01Z |
