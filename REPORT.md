# Spot placement score log

Generated 2026-09-30 05:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 234 | 30% | 4.1 | 9 (09-30 05:24Z) |
| ap-northeast-1 | 234 | 9% | 2.4 | 2 (09-30 05:24Z) |
| ap-northeast-2 | 234 | 35% | 5.1 | 9 (09-30 05:24Z) |
| ap-south-1 | 234 | 3% | 1.9 | 1 (09-30 05:24Z) |
| ap-southeast-2 | 234 | 0% | 1.0 | 1 (09-30 05:24Z) |
| ap-southeast-3 | 234 | 21% | 3.4 | 1 (09-30 05:24Z) |
| us-east-1 | 234 | 8% | 2.4 | 9 (09-30 05:24Z) |
| us-east-2 | 234 | 20% | 3.1 | 9 (09-30 05:24Z) |
| us-west-2 | 234 | 9% | 2.2 | 1 (09-30 05:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        114999999999999999999999999999999999999999999999
ap-northeast-1   111111898994558941221222111211481882137961222122
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111121111111111111111111111111111111111221111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   115368786755668889111111111543788768111118711111
us-east-1        999199911111112111112911111221112211111291222999
us-east-2        999999911111111111111111999999911111191699991119
us-west-2        999999111111111111112211111111112222211111211111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 7 | 7 | 3 | 4 | 3 | 6 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 4 | 3 | 2 | 4 | 4 | 7 | 6 | 4 | 5 | 4 | 6 | 4 | 2 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 4 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 80 | 0% | 1.5 | 1 (09-30 02:34Z) |
| ap-east-1 ape1-az2 | 166 | 42% | 5.2 | 9 (09-30 05:24Z) |
| ap-northeast-1 apne1-az1 | 31 | 0% | 1.3 | 2 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 104 | 12% | 2.7 | 1 (09-30 02:34Z) |
| ap-northeast-2 apne2-az1 | 212 | 35% | 5.1 | 9 (09-30 05:24Z) |
| ap-northeast-2 apne2-az3 | 216 | 38% | 5.2 | 9 (09-30 05:24Z) |
| ap-northeast-2 apne2-az4 | 231 | 35% | 5.1 | 9 (09-30 05:24Z) |
| ap-south-1 aps1-az1 | 69 | 1% | 1.7 | 1 (09-30 03:29Z) |
| ap-south-1 aps1-az3 | 92 | 3% | 2.6 | 1 (09-30 04:28Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 21 | 0% | 1.0 | 1 (09-29 16:27Z) |
| ap-southeast-3 apse3-az1 | 45 | 0% | 1.0 | 1 (09-30 02:34Z) |
| ap-southeast-3 apse3-az3 | 172 | 26% | 4.1 | 7 (09-30 01:01Z) |
| us-east-1 use1-az1 | 34 | 0% | 1.2 | 1 (09-30 04:28Z) |
| us-east-1 use1-az2 | 69 | 3% | 1.5 | 4 (09-30 04:28Z) |
| us-east-1 use1-az4 | 72 | 22% | 3.1 | 9 (09-30 05:24Z) |
| us-east-1 use1-az5 | 71 | 21% | 3.1 | 9 (09-30 05:24Z) |
| us-east-1 use1-az6 | 56 | 14% | 2.5 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 92 | 32% | 3.9 | 9 (09-30 05:24Z) |
| us-east-2 use2-az2 | 118 | 34% | 4.2 | 9 (09-30 05:24Z) |
| us-east-2 use2-az3 | 137 | 31% | 4.3 | 9 (09-30 05:24Z) |
| us-west-2 usw2-az1 | 75 | 27% | 3.7 | 1 (09-30 01:40Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 103 | 17% | 3.0 | 1 (09-30 03:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 234 | 35% | 5.1 | 9 (09-30 05:24Z) |
| ap-northeast-1 | 234 | 74% | 7.2 | 2 (09-30 05:24Z) |
| ap-northeast-2 | 234 | 100% | 9.0 | 9 (09-30 05:24Z) |
| ap-south-1 | 234 | 59% | 6.3 | 9 (09-30 05:24Z) |
| ap-southeast-2 | 234 | 17% | 3.2 | 2 (09-30 05:24Z) |
| ap-southeast-3 | 234 | 21% | 3.4 | 1 (09-30 05:24Z) |
| us-east-1 | 234 | 75% | 6.9 | 9 (09-30 05:24Z) |
| us-east-2 | 234 | 75% | 7.3 | 9 (09-30 05:24Z) |
| us-west-2 | 234 | 55% | 5.9 | 4 (09-30 05:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111389999999999999333522233389999999999999222332
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       932112299999999999999999421711152999999999999999
ap-southeast-2   222242794999932212222222222222295922922112222222
ap-southeast-3   115368786755668889111111111543788768111118711111
us-east-1        999999922123445433698957948995944544359593655999
us-east-2        999999992233332233223999999999933433399999999999
us-west-2        999999999944343322444422992244945355532243533324
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 6 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 5 | 4 | 3 | 5 | 4 | 2 | 6 | 4 | 7 | 7 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 5 | 2 | 3 | 3 | 4 | 6 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 5 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 9 | 7 | 7 | 5 | 8 | 7 | 9 | 8 | 6 | 8 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 124 | 56% | 6.4 | 9 (09-30 05:24Z) |
| ap-east-1 ape1-az2 | 95 | 57% | 6.4 | 9 (09-30 04:28Z) |
| ap-east-1 ape1-az3 | 92 | 52% | 6.1 | 9 (09-30 05:24Z) |
| ap-northeast-1 apne1-az1 | 108 | 93% | 8.5 | 9 (09-29 22:22Z) |
| ap-northeast-1 apne1-az2 | 44 | 41% | 5.5 | 9 (09-29 21:21Z) |
| ap-northeast-1 apne1-az4 | 138 | 99% | 8.9 | 9 (09-29 22:22Z) |
| ap-northeast-2 apne2-az1 | 181 | 100% | 9.0 | 9 (09-30 05:24Z) |
| ap-northeast-2 apne2-az2 | 52 | 73% | 7.3 | 9 (09-30 01:01Z) |
| ap-northeast-2 apne2-az3 | 209 | 100% | 9.0 | 9 (09-30 05:24Z) |
| ap-northeast-2 apne2-az4 | 118 | 60% | 6.6 | 9 (09-30 05:24Z) |
| ap-south-1 aps1-az1 | 72 | 69% | 7.2 | 9 (09-30 04:28Z) |
| ap-south-1 aps1-az2 | 85 | 58% | 6.5 | 9 (09-30 05:24Z) |
| ap-south-1 aps1-az3 | 95 | 81% | 7.9 | 9 (09-30 04:28Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 51 | 22% | 4.2 | 8 (09-29 14:24Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 88 | 98% | 8.8 | 9 (09-30 04:28Z) |
| us-east-1 use1-az5 | 50 | 98% | 8.9 | 9 (09-30 05:24Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 89 | 99% | 8.9 | 9 (09-30 05:24Z) |
| us-east-2 use2-az2 | 124 | 98% | 8.9 | 9 (09-30 04:28Z) |
| us-east-2 use2-az3 | 115 | 93% | 8.5 | 9 (09-30 05:24Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 72 | 99% | 8.9 | 9 (09-29 12:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.731300 | 2026-09-30T05:24:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.868200 | 2026-09-30T05:24:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.792900 | 2026-09-30T05:24:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.971500 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594400 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566900 | 2026-09-30T05:24:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-30T05:24:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.604100 | 2026-09-30T05:24:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.351500 | 2026-09-30T05:24:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.639700 | 2026-09-30T05:24:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.343000 | 2026-09-30T05:24:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719800 | 2026-09-30T05:24:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-09-30T05:24:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.631800 | 2026-09-30T05:24:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.594700 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1a | Windows | 0.305100 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.459800 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.442100 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.398600 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438300 | 2026-09-30T05:24:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530700 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524200 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2b | Windows | 0.640600 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-09-30T05:24:32Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513300 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.503800 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2b | Windows | 0.332400 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486400 | 2026-09-30T05:24:32Z |
| us-west-2 | us-west-2c | Windows | 0.331200 | 2026-09-30T05:24:32Z |
