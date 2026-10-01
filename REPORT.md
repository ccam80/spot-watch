# Spot placement score log

Generated 2026-10-01 21:46 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 257 | 33% | 4.3 | 9 (10-01 21:46Z) |
| ap-northeast-1 | 257 | 11% | 2.5 | 8 (10-01 21:46Z) |
| ap-northeast-2 | 257 | 40% | 5.4 | 9 (10-01 21:46Z) |
| ap-south-1 | 257 | 2% | 1.8 | 1 (10-01 21:46Z) |
| ap-southeast-2 | 257 | 0% | 1.0 | 1 (10-01 21:46Z) |
| ap-southeast-3 | 257 | 21% | 3.4 | 9 (10-01 21:46Z) |
| us-east-1 | 257 | 8% | 2.4 | 2 (10-01 21:46Z) |
| us-east-2 | 257 | 24% | 3.4 | 9 (10-01 21:46Z) |
| us-west-2 | 257 | 9% | 2.2 | 2 (10-01 21:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999998999991111119939
ap-northeast-1   211121148188213796122212222221111899127998121298
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111122111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111154378876811111871111111111111476516111111999
us-east-1        111122111221111129122299991322222222232222211922
us-east-2        199999991111119169999111999999911111817121899999
us-west-2        111111111222221111121111112112222222222212111222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 6 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 1 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 88 | 0% | 1.4 | 1 (10-01 01:09Z) |
| ap-east-1 ape1-az2 | 185 | 46% | 5.5 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az1 | 36 | 0% | 1.3 | 2 (10-01 17:00Z) |
| ap-northeast-1 apne1-az4 | 118 | 18% | 3.1 | 8 (10-01 21:46Z) |
| ap-northeast-2 apne2-az1 | 231 | 40% | 5.3 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az3 | 239 | 44% | 5.6 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az4 | 254 | 41% | 5.4 | 9 (10-01 21:46Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 98 | 3% | 2.5 | 1 (09-30 23:20Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 25 | 0% | 1.0 | 1 (09-30 23:20Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 185 | 28% | 4.1 | 9 (10-01 21:46Z) |
| us-east-1 use1-az1 | 39 | 0% | 1.2 | 1 (10-01 21:46Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 79 | 23% | 3.1 | 1 (10-01 21:46Z) |
| us-east-1 use1-az5 | 79 | 20% | 2.9 | 1 (10-01 01:09Z) |
| us-east-1 use1-az6 | 60 | 15% | 2.5 | 9 (10-01 10:01Z) |
| us-east-2 use2-az1 | 101 | 33% | 4.0 | 9 (10-01 10:01Z) |
| us-east-2 use2-az2 | 131 | 39% | 4.6 | 9 (10-01 21:46Z) |
| us-east-2 use2-az3 | 154 | 37% | 4.6 | 9 (10-01 21:46Z) |
| us-west-2 usw2-az1 | 81 | 25% | 3.5 | 1 (10-01 02:39Z) |
| us-west-2 usw2-az2 | 49 | 22% | 3.3 | 1 (10-01 17:00Z) |
| us-west-2 usw2-az3 | 106 | 17% | 2.9 | 1 (09-30 19:21Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 257 | 40% | 5.4 | 9 (10-01 21:46Z) |
| ap-northeast-1 | 257 | 74% | 7.2 | 9 (10-01 21:46Z) |
| ap-northeast-2 | 257 | 100% | 9.0 | 9 (10-01 21:46Z) |
| ap-south-1 | 257 | 57% | 6.1 | 9 (10-01 21:46Z) |
| ap-southeast-2 | 257 | 15% | 3.1 | 2 (10-01 21:46Z) |
| ap-southeast-3 | 257 | 21% | 3.4 | 9 (10-01 21:46Z) |
| us-east-1 | 257 | 71% | 6.7 | 4 (10-01 21:46Z) |
| us-east-2 | 257 | 75% | 7.3 | 9 (10-01 21:46Z) |
| us-west-2 | 257 | 53% | 5.7 | 4 (10-01 21:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   223338999999999999922233223443799999999999922499
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       942171115299999999999999911111111111199299999299
ap-southeast-2   222222229592292211222222222222222222222222222222
ap-southeast-3   111154378876811111871111111111111476516111111999
us-east-1        794899594454435959365599993655444333443334455944
us-east-2        999999993343339999999999999999983292998359999999
us-west-2        299224494535553224353332425345545544444544433934
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 6 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 6 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 4 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 146 | 63% | 6.8 | 9 (10-01 21:46Z) |
| ap-east-1 ape1-az2 | 117 | 65% | 6.9 | 9 (10-01 17:00Z) |
| ap-east-1 ape1-az3 | 113 | 61% | 6.7 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az1 | 122 | 92% | 8.5 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az2 | 57 | 54% | 6.3 | 9 (10-01 21:46Z) |
| ap-northeast-1 apne1-az4 | 152 | 99% | 9.0 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az1 | 201 | 100% | 9.0 | 9 (10-01 21:46Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 229 | 100% | 9.0 | 9 (10-01 10:01Z) |
| ap-northeast-2 apne2-az4 | 139 | 66% | 7.0 | 9 (10-01 17:00Z) |
| ap-south-1 aps1-az1 | 78 | 72% | 7.3 | 9 (10-01 21:46Z) |
| ap-south-1 aps1-az2 | 93 | 61% | 6.7 | 9 (10-01 21:46Z) |
| ap-south-1 aps1-az3 | 101 | 82% | 7.9 | 9 (10-01 21:46Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 91 | 97% | 8.8 | 9 (10-01 10:01Z) |
| us-east-1 use1-az5 | 52 | 98% | 8.9 | 9 (10-01 10:01Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 95 | 99% | 8.9 | 9 (10-01 02:39Z) |
| us-east-2 use2-az2 | 135 | 99% | 8.9 | 9 (10-01 21:46Z) |
| us-east-2 use2-az3 | 123 | 93% | 8.6 | 9 (10-01 17:00Z) |
| us-west-2 usw2-az1 | 64 | 98% | 8.9 | 9 (10-01 10:01Z) |
| us-west-2 usw2-az2 | 59 | 95% | 8.6 | 2 (09-30 12:38Z) |
| us-west-2 usw2-az3 | 76 | 95% | 8.6 | 9 (10-01 10:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.735800 | 2026-10-01T21:46:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.865100 | 2026-10-01T21:46:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.792400 | 2026-10-01T21:46:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.965400 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592100 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.576600 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565400 | 2026-10-01T21:46:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-01T21:46:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.638300 | 2026-10-01T21:46:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.356500 | 2026-10-01T21:46:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.692300 | 2026-10-01T21:46:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.356900 | 2026-10-01T21:46:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729600 | 2026-10-01T21:46:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-10-01T21:46:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.584900 | 2026-10-01T21:46:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.556000 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1a | Windows | 0.299800 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.440800 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.451900 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.397000 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.441700 | 2026-10-01T21:46:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.531600 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523400 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2b | Windows | 0.641200 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513200 | 2026-10-01T21:46:32Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.508200 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2a | Windows | 0.332300 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.499800 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2b | Windows | 0.332000 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.485900 | 2026-10-01T21:46:32Z |
| us-west-2 | us-west-2c | Windows | 0.331200 | 2026-10-01T21:46:32Z |
