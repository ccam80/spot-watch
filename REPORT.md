# Spot placement score log

Generated 2026-10-30 15:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 453 | 48% | 5.2 | 9 (10-30 15:15Z) |
| ap-northeast-1 | 453 | 15% | 2.7 | 8 (10-30 15:15Z) |
| ap-northeast-2 | 453 | 66% | 6.9 | 9 (10-30 15:15Z) |
| ap-south-1 | 453 | 2% | 1.7 | 1 (10-30 15:15Z) |
| ap-southeast-2 | 453 | 0% | 1.0 | 1 (10-30 15:15Z) |
| ap-southeast-3 | 453 | 26% | 3.3 | 6 (10-30 15:15Z) |
| us-east-1 | 453 | 11% | 2.7 | 2 (10-30 15:15Z) |
| us-east-2 | 453 | 30% | 3.7 | 1 (10-30 15:15Z) |
| us-west-2 | 453 | 9% | 2.2 | 1 (10-30 15:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999111111199999711111122144212121999999999999999
ap-northeast-1   122223222111111111122221111122221111111111122228
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111112211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   863112111111111111111112332111111111111111111786
us-east-1        111111111111222233333233332211112333333332332222
us-east-2        111111111111111411111111111111111111289912911111
us-west-2        222222222112222221111211111122222222211122111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 146 | 6% | 1.6 | 1 (10-30 14:17Z) |
| ap-east-1 ape1-az2 | 335 | 64% | 6.6 | 9 (10-30 15:15Z) |
| ap-northeast-1 apne1-az1 | 93 | 4% | 1.4 | 1 (10-30 12:24Z) |
| ap-northeast-1 apne1-az4 | 202 | 27% | 3.5 | 6 (10-30 15:15Z) |
| ap-northeast-2 apne2-az1 | 391 | 59% | 6.4 | 9 (10-30 15:15Z) |
| ap-northeast-2 apne2-az3 | 422 | 65% | 6.8 | 9 (10-30 15:15Z) |
| ap-northeast-2 apne2-az4 | 449 | 66% | 6.9 | 9 (10-30 15:15Z) |
| ap-south-1 aps1-az1 | 129 | 1% | 1.4 | 1 (10-30 15:15Z) |
| ap-south-1 aps1-az3 | 122 | 6% | 2.5 | 1 (10-30 08:21Z) |
| ap-southeast-2 apse2-az1 | 82 | 2% | 1.2 | 1 (10-30 13:17Z) |
| ap-southeast-2 apse2-az2 | 51 | 0% | 1.0 | 1 (10-30 13:17Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 292 | 38% | 4.4 | 6 (10-30 15:15Z) |
| us-east-1 use1-az1 | 88 | 0% | 1.1 | 1 (10-30 13:17Z) |
| us-east-1 use1-az2 | 122 | 2% | 1.4 | 1 (10-30 11:13Z) |
| us-east-1 use1-az4 | 149 | 24% | 3.1 | 1 (10-30 13:17Z) |
| us-east-1 use1-az5 | 145 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 use1-az6 | 108 | 25% | 3.1 | 1 (10-30 15:15Z) |
| us-east-2 use2-az1 | 189 | 43% | 4.6 | 1 (10-30 12:24Z) |
| us-east-2 use2-az2 | 235 | 49% | 5.2 | 1 (10-30 15:15Z) |
| us-east-2 use2-az3 | 267 | 46% | 5.0 | 1 (10-30 10:16Z) |
| us-west-2 usw2-az1 | 142 | 25% | 3.4 | 1 (10-30 08:21Z) |
| us-west-2 usw2-az2 | 109 | 18% | 2.7 | 1 (10-30 13:17Z) |
| us-west-2 usw2-az3 | 182 | 17% | 2.7 | 1 (10-30 15:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 453 | 66% | 7.0 | 9 (10-30 15:15Z) |
| ap-northeast-1 | 453 | 70% | 6.9 | 9 (10-30 15:15Z) |
| ap-northeast-2 | 453 | 100% | 9.0 | 9 (10-30 15:15Z) |
| ap-south-1 | 453 | 60% | 6.2 | 1 (10-30 15:15Z) |
| ap-southeast-2 | 453 | 21% | 3.2 | 1 (10-30 15:15Z) |
| ap-southeast-3 | 453 | 26% | 3.3 | 6 (10-30 15:15Z) |
| us-east-1 | 453 | 71% | 6.4 | 2 (10-30 15:15Z) |
| us-east-2 | 453 | 68% | 6.7 | 2 (10-30 15:15Z) |
| us-west-2 | 453 | 52% | 5.6 | 4 (10-30 15:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999993111111111199999999999991111111111339999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       112999999999711111111111129999999999111111112211
ap-southeast-2   999911111111111114399999999911111111111111111111
ap-southeast-3   863112111111111111111112332111111111111111111786
us-east-1        221112224446666577995656555654546666699999999932
us-east-2        222222222252222992229912222121222224999999993222
us-west-2        554444444335599955449999334445534455593355999994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 290 | 81% | 7.9 | 9 (10-30 15:15Z) |
| ap-east-1 ape1-az2 | 251 | 84% | 8.0 | 9 (10-30 15:15Z) |
| ap-east-1 ape1-az3 | 275 | 84% | 8.0 | 9 (10-30 15:15Z) |
| ap-northeast-1 apne1-az1 | 191 | 94% | 8.6 | 9 (10-30 15:15Z) |
| ap-northeast-1 apne1-az2 | 154 | 82% | 7.9 | 9 (10-30 15:15Z) |
| ap-northeast-1 apne1-az4 | 237 | 99% | 8.9 | 9 (10-30 15:15Z) |
| ap-northeast-2 apne2-az1 | 371 | 100% | 9.0 | 9 (10-30 15:15Z) |
| ap-northeast-2 apne2-az2 | 92 | 83% | 7.9 | 8 (10-30 01:19Z) |
| ap-northeast-2 apne2-az3 | 397 | 100% | 9.0 | 9 (10-30 15:15Z) |
| ap-northeast-2 apne2-az4 | 296 | 84% | 8.0 | 9 (10-30 15:15Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 72 | 38% | 5.1 | 6 (10-30 15:15Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 97 | 100% | 9.0 | 9 (10-30 10:16Z) |
| us-east-1 use1-az4 | 127 | 91% | 8.3 | 9 (10-30 11:13Z) |
| us-east-1 use1-az5 | 95 | 98% | 8.8 | 9 (10-30 13:17Z) |
| us-east-1 use1-az6 | 114 | 91% | 8.4 | 9 (10-30 11:13Z) |
| us-east-2 use2-az1 | 158 | 99% | 8.9 | 9 (10-30 11:13Z) |
| us-east-2 use2-az2 | 185 | 99% | 8.9 | 9 (10-30 08:21Z) |
| us-east-2 use2-az3 | 205 | 96% | 8.7 | 9 (10-30 11:13Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 118 | 89% | 8.2 | 9 (10-30 14:17Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.699400 | 2026-10-30T15:15:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T15:15:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.745600 | 2026-10-30T15:15:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.935800 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585500 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589800 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571300 | 2026-10-30T15:15:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T15:15:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.602900 | 2026-10-30T15:15:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.460600 | 2026-10-30T15:15:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.572500 | 2026-10-30T15:15:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.386600 | 2026-10-30T15:15:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652500 | 2026-10-30T15:15:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517800 | 2026-10-30T15:15:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657400 | 2026-10-30T15:15:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.578100 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.542400 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524500 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516300 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.571300 | 2026-10-30T15:15:46Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.557400 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547600 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546100 | 2026-10-30T15:15:46Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559800 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2a | Windows | 0.315700 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579800 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2b | Windows | 0.323900 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.551900 | 2026-10-30T15:15:46Z |
| us-west-2 | us-west-2c | Windows | 0.315900 | 2026-10-30T15:15:46Z |
