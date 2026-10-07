# Spot placement score log

Generated 2026-10-07 21:56 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 283 | 33% | 4.2 | 1 (10-07 21:56Z) |
| ap-northeast-1 | 283 | 16% | 2.8 | 7 (10-07 21:56Z) |
| ap-northeast-2 | 283 | 45% | 5.7 | 9 (10-07 21:56Z) |
| ap-south-1 | 283 | 2% | 1.8 | 2 (10-07 21:56Z) |
| ap-southeast-2 | 283 | 0% | 1.0 | 1 (10-07 21:56Z) |
| ap-southeast-3 | 283 | 20% | 3.2 | 8 (10-07 21:56Z) |
| us-east-1 | 283 | 10% | 2.6 | 1 (10-07 21:56Z) |
| us-east-2 | 283 | 27% | 3.6 | 1 (10-07 21:56Z) |
| us-west-2 | 283 | 11% | 2.4 | 1 (10-07 21:56Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999899999111111993991191199998121111111111111
ap-northeast-1   222111189912799812129821999999999999119111151197
ap-northeast-2   999999999999999999999999999999999999914999999999
ap-south-1       111111111111111111111121111111111122222222222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111147651611111199911411111111111111111111388
us-east-1        132222222223222221192292223311991999992111121111
us-east-2        999991111181712189999999911999999999991118111111
us-west-2        211222222222221211122212129999999919911211212111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 6 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 6 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 94 | 0% | 1.4 | 1 (10-07 08:33Z) |
| ap-east-1 ape1-az2 | 197 | 47% | 5.4 | 1 (10-07 21:56Z) |
| ap-northeast-1 apne1-az1 | 45 | 9% | 1.8 | 1 (10-07 16:22Z) |
| ap-northeast-1 apne1-az4 | 138 | 26% | 3.7 | 7 (10-07 21:56Z) |
| ap-northeast-2 apne2-az1 | 245 | 42% | 5.4 | 9 (10-07 21:56Z) |
| ap-northeast-2 apne2-az3 | 258 | 47% | 5.7 | 9 (10-07 21:56Z) |
| ap-northeast-2 apne2-az4 | 280 | 46% | 5.7 | 9 (10-07 21:56Z) |
| ap-south-1 aps1-az1 | 73 | 1% | 1.6 | 1 (10-06 10:07Z) |
| ap-south-1 aps1-az3 | 106 | 3% | 2.4 | 1 (10-07 01:27Z) |
| ap-southeast-2 apse2-az1 | 41 | 0% | 1.1 | 1 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 55 | 0% | 1.0 | 1 (10-07 01:27Z) |
| ap-southeast-3 apse3-az3 | 193 | 28% | 4.1 | 8 (10-07 21:56Z) |
| us-east-1 use1-az1 | 43 | 0% | 1.1 | 1 (10-07 16:22Z) |
| us-east-1 use1-az2 | 78 | 4% | 1.6 | 1 (10-07 21:56Z) |
| us-east-1 use1-az4 | 87 | 29% | 3.6 | 1 (10-06 02:54Z) |
| us-east-1 use1-az5 | 91 | 25% | 3.3 | 1 (10-07 21:56Z) |
| us-east-1 use1-az6 | 71 | 21% | 2.9 | 1 (10-07 01:27Z) |
| us-east-2 use2-az1 | 113 | 38% | 4.4 | 2 (10-06 10:07Z) |
| us-east-2 use2-az2 | 149 | 43% | 4.9 | 1 (10-07 08:33Z) |
| us-east-2 use2-az3 | 173 | 41% | 4.8 | 1 (10-07 21:56Z) |
| us-west-2 usw2-az1 | 97 | 29% | 3.8 | 1 (10-07 21:56Z) |
| us-west-2 usw2-az2 | 56 | 25% | 3.4 | 1 (10-07 16:22Z) |
| us-west-2 usw2-az3 | 119 | 21% | 3.2 | 1 (10-07 08:33Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 283 | 46% | 5.8 | 9 (10-07 21:56Z) |
| ap-northeast-1 | 283 | 73% | 7.2 | 9 (10-07 21:56Z) |
| ap-northeast-2 | 283 | 100% | 9.0 | 9 (10-07 21:56Z) |
| ap-south-1 | 283 | 59% | 6.3 | 9 (10-07 21:56Z) |
| ap-southeast-2 | 283 | 16% | 3.1 | 1 (10-07 21:56Z) |
| ap-southeast-3 | 283 | 20% | 3.2 | 8 (10-07 21:56Z) |
| us-east-1 | 283 | 71% | 6.6 | 3 (10-07 21:56Z) |
| us-east-2 | 283 | 75% | 7.2 | 1 (10-07 21:56Z) |
| us-west-2 | 283 | 53% | 5.8 | 2 (10-07 21:56Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   344379999999999992249922999999999999919923991399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111119929999929999999999999999922992999299
ap-southeast-2   222222222222222222222222222222292999229111111191
ap-southeast-3   111111147651611111199911411111111111111111111388
us-east-1        365544433344333445594498557634999999995545334333
us-east-2        999998329299835999999999939999999999992399332121
us-west-2        534554554444454443393449959999999999994323544132
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 6 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 166 | 67% | 7.0 | 9 (10-07 21:56Z) |
| ap-east-1 ape1-az2 | 136 | 70% | 7.2 | 9 (10-07 21:56Z) |
| ap-east-1 ape1-az3 | 132 | 67% | 7.0 | 9 (10-07 21:56Z) |
| ap-northeast-1 apne1-az1 | 134 | 92% | 8.5 | 9 (10-07 21:56Z) |
| ap-northeast-1 apne1-az2 | 70 | 63% | 6.8 | 9 (10-07 21:56Z) |
| ap-northeast-1 apne1-az4 | 162 | 99% | 8.9 | 9 (10-07 16:22Z) |
| ap-northeast-2 apne2-az1 | 219 | 100% | 9.0 | 9 (10-07 21:56Z) |
| ap-northeast-2 apne2-az2 | 63 | 78% | 7.6 | 9 (10-06 21:35Z) |
| ap-northeast-2 apne2-az3 | 244 | 100% | 9.0 | 9 (10-07 21:56Z) |
| ap-northeast-2 apne2-az4 | 158 | 70% | 7.2 | 9 (10-07 21:56Z) |
| ap-south-1 aps1-az1 | 95 | 77% | 7.6 | 9 (10-07 21:56Z) |
| ap-south-1 aps1-az2 | 102 | 65% | 6.9 | 9 (10-07 21:56Z) |
| ap-south-1 aps1-az3 | 111 | 84% | 8.0 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 55 | 24% | 4.3 | 3 (10-07 08:33Z) |
| us-east-1 use1-az1 | 15 | 80% | 7.4 | 2 (10-07 08:33Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 96 | 97% | 8.8 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 58 | 98% | 8.9 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 102 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 71 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707900 | 2026-10-07T21:56:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-07T21:56:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.755100 | 2026-10-07T21:56:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938200 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.603000 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578600 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572700 | 2026-10-07T21:56:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-10-07T21:56:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.643400 | 2026-10-07T21:56:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.386500 | 2026-10-07T21:56:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.704400 | 2026-10-07T21:56:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.355500 | 2026-10-07T21:56:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719900 | 2026-10-07T21:56:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.506000 | 2026-10-07T21:56:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.470900 | 2026-10-07T21:56:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.589000 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.493100 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.484000 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.413800 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.504300 | 2026-10-07T21:56:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534500 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2a | Windows | 0.640400 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528900 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516100 | 2026-10-07T21:56:45Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.529900 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2a | Windows | 0.325600 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.493700 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2b | Windows | 0.326500 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494500 | 2026-10-07T21:56:45Z |
| us-west-2 | us-west-2c | Windows | 0.323900 | 2026-10-07T21:56:45Z |
