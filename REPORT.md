# Spot placement score log

Generated 2026-10-02 08:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 259 | 34% | 4.3 | 1 (10-02 08:24Z) |
| ap-northeast-1 | 259 | 11% | 2.5 | 1 (10-02 08:24Z) |
| ap-northeast-2 | 259 | 41% | 5.4 | 9 (10-02 08:24Z) |
| ap-south-1 | 259 | 2% | 1.8 | 1 (10-02 08:24Z) |
| ap-southeast-2 | 259 | 0% | 1.0 | 1 (10-02 08:24Z) |
| ap-southeast-3 | 259 | 21% | 3.3 | 1 (10-02 08:24Z) |
| us-east-1 | 259 | 8% | 2.5 | 2 (10-02 08:24Z) |
| us-east-2 | 259 | 24% | 3.4 | 9 (10-02 08:24Z) |
| us-west-2 | 259 | 8% | 2.2 | 2 (10-02 08:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999899999111111993991
ap-northeast-1   112114818821379612221222222111189912799812129821
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111112211111111111111111111111111121
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   115437887681111187111111111111147651611111199911
us-east-1        112211122111112912229999132222222223222221192292
us-east-2        999999111111916999911199999991111181712189999999
us-west-2        111111122222111112111111211222222222221211122212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 1 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 186 | 47% | 5.5 | 9 (10-02 01:36Z) |
| ap-northeast-1 apne1-az1 | 36 | 0% | 1.3 | 2 (10-01 17:00Z) |
| ap-northeast-1 apne1-az4 | 119 | 18% | 3.1 | 1 (10-02 08:24Z) |
| ap-northeast-2 apne2-az1 | 233 | 40% | 5.3 | 9 (10-02 08:24Z) |
| ap-northeast-2 apne2-az3 | 241 | 44% | 5.6 | 9 (10-02 08:24Z) |
| ap-northeast-2 apne2-az4 | 256 | 41% | 5.5 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 99 | 3% | 2.5 | 1 (10-02 08:24Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 26 | 0% | 1.0 | 1 (10-02 08:24Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 185 | 28% | 4.1 | 9 (10-01 21:46Z) |
| us-east-1 use1-az1 | 39 | 0% | 1.2 | 1 (10-01 21:46Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 80 | 24% | 3.2 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 81 | 21% | 3.0 | 1 (10-02 08:24Z) |
| us-east-1 use1-az6 | 60 | 15% | 2.5 | 9 (10-01 10:01Z) |
| us-east-2 use2-az1 | 102 | 33% | 4.0 | 9 (10-02 01:36Z) |
| us-east-2 use2-az2 | 132 | 39% | 4.6 | 9 (10-02 01:36Z) |
| us-east-2 use2-az3 | 156 | 38% | 4.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 82 | 24% | 3.5 | 1 (10-02 08:24Z) |
| us-west-2 usw2-az2 | 49 | 22% | 3.3 | 1 (10-01 17:00Z) |
| us-west-2 usw2-az3 | 107 | 17% | 2.9 | 1 (10-02 01:36Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 259 | 41% | 5.5 | 9 (10-02 08:24Z) |
| ap-northeast-1 | 259 | 73% | 7.1 | 2 (10-02 08:24Z) |
| ap-northeast-2 | 259 | 100% | 9.0 | 9 (10-02 08:24Z) |
| ap-south-1 | 259 | 57% | 6.1 | 9 (10-02 08:24Z) |
| ap-southeast-2 | 259 | 15% | 3.1 | 2 (10-02 08:24Z) |
| ap-southeast-3 | 259 | 21% | 3.3 | 1 (10-02 08:24Z) |
| us-east-1 | 259 | 71% | 6.7 | 8 (10-02 08:24Z) |
| us-east-2 | 259 | 76% | 7.3 | 9 (10-02 08:24Z) |
| us-west-2 | 259 | 53% | 5.7 | 9 (10-02 08:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   333899999999999992223322344379999999999992249922
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       217111529999999999999991111111111119929999929999
ap-southeast-2   222222959229221122222222222222222222222222222222
ap-southeast-3   115437887681111187111111111111147651611111199911
us-east-1        489959445443595936559999365544433344333445594498
us-east-2        999999334333999999999999999998329299835999999999
us-west-2        922449453555322435333242534554554444454443393449
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 6 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 4 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 148 | 64% | 6.8 | 9 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 119 | 66% | 6.9 | 9 (10-02 08:24Z) |
| ap-east-1 ape1-az3 | 113 | 61% | 6.7 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az1 | 122 | 92% | 8.5 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az2 | 57 | 54% | 6.3 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az4 | 152 | 99% | 9.0 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az1 | 203 | 100% | 9.0 | 9 (10-02 08:24Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 231 | 100% | 9.0 | 9 (10-02 08:24Z) |
| ap-northeast-2 apne2-az4 | 141 | 67% | 7.0 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az1 | 80 | 72% | 7.3 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 101 | 82% | 7.9 | 9 (10-01 21:46Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 92 | 97% | 8.8 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 53 | 98% | 8.9 | 9 (10-02 01:36Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 95 | 99% | 8.9 | 9 (10-01 02:39Z) |
| us-east-2 use2-az2 | 137 | 99% | 8.9 | 9 (10-02 08:24Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 64 | 98% | 8.9 | 9 (10-01 10:01Z) |
| us-west-2 usw2-az2 | 59 | 95% | 8.6 | 2 (09-30 12:38Z) |
| us-west-2 usw2-az3 | 77 | 95% | 8.6 | 9 (10-02 08:24Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.736800 | 2026-10-02T08:24:29Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.851400 | 2026-10-02T08:24:29Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.782400 | 2026-10-02T08:24:29Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.965400 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592300 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577100 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565200 | 2026-10-02T08:24:29Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-02T08:24:29Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.648900 | 2026-10-02T08:24:29Z |
| ap-south-1 | ap-south-1a | Windows | 0.356600 | 2026-10-02T08:24:29Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.696200 | 2026-10-02T08:24:29Z |
| ap-south-1 | ap-south-1b | Windows | 0.358900 | 2026-10-02T08:24:29Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729800 | 2026-10-02T08:24:29Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497900 | 2026-10-02T08:24:29Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.574000 | 2026-10-02T08:24:29Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.554500 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1a | Windows | 0.298000 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.439200 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.452600 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395900 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.442200 | 2026-10-02T08:24:29Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.533000 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2a | Windows | 0.641800 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525000 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2b | Windows | 0.641500 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513600 | 2026-10-02T08:24:29Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.506300 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499500 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2b | Windows | 0.332100 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.485400 | 2026-10-02T08:24:29Z |
| us-west-2 | us-west-2c | Windows | 0.331300 | 2026-10-02T08:24:29Z |
