# Spot placement score log

Generated 2026-10-29 03:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 417 | 47% | 5.2 | 9 (10-29 03:19Z) |
| ap-northeast-1 | 417 | 16% | 2.8 | 1 (10-29 03:19Z) |
| ap-northeast-2 | 417 | 63% | 6.7 | 9 (10-29 03:19Z) |
| ap-south-1 | 417 | 3% | 1.8 | 1 (10-29 03:19Z) |
| ap-southeast-2 | 417 | 0% | 1.0 | 1 (10-29 03:19Z) |
| ap-southeast-3 | 417 | 27% | 3.5 | 1 (10-29 03:19Z) |
| us-east-1 | 417 | 12% | 2.7 | 1 (10-29 03:19Z) |
| us-east-2 | 417 | 32% | 3.8 | 1 (10-29 03:19Z) |
| us-west-2 | 417 | 10% | 2.2 | 2 (10-29 03:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999911111199999999999999111111199
ap-northeast-1   919292112211312222221111111111121112122223222111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911169111111111111111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   289886127111864885411111111111115688863112111111
us-east-1        399729992192332223331112211122333331111111111111
us-east-2        939919991119611199991119111999911111111111111111
us-west-2        919191112121111111111111112111122222222222222112
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
| us-east-1 | 3 | 3 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 8 | 4 | 6 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 134 | 7% | 1.6 | 1 (10-29 01:18Z) |
| ap-east-1 ape1-az2 | 311 | 63% | 6.5 | 9 (10-29 03:19Z) |
| ap-northeast-1 apne1-az1 | 77 | 5% | 1.5 | 1 (10-29 03:19Z) |
| ap-northeast-1 apne1-az4 | 190 | 28% | 3.7 | 1 (10-29 01:18Z) |
| ap-northeast-2 apne2-az1 | 364 | 56% | 6.2 | 7 (10-29 03:19Z) |
| ap-northeast-2 apne2-az3 | 386 | 62% | 6.6 | 9 (10-29 03:19Z) |
| ap-northeast-2 apne2-az4 | 413 | 63% | 6.8 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az1 | 109 | 1% | 1.4 | 1 (10-29 01:18Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 72 | 3% | 1.3 | 1 (10-29 03:19Z) |
| ap-southeast-2 apse2-az2 | 43 | 0% | 1.0 | 1 (10-28 16:18Z) |
| ap-southeast-3 apse3-az1 | 78 | 0% | 1.0 | 1 (10-28 23:14Z) |
| ap-southeast-3 apse3-az3 | 275 | 40% | 4.6 | 1 (10-29 02:22Z) |
| us-east-1 use1-az1 | 79 | 0% | 1.1 | 1 (10-29 03:19Z) |
| us-east-1 use1-az2 | 111 | 3% | 1.4 | 1 (10-29 01:18Z) |
| us-east-1 use1-az4 | 131 | 27% | 3.4 | 1 (10-29 03:19Z) |
| us-east-1 use1-az5 | 135 | 28% | 3.4 | 1 (10-29 02:22Z) |
| us-east-1 use1-az6 | 97 | 28% | 3.4 | 1 (10-28 23:14Z) |
| us-east-2 use2-az1 | 171 | 46% | 4.9 | 1 (10-29 03:19Z) |
| us-east-2 use2-az2 | 221 | 51% | 5.4 | 1 (10-29 01:18Z) |
| us-east-2 use2-az3 | 255 | 48% | 5.2 | 1 (10-29 02:22Z) |
| us-west-2 usw2-az1 | 139 | 26% | 3.4 | 1 (10-28 19:14Z) |
| us-west-2 usw2-az2 | 98 | 20% | 2.9 | 1 (10-29 03:19Z) |
| us-west-2 usw2-az3 | 160 | 19% | 3.0 | 1 (10-29 01:18Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 417 | 63% | 6.8 | 9 (10-29 03:19Z) |
| ap-northeast-1 | 417 | 72% | 7.0 | 1 (10-29 03:19Z) |
| ap-northeast-2 | 417 | 100% | 9.0 | 9 (10-29 03:19Z) |
| ap-south-1 | 417 | 63% | 6.4 | 9 (10-29 03:19Z) |
| ap-southeast-2 | 417 | 21% | 3.3 | 1 (10-29 03:19Z) |
| ap-southeast-3 | 417 | 27% | 3.5 | 1 (10-29 03:19Z) |
| us-east-1 | 417 | 69% | 6.4 | 6 (10-29 03:19Z) |
| us-east-2 | 417 | 71% | 6.9 | 2 (10-29 03:19Z) |
| us-west-2 | 417 | 51% | 5.6 | 5 (10-29 03:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999199911999999992211111122279999999999993111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999919911211999999999911111111111112999999999
ap-southeast-2   999911111111119911111111111119999999999911111111
ap-southeast-3   289886127111864885411111111111115688863112111111
us-east-1        999999994399554457669969654459654352221112224446
us-east-2        989939999999999999999999999999999912222222222252
us-west-2        999993494459113333343333335594399459554444444335
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
| us-east-2 | 7 | 6 | 7 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 261 | 79% | 7.8 | 9 (10-29 03:19Z) |
| ap-east-1 ape1-az2 | 220 | 81% | 7.9 | 9 (10-29 03:19Z) |
| ap-east-1 ape1-az3 | 239 | 82% | 7.9 | 9 (10-29 03:19Z) |
| ap-northeast-1 apne1-az1 | 182 | 94% | 8.6 | 9 (10-28 22:15Z) |
| ap-northeast-1 apne1-az2 | 137 | 80% | 7.8 | 9 (10-28 23:14Z) |
| ap-northeast-1 apne1-az4 | 228 | 99% | 8.9 | 9 (10-28 22:15Z) |
| ap-northeast-2 apne2-az1 | 337 | 100% | 9.0 | 9 (10-29 03:19Z) |
| ap-northeast-2 apne2-az2 | 87 | 82% | 7.8 | 9 (10-29 01:18Z) |
| ap-northeast-2 apne2-az3 | 361 | 100% | 9.0 | 9 (10-29 03:19Z) |
| ap-northeast-2 apne2-az4 | 263 | 82% | 7.9 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az1 | 146 | 85% | 8.1 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az2 | 157 | 77% | 7.6 | 9 (10-29 03:19Z) |
| ap-south-1 aps1-az3 | 169 | 89% | 8.3 | 9 (10-29 03:19Z) |
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
| us-west-2 usw2-az2 | 79 | 95% | 8.6 | 2 (10-29 03:19Z) |
| us-west-2 usw2-az3 | 104 | 91% | 8.4 | 2 (10-29 02:22Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703600 | 2026-10-29T03:19:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-29T03:19:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.776300 | 2026-10-29T03:19:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.967900 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584700 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.587200 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570200 | 2026-10-29T03:19:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-29T03:19:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.583300 | 2026-10-29T03:19:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.458100 | 2026-10-29T03:19:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.612000 | 2026-10-29T03:19:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.397300 | 2026-10-29T03:19:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652500 | 2026-10-29T03:19:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.522300 | 2026-10-29T03:19:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656800 | 2026-10-29T03:19:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559400 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.586300 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.505500 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.528300 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516700 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.554600 | 2026-10-29T03:19:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.567900 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2a | Windows | 0.638700 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2b | Windows | 0.637700 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548200 | 2026-10-29T03:19:45Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.565100 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2a | Windows | 0.318400 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.590100 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2b | Windows | 0.326200 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.561800 | 2026-10-29T03:19:45Z |
| us-west-2 | us-west-2c | Windows | 0.318000 | 2026-10-29T03:19:45Z |
