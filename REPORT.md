# Spot placement score log

Generated 2026-11-17 13:10 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 545 | 48% | 5.2 | 1 (11-17 13:10Z) |
| ap-northeast-1 | 545 | 17% | 2.8 | 2 (11-17 13:10Z) |
| ap-northeast-2 | 545 | 69% | 7.0 | 1 (11-17 13:10Z) |
| ap-south-1 | 545 | 3% | 1.7 | 1 (11-17 13:10Z) |
| ap-southeast-2 | 545 | 1% | 1.0 | 1 (11-17 13:10Z) |
| ap-southeast-3 | 545 | 23% | 3.1 | 1 (11-17 13:10Z) |
| us-east-1 | 545 | 11% | 2.7 | 4 (11-17 13:10Z) |
| us-east-2 | 545 | 30% | 3.7 | 1 (11-17 13:10Z) |
| us-west-2 | 545 | 9% | 2.1 | 1 (11-17 13:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        129911191999919998199191219111111111991996113911
ap-northeast-1   122112111191999199112111115111211299959999911912
ap-northeast-2   999999999999999999999999919111111111999999997991
ap-south-1       111222221222113119111122111111111111111911111111
ap-southeast-2   171111111111111111111111111111111111111111111111
ap-southeast-3   111113111111111131111111113111111111112113111311
us-east-1        333322322132222223292933224232333442233237374654
us-east-2        111911111119999199991111111111111111199199199911
us-west-2        111911111229221112111112122211121221112191111211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 170 | 5% | 1.5 | 1 (11-17 03:43Z) |
| ap-east-1 ape1-az2 | 398 | 66% | 6.6 | 1 (11-17 13:10Z) |
| ap-northeast-1 apne1-az1 | 132 | 11% | 2.0 | 1 (11-17 13:10Z) |
| ap-northeast-1 apne1-az4 | 253 | 28% | 3.6 | 1 (11-17 03:43Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 502 | 69% | 7.0 | 1 (11-17 13:10Z) |
| ap-northeast-2 apne2-az4 | 531 | 70% | 7.2 | 9 (11-17 03:43Z) |
| ap-south-1 aps1-az1 | 159 | 1% | 1.3 | 1 (11-17 13:10Z) |
| ap-south-1 aps1-az3 | 157 | 7% | 2.3 | 1 (11-17 03:43Z) |
| ap-southeast-2 apse2-az1 | 113 | 3% | 1.2 | 1 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 95 | 0% | 1.0 | 1 (11-17 03:43Z) |
| ap-southeast-3 apse3-az3 | 331 | 37% | 4.2 | 1 (11-17 13:10Z) |
| us-east-1 use1-az1 | 117 | 0% | 1.1 | 1 (11-17 13:10Z) |
| us-east-1 use1-az2 | 143 | 3% | 1.4 | 1 (11-16 20:20Z) |
| us-east-1 use1-az4 | 176 | 22% | 2.9 | 1 (11-17 13:10Z) |
| us-east-1 use1-az5 | 173 | 24% | 3.1 | 1 (11-17 03:43Z) |
| us-east-1 use1-az6 | 133 | 23% | 3.0 | 1 (11-16 09:29Z) |
| us-east-2 use2-az1 | 239 | 43% | 4.6 | 1 (11-17 13:10Z) |
| us-east-2 use2-az2 | 278 | 51% | 5.3 | 1 (11-17 03:43Z) |
| us-east-2 use2-az3 | 305 | 48% | 5.1 | 9 (11-16 09:29Z) |
| us-west-2 usw2-az1 | 171 | 22% | 3.0 | 1 (11-17 03:43Z) |
| us-west-2 usw2-az2 | 127 | 17% | 2.5 | 1 (11-17 13:10Z) |
| us-west-2 usw2-az3 | 206 | 17% | 2.7 | 1 (11-16 09:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 545 | 72% | 7.3 | 9 (11-17 13:10Z) |
| ap-northeast-1 | 545 | 72% | 7.0 | 9 (11-17 13:10Z) |
| ap-northeast-2 | 545 | 100% | 9.0 | 9 (11-17 13:10Z) |
| ap-south-1 | 545 | 59% | 6.1 | 1 (11-17 13:10Z) |
| ap-southeast-2 | 545 | 27% | 3.6 | 9 (11-17 13:10Z) |
| ap-southeast-3 | 545 | 23% | 3.1 | 1 (11-17 13:10Z) |
| us-east-1 | 545 | 72% | 6.5 | 8 (11-17 13:10Z) |
| us-east-2 | 545 | 68% | 6.7 | 5 (11-17 13:10Z) |
| us-west-2 | 545 | 51% | 5.6 | 9 (11-17 13:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   199199229999999999939229929928942999999999922929
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       119229921992179119913922911111191111119911111111
ap-southeast-2   191991199999999199119119119919911913299999111819
ap-southeast-3   111113111111111131111111113111111111112113111311
us-east-1        976555795799999999995996699689669789999979999988
us-east-2        912911191199999999991199199199999999999999199995
us-west-2        342949441959559999994943349334341942399399911599
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 7 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 349 | 85% | 8.1 | 9 (11-17 03:43Z) |
| ap-east-1 ape1-az2 | 319 | 87% | 8.2 | 9 (11-17 13:10Z) |
| ap-east-1 ape1-az3 | 348 | 87% | 8.2 | 9 (11-17 13:10Z) |
| ap-northeast-1 apne1-az1 | 219 | 95% | 8.7 | 9 (11-17 13:10Z) |
| ap-northeast-1 apne1-az2 | 204 | 87% | 8.2 | 9 (11-17 13:10Z) |
| ap-northeast-1 apne1-az4 | 280 | 99% | 8.9 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az1 | 441 | 100% | 9.0 | 9 (11-17 03:43Z) |
| ap-northeast-2 apne2-az2 | 121 | 87% | 8.1 | 9 (11-17 13:10Z) |
| ap-northeast-2 apne2-az3 | 457 | 100% | 9.0 | 9 (11-17 13:10Z) |
| ap-northeast-2 apne2-az4 | 357 | 87% | 8.2 | 9 (11-17 13:10Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 73 | 86% | 8.1 | 9 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 88 | 84% | 8.0 | 9 (11-17 13:10Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 157 | 92% | 8.4 | 9 (11-16 09:29Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 138 | 93% | 8.5 | 9 (11-16 01:54Z) |
| us-east-2 use2-az1 | 194 | 99% | 8.9 | 9 (11-17 03:43Z) |
| us-east-2 use2-az2 | 214 | 99% | 8.9 | 9 (11-17 03:43Z) |
| us-east-2 use2-az3 | 240 | 97% | 8.8 | 9 (11-17 03:43Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.701600 | 2026-11-17T13:10:23Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-17T13:10:23Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.719700 | 2026-11-17T13:10:23Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.612300 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.624100 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.609700 | 2026-11-17T13:10:23Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-17T13:10:23Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.712500 | 2026-11-17T13:10:23Z |
| ap-south-1 | ap-south-1a | Windows | 0.406900 | 2026-11-17T13:10:23Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.660200 | 2026-11-17T13:10:23Z |
| ap-south-1 | ap-south-1b | Windows | 0.401900 | 2026-11-17T13:10:23Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.647900 | 2026-11-17T13:10:23Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517300 | 2026-11-17T13:10:23Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.488500 | 2026-11-17T13:10:23Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.874300 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.879000 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.617700 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.649500 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.546100 | 2026-11-17T13:10:23Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535900 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.555900 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.540400 | 2026-11-17T13:10:23Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.663700 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2a | Windows | 0.329100 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.618200 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.647200 | 2026-11-17T13:10:23Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-17T13:10:23Z |
