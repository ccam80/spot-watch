# Spot placement score log

Generated 2026-10-31 06:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 468 | 47% | 5.2 | 1 (10-31 06:19Z) |
| ap-northeast-1 | 468 | 14% | 2.6 | 1 (10-31 06:19Z) |
| ap-northeast-2 | 468 | 66% | 6.9 | 1 (10-31 06:19Z) |
| ap-south-1 | 468 | 2% | 1.7 | 1 (10-31 06:19Z) |
| ap-southeast-2 | 468 | 0% | 1.0 | 1 (10-31 06:19Z) |
| ap-southeast-3 | 468 | 25% | 3.3 | 1 (10-31 06:19Z) |
| us-east-1 | 468 | 10% | 2.6 | 2 (10-31 06:19Z) |
| us-east-2 | 468 | 29% | 3.6 | 1 (10-31 06:19Z) |
| us-west-2 | 468 | 9% | 2.1 | 1 (10-31 06:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        711111122144212121999999999999999991111119991111
ap-northeast-1   111122221111122221111111111122228711112421114421
ap-northeast-2   999999999999999999999999999999999999999999999911
ap-south-1       111111111111111111111111111112211112111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111112332111111111111111111786751111111111111
us-east-1        233333233332211112333333332332222222221112222222
us-east-2        411111111111111111111289912911111111111111111111
us-west-2        221111211111122222222211122111111111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 154 | 6% | 1.6 | 1 (10-31 06:19Z) |
| ap-east-1 ape1-az2 | 343 | 64% | 6.6 | 9 (10-31 02:17Z) |
| ap-northeast-1 apne1-az1 | 98 | 4% | 1.4 | 1 (10-31 02:17Z) |
| ap-northeast-1 apne1-az4 | 212 | 25% | 3.5 | 1 (10-31 06:19Z) |
| ap-northeast-2 apne2-az1 | 403 | 60% | 6.4 | 9 (10-31 03:15Z) |
| ap-northeast-2 apne2-az3 | 435 | 66% | 6.9 | 8 (10-31 04:15Z) |
| ap-northeast-2 apne2-az4 | 462 | 67% | 7.0 | 9 (10-31 04:15Z) |
| ap-south-1 aps1-az1 | 133 | 1% | 1.4 | 1 (10-31 06:19Z) |
| ap-south-1 aps1-az3 | 126 | 6% | 2.4 | 1 (10-31 05:13Z) |
| ap-southeast-2 apse2-az1 | 87 | 2% | 1.2 | 1 (10-31 02:17Z) |
| ap-southeast-2 apse2-az2 | 56 | 0% | 1.0 | 1 (10-31 04:15Z) |
| ap-southeast-3 apse3-az1 | 84 | 0% | 1.0 | 1 (10-31 06:19Z) |
| ap-southeast-3 apse3-az3 | 296 | 39% | 4.4 | 1 (10-30 23:11Z) |
| us-east-1 use1-az1 | 94 | 0% | 1.1 | 1 (10-31 06:19Z) |
| us-east-1 use1-az2 | 127 | 2% | 1.4 | 1 (10-31 06:19Z) |
| us-east-1 use1-az4 | 154 | 23% | 3.0 | 1 (10-31 05:13Z) |
| us-east-1 use1-az5 | 151 | 25% | 3.2 | 1 (10-31 00:33Z) |
| us-east-1 use1-az6 | 113 | 24% | 3.0 | 1 (10-31 06:19Z) |
| us-east-2 use2-az1 | 195 | 42% | 4.5 | 1 (10-31 06:19Z) |
| us-east-2 use2-az2 | 239 | 49% | 5.1 | 1 (10-31 06:19Z) |
| us-east-2 use2-az3 | 271 | 45% | 5.0 | 1 (10-30 22:12Z) |
| us-west-2 usw2-az1 | 146 | 25% | 3.3 | 1 (10-31 00:33Z) |
| us-west-2 usw2-az2 | 114 | 18% | 2.6 | 1 (10-31 02:17Z) |
| us-west-2 usw2-az3 | 187 | 17% | 2.7 | 1 (10-31 06:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 468 | 67% | 7.0 | 9 (10-31 06:19Z) |
| ap-northeast-1 | 468 | 71% | 6.9 | 9 (10-31 06:19Z) |
| ap-northeast-2 | 468 | 100% | 9.0 | 9 (10-31 06:19Z) |
| ap-south-1 | 468 | 61% | 6.2 | 9 (10-31 06:19Z) |
| ap-southeast-2 | 468 | 22% | 3.3 | 9 (10-31 06:19Z) |
| ap-southeast-3 | 468 | 25% | 3.3 | 1 (10-31 06:19Z) |
| us-east-1 | 468 | 69% | 6.3 | 9 (10-31 06:19Z) |
| us-east-2 | 468 | 66% | 6.6 | 9 (10-31 06:19Z) |
| us-west-2 | 468 | 51% | 5.6 | 3 (10-31 06:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111199999999999991111111111339999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111129999999999111111112211112999999999999
ap-southeast-2   114399999999911111111111111111111111111119999999
ap-southeast-3   111111112332111111111111111111786751111111111111
us-east-1        577995656555654546666699999999932323334339394399
us-east-2        992229912222121222224999999993222222222222228999
us-west-2        955449999334445534455593355999994844395931211233
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 301 | 82% | 7.9 | 9 (10-31 04:15Z) |
| ap-east-1 ape1-az2 | 260 | 84% | 8.1 | 9 (10-31 06:19Z) |
| ap-east-1 ape1-az3 | 289 | 85% | 8.1 | 9 (10-31 06:19Z) |
| ap-northeast-1 apne1-az1 | 199 | 94% | 8.6 | 9 (10-31 05:13Z) |
| ap-northeast-1 apne1-az2 | 166 | 84% | 8.0 | 9 (10-31 04:15Z) |
| ap-northeast-1 apne1-az4 | 250 | 99% | 8.9 | 9 (10-31 05:13Z) |
| ap-northeast-2 apne2-az1 | 385 | 100% | 9.0 | 9 (10-31 06:19Z) |
| ap-northeast-2 apne2-az2 | 98 | 84% | 7.9 | 9 (10-31 05:13Z) |
| ap-northeast-2 apne2-az3 | 410 | 100% | 9.0 | 9 (10-31 06:19Z) |
| ap-northeast-2 apne2-az4 | 307 | 85% | 8.1 | 9 (10-31 06:19Z) |
| ap-south-1 aps1-az1 | 162 | 86% | 8.2 | 9 (10-31 05:13Z) |
| ap-south-1 aps1-az2 | 176 | 79% | 7.7 | 9 (10-31 06:19Z) |
| ap-south-1 aps1-az3 | 179 | 89% | 8.3 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az1 | 54 | 81% | 7.9 | 9 (10-31 04:15Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 63 | 79% | 7.7 | 9 (10-31 06:19Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 98 | 100% | 9.0 | 9 (10-31 05:13Z) |
| us-east-1 use1-az4 | 128 | 91% | 8.3 | 9 (10-31 06:19Z) |
| us-east-1 use1-az5 | 95 | 98% | 8.8 | 9 (10-30 13:17Z) |
| us-east-1 use1-az6 | 115 | 91% | 8.4 | 9 (10-31 05:13Z) |
| us-east-2 use2-az1 | 160 | 99% | 8.9 | 9 (10-31 05:13Z) |
| us-east-2 use2-az2 | 186 | 99% | 8.9 | 9 (10-31 06:19Z) |
| us-east-2 use2-az3 | 207 | 96% | 8.7 | 9 (10-31 06:19Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 119 | 89% | 8.2 | 9 (10-30 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700500 | 2026-10-31T06:19:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T06:19:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742700 | 2026-10-31T06:19:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.896300 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584400 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590800 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572200 | 2026-10-31T06:19:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T06:19:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.624100 | 2026-10-31T06:19:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T06:19:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.544800 | 2026-10-31T06:19:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.382700 | 2026-10-31T06:19:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652100 | 2026-10-31T06:19:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515500 | 2026-10-31T06:19:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655900 | 2026-10-31T06:19:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.571800 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.556100 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.515700 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.505900 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558300 | 2026-10-31T06:19:46Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554800 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547300 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2b | Windows | 0.637300 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T06:19:46Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556200 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2a | Windows | 0.314700 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572400 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2b | Windows | 0.323000 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.545300 | 2026-10-31T06:19:46Z |
| us-west-2 | us-west-2c | Windows | 0.314400 | 2026-10-31T06:19:46Z |
