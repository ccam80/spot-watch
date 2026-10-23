# Spot placement score log

Generated 2026-10-23 14:57 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 359 | 43% | 4.9 | 9 (10-23 14:57Z) |
| ap-northeast-1 | 359 | 15% | 2.7 | 2 (10-23 14:57Z) |
| ap-northeast-2 | 359 | 57% | 6.4 | 9 (10-23 14:57Z) |
| ap-south-1 | 359 | 2% | 1.8 | 1 (10-23 14:57Z) |
| ap-southeast-2 | 359 | 1% | 1.1 | 1 (10-23 14:57Z) |
| ap-southeast-3 | 359 | 26% | 3.5 | 9 (10-23 14:57Z) |
| us-east-1 | 359 | 10% | 2.6 | 2 (10-23 14:57Z) |
| us-east-2 | 359 | 30% | 3.7 | 1 (10-23 14:57Z) |
| us-west-2 | 359 | 11% | 2.3 | 2 (10-23 14:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999991119999999999999999
ap-northeast-1   211421111322129324165912221981121211121111282112
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222221112222222222222222222222222222222222211111
ap-southeast-2   111111111111191191111111111111111111111111111111
ap-southeast-3   311518214387518679924748811787113651189911599119
us-east-1        321323122222333221923999999112132112121115123222
us-east-2        129111999111161999999199999119991119911199111191
us-west-2        111221111222112121219119211211111113122195121122
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
| ap-east-1 ape1-az2 | 262 | 58% | 6.2 | 9 (10-23 14:57Z) |
| ap-northeast-1 apne1-az1 | 60 | 7% | 1.7 | 1 (10-23 14:57Z) |
| ap-northeast-1 apne1-az4 | 163 | 26% | 3.6 | 8 (10-22 19:59Z) |
| ap-northeast-2 apne2-az1 | 313 | 52% | 5.9 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az3 | 331 | 57% | 6.3 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az4 | 356 | 57% | 6.4 | 9 (10-23 14:57Z) |
| ap-south-1 aps1-az1 | 87 | 1% | 1.5 | 1 (10-23 09:57Z) |
| ap-south-1 aps1-az3 | 116 | 3% | 2.3 | 1 (10-22 15:10Z) |
| ap-southeast-2 apse2-az1 | 58 | 3% | 1.3 | 1 (10-23 04:37Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 75 | 0% | 1.0 | 1 (10-21 10:02Z) |
| ap-southeast-3 apse3-az3 | 242 | 36% | 4.4 | 9 (10-23 14:57Z) |
| us-east-1 use1-az1 | 71 | 0% | 1.1 | 1 (10-23 14:57Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 111 | 29% | 3.5 | 1 (10-23 14:57Z) |
| us-east-1 use1-az5 | 113 | 27% | 3.4 | 1 (10-22 15:10Z) |
| us-east-1 use1-az6 | 81 | 25% | 3.2 | 1 (10-21 23:14Z) |
| us-east-2 use2-az1 | 146 | 44% | 4.8 | 1 (10-23 14:57Z) |
| us-east-2 use2-az2 | 187 | 49% | 5.2 | 9 (10-23 09:57Z) |
| us-east-2 use2-az3 | 217 | 47% | 5.2 | 9 (10-23 09:57Z) |
| us-west-2 usw2-az1 | 130 | 26% | 3.5 | 1 (10-22 15:10Z) |
| us-west-2 usw2-az2 | 80 | 22% | 3.1 | 1 (10-23 14:57Z) |
| us-west-2 usw2-az3 | 133 | 22% | 3.2 | 1 (10-23 09:57Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 359 | 57% | 6.4 | 9 (10-23 14:57Z) |
| ap-northeast-1 | 359 | 73% | 7.1 | 9 (10-23 14:57Z) |
| ap-northeast-2 | 359 | 100% | 9.0 | 9 (10-23 14:57Z) |
| ap-south-1 | 359 | 62% | 6.4 | 1 (10-23 14:57Z) |
| ap-southeast-2 | 359 | 19% | 3.2 | 1 (10-23 14:57Z) |
| ap-southeast-3 | 359 | 26% | 3.5 | 9 (10-23 14:57Z) |
| us-east-1 | 359 | 70% | 6.5 | 4 (10-23 14:57Z) |
| us-east-2 | 359 | 70% | 6.9 | 5 (10-23 14:57Z) |
| us-west-2 | 359 | 52% | 5.7 | 5 (10-23 14:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   921999119999999999999999932991239992399923999239
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992299912999999999999999992999922282299992999991
ap-southeast-2   111111111111999999999999111911111111111111111111
ap-southeast-3   311518214387518679924748811787113651189911599119
us-east-1        555546793446599999999999999464563444364339246564
us-east-2        229111999311399999999999999239995299912999722195
us-west-2        433554334454439999999999999534394339145399933345
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
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 223 | 76% | 7.5 | 9 (10-23 14:57Z) |
| ap-east-1 ape1-az2 | 187 | 78% | 7.7 | 9 (10-23 14:57Z) |
| ap-east-1 ape1-az3 | 193 | 77% | 7.6 | 9 (10-23 14:57Z) |
| ap-northeast-1 apne1-az1 | 161 | 93% | 8.6 | 9 (10-23 14:57Z) |
| ap-northeast-1 apne1-az2 | 108 | 75% | 7.5 | 9 (10-23 14:57Z) |
| ap-northeast-1 apne1-az4 | 203 | 99% | 8.9 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az1 | 284 | 100% | 9.0 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az2 | 76 | 79% | 7.7 | 3 (10-23 04:37Z) |
| ap-northeast-2 apne2-az3 | 312 | 100% | 9.0 | 9 (10-23 14:57Z) |
| ap-northeast-2 apne2-az4 | 221 | 79% | 7.7 | 9 (10-23 14:57Z) |
| ap-south-1 aps1-az1 | 123 | 82% | 7.9 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az2 | 133 | 73% | 7.3 | 6 (10-23 09:57Z) |
| ap-south-1 aps1-az3 | 145 | 87% | 8.2 | 9 (10-23 04:37Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.713100 | 2026-10-23T14:57:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-23T14:57:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.750100 | 2026-10-23T14:57:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.937600 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.587200 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580200 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565600 | 2026-10-23T14:57:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-23T14:57:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.532500 | 2026-10-23T14:57:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-10-23T14:57:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.738600 | 2026-10-23T14:57:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.381400 | 2026-10-23T14:57:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.669600 | 2026-10-23T14:57:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.472600 | 2026-10-23T14:57:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656300 | 2026-10-23T14:57:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.544100 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.549700 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.459700 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.489100 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.499200 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.496300 | 2026-10-23T14:57:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.561000 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2a | Windows | 0.640200 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548000 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2b | Windows | 0.638200 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.543800 | 2026-10-23T14:57:49Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.551300 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2a | Windows | 0.316800 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.553200 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2b | Windows | 0.330500 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528300 | 2026-10-23T14:57:49Z |
| us-west-2 | us-west-2c | Windows | 0.316500 | 2026-10-23T14:57:49Z |
