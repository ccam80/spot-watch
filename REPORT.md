# Spot placement score log

Generated 2026-10-07 01:27 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 280 | 33% | 4.2 | 1 (10-07 01:27Z) |
| ap-northeast-1 | 280 | 15% | 2.8 | 1 (10-07 01:27Z) |
| ap-northeast-2 | 280 | 45% | 5.7 | 9 (10-07 01:27Z) |
| ap-south-1 | 280 | 2% | 1.8 | 2 (10-07 01:27Z) |
| ap-southeast-2 | 280 | 0% | 1.0 | 1 (10-07 01:27Z) |
| ap-southeast-3 | 280 | 20% | 3.2 | 1 (10-07 01:27Z) |
| us-east-1 | 280 | 10% | 2.6 | 1 (10-07 01:27Z) |
| us-east-2 | 280 | 27% | 3.6 | 1 (10-07 01:27Z) |
| us-west-2 | 280 | 11% | 2.4 | 2 (10-07 01:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999899999111111993991191199998121111111111
ap-northeast-1   222222111189912799812129821999999999999119111151
ap-northeast-2   999999999999999999999999999999999999999914999999
ap-south-1       111111111111111111111111121111111111122222222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111147651611111199911411111111111111111111
us-east-1        999132222222223222221192292223311991999992111121
us-east-2        199999991111181712189999999911999999999991118111
us-west-2        111211222222222221211122212129999999919911211212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 6 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 93 | 0% | 1.4 | 1 (10-07 01:27Z) |
| ap-east-1 ape1-az2 | 195 | 47% | 5.5 | 1 (10-06 21:35Z) |
| ap-northeast-1 apne1-az1 | 44 | 9% | 1.9 | 1 (10-06 10:07Z) |
| ap-northeast-1 apne1-az4 | 135 | 25% | 3.6 | 1 (10-07 01:27Z) |
| ap-northeast-2 apne2-az1 | 242 | 41% | 5.4 | 1 (10-06 21:35Z) |
| ap-northeast-2 apne2-az3 | 255 | 46% | 5.7 | 9 (10-07 01:27Z) |
| ap-northeast-2 apne2-az4 | 277 | 45% | 5.7 | 9 (10-07 01:27Z) |
| ap-south-1 aps1-az1 | 73 | 1% | 1.6 | 1 (10-06 10:07Z) |
| ap-south-1 aps1-az3 | 106 | 3% | 2.4 | 1 (10-07 01:27Z) |
| ap-southeast-2 apse2-az1 | 40 | 0% | 1.1 | 1 (10-06 21:35Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 55 | 0% | 1.0 | 1 (10-07 01:27Z) |
| ap-southeast-3 apse3-az3 | 190 | 27% | 4.0 | 1 (10-06 10:07Z) |
| us-east-1 use1-az1 | 42 | 0% | 1.1 | 1 (10-06 16:46Z) |
| us-east-1 use1-az2 | 76 | 4% | 1.6 | 1 (10-06 16:46Z) |
| us-east-1 use1-az4 | 87 | 29% | 3.6 | 1 (10-06 02:54Z) |
| us-east-1 use1-az5 | 90 | 26% | 3.3 | 1 (10-06 21:35Z) |
| us-east-1 use1-az6 | 71 | 21% | 2.9 | 1 (10-07 01:27Z) |
| us-east-2 use2-az1 | 113 | 38% | 4.4 | 2 (10-06 10:07Z) |
| us-east-2 use2-az2 | 148 | 43% | 4.9 | 1 (10-07 01:27Z) |
| us-east-2 use2-az3 | 171 | 42% | 4.9 | 1 (10-06 21:35Z) |
| us-west-2 usw2-az1 | 96 | 29% | 3.8 | 1 (10-07 01:27Z) |
| us-west-2 usw2-az2 | 55 | 25% | 3.5 | 1 (10-06 10:07Z) |
| us-west-2 usw2-az3 | 118 | 21% | 3.2 | 1 (10-07 01:27Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 280 | 45% | 5.7 | 9 (10-07 01:27Z) |
| ap-northeast-1 | 280 | 74% | 7.2 | 1 (10-07 01:27Z) |
| ap-northeast-2 | 280 | 100% | 9.0 | 9 (10-07 01:27Z) |
| ap-south-1 | 280 | 59% | 6.3 | 9 (10-07 01:27Z) |
| ap-southeast-2 | 280 | 16% | 3.1 | 1 (10-07 01:27Z) |
| ap-southeast-3 | 280 | 20% | 3.2 | 1 (10-07 01:27Z) |
| us-east-1 | 280 | 71% | 6.6 | 4 (10-07 01:27Z) |
| us-east-2 | 280 | 75% | 7.3 | 2 (10-07 01:27Z) |
| us-west-2 | 280 | 54% | 5.8 | 4 (10-07 01:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   322344379999999999992249922999999999999919923991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       991111111111119929999929999999999999999922992999
ap-southeast-2   222222222222222222222222222222222292999229111111
ap-southeast-3   111111111147651611111199911411111111111111111111
us-east-1        999365544433344333445594498557634999999995545334
us-east-2        999999998329299835999999999939999999999992399332
us-west-2        242534554554444454443393449959999999999994323544
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 8 | 6 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 163 | 67% | 7.0 | 9 (10-07 01:27Z) |
| ap-east-1 ape1-az2 | 133 | 69% | 7.2 | 9 (10-07 01:27Z) |
| ap-east-1 ape1-az3 | 129 | 66% | 7.0 | 9 (10-07 01:27Z) |
| ap-northeast-1 apne1-az1 | 132 | 92% | 8.5 | 9 (10-06 21:35Z) |
| ap-northeast-1 apne1-az2 | 68 | 62% | 6.7 | 9 (10-06 21:35Z) |
| ap-northeast-1 apne1-az4 | 160 | 99% | 9.0 | 9 (10-06 16:46Z) |
| ap-northeast-2 apne2-az1 | 216 | 100% | 9.0 | 9 (10-07 01:27Z) |
| ap-northeast-2 apne2-az2 | 63 | 78% | 7.6 | 9 (10-06 21:35Z) |
| ap-northeast-2 apne2-az3 | 242 | 100% | 9.0 | 9 (10-07 01:27Z) |
| ap-northeast-2 apne2-az4 | 156 | 70% | 7.2 | 9 (10-07 01:27Z) |
| ap-south-1 aps1-az1 | 93 | 76% | 7.6 | 9 (10-07 01:27Z) |
| ap-south-1 aps1-az2 | 101 | 64% | 6.8 | 9 (10-07 01:27Z) |
| ap-south-1 aps1-az3 | 110 | 84% | 8.0 | 9 (10-07 01:27Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 32 | 62% | 6.8 | 9 (10-05 15:54Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 14 | 86% | 7.8 | 2 (10-07 01:27Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708900 | 2026-10-07T01:27:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-07T01:27:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.760300 | 2026-10-07T01:27:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.942700 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.602600 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578200 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569500 | 2026-10-07T01:27:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-10-07T01:27:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.652400 | 2026-10-07T01:27:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.382800 | 2026-10-07T01:27:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.713300 | 2026-10-07T01:27:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.356700 | 2026-10-07T01:27:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718000 | 2026-10-07T01:27:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499100 | 2026-10-07T01:27:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.485800 | 2026-10-07T01:27:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.598800 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.473000 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.485600 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.415800 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.502500 | 2026-10-07T01:27:35Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532000 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2a | Windows | 0.640200 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527200 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-07T01:27:35Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.529100 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2a | Windows | 0.328000 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.497600 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2b | Windows | 0.329200 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.491100 | 2026-10-07T01:27:35Z |
| us-west-2 | us-west-2c | Windows | 0.327400 | 2026-10-07T01:27:35Z |
