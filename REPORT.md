# Spot placement score log

Generated 2026-09-28 20:22 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 201 | 18% | 3.2 | 9 (09-28 20:22Z) |
| ap-northeast-1 | 201 | 6% | 2.3 | 8 (09-28 20:22Z) |
| ap-northeast-2 | 201 | 24% | 4.4 | 9 (09-28 20:22Z) |
| ap-south-1 | 201 | 3% | 2.0 | 1 (09-28 20:22Z) |
| ap-southeast-2 | 201 | 0% | 1.0 | 1 (09-28 20:22Z) |
| ap-southeast-3 | 201 | 18% | 3.4 | 8 (09-28 20:22Z) |
| us-east-1 | 201 | 6% | 2.4 | 2 (09-28 20:22Z) |
| us-east-2 | 201 | 16% | 2.9 | 1 (09-28 20:22Z) |
| us-west-2 | 201 | 11% | 2.4 | 1 (09-28 20:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999119199919999998899113991114999999999999
ap-northeast-1   322222211343221555316644442111111111111898994558
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111121111311411115999279134411111111121111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   996899951989158999928699989111111115368786755668
us-east-1        221232113122332239233222299991199999199911111112
us-east-2        192911219928999999999999999999999999999911111111
us-west-2        221122221112199519299129999999999999999111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 2 | 2 | 5 | 4 | 3 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 3 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 4 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 64 | 0% | 1.5 | 1 (09-28 20:22Z) |
| ap-east-1 ape1-az2 | 133 | 28% | 4.3 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az1 | 26 | 0% | 1.3 | 1 (09-28 15:24Z) |
| ap-northeast-1 apne1-az4 | 89 | 7% | 2.6 | 8 (09-28 20:22Z) |
| ap-northeast-2 apne2-az1 | 179 | 23% | 4.3 | 9 (09-28 20:22Z) |
| ap-northeast-2 apne2-az3 | 183 | 26% | 4.5 | 9 (09-28 20:22Z) |
| ap-northeast-2 apne2-az4 | 198 | 24% | 4.4 | 9 (09-28 20:22Z) |
| ap-south-1 aps1-az1 | 61 | 2% | 1.8 | 1 (09-28 16:27Z) |
| ap-south-1 aps1-az3 | 88 | 3% | 2.7 | 1 (09-28 17:21Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 41 | 0% | 1.0 | 1 (09-28 20:22Z) |
| ap-southeast-3 apse3-az3 | 152 | 22% | 3.9 | 8 (09-28 20:22Z) |
| us-east-1 use1-az1 | 21 | 0% | 1.3 | 1 (09-28 15:24Z) |
| us-east-1 use1-az2 | 59 | 3% | 1.6 | 9 (09-28 04:30Z) |
| us-east-1 use1-az4 | 54 | 24% | 3.4 | 1 (09-28 16:27Z) |
| us-east-1 use1-az5 | 62 | 18% | 2.8 | 1 (09-28 20:22Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 70 | 23% | 3.3 | 1 (09-28 16:27Z) |
| us-east-2 use2-az2 | 101 | 28% | 3.8 | 1 (09-28 20:22Z) |
| us-east-2 use2-az3 | 120 | 26% | 3.9 | 1 (09-28 19:19Z) |
| us-west-2 usw2-az1 | 70 | 29% | 3.9 | 9 (09-28 09:35Z) |
| us-west-2 usw2-az2 | 42 | 26% | 3.7 | 1 (09-28 17:21Z) |
| us-west-2 usw2-az3 | 98 | 18% | 3.1 | 9 (09-28 11:22Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 201 | 24% | 4.4 | 9 (09-28 20:22Z) |
| ap-northeast-1 | 201 | 78% | 7.4 | 9 (09-28 20:22Z) |
| ap-northeast-2 | 201 | 100% | 9.0 | 9 (09-28 20:22Z) |
| ap-south-1 | 201 | 55% | 6.1 | 9 (09-28 20:22Z) |
| ap-southeast-2 | 201 | 17% | 3.3 | 2 (09-28 20:22Z) |
| ap-southeast-3 | 201 | 18% | 3.4 | 8 (09-28 20:22Z) |
| us-east-1 | 201 | 76% | 7.0 | 5 (09-28 20:22Z) |
| us-east-2 | 201 | 77% | 7.4 | 2 (09-28 20:22Z) |
| us-west-2 | 201 | 60% | 6.2 | 3 (09-28 20:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   993499921999999999999999999111111111389999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999289998999999999999999999999999932112299999999
ap-southeast-2   512299222999999999999999922222222222242794999932
ap-southeast-3   996899951989158999928699989111111115368786755668
us-east-1        669954598347999999999999999999999999999922123445
us-east-2        499923489999999999999999999999999999999992233332
us-west-2        559554459934399999999999999999999999999999944343
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 7 | 5 | 6 | 6 | 8 | 7 | 8 | 7 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 3 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 93 | 42% | 5.5 | 9 (09-28 18:29Z) |
| ap-east-1 ape1-az2 | 71 | 42% | 5.5 | 9 (09-28 20:22Z) |
| ap-east-1 ape1-az3 | 67 | 34% | 5.1 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az1 | 99 | 92% | 8.5 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az2 | 36 | 28% | 4.7 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az4 | 123 | 100% | 9.0 | 9 (09-28 20:22Z) |
| ap-northeast-2 apne2-az1 | 156 | 100% | 9.0 | 9 (09-28 18:29Z) |
| ap-northeast-2 apne2-az2 | 39 | 67% | 7.0 | 9 (09-28 20:22Z) |
| ap-northeast-2 apne2-az3 | 178 | 100% | 9.0 | 9 (09-28 20:22Z) |
| ap-northeast-2 apne2-az4 | 86 | 45% | 5.7 | 9 (09-28 20:22Z) |
| ap-south-1 aps1-az1 | 58 | 62% | 6.7 | 9 (09-28 18:29Z) |
| ap-south-1 aps1-az2 | 64 | 44% | 5.6 | 9 (09-28 20:22Z) |
| ap-south-1 aps1-az3 | 81 | 78% | 7.7 | 9 (09-28 20:22Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 26 | 54% | 6.2 | 9 (09-28 17:21Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 84 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-east-1 use1-az5 | 46 | 98% | 8.8 | 9 (09-28 08:38Z) |
| us-east-1 use1-az6 | 73 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 74 | 99% | 8.9 | 9 (09-28 11:22Z) |
| us-east-2 use2-az2 | 108 | 98% | 8.9 | 9 (09-28 13:26Z) |
| us-east-2 use2-az3 | 99 | 92% | 8.5 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az1 | 62 | 98% | 8.9 | 9 (09-28 13:26Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 71 | 99% | 8.9 | 9 (09-28 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730400 | 2026-09-28T20:22:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.888900 | 2026-09-28T20:22:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.812400 | 2026-09-28T20:22:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.002900 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567700 | 2026-09-28T20:22:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T20:22:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.573700 | 2026-09-28T20:22:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.345300 | 2026-09-28T20:22:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.586600 | 2026-09-28T20:22:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.336000 | 2026-09-28T20:22:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.708900 | 2026-09-28T20:22:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497900 | 2026-09-28T20:22:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655400 | 2026-09-28T20:22:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.627500 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1a | Windows | 0.309600 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.473400 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.435800 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.384000 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.430400 | 2026-09-28T20:22:14Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527800 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514600 | 2026-09-28T20:22:14Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.512800 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491700 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.488200 | 2026-09-28T20:22:14Z |
| us-west-2 | us-west-2c | Windows | 0.331600 | 2026-09-28T20:22:14Z |
