# Spot placement score log

Generated 2026-10-16 20:59 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 322 | 37% | 4.5 | 9 (10-16 20:58Z) |
| ap-northeast-1 | 322 | 15% | 2.7 | 2 (10-16 20:58Z) |
| ap-northeast-2 | 322 | 52% | 6.1 | 9 (10-16 20:58Z) |
| ap-south-1 | 322 | 2% | 1.8 | 2 (10-16 20:58Z) |
| ap-southeast-2 | 322 | 0% | 1.0 | 1 (10-16 20:58Z) |
| ap-southeast-3 | 322 | 22% | 3.3 | 8 (10-16 20:58Z) |
| us-east-1 | 322 | 9% | 2.5 | 2 (10-16 20:58Z) |
| us-east-2 | 322 | 28% | 3.6 | 1 (10-16 20:58Z) |
| us-west-2 | 322 | 11% | 2.3 | 2 (10-16 20:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111822929999999999999999999999999
ap-northeast-1   111151197111111911122221192212121114221142111132
ap-northeast-2   999999999999999991999999999999999999999999999999
ap-south-1       222222222111221111112222222222111112222222111222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111388111113891199979395151122111131151821438
us-east-1        111121111222113232333192233222113333232132312222
us-east-2        118111111111111111181199999911112991112911199911
us-west-2        211212111111111111999911111111111111111122111122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 8 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 114 | 8% | 1.8 | 1 (10-16 20:58Z) |
| ap-east-1 ape1-az2 | 227 | 52% | 5.8 | 9 (10-16 20:58Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 152 | 25% | 3.5 | 2 (10-16 17:21Z) |
| ap-northeast-2 apne2-az1 | 282 | 49% | 5.8 | 4 (10-16 20:58Z) |
| ap-northeast-2 apne2-az3 | 294 | 52% | 6.0 | 9 (10-16 20:58Z) |
| ap-northeast-2 apne2-az4 | 319 | 52% | 6.1 | 9 (10-16 20:58Z) |
| ap-south-1 aps1-az1 | 83 | 1% | 1.6 | 1 (10-14 18:31Z) |
| ap-south-1 aps1-az3 | 111 | 3% | 2.3 | 1 (10-16 17:21Z) |
| ap-southeast-2 apse2-az1 | 51 | 0% | 1.1 | 1 (10-15 18:13Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 67 | 0% | 1.0 | 1 (10-16 20:58Z) |
| ap-southeast-3 apse3-az3 | 216 | 31% | 4.2 | 8 (10-16 20:58Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 89 | 3% | 1.5 | 1 (10-16 20:58Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 101 | 24% | 3.2 | 1 (10-16 17:21Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 127 | 39% | 4.5 | 9 (10-16 07:03Z) |
| us-east-2 use2-az2 | 164 | 45% | 4.9 | 1 (10-16 20:58Z) |
| us-east-2 use2-az3 | 195 | 43% | 4.9 | 1 (10-16 17:21Z) |
| us-west-2 usw2-az1 | 114 | 27% | 3.6 | 1 (10-16 20:58Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 322 | 52% | 6.1 | 9 (10-16 20:58Z) |
| ap-northeast-1 | 322 | 73% | 7.1 | 9 (10-16 20:58Z) |
| ap-northeast-2 | 322 | 100% | 9.0 | 9 (10-16 20:58Z) |
| ap-south-1 | 322 | 61% | 6.3 | 9 (10-16 20:58Z) |
| ap-southeast-2 | 322 | 17% | 3.1 | 1 (10-16 20:58Z) |
| ap-southeast-3 | 322 | 22% | 3.3 | 8 (10-16 20:58Z) |
| us-east-1 | 322 | 70% | 6.5 | 4 (10-16 20:58Z) |
| us-east-2 | 322 | 70% | 6.9 | 1 (10-16 20:58Z) |
| us-west-2 | 322 | 52% | 5.7 | 5 (10-16 20:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   923991399119911999999999999992399239992199911999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992999299919991499999999999299199912299229991299
ap-southeast-2   111111191111111189199999911111111111811111111111
ap-southeast-3   111111388111113891199979395151122111131151821438
us-east-1        545334333663546456998299999945426664355554679344
us-east-2        399332121211121211992299999911912991122911199931
us-west-2        323544132333133233999999359299442495343355433445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 196 | 72% | 7.3 | 9 (10-16 20:58Z) |
| ap-east-1 ape1-az2 | 165 | 75% | 7.5 | 9 (10-16 20:58Z) |
| ap-east-1 ape1-az3 | 165 | 73% | 7.4 | 9 (10-16 12:19Z) |
| ap-northeast-1 apne1-az1 | 152 | 93% | 8.5 | 9 (10-16 20:58Z) |
| ap-northeast-1 apne1-az2 | 92 | 71% | 7.2 | 9 (10-16 17:21Z) |
| ap-northeast-1 apne1-az4 | 183 | 98% | 8.9 | 9 (10-16 20:58Z) |
| ap-northeast-2 apne2-az1 | 254 | 100% | 9.0 | 9 (10-16 20:58Z) |
| ap-northeast-2 apne2-az2 | 70 | 79% | 7.6 | 9 (10-16 17:21Z) |
| ap-northeast-2 apne2-az3 | 277 | 100% | 9.0 | 9 (10-16 20:58Z) |
| ap-northeast-2 apne2-az4 | 191 | 75% | 7.5 | 9 (10-16 20:58Z) |
| ap-south-1 aps1-az1 | 113 | 81% | 7.8 | 9 (10-16 20:58Z) |
| ap-south-1 aps1-az2 | 115 | 69% | 7.1 | 9 (10-16 20:58Z) |
| ap-south-1 aps1-az3 | 132 | 86% | 8.1 | 9 (10-16 20:58Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 63 | 30% | 4.7 | 4 (10-16 12:19Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 81 | 100% | 9.0 | 9 (10-16 07:03Z) |
| us-east-1 use1-az4 | 103 | 94% | 8.6 | 9 (10-16 07:03Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 84 | 95% | 8.7 | 9 (10-16 07:03Z) |
| us-east-2 use2-az1 | 107 | 98% | 8.9 | 9 (10-15 07:20Z) |
| us-east-2 use2-az2 | 154 | 99% | 8.9 | 9 (10-16 07:03Z) |
| us-east-2 use2-az3 | 144 | 94% | 8.6 | 7 (10-16 12:19Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711100 | 2026-10-16T20:58:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-16T20:58:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.755700 | 2026-10-16T20:58:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.936600 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588000 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.583200 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570700 | 2026-10-16T20:58:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741400 | 2026-10-16T20:58:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.551300 | 2026-10-16T20:58:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.375200 | 2026-10-16T20:58:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.693500 | 2026-10-16T20:58:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.328300 | 2026-10-16T20:58:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.720200 | 2026-10-16T20:58:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.520400 | 2026-10-16T20:58:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.566200 | 2026-10-16T20:58:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.581700 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.444900 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.510300 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.472100 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.411900 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.463800 | 2026-10-16T20:58:58Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.546400 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2a | Windows | 0.643700 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.537100 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2b | Windows | 0.640300 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.534200 | 2026-10-16T20:58:58Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.525500 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2a | Windows | 0.314900 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499300 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2b | Windows | 0.330400 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.496100 | 2026-10-16T20:58:58Z |
| us-west-2 | us-west-2c | Windows | 0.314600 | 2026-10-16T20:58:58Z |
