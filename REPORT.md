# Spot placement score log

Generated 2026-11-20 11:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 554 | 48% | 5.1 | 1 (11-20 11:24Z) |
| ap-northeast-1 | 554 | 17% | 2.8 | 2 (11-20 11:24Z) |
| ap-northeast-2 | 554 | 69% | 7.0 | 1 (11-20 11:24Z) |
| ap-south-1 | 554 | 3% | 1.7 | 1 (11-20 11:24Z) |
| ap-southeast-2 | 554 | 1% | 1.0 | 1 (11-20 11:24Z) |
| ap-southeast-3 | 554 | 23% | 3.1 | 1 (11-20 11:24Z) |
| us-east-1 | 554 | 12% | 2.7 | 5 (11-20 11:24Z) |
| us-east-2 | 554 | 31% | 3.6 | 1 (11-20 11:24Z) |
| us-west-2 | 554 | 9% | 2.1 | 1 (11-20 11:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999919998199191219111111111991996113911911111111
ap-northeast-1   191999199112111115111211299959999911912112212112
ap-northeast-2   999999999999999919111111111999999997991716919991
ap-south-1       222113119111122111111111111111911111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111131111111113111111111112113111311111111111
us-east-1        132222223292933224232333442233237374654676546565
us-east-2        119999199991111111111111111199199199911199181111
us-west-2        229221112111112122211121221112191111211212121121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 173 | 5% | 1.5 | 1 (11-18 21:51Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 134 | 11% | 2.0 | 1 (11-20 11:24Z) |
| ap-northeast-1 apne1-az4 | 258 | 27% | 3.5 | 1 (11-20 03:02Z) |
| ap-northeast-2 apne2-az1 | 464 | 63% | 6.6 | 8 (11-20 03:02Z) |
| ap-northeast-2 apne2-az3 | 508 | 69% | 7.0 | 1 (11-20 11:24Z) |
| ap-northeast-2 apne2-az4 | 537 | 71% | 7.2 | 9 (11-20 03:02Z) |
| ap-south-1 aps1-az1 | 161 | 1% | 1.3 | 1 (11-20 11:24Z) |
| ap-south-1 aps1-az3 | 162 | 7% | 2.3 | 1 (11-20 03:02Z) |
| ap-southeast-2 apse2-az1 | 114 | 3% | 1.2 | 1 (11-20 11:24Z) |
| ap-southeast-2 apse2-az2 | 81 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az1 | 99 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az3 | 333 | 36% | 4.2 | 1 (11-20 11:24Z) |
| us-east-1 use1-az1 | 121 | 0% | 1.0 | 1 (11-20 11:24Z) |
| us-east-1 use1-az2 | 144 | 3% | 1.4 | 1 (11-18 21:51Z) |
| us-east-1 use1-az4 | 184 | 21% | 2.8 | 2 (11-20 11:24Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 140 | 22% | 2.9 | 2 (11-20 11:24Z) |
| us-east-2 use2-az1 | 242 | 43% | 4.6 | 1 (11-19 03:15Z) |
| us-east-2 use2-az2 | 283 | 51% | 5.3 | 9 (11-19 12:52Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 177 | 21% | 2.9 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az2 | 130 | 16% | 2.5 | 1 (11-20 11:24Z) |
| us-west-2 usw2-az3 | 209 | 16% | 2.6 | 1 (11-20 11:24Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 554 | 72% | 7.3 | 9 (11-20 11:24Z) |
| ap-northeast-1 | 554 | 72% | 7.0 | 9 (11-20 11:24Z) |
| ap-northeast-2 | 554 | 100% | 9.0 | 9 (11-20 11:24Z) |
| ap-south-1 | 554 | 58% | 6.0 | 1 (11-20 11:24Z) |
| ap-southeast-2 | 554 | 27% | 3.6 | 1 (11-20 11:24Z) |
| ap-southeast-3 | 554 | 23% | 3.1 | 1 (11-20 11:24Z) |
| us-east-1 | 554 | 73% | 6.6 | 8 (11-20 11:24Z) |
| us-east-2 | 554 | 68% | 6.7 | 9 (11-20 11:24Z) |
| us-west-2 | 554 | 51% | 5.6 | 4 (11-20 11:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999939229929928942999999999922929919939919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992179119913922911111191111119911111111111111111
ap-southeast-2   999999199119119119919911913299999111819119119911
ap-southeast-3   111111131111111113111111111112113111311111111111
us-east-1        799999999995996699689669789999979999988898888888
us-east-2        199999999991199199199999999999999199995899299199
us-west-2        959559999994943349334341942399399911599545353244
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 6 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 358 | 85% | 8.1 | 9 (11-20 11:24Z) |
| ap-east-1 ape1-az2 | 327 | 87% | 8.2 | 9 (11-20 11:24Z) |
| ap-east-1 ape1-az3 | 356 | 88% | 8.3 | 9 (11-20 11:24Z) |
| ap-northeast-1 apne1-az1 | 222 | 95% | 8.7 | 9 (11-19 21:24Z) |
| ap-northeast-1 apne1-az2 | 208 | 87% | 8.2 | 8 (11-20 11:24Z) |
| ap-northeast-1 apne1-az4 | 285 | 99% | 8.9 | 9 (11-19 21:24Z) |
| ap-northeast-2 apne2-az1 | 449 | 100% | 9.0 | 9 (11-20 11:24Z) |
| ap-northeast-2 apne2-az2 | 126 | 87% | 8.2 | 9 (11-20 11:24Z) |
| ap-northeast-2 apne2-az3 | 466 | 100% | 9.0 | 9 (11-20 11:24Z) |
| ap-northeast-2 apne2-az4 | 365 | 87% | 8.2 | 9 (11-20 11:24Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 76 | 87% | 8.2 | 9 (11-19 21:24Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 89 | 84% | 8.0 | 9 (11-19 12:52Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 159 | 91% | 8.4 | 3 (11-20 03:02Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 139 | 93% | 8.5 | 9 (11-18 04:11Z) |
| us-east-2 use2-az1 | 200 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az2 | 220 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az3 | 244 | 97% | 8.8 | 9 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.705000 | 2026-11-20T11:24:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-20T11:24:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.725200 | 2026-11-20T11:24:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.619700 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.632300 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612400 | 2026-11-20T11:24:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-20T11:24:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.685600 | 2026-11-20T11:24:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.420900 | 2026-11-20T11:24:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.734400 | 2026-11-20T11:24:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.419600 | 2026-11-20T11:24:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.634100 | 2026-11-20T11:24:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.534200 | 2026-11-20T11:24:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.486200 | 2026-11-20T11:24:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.552700 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.870300 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.894100 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1b | Windows | 0.292900 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.676300 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.768900 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.647400 | 2026-11-20T11:24:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532700 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.539300 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.530600 | 2026-11-20T11:24:00Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.631100 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2a | Windows | 0.314200 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.714700 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.575400 | 2026-11-20T11:24:00Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-20T11:24:00Z |
