# Spot placement score log

Generated 2026-11-19 12:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 551 | 48% | 5.1 | 1 (11-19 12:52Z) |
| ap-northeast-1 | 551 | 17% | 2.8 | 2 (11-19 12:52Z) |
| ap-northeast-2 | 551 | 69% | 7.0 | 9 (11-19 12:52Z) |
| ap-south-1 | 551 | 3% | 1.7 | 1 (11-19 12:52Z) |
| ap-southeast-2 | 551 | 1% | 1.0 | 1 (11-19 12:52Z) |
| ap-southeast-3 | 551 | 23% | 3.1 | 1 (11-19 12:52Z) |
| us-east-1 | 551 | 11% | 2.7 | 6 (11-19 12:52Z) |
| us-east-2 | 551 | 31% | 3.7 | 1 (11-19 12:52Z) |
| us-west-2 | 551 | 9% | 2.1 | 1 (11-19 12:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        191999919998199191219111111111991996113911911111
ap-northeast-1   111191999199112111115111211299959999911912112212
ap-northeast-2   999999999999999999919111111111999999997991716919
ap-south-1       221222113119111122111111111111111911111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111131111111113111111111112113111311111111
us-east-1        322132222223292933224232333442233237374654676546
us-east-2        111119999199991111111111111111199199199911199181
us-west-2        111229221112111112122211121221112191111211212121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 173 | 5% | 1.5 | 1 (11-18 21:51Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 133 | 11% | 2.0 | 1 (11-19 12:52Z) |
| ap-northeast-1 apne1-az4 | 256 | 27% | 3.6 | 1 (11-18 21:51Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 505 | 69% | 7.0 | 9 (11-19 12:52Z) |
| ap-northeast-2 apne2-az4 | 535 | 70% | 7.2 | 9 (11-19 12:52Z) |
| ap-south-1 aps1-az1 | 160 | 1% | 1.3 | 1 (11-19 03:15Z) |
| ap-south-1 aps1-az3 | 160 | 7% | 2.3 | 1 (11-18 21:51Z) |
| ap-southeast-2 apse2-az1 | 113 | 3% | 1.2 | 1 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 81 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az1 | 99 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az3 | 332 | 36% | 4.2 | 1 (11-19 12:52Z) |
| us-east-1 use1-az1 | 120 | 0% | 1.1 | 1 (11-19 12:52Z) |
| us-east-1 use1-az2 | 144 | 3% | 1.4 | 1 (11-18 21:51Z) |
| us-east-1 use1-az4 | 181 | 21% | 2.8 | 2 (11-19 12:52Z) |
| us-east-1 use1-az5 | 175 | 24% | 3.1 | 1 (11-18 04:11Z) |
| us-east-1 use1-az6 | 137 | 23% | 2.9 | 2 (11-19 12:52Z) |
| us-east-2 use2-az1 | 242 | 43% | 4.6 | 1 (11-19 03:15Z) |
| us-east-2 use2-az2 | 283 | 51% | 5.3 | 9 (11-19 12:52Z) |
| us-east-2 use2-az3 | 308 | 48% | 5.1 | 9 (11-19 12:52Z) |
| us-west-2 usw2-az1 | 175 | 21% | 3.0 | 2 (11-19 03:15Z) |
| us-west-2 usw2-az2 | 129 | 16% | 2.5 | 1 (11-19 12:52Z) |
| us-west-2 usw2-az3 | 208 | 16% | 2.6 | 1 (11-19 03:15Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 551 | 72% | 7.3 | 9 (11-19 12:52Z) |
| ap-northeast-1 | 551 | 72% | 7.0 | 9 (11-19 12:52Z) |
| ap-northeast-2 | 551 | 100% | 9.0 | 9 (11-19 12:52Z) |
| ap-south-1 | 551 | 59% | 6.0 | 1 (11-19 12:52Z) |
| ap-southeast-2 | 551 | 27% | 3.6 | 9 (11-19 12:52Z) |
| ap-southeast-3 | 551 | 23% | 3.1 | 1 (11-19 12:52Z) |
| us-east-1 | 551 | 73% | 6.5 | 8 (11-19 12:52Z) |
| us-east-2 | 551 | 68% | 6.7 | 9 (11-19 12:52Z) |
| us-west-2 | 551 | 51% | 5.6 | 3 (11-19 12:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   229999999999939229929928942999999999922929919939
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       921992179119913922911111191111119911111111111111
ap-southeast-2   199999999199119119119919911913299999111819119119
ap-southeast-3   111111111131111111113111111111112113111311111111
us-east-1        795799999999995996699689669789999979999988898888
us-east-2        191199999999991199199199999999999999199995899299
us-west-2        441959559999994943349334341942399399911599545353
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 6 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 355 | 85% | 8.1 | 9 (11-19 12:52Z) |
| ap-east-1 ape1-az2 | 325 | 87% | 8.2 | 9 (11-19 12:52Z) |
| ap-east-1 ape1-az3 | 353 | 88% | 8.3 | 9 (11-19 03:15Z) |
| ap-northeast-1 apne1-az1 | 221 | 95% | 8.7 | 9 (11-18 21:51Z) |
| ap-northeast-1 apne1-az2 | 206 | 87% | 8.2 | 9 (11-18 21:51Z) |
| ap-northeast-1 apne1-az4 | 284 | 99% | 8.9 | 9 (11-19 12:52Z) |
| ap-northeast-2 apne2-az1 | 446 | 100% | 9.0 | 9 (11-19 12:52Z) |
| ap-northeast-2 apne2-az2 | 124 | 87% | 8.2 | 9 (11-19 03:15Z) |
| ap-northeast-2 apne2-az3 | 463 | 100% | 9.0 | 9 (11-19 12:52Z) |
| ap-northeast-2 apne2-az4 | 362 | 87% | 8.2 | 9 (11-19 12:52Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 75 | 87% | 8.2 | 9 (11-19 12:52Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 89 | 84% | 8.0 | 9 (11-19 12:52Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 158 | 91% | 8.4 | 3 (11-18 04:11Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 139 | 93% | 8.5 | 9 (11-18 04:11Z) |
| us-east-2 use2-az1 | 198 | 99% | 8.9 | 9 (11-19 12:52Z) |
| us-east-2 use2-az2 | 218 | 99% | 8.9 | 9 (11-19 12:52Z) |
| us-east-2 use2-az3 | 243 | 97% | 8.8 | 8 (11-19 03:15Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.704600 | 2026-11-19T12:52:47Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-19T12:52:47Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.724500 | 2026-11-19T12:52:47Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.619500 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.631700 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612500 | 2026-11-19T12:52:47Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-19T12:52:47Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.716000 | 2026-11-19T12:52:47Z |
| ap-south-1 | ap-south-1a | Windows | 0.427300 | 2026-11-19T12:52:47Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.703700 | 2026-11-19T12:52:47Z |
| ap-south-1 | ap-south-1b | Windows | 0.412000 | 2026-11-19T12:52:47Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.666300 | 2026-11-19T12:52:47Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.521900 | 2026-11-19T12:52:47Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.470200 | 2026-11-19T12:52:47Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.551400 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.873300 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.894200 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1b | Windows | 0.289500 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.644800 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.729100 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.607000 | 2026-11-19T12:52:47Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534900 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.542200 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.531900 | 2026-11-19T12:52:47Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.636700 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2a | Windows | 0.320600 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.682700 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.607100 | 2026-11-19T12:52:47Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-19T12:52:47Z |
