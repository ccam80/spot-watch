# Spot placement score log

Generated 2026-10-04 06:47 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 268 | 35% | 4.4 | 8 (10-04 06:47Z) |
| ap-northeast-1 | 268 | 14% | 2.7 | 9 (10-04 06:47Z) |
| ap-northeast-2 | 268 | 43% | 5.6 | 9 (10-04 06:47Z) |
| ap-south-1 | 268 | 2% | 1.8 | 1 (10-04 06:47Z) |
| ap-southeast-2 | 268 | 0% | 1.0 | 1 (10-04 06:47Z) |
| ap-southeast-3 | 268 | 21% | 3.3 | 1 (10-04 06:47Z) |
| us-east-1 | 268 | 9% | 2.5 | 1 (10-04 06:47Z) |
| us-east-2 | 268 | 26% | 3.5 | 9 (10-04 06:47Z) |
| us-west-2 | 268 | 11% | 2.4 | 9 (10-04 06:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999899999111111993991191199998
ap-northeast-1   821379612221222222111189912799812129821999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111112211111111111111111111111111121111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   681111187111111111111147651611111199911411111111
us-east-1        111112912229999132222222223222221192292223311991
us-east-2        111916999911199999991111181712189999999911999999
us-west-2        222111112111111211222222222221211122212129999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 4 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 191 | 48% | 5.6 | 8 (10-04 06:47Z) |
| ap-northeast-1 apne1-az1 | 41 | 7% | 1.8 | 2 (10-03 17:12Z) |
| ap-northeast-1 apne1-az4 | 128 | 23% | 3.5 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az1 | 239 | 42% | 5.4 | 6 (10-04 06:47Z) |
| ap-northeast-2 apne2-az3 | 250 | 46% | 5.7 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az4 | 265 | 43% | 5.6 | 9 (10-04 06:47Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 52 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 81 | 25% | 3.3 | 9 (10-03 21:08Z) |
| us-east-1 use1-az5 | 84 | 23% | 3.1 | 9 (10-04 00:31Z) |
| us-east-1 use1-az6 | 63 | 17% | 2.7 | 9 (10-04 00:31Z) |
| us-east-2 use2-az1 | 106 | 36% | 4.2 | 9 (10-04 00:31Z) |
| us-east-2 use2-az2 | 139 | 42% | 4.8 | 9 (10-04 06:47Z) |
| us-east-2 use2-az3 | 163 | 40% | 4.8 | 9 (10-04 06:47Z) |
| us-west-2 usw2-az1 | 87 | 29% | 3.8 | 9 (10-04 06:47Z) |
| us-west-2 usw2-az2 | 52 | 25% | 3.5 | 9 (10-04 06:47Z) |
| us-west-2 usw2-az3 | 112 | 20% | 3.1 | 9 (10-04 06:47Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 268 | 43% | 5.6 | 9 (10-04 06:47Z) |
| ap-northeast-1 | 268 | 74% | 7.2 | 9 (10-04 06:47Z) |
| ap-northeast-2 | 268 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-south-1 | 268 | 59% | 6.2 | 9 (10-04 06:47Z) |
| ap-southeast-2 | 268 | 15% | 3.1 | 2 (10-04 06:47Z) |
| ap-southeast-3 | 268 | 21% | 3.3 | 1 (10-04 06:47Z) |
| us-east-1 | 268 | 72% | 6.7 | 9 (10-04 06:47Z) |
| us-east-2 | 268 | 76% | 7.4 | 9 (10-04 06:47Z) |
| us-west-2 | 268 | 54% | 5.8 | 9 (10-04 06:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999992223322344379999999999992249922999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999991111111111119929999929999999999999
ap-southeast-2   229221122222222222222222222222222222222222222292
ap-southeast-3   681111187111111111111147651611111199911411111111
us-east-1        443595936559999365544433344333445594498557634999
us-east-2        333999999999999999998329299835999999999939999999
us-west-2        555322435333242534554554444454443393449959999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 152 | 64% | 6.9 | 9 (10-03 17:12Z) |
| ap-east-1 ape1-az2 | 124 | 67% | 7.0 | 9 (10-04 06:47Z) |
| ap-east-1 ape1-az3 | 119 | 63% | 6.8 | 9 (10-04 00:31Z) |
| ap-northeast-1 apne1-az1 | 126 | 92% | 8.5 | 9 (10-03 17:12Z) |
| ap-northeast-1 apne1-az2 | 64 | 59% | 6.6 | 9 (10-04 06:47Z) |
| ap-northeast-1 apne1-az4 | 154 | 99% | 9.0 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az1 | 209 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az2 | 58 | 76% | 7.5 | 9 (10-04 00:31Z) |
| ap-northeast-2 apne2-az3 | 234 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az4 | 145 | 68% | 7.1 | 9 (10-03 17:12Z) |
| ap-south-1 aps1-az1 | 87 | 75% | 7.5 | 9 (10-04 00:31Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 106 | 83% | 8.0 | 9 (10-04 06:47Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 94 | 97% | 8.8 | 9 (10-04 00:31Z) |
| us-east-1 use1-az5 | 56 | 98% | 8.9 | 9 (10-04 06:47Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 98 | 99% | 8.9 | 9 (10-04 06:47Z) |
| us-east-2 use2-az2 | 144 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 70 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-west-2 usw2-az2 | 63 | 95% | 8.6 | 9 (10-04 06:47Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.723400 | 2026-10-04T06:47:09Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-04T06:47:09Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.778900 | 2026-10-04T06:47:09Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.958300 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593700 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577400 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565300 | 2026-10-04T06:47:09Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743600 | 2026-10-04T06:47:09Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.656100 | 2026-10-04T06:47:09Z |
| ap-south-1 | ap-south-1a | Windows | 0.367600 | 2026-10-04T06:47:09Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.702700 | 2026-10-04T06:47:09Z |
| ap-south-1 | ap-south-1b | Windows | 0.361700 | 2026-10-04T06:47:09Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.730800 | 2026-10-04T06:47:09Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497900 | 2026-10-04T06:47:09Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.529900 | 2026-10-04T06:47:09Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.576000 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1a | Windows | 0.287900 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.445000 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.477800 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.412900 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.498600 | 2026-10-04T06:47:09Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535300 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2a | Windows | 0.641300 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527600 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516200 | 2026-10-04T06:47:09Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.503400 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2a | Windows | 0.332200 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496200 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2b | Windows | 0.331600 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.482600 | 2026-10-04T06:47:09Z |
| us-west-2 | us-west-2c | Windows | 0.330700 | 2026-10-04T06:47:09Z |
