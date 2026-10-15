# Spot placement score log

Generated 2026-10-15 22:10 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 317 | 36% | 4.4 | 9 (10-15 22:10Z) |
| ap-northeast-1 | 317 | 15% | 2.7 | 1 (10-15 22:10Z) |
| ap-northeast-2 | 317 | 51% | 6.0 | 9 (10-15 22:10Z) |
| ap-south-1 | 317 | 2% | 1.8 | 1 (10-15 22:10Z) |
| ap-southeast-2 | 317 | 0% | 1.0 | 1 (10-15 22:10Z) |
| ap-southeast-3 | 317 | 22% | 3.3 | 8 (10-15 22:10Z) |
| us-east-1 | 317 | 9% | 2.5 | 3 (10-15 22:10Z) |
| us-east-2 | 317 | 27% | 3.5 | 1 (10-15 22:10Z) |
| us-west-2 | 317 | 11% | 2.3 | 1 (10-15 22:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        211111111111111111111118229299999999999999999999
ap-northeast-1   991191111511971111119111222211922121211142211421
ap-northeast-2   999149999999999999999919999999999999999999999999
ap-south-1       222222222222221112211111122222222221111122222221
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111113881111138911999793951511221111311518
us-east-1        999921111211112221132323331922332221133332321323
us-east-2        999911181111111111111111811999999111129911129111
us-west-2        199112112121111111111119999111111111111111111221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 110 | 8% | 1.8 | 1 (10-15 13:20Z) |
| ap-east-1 ape1-az2 | 222 | 51% | 5.7 | 9 (10-15 22:10Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 151 | 25% | 3.5 | 1 (10-15 22:10Z) |
| ap-northeast-2 apne2-az1 | 277 | 48% | 5.8 | 9 (10-15 22:10Z) |
| ap-northeast-2 apne2-az3 | 289 | 52% | 6.0 | 9 (10-15 22:10Z) |
| ap-northeast-2 apne2-az4 | 314 | 51% | 6.1 | 9 (10-15 22:10Z) |
| ap-south-1 aps1-az1 | 83 | 1% | 1.6 | 1 (10-14 18:31Z) |
| ap-south-1 aps1-az3 | 110 | 3% | 2.4 | 1 (10-15 22:10Z) |
| ap-southeast-2 apse2-az1 | 51 | 0% | 1.1 | 1 (10-15 18:13Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 63 | 0% | 1.0 | 1 (10-15 18:13Z) |
| ap-southeast-3 apse3-az3 | 212 | 31% | 4.2 | 8 (10-15 22:10Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 85 | 4% | 1.5 | 1 (10-15 13:20Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 100 | 24% | 3.2 | 1 (10-15 22:10Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 126 | 39% | 4.4 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 160 | 44% | 4.9 | 1 (10-15 13:20Z) |
| us-east-2 use2-az3 | 192 | 42% | 4.9 | 1 (10-15 22:10Z) |
| us-west-2 usw2-az1 | 111 | 28% | 3.6 | 1 (10-15 22:10Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 317 | 52% | 6.1 | 9 (10-15 22:10Z) |
| ap-northeast-1 | 317 | 73% | 7.1 | 9 (10-15 22:10Z) |
| ap-northeast-2 | 317 | 100% | 9.0 | 9 (10-15 22:10Z) |
| ap-south-1 | 317 | 61% | 6.3 | 9 (10-15 22:10Z) |
| ap-southeast-2 | 317 | 17% | 3.1 | 1 (10-15 22:10Z) |
| ap-southeast-3 | 317 | 22% | 3.3 | 8 (10-15 22:10Z) |
| us-east-1 | 317 | 71% | 6.5 | 6 (10-15 22:10Z) |
| us-east-2 | 317 | 70% | 6.9 | 1 (10-15 22:10Z) |
| us-west-2 | 317 | 52% | 5.7 | 4 (10-15 22:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999199239913991199119999999999999923992399921999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999229929992999199914999999999992991999122992299
ap-southeast-2   992291111111911111111891999999111111111118111111
ap-southeast-3   111111111113881111138911999793951511221111311518
us-east-1        999955453343336635464569982999999454266643555546
us-east-2        999923993321212111212119922999999119129911229111
us-west-2        999943235441323331332339999993592994424953433554
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 192 | 72% | 7.3 | 9 (10-15 22:10Z) |
| ap-east-1 ape1-az2 | 160 | 74% | 7.5 | 9 (10-15 22:10Z) |
| ap-east-1 ape1-az3 | 162 | 73% | 7.4 | 9 (10-15 22:10Z) |
| ap-northeast-1 apne1-az1 | 151 | 93% | 8.5 | 9 (10-15 22:10Z) |
| ap-northeast-1 apne1-az2 | 90 | 70% | 7.2 | 9 (10-15 22:10Z) |
| ap-northeast-1 apne1-az4 | 180 | 98% | 8.9 | 9 (10-15 18:13Z) |
| ap-northeast-2 apne2-az1 | 250 | 100% | 9.0 | 9 (10-15 18:13Z) |
| ap-northeast-2 apne2-az2 | 69 | 78% | 7.6 | 9 (10-15 22:10Z) |
| ap-northeast-2 apne2-az3 | 272 | 100% | 9.0 | 9 (10-15 22:10Z) |
| ap-northeast-2 apne2-az4 | 186 | 75% | 7.5 | 9 (10-15 22:10Z) |
| ap-south-1 aps1-az1 | 110 | 80% | 7.8 | 9 (10-15 22:10Z) |
| ap-south-1 aps1-az2 | 113 | 68% | 7.1 | 9 (10-15 22:10Z) |
| ap-south-1 aps1-az3 | 129 | 85% | 8.1 | 9 (10-15 18:13Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 62 | 31% | 4.7 | 5 (10-15 13:20Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 102 | 94% | 8.6 | 2 (10-15 07:20Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 107 | 98% | 8.9 | 9 (10-15 07:20Z) |
| us-east-2 use2-az2 | 152 | 99% | 8.9 | 9 (10-15 07:20Z) |
| us-east-2 use2-az3 | 141 | 94% | 8.6 | 9 (10-15 07:20Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.714000 | 2026-10-15T22:10:28Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-15T22:10:28Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.762700 | 2026-10-15T22:10:28Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.945700 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588300 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585200 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571800 | 2026-10-15T22:10:28Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741600 | 2026-10-15T22:10:28Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.556300 | 2026-10-15T22:10:28Z |
| ap-south-1 | ap-south-1a | Windows | 0.380300 | 2026-10-15T22:10:28Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.702400 | 2026-10-15T22:10:28Z |
| ap-south-1 | ap-south-1b | Windows | 0.327300 | 2026-10-15T22:10:28Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.722500 | 2026-10-15T22:10:28Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.528300 | 2026-10-15T22:10:28Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.533000 | 2026-10-15T22:10:28Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.598400 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.468100 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.506100 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.453900 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.414000 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.451900 | 2026-10-15T22:10:28Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545000 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2a | Windows | 0.643800 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.535300 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.530400 | 2026-10-15T22:10:28Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.530000 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2a | Windows | 0.315400 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499500 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2b | Windows | 0.330300 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.497600 | 2026-10-15T22:10:28Z |
| us-west-2 | us-west-2c | Windows | 0.315100 | 2026-10-15T22:10:28Z |
