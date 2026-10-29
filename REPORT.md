# Spot placement score log

Generated 2026-10-29 22:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 436 | 46% | 5.1 | 1 (10-29 22:15Z) |
| ap-northeast-1 | 436 | 15% | 2.7 | 2 (10-29 22:15Z) |
| ap-northeast-2 | 436 | 64% | 6.8 | 9 (10-29 22:15Z) |
| ap-south-1 | 436 | 3% | 1.7 | 1 (10-29 22:15Z) |
| ap-southeast-2 | 436 | 0% | 1.0 | 1 (10-29 22:15Z) |
| ap-southeast-3 | 436 | 26% | 3.4 | 1 (10-29 22:15Z) |
| us-east-1 | 436 | 11% | 2.7 | 1 (10-29 22:15Z) |
| us-east-2 | 436 | 30% | 3.7 | 1 (10-29 22:15Z) |
| us-west-2 | 436 | 10% | 2.2 | 2 (10-29 22:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111999999999999991111111999997111111221442121
ap-northeast-1   211111111111211121222232221111111111222211111222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111156888631121111111111111111123321111
us-east-1        311122111223333311111111111112222333332333322111
us-east-2        911191119999111111111111111111114111111111111111
us-west-2        111111121111222222222222221122222211112111111222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 5 | 3 | 4 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 143 | 6% | 1.6 | 1 (10-29 21:15Z) |
| ap-east-1 ape1-az2 | 318 | 63% | 6.5 | 1 (10-29 22:15Z) |
| ap-northeast-1 apne1-az1 | 86 | 5% | 1.5 | 1 (10-29 22:15Z) |
| ap-northeast-1 apne1-az4 | 198 | 27% | 3.6 | 1 (10-29 21:15Z) |
| ap-northeast-2 apne2-az1 | 378 | 57% | 6.3 | 9 (10-29 22:15Z) |
| ap-northeast-2 apne2-az3 | 405 | 64% | 6.7 | 9 (10-29 22:15Z) |
| ap-northeast-2 apne2-az4 | 432 | 65% | 6.9 | 9 (10-29 22:15Z) |
| ap-south-1 aps1-az1 | 121 | 1% | 1.4 | 1 (10-29 21:15Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 77 | 3% | 1.3 | 1 (10-29 22:15Z) |
| ap-southeast-2 apse2-az2 | 46 | 0% | 1.0 | 1 (10-29 19:14Z) |
| ap-southeast-3 apse3-az1 | 80 | 0% | 1.0 | 1 (10-29 14:17Z) |
| ap-southeast-3 apse3-az3 | 284 | 38% | 4.5 | 1 (10-29 22:15Z) |
| us-east-1 use1-az1 | 83 | 0% | 1.1 | 1 (10-29 19:14Z) |
| us-east-1 use1-az2 | 117 | 3% | 1.4 | 1 (10-29 21:15Z) |
| us-east-1 use1-az4 | 140 | 26% | 3.2 | 1 (10-29 19:14Z) |
| us-east-1 use1-az5 | 141 | 27% | 3.3 | 1 (10-29 22:15Z) |
| us-east-1 use1-az6 | 104 | 26% | 3.2 | 1 (10-29 17:15Z) |
| us-east-2 use2-az1 | 179 | 44% | 4.7 | 1 (10-29 18:20Z) |
| us-east-2 use2-az2 | 229 | 49% | 5.2 | 1 (10-29 21:15Z) |
| us-east-2 use2-az3 | 261 | 47% | 5.1 | 1 (10-29 22:15Z) |
| us-west-2 usw2-az1 | 140 | 26% | 3.4 | 1 (10-29 20:16Z) |
| us-west-2 usw2-az2 | 104 | 19% | 2.8 | 1 (10-29 22:15Z) |
| us-west-2 usw2-az3 | 173 | 18% | 2.8 | 1 (10-29 21:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 436 | 65% | 6.9 | 9 (10-29 22:15Z) |
| ap-northeast-1 | 436 | 72% | 7.0 | 9 (10-29 22:15Z) |
| ap-northeast-2 | 436 | 100% | 9.0 | 9 (10-29 22:15Z) |
| ap-south-1 | 436 | 61% | 6.3 | 9 (10-29 22:15Z) |
| ap-southeast-2 | 436 | 22% | 3.3 | 1 (10-29 22:15Z) |
| ap-southeast-3 | 436 | 26% | 3.4 | 1 (10-29 22:15Z) |
| us-east-1 | 436 | 70% | 6.4 | 5 (10-29 22:15Z) |
| us-east-2 | 436 | 68% | 6.7 | 2 (10-29 22:15Z) |
| us-west-2 | 436 | 51% | 5.6 | 5 (10-29 22:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   922111111222799999999999931111111111999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999111111111111129999999997111111111111299999
ap-southeast-2   111111111199999999999111111111111143999999999111
ap-southeast-3   111111111111156888631121111111111111111123321111
us-east-1        699696544596543522211122244466665779956565556545
us-east-2        999999999999999122222222222522229922299122221212
us-west-2        433333355943994595544444443355999554499993344455
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 8 | 9 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 274 | 80% | 7.8 | 9 (10-29 20:16Z) |
| ap-east-1 ape1-az2 | 238 | 83% | 8.0 | 9 (10-29 22:15Z) |
| ap-east-1 ape1-az3 | 258 | 83% | 8.0 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az1 | 189 | 94% | 8.6 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az2 | 149 | 82% | 7.9 | 9 (10-29 22:15Z) |
| ap-northeast-1 apne1-az4 | 233 | 99% | 8.9 | 9 (10-29 20:16Z) |
| ap-northeast-2 apne2-az1 | 354 | 100% | 9.0 | 9 (10-29 22:15Z) |
| ap-northeast-2 apne2-az2 | 91 | 82% | 7.9 | 9 (10-29 22:15Z) |
| ap-northeast-2 apne2-az3 | 380 | 100% | 9.0 | 9 (10-29 22:15Z) |
| ap-northeast-2 apne2-az4 | 281 | 83% | 8.0 | 9 (10-29 22:15Z) |
| ap-south-1 aps1-az1 | 149 | 85% | 8.1 | 9 (10-29 22:15Z) |
| ap-south-1 aps1-az2 | 161 | 77% | 7.6 | 9 (10-29 22:15Z) |
| ap-south-1 aps1-az3 | 170 | 88% | 8.3 | 3 (10-29 04:19Z) |
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
| us-west-2 usw2-az2 | 81 | 93% | 8.5 | 2 (10-29 06:26Z) |
| us-west-2 usw2-az3 | 113 | 89% | 8.3 | 9 (10-29 15:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702000 | 2026-10-29T22:15:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T22:15:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.760400 | 2026-10-29T22:15:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.955400 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585300 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.588800 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571000 | 2026-10-29T22:15:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-29T22:15:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.589400 | 2026-10-29T22:15:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.461900 | 2026-10-29T22:15:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.588200 | 2026-10-29T22:15:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.393800 | 2026-10-29T22:15:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653100 | 2026-10-29T22:15:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.521300 | 2026-10-29T22:15:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.657400 | 2026-10-29T22:15:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559200 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.572800 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.520700 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.526500 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.522000 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.573100 | 2026-10-29T22:15:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.556500 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547700 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546600 | 2026-10-29T22:15:49Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561000 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2a | Windows | 0.317900 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.582800 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2b | Windows | 0.324800 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.555500 | 2026-10-29T22:15:49Z |
| us-west-2 | us-west-2c | Windows | 0.316800 | 2026-10-29T22:15:49Z |
