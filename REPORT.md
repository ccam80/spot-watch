# Spot placement score log

Generated 2026-10-18 05:47 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 331 | 39% | 4.6 | 9 (10-18 05:47Z) |
| ap-northeast-1 | 331 | 15% | 2.7 | 6 (10-18 05:47Z) |
| ap-northeast-2 | 331 | 53% | 6.1 | 9 (10-18 05:47Z) |
| ap-south-1 | 331 | 2% | 1.8 | 2 (10-18 05:47Z) |
| ap-southeast-2 | 331 | 1% | 1.1 | 1 (10-18 05:47Z) |
| ap-southeast-3 | 331 | 23% | 3.3 | 2 (10-18 05:47Z) |
| us-east-1 | 331 | 9% | 2.5 | 2 (10-18 05:47Z) |
| us-east-2 | 331 | 29% | 3.6 | 9 (10-18 05:47Z) |
| us-west-2 | 331 | 11% | 2.3 | 1 (10-18 05:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111822929999999999999999999999999999999999
ap-northeast-1   111111911122221192212121114221142111132212932416
ap-northeast-2   999999991999999999999999999999999999999999999999
ap-south-1       111221111112222222222111112222222111222222222222
ap-southeast-2   111111111111111111111111111111111111111119119111
ap-southeast-3   111113891199979395151122111131151821438751867992
us-east-1        222113232333192233222113333232132312222233322192
us-east-2        111111111181199999911112991112911199911116199999
us-west-2        111111111999911111111111111111122111122211212121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 236 | 54% | 5.9 | 9 (10-18 05:47Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 156 | 25% | 3.6 | 4 (10-18 05:47Z) |
| ap-northeast-2 apne2-az1 | 290 | 49% | 5.8 | 9 (10-18 05:47Z) |
| ap-northeast-2 apne2-az3 | 303 | 53% | 6.1 | 9 (10-18 05:47Z) |
| ap-northeast-2 apne2-az4 | 328 | 53% | 6.2 | 9 (10-18 05:47Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 225 | 33% | 4.3 | 2 (10-18 05:47Z) |
| us-east-1 use1-az1 | 64 | 0% | 1.1 | 1 (10-18 05:47Z) |
| us-east-1 use1-az2 | 92 | 3% | 1.5 | 1 (10-17 13:39Z) |
| us-east-1 use1-az4 | 99 | 27% | 3.4 | 9 (10-18 00:55Z) |
| us-east-1 use1-az5 | 104 | 24% | 3.2 | 9 (10-18 00:55Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 130 | 40% | 4.5 | 9 (10-18 05:47Z) |
| us-east-2 use2-az2 | 171 | 45% | 5.0 | 9 (10-18 05:47Z) |
| us-east-2 use2-az3 | 202 | 44% | 4.9 | 9 (10-18 05:47Z) |
| us-west-2 usw2-az1 | 117 | 26% | 3.5 | 1 (10-17 13:39Z) |
| us-west-2 usw2-az2 | 70 | 24% | 3.3 | 1 (10-17 19:18Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 331 | 54% | 6.2 | 9 (10-18 05:47Z) |
| ap-northeast-1 | 331 | 74% | 7.2 | 9 (10-18 05:47Z) |
| ap-northeast-2 | 331 | 100% | 9.0 | 9 (10-18 05:47Z) |
| ap-south-1 | 331 | 62% | 6.4 | 9 (10-18 05:47Z) |
| ap-southeast-2 | 331 | 19% | 3.2 | 9 (10-18 05:47Z) |
| ap-southeast-3 | 331 | 23% | 3.3 | 2 (10-18 05:47Z) |
| us-east-1 | 331 | 71% | 6.5 | 9 (10-18 05:47Z) |
| us-east-2 | 331 | 70% | 6.9 | 9 (10-18 05:47Z) |
| us-west-2 | 331 | 52% | 5.7 | 9 (10-18 05:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   119911999999999999992399239992199911999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       919991499999999999299199912299229991299999999999
ap-southeast-2   111111189199999911111111111811111111111199999999
ap-southeast-3   111113891199979395151122111131151821438751867992
us-east-1        663546456998299999945426664355554679344659999999
us-east-2        211121211992299999911912991122911199931139999999
us-west-2        333133233999999359299442495343355433445443999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 202 | 73% | 7.4 | 9 (10-18 05:47Z) |
| ap-east-1 ape1-az2 | 168 | 76% | 7.5 | 9 (10-17 22:13Z) |
| ap-east-1 ape1-az3 | 170 | 74% | 7.4 | 9 (10-18 05:47Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 96 | 72% | 7.3 | 9 (10-18 00:55Z) |
| ap-northeast-1 apne1-az4 | 189 | 98% | 8.9 | 9 (10-18 05:47Z) |
| ap-northeast-2 apne2-az1 | 259 | 100% | 9.0 | 9 (10-18 00:55Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 285 | 100% | 9.0 | 9 (10-18 05:47Z) |
| ap-northeast-2 apne2-az4 | 197 | 76% | 7.6 | 9 (10-18 05:47Z) |
| ap-south-1 aps1-az1 | 116 | 81% | 7.9 | 9 (10-17 22:13Z) |
| ap-south-1 aps1-az2 | 119 | 70% | 7.2 | 9 (10-18 00:55Z) |
| ap-south-1 aps1-az3 | 136 | 86% | 8.2 | 9 (10-18 00:55Z) |
| ap-southeast-2 apse2-az1 | 28 | 64% | 6.8 | 9 (10-18 00:55Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 42 | 69% | 7.1 | 9 (10-18 05:47Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 83 | 100% | 9.0 | 9 (10-17 19:18Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 66 | 97% | 8.8 | 9 (10-18 00:55Z) |
| us-east-1 use1-az6 | 89 | 96% | 8.7 | 9 (10-18 05:47Z) |
| us-east-2 use2-az1 | 111 | 98% | 8.9 | 9 (10-18 05:47Z) |
| us-east-2 use2-az2 | 156 | 99% | 8.9 | 9 (10-17 22:13Z) |
| us-east-2 use2-az3 | 147 | 95% | 8.6 | 9 (10-18 05:47Z) |
| us-west-2 usw2-az1 | 76 | 97% | 8.8 | 9 (10-17 22:13Z) |
| us-west-2 usw2-az2 | 71 | 96% | 8.7 | 9 (10-18 05:47Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709500 | 2026-10-18T05:47:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-18T05:47:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.768200 | 2026-10-18T05:47:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.951200 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587500 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582000 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569000 | 2026-10-18T05:47:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741300 | 2026-10-18T05:47:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.552700 | 2026-10-18T05:47:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.388400 | 2026-10-18T05:47:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.718600 | 2026-10-18T05:47:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.348900 | 2026-10-18T05:47:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718100 | 2026-10-18T05:47:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.521300 | 2026-10-18T05:47:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.611500 | 2026-10-18T05:47:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.430200 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.532300 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.490600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.432600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.477900 | 2026-10-18T05:47:06Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549100 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2a | Windows | 0.643500 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.540300 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2b | Windows | 0.639300 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.538600 | 2026-10-18T05:47:06Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.521200 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2a | Windows | 0.314200 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.497000 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2b | Windows | 0.329900 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.492300 | 2026-10-18T05:47:06Z |
| us-west-2 | us-west-2c | Windows | 0.313800 | 2026-10-18T05:47:06Z |
