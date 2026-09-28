# Spot placement score log

Generated 2026-09-28 23:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 204 | 20% | 3.3 | 9 (09-28 23:21Z) |
| ap-northeast-1 | 204 | 7% | 2.3 | 1 (09-28 23:21Z) |
| ap-northeast-2 | 204 | 25% | 4.5 | 9 (09-28 23:21Z) |
| ap-south-1 | 204 | 3% | 2.0 | 1 (09-28 23:21Z) |
| ap-southeast-2 | 204 | 0% | 1.0 | 1 (09-28 23:21Z) |
| ap-southeast-3 | 204 | 19% | 3.5 | 9 (09-28 23:21Z) |
| us-east-1 | 204 | 6% | 2.4 | 1 (09-28 23:21Z) |
| us-east-2 | 204 | 16% | 2.9 | 1 (09-28 23:21Z) |
| us-west-2 | 204 | 11% | 2.4 | 1 (09-28 23:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999119199919999998899113991114999999999999999
ap-northeast-1   222211343221555316644442111111111111898994558941
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111121111311411115999279134411111111121111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   899951989158999928699989111111115368786755668889
us-east-1        232113122332239233222299991199999199911111112111
us-east-2        911219928999999999999999999999999999911111111111
us-west-2        122221112199519299129999999999999999111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 2 | 2 | 5 | 4 | 3 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 4 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 66 | 0% | 1.5 | 2 (09-28 22:21Z) |
| ap-east-1 ape1-az2 | 136 | 29% | 4.4 | 9 (09-28 23:21Z) |
| ap-northeast-1 apne1-az1 | 28 | 0% | 1.2 | 1 (09-28 23:21Z) |
| ap-northeast-1 apne1-az4 | 91 | 8% | 2.6 | 3 (09-28 22:21Z) |
| ap-northeast-2 apne2-az1 | 182 | 25% | 4.4 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az3 | 186 | 27% | 4.6 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az4 | 201 | 25% | 4.5 | 9 (09-28 23:21Z) |
| ap-south-1 aps1-az1 | 61 | 2% | 1.8 | 1 (09-28 16:27Z) |
| ap-south-1 aps1-az3 | 88 | 3% | 2.7 | 1 (09-28 17:21Z) |
| ap-southeast-2 apse2-az1 | 28 | 0% | 1.1 | 1 (09-28 23:21Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 41 | 0% | 1.0 | 1 (09-28 20:22Z) |
| ap-southeast-3 apse3-az3 | 155 | 23% | 4.0 | 9 (09-28 23:21Z) |
| us-east-1 use1-az1 | 23 | 0% | 1.3 | 1 (09-28 23:21Z) |
| us-east-1 use1-az2 | 60 | 3% | 1.6 | 1 (09-28 21:20Z) |
| us-east-1 use1-az4 | 56 | 23% | 3.3 | 1 (09-28 23:21Z) |
| us-east-1 use1-az5 | 62 | 18% | 2.8 | 1 (09-28 20:22Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 71 | 23% | 3.3 | 1 (09-28 23:21Z) |
| us-east-2 use2-az2 | 102 | 27% | 3.8 | 1 (09-28 21:20Z) |
| us-east-2 use2-az3 | 120 | 26% | 3.9 | 1 (09-28 19:19Z) |
| us-west-2 usw2-az1 | 71 | 28% | 3.9 | 1 (09-28 21:20Z) |
| us-west-2 usw2-az2 | 42 | 26% | 3.7 | 1 (09-28 17:21Z) |
| us-west-2 usw2-az3 | 98 | 18% | 3.1 | 9 (09-28 11:22Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 204 | 25% | 4.5 | 9 (09-28 23:21Z) |
| ap-northeast-1 | 204 | 78% | 7.5 | 9 (09-28 23:21Z) |
| ap-northeast-2 | 204 | 100% | 9.0 | 9 (09-28 23:21Z) |
| ap-south-1 | 204 | 56% | 6.2 | 9 (09-28 23:21Z) |
| ap-southeast-2 | 204 | 17% | 3.3 | 2 (09-28 23:21Z) |
| ap-southeast-3 | 204 | 19% | 3.5 | 9 (09-28 23:21Z) |
| us-east-1 | 204 | 75% | 6.9 | 3 (09-28 23:21Z) |
| us-east-2 | 204 | 75% | 7.3 | 3 (09-28 23:21Z) |
| us-west-2 | 204 | 59% | 6.1 | 2 (09-28 23:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   499921999999999999999999111111111389999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       289998999999999999999999999999932112299999999999
ap-southeast-2   299222999999999999999922222222222242794999932212
ap-southeast-3   899951989158999928699989111111115368786755668889
us-east-1        954598347999999999999999999999999999922123445433
us-east-2        923489999999999999999999999999999999992233332233
us-west-2        554459934399999999999999999999999999999944343322
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 7 | 5 | 6 | 6 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 8 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 96 | 44% | 5.6 | 9 (09-28 23:21Z) |
| ap-east-1 ape1-az2 | 71 | 42% | 5.5 | 9 (09-28 20:22Z) |
| ap-east-1 ape1-az3 | 70 | 37% | 5.2 | 9 (09-28 23:21Z) |
| ap-northeast-1 apne1-az1 | 99 | 92% | 8.5 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az2 | 39 | 33% | 5.0 | 9 (09-28 23:21Z) |
| ap-northeast-1 apne1-az4 | 126 | 100% | 9.0 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az1 | 159 | 100% | 9.0 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az2 | 42 | 69% | 7.1 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az3 | 181 | 100% | 9.0 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az4 | 89 | 47% | 5.8 | 9 (09-28 23:21Z) |
| ap-south-1 aps1-az1 | 58 | 62% | 6.7 | 9 (09-28 18:29Z) |
| ap-south-1 aps1-az2 | 67 | 46% | 5.8 | 9 (09-28 23:21Z) |
| ap-south-1 aps1-az3 | 84 | 79% | 7.7 | 9 (09-28 23:21Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.729400 | 2026-09-28T23:21:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.885800 | 2026-09-28T23:21:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.812400 | 2026-09-28T23:21:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.996900 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567600 | 2026-09-28T23:21:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T23:21:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.581500 | 2026-09-28T23:21:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.345300 | 2026-09-28T23:21:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.598700 | 2026-09-28T23:21:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.338100 | 2026-09-28T23:21:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.709900 | 2026-09-28T23:21:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-09-28T23:21:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.649300 | 2026-09-28T23:21:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.627500 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1a | Windows | 0.309600 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.465500 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.442400 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.381100 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.430400 | 2026-09-28T23:21:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529000 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2b | Windows | 0.640900 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-09-28T23:21:00Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.512800 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491700 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.488200 | 2026-09-28T23:21:00Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-28T23:21:00Z |
