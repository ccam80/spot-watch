# Spot placement score log

Generated 2026-10-03 06:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 263 | 33% | 4.3 | 1 (10-03 06:23Z) |
| ap-northeast-1 | 263 | 13% | 2.6 | 9 (10-03 06:23Z) |
| ap-northeast-2 | 263 | 42% | 5.5 | 9 (10-03 06:23Z) |
| ap-south-1 | 263 | 2% | 1.8 | 1 (10-03 06:23Z) |
| ap-southeast-2 | 263 | 0% | 1.0 | 1 (10-03 06:23Z) |
| ap-southeast-3 | 263 | 21% | 3.3 | 1 (10-03 06:23Z) |
| us-east-1 | 263 | 8% | 2.5 | 3 (10-03 06:23Z) |
| us-east-2 | 263 | 25% | 3.4 | 9 (10-03 06:23Z) |
| us-west-2 | 263 | 9% | 2.2 | 9 (10-03 06:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999998999991111119939911911
ap-northeast-1   148188213796122212222221111899127998121298219999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111122111111111111111111111111111211111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   378876811111871111111111111476516111111999114111
us-east-1        111221111129122299991322222222232222211922922233
us-east-2        991111119169999111999999911111817121899999999119
us-west-2        111222221111121111112112222222222212111222121299
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 3 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 187 | 47% | 5.5 | 9 (10-02 20:39Z) |
| ap-northeast-1 apne1-az1 | 40 | 8% | 1.8 | 6 (10-03 06:23Z) |
| ap-northeast-1 apne1-az4 | 123 | 20% | 3.3 | 9 (10-03 06:23Z) |
| ap-northeast-2 apne2-az1 | 237 | 41% | 5.4 | 9 (10-03 06:23Z) |
| ap-northeast-2 apne2-az3 | 245 | 45% | 5.6 | 9 (10-03 06:23Z) |
| ap-northeast-2 apne2-az4 | 260 | 42% | 5.5 | 9 (10-03 06:23Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 80 | 24% | 3.2 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 82 | 21% | 3.0 | 1 (10-02 15:43Z) |
| us-east-1 use1-az6 | 61 | 15% | 2.5 | 1 (10-03 06:23Z) |
| us-east-2 use2-az1 | 104 | 35% | 4.1 | 9 (10-03 06:23Z) |
| us-east-2 use2-az2 | 134 | 40% | 4.7 | 9 (10-03 06:23Z) |
| us-east-2 use2-az3 | 158 | 39% | 4.7 | 9 (10-03 06:23Z) |
| us-west-2 usw2-az1 | 83 | 25% | 3.6 | 9 (10-03 06:23Z) |
| us-west-2 usw2-az2 | 50 | 22% | 3.3 | 1 (10-03 00:24Z) |
| us-west-2 usw2-az3 | 108 | 17% | 2.9 | 4 (10-03 00:24Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 263 | 42% | 5.5 | 9 (10-03 06:23Z) |
| ap-northeast-1 | 263 | 73% | 7.2 | 9 (10-03 06:23Z) |
| ap-northeast-2 | 263 | 100% | 9.0 | 9 (10-03 06:23Z) |
| ap-south-1 | 263 | 58% | 6.2 | 9 (10-03 06:23Z) |
| ap-southeast-2 | 263 | 15% | 3.1 | 2 (10-03 06:23Z) |
| ap-southeast-3 | 263 | 21% | 3.3 | 1 (10-03 06:23Z) |
| us-east-1 | 263 | 72% | 6.7 | 6 (10-03 06:23Z) |
| us-east-2 | 263 | 76% | 7.3 | 9 (10-03 06:23Z) |
| us-west-2 | 263 | 53% | 5.7 | 9 (10-03 06:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999922233223443799999999999922499229999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       115299999999999999911111111111199299999299999999
ap-southeast-2   229592292211222222222222222222222222222222222222
ap-southeast-3   378876811111871111111111111476516111111999114111
us-east-1        594454435959365599993655444333443334455944985576
us-east-2        993343339999999999999999983292998359999999999399
us-west-2        494535553224353332425345545544444544433934499599
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 151 | 64% | 6.9 | 9 (10-03 06:23Z) |
| ap-east-1 ape1-az2 | 122 | 66% | 7.0 | 9 (10-03 00:24Z) |
| ap-east-1 ape1-az3 | 116 | 62% | 6.7 | 9 (10-03 06:23Z) |
| ap-northeast-1 apne1-az1 | 125 | 92% | 8.5 | 9 (10-03 06:23Z) |
| ap-northeast-1 apne1-az2 | 61 | 57% | 6.4 | 9 (10-03 06:23Z) |
| ap-northeast-1 apne1-az4 | 153 | 99% | 9.0 | 9 (10-03 06:23Z) |
| ap-northeast-2 apne2-az1 | 207 | 100% | 9.0 | 9 (10-03 06:23Z) |
| ap-northeast-2 apne2-az2 | 55 | 75% | 7.4 | 9 (10-02 20:39Z) |
| ap-northeast-2 apne2-az3 | 232 | 100% | 9.0 | 9 (10-02 15:43Z) |
| ap-northeast-2 apne2-az4 | 143 | 67% | 7.0 | 9 (10-02 20:39Z) |
| ap-south-1 aps1-az1 | 84 | 74% | 7.4 | 9 (10-03 06:23Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 103 | 83% | 8.0 | 9 (10-03 00:24Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 92 | 97% | 8.8 | 9 (10-02 01:36Z) |
| us-east-1 use1-az5 | 53 | 98% | 8.9 | 9 (10-02 01:36Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 97 | 99% | 8.9 | 9 (10-03 06:23Z) |
| us-east-2 use2-az2 | 140 | 99% | 8.9 | 9 (10-03 06:23Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 66 | 98% | 8.9 | 9 (10-03 06:23Z) |
| us-west-2 usw2-az2 | 60 | 95% | 8.6 | 9 (10-02 15:43Z) |
| us-west-2 usw2-az3 | 78 | 95% | 8.6 | 9 (10-02 15:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.729300 | 2026-10-03T06:23:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-03T06:23:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.781200 | 2026-10-03T06:23:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964200 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592400 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565100 | 2026-10-03T06:23:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743500 | 2026-10-03T06:23:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.647600 | 2026-10-03T06:23:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.360000 | 2026-10-03T06:23:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.699100 | 2026-10-03T06:23:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.359700 | 2026-10-03T06:23:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729000 | 2026-10-03T06:23:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-10-03T06:23:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.550900 | 2026-10-03T06:23:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.574500 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1a | Windows | 0.295100 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.444200 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.465900 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.404400 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.458500 | 2026-10-03T06:23:35Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535000 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2a | Windows | 0.641600 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527200 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2b | Windows | 0.641500 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-03T06:23:35Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.502500 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.497500 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.482400 | 2026-10-03T06:23:35Z |
| us-west-2 | us-west-2c | Windows | 0.331700 | 2026-10-03T06:23:35Z |
