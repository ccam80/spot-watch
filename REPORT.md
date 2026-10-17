# Spot placement score log

Generated 2026-10-17 22:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 329 | 39% | 4.6 | 9 (10-17 22:13Z) |
| ap-northeast-1 | 329 | 15% | 2.7 | 4 (10-17 22:13Z) |
| ap-northeast-2 | 329 | 53% | 6.1 | 9 (10-17 22:13Z) |
| ap-south-1 | 329 | 2% | 1.8 | 2 (10-17 22:13Z) |
| ap-southeast-2 | 329 | 1% | 1.1 | 1 (10-17 22:13Z) |
| ap-southeast-3 | 329 | 23% | 3.3 | 9 (10-17 22:13Z) |
| us-east-1 | 329 | 9% | 2.5 | 1 (10-17 22:13Z) |
| us-east-2 | 329 | 28% | 3.6 | 9 (10-17 22:13Z) |
| us-west-2 | 329 | 11% | 2.3 | 1 (10-17 22:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111118229299999999999999999999999999999999
ap-northeast-1   971111119111222211922121211142211421111322129324
ap-northeast-2   999999999919999999999999999999999999999999999999
ap-south-1       221112211111122222222221111122222221112222222222
ap-southeast-2   111111111111111111111111111111111111111111191191
ap-southeast-3   881111138911999793951511221111311518214387518679
us-east-1        112221132323331922332221133332321323122222333221
us-east-2        111111111111811999999111129911129111999111161999
us-west-2        111111111119999111111111111111111221111222112121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 8 | 5 | 5 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 234 | 54% | 5.9 | 9 (10-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 155 | 25% | 3.5 | 3 (10-17 22:13Z) |
| ap-northeast-2 apne2-az1 | 288 | 49% | 5.8 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 301 | 53% | 6.1 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az4 | 326 | 53% | 6.2 | 9 (10-17 22:13Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 223 | 33% | 4.3 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 63 | 0% | 1.1 | 1 (10-17 22:13Z) |
| us-east-1 use1-az2 | 92 | 3% | 1.5 | 1 (10-17 13:39Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 103 | 23% | 3.1 | 1 (10-17 19:18Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 128 | 40% | 4.5 | 9 (10-17 22:13Z) |
| us-east-2 use2-az2 | 169 | 45% | 4.9 | 9 (10-17 22:13Z) |
| us-east-2 use2-az3 | 200 | 43% | 4.9 | 9 (10-17 22:13Z) |
| us-west-2 usw2-az1 | 117 | 26% | 3.5 | 1 (10-17 13:39Z) |
| us-west-2 usw2-az2 | 70 | 24% | 3.3 | 1 (10-17 19:18Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 329 | 53% | 6.2 | 9 (10-17 22:13Z) |
| ap-northeast-1 | 329 | 74% | 7.2 | 9 (10-17 22:13Z) |
| ap-northeast-2 | 329 | 100% | 9.0 | 9 (10-17 22:13Z) |
| ap-south-1 | 329 | 61% | 6.4 | 9 (10-17 22:13Z) |
| ap-southeast-2 | 329 | 18% | 3.2 | 9 (10-17 22:13Z) |
| ap-southeast-3 | 329 | 23% | 3.3 | 9 (10-17 22:13Z) |
| us-east-1 | 329 | 71% | 6.5 | 9 (10-17 22:13Z) |
| us-east-2 | 329 | 70% | 6.9 | 9 (10-17 22:13Z) |
| us-west-2 | 329 | 52% | 5.7 | 9 (10-17 22:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   991199119999999999999923992399921999119999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999199914999999999992991999122992299912999999999
ap-southeast-2   911111111891999999111111111118111111111111999999
ap-southeast-3   881111138911999793951511221111311518214387518679
us-east-1        336635464569982999999454266643555546793446599999
us-east-2        212111212119922999999119129911229111999311399999
us-west-2        323331332339999993592994424953433554334454439999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 200 | 73% | 7.4 | 9 (10-17 19:18Z) |
| ap-east-1 ape1-az2 | 168 | 76% | 7.5 | 9 (10-17 22:13Z) |
| ap-east-1 ape1-az3 | 169 | 74% | 7.4 | 9 (10-17 19:18Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 95 | 72% | 7.3 | 9 (10-17 17:03Z) |
| ap-northeast-1 apne1-az4 | 187 | 98% | 8.9 | 9 (10-17 19:18Z) |
| ap-northeast-2 apne2-az1 | 258 | 100% | 9.0 | 9 (10-17 17:03Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 283 | 100% | 9.0 | 9 (10-17 19:18Z) |
| ap-northeast-2 apne2-az4 | 196 | 76% | 7.6 | 9 (10-17 22:13Z) |
| ap-south-1 aps1-az1 | 116 | 81% | 7.9 | 9 (10-17 22:13Z) |
| ap-south-1 aps1-az2 | 118 | 69% | 7.2 | 9 (10-17 17:03Z) |
| ap-south-1 aps1-az3 | 135 | 86% | 8.2 | 9 (10-17 17:03Z) |
| ap-southeast-2 apse2-az1 | 27 | 63% | 6.7 | 9 (10-17 22:13Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 41 | 68% | 7.0 | 9 (10-17 22:13Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 83 | 100% | 9.0 | 9 (10-17 19:18Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 65 | 97% | 8.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az6 | 87 | 95% | 8.7 | 9 (10-17 19:18Z) |
| us-east-2 use2-az1 | 110 | 98% | 8.9 | 9 (10-17 19:18Z) |
| us-east-2 use2-az2 | 156 | 99% | 8.9 | 9 (10-17 22:13Z) |
| us-east-2 use2-az3 | 146 | 95% | 8.6 | 9 (10-17 19:18Z) |
| us-west-2 usw2-az1 | 76 | 97% | 8.8 | 9 (10-17 22:13Z) |
| us-west-2 usw2-az2 | 70 | 96% | 8.7 | 9 (10-17 13:39Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710000 | 2026-10-17T22:13:11Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-17T22:13:11Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.762000 | 2026-10-17T22:13:11Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.942900 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587900 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582000 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569500 | 2026-10-17T22:13:11Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741300 | 2026-10-17T22:13:11Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.559900 | 2026-10-17T22:13:11Z |
| ap-south-1 | ap-south-1a | Windows | 0.388800 | 2026-10-17T22:13:11Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.718600 | 2026-10-17T22:13:11Z |
| ap-south-1 | ap-south-1b | Windows | 0.348800 | 2026-10-17T22:13:11Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718700 | 2026-10-17T22:13:11Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522900 | 2026-10-17T22:13:11Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.601100 | 2026-10-17T22:13:11Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.431100 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.533200 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.484700 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.431700 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.477900 | 2026-10-17T22:13:11Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549000 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2a | Windows | 0.643500 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.540300 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2b | Windows | 0.639500 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.538500 | 2026-10-17T22:13:11Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.521600 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2a | Windows | 0.314400 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.497800 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2b | Windows | 0.329900 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.493400 | 2026-10-17T22:13:11Z |
| us-west-2 | us-west-2c | Windows | 0.314000 | 2026-10-17T22:13:11Z |
