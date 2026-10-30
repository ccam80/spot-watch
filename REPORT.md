# Spot placement score log

Generated 2026-10-30 03:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 441 | 46% | 5.1 | 9 (10-30 03:19Z) |
| ap-northeast-1 | 441 | 15% | 2.7 | 1 (10-30 03:19Z) |
| ap-northeast-2 | 441 | 65% | 6.9 | 9 (10-30 03:19Z) |
| ap-south-1 | 441 | 2% | 1.7 | 1 (10-30 03:19Z) |
| ap-southeast-2 | 441 | 0% | 1.0 | 1 (10-30 03:19Z) |
| ap-southeast-3 | 441 | 26% | 3.4 | 1 (10-30 03:19Z) |
| us-east-1 | 441 | 11% | 2.7 | 3 (10-30 03:19Z) |
| us-east-2 | 441 | 30% | 3.7 | 1 (10-30 03:19Z) |
| us-west-2 | 441 | 10% | 2.2 | 2 (10-30 03:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199999999999999111111199999711111122144212121999
ap-northeast-1   111111121112122223222111111111122221111122221111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111115688863112111111111111111112332111111111
us-east-1        211122333331111111111111222233333233332211112333
us-east-2        111999911111111111111111111411111111111111111111
us-west-2        112111122222222222222112222221111211111122222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 6 | 7 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 143 | 6% | 1.6 | 1 (10-29 21:15Z) |
| ap-east-1 ape1-az2 | 323 | 63% | 6.5 | 9 (10-30 03:19Z) |
| ap-northeast-1 apne1-az1 | 90 | 4% | 1.5 | 1 (10-30 03:19Z) |
| ap-northeast-1 apne1-az4 | 198 | 27% | 3.6 | 1 (10-29 21:15Z) |
| ap-northeast-2 apne2-az1 | 383 | 58% | 6.3 | 9 (10-30 03:19Z) |
| ap-northeast-2 apne2-az3 | 410 | 64% | 6.8 | 9 (10-30 03:19Z) |
| ap-northeast-2 apne2-az4 | 437 | 65% | 6.9 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az1 | 122 | 1% | 1.4 | 1 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 80 | 2% | 1.2 | 1 (10-30 01:19Z) |
| ap-southeast-2 apse2-az2 | 47 | 0% | 1.0 | 1 (10-30 02:22Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 287 | 38% | 4.4 | 1 (10-30 03:19Z) |
| us-east-1 use1-az1 | 84 | 0% | 1.1 | 1 (10-30 01:19Z) |
| us-east-1 use1-az2 | 118 | 3% | 1.4 | 1 (10-30 02:22Z) |
| us-east-1 use1-az4 | 143 | 25% | 3.2 | 1 (10-30 03:19Z) |
| us-east-1 use1-az5 | 143 | 27% | 3.3 | 1 (10-30 00:41Z) |
| us-east-1 use1-az6 | 105 | 26% | 3.2 | 1 (10-30 02:22Z) |
| us-east-2 use2-az1 | 182 | 43% | 4.6 | 1 (10-30 03:19Z) |
| us-east-2 use2-az2 | 229 | 49% | 5.2 | 1 (10-29 21:15Z) |
| us-east-2 use2-az3 | 263 | 46% | 5.1 | 1 (10-30 00:41Z) |
| us-west-2 usw2-az1 | 140 | 26% | 3.4 | 1 (10-29 20:16Z) |
| us-west-2 usw2-az2 | 107 | 19% | 2.7 | 1 (10-30 01:19Z) |
| us-west-2 usw2-az3 | 175 | 18% | 2.8 | 1 (10-30 03:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 441 | 65% | 6.9 | 9 (10-30 03:19Z) |
| ap-northeast-1 | 441 | 71% | 6.9 | 1 (10-30 03:19Z) |
| ap-northeast-2 | 441 | 100% | 9.0 | 9 (10-30 03:19Z) |
| ap-south-1 | 441 | 62% | 6.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 | 441 | 22% | 3.3 | 1 (10-30 03:19Z) |
| ap-southeast-3 | 441 | 26% | 3.4 | 1 (10-30 03:19Z) |
| us-east-1 | 441 | 70% | 6.4 | 6 (10-30 03:19Z) |
| us-east-2 | 441 | 68% | 6.7 | 4 (10-30 03:19Z) |
| us-west-2 | 441 | 51% | 5.6 | 5 (10-30 03:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111122279999999999993111111111199999999999991111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911111111111112999999999711111111111129999999999
ap-southeast-2   111119999999999911111111111114399999999911111111
ap-southeast-3   111111115688863112111111111111111112332111111111
us-east-1        654459654352221112224446666577995656555654546666
us-east-2        999999999912222222222252222992229912222121222224
us-west-2        335594399459554444444335599955449999334445534455
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 279 | 81% | 7.8 | 9 (10-30 03:19Z) |
| ap-east-1 ape1-az2 | 243 | 83% | 8.0 | 9 (10-30 03:19Z) |
| ap-east-1 ape1-az3 | 263 | 83% | 8.0 | 9 (10-30 03:19Z) |
| ap-northeast-1 apne1-az1 | 189 | 94% | 8.6 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az2 | 150 | 82% | 7.9 | 9 (10-29 23:14Z) |
| ap-northeast-1 apne1-az4 | 234 | 99% | 8.9 | 9 (10-29 23:14Z) |
| ap-northeast-2 apne2-az1 | 359 | 100% | 9.0 | 9 (10-30 03:19Z) |
| ap-northeast-2 apne2-az2 | 92 | 83% | 7.9 | 8 (10-30 01:19Z) |
| ap-northeast-2 apne2-az3 | 385 | 100% | 9.0 | 9 (10-30 03:19Z) |
| ap-northeast-2 apne2-az4 | 286 | 84% | 8.0 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 120 | 91% | 8.4 | 2 (10-29 10:16Z) |
| us-east-1 use1-az5 | 88 | 98% | 8.8 | 9 (10-29 11:15Z) |
| us-east-1 use1-az6 | 108 | 92% | 8.4 | 7 (10-29 11:15Z) |
| us-east-2 use2-az1 | 152 | 99% | 8.9 | 9 (10-29 12:24Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 198 | 96% | 8.7 | 9 (10-29 13:17Z) |
| us-west-2 usw2-az1 | 88 | 98% | 8.8 | 9 (10-29 14:17Z) |
| us-west-2 usw2-az2 | 84 | 89% | 8.2 | 2 (10-30 03:19Z) |
| us-west-2 usw2-az3 | 113 | 89% | 8.3 | 9 (10-29 15:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700200 | 2026-10-30T03:19:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T03:19:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.760400 | 2026-10-30T03:19:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947900 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585500 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589200 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571000 | 2026-10-30T03:19:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T03:19:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.592100 | 2026-10-30T03:19:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.461900 | 2026-10-30T03:19:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.588200 | 2026-10-30T03:19:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.389900 | 2026-10-30T03:19:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-30T03:19:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.521300 | 2026-10-30T03:19:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-30T03:19:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559200 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.572800 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.531300 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.526500 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.522000 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.572800 | 2026-10-30T03:19:35Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.556500 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547100 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-30T03:19:35Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561000 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2a | Windows | 0.317400 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.582800 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2b | Windows | 0.324400 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.555500 | 2026-10-30T03:19:35Z |
| us-west-2 | us-west-2c | Windows | 0.316800 | 2026-10-30T03:19:35Z |
