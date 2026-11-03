# Spot placement score log

Generated 2026-11-03 15:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 495 | 49% | 5.2 | 1 (11-03 15:00Z) |
| ap-northeast-1 | 495 | 16% | 2.7 | 9 (11-03 15:00Z) |
| ap-northeast-2 | 495 | 68% | 7.0 | 9 (11-03 15:00Z) |
| ap-south-1 | 495 | 3% | 1.7 | 1 (11-03 15:00Z) |
| ap-southeast-2 | 495 | 0% | 1.0 | 1 (11-03 15:00Z) |
| ap-southeast-3 | 495 | 26% | 3.3 | 1 (11-03 15:00Z) |
| us-east-1 | 495 | 11% | 2.6 | 1 (11-03 15:00Z) |
| us-east-2 | 495 | 30% | 3.7 | 9 (11-03 15:00Z) |
| us-west-2 | 495 | 9% | 2.1 | 2 (11-03 15:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991111119991111199999999911199999999919191
ap-northeast-1   122228711112421114421111121187911147888195119119
ap-northeast-2   999999999999999999911999999999919999999999999999
ap-south-1       112211112111111111111111111111111111111169811111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111786751111111111111111155125411183973138618111
us-east-1        332222222221112222222222222122111111111299991211
us-east-2        911111111111111111111119911121119991196999999119
us-west-2        111111111111111111111111119413111111111171112112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 157 | 6% | 1.6 | 1 (11-03 15:00Z) |
| ap-east-1 ape1-az2 | 366 | 66% | 6.6 | 9 (11-03 06:36Z) |
| ap-northeast-1 apne1-az1 | 108 | 8% | 1.7 | 1 (11-02 23:26Z) |
| ap-northeast-1 apne1-az4 | 223 | 26% | 3.5 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az1 | 425 | 62% | 6.5 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az3 | 462 | 68% | 7.0 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az4 | 488 | 69% | 7.1 | 9 (11-03 15:00Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 136 | 7% | 2.4 | 1 (11-03 15:00Z) |
| ap-southeast-2 apse2-az1 | 95 | 2% | 1.2 | 1 (11-03 06:36Z) |
| ap-southeast-2 apse2-az2 | 64 | 0% | 1.0 | 1 (11-03 15:00Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 310 | 39% | 4.4 | 1 (11-02 23:26Z) |
| us-east-1 use1-az1 | 102 | 0% | 1.1 | 1 (11-02 23:26Z) |
| us-east-1 use1-az2 | 134 | 3% | 1.4 | 9 (11-01 14:59Z) |
| us-east-1 use1-az4 | 161 | 24% | 3.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 159 | 26% | 3.2 | 1 (11-03 06:36Z) |
| us-east-1 use1-az6 | 121 | 25% | 3.1 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 211 | 43% | 4.6 | 9 (11-02 15:37Z) |
| us-east-2 use2-az2 | 254 | 50% | 5.3 | 8 (11-03 15:00Z) |
| us-east-2 use2-az3 | 281 | 47% | 5.1 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 155 | 24% | 3.2 | 1 (11-03 15:00Z) |
| us-west-2 usw2-az2 | 119 | 18% | 2.6 | 1 (11-02 23:26Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 495 | 69% | 7.1 | 9 (11-03 15:00Z) |
| ap-northeast-1 | 495 | 73% | 7.0 | 9 (11-03 15:00Z) |
| ap-northeast-2 | 495 | 100% | 9.0 | 9 (11-03 15:00Z) |
| ap-south-1 | 495 | 62% | 6.3 | 1 (11-03 15:00Z) |
| ap-southeast-2 | 495 | 24% | 3.4 | 9 (11-03 15:00Z) |
| ap-southeast-3 | 495 | 26% | 3.3 | 1 (11-03 15:00Z) |
| us-east-1 | 495 | 70% | 6.4 | 3 (11-03 15:00Z) |
| us-east-2 | 495 | 67% | 6.7 | 9 (11-03 15:00Z) |
| us-west-2 | 495 | 52% | 5.6 | 4 (11-03 15:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   339999999999999999999999999999999999999999929999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       112211112999999999999799999999999999999999911911
ap-southeast-2   111111111111119999999111319999999999999199111119
ap-southeast-3   111786751111111111111111155125411183973138618111
us-east-1        999932323334339394399999999999322999999999994523
us-east-2        993222222222222228999999999999929991999999999199
us-west-2        999994844395931211233244999549992999999999449244
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 318 | 83% | 8.0 | 9 (11-03 15:00Z) |
| ap-east-1 ape1-az2 | 276 | 85% | 8.1 | 9 (11-03 15:00Z) |
| ap-east-1 ape1-az3 | 305 | 86% | 8.1 | 9 (11-03 15:00Z) |
| ap-northeast-1 apne1-az1 | 205 | 95% | 8.7 | 9 (11-01 07:25Z) |
| ap-northeast-1 apne1-az2 | 179 | 85% | 8.1 | 9 (11-03 15:00Z) |
| ap-northeast-1 apne1-az4 | 263 | 99% | 8.9 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az1 | 405 | 100% | 9.0 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 423 | 100% | 9.0 | 9 (11-03 15:00Z) |
| ap-northeast-2 apne2-az4 | 320 | 85% | 8.1 | 9 (11-03 15:00Z) |
| ap-south-1 aps1-az1 | 172 | 87% | 8.2 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az2 | 183 | 80% | 7.7 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az3 | 192 | 90% | 8.4 | 9 (11-02 23:26Z) |
| ap-southeast-2 apse2-az1 | 60 | 83% | 8.0 | 9 (11-03 15:00Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 103 | 98% | 8.9 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 124 | 92% | 8.4 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 175 | 99% | 8.9 | 9 (11-03 06:36Z) |
| us-east-2 use2-az2 | 193 | 99% | 8.9 | 9 (11-03 06:36Z) |
| us-east-2 use2-az3 | 221 | 96% | 8.7 | 9 (11-03 15:00Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 126 | 90% | 8.3 | 9 (11-02 15:37Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722800 | 2026-11-03T15:00:23Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-03T15:00:23Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732400 | 2026-11-03T15:00:23Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579700 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590200 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572300 | 2026-11-03T15:00:23Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-03T15:00:23Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.622000 | 2026-11-03T15:00:23Z |
| ap-south-1 | ap-south-1a | Windows | 0.449400 | 2026-11-03T15:00:23Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.514600 | 2026-11-03T15:00:23Z |
| ap-south-1 | ap-south-1b | Windows | 0.372000 | 2026-11-03T15:00:23Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.608100 | 2026-11-03T15:00:23Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510400 | 2026-11-03T15:00:23Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.723700 | 2026-11-03T15:00:23Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.503100 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.548300 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.483900 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.490800 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.564800 | 2026-11-03T15:00:23Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.556900 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550200 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547400 | 2026-11-03T15:00:23Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.588400 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2a | Windows | 0.308800 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.629400 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2b | Windows | 0.321700 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.590700 | 2026-11-03T15:00:23Z |
| us-west-2 | us-west-2c | Windows | 0.308200 | 2026-11-03T15:00:23Z |
