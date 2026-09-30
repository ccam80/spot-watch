# Spot placement score log

Generated 2026-09-30 18:27 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 247 | 34% | 4.3 | 9 (09-30 18:27Z) |
| ap-northeast-1 | 247 | 9% | 2.4 | 2 (09-30 18:27Z) |
| ap-northeast-2 | 247 | 38% | 5.3 | 9 (09-30 18:27Z) |
| ap-south-1 | 247 | 2% | 1.9 | 1 (09-30 18:27Z) |
| ap-southeast-2 | 247 | 0% | 1.0 | 1 (09-30 18:27Z) |
| ap-southeast-3 | 247 | 21% | 3.3 | 1 (09-30 18:27Z) |
| us-east-1 | 247 | 8% | 2.4 | 3 (09-30 18:27Z) |
| us-east-2 | 247 | 22% | 3.2 | 1 (09-30 18:27Z) |
| us-west-2 | 247 | 9% | 2.2 | 2 (09-30 18:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999899999
ap-northeast-1   589412212221112114818821379612221222222111189912
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111112211111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   688891111111115437887681111187111111111111147651
us-east-1        121111129111112211122111112912229999132222222223
us-east-2        111111111119999999111111916999911199999991111181
us-west-2        111111122111111111122222111112111111211222222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 7 | 7 | 3 | 4 | 4 | 6 | 6 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 4 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 1 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 4 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 84 | 0% | 1.5 | 2 (09-30 17:22Z) |
| ap-east-1 ape1-az2 | 179 | 46% | 5.5 | 9 (09-30 18:27Z) |
| ap-northeast-1 apne1-az1 | 35 | 0% | 1.3 | 1 (09-30 18:27Z) |
| ap-northeast-1 apne1-az4 | 110 | 14% | 2.9 | 1 (09-30 18:27Z) |
| ap-northeast-2 apne2-az1 | 221 | 37% | 5.1 | 9 (09-30 18:27Z) |
| ap-northeast-2 apne2-az3 | 229 | 41% | 5.4 | 9 (09-30 18:27Z) |
| ap-northeast-2 apne2-az4 | 244 | 39% | 5.3 | 9 (09-30 18:27Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 96 | 3% | 2.6 | 1 (09-30 15:25Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 23 | 0% | 1.0 | 1 (09-30 18:27Z) |
| ap-southeast-3 apse3-az1 | 47 | 0% | 1.0 | 1 (09-30 16:27Z) |
| ap-southeast-3 apse3-az3 | 180 | 27% | 4.0 | 1 (09-30 18:27Z) |
| us-east-1 use1-az1 | 38 | 0% | 1.2 | 1 (09-30 13:26Z) |
| us-east-1 use1-az2 | 71 | 3% | 1.5 | 1 (09-30 17:22Z) |
| us-east-1 use1-az4 | 77 | 22% | 3.1 | 1 (09-30 14:26Z) |
| us-east-1 use1-az5 | 74 | 22% | 3.1 | 1 (09-30 16:27Z) |
| us-east-1 use1-az6 | 56 | 14% | 2.5 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 99 | 31% | 3.9 | 1 (09-30 14:26Z) |
| us-east-2 use2-az2 | 124 | 37% | 4.5 | 9 (09-30 11:20Z) |
| us-east-2 use2-az3 | 145 | 34% | 4.5 | 8 (09-30 17:22Z) |
| us-west-2 usw2-az1 | 77 | 26% | 3.7 | 1 (09-30 17:22Z) |
| us-west-2 usw2-az2 | 48 | 23% | 3.4 | 1 (09-30 18:27Z) |
| us-west-2 usw2-az3 | 105 | 17% | 2.9 | 1 (09-30 08:33Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 247 | 38% | 5.3 | 9 (09-30 18:27Z) |
| ap-northeast-1 | 247 | 74% | 7.2 | 9 (09-30 18:27Z) |
| ap-northeast-2 | 247 | 100% | 9.0 | 9 (09-30 18:27Z) |
| ap-south-1 | 247 | 56% | 6.0 | 9 (09-30 18:27Z) |
| ap-southeast-2 | 247 | 16% | 3.2 | 2 (09-30 18:27Z) |
| ap-southeast-3 | 247 | 21% | 3.3 | 1 (09-30 18:27Z) |
| us-east-1 | 247 | 73% | 6.8 | 4 (09-30 18:27Z) |
| us-east-2 | 247 | 75% | 7.3 | 9 (09-30 18:27Z) |
| us-west-2 | 247 | 54% | 5.8 | 4 (09-30 18:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999993335222333899999999999992223322344379999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999994217111529999999999999991111111111119
ap-southeast-2   322122222222222222959229221122222222222222222222
ap-southeast-3   688891111111115437887681111187111111111111147651
us-east-1        454336989579489959445443595936559999365544433344
us-east-2        322332239999999999334333999999999999999998329299
us-west-2        433224444229922449453555322435333242534554554444
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 3 | 6 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 4 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 137 | 61% | 6.6 | 9 (09-30 18:27Z) |
| ap-east-1 ape1-az2 | 108 | 62% | 6.7 | 9 (09-30 18:27Z) |
| ap-east-1 ape1-az3 | 105 | 58% | 6.5 | 9 (09-30 18:27Z) |
| ap-northeast-1 apne1-az1 | 117 | 91% | 8.5 | 9 (09-30 18:27Z) |
| ap-northeast-1 apne1-az2 | 51 | 49% | 5.9 | 9 (09-30 18:27Z) |
| ap-northeast-1 apne1-az4 | 145 | 99% | 9.0 | 9 (09-30 18:27Z) |
| ap-northeast-2 apne2-az1 | 193 | 100% | 9.0 | 9 (09-30 18:27Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 222 | 100% | 9.0 | 9 (09-30 18:27Z) |
| ap-northeast-2 apne2-az4 | 131 | 64% | 6.8 | 9 (09-30 18:27Z) |
| ap-south-1 aps1-az1 | 72 | 69% | 7.2 | 9 (09-30 04:28Z) |
| ap-south-1 aps1-az2 | 86 | 58% | 6.5 | 7 (09-30 18:27Z) |
| ap-south-1 aps1-az3 | 95 | 81% | 7.9 | 9 (09-30 04:28Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 52 | 21% | 4.2 | 4 (09-30 14:26Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 90 | 97% | 8.8 | 2 (09-30 08:33Z) |
| us-east-1 use1-az5 | 51 | 98% | 8.9 | 9 (09-30 06:39Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 94 | 99% | 8.9 | 9 (09-30 11:20Z) |
| us-east-2 use2-az2 | 131 | 98% | 8.9 | 9 (09-30 15:25Z) |
| us-east-2 use2-az3 | 121 | 93% | 8.6 | 9 (09-30 11:20Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 59 | 95% | 8.6 | 2 (09-30 12:38Z) |
| us-west-2 usw2-az3 | 75 | 95% | 8.6 | 2 (09-30 13:26Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.731100 | 2026-09-30T18:27:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.852600 | 2026-09-30T18:27:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.777000 | 2026-09-30T18:27:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964300 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.576900 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566200 | 2026-09-30T18:27:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-09-30T18:27:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.617600 | 2026-09-30T18:27:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.352800 | 2026-09-30T18:27:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.654100 | 2026-09-30T18:27:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.349100 | 2026-09-30T18:27:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729100 | 2026-09-30T18:27:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-09-30T18:27:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.613900 | 2026-09-30T18:27:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.584900 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1a | Windows | 0.303200 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.450800 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.452500 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.397800 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438800 | 2026-09-30T18:27:46Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529400 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2a | Windows | 0.640700 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523200 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2b | Windows | 0.640500 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514500 | 2026-09-30T18:27:46Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.511800 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.503500 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-30T18:27:46Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-30T18:27:46Z |
