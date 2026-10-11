# Spot placement score log

Generated 2026-10-11 12:40 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 298 | 32% | 4.1 | 9 (10-11 12:40Z) |
| ap-northeast-1 | 298 | 15% | 2.8 | 1 (10-11 12:40Z) |
| ap-northeast-2 | 298 | 48% | 5.8 | 9 (10-11 12:40Z) |
| ap-south-1 | 298 | 2% | 1.8 | 2 (10-11 12:40Z) |
| ap-southeast-2 | 298 | 0% | 1.0 | 1 (10-11 12:40Z) |
| ap-southeast-3 | 298 | 21% | 3.3 | 9 (10-11 12:40Z) |
| us-east-1 | 298 | 10% | 2.6 | 2 (10-11 12:40Z) |
| us-east-2 | 298 | 27% | 3.5 | 9 (10-11 12:40Z) |
| us-west-2 | 298 | 12% | 2.4 | 1 (10-11 12:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111993991191199998121111111111111111111111822929
ap-northeast-1   812129821999999999999119111151197111111911122221
ap-northeast-2   999999999999999999999914999999999999999991999999
ap-south-1       111111121111111111122222222222222111221111112222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111199911411111111111111111111388111113891199979
us-east-1        221192292223311991999992111121111222113232333192
us-east-2        189999999911999999999991118111111111111111181199
us-west-2        211122212129999999919911211212111111111111999911
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 99 | 2% | 1.5 | 6 (10-11 12:40Z) |
| ap-east-1 ape1-az2 | 203 | 47% | 5.4 | 9 (10-11 12:40Z) |
| ap-northeast-1 apne1-az1 | 50 | 8% | 1.8 | 1 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 143 | 26% | 3.6 | 1 (10-11 12:40Z) |
| ap-northeast-2 apne2-az1 | 258 | 45% | 5.6 | 9 (10-11 12:40Z) |
| ap-northeast-2 apne2-az3 | 270 | 49% | 5.8 | 6 (10-11 12:40Z) |
| ap-northeast-2 apne2-az4 | 295 | 48% | 5.9 | 9 (10-11 12:40Z) |
| ap-south-1 aps1-az1 | 77 | 1% | 1.6 | 1 (10-10 08:24Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 47 | 0% | 1.1 | 1 (10-10 08:24Z) |
| ap-southeast-2 apse2-az2 | 30 | 0% | 1.0 | 1 (10-10 08:24Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 203 | 30% | 4.2 | 9 (10-11 12:40Z) |
| us-east-1 use1-az1 | 55 | 0% | 1.1 | 1 (10-11 05:37Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 94 | 28% | 3.5 | 9 (10-11 05:37Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 119 | 37% | 4.3 | 9 (10-11 12:40Z) |
| us-east-2 use2-az2 | 152 | 43% | 4.9 | 9 (10-11 12:40Z) |
| us-east-2 use2-az3 | 180 | 41% | 4.8 | 9 (10-11 12:40Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 64 | 27% | 3.5 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 298 | 49% | 5.9 | 9 (10-11 12:40Z) |
| ap-northeast-1 | 298 | 73% | 7.2 | 9 (10-11 12:40Z) |
| ap-northeast-2 | 298 | 100% | 9.0 | 9 (10-11 12:40Z) |
| ap-south-1 | 298 | 60% | 6.3 | 9 (10-11 12:40Z) |
| ap-southeast-2 | 298 | 17% | 3.2 | 9 (10-11 12:40Z) |
| ap-southeast-3 | 298 | 21% | 3.3 | 9 (10-11 12:40Z) |
| us-east-1 | 298 | 71% | 6.6 | 9 (10-11 12:40Z) |
| us-east-2 | 298 | 72% | 7.1 | 9 (10-11 12:40Z) |
| us-west-2 | 298 | 53% | 5.7 | 9 (10-11 12:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992249922999999999999919923991399119911999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999929999999999999999922992999299919991499999999
ap-southeast-2   222222222222222292999229111111191111111189199999
ap-southeast-3   111199911411111111111111111111388111113891199979
us-east-1        445594498557634999999995545334333663546456998299
us-east-2        999999999939999999999992399332121211121211992299
us-west-2        443393449959999999999994323544132333133233999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 176 | 69% | 7.2 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az2 | 146 | 72% | 7.3 | 9 (10-10 20:01Z) |
| ap-east-1 ape1-az3 | 145 | 70% | 7.2 | 9 (10-11 05:37Z) |
| ap-northeast-1 apne1-az1 | 141 | 92% | 8.5 | 9 (10-11 12:40Z) |
| ap-northeast-1 apne1-az2 | 76 | 66% | 6.9 | 9 (10-10 23:28Z) |
| ap-northeast-1 apne1-az4 | 168 | 99% | 8.9 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az1 | 233 | 100% | 9.0 | 9 (10-11 12:40Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 254 | 100% | 9.0 | 9 (10-10 20:01Z) |
| ap-northeast-2 apne2-az4 | 169 | 72% | 7.3 | 9 (10-10 23:28Z) |
| ap-south-1 aps1-az1 | 104 | 79% | 7.7 | 9 (10-11 12:40Z) |
| ap-south-1 aps1-az2 | 106 | 66% | 6.9 | 9 (10-10 01:42Z) |
| ap-south-1 aps1-az3 | 120 | 85% | 8.1 | 9 (10-11 12:40Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 60 | 28% | 4.6 | 9 (10-11 12:40Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 100 | 95% | 8.7 | 9 (10-11 12:40Z) |
| us-east-1 use1-az5 | 60 | 97% | 8.8 | 9 (10-11 12:40Z) |
| us-east-1 use1-az6 | 81 | 95% | 8.7 | 9 (10-10 08:24Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 134 | 94% | 8.6 | 9 (10-11 12:40Z) |
| us-west-2 usw2-az1 | 73 | 97% | 8.8 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 86 | 95% | 8.7 | 9 (10-11 12:40Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711600 | 2026-10-11T12:40:15Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-11T12:40:15Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.767000 | 2026-10-11T12:40:15Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.951500 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.599600 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586200 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.577500 | 2026-10-11T12:40:15Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742300 | 2026-10-11T12:40:15Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.574500 | 2026-10-11T12:40:15Z |
| ap-south-1 | ap-south-1a | Windows | 0.369100 | 2026-10-11T12:40:15Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.661500 | 2026-10-11T12:40:15Z |
| ap-south-1 | ap-south-1b | Windows | 0.350600 | 2026-10-11T12:40:15Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.721500 | 2026-10-11T12:40:15Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507000 | 2026-10-11T12:40:15Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.409000 | 2026-10-11T12:40:15Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.525900 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.480900 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.458000 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395000 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.455900 | 2026-10-11T12:40:15Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535200 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2a | Windows | 0.640000 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2b | Windows | 0.640000 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516800 | 2026-10-11T12:40:15Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.522100 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2a | Windows | 0.320300 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.487500 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2b | Windows | 0.321500 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.489700 | 2026-10-11T12:40:15Z |
| us-west-2 | us-west-2c | Windows | 0.320300 | 2026-10-11T12:40:15Z |
