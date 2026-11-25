# Spot placement score log

Generated 2026-11-25 12:40 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 569 | 46% | 5.0 | 1 (11-25 12:40Z) |
| ap-northeast-1 | 569 | 18% | 2.8 | 1 (11-25 12:40Z) |
| ap-northeast-2 | 569 | 68% | 7.0 | 9 (11-25 12:40Z) |
| ap-south-1 | 569 | 3% | 1.7 | 1 (11-25 12:40Z) |
| ap-southeast-2 | 569 | 1% | 1.0 | 1 (11-25 12:40Z) |
| ap-southeast-3 | 569 | 22% | 3.0 | 1 (11-25 12:40Z) |
| us-east-1 | 569 | 13% | 2.8 | 5 (11-25 12:40Z) |
| us-east-2 | 569 | 30% | 3.6 | 1 (11-25 12:40Z) |
| us-west-2 | 569 | 9% | 2.1 | 1 (11-25 12:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        219111111111991996113911911111111111111111111111
ap-northeast-1   115111211299959999911912112212112999991292111111
ap-northeast-2   919111111111999999997991716919991999911111199999
ap-south-1       111111111111111911111111111111111111911211221111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   113111111111112113111311111111111111111111111111
us-east-1        224232333442233237374654676546565667544654554445
us-east-2        111111111111199199199911199181111111111111111191
us-west-2        122211121221112191111211212121121115213191121211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 5 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 401 | 66% | 6.6 | 1 (11-25 02:18Z) |
| ap-northeast-1 apne1-az1 | 139 | 11% | 1.9 | 1 (11-25 12:40Z) |
| ap-northeast-1 apne1-az4 | 268 | 28% | 3.6 | 1 (11-25 02:18Z) |
| ap-northeast-2 apne2-az1 | 474 | 63% | 6.6 | 9 (11-25 02:18Z) |
| ap-northeast-2 apne2-az3 | 519 | 68% | 6.9 | 9 (11-25 12:40Z) |
| ap-northeast-2 apne2-az4 | 549 | 71% | 7.2 | 9 (11-25 12:40Z) |
| ap-south-1 aps1-az1 | 170 | 2% | 1.4 | 1 (11-25 12:40Z) |
| ap-south-1 aps1-az3 | 166 | 7% | 2.3 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az1 | 118 | 3% | 1.2 | 1 (11-25 12:40Z) |
| ap-southeast-2 apse2-az2 | 85 | 0% | 1.0 | 1 (11-24 05:56Z) |
| ap-southeast-3 apse3-az1 | 103 | 0% | 1.0 | 1 (11-23 00:46Z) |
| ap-southeast-3 apse3-az3 | 337 | 36% | 4.2 | 1 (11-25 12:40Z) |
| us-east-1 use1-az1 | 128 | 0% | 1.0 | 1 (11-25 12:40Z) |
| us-east-1 use1-az2 | 148 | 3% | 1.4 | 1 (11-24 17:31Z) |
| us-east-1 use1-az4 | 196 | 19% | 2.8 | 2 (11-25 12:40Z) |
| us-east-1 use1-az5 | 181 | 23% | 3.0 | 1 (11-25 02:18Z) |
| us-east-1 use1-az6 | 148 | 21% | 2.9 | 1 (11-24 17:31Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 288 | 51% | 5.3 | 9 (11-25 02:18Z) |
| us-east-2 use2-az3 | 312 | 48% | 5.1 | 9 (11-25 02:18Z) |
| us-west-2 usw2-az1 | 183 | 21% | 2.9 | 1 (11-25 02:18Z) |
| us-west-2 usw2-az2 | 138 | 15% | 2.4 | 1 (11-25 12:40Z) |
| us-west-2 usw2-az3 | 219 | 16% | 2.6 | 1 (11-25 12:40Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 569 | 73% | 7.4 | 9 (11-25 12:40Z) |
| ap-northeast-1 | 569 | 73% | 7.0 | 9 (11-25 12:40Z) |
| ap-northeast-2 | 569 | 100% | 9.0 | 9 (11-25 12:40Z) |
| ap-south-1 | 569 | 57% | 5.9 | 1 (11-25 12:40Z) |
| ap-southeast-2 | 569 | 28% | 3.7 | 9 (11-25 12:40Z) |
| ap-southeast-3 | 569 | 22% | 3.0 | 1 (11-25 12:40Z) |
| us-east-1 | 569 | 73% | 6.6 | 8 (11-25 12:40Z) |
| us-east-2 | 569 | 68% | 6.7 | 3 (11-25 12:40Z) |
| us-west-2 | 569 | 52% | 5.7 | 9 (11-25 12:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   929928942999999999922929919939919999999999992919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911111191111119911111111111111111111911211221411
ap-southeast-2   119919911913299999111819119119911999991999191919
ap-southeast-3   113111111111112113111311111111111111111111111111
us-east-1        699689669789999979999988898888888999998999987888
us-east-2        199199999999999999199995899299199329111994939993
us-west-2        349334341942399399911599545353244449956999959699
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 371 | 85% | 8.1 | 9 (11-25 12:40Z) |
| ap-east-1 ape1-az2 | 334 | 88% | 8.3 | 9 (11-23 08:55Z) |
| ap-east-1 ape1-az3 | 368 | 88% | 8.3 | 9 (11-25 12:40Z) |
| ap-northeast-1 apne1-az1 | 228 | 95% | 8.7 | 9 (11-24 17:31Z) |
| ap-northeast-1 apne1-az2 | 215 | 87% | 8.2 | 9 (11-24 17:31Z) |
| ap-northeast-1 apne1-az4 | 293 | 99% | 8.9 | 9 (11-25 12:40Z) |
| ap-northeast-2 apne2-az1 | 459 | 100% | 9.0 | 9 (11-25 12:40Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 480 | 100% | 9.0 | 9 (11-25 12:40Z) |
| ap-northeast-2 apne2-az4 | 376 | 88% | 8.2 | 9 (11-25 12:40Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 83 | 88% | 8.2 | 9 (11-24 17:31Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 96 | 85% | 8.1 | 9 (11-25 12:40Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 205 | 99% | 8.9 | 9 (11-25 02:18Z) |
| us-east-2 use2-az2 | 223 | 99% | 8.9 | 9 (11-25 02:18Z) |
| us-east-2 use2-az3 | 248 | 97% | 8.8 | 9 (11-25 02:18Z) |
| us-west-2 usw2-az1 | 111 | 98% | 8.9 | 9 (11-25 12:40Z) |
| us-west-2 usw2-az2 | 99 | 91% | 8.4 | 9 (11-25 12:40Z) |
| us-west-2 usw2-az3 | 151 | 89% | 8.2 | 9 (11-25 12:40Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708800 | 2026-11-25T12:40:21Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-25T12:40:21Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.729900 | 2026-11-25T12:40:21Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.616000 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.631000 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612900 | 2026-11-25T12:40:21Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-25T12:40:21Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.762000 | 2026-11-25T12:40:21Z |
| ap-south-1 | ap-south-1a | Windows | 0.403300 | 2026-11-25T12:40:21Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.743000 | 2026-11-25T12:40:21Z |
| ap-south-1 | ap-south-1b | Windows | 0.422000 | 2026-11-25T12:40:21Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.664900 | 2026-11-25T12:40:21Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.514400 | 2026-11-25T12:40:21Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.550500 | 2026-11-25T12:40:21Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.530700 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.836300 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.899400 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1b | Windows | 0.328200 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.836100 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.851100 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.848600 | 2026-11-25T12:40:21Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.540600 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550300 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546000 | 2026-11-25T12:40:21Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556400 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2a | Windows | 0.298500 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.851600 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.529900 | 2026-11-25T12:40:21Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-25T12:40:21Z |
