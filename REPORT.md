# Spot placement score log

Generated 2026-10-30 13:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 451 | 48% | 5.2 | 9 (10-30 13:17Z) |
| ap-northeast-1 | 451 | 14% | 2.7 | 2 (10-30 13:17Z) |
| ap-northeast-2 | 451 | 65% | 6.9 | 9 (10-30 13:17Z) |
| ap-south-1 | 451 | 2% | 1.7 | 2 (10-30 13:17Z) |
| ap-southeast-2 | 451 | 0% | 1.0 | 1 (10-30 13:17Z) |
| ap-southeast-3 | 451 | 25% | 3.3 | 7 (10-30 13:17Z) |
| us-east-1 | 451 | 11% | 2.7 | 2 (10-30 13:17Z) |
| us-east-2 | 451 | 30% | 3.7 | 1 (10-30 13:17Z) |
| us-west-2 | 451 | 10% | 2.2 | 1 (10-30 13:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999991111111999997111111221442121219999999999999
ap-northeast-1   121222232221111111111222211111222211111111111222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111122
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   888631121111111111111111123321111111111111111117
us-east-1        311111111111112222333332333322111123333333323322
us-east-2        111111111111111114111111111111111111112899129111
us-west-2        222222222221122222211112111111222222222111221111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 145 | 6% | 1.6 | 1 (10-30 12:24Z) |
| ap-east-1 ape1-az2 | 333 | 64% | 6.6 | 9 (10-30 13:17Z) |
| ap-northeast-1 apne1-az1 | 93 | 4% | 1.4 | 1 (10-30 12:24Z) |
| ap-northeast-1 apne1-az4 | 201 | 26% | 3.5 | 1 (10-30 10:16Z) |
| ap-northeast-2 apne2-az1 | 389 | 59% | 6.3 | 9 (10-30 09:18Z) |
| ap-northeast-2 apne2-az3 | 420 | 65% | 6.8 | 9 (10-30 13:17Z) |
| ap-northeast-2 apne2-az4 | 447 | 66% | 6.9 | 9 (10-30 13:17Z) |
| ap-south-1 aps1-az1 | 127 | 1% | 1.4 | 1 (10-30 13:17Z) |
| ap-south-1 aps1-az3 | 122 | 6% | 2.5 | 1 (10-30 08:21Z) |
| ap-southeast-2 apse2-az1 | 82 | 2% | 1.2 | 1 (10-30 13:17Z) |
| ap-southeast-2 apse2-az2 | 51 | 0% | 1.0 | 1 (10-30 13:17Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 290 | 38% | 4.4 | 7 (10-30 13:17Z) |
| us-east-1 use1-az1 | 88 | 0% | 1.1 | 1 (10-30 13:17Z) |
| us-east-1 use1-az2 | 122 | 2% | 1.4 | 1 (10-30 11:13Z) |
| us-east-1 use1-az4 | 149 | 24% | 3.1 | 1 (10-30 13:17Z) |
| us-east-1 use1-az5 | 145 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 use1-az6 | 106 | 25% | 3.2 | 1 (10-30 11:13Z) |
| us-east-2 use2-az1 | 189 | 43% | 4.6 | 1 (10-30 12:24Z) |
| us-east-2 use2-az2 | 233 | 50% | 5.2 | 9 (10-30 10:16Z) |
| us-east-2 use2-az3 | 267 | 46% | 5.0 | 1 (10-30 10:16Z) |
| us-west-2 usw2-az1 | 142 | 25% | 3.4 | 1 (10-30 08:21Z) |
| us-west-2 usw2-az2 | 109 | 18% | 2.7 | 1 (10-30 13:17Z) |
| us-west-2 usw2-az3 | 180 | 17% | 2.8 | 1 (10-30 12:24Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 451 | 66% | 7.0 | 9 (10-30 13:17Z) |
| ap-northeast-1 | 451 | 70% | 6.9 | 9 (10-30 13:17Z) |
| ap-northeast-2 | 451 | 100% | 9.0 | 9 (10-30 13:17Z) |
| ap-south-1 | 451 | 61% | 6.2 | 2 (10-30 13:17Z) |
| ap-southeast-2 | 451 | 21% | 3.3 | 1 (10-30 13:17Z) |
| ap-southeast-3 | 451 | 25% | 3.3 | 7 (10-30 13:17Z) |
| us-east-1 | 451 | 71% | 6.4 | 9 (10-30 13:17Z) |
| us-east-2 | 451 | 68% | 6.7 | 2 (10-30 13:17Z) |
| us-west-2 | 451 | 52% | 5.6 | 9 (10-30 13:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999931111111111999999999999911111111113399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111129999999997111111111111299999999991111111122
ap-southeast-2   999999111111111111143999999999111111111111111111
ap-southeast-3   888631121111111111111111123321111111111111111117
us-east-1        522211122244466665779956565556545466666999999999
us-east-2        122222222222522229922299122221212222249999999932
us-west-2        595544444443355999554499993344455344555933559999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 288 | 81% | 7.9 | 9 (10-30 13:17Z) |
| ap-east-1 ape1-az2 | 249 | 84% | 8.0 | 9 (10-30 13:17Z) |
| ap-east-1 ape1-az3 | 273 | 84% | 8.0 | 9 (10-30 13:17Z) |
| ap-northeast-1 apne1-az1 | 189 | 94% | 8.6 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az2 | 152 | 82% | 7.9 | 9 (10-30 13:17Z) |
| ap-northeast-1 apne1-az4 | 235 | 99% | 8.9 | 9 (10-30 13:17Z) |
| ap-northeast-2 apne2-az1 | 369 | 100% | 9.0 | 9 (10-30 13:17Z) |
| ap-northeast-2 apne2-az2 | 92 | 83% | 7.9 | 8 (10-30 01:19Z) |
| ap-northeast-2 apne2-az3 | 395 | 100% | 9.0 | 9 (10-30 13:17Z) |
| ap-northeast-2 apne2-az4 | 294 | 84% | 8.0 | 9 (10-30 13:17Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
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
| us-west-2 usw2-az3 | 117 | 89% | 8.2 | 9 (10-30 13:17Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.699400 | 2026-10-30T13:17:07Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T13:17:07Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.745600 | 2026-10-30T13:17:07Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.935800 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585500 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589800 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571300 | 2026-10-30T13:17:07Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T13:17:07Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.602900 | 2026-10-30T13:17:07Z |
| ap-south-1 | ap-south-1a | Windows | 0.460600 | 2026-10-30T13:17:07Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.572500 | 2026-10-30T13:17:07Z |
| ap-south-1 | ap-south-1b | Windows | 0.386600 | 2026-10-30T13:17:07Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-30T13:17:07Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517800 | 2026-10-30T13:17:07Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657400 | 2026-10-30T13:17:07Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.580200 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.542400 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.525000 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.517900 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.571500 | 2026-10-30T13:17:07Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.557400 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547600 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546100 | 2026-10-30T13:17:07Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559800 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2a | Windows | 0.315700 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579800 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2b | Windows | 0.323900 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.551900 | 2026-10-30T13:17:07Z |
| us-west-2 | us-west-2c | Windows | 0.315900 | 2026-10-30T13:17:07Z |
