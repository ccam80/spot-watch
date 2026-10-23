# Spot placement score log

Generated 2026-10-23 19:06 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 360 | 43% | 4.9 | 1 (10-23 19:06Z) |
| ap-northeast-1 | 360 | 15% | 2.7 | 4 (10-23 19:06Z) |
| ap-northeast-2 | 360 | 57% | 6.4 | 9 (10-23 19:06Z) |
| ap-south-1 | 360 | 2% | 1.8 | 1 (10-23 19:06Z) |
| ap-southeast-2 | 360 | 1% | 1.1 | 1 (10-23 19:06Z) |
| ap-southeast-3 | 360 | 26% | 3.4 | 1 (10-23 19:06Z) |
| us-east-1 | 360 | 10% | 2.6 | 2 (10-23 19:06Z) |
| us-east-2 | 360 | 30% | 3.7 | 1 (10-23 19:06Z) |
| us-west-2 | 360 | 11% | 2.3 | 1 (10-23 19:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999911199999999999999991
ap-northeast-1   114211113221293241659122219811212111211112821124
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222211122222222222222222222222222222222222111111
ap-southeast-2   111111111111911911111111111111111111111111111111
ap-southeast-3   115182143875186799247488117871136511899115991191
us-east-1        213231222223332219239999991121321121211151232222
us-east-2        291119991111619999991999991199911199111991111911
us-west-2        112211112221121212191192112111111131221951211221
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
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 262 | 58% | 6.2 | 9 (10-23 14:57Z) |
| ap-northeast-1 apne1-az1 | 60 | 7% | 1.7 | 1 (10-23 14:57Z) |
| ap-northeast-1 apne1-az4 | 164 | 26% | 3.6 | 3 (10-23 19:06Z) |
| ap-northeast-2 apne2-az1 | 313 | 52% | 5.9 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az3 | 331 | 57% | 6.3 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az4 | 357 | 57% | 6.4 | 9 (10-23 19:06Z) |
| ap-south-1 aps1-az1 | 88 | 1% | 1.5 | 1 (10-23 19:06Z) |
| ap-south-1 aps1-az3 | 116 | 3% | 2.3 | 1 (10-22 15:10Z) |
| ap-southeast-2 apse2-az1 | 58 | 3% | 1.3 | 1 (10-23 04:37Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 242 | 36% | 4.4 | 9 (10-23 14:57Z) |
| us-east-1 use1-az1 | 72 | 0% | 1.1 | 1 (10-23 19:06Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 111 | 29% | 3.5 | 1 (10-23 14:57Z) |
| us-east-1 use1-az5 | 113 | 27% | 3.4 | 1 (10-22 15:10Z) |
| us-east-1 use1-az6 | 82 | 24% | 3.1 | 1 (10-23 19:06Z) |
| us-east-2 use2-az1 | 147 | 44% | 4.8 | 1 (10-23 19:06Z) |
| us-east-2 use2-az2 | 188 | 48% | 5.2 | 1 (10-23 19:06Z) |
| us-east-2 use2-az3 | 217 | 47% | 5.2 | 9 (10-23 09:57Z) |
| us-west-2 usw2-az1 | 130 | 26% | 3.5 | 1 (10-22 15:10Z) |
| us-west-2 usw2-az2 | 80 | 22% | 3.1 | 1 (10-23 14:57Z) |
| us-west-2 usw2-az3 | 134 | 22% | 3.2 | 1 (10-23 19:06Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 360 | 57% | 6.5 | 9 (10-23 19:06Z) |
| ap-northeast-1 | 360 | 73% | 7.1 | 9 (10-23 19:06Z) |
| ap-northeast-2 | 360 | 100% | 9.0 | 9 (10-23 19:06Z) |
| ap-south-1 | 360 | 62% | 6.5 | 9 (10-23 19:06Z) |
| ap-southeast-2 | 360 | 19% | 3.2 | 1 (10-23 19:06Z) |
| ap-southeast-3 | 360 | 26% | 3.4 | 1 (10-23 19:06Z) |
| us-east-1 | 360 | 70% | 6.5 | 5 (10-23 19:06Z) |
| us-east-2 | 360 | 70% | 6.9 | 2 (10-23 19:06Z) |
| us-west-2 | 360 | 52% | 5.7 | 4 (10-23 19:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   219991199999999999999999329912399923999239992399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       922999129999999999999999929999222822999929999919
ap-southeast-2   111111111119999999999991119111111111111111111111
ap-southeast-3   115182143875186799247488117871136511899115991191
us-east-1        555467934465999999999999994645634443643392465645
us-east-2        291119993113999999999999992399952999129997221952
us-west-2        335543344544399999999999995343943391453999333454
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 224 | 76% | 7.6 | 9 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 187 | 78% | 7.7 | 9 (10-23 14:57Z) |
| ap-east-1 ape1-az3 | 194 | 77% | 7.6 | 9 (10-23 19:06Z) |
| ap-northeast-1 apne1-az1 | 162 | 93% | 8.6 | 9 (10-23 19:06Z) |
| ap-northeast-1 apne1-az2 | 109 | 75% | 7.5 | 9 (10-23 19:06Z) |
| ap-northeast-1 apne1-az4 | 204 | 99% | 8.9 | 9 (10-23 19:06Z) |
| ap-northeast-2 apne2-az1 | 285 | 100% | 9.0 | 9 (10-23 19:06Z) |
| ap-northeast-2 apne2-az2 | 76 | 79% | 7.7 | 3 (10-23 04:37Z) |
| ap-northeast-2 apne2-az3 | 313 | 100% | 9.0 | 9 (10-23 19:06Z) |
| ap-northeast-2 apne2-az4 | 221 | 79% | 7.7 | 9 (10-23 14:57Z) |
| ap-south-1 aps1-az1 | 124 | 82% | 7.9 | 9 (10-23 19:06Z) |
| ap-south-1 aps1-az2 | 134 | 73% | 7.3 | 9 (10-23 19:06Z) |
| ap-south-1 aps1-az3 | 146 | 87% | 8.2 | 9 (10-23 19:06Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 70 | 36% | 5.0 | 9 (10-23 14:57Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.713100 | 2026-10-23T19:06:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-23T19:06:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.754600 | 2026-10-23T19:06:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.937600 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587000 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580200 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565600 | 2026-10-23T19:06:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-23T19:06:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.528900 | 2026-10-23T19:06:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.391500 | 2026-10-23T19:06:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.736500 | 2026-10-23T19:06:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.381400 | 2026-10-23T19:06:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.669600 | 2026-10-23T19:06:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.472600 | 2026-10-23T19:06:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656300 | 2026-10-23T19:06:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.544100 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.559800 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.453900 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.491400 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.499200 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.496300 | 2026-10-23T19:06:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.562000 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2a | Windows | 0.640200 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548000 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2b | Windows | 0.638200 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.543800 | 2026-10-23T19:06:32Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.551300 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2a | Windows | 0.316800 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.559400 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2b | Windows | 0.330100 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528600 | 2026-10-23T19:06:32Z |
| us-west-2 | us-west-2c | Windows | 0.316500 | 2026-10-23T19:06:32Z |
