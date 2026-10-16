# Spot placement score log

Generated 2026-10-16 12:20 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 320 | 37% | 4.4 | 9 (10-16 12:19Z) |
| ap-northeast-1 | 320 | 15% | 2.7 | 1 (10-16 12:19Z) |
| ap-northeast-2 | 320 | 51% | 6.0 | 9 (10-16 12:19Z) |
| ap-south-1 | 320 | 2% | 1.8 | 2 (10-16 12:19Z) |
| ap-southeast-2 | 320 | 0% | 1.0 | 1 (10-16 12:19Z) |
| ap-southeast-3 | 320 | 22% | 3.2 | 4 (10-16 12:19Z) |
| us-east-1 | 320 | 9% | 2.5 | 2 (10-16 12:19Z) |
| us-east-2 | 320 | 28% | 3.6 | 9 (10-16 12:19Z) |
| us-west-2 | 320 | 11% | 2.3 | 1 (10-16 12:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111118229299999999999999999999999
ap-northeast-1   191111511971111119111222211922121211142211421111
ap-northeast-2   149999999999999999919999999999999999999999999999
ap-south-1       222222222221112211111122222222221111122222221112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111113881111138911999793951511221111311518214
us-east-1        921111211112221132323331922332221133332321323122
us-east-2        911181111111111111111811999999111129911129111999
us-west-2        112112121111111111119999111111111111111111221111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 8 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 113 | 8% | 1.8 | 1 (10-16 12:19Z) |
| ap-east-1 ape1-az2 | 225 | 52% | 5.8 | 9 (10-16 12:19Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 151 | 25% | 3.5 | 1 (10-15 22:10Z) |
| ap-northeast-2 apne2-az1 | 280 | 49% | 5.8 | 9 (10-16 12:19Z) |
| ap-northeast-2 apne2-az3 | 292 | 52% | 6.0 | 9 (10-16 12:19Z) |
| ap-northeast-2 apne2-az4 | 317 | 52% | 6.1 | 9 (10-16 12:19Z) |
| ap-south-1 aps1-az1 | 83 | 1% | 1.6 | 1 (10-14 18:31Z) |
| ap-south-1 aps1-az3 | 110 | 3% | 2.4 | 1 (10-15 22:10Z) |
| ap-southeast-2 apse2-az1 | 51 | 0% | 1.1 | 1 (10-15 18:13Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 66 | 0% | 1.0 | 1 (10-16 12:19Z) |
| ap-southeast-3 apse3-az3 | 214 | 31% | 4.2 | 4 (10-16 12:19Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 88 | 3% | 1.5 | 1 (10-16 12:19Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 100 | 24% | 3.2 | 1 (10-15 22:10Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 127 | 39% | 4.5 | 9 (10-16 07:03Z) |
| us-east-2 use2-az2 | 163 | 45% | 4.9 | 1 (10-16 12:19Z) |
| us-east-2 use2-az3 | 194 | 43% | 4.9 | 7 (10-16 12:19Z) |
| us-west-2 usw2-az1 | 112 | 28% | 3.6 | 1 (10-16 01:13Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 320 | 52% | 6.1 | 9 (10-16 12:19Z) |
| ap-northeast-1 | 320 | 73% | 7.1 | 9 (10-16 12:19Z) |
| ap-northeast-2 | 320 | 100% | 9.0 | 9 (10-16 12:19Z) |
| ap-south-1 | 320 | 60% | 6.3 | 2 (10-16 12:19Z) |
| ap-southeast-2 | 320 | 17% | 3.1 | 1 (10-16 12:19Z) |
| ap-southeast-3 | 320 | 22% | 3.2 | 4 (10-16 12:19Z) |
| us-east-1 | 320 | 71% | 6.5 | 3 (10-16 12:19Z) |
| us-east-2 | 320 | 71% | 6.9 | 9 (10-16 12:19Z) |
| us-west-2 | 320 | 52% | 5.7 | 4 (10-16 12:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   199239913991199119999999999999923992399921999119
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       229929992999199914999999999992991999122992299912
ap-southeast-2   291111111911111111891999999111111111118111111111
ap-southeast-3   111111113881111138911999793951511221111311518214
us-east-1        955453343336635464569982999999454266643555546793
us-east-2        923993321212111212119922999999119129911229111999
us-west-2        943235441323331332339999993592994424953433554334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 194 | 72% | 7.3 | 9 (10-16 12:19Z) |
| ap-east-1 ape1-az2 | 163 | 75% | 7.5 | 9 (10-16 12:19Z) |
| ap-east-1 ape1-az3 | 165 | 73% | 7.4 | 9 (10-16 12:19Z) |
| ap-northeast-1 apne1-az1 | 151 | 93% | 8.5 | 9 (10-15 22:10Z) |
| ap-northeast-1 apne1-az2 | 91 | 70% | 7.2 | 9 (10-16 12:19Z) |
| ap-northeast-1 apne1-az4 | 181 | 98% | 8.9 | 9 (10-16 12:19Z) |
| ap-northeast-2 apne2-az1 | 252 | 100% | 9.0 | 9 (10-16 12:19Z) |
| ap-northeast-2 apne2-az2 | 69 | 78% | 7.6 | 9 (10-15 22:10Z) |
| ap-northeast-2 apne2-az3 | 275 | 100% | 9.0 | 9 (10-16 12:19Z) |
| ap-northeast-2 apne2-az4 | 189 | 75% | 7.5 | 9 (10-16 12:19Z) |
| ap-south-1 aps1-az1 | 111 | 80% | 7.8 | 9 (10-16 01:13Z) |
| ap-south-1 aps1-az2 | 114 | 68% | 7.1 | 9 (10-16 01:13Z) |
| ap-south-1 aps1-az3 | 130 | 85% | 8.1 | 9 (10-16 01:13Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 63 | 30% | 4.7 | 4 (10-16 12:19Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 81 | 100% | 9.0 | 9 (10-16 07:03Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 84 | 95% | 8.7 | 9 (10-16 07:03Z) |
| us-east-2 use2-az1 | 107 | 98% | 8.9 | 9 (10-15 07:20Z) |
| us-east-2 use2-az2 | 154 | 99% | 8.9 | 9 (10-16 07:03Z) |
| us-east-2 use2-az3 | 144 | 94% | 8.6 | 7 (10-16 12:19Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711400 | 2026-10-16T12:19:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-16T12:19:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.755600 | 2026-10-16T12:19:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.936600 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588200 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.583800 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571200 | 2026-10-16T12:19:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741500 | 2026-10-16T12:19:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.553500 | 2026-10-16T12:19:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.376700 | 2026-10-16T12:19:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.695200 | 2026-10-16T12:19:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.328500 | 2026-10-16T12:19:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.720400 | 2026-10-16T12:19:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.524800 | 2026-10-16T12:19:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.550100 | 2026-10-16T12:19:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.588900 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.448500 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.507700 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.467800 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.416600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.454600 | 2026-10-16T12:19:58Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545500 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2a | Windows | 0.643600 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.535800 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2b | Windows | 0.640200 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.532400 | 2026-10-16T12:19:58Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.527200 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2a | Windows | 0.314900 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499500 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2b | Windows | 0.330200 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.496800 | 2026-10-16T12:19:58Z |
| us-west-2 | us-west-2c | Windows | 0.314500 | 2026-10-16T12:19:58Z |
