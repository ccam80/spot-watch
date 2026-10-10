# Spot placement score log

Generated 2026-10-10 01:42 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 292 | 32% | 4.1 | 1 (10-10 01:42Z) |
| ap-northeast-1 | 292 | 16% | 2.8 | 1 (10-10 01:42Z) |
| ap-northeast-2 | 292 | 47% | 5.8 | 1 (10-10 01:42Z) |
| ap-south-1 | 292 | 2% | 1.8 | 1 (10-10 01:42Z) |
| ap-southeast-2 | 292 | 0% | 1.0 | 1 (10-10 01:42Z) |
| ap-southeast-3 | 292 | 20% | 3.2 | 1 (10-10 01:42Z) |
| us-east-1 | 292 | 10% | 2.5 | 2 (10-10 01:42Z) |
| us-east-2 | 292 | 26% | 3.5 | 1 (10-10 01:42Z) |
| us-west-2 | 292 | 11% | 2.3 | 1 (10-10 01:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999111111993991191199998121111111111111111111111
ap-northeast-1   912799812129821999999999999119111151197111111911
ap-northeast-2   999999999999999999999999999914999999999999999991
ap-south-1       111111111111121111111111122222222222222111221111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   651611111199911411111111111111111111388111113891
us-east-1        223222221192292223311991999992111121111222113232
us-east-2        181712189999999911999999999991118111111111111111
us-west-2        222221211122212129999999919911211212111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 96 | 0% | 1.4 | 1 (10-10 01:42Z) |
| ap-east-1 ape1-az2 | 200 | 46% | 5.4 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 49 | 8% | 1.8 | 1 (10-09 21:36Z) |
| ap-northeast-1 apne1-az4 | 141 | 26% | 3.7 | 1 (10-10 01:42Z) |
| ap-northeast-2 apne2-az1 | 253 | 43% | 5.5 | 9 (10-09 21:36Z) |
| ap-northeast-2 apne2-az3 | 266 | 48% | 5.8 | 1 (10-10 01:42Z) |
| ap-northeast-2 apne2-az4 | 289 | 47% | 5.8 | 1 (10-10 01:42Z) |
| ap-south-1 aps1-az1 | 76 | 1% | 1.6 | 1 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 46 | 0% | 1.1 | 1 (10-09 21:36Z) |
| ap-southeast-2 apse2-az2 | 29 | 0% | 1.0 | 1 (10-09 08:55Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 198 | 28% | 4.1 | 9 (10-09 21:36Z) |
| us-east-1 use1-az1 | 51 | 0% | 1.1 | 1 (10-10 01:42Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 92 | 27% | 3.4 | 1 (10-10 01:42Z) |
| us-east-1 use1-az5 | 92 | 25% | 3.3 | 1 (10-08 16:24Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 117 | 37% | 4.3 | 1 (10-10 01:42Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 175 | 41% | 4.8 | 1 (10-09 08:55Z) |
| us-west-2 usw2-az1 | 99 | 28% | 3.7 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az2 | 61 | 23% | 3.2 | 1 (10-09 21:36Z) |
| us-west-2 usw2-az3 | 122 | 20% | 3.2 | 1 (10-10 01:42Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 292 | 48% | 5.9 | 9 (10-10 01:42Z) |
| ap-northeast-1 | 292 | 73% | 7.1 | 9 (10-10 01:42Z) |
| ap-northeast-2 | 292 | 100% | 9.0 | 9 (10-10 01:42Z) |
| ap-south-1 | 292 | 60% | 6.3 | 9 (10-10 01:42Z) |
| ap-southeast-2 | 292 | 16% | 3.1 | 9 (10-10 01:42Z) |
| ap-southeast-3 | 292 | 20% | 3.2 | 1 (10-10 01:42Z) |
| us-east-1 | 292 | 71% | 6.6 | 6 (10-10 01:42Z) |
| us-east-2 | 292 | 72% | 7.1 | 1 (10-10 01:42Z) |
| us-west-2 | 292 | 52% | 5.7 | 3 (10-10 01:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999992249922999999999999919923991399119911999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       119929999929999999999999999922992999299919991499
ap-southeast-2   222222222222222222222292999229111111191111111189
ap-southeast-3   651611111199911411111111111111111111388111113891
us-east-1        344333445594498557634999999995545334333663546456
us-east-2        299835999999999939999999999992399332121211121211
us-west-2        444454443393449959999999999994323544132333133233
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 5 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 69% | 7.1 | 9 (10-10 01:42Z) |
| ap-east-1 ape1-az2 | 143 | 71% | 7.3 | 9 (10-09 16:07Z) |
| ap-east-1 ape1-az3 | 141 | 69% | 7.1 | 9 (10-10 01:42Z) |
| ap-northeast-1 apne1-az1 | 138 | 92% | 8.5 | 9 (10-09 21:36Z) |
| ap-northeast-1 apne1-az2 | 74 | 65% | 6.9 | 9 (10-10 01:42Z) |
| ap-northeast-1 apne1-az4 | 167 | 99% | 8.9 | 9 (10-10 01:42Z) |
| ap-northeast-2 apne2-az1 | 228 | 100% | 9.0 | 9 (10-10 01:42Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 251 | 100% | 9.0 | 9 (10-10 01:42Z) |
| ap-northeast-2 apne2-az4 | 166 | 72% | 7.3 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az1 | 99 | 78% | 7.7 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 117 | 85% | 8.1 | 9 (10-10 01:42Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 58 | 26% | 4.5 | 9 (10-09 21:36Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 98 | 95% | 8.6 | 2 (10-09 08:55Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 80 | 95% | 8.7 | 2 (10-09 08:55Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707400 | 2026-10-10T01:42:20Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-10T01:42:20Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.767100 | 2026-10-10T01:42:20Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.946000 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.600600 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581700 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574600 | 2026-10-10T01:42:20Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-10-10T01:42:20Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.608700 | 2026-10-10T01:42:20Z |
| ap-south-1 | ap-south-1a | Windows | 0.374500 | 2026-10-10T01:42:20Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.680300 | 2026-10-10T01:42:20Z |
| ap-south-1 | ap-south-1b | Windows | 0.352500 | 2026-10-10T01:42:20Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.716500 | 2026-10-10T01:42:20Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499100 | 2026-10-10T01:42:20Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.432400 | 2026-10-10T01:42:20Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574100 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.555400 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.484500 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.475200 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.402000 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.477000 | 2026-10-10T01:42:20Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534800 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2a | Windows | 0.640000 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529400 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2b | Windows | 0.640300 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.517600 | 2026-10-10T01:42:20Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.527300 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2a | Windows | 0.321700 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.490200 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2b | Windows | 0.324200 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.493700 | 2026-10-10T01:42:20Z |
| us-west-2 | us-west-2c | Windows | 0.321500 | 2026-10-10T01:42:20Z |
