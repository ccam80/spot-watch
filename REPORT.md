# Spot placement score log

Generated 2026-10-05 22:33 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 275 | 34% | 4.3 | 1 (10-05 22:33Z) |
| ap-northeast-1 | 275 | 15% | 2.8 | 1 (10-05 22:33Z) |
| ap-northeast-2 | 275 | 44% | 5.6 | 9 (10-05 22:33Z) |
| ap-south-1 | 275 | 2% | 1.8 | 2 (10-05 22:33Z) |
| ap-southeast-2 | 275 | 0% | 1.0 | 1 (10-05 22:33Z) |
| ap-southeast-3 | 275 | 20% | 3.2 | 1 (10-05 22:33Z) |
| us-east-1 | 275 | 10% | 2.6 | 1 (10-05 22:33Z) |
| us-east-2 | 275 | 27% | 3.6 | 1 (10-05 22:33Z) |
| us-west-2 | 275 | 12% | 2.4 | 2 (10-05 22:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999998999991111119939911911999981211111
ap-northeast-1   122212222221111899127998121298219999999999991191
ap-northeast-2   999999999999999999999999999999999999999999999149
ap-south-1       122111111111111111111111111111211111111111222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   871111111111111476516111111999114111111111111111
us-east-1        122299991322222222232222211922922233119919999921
us-east-2        999111999999911111817121899999999119999999999911
us-west-2        121111112112222222222212111222121299999999199112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 4 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 92 | 0% | 1.4 | 1 (10-05 22:33Z) |
| ap-east-1 ape1-az2 | 192 | 48% | 5.5 | 1 (10-05 06:55Z) |
| ap-northeast-1 apne1-az1 | 42 | 10% | 1.9 | 7 (10-05 15:54Z) |
| ap-northeast-1 apne1-az4 | 133 | 26% | 3.6 | 1 (10-05 22:33Z) |
| ap-northeast-2 apne2-az1 | 240 | 42% | 5.4 | 1 (10-05 06:55Z) |
| ap-northeast-2 apne2-az3 | 251 | 46% | 5.7 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az4 | 272 | 44% | 5.6 | 9 (10-05 22:33Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 103 | 3% | 2.4 | 1 (10-05 22:33Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 54 | 0% | 1.0 | 1 (10-05 22:33Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 75 | 4% | 1.6 | 1 (10-05 22:33Z) |
| us-east-1 use1-az4 | 86 | 29% | 3.6 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 88 | 26% | 3.4 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 69 | 22% | 3.0 | 1 (10-05 22:33Z) |
| us-east-2 use2-az1 | 111 | 39% | 4.4 | 9 (10-05 06:55Z) |
| us-east-2 use2-az2 | 146 | 44% | 4.9 | 1 (10-05 22:33Z) |
| us-east-2 use2-az3 | 168 | 42% | 5.0 | 9 (10-05 06:55Z) |
| us-west-2 usw2-az1 | 93 | 30% | 3.9 | 1 (10-05 22:33Z) |
| us-west-2 usw2-az2 | 53 | 26% | 3.6 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az3 | 117 | 21% | 3.2 | 1 (10-05 22:33Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 275 | 44% | 5.7 | 9 (10-05 22:33Z) |
| ap-northeast-1 | 275 | 74% | 7.2 | 9 (10-05 22:33Z) |
| ap-northeast-2 | 275 | 100% | 9.0 | 9 (10-05 22:33Z) |
| ap-south-1 | 275 | 59% | 6.2 | 9 (10-05 22:33Z) |
| ap-southeast-2 | 275 | 16% | 3.2 | 1 (10-05 22:33Z) |
| ap-southeast-3 | 275 | 20% | 3.2 | 1 (10-05 22:33Z) |
| us-east-1 | 275 | 72% | 6.7 | 5 (10-05 22:33Z) |
| us-east-2 | 275 | 76% | 7.3 | 3 (10-05 22:33Z) |
| us-west-2 | 275 | 55% | 5.9 | 3 (10-05 22:33Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   922233223443799999999999922499229999999999999199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999911111111111199299999299999999999999999229
ap-southeast-2   222222222222222222222222222222222222222929992291
ap-southeast-3   871111111111111476516111111999114111111111111111
us-east-1        365599993655444333443334455944985576349999999955
us-east-2        999999999999983292998359999999999399999999999923
us-west-2        353332425345545544444544433934499599999999999943
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 7 | 5 | 7 | 5 | 6 | 6 | 5 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 159 | 66% | 7.0 | 9 (10-05 22:33Z) |
| ap-east-1 ape1-az2 | 128 | 68% | 7.1 | 9 (10-05 22:33Z) |
| ap-east-1 ape1-az3 | 124 | 65% | 6.9 | 9 (10-05 22:33Z) |
| ap-northeast-1 apne1-az1 | 129 | 92% | 8.5 | 9 (10-04 21:19Z) |
| ap-northeast-1 apne1-az2 | 66 | 61% | 6.6 | 9 (10-05 22:33Z) |
| ap-northeast-1 apne1-az4 | 159 | 99% | 9.0 | 9 (10-05 22:33Z) |
| ap-northeast-2 apne2-az1 | 213 | 100% | 9.0 | 9 (10-05 22:33Z) |
| ap-northeast-2 apne2-az2 | 62 | 77% | 7.6 | 9 (10-05 15:54Z) |
| ap-northeast-2 apne2-az3 | 237 | 100% | 9.0 | 9 (10-05 22:33Z) |
| ap-northeast-2 apne2-az4 | 151 | 69% | 7.1 | 9 (10-05 22:33Z) |
| ap-south-1 aps1-az1 | 90 | 76% | 7.5 | 9 (10-05 00:49Z) |
| ap-south-1 aps1-az2 | 97 | 63% | 6.8 | 9 (10-05 22:33Z) |
| ap-south-1 aps1-az3 | 108 | 83% | 8.0 | 9 (10-05 22:33Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 32 | 62% | 6.8 | 9 (10-05 15:54Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 96 | 97% | 8.8 | 9 (10-05 06:55Z) |
| us-east-1 use1-az5 | 58 | 98% | 8.9 | 9 (10-05 06:55Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 100 | 99% | 8.9 | 9 (10-05 06:55Z) |
| us-east-2 use2-az2 | 145 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-east-2 use2-az3 | 128 | 94% | 8.6 | 9 (10-05 06:55Z) |
| us-west-2 usw2-az1 | 71 | 99% | 8.9 | 9 (10-05 00:49Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710600 | 2026-10-05T22:33:40Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-05T22:33:40Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.763500 | 2026-10-05T22:33:40Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.946500 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.602400 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577200 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565100 | 2026-10-05T22:33:40Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-10-05T22:33:40Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.651500 | 2026-10-05T22:33:40Z |
| ap-south-1 | ap-south-1a | Windows | 0.375100 | 2026-10-05T22:33:40Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.724000 | 2026-10-05T22:33:40Z |
| ap-south-1 | ap-south-1b | Windows | 0.358600 | 2026-10-05T22:33:40Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.717300 | 2026-10-05T22:33:40Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502900 | 2026-10-05T22:33:40Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.498800 | 2026-10-05T22:33:40Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.590300 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.452700 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.482400 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.404700 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.502800 | 2026-10-05T22:33:40Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.533400 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528600 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-10-05T22:33:40Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.510800 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2a | Windows | 0.329800 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.486400 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2b | Windows | 0.331300 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.478500 | 2026-10-05T22:33:40Z |
| us-west-2 | us-west-2c | Windows | 0.328900 | 2026-10-05T22:33:40Z |
