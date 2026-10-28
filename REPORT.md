# Spot placement score log

Generated 2026-10-28 10:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 400 | 47% | 5.2 | 9 (10-28 10:17Z) |
| ap-northeast-1 | 400 | 16% | 2.8 | 1 (10-28 10:17Z) |
| ap-northeast-2 | 400 | 61% | 6.6 | 9 (10-28 10:17Z) |
| ap-south-1 | 400 | 3% | 1.8 | 1 (10-28 10:17Z) |
| ap-southeast-2 | 400 | 0% | 1.1 | 1 (10-28 10:17Z) |
| ap-southeast-3 | 400 | 27% | 3.5 | 1 (10-28 10:17Z) |
| us-east-1 | 400 | 12% | 2.7 | 3 (10-28 10:17Z) |
| us-east-2 | 400 | 33% | 3.9 | 9 (10-28 10:17Z) |
| us-west-2 | 400 | 11% | 2.3 | 1 (10-28 10:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999919999999999999999999999999999111111999999
ap-northeast-1   128211249999949999192921122113122222211111111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       221111111111114999111691111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   159911919112858742898861271118648854111111111111
us-east-1        512322223221991993997299921923322233311122111223
us-east-2        911119111199999919399199911196111999911191119999
us-west-2        512112212222222119191911121211111111111111121111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 8 | 5 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 127 | 7% | 1.7 | 1 (10-28 10:17Z) |
| ap-east-1 ape1-az2 | 300 | 62% | 6.4 | 9 (10-28 10:17Z) |
| ap-northeast-1 apne1-az1 | 70 | 6% | 1.6 | 1 (10-28 08:21Z) |
| ap-northeast-1 apne1-az4 | 181 | 29% | 3.8 | 1 (10-28 05:16Z) |
| ap-northeast-2 apne2-az1 | 349 | 54% | 6.1 | 2 (10-28 08:21Z) |
| ap-northeast-2 apne2-az3 | 369 | 60% | 6.5 | 7 (10-28 10:17Z) |
| ap-northeast-2 apne2-az4 | 396 | 61% | 6.7 | 9 (10-28 10:17Z) |
| ap-south-1 aps1-az1 | 98 | 1% | 1.5 | 1 (10-28 10:17Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 68 | 3% | 1.3 | 1 (10-28 08:21Z) |
| ap-southeast-2 apse2-az2 | 42 | 0% | 1.0 | 1 (10-28 06:26Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 265 | 39% | 4.5 | 1 (10-28 04:19Z) |
| us-east-1 use1-az1 | 76 | 0% | 1.1 | 1 (10-28 06:26Z) |
| us-east-1 use1-az2 | 105 | 3% | 1.4 | 1 (10-28 05:16Z) |
| us-east-1 use1-az4 | 125 | 29% | 3.5 | 1 (10-28 06:26Z) |
| us-east-1 use1-az5 | 131 | 29% | 3.5 | 1 (10-28 08:21Z) |
| us-east-1 use1-az6 | 94 | 29% | 3.4 | 1 (10-28 10:17Z) |
| us-east-2 use2-az1 | 166 | 47% | 5.0 | 9 (10-28 10:17Z) |
| us-east-2 use2-az2 | 214 | 53% | 5.5 | 9 (10-28 10:17Z) |
| us-east-2 use2-az3 | 247 | 49% | 5.3 | 9 (10-28 10:17Z) |
| us-west-2 usw2-az1 | 137 | 26% | 3.5 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az2 | 93 | 22% | 3.0 | 1 (10-28 08:21Z) |
| us-west-2 usw2-az3 | 150 | 21% | 3.1 | 1 (10-28 10:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 400 | 62% | 6.7 | 9 (10-28 10:17Z) |
| ap-northeast-1 | 400 | 72% | 7.0 | 2 (10-28 10:17Z) |
| ap-northeast-2 | 400 | 100% | 9.0 | 9 (10-28 10:17Z) |
| ap-south-1 | 400 | 63% | 6.5 | 1 (10-28 10:17Z) |
| ap-southeast-2 | 400 | 20% | 3.2 | 9 (10-28 10:17Z) |
| ap-southeast-3 | 400 | 27% | 3.5 | 1 (10-28 10:17Z) |
| us-east-1 | 400 | 71% | 6.5 | 6 (10-28 10:17Z) |
| us-east-2 | 400 | 72% | 7.0 | 9 (10-28 10:17Z) |
| us-west-2 | 400 | 51% | 5.6 | 3 (10-28 10:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399923999999999999999991999119999999922111111222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299999199999999999999999199112119999999999111111
ap-southeast-2   111111111111191999999111111111199111111111111199
ap-southeast-3   159911919112858742898861271118648854111111111111
us-east-1        924656456599999999999999943995544576699696544596
us-east-2        972219522699999919899399999999999999999999999999
us-west-2        993334545345999549999934944591133333433333355943
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 248 | 78% | 7.7 | 9 (10-28 10:17Z) |
| ap-east-1 ape1-az2 | 210 | 80% | 7.8 | 9 (10-28 10:17Z) |
| ap-east-1 ape1-az3 | 223 | 80% | 7.8 | 9 (10-28 10:17Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 321 | 100% | 9.0 | 9 (10-28 10:17Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 344 | 100% | 9.0 | 9 (10-28 10:17Z) |
| ap-northeast-2 apne2-az4 | 248 | 81% | 7.9 | 9 (10-28 10:17Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 36 | 72% | 7.3 | 9 (10-28 09:18Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 47 | 72% | 7.3 | 9 (10-28 10:17Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 116 | 94% | 8.6 | 9 (10-28 09:18Z) |
| us-east-1 use1-az5 | 86 | 98% | 8.8 | 9 (10-28 09:18Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 147 | 99% | 8.9 | 9 (10-28 10:17Z) |
| us-east-2 use2-az2 | 181 | 99% | 8.9 | 9 (10-28 10:17Z) |
| us-east-2 use2-az3 | 191 | 96% | 8.7 | 9 (10-28 10:17Z) |
| us-west-2 usw2-az1 | 84 | 98% | 8.8 | 9 (10-28 08:21Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 100 | 92% | 8.4 | 2 (10-28 07:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703500 | 2026-10-28T10:17:18Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T10:17:18Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790600 | 2026-10-28T10:17:18Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.973600 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584700 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570600 | 2026-10-28T10:17:18Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T10:17:18Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.571500 | 2026-10-28T10:17:18Z |
| ap-south-1 | ap-south-1a | Windows | 0.456800 | 2026-10-28T10:17:18Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.632800 | 2026-10-28T10:17:18Z |
| ap-south-1 | ap-south-1b | Windows | 0.402700 | 2026-10-28T10:17:18Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656200 | 2026-10-28T10:17:18Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517700 | 2026-10-28T10:17:18Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660700 | 2026-10-28T10:17:18Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.595800 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.475100 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524700 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520500 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.542100 | 2026-10-28T10:17:18Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.565300 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-28T10:17:18Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566000 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2a | Windows | 0.319200 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2b | Windows | 0.327200 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.562900 | 2026-10-28T10:17:18Z |
| us-west-2 | us-west-2c | Windows | 0.318800 | 2026-10-28T10:17:18Z |
