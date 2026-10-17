# Spot placement score log

Generated 2026-10-17 13:39 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 326 | 38% | 4.5 | 9 (10-17 13:39Z) |
| ap-northeast-1 | 326 | 15% | 2.7 | 9 (10-17 13:39Z) |
| ap-northeast-2 | 326 | 52% | 6.1 | 9 (10-17 13:39Z) |
| ap-south-1 | 326 | 2% | 1.8 | 2 (10-17 13:39Z) |
| ap-southeast-2 | 326 | 0% | 1.0 | 1 (10-17 13:39Z) |
| ap-southeast-3 | 326 | 22% | 3.3 | 8 (10-17 13:39Z) |
| us-east-1 | 326 | 9% | 2.5 | 3 (10-17 13:39Z) |
| us-east-2 | 326 | 28% | 3.6 | 1 (10-17 13:39Z) |
| us-west-2 | 326 | 11% | 2.3 | 2 (10-17 13:39Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111118229299999999999999999999999999999
ap-northeast-1   511971111119111222211922121211142211421111322129
ap-northeast-2   999999999999919999999999999999999999999999999999
ap-south-1       222221112211111122222222221111122222221112222222
ap-southeast-2   111111111111111111111111111111111111111111111191
ap-southeast-3   113881111138911999793951511221111311518214387518
us-east-1        211112221132323331922332221133332321323122222333
us-east-2        111111111111111811999999111129911129111999111161
us-west-2        121111111111119999111111111111111111221111222112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 8 | 5 | 5 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 231 | 53% | 5.8 | 9 (10-17 13:39Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 153 | 25% | 3.6 | 9 (10-17 13:39Z) |
| ap-northeast-2 apne2-az1 | 285 | 49% | 5.8 | 2 (10-17 13:39Z) |
| ap-northeast-2 apne2-az3 | 298 | 53% | 6.1 | 9 (10-17 13:39Z) |
| ap-northeast-2 apne2-az4 | 323 | 53% | 6.1 | 9 (10-17 13:39Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 52 | 2% | 1.2 | 9 (10-17 09:13Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 220 | 32% | 4.2 | 8 (10-17 13:39Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 92 | 3% | 1.5 | 1 (10-17 13:39Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 102 | 24% | 3.1 | 1 (10-17 09:13Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 127 | 39% | 4.5 | 9 (10-16 07:03Z) |
| us-east-2 use2-az2 | 166 | 44% | 4.9 | 1 (10-17 04:14Z) |
| us-east-2 use2-az3 | 197 | 42% | 4.9 | 1 (10-17 13:39Z) |
| us-west-2 usw2-az1 | 117 | 26% | 3.5 | 1 (10-17 13:39Z) |
| us-west-2 usw2-az2 | 68 | 25% | 3.4 | 1 (10-17 09:13Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 326 | 53% | 6.2 | 9 (10-17 13:39Z) |
| ap-northeast-1 | 326 | 73% | 7.1 | 9 (10-17 13:39Z) |
| ap-northeast-2 | 326 | 100% | 9.0 | 9 (10-17 13:39Z) |
| ap-south-1 | 326 | 61% | 6.4 | 9 (10-17 13:39Z) |
| ap-southeast-2 | 326 | 17% | 3.1 | 9 (10-17 13:39Z) |
| ap-southeast-3 | 326 | 22% | 3.3 | 8 (10-17 13:39Z) |
| us-east-1 | 326 | 71% | 6.5 | 9 (10-17 13:39Z) |
| us-east-2 | 326 | 70% | 6.9 | 9 (10-17 13:39Z) |
| us-west-2 | 326 | 51% | 5.7 | 9 (10-17 13:39Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   913991199119999999999999923992399921999119999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992999199914999999999992991999122992299912999999
ap-southeast-2   111911111111891999999111111111118111111111111999
ap-southeast-3   113881111138911999793951511221111311518214387518
us-east-1        343336635464569982999999454266643555546793446599
us-east-2        321212111212119922999999119129911229111999311399
us-west-2        441323331332339999993592994424953433554334454439
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 198 | 73% | 7.4 | 9 (10-17 13:39Z) |
| ap-east-1 ape1-az2 | 167 | 75% | 7.5 | 9 (10-17 09:13Z) |
| ap-east-1 ape1-az3 | 168 | 74% | 7.4 | 9 (10-17 13:39Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 94 | 71% | 7.3 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az4 | 185 | 98% | 8.9 | 9 (10-17 13:39Z) |
| ap-northeast-2 apne2-az1 | 257 | 100% | 9.0 | 9 (10-17 09:13Z) |
| ap-northeast-2 apne2-az2 | 71 | 79% | 7.7 | 9 (10-17 04:14Z) |
| ap-northeast-2 apne2-az3 | 281 | 100% | 9.0 | 9 (10-17 13:39Z) |
| ap-northeast-2 apne2-az4 | 194 | 76% | 7.5 | 9 (10-17 13:39Z) |
| ap-south-1 aps1-az1 | 115 | 81% | 7.9 | 9 (10-17 09:13Z) |
| ap-south-1 aps1-az2 | 117 | 69% | 7.1 | 9 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 134 | 86% | 8.2 | 9 (10-17 09:13Z) |
| ap-southeast-2 apse2-az1 | 25 | 60% | 6.5 | 9 (10-17 09:13Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 39 | 67% | 6.9 | 9 (10-17 13:39Z) |
| ap-southeast-3 apse3-az3 | 63 | 30% | 4.7 | 4 (10-16 12:19Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 82 | 100% | 9.0 | 9 (10-17 13:39Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 63 | 97% | 8.8 | 9 (10-17 09:13Z) |
| us-east-1 use1-az6 | 86 | 95% | 8.7 | 9 (10-17 13:39Z) |
| us-east-2 use2-az1 | 109 | 98% | 8.9 | 9 (10-17 13:39Z) |
| us-east-2 use2-az2 | 155 | 99% | 8.9 | 9 (10-17 09:13Z) |
| us-east-2 use2-az3 | 144 | 94% | 8.6 | 7 (10-16 12:19Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 70 | 96% | 8.7 | 9 (10-17 13:39Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710800 | 2026-10-17T13:39:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-17T13:39:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.756900 | 2026-10-17T13:39:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.939800 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587400 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582100 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569800 | 2026-10-17T13:39:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741300 | 2026-10-17T13:39:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.560700 | 2026-10-17T13:39:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-10-17T13:39:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.705700 | 2026-10-17T13:39:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.348800 | 2026-10-17T13:39:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719000 | 2026-10-17T13:39:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523600 | 2026-10-17T13:39:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.585000 | 2026-10-17T13:39:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.432300 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.533600 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.482500 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.422300 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.471500 | 2026-10-17T13:39:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548200 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2a | Windows | 0.643600 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.538800 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2b | Windows | 0.639700 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.536200 | 2026-10-17T13:39:32Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.522700 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2a | Windows | 0.314800 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499800 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2b | Windows | 0.330300 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.495700 | 2026-10-17T13:39:32Z |
| us-west-2 | us-west-2c | Windows | 0.314400 | 2026-10-17T13:39:32Z |
