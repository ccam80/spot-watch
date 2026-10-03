# Spot placement score log

Generated 2026-10-03 17:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 265 | 34% | 4.3 | 9 (10-03 17:12Z) |
| ap-northeast-1 | 265 | 13% | 2.7 | 9 (10-03 17:12Z) |
| ap-northeast-2 | 265 | 42% | 5.5 | 9 (10-03 17:12Z) |
| ap-south-1 | 265 | 2% | 1.8 | 1 (10-03 17:12Z) |
| ap-southeast-2 | 265 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 | 265 | 21% | 3.3 | 1 (10-03 17:12Z) |
| us-east-1 | 265 | 8% | 2.4 | 1 (10-03 17:12Z) |
| us-east-2 | 265 | 25% | 3.5 | 9 (10-03 17:12Z) |
| us-west-2 | 265 | 10% | 2.3 | 9 (10-03 17:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999899999111111993991191199
ap-northeast-1   818821379612221222222111189912799812129821999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111112211111111111111111111111111121111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   887681111187111111111111147651611111199911411111
us-east-1        122111112912229999132222222223222221192292223311
us-east-2        111111916999911199999991111181712189999999911999
us-west-2        122222111112111111211222222222221211122212129999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 3 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 189 | 48% | 5.5 | 9 (10-03 17:12Z) |
| ap-northeast-1 apne1-az1 | 41 | 7% | 1.8 | 2 (10-03 17:12Z) |
| ap-northeast-1 apne1-az4 | 125 | 22% | 3.4 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az1 | 238 | 42% | 5.4 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az3 | 247 | 45% | 5.7 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az4 | 262 | 43% | 5.6 | 9 (10-03 17:12Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 52 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 80 | 24% | 3.2 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 82 | 21% | 3.0 | 1 (10-02 15:43Z) |
| us-east-1 use1-az6 | 61 | 15% | 2.5 | 1 (10-03 06:23Z) |
| us-east-2 use2-az1 | 105 | 35% | 4.2 | 9 (10-03 12:27Z) |
| us-east-2 use2-az2 | 136 | 41% | 4.8 | 9 (10-03 17:12Z) |
| us-east-2 use2-az3 | 160 | 39% | 4.8 | 9 (10-03 17:12Z) |
| us-west-2 usw2-az1 | 84 | 26% | 3.6 | 9 (10-03 12:27Z) |
| us-west-2 usw2-az2 | 51 | 24% | 3.4 | 9 (10-03 12:27Z) |
| us-west-2 usw2-az3 | 110 | 18% | 3.0 | 9 (10-03 17:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 265 | 42% | 5.5 | 9 (10-03 17:12Z) |
| ap-northeast-1 | 265 | 74% | 7.2 | 9 (10-03 17:12Z) |
| ap-northeast-2 | 265 | 100% | 9.0 | 9 (10-03 17:12Z) |
| ap-south-1 | 265 | 58% | 6.2 | 9 (10-03 17:12Z) |
| ap-southeast-2 | 265 | 15% | 3.1 | 2 (10-03 17:12Z) |
| ap-southeast-3 | 265 | 21% | 3.3 | 1 (10-03 17:12Z) |
| us-east-1 | 265 | 71% | 6.6 | 4 (10-03 17:12Z) |
| us-east-2 | 265 | 76% | 7.3 | 9 (10-03 17:12Z) |
| us-west-2 | 265 | 54% | 5.8 | 9 (10-03 17:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999992223322344379999999999992249922999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       529999999999999991111111111119929999929999999999
ap-southeast-2   959229221122222222222222222222222222222222222222
ap-southeast-3   887681111187111111111111147651611111199911411111
us-east-1        445443595936559999365544433344333445594498557634
us-east-2        334333999999999999999998329299835999999999939999
us-west-2        453555322435333242534554554444454443393449959999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 152 | 64% | 6.9 | 9 (10-03 17:12Z) |
| ap-east-1 ape1-az2 | 123 | 67% | 7.0 | 9 (10-03 12:27Z) |
| ap-east-1 ape1-az3 | 117 | 62% | 6.7 | 9 (10-03 17:12Z) |
| ap-northeast-1 apne1-az1 | 126 | 92% | 8.5 | 9 (10-03 17:12Z) |
| ap-northeast-1 apne1-az2 | 62 | 58% | 6.5 | 9 (10-03 12:27Z) |
| ap-northeast-1 apne1-az4 | 154 | 99% | 9.0 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az1 | 208 | 100% | 9.0 | 9 (10-03 12:27Z) |
| ap-northeast-2 apne2-az2 | 56 | 75% | 7.4 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az3 | 233 | 100% | 9.0 | 9 (10-03 12:27Z) |
| ap-northeast-2 apne2-az4 | 145 | 68% | 7.1 | 9 (10-03 17:12Z) |
| ap-south-1 aps1-az1 | 85 | 74% | 7.4 | 9 (10-03 12:27Z) |
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
| us-east-2 use2-az1 | 97 | 99% | 8.9 | 9 (10-03 06:23Z) |
| us-east-2 use2-az2 | 142 | 99% | 8.9 | 9 (10-03 17:12Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 68 | 99% | 8.9 | 9 (10-03 17:12Z) |
| us-west-2 usw2-az2 | 62 | 95% | 8.6 | 9 (10-03 17:12Z) |
| us-west-2 usw2-az3 | 80 | 95% | 8.7 | 9 (10-03 17:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.728400 | 2026-10-03T17:12:31Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-03T17:12:31Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783200 | 2026-10-03T17:12:31Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.962100 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593200 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565200 | 2026-10-03T17:12:31Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743500 | 2026-10-03T17:12:31Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.650000 | 2026-10-03T17:12:31Z |
| ap-south-1 | ap-south-1a | Windows | 0.367500 | 2026-10-03T17:12:31Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.701900 | 2026-10-03T17:12:31Z |
| ap-south-1 | ap-south-1b | Windows | 0.360900 | 2026-10-03T17:12:31Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.728300 | 2026-10-03T17:12:31Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-10-03T17:12:31Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.544300 | 2026-10-03T17:12:31Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.577500 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1a | Windows | 0.293000 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.444300 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.469300 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.410200 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.482700 | 2026-10-03T17:12:31Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534500 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525200 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2b | Windows | 0.641600 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-03T17:12:31Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.502200 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2a | Windows | 0.332700 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496300 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2b | Windows | 0.332300 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.481600 | 2026-10-03T17:12:31Z |
| us-west-2 | us-west-2c | Windows | 0.331600 | 2026-10-03T17:12:31Z |
