# Spot placement score log

Generated 2026-10-03 00:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 262 | 34% | 4.3 | 1 (10-03 00:24Z) |
| ap-northeast-1 | 262 | 12% | 2.6 | 9 (10-03 00:24Z) |
| ap-northeast-2 | 262 | 42% | 5.5 | 9 (10-03 00:24Z) |
| ap-south-1 | 262 | 2% | 1.8 | 1 (10-03 00:24Z) |
| ap-southeast-2 | 262 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 | 262 | 21% | 3.3 | 1 (10-03 00:24Z) |
| us-east-1 | 262 | 8% | 2.5 | 3 (10-03 00:24Z) |
| us-east-2 | 262 | 24% | 3.4 | 1 (10-03 00:24Z) |
| us-west-2 | 262 | 9% | 2.2 | 9 (10-03 00:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999899999111111993991191
ap-northeast-1   114818821379612221222222111189912799812129821999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111112211111111111111111111111111121111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   437887681111187111111111111147651611111199911411
us-east-1        211122111112912229999132222222223222221192292223
us-east-2        999111111916999911199999991111181712189999999911
us-west-2        111122222111112111111211222222222221211122212129
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 187 | 47% | 5.5 | 9 (10-02 20:39Z) |
| ap-northeast-1 apne1-az1 | 39 | 5% | 1.7 | 8 (10-03 00:24Z) |
| ap-northeast-1 apne1-az4 | 122 | 20% | 3.2 | 9 (10-03 00:24Z) |
| ap-northeast-2 apne2-az1 | 236 | 41% | 5.4 | 9 (10-03 00:24Z) |
| ap-northeast-2 apne2-az3 | 244 | 45% | 5.6 | 9 (10-03 00:24Z) |
| ap-northeast-2 apne2-az4 | 259 | 42% | 5.5 | 9 (10-03 00:24Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 80 | 24% | 3.2 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 82 | 21% | 3.0 | 1 (10-02 15:43Z) |
| us-east-1 use1-az6 | 60 | 15% | 2.5 | 9 (10-01 10:01Z) |
| us-east-2 use2-az1 | 103 | 34% | 4.1 | 9 (10-02 15:43Z) |
| us-east-2 use2-az2 | 133 | 40% | 4.7 | 9 (10-02 15:43Z) |
| us-east-2 use2-az3 | 157 | 38% | 4.7 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az1 | 82 | 24% | 3.5 | 1 (10-02 08:24Z) |
| us-west-2 usw2-az2 | 50 | 22% | 3.3 | 1 (10-03 00:24Z) |
| us-west-2 usw2-az3 | 108 | 17% | 2.9 | 4 (10-03 00:24Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 262 | 42% | 5.5 | 9 (10-03 00:24Z) |
| ap-northeast-1 | 262 | 73% | 7.2 | 9 (10-03 00:24Z) |
| ap-northeast-2 | 262 | 100% | 9.0 | 9 (10-03 00:24Z) |
| ap-south-1 | 262 | 58% | 6.2 | 9 (10-03 00:24Z) |
| ap-southeast-2 | 262 | 15% | 3.1 | 2 (10-03 00:24Z) |
| ap-southeast-3 | 262 | 21% | 3.3 | 1 (10-03 00:24Z) |
| us-east-1 | 262 | 72% | 6.7 | 7 (10-03 00:24Z) |
| us-east-2 | 262 | 76% | 7.3 | 9 (10-03 00:24Z) |
| us-west-2 | 262 | 53% | 5.7 | 9 (10-03 00:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   899999999999992223322344379999999999992249922999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111529999999999999991111111111119929999929999999
ap-southeast-2   222959229221122222222222222222222222222222222222
ap-southeast-3   437887681111187111111111111147651611111199911411
us-east-1        959445443595936559999365544433344333445594498557
us-east-2        999334333999999999999999998329299835999999999939
us-west-2        449453555322435333242534554554444454443393449959
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 150 | 64% | 6.8 | 9 (10-03 00:24Z) |
| ap-east-1 ape1-az2 | 122 | 66% | 7.0 | 9 (10-03 00:24Z) |
| ap-east-1 ape1-az3 | 115 | 62% | 6.7 | 9 (10-03 00:24Z) |
| ap-northeast-1 apne1-az1 | 124 | 92% | 8.5 | 9 (10-03 00:24Z) |
| ap-northeast-1 apne1-az2 | 60 | 57% | 6.4 | 9 (10-03 00:24Z) |
| ap-northeast-1 apne1-az4 | 152 | 99% | 9.0 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az1 | 206 | 100% | 9.0 | 9 (10-03 00:24Z) |
| ap-northeast-2 apne2-az2 | 55 | 75% | 7.4 | 9 (10-02 20:39Z) |
| ap-northeast-2 apne2-az3 | 232 | 100% | 9.0 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az4 | 143 | 67% | 7.0 | 9 (10-02 20:39Z) |
| ap-south-1 aps1-az1 | 83 | 73% | 7.4 | 9 (10-03 00:24Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 103 | 83% | 8.0 | 9 (10-03 00:24Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 92 | 97% | 8.8 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 53 | 98% | 8.9 | 9 (10-02 01:36Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 96 | 99% | 8.9 | 9 (10-03 00:24Z) |
| us-east-2 use2-az2 | 139 | 99% | 8.9 | 9 (10-03 00:24Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 65 | 98% | 8.9 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az2 | 60 | 95% | 8.6 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az3 | 78 | 95% | 8.6 | 9 (10-02 15:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.731800 | 2026-10-03T00:24:41Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.841100 | 2026-10-03T00:24:41Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.781300 | 2026-10-03T00:24:41Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964200 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591800 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577400 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565100 | 2026-10-03T00:24:41Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-03T00:24:41Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.647100 | 2026-10-03T00:24:41Z |
| ap-south-1 | ap-south-1a | Windows | 0.360000 | 2026-10-03T00:24:41Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.696300 | 2026-10-03T00:24:41Z |
| ap-south-1 | ap-south-1b | Windows | 0.359500 | 2026-10-03T00:24:41Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729000 | 2026-10-03T00:24:41Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-10-03T00:24:41Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.551800 | 2026-10-03T00:24:41Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.565400 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1a | Windows | 0.295900 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.444000 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.459900 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395600 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.458500 | 2026-10-03T00:24:41Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534000 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2a | Windows | 0.641600 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525800 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2b | Windows | 0.641300 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-03T00:24:41Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.503000 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.497900 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.483600 | 2026-10-03T00:24:41Z |
| us-west-2 | us-west-2c | Windows | 0.331800 | 2026-10-03T00:24:41Z |
