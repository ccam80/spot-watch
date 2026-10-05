# Spot placement score log

Generated 2026-10-05 00:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 272 | 34% | 4.3 | 1 (10-05 00:49Z) |
| ap-northeast-1 | 272 | 15% | 2.8 | 1 (10-05 00:49Z) |
| ap-northeast-2 | 272 | 44% | 5.6 | 9 (10-05 00:49Z) |
| ap-south-1 | 272 | 2% | 1.8 | 2 (10-05 00:49Z) |
| ap-southeast-2 | 272 | 0% | 1.0 | 1 (10-05 00:49Z) |
| ap-southeast-3 | 272 | 20% | 3.2 | 1 (10-05 00:49Z) |
| us-east-1 | 272 | 10% | 2.6 | 9 (10-05 00:49Z) |
| us-east-2 | 272 | 27% | 3.6 | 9 (10-05 00:49Z) |
| us-west-2 | 272 | 12% | 2.4 | 9 (10-05 00:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999998999991111119939911911999981211
ap-northeast-1   796122212222221111899127998121298219999999999991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111122111111111111111111111111111211111111111222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111871111111111111476516111111999114111111111111
us-east-1        129122299991322222222232222211922922233119919999
us-east-2        169999111999999911111817121899999999119999999999
us-west-2        111121111112112222222222212111222121299999999199
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 4 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 90 | 0% | 1.4 | 2 (10-04 18:06Z) |
| ap-east-1 ape1-az2 | 191 | 48% | 5.6 | 8 (10-04 06:47Z) |
| ap-northeast-1 apne1-az1 | 41 | 7% | 1.8 | 2 (10-03 17:12Z) |
| ap-northeast-1 apne1-az4 | 131 | 25% | 3.6 | 9 (10-04 21:19Z) |
| ap-northeast-2 apne2-az1 | 239 | 42% | 5.4 | 6 (10-04 06:47Z) |
| ap-northeast-2 apne2-az3 | 251 | 46% | 5.7 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az4 | 269 | 44% | 5.6 | 9 (10-05 00:49Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 52 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 74 | 4% | 1.6 | 9 (10-05 00:49Z) |
| us-east-1 use1-az4 | 85 | 28% | 3.5 | 9 (10-05 00:49Z) |
| us-east-1 use1-az5 | 87 | 25% | 3.3 | 9 (10-05 00:49Z) |
| us-east-1 use1-az6 | 67 | 22% | 3.1 | 9 (10-05 00:49Z) |
| us-east-2 use2-az1 | 110 | 38% | 4.4 | 9 (10-05 00:49Z) |
| us-east-2 use2-az2 | 143 | 44% | 5.0 | 9 (10-05 00:49Z) |
| us-east-2 use2-az3 | 167 | 42% | 4.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az1 | 90 | 31% | 4.0 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 53 | 26% | 3.6 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az3 | 115 | 22% | 3.3 | 9 (10-05 00:49Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 272 | 44% | 5.6 | 9 (10-05 00:49Z) |
| ap-northeast-1 | 272 | 74% | 7.2 | 9 (10-05 00:49Z) |
| ap-northeast-2 | 272 | 100% | 9.0 | 9 (10-05 00:49Z) |
| ap-south-1 | 272 | 59% | 6.3 | 9 (10-05 00:49Z) |
| ap-southeast-2 | 272 | 16% | 3.2 | 2 (10-05 00:49Z) |
| ap-southeast-3 | 272 | 20% | 3.2 | 1 (10-05 00:49Z) |
| us-east-1 | 272 | 72% | 6.7 | 9 (10-05 00:49Z) |
| us-east-2 | 272 | 76% | 7.4 | 9 (10-05 00:49Z) |
| us-west-2 | 272 | 55% | 5.9 | 9 (10-05 00:49Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999922233223443799999999999922499229999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999911111111111199299999299999999999999999
ap-southeast-2   211222222222222222222222222222222222222222929992
ap-southeast-3   111871111111111111476516111111999114111111111111
us-east-1        959365599993655444333443334455944985576349999999
us-east-2        999999999999999983292998359999999999399999999999
us-west-2        224353332425345545544444544433934499599999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 156 | 65% | 6.9 | 9 (10-05 00:49Z) |
| ap-east-1 ape1-az2 | 125 | 67% | 7.0 | 9 (10-05 00:49Z) |
| ap-east-1 ape1-az3 | 121 | 64% | 6.8 | 9 (10-05 00:49Z) |
| ap-northeast-1 apne1-az1 | 129 | 92% | 8.5 | 9 (10-04 21:19Z) |
| ap-northeast-1 apne1-az2 | 64 | 59% | 6.6 | 9 (10-04 06:47Z) |
| ap-northeast-1 apne1-az4 | 157 | 99% | 9.0 | 9 (10-04 21:19Z) |
| ap-northeast-2 apne2-az1 | 210 | 100% | 9.0 | 9 (10-05 00:49Z) |
| ap-northeast-2 apne2-az2 | 61 | 77% | 7.6 | 9 (10-04 21:19Z) |
| ap-northeast-2 apne2-az3 | 234 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az4 | 148 | 68% | 7.1 | 9 (10-04 21:19Z) |
| ap-south-1 aps1-az1 | 90 | 76% | 7.5 | 9 (10-05 00:49Z) |
| ap-south-1 aps1-az2 | 96 | 62% | 6.7 | 9 (10-04 21:19Z) |
| ap-south-1 aps1-az3 | 107 | 83% | 8.0 | 9 (10-05 00:49Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 31 | 61% | 6.7 | 9 (10-04 18:06Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 95 | 97% | 8.8 | 9 (10-04 13:09Z) |
| us-east-1 use1-az5 | 57 | 98% | 8.9 | 9 (10-05 00:49Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 99 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-east-2 use2-az2 | 145 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-east-2 use2-az3 | 127 | 94% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az1 | 71 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.719300 | 2026-10-05T00:49:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-05T00:49:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.772800 | 2026-10-05T00:49:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956800 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596700 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577100 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565400 | 2026-10-05T00:49:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743600 | 2026-10-05T00:49:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.656800 | 2026-10-05T00:49:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.370100 | 2026-10-05T00:49:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.715600 | 2026-10-05T00:49:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.361300 | 2026-10-05T00:49:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.720800 | 2026-10-05T00:49:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502600 | 2026-10-05T00:49:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.512100 | 2026-10-05T00:49:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.573000 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1a | Windows | 0.285700 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.443400 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.482300 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.412000 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.503900 | 2026-10-05T00:49:05Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534900 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527900 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2b | Windows | 0.640900 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515800 | 2026-10-05T00:49:05Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.508300 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2a | Windows | 0.330800 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491600 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2b | Windows | 0.332100 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.480400 | 2026-10-05T00:49:05Z |
| us-west-2 | us-west-2c | Windows | 0.329600 | 2026-10-05T00:49:05Z |
