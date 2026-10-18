# Spot placement score log

Generated 2026-10-18 20:34 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 335 | 40% | 4.6 | 9 (10-18 20:34Z) |
| ap-northeast-1 | 335 | 15% | 2.8 | 2 (10-18 20:34Z) |
| ap-northeast-2 | 335 | 53% | 6.2 | 9 (10-18 20:34Z) |
| ap-south-1 | 335 | 2% | 1.8 | 2 (10-18 20:34Z) |
| ap-southeast-2 | 335 | 1% | 1.1 | 1 (10-18 20:34Z) |
| ap-southeast-3 | 335 | 24% | 3.4 | 8 (10-18 20:34Z) |
| us-east-1 | 335 | 10% | 2.6 | 9 (10-18 20:34Z) |
| us-east-2 | 335 | 29% | 3.7 | 9 (10-18 20:34Z) |
| us-west-2 | 335 | 11% | 2.3 | 9 (10-18 20:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111118229299999999999999999999999999999999999999
ap-northeast-1   119111222211922121211142211421111322129324165912
ap-northeast-2   999919999999999999999999999999999999999999999999
ap-south-1       211111122222222221111122222221112222222222222222
ap-southeast-2   111111111111111111111111111111111111191191111111
ap-southeast-3   138911999793951511221111311518214387518679924748
us-east-1        132323331922332221133332321323122222333221923999
us-east-2        111111811999999111129911129111999111161999999199
us-west-2        111119999111111111111111111221111222112121219119
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 240 | 55% | 6.0 | 9 (10-18 20:34Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 157 | 25% | 3.6 | 8 (10-18 14:30Z) |
| ap-northeast-2 apne2-az1 | 293 | 50% | 5.8 | 6 (10-18 18:01Z) |
| ap-northeast-2 apne2-az3 | 307 | 54% | 6.1 | 9 (10-18 20:34Z) |
| ap-northeast-2 apne2-az4 | 332 | 54% | 6.2 | 9 (10-18 20:34Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 226 | 33% | 4.3 | 7 (10-18 14:30Z) |
| us-east-1 use1-az1 | 64 | 0% | 1.1 | 1 (10-18 05:47Z) |
| us-east-1 use1-az2 | 93 | 3% | 1.5 | 2 (10-18 14:30Z) |
| us-east-1 use1-az4 | 102 | 29% | 3.6 | 9 (10-18 20:34Z) |
| us-east-1 use1-az5 | 107 | 26% | 3.3 | 9 (10-18 20:34Z) |
| us-east-1 use1-az6 | 77 | 23% | 3.1 | 9 (10-18 20:34Z) |
| us-east-2 use2-az1 | 133 | 41% | 4.6 | 9 (10-18 20:34Z) |
| us-east-2 use2-az2 | 174 | 46% | 5.0 | 9 (10-18 20:34Z) |
| us-east-2 use2-az3 | 205 | 44% | 5.0 | 9 (10-18 20:34Z) |
| us-west-2 usw2-az1 | 119 | 28% | 3.6 | 9 (10-18 20:34Z) |
| us-west-2 usw2-az2 | 71 | 25% | 3.4 | 9 (10-18 10:55Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 335 | 54% | 6.3 | 9 (10-18 20:34Z) |
| ap-northeast-1 | 335 | 74% | 7.2 | 9 (10-18 20:34Z) |
| ap-northeast-2 | 335 | 100% | 9.0 | 9 (10-18 20:34Z) |
| ap-south-1 | 335 | 62% | 6.4 | 9 (10-18 20:34Z) |
| ap-southeast-2 | 335 | 20% | 3.3 | 9 (10-18 20:34Z) |
| ap-southeast-3 | 335 | 24% | 3.4 | 8 (10-18 20:34Z) |
| us-east-1 | 335 | 71% | 6.6 | 9 (10-18 20:34Z) |
| us-east-2 | 335 | 71% | 6.9 | 9 (10-18 20:34Z) |
| us-west-2 | 335 | 53% | 5.7 | 9 (10-18 20:34Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   119999999999999923992399921999119999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       914999999999992991999122992299912999999999999999
ap-southeast-2   111891999999111111111118111111111111999999999999
ap-southeast-3   138911999793951511221111311518214387518679924748
us-east-1        464569982999999454266643555546793446599999999999
us-east-2        212119922999999119129911229111999311399999999999
us-west-2        332339999993592994424953433554334454439999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 204 | 74% | 7.4 | 9 (10-18 20:34Z) |
| ap-east-1 ape1-az2 | 170 | 76% | 7.6 | 9 (10-18 18:01Z) |
| ap-east-1 ape1-az3 | 171 | 74% | 7.5 | 9 (10-18 20:34Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 98 | 72% | 7.3 | 9 (10-18 18:01Z) |
| ap-northeast-1 apne1-az4 | 191 | 98% | 8.9 | 9 (10-18 20:34Z) |
| ap-northeast-2 apne2-az1 | 261 | 100% | 9.0 | 9 (10-18 18:01Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 288 | 100% | 9.0 | 9 (10-18 20:34Z) |
| ap-northeast-2 apne2-az4 | 199 | 76% | 7.6 | 9 (10-18 20:34Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 120 | 70% | 7.2 | 9 (10-18 10:55Z) |
| ap-south-1 aps1-az3 | 137 | 86% | 8.2 | 9 (10-18 10:55Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 43 | 70% | 7.1 | 9 (10-18 14:30Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 84 | 100% | 9.0 | 9 (10-18 20:34Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 69 | 97% | 8.8 | 9 (10-18 18:01Z) |
| us-east-1 use1-az6 | 90 | 96% | 8.7 | 9 (10-18 20:34Z) |
| us-east-2 use2-az1 | 112 | 98% | 8.9 | 9 (10-18 20:34Z) |
| us-east-2 use2-az2 | 158 | 99% | 8.9 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 149 | 95% | 8.6 | 9 (10-18 20:34Z) |
| us-west-2 usw2-az1 | 78 | 97% | 8.8 | 9 (10-18 18:01Z) |
| us-west-2 usw2-az2 | 72 | 96% | 8.7 | 9 (10-18 20:34Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709100 | 2026-10-18T20:34:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-18T20:34:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.765200 | 2026-10-18T20:34:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.946200 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585600 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581700 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567600 | 2026-10-18T20:34:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741200 | 2026-10-18T20:34:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.549600 | 2026-10-18T20:34:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.385500 | 2026-10-18T20:34:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.712200 | 2026-10-18T20:34:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.353700 | 2026-10-18T20:34:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.708300 | 2026-10-18T20:34:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.519400 | 2026-10-18T20:34:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.638300 | 2026-10-18T20:34:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.567000 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.429800 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.531700 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.506700 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.433600 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.487800 | 2026-10-18T20:34:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550000 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2a | Windows | 0.643400 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.542500 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2b | Windows | 0.639300 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.539600 | 2026-10-18T20:34:00Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.524800 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2a | Windows | 0.314700 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.500500 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2b | Windows | 0.331000 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494000 | 2026-10-18T20:34:00Z |
| us-west-2 | us-west-2c | Windows | 0.314700 | 2026-10-18T20:34:00Z |
