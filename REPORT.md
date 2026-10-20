# Spot placement score log

Generated 2026-10-20 00:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 341 | 40% | 4.7 | 1 (10-20 00:15Z) |
| ap-northeast-1 | 341 | 16% | 2.8 | 1 (10-20 00:15Z) |
| ap-northeast-2 | 341 | 54% | 6.2 | 9 (10-20 00:15Z) |
| ap-south-1 | 341 | 2% | 1.8 | 2 (10-20 00:15Z) |
| ap-southeast-2 | 341 | 1% | 1.1 | 1 (10-20 00:15Z) |
| ap-southeast-3 | 341 | 24% | 3.4 | 7 (10-20 00:15Z) |
| us-east-1 | 341 | 11% | 2.7 | 2 (10-20 00:15Z) |
| us-east-2 | 341 | 30% | 3.7 | 9 (10-20 00:15Z) |
| us-west-2 | 341 | 11% | 2.3 | 1 (10-20 00:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        229299999999999999999999999999999999999999999991
ap-northeast-1   222211922121211142211421111322129324165912221981
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       122222222221111122222221112222222222222222222222
ap-southeast-2   111111111111111111111111111111191191111111111111
ap-southeast-3   999793951511221111311518214387518679924748811787
us-east-1        331922332221133332321323122222333221923999999112
us-east-2        811999999111129911129111999111161999999199999119
us-west-2        999111111111111111111221111222112121219119211211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 6 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 119 | 8% | 1.7 | 1 (10-20 00:15Z) |
| ap-east-1 ape1-az2 | 245 | 56% | 6.0 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 159 | 26% | 3.6 | 7 (10-19 20:59Z) |
| ap-northeast-2 apne2-az1 | 295 | 50% | 5.9 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az3 | 313 | 55% | 6.2 | 9 (10-20 00:15Z) |
| ap-northeast-2 apne2-az4 | 338 | 55% | 6.3 | 9 (10-20 00:15Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 72 | 0% | 1.0 | 1 (10-20 00:15Z) |
| ap-southeast-3 apse3-az3 | 231 | 34% | 4.3 | 7 (10-20 00:15Z) |
| us-east-1 use1-az1 | 65 | 0% | 1.1 | 1 (10-19 07:40Z) |
| us-east-1 use1-az2 | 96 | 3% | 1.5 | 1 (10-20 00:15Z) |
| us-east-1 use1-az4 | 104 | 31% | 3.7 | 9 (10-19 01:08Z) |
| us-east-1 use1-az5 | 110 | 28% | 3.5 | 8 (10-19 07:40Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 137 | 43% | 4.8 | 9 (10-20 00:15Z) |
| us-east-2 use2-az2 | 178 | 47% | 5.1 | 9 (10-20 00:15Z) |
| us-east-2 use2-az3 | 209 | 45% | 5.1 | 9 (10-20 00:15Z) |
| us-west-2 usw2-az1 | 123 | 27% | 3.5 | 1 (10-20 00:15Z) |
| us-west-2 usw2-az2 | 72 | 25% | 3.3 | 1 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 341 | 55% | 6.3 | 9 (10-20 00:15Z) |
| ap-northeast-1 | 341 | 74% | 7.2 | 1 (10-20 00:15Z) |
| ap-northeast-2 | 341 | 100% | 9.0 | 9 (10-20 00:15Z) |
| ap-south-1 | 341 | 62% | 6.5 | 9 (10-20 00:15Z) |
| ap-southeast-2 | 341 | 20% | 3.3 | 1 (10-20 00:15Z) |
| ap-southeast-3 | 341 | 24% | 3.4 | 7 (10-20 00:15Z) |
| us-east-1 | 341 | 71% | 6.6 | 4 (10-20 00:15Z) |
| us-east-2 | 341 | 71% | 6.9 | 9 (10-20 00:15Z) |
| us-west-2 | 341 | 53% | 5.8 | 4 (10-20 00:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999923992399921999119999999999999999932991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999992991999122992299912999999999999999992999
ap-southeast-2   999999111111111118111111111111999999999999111911
ap-southeast-3   999793951511221111311518214387518679924748811787
us-east-1        982999999454266643555546793446599999999999999464
us-east-2        922999999119129911229111999311399999999999999239
us-west-2        999993592994424953433554334454439999999999999534
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 6 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 209 | 74% | 7.4 | 9 (10-20 00:15Z) |
| ap-east-1 ape1-az2 | 172 | 76% | 7.6 | 9 (10-19 15:31Z) |
| ap-east-1 ape1-az3 | 176 | 75% | 7.5 | 9 (10-20 00:15Z) |
| ap-northeast-1 apne1-az1 | 157 | 93% | 8.6 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az2 | 99 | 73% | 7.3 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az4 | 194 | 98% | 8.9 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az1 | 266 | 100% | 9.0 | 9 (10-20 00:15Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 294 | 100% | 9.0 | 9 (10-20 00:15Z) |
| ap-northeast-2 apne2-az4 | 204 | 77% | 7.6 | 9 (10-20 00:15Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 125 | 71% | 7.3 | 9 (10-20 00:15Z) |
| ap-south-1 aps1-az3 | 141 | 87% | 8.2 | 9 (10-20 00:15Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 116 | 98% | 8.9 | 9 (10-20 00:15Z) |
| us-east-2 use2-az2 | 159 | 99% | 8.9 | 9 (10-20 00:15Z) |
| us-east-2 use2-az3 | 153 | 95% | 8.6 | 9 (10-20 00:15Z) |
| us-west-2 usw2-az1 | 79 | 97% | 8.8 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az2 | 74 | 96% | 8.7 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709000 | 2026-10-20T00:15:57Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-20T00:15:57Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764200 | 2026-10-20T00:15:57Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947100 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584600 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580900 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566200 | 2026-10-20T00:15:57Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-10-20T00:15:57Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.558500 | 2026-10-20T00:15:57Z |
| ap-south-1 | ap-south-1a | Windows | 0.390700 | 2026-10-20T00:15:57Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.740800 | 2026-10-20T00:15:57Z |
| ap-south-1 | ap-south-1b | Windows | 0.371900 | 2026-10-20T00:15:57Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.697600 | 2026-10-20T00:15:57Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508500 | 2026-10-20T00:15:57Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.663100 | 2026-10-20T00:15:57Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550500 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.446800 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.525400 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.517000 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.449100 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.500800 | 2026-10-20T00:15:57Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.552700 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2a | Windows | 0.643000 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545600 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2b | Windows | 0.639400 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.542200 | 2026-10-20T00:15:57Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.534500 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2a | Windows | 0.316000 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526500 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2b | Windows | 0.328000 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.521200 | 2026-10-20T00:15:57Z |
| us-west-2 | us-west-2c | Windows | 0.315300 | 2026-10-20T00:15:57Z |
