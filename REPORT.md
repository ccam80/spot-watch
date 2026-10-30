# Spot placement score log

Generated 2026-10-30 08:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 446 | 47% | 5.1 | 9 (10-30 08:21Z) |
| ap-northeast-1 | 446 | 15% | 2.7 | 1 (10-30 08:21Z) |
| ap-northeast-2 | 446 | 65% | 6.9 | 9 (10-30 08:21Z) |
| ap-south-1 | 446 | 2% | 1.7 | 1 (10-30 08:21Z) |
| ap-southeast-2 | 446 | 0% | 1.0 | 1 (10-30 08:21Z) |
| ap-southeast-3 | 446 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 | 446 | 11% | 2.7 | 3 (10-30 08:21Z) |
| us-east-2 | 446 | 30% | 3.7 | 1 (10-30 08:21Z) |
| us-west-2 | 446 | 10% | 2.2 | 2 (10-30 08:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999911111119999971111112214421212199999999
ap-northeast-1   112111212222322211111111112222111112222111111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111568886311211111111111111111233211111111111111
us-east-1        233333111111111111122223333323333221111233333333
us-east-2        991111111111111111111141111111111111111111128991
us-west-2        112222222222222211222222111121111112222222221112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 144 | 6% | 1.6 | 1 (10-30 08:21Z) |
| ap-east-1 ape1-az2 | 328 | 64% | 6.5 | 9 (10-30 08:21Z) |
| ap-northeast-1 apne1-az1 | 91 | 4% | 1.5 | 1 (10-30 04:19Z) |
| ap-northeast-1 apne1-az4 | 200 | 26% | 3.5 | 1 (10-30 08:21Z) |
| ap-northeast-2 apne2-az1 | 388 | 59% | 6.3 | 9 (10-30 08:21Z) |
| ap-northeast-2 apne2-az3 | 415 | 65% | 6.8 | 9 (10-30 08:21Z) |
| ap-northeast-2 apne2-az4 | 442 | 65% | 6.9 | 9 (10-30 08:21Z) |
| ap-south-1 aps1-az1 | 123 | 1% | 1.4 | 1 (10-30 07:17Z) |
| ap-south-1 aps1-az3 | 122 | 6% | 2.5 | 1 (10-30 08:21Z) |
| ap-southeast-2 apse2-az1 | 81 | 2% | 1.2 | 1 (10-30 04:19Z) |
| ap-southeast-2 apse2-az2 | 49 | 0% | 1.0 | 1 (10-30 08:21Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 287 | 38% | 4.4 | 1 (10-30 03:19Z) |
| us-east-1 use1-az1 | 86 | 0% | 1.1 | 1 (10-30 06:26Z) |
| us-east-1 use1-az2 | 120 | 2% | 1.4 | 1 (10-30 07:17Z) |
| us-east-1 use1-az4 | 145 | 25% | 3.1 | 1 (10-30 06:26Z) |
| us-east-1 use1-az5 | 145 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 use1-az6 | 105 | 26% | 3.2 | 1 (10-30 02:22Z) |
| us-east-2 use2-az1 | 185 | 43% | 4.7 | 9 (10-30 07:17Z) |
| us-east-2 use2-az2 | 232 | 50% | 5.2 | 9 (10-30 07:17Z) |
| us-east-2 use2-az3 | 266 | 46% | 5.0 | 8 (10-30 07:17Z) |
| us-west-2 usw2-az1 | 142 | 25% | 3.4 | 1 (10-30 08:21Z) |
| us-west-2 usw2-az2 | 108 | 19% | 2.7 | 1 (10-30 04:19Z) |
| us-west-2 usw2-az3 | 176 | 18% | 2.8 | 1 (10-30 07:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 446 | 66% | 6.9 | 9 (10-30 08:21Z) |
| ap-northeast-1 | 446 | 70% | 6.9 | 1 (10-30 08:21Z) |
| ap-northeast-2 | 446 | 100% | 9.0 | 9 (10-30 08:21Z) |
| ap-south-1 | 446 | 61% | 6.3 | 1 (10-30 08:21Z) |
| ap-southeast-2 | 446 | 22% | 3.3 | 1 (10-30 08:21Z) |
| ap-southeast-3 | 446 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 | 446 | 71% | 6.4 | 9 (10-30 08:21Z) |
| us-east-2 | 446 | 68% | 6.7 | 9 (10-30 08:21Z) |
| us-west-2 | 446 | 51% | 5.6 | 5 (10-30 08:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   227999999999999311111111119999999999999111111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111299999999971111111111112999999999911111
ap-southeast-2   999999999991111111111111439999999991111111111111
ap-southeast-3   111568886311211111111111111111233211111111111111
us-east-1        965435222111222444666657799565655565454666669999
us-east-2        999991222222222225222299222991222212122222499999
us-west-2        439945955444444433559995544999933444553445559335
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 283 | 81% | 7.9 | 9 (10-30 08:21Z) |
| ap-east-1 ape1-az2 | 247 | 83% | 8.0 | 9 (10-30 08:21Z) |
| ap-east-1 ape1-az3 | 268 | 84% | 8.0 | 9 (10-30 08:21Z) |
| ap-northeast-1 apne1-az1 | 189 | 94% | 8.6 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az2 | 150 | 82% | 7.9 | 9 (10-29 23:14Z) |
| ap-northeast-1 apne1-az4 | 234 | 99% | 8.9 | 9 (10-29 23:14Z) |
| ap-northeast-2 apne2-az1 | 364 | 100% | 9.0 | 9 (10-30 08:21Z) |
| ap-northeast-2 apne2-az2 | 92 | 83% | 7.9 | 8 (10-30 01:19Z) |
| ap-northeast-2 apne2-az3 | 390 | 100% | 9.0 | 9 (10-30 08:21Z) |
| ap-northeast-2 apne2-az4 | 291 | 84% | 8.0 | 9 (10-30 08:21Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 96 | 100% | 9.0 | 9 (10-30 06:26Z) |
| us-east-1 use1-az4 | 124 | 90% | 8.3 | 9 (10-30 08:21Z) |
| us-east-1 use1-az5 | 90 | 98% | 8.8 | 9 (10-30 07:17Z) |
| us-east-1 use1-az6 | 111 | 91% | 8.4 | 9 (10-30 08:21Z) |
| us-east-2 use2-az1 | 155 | 99% | 8.9 | 9 (10-30 07:17Z) |
| us-east-2 use2-az2 | 185 | 99% | 8.9 | 9 (10-30 08:21Z) |
| us-east-2 use2-az3 | 202 | 96% | 8.7 | 9 (10-30 08:21Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 84 | 89% | 8.2 | 2 (10-30 03:19Z) |
| us-west-2 usw2-az3 | 114 | 89% | 8.2 | 2 (10-30 04:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.699800 | 2026-10-30T08:21:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T08:21:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.745600 | 2026-10-30T08:21:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947900 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585500 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589200 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571300 | 2026-10-30T08:21:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T08:21:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.592100 | 2026-10-30T08:21:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.464400 | 2026-10-30T08:21:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.574800 | 2026-10-30T08:21:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.386600 | 2026-10-30T08:21:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653000 | 2026-10-30T08:21:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517800 | 2026-10-30T08:21:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-30T08:21:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559200 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.580200 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.532300 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.525000 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520300 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.572800 | 2026-10-30T08:21:24Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554700 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547100 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-30T08:21:24Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.560500 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2a | Windows | 0.316800 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579800 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2b | Windows | 0.323900 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.555100 | 2026-10-30T08:21:24Z |
| us-west-2 | us-west-2c | Windows | 0.316400 | 2026-10-30T08:21:24Z |
