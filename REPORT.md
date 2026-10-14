# Spot placement score log

Generated 2026-10-14 13:38 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 310 | 35% | 4.3 | 9 (10-14 13:38Z) |
| ap-northeast-1 | 310 | 15% | 2.8 | 4 (10-14 13:38Z) |
| ap-northeast-2 | 310 | 50% | 6.0 | 9 (10-14 13:38Z) |
| ap-south-1 | 310 | 2% | 1.8 | 2 (10-14 13:38Z) |
| ap-southeast-2 | 310 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 | 310 | 22% | 3.3 | 1 (10-14 13:38Z) |
| us-east-1 | 310 | 9% | 2.6 | 3 (10-14 13:38Z) |
| us-east-2 | 310 | 27% | 3.6 | 1 (10-14 13:38Z) |
| us-west-2 | 310 | 12% | 2.4 | 1 (10-14 13:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199998121111111111111111111111822929999999999999
ap-northeast-1   999999999119111151197111111911122221192212121114
ap-northeast-2   999999999914999999999999999991999999999999999999
ap-south-1       111111122222222222222111221111112222222222111112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111111111388111113891199979395151122111
us-east-1        311991999992111121111222113232333192233222113333
us-east-2        999999999991118111111111111111181199999911112991
us-west-2        999999919911211212111111111111999911111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 5 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 107 | 8% | 1.8 | 5 (10-13 17:32Z) |
| ap-east-1 ape1-az2 | 215 | 50% | 5.6 | 9 (10-14 13:38Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 147 | 26% | 3.6 | 1 (10-14 01:49Z) |
| ap-northeast-2 apne2-az1 | 270 | 47% | 5.7 | 9 (10-14 13:38Z) |
| ap-northeast-2 apne2-az3 | 282 | 51% | 5.9 | 9 (10-14 13:38Z) |
| ap-northeast-2 apne2-az4 | 307 | 50% | 6.0 | 9 (10-14 13:38Z) |
| ap-south-1 aps1-az1 | 82 | 1% | 1.6 | 1 (10-14 13:38Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 49 | 0% | 1.1 | 1 (10-14 13:38Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 58 | 0% | 1.0 | 1 (10-12 18:57Z) |
| ap-southeast-3 apse3-az3 | 209 | 31% | 4.2 | 2 (10-13 22:38Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 81 | 4% | 1.6 | 1 (10-13 22:38Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 97 | 25% | 3.2 | 1 (10-14 01:49Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 126 | 39% | 4.4 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 156 | 45% | 5.0 | 9 (10-14 01:49Z) |
| us-east-2 use2-az3 | 187 | 43% | 4.9 | 9 (10-14 07:30Z) |
| us-west-2 usw2-az1 | 105 | 30% | 3.8 | 1 (10-14 01:49Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 310 | 51% | 6.0 | 9 (10-14 13:38Z) |
| ap-northeast-1 | 310 | 73% | 7.1 | 9 (10-14 13:38Z) |
| ap-northeast-2 | 310 | 100% | 9.0 | 9 (10-14 13:38Z) |
| ap-south-1 | 310 | 61% | 6.3 | 2 (10-14 13:38Z) |
| ap-southeast-2 | 310 | 17% | 3.2 | 1 (10-14 13:38Z) |
| ap-southeast-3 | 310 | 22% | 3.3 | 1 (10-14 13:38Z) |
| us-east-1 | 310 | 71% | 6.6 | 4 (10-14 13:38Z) |
| us-east-2 | 310 | 72% | 7.0 | 1 (10-14 13:38Z) |
| us-west-2 | 310 | 53% | 5.7 | 5 (10-14 13:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999919923991399119911999999999999992399239
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999922992999299919991499999999999299199912
ap-southeast-2   222292999229111111191111111189199999911111111111
ap-southeast-3   111111111111111111388111113891199979395151122111
us-east-1        634999999995545334333663546456998299999945426664
us-east-2        999999999992399332121211121211992299999911912991
us-west-2        999999999994323544132333133233999999359299442495
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 8 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 185 | 71% | 7.2 | 9 (10-14 13:38Z) |
| ap-east-1 ape1-az2 | 155 | 74% | 7.4 | 9 (10-14 13:38Z) |
| ap-east-1 ape1-az3 | 155 | 72% | 7.3 | 9 (10-14 13:38Z) |
| ap-northeast-1 apne1-az1 | 146 | 92% | 8.5 | 9 (10-14 13:38Z) |
| ap-northeast-1 apne1-az2 | 84 | 69% | 7.1 | 9 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 176 | 98% | 8.9 | 9 (10-14 13:38Z) |
| ap-northeast-2 apne2-az1 | 244 | 100% | 9.0 | 9 (10-14 13:38Z) |
| ap-northeast-2 apne2-az2 | 67 | 78% | 7.6 | 2 (10-14 13:38Z) |
| ap-northeast-2 apne2-az3 | 265 | 100% | 9.0 | 9 (10-14 13:38Z) |
| ap-northeast-2 apne2-az4 | 179 | 74% | 7.4 | 9 (10-14 13:38Z) |
| ap-south-1 aps1-az1 | 109 | 80% | 7.8 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az2 | 109 | 67% | 7.0 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az3 | 126 | 86% | 8.2 | 9 (10-14 01:49Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 20 | 60% | 6.0 | 2 (10-14 07:30Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 106 | 98% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 151 | 99% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az3 | 140 | 94% | 8.6 | 9 (10-14 07:30Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.716800 | 2026-10-14T13:38:16Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-14T13:38:16Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.756800 | 2026-10-14T13:38:16Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938700 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591300 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586700 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574700 | 2026-10-14T13:38:16Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741900 | 2026-10-14T13:38:16Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548200 | 2026-10-14T13:38:16Z |
| ap-south-1 | ap-south-1a | Windows | 0.387800 | 2026-10-14T13:38:16Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.704300 | 2026-10-14T13:38:16Z |
| ap-south-1 | ap-south-1b | Windows | 0.333700 | 2026-10-14T13:38:16Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.723500 | 2026-10-14T13:38:16Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.528300 | 2026-10-14T13:38:16Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.507100 | 2026-10-14T13:38:16Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.623500 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.483900 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.502900 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.475300 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.421200 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.476400 | 2026-10-14T13:38:16Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.541800 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2a | Windows | 0.643800 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.532800 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.525600 | 2026-10-14T13:38:16Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.533700 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2a | Windows | 0.316900 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498500 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2b | Windows | 0.333300 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.499800 | 2026-10-14T13:38:16Z |
| us-west-2 | us-west-2c | Windows | 0.316900 | 2026-10-14T13:38:16Z |
