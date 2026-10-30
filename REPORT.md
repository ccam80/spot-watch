# Spot placement score log

Generated 2026-10-30 10:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 448 | 47% | 5.2 | 9 (10-30 10:16Z) |
| ap-northeast-1 | 448 | 15% | 2.7 | 1 (10-30 10:16Z) |
| ap-northeast-2 | 448 | 65% | 6.9 | 9 (10-30 10:16Z) |
| ap-south-1 | 448 | 2% | 1.7 | 1 (10-30 10:16Z) |
| ap-southeast-2 | 448 | 0% | 1.0 | 1 (10-30 10:16Z) |
| ap-southeast-3 | 448 | 25% | 3.3 | 1 (10-30 10:16Z) |
| us-east-1 | 448 | 11% | 2.7 | 3 (10-30 10:16Z) |
| us-east-2 | 448 | 30% | 3.7 | 9 (10-30 10:16Z) |
| us-west-2 | 448 | 10% | 2.2 | 1 (10-30 10:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991111111999997111111221442121219999999999
ap-northeast-1   211121222232221111111111222211111222211111111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   156888631121111111111111111123321111111111111111
us-east-1        333311111111111112222333332333322111123333333323
us-east-2        111111111111111111114111111111111111111112899129
us-west-2        222222222222221122222211112111111222222222111221
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
| ap-east-1 ape1-az2 | 330 | 64% | 6.5 | 9 (10-30 10:16Z) |
| ap-northeast-1 apne1-az1 | 92 | 4% | 1.4 | 1 (10-30 09:18Z) |
| ap-northeast-1 apne1-az4 | 201 | 26% | 3.5 | 1 (10-30 10:16Z) |
| ap-northeast-2 apne2-az1 | 389 | 59% | 6.3 | 9 (10-30 09:18Z) |
| ap-northeast-2 apne2-az3 | 417 | 65% | 6.8 | 9 (10-30 10:16Z) |
| ap-northeast-2 apne2-az4 | 444 | 66% | 6.9 | 9 (10-30 10:16Z) |
| ap-south-1 aps1-az1 | 125 | 1% | 1.4 | 1 (10-30 10:16Z) |
| ap-south-1 aps1-az3 | 122 | 6% | 2.5 | 1 (10-30 08:21Z) |
| ap-southeast-2 apse2-az1 | 81 | 2% | 1.2 | 1 (10-30 04:19Z) |
| ap-southeast-2 apse2-az2 | 49 | 0% | 1.0 | 1 (10-30 08:21Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 288 | 38% | 4.4 | 1 (10-30 09:18Z) |
| us-east-1 use1-az1 | 86 | 0% | 1.1 | 1 (10-30 06:26Z) |
| us-east-1 use1-az2 | 121 | 2% | 1.4 | 1 (10-30 10:16Z) |
| us-east-1 use1-az4 | 146 | 25% | 3.1 | 1 (10-30 09:18Z) |
| us-east-1 use1-az5 | 145 | 26% | 3.3 | 1 (10-30 08:21Z) |
| us-east-1 use1-az6 | 105 | 26% | 3.2 | 1 (10-30 02:22Z) |
| us-east-2 use2-az1 | 187 | 43% | 4.7 | 9 (10-30 10:16Z) |
| us-east-2 use2-az2 | 233 | 50% | 5.2 | 9 (10-30 10:16Z) |
| us-east-2 use2-az3 | 267 | 46% | 5.0 | 1 (10-30 10:16Z) |
| us-west-2 usw2-az1 | 142 | 25% | 3.4 | 1 (10-30 08:21Z) |
| us-west-2 usw2-az2 | 108 | 19% | 2.7 | 1 (10-30 04:19Z) |
| us-west-2 usw2-az3 | 178 | 17% | 2.8 | 1 (10-30 10:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 448 | 66% | 7.0 | 9 (10-30 10:16Z) |
| ap-northeast-1 | 448 | 70% | 6.9 | 3 (10-30 10:16Z) |
| ap-northeast-2 | 448 | 100% | 9.0 | 9 (10-30 10:16Z) |
| ap-south-1 | 448 | 61% | 6.2 | 1 (10-30 10:16Z) |
| ap-southeast-2 | 448 | 21% | 3.3 | 1 (10-30 10:16Z) |
| ap-southeast-3 | 448 | 25% | 3.3 | 1 (10-30 10:16Z) |
| us-east-1 | 448 | 71% | 6.4 | 9 (10-30 10:16Z) |
| us-east-2 | 448 | 68% | 6.7 | 9 (10-30 10:16Z) |
| us-west-2 | 448 | 51% | 5.6 | 9 (10-30 10:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   799999999999931111111111999999999999911111111113
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111129999999997111111111111299999999991111111
ap-southeast-2   999999999111111111111143999999999111111111111111
ap-southeast-3   156888631121111111111111111123321111111111111111
us-east-1        543522211122244466665779956565556545466666999999
us-east-2        999122222222222522229922299122221212222249999999
us-west-2        994595544444443355999554499993344455344555933559
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 285 | 81% | 7.9 | 9 (10-30 10:16Z) |
| ap-east-1 ape1-az2 | 247 | 83% | 8.0 | 9 (10-30 08:21Z) |
| ap-east-1 ape1-az3 | 270 | 84% | 8.0 | 9 (10-30 10:16Z) |
| ap-northeast-1 apne1-az1 | 189 | 94% | 8.6 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az2 | 150 | 82% | 7.9 | 9 (10-29 23:14Z) |
| ap-northeast-1 apne1-az4 | 234 | 99% | 8.9 | 9 (10-29 23:14Z) |
| ap-northeast-2 apne2-az1 | 366 | 100% | 9.0 | 9 (10-30 10:16Z) |
| ap-northeast-2 apne2-az2 | 92 | 83% | 7.9 | 8 (10-30 01:19Z) |
| ap-northeast-2 apne2-az3 | 392 | 100% | 9.0 | 9 (10-30 10:16Z) |
| ap-northeast-2 apne2-az4 | 292 | 84% | 8.0 | 9 (10-30 09:18Z) |
| ap-south-1 aps1-az1 | 154 | 86% | 8.1 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az2 | 166 | 78% | 7.6 | 9 (10-30 03:19Z) |
| ap-south-1 aps1-az3 | 174 | 89% | 8.3 | 9 (10-30 03:19Z) |
| ap-southeast-2 apse2-az1 | 52 | 81% | 7.8 | 9 (10-29 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 59 | 78% | 7.6 | 9 (10-29 18:20Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 97 | 100% | 9.0 | 9 (10-30 10:16Z) |
| us-east-1 use1-az4 | 126 | 90% | 8.3 | 9 (10-30 10:16Z) |
| us-east-1 use1-az5 | 92 | 98% | 8.8 | 9 (10-30 10:16Z) |
| us-east-1 use1-az6 | 113 | 91% | 8.4 | 9 (10-30 10:16Z) |
| us-east-2 use2-az1 | 157 | 99% | 8.9 | 9 (10-30 10:16Z) |
| us-east-2 use2-az2 | 185 | 99% | 8.9 | 9 (10-30 08:21Z) |
| us-east-2 use2-az3 | 204 | 96% | 8.7 | 9 (10-30 10:16Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 84 | 89% | 8.2 | 2 (10-30 03:19Z) |
| us-west-2 usw2-az3 | 114 | 89% | 8.2 | 2 (10-30 04:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.699800 | 2026-10-30T10:16:51Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-30T10:16:51Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.745600 | 2026-10-30T10:16:51Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947900 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585500 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.589400 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571300 | 2026-10-30T10:16:51Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-30T10:16:51Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.602900 | 2026-10-30T10:16:51Z |
| ap-south-1 | ap-south-1a | Windows | 0.464400 | 2026-10-30T10:16:51Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.574800 | 2026-10-30T10:16:51Z |
| ap-south-1 | ap-south-1b | Windows | 0.386600 | 2026-10-30T10:16:51Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-30T10:16:51Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517800 | 2026-10-30T10:16:51Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657300 | 2026-10-30T10:16:51Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559200 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.580200 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.532300 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.525000 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.517900 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.571500 | 2026-10-30T10:16:51Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554700 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547600 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546100 | 2026-10-30T10:16:51Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.560500 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2a | Windows | 0.316200 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579800 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2b | Windows | 0.323900 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.553500 | 2026-10-30T10:16:51Z |
| us-west-2 | us-west-2c | Windows | 0.316400 | 2026-10-30T10:16:51Z |
