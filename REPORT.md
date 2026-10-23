# Spot placement score log

Generated 2026-10-23 09:58 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 358 | 43% | 4.9 | 9 (10-23 09:57Z) |
| ap-northeast-1 | 358 | 15% | 2.7 | 1 (10-23 09:57Z) |
| ap-northeast-2 | 358 | 56% | 6.4 | 9 (10-23 09:57Z) |
| ap-south-1 | 358 | 2% | 1.8 | 1 (10-23 09:57Z) |
| ap-southeast-2 | 358 | 1% | 1.1 | 1 (10-23 09:57Z) |
| ap-southeast-3 | 358 | 25% | 3.4 | 1 (10-23 09:57Z) |
| us-east-1 | 358 | 10% | 2.6 | 2 (10-23 09:57Z) |
| us-east-2 | 358 | 30% | 3.8 | 9 (10-23 09:57Z) |
| us-west-2 | 358 | 11% | 2.3 | 2 (10-23 09:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999111999999999999999
ap-northeast-1   221142111132212932416591222198112121112111128211
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222111222222222222222222222222222222222221111
ap-southeast-2   111111111111119119111111111111111111111111111111
ap-southeast-3   131151821438751867992474881178711365118991159911
us-east-1        232132312222233322192399999911213211212111512322
us-east-2        112911199911116199999919999911999111991119911119
us-west-2        111122111122211212121911921121111111312219512112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 5 | 4 | 7 | 5 | 5 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 5 | 5 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 122 | 7% | 1.7 | 1 (10-22 15:10Z) |
| ap-east-1 ape1-az2 | 261 | 58% | 6.2 | 9 (10-23 09:57Z) |
| ap-northeast-1 apne1-az1 | 59 | 7% | 1.7 | 1 (10-22 23:16Z) |
| ap-northeast-1 apne1-az4 | 163 | 26% | 3.6 | 8 (10-22 19:59Z) |
| ap-northeast-2 apne2-az1 | 312 | 52% | 5.9 | 8 (10-23 09:57Z) |
| ap-northeast-2 apne2-az3 | 330 | 57% | 6.3 | 9 (10-23 09:57Z) |
| ap-northeast-2 apne2-az4 | 355 | 57% | 6.4 | 9 (10-23 09:57Z) |
| ap-south-1 aps1-az1 | 87 | 1% | 1.5 | 1 (10-23 09:57Z) |
| ap-south-1 aps1-az3 | 116 | 3% | 2.3 | 1 (10-22 15:10Z) |
| ap-southeast-2 apse2-az1 | 58 | 3% | 1.3 | 1 (10-23 04:37Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 75 | 0% | 1.0 | 1 (10-21 10:02Z) |
| ap-southeast-3 apse3-az3 | 241 | 36% | 4.4 | 9 (10-22 23:16Z) |
| us-east-1 use1-az1 | 70 | 0% | 1.1 | 1 (10-23 04:37Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 110 | 29% | 3.5 | 1 (10-23 04:37Z) |
| us-east-1 use1-az5 | 113 | 27% | 3.4 | 1 (10-22 15:10Z) |
| us-east-1 use1-az6 | 81 | 25% | 3.2 | 1 (10-21 23:14Z) |
| us-east-2 use2-az1 | 145 | 44% | 4.8 | 9 (10-23 09:57Z) |
| us-east-2 use2-az2 | 187 | 49% | 5.2 | 9 (10-23 09:57Z) |
| us-east-2 use2-az3 | 217 | 47% | 5.2 | 9 (10-23 09:57Z) |
| us-west-2 usw2-az1 | 130 | 26% | 3.5 | 1 (10-22 15:10Z) |
| us-west-2 usw2-az2 | 79 | 23% | 3.1 | 1 (10-23 04:37Z) |
| us-west-2 usw2-az3 | 133 | 22% | 3.2 | 1 (10-23 09:57Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 358 | 57% | 6.4 | 9 (10-23 09:57Z) |
| ap-northeast-1 | 358 | 73% | 7.1 | 3 (10-23 09:57Z) |
| ap-northeast-2 | 358 | 100% | 9.0 | 9 (10-23 09:57Z) |
| ap-south-1 | 358 | 63% | 6.5 | 9 (10-23 09:57Z) |
| ap-southeast-2 | 358 | 19% | 3.2 | 1 (10-23 09:57Z) |
| ap-southeast-3 | 358 | 25% | 3.4 | 1 (10-23 09:57Z) |
| us-east-1 | 358 | 70% | 6.5 | 6 (10-23 09:57Z) |
| us-east-2 | 358 | 70% | 6.9 | 9 (10-23 09:57Z) |
| us-west-2 | 358 | 52% | 5.7 | 4 (10-23 09:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992199911999999999999999993299123999239992399923
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299229991299999999999999999299992228229999299999
ap-southeast-2   811111111111199999999999911191111111111111111111
ap-southeast-3   131151821438751867992474881178711365118991159911
us-east-1        355554679344659999999999999946456344436433924656
us-east-2        122911199931139999999999999923999529991299972219
us-west-2        343355433445443999999999999953439433914539993334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 222 | 76% | 7.5 | 9 (10-23 09:57Z) |
| ap-east-1 ape1-az2 | 186 | 78% | 7.7 | 9 (10-23 09:57Z) |
| ap-east-1 ape1-az3 | 192 | 77% | 7.6 | 9 (10-23 09:57Z) |
| ap-northeast-1 apne1-az1 | 160 | 93% | 8.6 | 9 (10-21 15:08Z) |
| ap-northeast-1 apne1-az2 | 107 | 75% | 7.5 | 9 (10-22 23:16Z) |
| ap-northeast-1 apne1-az4 | 202 | 99% | 8.9 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az1 | 283 | 100% | 9.0 | 9 (10-23 09:57Z) |
| ap-northeast-2 apne2-az2 | 76 | 79% | 7.7 | 3 (10-23 04:37Z) |
| ap-northeast-2 apne2-az3 | 311 | 100% | 9.0 | 9 (10-23 09:57Z) |
| ap-northeast-2 apne2-az4 | 220 | 79% | 7.7 | 9 (10-23 09:57Z) |
| ap-south-1 aps1-az1 | 123 | 82% | 7.9 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az2 | 133 | 73% | 7.3 | 6 (10-23 09:57Z) |
| ap-south-1 aps1-az3 | 145 | 87% | 8.2 | 9 (10-23 04:37Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 69 | 35% | 5.0 | 9 (10-22 23:16Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 86 | 100% | 9.0 | 9 (10-22 10:03Z) |
| us-east-1 use1-az4 | 105 | 94% | 8.6 | 9 (10-22 10:03Z) |
| us-east-1 use1-az5 | 71 | 97% | 8.8 | 9 (10-22 10:03Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 124 | 98% | 8.9 | 9 (10-23 09:57Z) |
| us-east-2 use2-az2 | 165 | 99% | 8.9 | 9 (10-23 09:57Z) |
| us-east-2 use2-az3 | 162 | 95% | 8.7 | 9 (10-23 09:57Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 75 | 96% | 8.7 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az3 | 94 | 94% | 8.6 | 2 (10-23 04:37Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.713500 | 2026-10-23T09:57:53Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-23T09:57:53Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.750100 | 2026-10-23T09:57:53Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.931500 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587200 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580100 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565700 | 2026-10-23T09:57:53Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-23T09:57:53Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.532700 | 2026-10-23T09:57:53Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-10-23T09:57:53Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.751400 | 2026-10-23T09:57:53Z |
| ap-south-1 | ap-south-1b | Windows | 0.376600 | 2026-10-23T09:57:53Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.669500 | 2026-10-23T09:57:53Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.475600 | 2026-10-23T09:57:53Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656300 | 2026-10-23T09:57:53Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.539500 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.549700 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.459700 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.495000 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.498600 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.495000 | 2026-10-23T09:57:53Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.561000 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2a | Windows | 0.640300 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547400 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2b | Windows | 0.638200 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.544400 | 2026-10-23T09:57:53Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.548700 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2a | Windows | 0.316700 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.553200 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2b | Windows | 0.330500 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527200 | 2026-10-23T09:57:53Z |
| us-west-2 | us-west-2c | Windows | 0.316500 | 2026-10-23T09:57:53Z |
