# Spot placement score log

Generated 2026-10-19 01:08 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 337 | 40% | 4.7 | 9 (10-19 01:08Z) |
| ap-northeast-1 | 337 | 15% | 2.8 | 2 (10-19 01:08Z) |
| ap-northeast-2 | 337 | 54% | 6.2 | 9 (10-19 01:08Z) |
| ap-south-1 | 337 | 2% | 1.8 | 2 (10-19 01:08Z) |
| ap-southeast-2 | 337 | 1% | 1.1 | 1 (10-19 01:08Z) |
| ap-southeast-3 | 337 | 24% | 3.4 | 1 (10-19 01:08Z) |
| us-east-1 | 337 | 10% | 2.6 | 9 (10-19 01:08Z) |
| us-east-2 | 337 | 30% | 3.7 | 9 (10-19 01:08Z) |
| us-west-2 | 337 | 11% | 2.3 | 1 (10-19 01:08Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111822929999999999999999999999999999999999999999
ap-northeast-1   911122221192212121114221142111132212932416591222
ap-northeast-2   991999999999999999999999999999999999999999999999
ap-south-1       111112222222222111112222222111222222222222222222
ap-southeast-2   111111111111111111111111111111111119119111111111
ap-southeast-3   891199979395151122111131151821438751867992474881
us-east-1        232333192233222113333232132312222233322192399999
us-east-2        111181199999911112991112911199911116199999919999
us-west-2        111999911111111111111111122111122211212121911921
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 242 | 55% | 6.0 | 9 (10-19 01:08Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 157 | 25% | 3.6 | 8 (10-18 14:30Z) |
| ap-northeast-2 apne2-az1 | 293 | 50% | 5.8 | 6 (10-18 18:01Z) |
| ap-northeast-2 apne2-az3 | 309 | 54% | 6.2 | 8 (10-19 01:08Z) |
| ap-northeast-2 apne2-az4 | 334 | 54% | 6.2 | 9 (10-19 01:08Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 227 | 33% | 4.3 | 8 (10-18 23:02Z) |
| us-east-1 use1-az1 | 64 | 0% | 1.1 | 1 (10-18 05:47Z) |
| us-east-1 use1-az2 | 93 | 3% | 1.5 | 2 (10-18 14:30Z) |
| us-east-1 use1-az4 | 104 | 31% | 3.7 | 9 (10-19 01:08Z) |
| us-east-1 use1-az5 | 109 | 28% | 3.4 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 135 | 42% | 4.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az2 | 176 | 47% | 5.1 | 9 (10-19 01:08Z) |
| us-east-2 use2-az3 | 207 | 45% | 5.0 | 9 (10-19 01:08Z) |
| us-west-2 usw2-az1 | 120 | 28% | 3.6 | 1 (10-19 01:08Z) |
| us-west-2 usw2-az2 | 71 | 25% | 3.4 | 9 (10-18 10:55Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 337 | 55% | 6.3 | 9 (10-19 01:08Z) |
| ap-northeast-1 | 337 | 74% | 7.2 | 3 (10-19 01:08Z) |
| ap-northeast-2 | 337 | 100% | 9.0 | 9 (10-19 01:08Z) |
| ap-south-1 | 337 | 62% | 6.5 | 9 (10-19 01:08Z) |
| ap-southeast-2 | 337 | 20% | 3.3 | 1 (10-19 01:08Z) |
| ap-southeast-3 | 337 | 24% | 3.4 | 1 (10-19 01:08Z) |
| us-east-1 | 337 | 72% | 6.6 | 9 (10-19 01:08Z) |
| us-east-2 | 337 | 71% | 6.9 | 9 (10-19 01:08Z) |
| us-west-2 | 337 | 53% | 5.8 | 9 (10-19 01:08Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999992399239992199911999999999999999993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       499999999999299199912299229991299999999999999999
ap-southeast-2   189199999911111111111811111111111199999999999911
ap-southeast-3   891199979395151122111131151821438751867992474881
us-east-1        456998299999945426664355554679344659999999999999
us-east-2        211992299999911912991122911199931139999999999999
us-west-2        233999999359299442495343355433445443999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 206 | 74% | 7.4 | 9 (10-19 01:08Z) |
| ap-east-1 ape1-az2 | 170 | 76% | 7.6 | 9 (10-18 18:01Z) |
| ap-east-1 ape1-az3 | 172 | 74% | 7.5 | 9 (10-19 01:08Z) |
| ap-northeast-1 apne1-az1 | 155 | 93% | 8.5 | 9 (10-18 23:02Z) |
| ap-northeast-1 apne1-az2 | 98 | 72% | 7.3 | 9 (10-18 18:01Z) |
| ap-northeast-1 apne1-az4 | 192 | 98% | 8.9 | 9 (10-18 23:02Z) |
| ap-northeast-2 apne2-az1 | 262 | 100% | 9.0 | 9 (10-19 01:08Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 290 | 100% | 9.0 | 9 (10-19 01:08Z) |
| ap-northeast-2 apne2-az4 | 200 | 76% | 7.6 | 9 (10-18 23:02Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 122 | 70% | 7.2 | 9 (10-19 01:08Z) |
| ap-south-1 aps1-az3 | 138 | 86% | 8.2 | 9 (10-19 01:08Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 43 | 70% | 7.1 | 9 (10-18 14:30Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 114 | 98% | 8.9 | 9 (10-19 01:08Z) |
| us-east-2 use2-az2 | 158 | 99% | 8.9 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 151 | 95% | 8.6 | 9 (10-19 01:08Z) |
| us-west-2 usw2-az1 | 78 | 97% | 8.8 | 9 (10-18 18:01Z) |
| us-west-2 usw2-az2 | 73 | 96% | 8.7 | 9 (10-18 23:02Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709100 | 2026-10-19T01:08:19Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-19T01:08:19Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.763200 | 2026-10-19T01:08:19Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.946200 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585400 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581700 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567300 | 2026-10-19T01:08:19Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741200 | 2026-10-19T01:08:19Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.550900 | 2026-10-19T01:08:19Z |
| ap-south-1 | ap-south-1a | Windows | 0.389200 | 2026-10-19T01:08:19Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.712200 | 2026-10-19T01:08:19Z |
| ap-south-1 | ap-south-1b | Windows | 0.357500 | 2026-10-19T01:08:19Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.708300 | 2026-10-19T01:08:19Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.516500 | 2026-10-19T01:08:19Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.644100 | 2026-10-19T01:08:19Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.563800 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.430200 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.531700 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.506700 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.438900 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.488700 | 2026-10-19T01:08:19Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550100 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2a | Windows | 0.643400 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.542500 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2b | Windows | 0.639300 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.539900 | 2026-10-19T01:08:19Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.526700 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2a | Windows | 0.315100 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.505200 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2b | Windows | 0.330300 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494000 | 2026-10-19T01:08:19Z |
| us-west-2 | us-west-2c | Windows | 0.314700 | 2026-10-19T01:08:19Z |
