# Spot placement score log

Generated 2026-10-29 00:40 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 414 | 47% | 5.2 | 1 (10-29 00:40Z) |
| ap-northeast-1 | 414 | 16% | 2.8 | 2 (10-29 00:40Z) |
| ap-northeast-2 | 414 | 62% | 6.7 | 9 (10-29 00:40Z) |
| ap-south-1 | 414 | 3% | 1.8 | 1 (10-29 00:40Z) |
| ap-southeast-2 | 414 | 0% | 1.0 | 1 (10-29 00:40Z) |
| ap-southeast-3 | 414 | 28% | 3.5 | 1 (10-29 00:40Z) |
| us-east-1 | 414 | 12% | 2.7 | 1 (10-29 00:40Z) |
| us-east-2 | 414 | 32% | 3.8 | 1 (10-29 00:40Z) |
| us-west-2 | 414 | 10% | 2.3 | 2 (10-29 00:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999911111199999999999999111111
ap-northeast-1   999919292112211312222221111111111121112122223222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       499911169111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   874289886127111864885411111111111115688863112111
us-east-1        199399729992192332223331112211122333331111111111
us-east-2        991939919991119611199991119111999911111111111111
us-west-2        211919191112121111111111111112111122222222222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 6 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 8 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 133 | 7% | 1.6 | 1 (10-29 00:40Z) |
| ap-east-1 ape1-az2 | 309 | 63% | 6.5 | 1 (10-28 19:14Z) |
| ap-northeast-1 apne1-az1 | 75 | 5% | 1.5 | 1 (10-28 22:15Z) |
| ap-northeast-1 apne1-az4 | 189 | 28% | 3.7 | 1 (10-29 00:40Z) |
| ap-northeast-2 apne2-az1 | 361 | 55% | 6.2 | 9 (10-29 00:40Z) |
| ap-northeast-2 apne2-az3 | 383 | 62% | 6.6 | 9 (10-29 00:40Z) |
| ap-northeast-2 apne2-az4 | 410 | 63% | 6.7 | 9 (10-29 00:40Z) |
| ap-south-1 aps1-az1 | 108 | 1% | 1.4 | 1 (10-29 00:40Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 70 | 3% | 1.3 | 1 (10-28 16:18Z) |
| ap-southeast-2 apse2-az2 | 43 | 0% | 1.0 | 1 (10-28 16:18Z) |
| ap-southeast-3 apse3-az1 | 78 | 0% | 1.0 | 1 (10-28 23:14Z) |
| ap-southeast-3 apse3-az3 | 274 | 40% | 4.6 | 1 (10-28 22:15Z) |
| us-east-1 use1-az1 | 78 | 0% | 1.1 | 1 (10-28 16:18Z) |
| us-east-1 use1-az2 | 110 | 3% | 1.4 | 1 (10-29 00:40Z) |
| us-east-1 use1-az4 | 130 | 28% | 3.4 | 1 (10-28 22:15Z) |
| us-east-1 use1-az5 | 134 | 28% | 3.5 | 1 (10-28 19:14Z) |
| us-east-1 use1-az6 | 97 | 28% | 3.4 | 1 (10-28 23:14Z) |
| us-east-2 use2-az1 | 170 | 46% | 4.9 | 1 (10-28 22:15Z) |
| us-east-2 use2-az2 | 220 | 51% | 5.4 | 1 (10-29 00:40Z) |
| us-east-2 use2-az3 | 253 | 48% | 5.2 | 1 (10-29 00:40Z) |
| us-west-2 usw2-az1 | 139 | 26% | 3.4 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az2 | 96 | 21% | 2.9 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az3 | 159 | 19% | 3.0 | 1 (10-29 00:40Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 414 | 63% | 6.8 | 9 (10-29 00:40Z) |
| ap-northeast-1 | 414 | 73% | 7.1 | 3 (10-29 00:40Z) |
| ap-northeast-2 | 414 | 100% | 9.0 | 9 (10-29 00:40Z) |
| ap-south-1 | 414 | 63% | 6.4 | 9 (10-29 00:40Z) |
| ap-southeast-2 | 414 | 21% | 3.3 | 1 (10-29 00:40Z) |
| ap-southeast-3 | 414 | 28% | 3.5 | 1 (10-29 00:40Z) |
| us-east-1 | 414 | 69% | 6.4 | 4 (10-29 00:40Z) |
| us-east-2 | 414 | 71% | 6.9 | 2 (10-29 00:40Z) |
| us-west-2 | 414 | 51% | 5.6 | 4 (10-29 00:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999199911999999992211111122279999999999993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999919911211999999999911111111111112999999
ap-southeast-2   199999911111111119911111111111119999999999911111
ap-southeast-3   874289886127111864885411111111111115688863112111
us-east-1        999999999994399554457669969654459654352221112224
us-east-2        991989939999999999999999999999999999912222222222
us-west-2        954999993494459113333343333335594399459554444444
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 6 | 8 | 6 | 7 | 8 | 6 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 258 | 79% | 7.7 | 9 (10-29 00:40Z) |
| ap-east-1 ape1-az2 | 217 | 81% | 7.9 | 9 (10-29 00:40Z) |
| ap-east-1 ape1-az3 | 236 | 81% | 7.9 | 9 (10-29 00:40Z) |
| ap-northeast-1 apne1-az1 | 182 | 94% | 8.6 | 9 (10-28 22:15Z) |
| ap-northeast-1 apne1-az2 | 137 | 80% | 7.8 | 9 (10-28 23:14Z) |
| ap-northeast-1 apne1-az4 | 228 | 99% | 8.9 | 9 (10-28 22:15Z) |
| ap-northeast-2 apne2-az1 | 334 | 100% | 9.0 | 9 (10-29 00:40Z) |
| ap-northeast-2 apne2-az2 | 86 | 81% | 7.8 | 9 (10-29 00:40Z) |
| ap-northeast-2 apne2-az3 | 358 | 100% | 9.0 | 9 (10-29 00:40Z) |
| ap-northeast-2 apne2-az4 | 260 | 82% | 7.9 | 9 (10-29 00:40Z) |
| ap-south-1 aps1-az1 | 143 | 85% | 8.1 | 9 (10-29 00:40Z) |
| ap-south-1 aps1-az2 | 154 | 77% | 7.5 | 9 (10-29 00:40Z) |
| ap-south-1 aps1-az3 | 166 | 89% | 8.3 | 9 (10-29 00:40Z) |
| ap-southeast-2 apse2-az1 | 44 | 77% | 7.6 | 9 (10-28 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 52 | 75% | 7.5 | 9 (10-28 16:18Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 116 | 94% | 8.6 | 9 (10-28 09:18Z) |
| us-east-1 use1-az5 | 86 | 98% | 8.8 | 9 (10-28 09:18Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 149 | 99% | 8.9 | 9 (10-28 12:23Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 194 | 96% | 8.7 | 9 (10-28 13:16Z) |
| us-west-2 usw2-az1 | 85 | 98% | 8.8 | 9 (10-28 12:23Z) |
| us-west-2 usw2-az2 | 78 | 96% | 8.7 | 9 (10-28 11:16Z) |
| us-west-2 usw2-az3 | 103 | 92% | 8.5 | 9 (10-28 15:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703600 | 2026-10-29T00:40:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T00:40:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.776300 | 2026-10-29T00:40:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.971300 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584700 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586600 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570200 | 2026-10-29T00:40:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-29T00:40:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.580200 | 2026-10-29T00:40:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.458100 | 2026-10-29T00:40:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.612000 | 2026-10-29T00:40:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.400300 | 2026-10-29T00:40:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652500 | 2026-10-29T00:40:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517700 | 2026-10-29T00:40:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656800 | 2026-10-29T00:40:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.561400 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.586300 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.500500 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.529100 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516700 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.553000 | 2026-10-29T00:40:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.567900 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2a | Windows | 0.638700 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548200 | 2026-10-29T00:40:45Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.565100 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2a | Windows | 0.318500 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.590100 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2b | Windows | 0.326200 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.561900 | 2026-10-29T00:40:45Z |
| us-west-2 | us-west-2c | Windows | 0.318200 | 2026-10-29T00:40:45Z |
