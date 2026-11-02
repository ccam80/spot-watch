# Spot placement score log

Generated 2026-11-02 15:37 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 492 | 49% | 5.3 | 9 (11-02 15:37Z) |
| ap-northeast-1 | 492 | 16% | 2.7 | 9 (11-02 15:37Z) |
| ap-northeast-2 | 492 | 68% | 7.0 | 9 (11-02 15:37Z) |
| ap-south-1 | 492 | 3% | 1.7 | 1 (11-02 15:37Z) |
| ap-southeast-2 | 492 | 0% | 1.0 | 1 (11-02 15:37Z) |
| ap-southeast-3 | 492 | 26% | 3.3 | 8 (11-02 15:37Z) |
| us-east-1 | 492 | 11% | 2.6 | 1 (11-02 15:37Z) |
| us-east-2 | 492 | 30% | 3.7 | 9 (11-02 15:37Z) |
| us-west-2 | 492 | 9% | 2.1 | 2 (11-02 15:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999991111119991111199999999911199999999919
ap-northeast-1   111122228711112421114421111121187911147888195119
ap-northeast-2   999999999999999999999911999999999919999999999999
ap-south-1       111112211112111111111111111111111111111111169811
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111786751111111111111111155125411183973138618
us-east-1        332332222222221112222222222222122111111111299991
us-east-2        912911111111111111111111119911121119991196999999
us-west-2        122111111111111111111111111119413111111111171112
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
| ap-east-1 ape1-az1 | 156 | 6% | 1.6 | 2 (11-02 15:37Z) |
| ap-east-1 ape1-az2 | 364 | 66% | 6.7 | 9 (11-02 15:37Z) |
| ap-northeast-1 apne1-az1 | 107 | 8% | 1.7 | 6 (11-01 00:41Z) |
| ap-northeast-1 apne1-az4 | 221 | 26% | 3.5 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az1 | 422 | 62% | 6.5 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 459 | 68% | 7.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az4 | 485 | 68% | 7.1 | 9 (11-02 15:37Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 134 | 7% | 2.4 | 8 (11-01 23:31Z) |
| ap-southeast-2 apse2-az1 | 93 | 2% | 1.2 | 1 (11-01 07:25Z) |
| ap-southeast-2 apse2-az2 | 61 | 0% | 1.0 | 1 (11-01 00:41Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 309 | 39% | 4.4 | 8 (11-02 15:37Z) |
| us-east-1 use1-az1 | 101 | 0% | 1.1 | 1 (11-01 07:25Z) |
| us-east-1 use1-az2 | 134 | 3% | 1.4 | 9 (11-01 14:59Z) |
| us-east-1 use1-az4 | 161 | 24% | 3.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 158 | 26% | 3.2 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 121 | 25% | 3.1 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 211 | 43% | 4.6 | 9 (11-02 15:37Z) |
| us-east-2 use2-az2 | 253 | 50% | 5.3 | 9 (11-02 15:37Z) |
| us-east-2 use2-az3 | 280 | 47% | 5.1 | 9 (11-02 15:37Z) |
| us-west-2 usw2-az1 | 153 | 24% | 3.2 | 1 (11-02 05:51Z) |
| us-west-2 usw2-az2 | 118 | 18% | 2.6 | 1 (11-01 07:25Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 492 | 69% | 7.1 | 9 (11-02 15:37Z) |
| ap-northeast-1 | 492 | 72% | 7.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 | 492 | 100% | 9.0 | 9 (11-02 15:37Z) |
| ap-south-1 | 492 | 62% | 6.3 | 1 (11-02 15:37Z) |
| ap-southeast-2 | 492 | 24% | 3.4 | 1 (11-02 15:37Z) |
| ap-southeast-3 | 492 | 26% | 3.3 | 8 (11-02 15:37Z) |
| us-east-1 | 492 | 70% | 6.4 | 4 (11-02 15:37Z) |
| us-east-2 | 492 | 67% | 6.7 | 9 (11-02 15:37Z) |
| us-west-2 | 492 | 52% | 5.7 | 9 (11-02 15:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111339999999999999999999999999999999999999999929
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111112211112999999999999799999999999999999999911
ap-southeast-2   111111111111111119999999111319999999999999199111
ap-southeast-3   111111786751111111111111111155125411183973138618
us-east-1        999999932323334339394399999999999322999999999994
us-east-2        999993222222222222228999999999999929991999999999
us-west-2        355999994844395931211233244999549992999999999449
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
| ap-east-1 ape1-az1 | 315 | 83% | 8.0 | 9 (11-02 15:37Z) |
| ap-east-1 ape1-az2 | 274 | 85% | 8.1 | 9 (11-02 05:51Z) |
| ap-east-1 ape1-az3 | 302 | 85% | 8.1 | 9 (11-02 15:37Z) |
| ap-northeast-1 apne1-az1 | 205 | 95% | 8.7 | 9 (11-01 07:25Z) |
| ap-northeast-1 apne1-az2 | 176 | 85% | 8.1 | 9 (11-01 23:31Z) |
| ap-northeast-1 apne1-az4 | 261 | 99% | 8.9 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az1 | 402 | 100% | 9.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 420 | 100% | 9.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az4 | 317 | 85% | 8.1 | 9 (11-02 15:37Z) |
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
| us-east-2 use2-az1 | 174 | 99% | 8.9 | 9 (11-02 15:37Z) |
| us-east-2 use2-az2 | 192 | 99% | 8.9 | 9 (11-02 05:51Z) |
| us-east-2 use2-az3 | 219 | 96% | 8.7 | 9 (11-02 15:37Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 126 | 90% | 8.3 | 9 (11-02 15:37Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722600 | 2026-11-02T15:37:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-02T15:37:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732600 | 2026-11-02T15:37:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580800 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591400 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572600 | 2026-11-02T15:37:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-02T15:37:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.641300 | 2026-11-02T15:37:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.460100 | 2026-11-02T15:37:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500500 | 2026-11-02T15:37:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.377300 | 2026-11-02T15:37:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.631000 | 2026-11-02T15:37:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517600 | 2026-11-02T15:37:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.707100 | 2026-11-02T15:37:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556500 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.529700 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.551800 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.494700 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.504300 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.566800 | 2026-11-02T15:37:50Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.578000 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550400 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548800 | 2026-11-02T15:37:50Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559200 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2a | Windows | 0.309900 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.601800 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2b | Windows | 0.318300 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.560200 | 2026-11-02T15:37:50Z |
| us-west-2 | us-west-2c | Windows | 0.308900 | 2026-11-02T15:37:50Z |
