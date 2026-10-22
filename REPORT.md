# Spot placement score log

Generated 2026-10-22 04:32 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 352 | 42% | 4.8 | 9 (10-22 04:32Z) |
| ap-northeast-1 | 352 | 15% | 2.7 | 1 (10-22 04:32Z) |
| ap-northeast-2 | 352 | 56% | 6.3 | 9 (10-22 04:32Z) |
| ap-south-1 | 352 | 2% | 1.8 | 2 (10-22 04:32Z) |
| ap-southeast-2 | 352 | 1% | 1.1 | 1 (10-22 04:32Z) |
| ap-southeast-3 | 352 | 25% | 3.4 | 1 (10-22 04:32Z) |
| us-east-1 | 352 | 10% | 2.6 | 1 (10-22 04:32Z) |
| us-east-2 | 352 | 30% | 3.8 | 9 (10-22 04:32Z) |
| us-west-2 | 352 | 11% | 2.3 | 9 (10-22 04:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999111999999999
ap-northeast-1   121114221142111132212932416591222198112121112111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111112222222111222222222222222222222222222222222
ap-southeast-2   111111111111111111119119111111111111111111111111
ap-southeast-3   122111131151821438751867992474881178711365118991
us-east-1        113333232132312222233322192399999911213211212111
us-east-2        112991112911199911116199999919999911999111991119
us-west-2        111111111122111122211212121911921121111111312219
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 5 | 4 | 7 | 5 | 4 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 5 | 5 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 121 | 7% | 1.7 | 1 (10-20 20:29Z) |
| ap-east-1 ape1-az2 | 255 | 57% | 6.1 | 9 (10-22 04:32Z) |
| ap-northeast-1 apne1-az1 | 56 | 7% | 1.7 | 1 (10-21 15:08Z) |
| ap-northeast-1 apne1-az4 | 161 | 26% | 3.6 | 1 (10-21 10:02Z) |
| ap-northeast-2 apne2-az1 | 306 | 51% | 5.9 | 3 (10-22 04:32Z) |
| ap-northeast-2 apne2-az3 | 324 | 56% | 6.3 | 9 (10-22 04:32Z) |
| ap-northeast-2 apne2-az4 | 349 | 56% | 6.3 | 9 (10-22 04:32Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 115 | 3% | 2.3 | 1 (10-21 15:08Z) |
| ap-southeast-2 apse2-az1 | 55 | 4% | 1.4 | 1 (10-21 04:33Z) |
| ap-southeast-2 apse2-az2 | 36 | 0% | 1.0 | 1 (10-21 23:14Z) |
| ap-southeast-3 apse3-az1 | 75 | 0% | 1.0 | 1 (10-21 10:02Z) |
| ap-southeast-3 apse3-az3 | 238 | 35% | 4.4 | 9 (10-21 23:14Z) |
| us-east-1 use1-az1 | 69 | 0% | 1.1 | 1 (10-22 04:32Z) |
| us-east-1 use1-az2 | 98 | 3% | 1.5 | 1 (10-20 20:29Z) |
| us-east-1 use1-az4 | 108 | 30% | 3.6 | 1 (10-21 23:14Z) |
| us-east-1 use1-az5 | 112 | 28% | 3.4 | 1 (10-21 10:02Z) |
| us-east-1 use1-az6 | 81 | 25% | 3.2 | 1 (10-21 23:14Z) |
| us-east-2 use2-az1 | 143 | 44% | 4.8 | 9 (10-22 04:32Z) |
| us-east-2 use2-az2 | 185 | 48% | 5.2 | 9 (10-22 04:32Z) |
| us-east-2 use2-az3 | 214 | 47% | 5.2 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az1 | 128 | 27% | 3.5 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az2 | 76 | 24% | 3.2 | 1 (10-21 15:08Z) |
| us-west-2 usw2-az3 | 131 | 22% | 3.3 | 4 (10-22 04:32Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 352 | 57% | 6.4 | 9 (10-22 04:32Z) |
| ap-northeast-1 | 352 | 73% | 7.1 | 2 (10-22 04:32Z) |
| ap-northeast-2 | 352 | 100% | 9.0 | 9 (10-22 04:32Z) |
| ap-south-1 | 352 | 62% | 6.4 | 9 (10-22 04:32Z) |
| ap-southeast-2 | 352 | 19% | 3.2 | 1 (10-22 04:32Z) |
| ap-southeast-3 | 352 | 25% | 3.4 | 1 (10-22 04:32Z) |
| us-east-1 | 352 | 70% | 6.5 | 3 (10-22 04:32Z) |
| us-east-2 | 352 | 71% | 6.9 | 9 (10-22 04:32Z) |
| us-west-2 | 352 | 52% | 5.7 | 9 (10-22 04:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399239992199911999999999999999993299123999239992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       199912299229991299999999999999999299992228229999
ap-southeast-2   111111811111111111199999999999911191111111111111
ap-southeast-3   122111131151821438751867992474881178711365118991
us-east-1        426664355554679344659999999999999946456344436433
us-east-2        912991122911199931139999999999999923999529991299
us-west-2        442495343355433445443999999999999953439433914539
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 217 | 75% | 7.5 | 9 (10-21 20:04Z) |
| ap-east-1 ape1-az2 | 182 | 77% | 7.6 | 9 (10-21 23:14Z) |
| ap-east-1 ape1-az3 | 186 | 76% | 7.6 | 9 (10-22 04:32Z) |
| ap-northeast-1 apne1-az1 | 160 | 93% | 8.6 | 9 (10-21 15:08Z) |
| ap-northeast-1 apne1-az2 | 104 | 74% | 7.4 | 9 (10-21 23:14Z) |
| ap-northeast-1 apne1-az4 | 199 | 98% | 8.9 | 9 (10-21 20:04Z) |
| ap-northeast-2 apne2-az1 | 277 | 100% | 9.0 | 9 (10-22 04:32Z) |
| ap-northeast-2 apne2-az2 | 75 | 80% | 7.7 | 9 (10-21 23:14Z) |
| ap-northeast-2 apne2-az3 | 305 | 100% | 9.0 | 9 (10-22 04:32Z) |
| ap-northeast-2 apne2-az4 | 214 | 78% | 7.7 | 9 (10-21 23:14Z) |
| ap-south-1 aps1-az1 | 120 | 82% | 7.9 | 9 (10-22 04:32Z) |
| ap-south-1 aps1-az2 | 128 | 72% | 7.3 | 9 (10-22 04:32Z) |
| ap-south-1 aps1-az3 | 144 | 87% | 8.2 | 9 (10-22 04:32Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 67 | 33% | 4.9 | 9 (10-21 23:14Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 123 | 98% | 8.9 | 9 (10-22 04:32Z) |
| us-east-2 use2-az2 | 163 | 99% | 8.9 | 9 (10-21 10:02Z) |
| us-east-2 use2-az3 | 160 | 95% | 8.7 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 75 | 96% | 8.7 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az3 | 93 | 95% | 8.6 | 9 (10-22 04:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712400 | 2026-10-22T04:32:29Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-22T04:32:29Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764700 | 2026-10-22T04:32:29Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.943700 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585600 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580900 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566300 | 2026-10-22T04:32:29Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741000 | 2026-10-22T04:32:29Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548700 | 2026-10-22T04:32:29Z |
| ap-south-1 | ap-south-1a | Windows | 0.395600 | 2026-10-22T04:32:29Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.773400 | 2026-10-22T04:32:29Z |
| ap-south-1 | ap-south-1b | Windows | 0.380500 | 2026-10-22T04:32:29Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.670600 | 2026-10-22T04:32:29Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.476100 | 2026-10-22T04:32:29Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.658300 | 2026-10-22T04:32:29Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.541800 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.518900 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.482600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.488800 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.472600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.491200 | 2026-10-22T04:32:29Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.553000 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2a | Windows | 0.640500 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545600 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2b | Windows | 0.638600 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.542500 | 2026-10-22T04:32:29Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.547100 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2a | Windows | 0.316200 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.544000 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2b | Windows | 0.330100 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.522200 | 2026-10-22T04:32:29Z |
| us-west-2 | us-west-2c | Windows | 0.316000 | 2026-10-22T04:32:29Z |
