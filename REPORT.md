# Spot placement score log

Generated 2026-10-05 15:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 274 | 34% | 4.3 | 1 (10-05 15:54Z) |
| ap-northeast-1 | 274 | 15% | 2.8 | 9 (10-05 15:54Z) |
| ap-northeast-2 | 274 | 43% | 5.6 | 4 (10-05 15:54Z) |
| ap-south-1 | 274 | 2% | 1.8 | 2 (10-05 15:54Z) |
| ap-southeast-2 | 274 | 0% | 1.0 | 1 (10-05 15:54Z) |
| ap-southeast-3 | 274 | 20% | 3.2 | 1 (10-05 15:54Z) |
| us-east-1 | 274 | 10% | 2.6 | 2 (10-05 15:54Z) |
| us-east-2 | 274 | 27% | 3.6 | 1 (10-05 15:54Z) |
| us-west-2 | 274 | 12% | 2.4 | 1 (10-05 15:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999899999111111993991191199998121111
ap-northeast-1   612221222222111189912799812129821999999999999119
ap-northeast-2   999999999999999999999999999999999999999999999914
ap-south-1       112211111111111111111111111111121111111111122222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   187111111111111147651611111199911411111111111111
us-east-1        912229999132222222223222221192292223311991999992
us-east-2        999911199999991111181712189999999911999999999991
us-west-2        112111111211222222222221211122212129999999919911
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 91 | 0% | 1.4 | 1 (10-05 15:54Z) |
| ap-east-1 ape1-az2 | 192 | 48% | 5.5 | 1 (10-05 06:55Z) |
| ap-northeast-1 apne1-az1 | 42 | 10% | 1.9 | 7 (10-05 15:54Z) |
| ap-northeast-1 apne1-az4 | 132 | 26% | 3.6 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az1 | 240 | 42% | 5.4 | 1 (10-05 06:55Z) |
| ap-northeast-2 apne2-az3 | 251 | 46% | 5.7 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az4 | 271 | 44% | 5.6 | 4 (10-05 15:54Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 102 | 3% | 2.5 | 1 (10-05 15:54Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 53 | 0% | 1.0 | 1 (10-05 15:54Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 74 | 4% | 1.6 | 9 (10-05 00:49Z) |
| us-east-1 use1-az4 | 86 | 29% | 3.6 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 88 | 26% | 3.4 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 68 | 22% | 3.0 | 1 (10-05 15:54Z) |
| us-east-2 use2-az1 | 111 | 39% | 4.4 | 9 (10-05 06:55Z) |
| us-east-2 use2-az2 | 145 | 44% | 5.0 | 1 (10-05 15:54Z) |
| us-east-2 use2-az3 | 168 | 42% | 5.0 | 9 (10-05 06:55Z) |
| us-west-2 usw2-az1 | 92 | 30% | 3.9 | 1 (10-05 15:54Z) |
| us-west-2 usw2-az2 | 53 | 26% | 3.6 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az3 | 116 | 22% | 3.3 | 1 (10-05 15:54Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 274 | 44% | 5.6 | 9 (10-05 15:54Z) |
| ap-northeast-1 | 274 | 74% | 7.2 | 9 (10-05 15:54Z) |
| ap-northeast-2 | 274 | 100% | 9.0 | 9 (10-05 15:54Z) |
| ap-south-1 | 274 | 59% | 6.2 | 2 (10-05 15:54Z) |
| ap-southeast-2 | 274 | 16% | 3.2 | 9 (10-05 15:54Z) |
| ap-southeast-3 | 274 | 20% | 3.2 | 1 (10-05 15:54Z) |
| us-east-1 | 274 | 72% | 6.7 | 5 (10-05 15:54Z) |
| us-east-2 | 274 | 76% | 7.4 | 2 (10-05 15:54Z) |
| us-west-2 | 274 | 55% | 5.9 | 4 (10-05 15:54Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992223322344379999999999992249922999999999999919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999991111111111119929999929999999999999999922
ap-southeast-2   122222222222222222222222222222222222222292999229
ap-southeast-3   187111111111111147651611111199911411111111111111
us-east-1        936559999365544433344333445594498557634999999995
us-east-2        999999999999998329299835999999999939999999999992
us-west-2        435333242534554554444454443393449959999999999994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 158 | 66% | 6.9 | 9 (10-05 15:54Z) |
| ap-east-1 ape1-az2 | 127 | 68% | 7.1 | 9 (10-05 15:54Z) |
| ap-east-1 ape1-az3 | 123 | 64% | 6.9 | 9 (10-05 15:54Z) |
| ap-northeast-1 apne1-az1 | 129 | 92% | 8.5 | 9 (10-04 21:19Z) |
| ap-northeast-1 apne1-az2 | 65 | 60% | 6.6 | 9 (10-05 15:54Z) |
| ap-northeast-1 apne1-az4 | 158 | 99% | 9.0 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az1 | 212 | 100% | 9.0 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az2 | 62 | 77% | 7.6 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az3 | 236 | 100% | 9.0 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az4 | 150 | 69% | 7.1 | 9 (10-05 15:54Z) |
| ap-south-1 aps1-az1 | 90 | 76% | 7.5 | 9 (10-05 00:49Z) |
| ap-south-1 aps1-az2 | 96 | 62% | 6.7 | 9 (10-04 21:19Z) |
| ap-south-1 aps1-az3 | 107 | 83% | 8.0 | 9 (10-05 00:49Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 32 | 62% | 6.8 | 9 (10-05 15:54Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 96 | 97% | 8.8 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 58 | 98% | 8.9 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 100 | 99% | 8.9 | 9 (10-05 06:55Z) |
| us-east-2 use2-az2 | 145 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-east-2 use2-az3 | 128 | 94% | 8.6 | 9 (10-05 06:55Z) |
| us-west-2 usw2-az1 | 71 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.713800 | 2026-10-05T15:54:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-05T15:54:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764600 | 2026-10-05T15:54:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947600 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.599900 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577000 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565200 | 2026-10-05T15:54:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-05T15:54:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.653000 | 2026-10-05T15:54:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.372600 | 2026-10-05T15:54:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.720600 | 2026-10-05T15:54:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.358800 | 2026-10-05T15:54:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.717700 | 2026-10-05T15:54:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503200 | 2026-10-05T15:54:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.502600 | 2026-10-05T15:54:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.575100 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.450700 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.484800 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.401600 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.506700 | 2026-10-05T15:54:58Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534300 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528000 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-10-05T15:54:58Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.510700 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2a | Windows | 0.330200 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.490100 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2b | Windows | 0.331300 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.481100 | 2026-10-05T15:54:58Z |
| us-west-2 | us-west-2c | Windows | 0.329100 | 2026-10-05T15:54:58Z |
