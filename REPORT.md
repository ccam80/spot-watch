# Spot placement score log

Generated 2026-10-30 18:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 456 | 48% | 5.2 | 1 (10-30 18:16Z) |
| ap-northeast-1 | 456 | 15% | 2.7 | 1 (10-30 18:16Z) |
| ap-northeast-2 | 456 | 66% | 6.9 | 9 (10-30 18:16Z) |
| ap-south-1 | 456 | 2% | 1.7 | 2 (10-30 18:16Z) |
| ap-southeast-2 | 456 | 0% | 1.0 | 1 (10-30 18:16Z) |
| ap-southeast-3 | 456 | 26% | 3.3 | 1 (10-30 18:16Z) |
| us-east-1 | 456 | 11% | 2.7 | 2 (10-30 18:16Z) |
| us-east-2 | 456 | 30% | 3.6 | 1 (10-30 18:16Z) |
| us-west-2 | 456 | 9% | 2.2 | 1 (10-30 18:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111199999711111122144212121999999999999999991
ap-northeast-1   223222111111111122221111122221111111111122228711
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111112211112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   112111111111111111112332111111111111111111786751
us-east-1        111111111222233333233332211112333333332332222222
us-east-2        111111111111411111111111111111111289912911111111
us-west-2        222222112222221111211111122222222211122111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 146 | 6% | 1.6 | 1 (10-30 14:17Z) |
| ap-east-1 ape1-az2 | 338 | 64% | 6.6 | 1 (10-30 18:16Z) |
| ap-northeast-1 apne1-az1 | 95 | 4% | 1.4 | 1 (10-30 18:16Z) |
| ap-northeast-1 apne1-az4 | 203 | 27% | 3.6 | 4 (10-30 16:17Z) |
| ap-northeast-2 apne2-az1 | 394 | 59% | 6.4 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az3 | 425 | 66% | 6.8 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az4 | 452 | 66% | 7.0 | 9 (10-30 18:16Z) |
| ap-south-1 aps1-az1 | 130 | 1% | 1.4 | 1 (10-30 17:12Z) |
| ap-south-1 aps1-az3 | 122 | 6% | 2.5 | 1 (10-30 08:21Z) |
| ap-southeast-2 apse2-az1 | 85 | 2% | 1.2 | 1 (10-30 18:16Z) |
| ap-southeast-2 apse2-az2 | 52 | 0% | 1.0 | 1 (10-30 17:12Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 295 | 39% | 4.4 | 1 (10-30 18:16Z) |
| us-east-1 use1-az1 | 89 | 0% | 1.1 | 1 (10-30 17:12Z) |
| us-east-1 use1-az2 | 122 | 2% | 1.4 | 1 (10-30 11:13Z) |
| us-east-1 use1-az4 | 150 | 24% | 3.1 | 1 (10-30 17:12Z) |
| us-east-1 use1-az5 | 146 | 26% | 3.3 | 1 (10-30 18:16Z) |
| us-east-1 use1-az6 | 108 | 25% | 3.1 | 1 (10-30 15:15Z) |
| us-east-2 use2-az1 | 189 | 43% | 4.6 | 1 (10-30 12:24Z) |
| us-east-2 use2-az2 | 235 | 49% | 5.2 | 1 (10-30 15:15Z) |
| us-east-2 use2-az3 | 269 | 46% | 5.0 | 1 (10-30 18:16Z) |
| us-west-2 usw2-az1 | 142 | 25% | 3.4 | 1 (10-30 08:21Z) |
| us-west-2 usw2-az2 | 111 | 18% | 2.7 | 1 (10-30 18:16Z) |
| us-west-2 usw2-az3 | 182 | 17% | 2.7 | 1 (10-30 15:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 456 | 66% | 7.0 | 9 (10-30 18:16Z) |
| ap-northeast-1 | 456 | 70% | 6.9 | 9 (10-30 18:16Z) |
| ap-northeast-2 | 456 | 100% | 9.0 | 9 (10-30 18:16Z) |
| ap-south-1 | 456 | 60% | 6.2 | 2 (10-30 18:16Z) |
| ap-southeast-2 | 456 | 21% | 3.2 | 1 (10-30 18:16Z) |
| ap-southeast-3 | 456 | 26% | 3.3 | 1 (10-30 18:16Z) |
| us-east-1 | 456 | 70% | 6.4 | 3 (10-30 18:16Z) |
| us-east-2 | 456 | 67% | 6.6 | 2 (10-30 18:16Z) |
| us-west-2 | 456 | 52% | 5.6 | 4 (10-30 18:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999993111111111199999999999991111111111339999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999711111111111129999999999111111112211112
ap-southeast-2   911111111111114399999999911111111111111111111111
ap-southeast-3   112111111111111111112332111111111111111111786751
us-east-1        112224446666577995656555654546666699999999932323
us-east-2        222222252222992229912222121222224999999993222222
us-west-2        444444335599955449999334445534455593355999994844
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 293 | 82% | 7.9 | 9 (10-30 18:16Z) |
| ap-east-1 ape1-az2 | 254 | 84% | 8.0 | 9 (10-30 18:16Z) |
| ap-east-1 ape1-az3 | 278 | 84% | 8.1 | 9 (10-30 18:16Z) |
| ap-northeast-1 apne1-az1 | 194 | 94% | 8.6 | 9 (10-30 18:16Z) |
| ap-northeast-1 apne1-az2 | 157 | 83% | 7.9 | 9 (10-30 18:16Z) |
| ap-northeast-1 apne1-az4 | 240 | 99% | 8.9 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az1 | 374 | 100% | 9.0 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az2 | 94 | 83% | 7.9 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az3 | 400 | 100% | 9.0 | 9 (10-30 18:16Z) |
| ap-northeast-2 apne2-az4 | 299 | 84% | 8.1 | 9 (10-30 18:16Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.699400 | 2026-10-30T18:16:15Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T18:16:15Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.745600 | 2026-10-30T18:16:15Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.928100 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585900 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589800 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571700 | 2026-10-30T18:16:15Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T18:16:15Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.616700 | 2026-10-30T18:16:15Z |
| ap-south-1 | ap-south-1a | Windows | 0.460600 | 2026-10-30T18:16:15Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.572500 | 2026-10-30T18:16:15Z |
| ap-south-1 | ap-south-1b | Windows | 0.384700 | 2026-10-30T18:16:15Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652500 | 2026-10-30T18:16:15Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515500 | 2026-10-30T18:16:15Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656800 | 2026-10-30T18:16:15Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.578100 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.542400 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524500 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516300 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.568800 | 2026-10-30T18:16:15Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.557400 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547800 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546000 | 2026-10-30T18:16:15Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559800 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2a | Windows | 0.315700 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.574400 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2b | Windows | 0.323500 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547300 | 2026-10-30T18:16:15Z |
| us-west-2 | us-west-2c | Windows | 0.315900 | 2026-10-30T18:16:15Z |
