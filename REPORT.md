# Spot placement score log

Generated 2026-10-29 12:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 426 | 47% | 5.2 | 1 (10-29 12:24Z) |
| ap-northeast-1 | 426 | 15% | 2.7 | 2 (10-29 12:24Z) |
| ap-northeast-2 | 426 | 63% | 6.8 | 9 (10-29 12:24Z) |
| ap-south-1 | 426 | 3% | 1.7 | 1 (10-29 12:24Z) |
| ap-southeast-2 | 426 | 0% | 1.0 | 1 (10-29 12:24Z) |
| ap-southeast-3 | 426 | 27% | 3.4 | 1 (10-29 12:24Z) |
| us-east-1 | 426 | 11% | 2.7 | 3 (10-29 12:24Z) |
| us-east-2 | 426 | 31% | 3.8 | 1 (10-29 12:24Z) |
| us-west-2 | 426 | 10% | 2.2 | 1 (10-29 12:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999911111199999999999999111111199999711111
ap-northeast-1   211312222221111111111121112122223222111111111122
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111864885411111111111115688863112111111111111111
us-east-1        192332223331112211122333331111111111111222233333
us-east-2        119611199991119111999911111111111111111111411111
us-west-2        121111111111111112111122222222222222112222221111
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
| ap-east-1 ape1-az1 | 138 | 7% | 1.6 | 1 (10-29 12:24Z) |
| ap-east-1 ape1-az2 | 315 | 64% | 6.5 | 7 (10-29 07:18Z) |
| ap-northeast-1 apne1-az1 | 81 | 5% | 1.5 | 1 (10-29 12:24Z) |
| ap-northeast-1 apne1-az4 | 193 | 27% | 3.6 | 1 (10-29 11:15Z) |
| ap-northeast-2 apne2-az1 | 369 | 56% | 6.2 | 9 (10-29 09:18Z) |
| ap-northeast-2 apne2-az3 | 395 | 63% | 6.7 | 9 (10-29 12:24Z) |
| ap-northeast-2 apne2-az4 | 422 | 64% | 6.8 | 9 (10-29 12:24Z) |
| ap-south-1 aps1-az1 | 114 | 1% | 1.4 | 1 (10-29 12:24Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 74 | 3% | 1.3 | 1 (10-29 10:16Z) |
| ap-southeast-2 apse2-az2 | 45 | 0% | 1.0 | 1 (10-29 08:21Z) |
| ap-southeast-3 apse3-az1 | 79 | 0% | 1.0 | 1 (10-29 09:18Z) |
| ap-southeast-3 apse3-az3 | 279 | 39% | 4.5 | 1 (10-29 12:24Z) |
| us-east-1 use1-az1 | 81 | 0% | 1.1 | 1 (10-29 10:16Z) |
| us-east-1 use1-az2 | 114 | 3% | 1.4 | 1 (10-29 11:15Z) |
| us-east-1 use1-az4 | 136 | 26% | 3.3 | 1 (10-29 12:24Z) |
| us-east-1 use1-az5 | 138 | 28% | 3.4 | 1 (10-29 12:24Z) |
| us-east-1 use1-az6 | 102 | 26% | 3.2 | 1 (10-29 10:16Z) |
| us-east-2 use2-az1 | 176 | 44% | 4.8 | 1 (10-29 12:24Z) |
| us-east-2 use2-az2 | 225 | 50% | 5.3 | 1 (10-29 11:15Z) |
| us-east-2 use2-az3 | 257 | 47% | 5.2 | 1 (10-29 11:15Z) |
| us-west-2 usw2-az1 | 139 | 26% | 3.4 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az2 | 100 | 20% | 2.8 | 1 (10-29 10:16Z) |
| us-west-2 usw2-az3 | 167 | 19% | 2.9 | 1 (10-29 12:24Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 426 | 64% | 6.8 | 9 (10-29 12:24Z) |
| ap-northeast-1 | 426 | 71% | 7.0 | 9 (10-29 12:24Z) |
| ap-northeast-2 | 426 | 100% | 9.0 | 9 (10-29 12:24Z) |
| ap-south-1 | 426 | 62% | 6.3 | 1 (10-29 12:24Z) |
| ap-southeast-2 | 426 | 21% | 3.3 | 9 (10-29 12:24Z) |
| ap-southeast-3 | 426 | 27% | 3.4 | 1 (10-29 12:24Z) |
| us-east-1 | 426 | 70% | 6.4 | 5 (10-29 12:24Z) |
| us-east-2 | 426 | 70% | 6.8 | 9 (10-29 12:24Z) |
| us-west-2 | 426 | 51% | 5.6 | 9 (10-29 12:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   911999999992211111122279999999999993111111111199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911211999999999911111111111112999999999711111111
ap-southeast-2   111119911111111111119999999999911111111111114399
ap-southeast-3   111864885411111111111115688863112111111111111111
us-east-1        399554457669969654459654352221112224446666577995
us-east-2        999999999999999999999999912222222222252222992229
us-west-2        459113333343333335594399459554444444335599955449
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
| ap-east-1 ape1-az2 | 229 | 82% | 7.9 | 9 (10-29 12:24Z) |
| ap-east-1 ape1-az3 | 248 | 82% | 7.9 | 9 (10-29 12:24Z) |
| ap-northeast-1 apne1-az1 | 182 | 94% | 8.6 | 9 (10-28 22:15Z) |
| ap-northeast-1 apne1-az2 | 139 | 81% | 7.8 | 9 (10-29 12:24Z) |
| ap-northeast-1 apne1-az4 | 228 | 99% | 8.9 | 9 (10-28 22:15Z) |
| ap-northeast-2 apne2-az1 | 345 | 100% | 9.0 | 9 (10-29 11:15Z) |
| ap-northeast-2 apne2-az2 | 87 | 82% | 7.8 | 9 (10-29 01:18Z) |
| ap-northeast-2 apne2-az3 | 370 | 100% | 9.0 | 9 (10-29 12:24Z) |
| ap-northeast-2 apne2-az4 | 272 | 83% | 8.0 | 9 (10-29 12:24Z) |
| ap-south-1 aps1-az1 | 146 | 85% | 8.1 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az2 | 158 | 77% | 7.5 | 2 (10-29 04:19Z) |
| ap-south-1 aps1-az3 | 170 | 88% | 8.3 | 3 (10-29 04:19Z) |
| ap-southeast-2 apse2-az1 | 46 | 78% | 7.7 | 9 (10-29 12:24Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 53 | 75% | 7.5 | 9 (10-29 12:24Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 120 | 91% | 8.4 | 2 (10-29 10:16Z) |
| us-east-1 use1-az5 | 88 | 98% | 8.8 | 9 (10-29 11:15Z) |
| us-east-1 use1-az6 | 108 | 92% | 8.4 | 7 (10-29 11:15Z) |
| us-east-2 use2-az1 | 152 | 99% | 8.9 | 9 (10-29 12:24Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 197 | 96% | 8.7 | 9 (10-29 12:24Z) |
| us-west-2 usw2-az1 | 87 | 98% | 8.8 | 9 (10-29 07:18Z) |
| us-west-2 usw2-az2 | 81 | 93% | 8.5 | 2 (10-29 06:26Z) |
| us-west-2 usw2-az3 | 111 | 89% | 8.2 | 9 (10-29 12:24Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702700 | 2026-10-29T12:24:26Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T12:24:26Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764200 | 2026-10-29T12:24:26Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.962300 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585200 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.587200 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-29T12:24:26Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-29T12:24:26Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.587400 | 2026-10-29T12:24:26Z |
| ap-south-1 | ap-south-1a | Windows | 0.459300 | 2026-10-29T12:24:26Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.603600 | 2026-10-29T12:24:26Z |
| ap-south-1 | ap-south-1b | Windows | 0.394700 | 2026-10-29T12:24:26Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-29T12:24:26Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522300 | 2026-10-29T12:24:26Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-29T12:24:26Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559100 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.584400 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.510500 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.528600 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516800 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.564200 | 2026-10-29T12:24:26Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.566600 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2a | Windows | 0.638600 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548700 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547700 | 2026-10-29T12:24:26Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563700 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2a | Windows | 0.318000 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.587400 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2b | Windows | 0.325900 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.560400 | 2026-10-29T12:24:26Z |
| us-west-2 | us-west-2c | Windows | 0.317700 | 2026-10-29T12:24:26Z |
