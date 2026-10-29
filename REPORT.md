# Spot placement score log

Generated 2026-10-29 11:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 425 | 48% | 5.2 | 1 (10-29 11:15Z) |
| ap-northeast-1 | 425 | 15% | 2.7 | 2 (10-29 11:15Z) |
| ap-northeast-2 | 425 | 63% | 6.8 | 9 (10-29 11:15Z) |
| ap-south-1 | 425 | 3% | 1.8 | 1 (10-29 11:15Z) |
| ap-southeast-2 | 425 | 0% | 1.0 | 1 (10-29 11:15Z) |
| ap-southeast-3 | 425 | 27% | 3.4 | 1 (10-29 11:15Z) |
| us-east-1 | 425 | 11% | 2.7 | 3 (10-29 11:15Z) |
| us-east-2 | 425 | 31% | 3.8 | 1 (10-29 11:15Z) |
| us-west-2 | 425 | 10% | 2.2 | 1 (10-29 11:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999991111119999999999999911111119999971111
ap-northeast-1   221131222222111111111112111212222322211111111112
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   711186488541111111111111568886311211111111111111
us-east-1        219233222333111221112233333111111111111122223333
us-east-2        111961119999111911199991111111111111111111141111
us-west-2        212111111111111111211112222222222222211222222111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 6 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 3 | 4 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 137 | 7% | 1.6 | 1 (10-29 11:15Z) |
| ap-east-1 ape1-az2 | 315 | 64% | 6.5 | 7 (10-29 07:18Z) |
| ap-northeast-1 apne1-az1 | 80 | 5% | 1.5 | 1 (10-29 10:16Z) |
| ap-northeast-1 apne1-az4 | 193 | 27% | 3.6 | 1 (10-29 11:15Z) |
| ap-northeast-2 apne2-az1 | 369 | 56% | 6.2 | 9 (10-29 09:18Z) |
| ap-northeast-2 apne2-az3 | 394 | 63% | 6.7 | 9 (10-29 11:15Z) |
| ap-northeast-2 apne2-az4 | 421 | 64% | 6.8 | 9 (10-29 11:15Z) |
| ap-south-1 aps1-az1 | 113 | 1% | 1.4 | 1 (10-29 11:15Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 74 | 3% | 1.3 | 1 (10-29 10:16Z) |
| ap-southeast-2 apse2-az2 | 45 | 0% | 1.0 | 1 (10-29 08:21Z) |
| ap-southeast-3 apse3-az1 | 79 | 0% | 1.0 | 1 (10-29 09:18Z) |
| ap-southeast-3 apse3-az3 | 278 | 39% | 4.5 | 1 (10-29 10:16Z) |
| us-east-1 use1-az1 | 81 | 0% | 1.1 | 1 (10-29 10:16Z) |
| us-east-1 use1-az2 | 114 | 3% | 1.4 | 1 (10-29 11:15Z) |
| us-east-1 use1-az4 | 135 | 27% | 3.3 | 1 (10-29 10:16Z) |
| us-east-1 use1-az5 | 137 | 28% | 3.4 | 1 (10-29 11:15Z) |
| us-east-1 use1-az6 | 102 | 26% | 3.2 | 1 (10-29 10:16Z) |
| us-east-2 use2-az1 | 175 | 45% | 4.8 | 1 (10-29 10:16Z) |
| us-east-2 use2-az2 | 225 | 50% | 5.3 | 1 (10-29 11:15Z) |
| us-east-2 use2-az3 | 257 | 47% | 5.2 | 1 (10-29 11:15Z) |
| us-west-2 usw2-az1 | 139 | 26% | 3.4 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az2 | 100 | 20% | 2.8 | 1 (10-29 10:16Z) |
| us-west-2 usw2-az3 | 166 | 19% | 2.9 | 1 (10-29 11:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 425 | 64% | 6.8 | 9 (10-29 11:15Z) |
| ap-northeast-1 | 425 | 71% | 6.9 | 9 (10-29 11:15Z) |
| ap-northeast-2 | 425 | 100% | 9.0 | 9 (10-29 11:15Z) |
| ap-south-1 | 425 | 62% | 6.3 | 1 (10-29 11:15Z) |
| ap-southeast-2 | 425 | 21% | 3.2 | 9 (10-29 11:15Z) |
| ap-southeast-3 | 425 | 27% | 3.4 | 1 (10-29 11:15Z) |
| us-east-1 | 425 | 70% | 6.4 | 9 (10-29 11:15Z) |
| us-east-2 | 425 | 70% | 6.8 | 2 (10-29 11:15Z) |
| us-west-2 | 425 | 51% | 5.6 | 4 (10-29 11:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   991199999999221111112227999999999999311111111119
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       991121199999999991111111111111299999999971111111
ap-southeast-2   111111991111111111111999999999991111111111111439
ap-southeast-3   711186488541111111111111568886311211111111111111
us-east-1        439955445766996965445965435222111222444666657799
us-east-2        999999999999999999999999991222222222225222299222
us-west-2        445911333334333333559439945955444444433559995544
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 6 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 269 | 80% | 7.8 | 9 (10-29 11:15Z) |
| ap-east-1 ape1-az2 | 228 | 82% | 7.9 | 9 (10-29 11:15Z) |
| ap-east-1 ape1-az3 | 247 | 82% | 7.9 | 9 (10-29 11:15Z) |
| ap-northeast-1 apne1-az1 | 182 | 94% | 8.6 | 9 (10-28 22:15Z) |
| ap-northeast-1 apne1-az2 | 138 | 80% | 7.8 | 8 (10-29 11:15Z) |
| ap-northeast-1 apne1-az4 | 228 | 99% | 8.9 | 9 (10-28 22:15Z) |
| ap-northeast-2 apne2-az1 | 345 | 100% | 9.0 | 9 (10-29 11:15Z) |
| ap-northeast-2 apne2-az2 | 87 | 82% | 7.8 | 9 (10-29 01:18Z) |
| ap-northeast-2 apne2-az3 | 369 | 100% | 9.0 | 9 (10-29 11:15Z) |
| ap-northeast-2 apne2-az4 | 271 | 83% | 8.0 | 9 (10-29 11:15Z) |
| ap-south-1 aps1-az1 | 146 | 85% | 8.1 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az2 | 158 | 77% | 7.5 | 2 (10-29 04:19Z) |
| ap-south-1 aps1-az3 | 170 | 88% | 8.3 | 3 (10-29 04:19Z) |
| ap-southeast-2 apse2-az1 | 45 | 78% | 7.6 | 9 (10-29 11:15Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 52 | 75% | 7.5 | 9 (10-28 16:18Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 120 | 91% | 8.4 | 2 (10-29 10:16Z) |
| us-east-1 use1-az5 | 88 | 98% | 8.8 | 9 (10-29 11:15Z) |
| us-east-1 use1-az6 | 108 | 92% | 8.4 | 7 (10-29 11:15Z) |
| us-east-2 use2-az1 | 151 | 99% | 8.9 | 9 (10-29 08:21Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 196 | 96% | 8.7 | 9 (10-29 08:21Z) |
| us-west-2 usw2-az1 | 87 | 98% | 8.8 | 9 (10-29 07:18Z) |
| us-west-2 usw2-az2 | 81 | 93% | 8.5 | 2 (10-29 06:26Z) |
| us-west-2 usw2-az3 | 110 | 89% | 8.2 | 2 (10-29 09:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702700 | 2026-10-29T11:15:18Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T11:15:18Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764200 | 2026-10-29T11:15:18Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.962300 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585200 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.587200 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-29T11:15:18Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-29T11:15:18Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.587400 | 2026-10-29T11:15:18Z |
| ap-south-1 | ap-south-1a | Windows | 0.459300 | 2026-10-29T11:15:18Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.603600 | 2026-10-29T11:15:18Z |
| ap-south-1 | ap-south-1b | Windows | 0.394700 | 2026-10-29T11:15:18Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-29T11:15:18Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522300 | 2026-10-29T11:15:18Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-29T11:15:18Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559100 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.584400 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.510500 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.528600 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516800 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.564200 | 2026-10-29T11:15:18Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.566600 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2a | Windows | 0.638600 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548700 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547700 | 2026-10-29T11:15:18Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563700 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2a | Windows | 0.318000 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.587400 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2b | Windows | 0.325900 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.560400 | 2026-10-29T11:15:18Z |
| us-west-2 | us-west-2c | Windows | 0.318000 | 2026-10-29T11:15:18Z |
