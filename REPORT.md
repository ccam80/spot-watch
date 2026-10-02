# Spot placement score log

Generated 2026-10-02 15:43 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 260 | 33% | 4.3 | 1 (10-02 15:43Z) |
| ap-northeast-1 | 260 | 12% | 2.6 | 9 (10-02 15:43Z) |
| ap-northeast-2 | 260 | 41% | 5.5 | 9 (10-02 15:43Z) |
| ap-south-1 | 260 | 2% | 1.8 | 1 (10-02 15:43Z) |
| ap-southeast-2 | 260 | 0% | 1.0 | 1 (10-02 15:43Z) |
| ap-southeast-3 | 260 | 21% | 3.4 | 4 (10-02 15:43Z) |
| us-east-1 | 260 | 8% | 2.5 | 2 (10-02 15:43Z) |
| us-east-2 | 260 | 25% | 3.4 | 9 (10-02 15:43Z) |
| us-west-2 | 260 | 8% | 2.2 | 1 (10-02 15:43Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999998999991111119939911
ap-northeast-1   121148188213796122212222221111899127998121298219
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111122111111111111111111111111111211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   154378876811111871111111111111476516111111999114
us-east-1        122111221111129122299991322222222232222211922922
us-east-2        999991111119169999111999999911111817121899999999
us-west-2        111111222221111121111112112222222222212111222121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 186 | 47% | 5.5 | 9 (10-02 01:36Z) |
| ap-northeast-1 apne1-az1 | 37 | 3% | 1.5 | 8 (10-02 15:43Z) |
| ap-northeast-1 apne1-az4 | 120 | 18% | 3.1 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az1 | 234 | 41% | 5.4 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az3 | 242 | 44% | 5.6 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az4 | 257 | 42% | 5.5 | 9 (10-02 15:43Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 99 | 3% | 2.5 | 1 (10-02 08:24Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 26 | 0% | 1.0 | 1 (10-02 08:24Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 186 | 28% | 4.1 | 4 (10-02 15:43Z) |
| us-east-1 use1-az1 | 39 | 0% | 1.2 | 1 (10-01 21:46Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 80 | 24% | 3.2 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 82 | 21% | 3.0 | 1 (10-02 15:43Z) |
| us-east-1 use1-az6 | 60 | 15% | 2.5 | 9 (10-01 10:01Z) |
| us-east-2 use2-az1 | 103 | 34% | 4.1 | 9 (10-02 15:43Z) |
| us-east-2 use2-az2 | 133 | 40% | 4.7 | 9 (10-02 15:43Z) |
| us-east-2 use2-az3 | 157 | 38% | 4.7 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az1 | 82 | 24% | 3.5 | 1 (10-02 08:24Z) |
| us-west-2 usw2-az2 | 49 | 22% | 3.3 | 1 (10-01 17:00Z) |
| us-west-2 usw2-az3 | 107 | 17% | 2.9 | 1 (10-02 01:36Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 260 | 41% | 5.5 | 9 (10-02 15:43Z) |
| ap-northeast-1 | 260 | 73% | 7.2 | 9 (10-02 15:43Z) |
| ap-northeast-2 | 260 | 100% | 9.0 | 9 (10-02 15:43Z) |
| ap-south-1 | 260 | 57% | 6.1 | 9 (10-02 15:43Z) |
| ap-southeast-2 | 260 | 15% | 3.1 | 2 (10-02 15:43Z) |
| ap-southeast-3 | 260 | 21% | 3.4 | 4 (10-02 15:43Z) |
| us-east-1 | 260 | 72% | 6.7 | 5 (10-02 15:43Z) |
| us-east-2 | 260 | 76% | 7.3 | 9 (10-02 15:43Z) |
| us-west-2 | 260 | 53% | 5.7 | 9 (10-02 15:43Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   338999999999999922233223443799999999999922499229
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       171115299999999999999911111111111199299999299999
ap-southeast-2   222229592292211222222222222222222222222222222222
ap-southeast-3   154378876811111871111111111111476516111111999114
us-east-1        899594454435959365599993655444333443334455944985
us-east-2        999993343339999999999999999983292998359999999999
us-west-2        224494535553224353332425345545544444544433934499
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 6 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 148 | 64% | 6.8 | 9 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 120 | 66% | 7.0 | 9 (10-02 15:43Z) |
| ap-east-1 ape1-az3 | 113 | 61% | 6.7 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az1 | 122 | 92% | 8.5 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az2 | 58 | 55% | 6.3 | 9 (10-02 15:43Z) |
| ap-northeast-1 apne1-az4 | 152 | 99% | 9.0 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az1 | 204 | 100% | 9.0 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 232 | 100% | 9.0 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az4 | 142 | 67% | 7.0 | 9 (10-02 15:43Z) |
| ap-south-1 aps1-az1 | 81 | 73% | 7.4 | 9 (10-02 15:43Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 101 | 82% | 7.9 | 9 (10-01 21:46Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 92 | 97% | 8.8 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 53 | 98% | 8.9 | 9 (10-02 01:36Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 95 | 99% | 8.9 | 9 (10-01 02:39Z) |
| us-east-2 use2-az2 | 138 | 99% | 8.9 | 9 (10-02 15:43Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 65 | 98% | 8.9 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az2 | 60 | 95% | 8.6 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az3 | 78 | 95% | 8.6 | 9 (10-02 15:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.736400 | 2026-10-02T15:43:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.858300 | 2026-10-02T15:43:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.787400 | 2026-10-02T15:43:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.970400 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591800 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565100 | 2026-10-02T15:43:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-02T15:43:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.648900 | 2026-10-02T15:43:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.356400 | 2026-10-02T15:43:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.696500 | 2026-10-02T15:43:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.359500 | 2026-10-02T15:43:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.730200 | 2026-10-02T15:43:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499100 | 2026-10-02T15:43:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.561400 | 2026-10-02T15:43:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.556500 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1a | Windows | 0.297600 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.438700 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.459900 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.395600 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.445900 | 2026-10-02T15:43:50Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535200 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525900 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2b | Windows | 0.641500 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-02T15:43:50Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.506300 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2a | Windows | 0.332600 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499000 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2b | Windows | 0.332200 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.485200 | 2026-10-02T15:43:50Z |
| us-west-2 | us-west-2c | Windows | 0.331600 | 2026-10-02T15:43:50Z |
