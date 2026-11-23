# Spot placement score log

Generated 2026-11-23 00:46 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 563 | 47% | 5.0 | 1 (11-23 00:46Z) |
| ap-northeast-1 | 563 | 18% | 2.8 | 2 (11-23 00:46Z) |
| ap-northeast-2 | 563 | 68% | 7.0 | 1 (11-23 00:46Z) |
| ap-south-1 | 563 | 3% | 1.7 | 1 (11-23 00:46Z) |
| ap-southeast-2 | 563 | 1% | 1.0 | 1 (11-23 00:46Z) |
| ap-southeast-3 | 563 | 23% | 3.0 | 1 (11-23 00:46Z) |
| us-east-1 | 563 | 13% | 2.8 | 4 (11-23 00:46Z) |
| us-east-2 | 563 | 30% | 3.6 | 1 (11-23 00:46Z) |
| us-west-2 | 563 | 9% | 2.1 | 1 (11-23 00:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        199191219111111111991996113911911111111111111111
ap-northeast-1   112111115111211299959999911912112212112999991292
ap-northeast-2   999999919111111111999999997991716919991999911111
ap-south-1       111122111111111111111911111111111111111111911211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111113111111111112113111311111111111111111111
us-east-1        292933224232333442233237374654676546565667544654
us-east-2        991111111111111111199199199911199181111111111111
us-west-2        111112122211121221112191111211212121121115213191
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 3 | 5 | 5 | 7 | 4 | 5 | 6 | 3 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 175 | 5% | 1.5 | 1 (11-22 03:03Z) |
| ap-east-1 ape1-az2 | 400 | 66% | 6.6 | 1 (11-23 00:46Z) |
| ap-northeast-1 apne1-az1 | 135 | 11% | 2.0 | 1 (11-21 01:25Z) |
| ap-northeast-1 apne1-az4 | 267 | 28% | 3.6 | 1 (11-23 00:46Z) |
| ap-northeast-2 apne2-az1 | 470 | 63% | 6.6 | 1 (11-23 00:46Z) |
| ap-northeast-2 apne2-az3 | 513 | 68% | 6.9 | 1 (11-22 19:28Z) |
| ap-northeast-2 apne2-az4 | 543 | 71% | 7.2 | 1 (11-23 00:46Z) |
| ap-south-1 aps1-az1 | 167 | 2% | 1.4 | 1 (11-22 11:09Z) |
| ap-south-1 aps1-az3 | 165 | 7% | 2.3 | 1 (11-23 00:46Z) |
| ap-southeast-2 apse2-az1 | 116 | 3% | 1.2 | 1 (11-23 00:46Z) |
| ap-southeast-2 apse2-az2 | 83 | 0% | 1.0 | 1 (11-22 19:28Z) |
| ap-southeast-3 apse3-az1 | 103 | 0% | 1.0 | 1 (11-23 00:46Z) |
| ap-southeast-3 apse3-az3 | 334 | 36% | 4.2 | 1 (11-21 01:25Z) |
| us-east-1 use1-az1 | 124 | 0% | 1.0 | 1 (11-22 19:28Z) |
| us-east-1 use1-az2 | 147 | 3% | 1.4 | 1 (11-22 11:09Z) |
| us-east-1 use1-az4 | 190 | 20% | 2.8 | 2 (11-22 11:09Z) |
| us-east-1 use1-az5 | 178 | 24% | 3.0 | 1 (11-23 00:46Z) |
| us-east-1 use1-az6 | 147 | 21% | 2.9 | 2 (11-22 11:09Z) |
| us-east-2 use2-az1 | 245 | 42% | 4.6 | 1 (11-22 03:03Z) |
| us-east-2 use2-az2 | 286 | 51% | 5.3 | 1 (11-22 11:09Z) |
| us-east-2 use2-az3 | 311 | 48% | 5.1 | 1 (11-23 00:46Z) |
| us-west-2 usw2-az1 | 181 | 21% | 3.0 | 1 (11-23 00:46Z) |
| us-west-2 usw2-az2 | 134 | 16% | 2.4 | 1 (11-22 19:28Z) |
| us-west-2 usw2-az3 | 216 | 16% | 2.6 | 9 (11-22 19:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 563 | 73% | 7.4 | 9 (11-23 00:46Z) |
| ap-northeast-1 | 563 | 73% | 7.0 | 9 (11-23 00:46Z) |
| ap-northeast-2 | 563 | 100% | 9.0 | 9 (11-23 00:46Z) |
| ap-south-1 | 563 | 58% | 5.9 | 1 (11-23 00:46Z) |
| ap-southeast-2 | 563 | 28% | 3.7 | 9 (11-23 00:46Z) |
| ap-southeast-3 | 563 | 23% | 3.0 | 1 (11-23 00:46Z) |
| us-east-1 | 563 | 73% | 6.6 | 9 (11-23 00:46Z) |
| us-east-2 | 563 | 68% | 6.7 | 4 (11-23 00:46Z) |
| us-west-2 | 563 | 52% | 5.6 | 9 (11-23 00:46Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   939229929928942999999999922929919939919999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       913922911111191111119911111111111111111111911211
ap-southeast-2   119119119919911913299999111819119119911999991999
ap-southeast-3   111111113111111111112113111311111111111111111111
us-east-1        995996699689669789999979999988898888888999998999
us-east-2        991199199199999999999999199995899299199329111994
us-west-2        994943349334341942399399911599545353244449956999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 365 | 85% | 8.1 | 9 (11-23 00:46Z) |
| ap-east-1 ape1-az2 | 333 | 88% | 8.3 | 9 (11-23 00:46Z) |
| ap-east-1 ape1-az3 | 362 | 88% | 8.3 | 9 (11-22 19:28Z) |
| ap-northeast-1 apne1-az1 | 226 | 95% | 8.7 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az2 | 213 | 87% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-1 apne1-az4 | 290 | 99% | 8.9 | 9 (11-22 11:09Z) |
| ap-northeast-2 apne2-az1 | 454 | 100% | 9.0 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az2 | 128 | 88% | 8.2 | 9 (11-22 03:03Z) |
| ap-northeast-2 apne2-az3 | 474 | 100% | 9.0 | 9 (11-23 00:46Z) |
| ap-northeast-2 apne2-az4 | 372 | 87% | 8.2 | 9 (11-23 00:46Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 81 | 88% | 8.2 | 9 (11-23 00:46Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 94 | 85% | 8.1 | 9 (11-22 19:28Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 122 | 99% | 9.0 | 9 (11-23 00:46Z) |
| us-east-1 use1-az4 | 161 | 91% | 8.4 | 9 (11-22 11:09Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 201 | 99% | 8.9 | 9 (11-22 11:09Z) |
| us-east-2 use2-az2 | 220 | 99% | 8.9 | 9 (11-20 11:24Z) |
| us-east-2 use2-az3 | 245 | 97% | 8.8 | 9 (11-21 09:39Z) |
| us-west-2 usw2-az1 | 107 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-west-2 usw2-az2 | 98 | 91% | 8.3 | 9 (11-21 17:22Z) |
| us-west-2 usw2-az3 | 147 | 88% | 8.2 | 9 (11-23 00:46Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.704500 | 2026-11-23T00:46:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-23T00:46:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.724500 | 2026-11-23T00:46:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591000 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.614900 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.589500 | 2026-11-23T00:46:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-23T00:46:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.719500 | 2026-11-23T00:46:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.420900 | 2026-11-23T00:46:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.768400 | 2026-11-23T00:46:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.420400 | 2026-11-23T00:46:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.635800 | 2026-11-23T00:46:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.529800 | 2026-11-23T00:46:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.520100 | 2026-11-23T00:46:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.547400 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.858300 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.895000 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1b | Windows | 0.311700 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.759600 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.809800 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.742500 | 2026-11-23T00:46:06Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.528900 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536400 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.527200 | 2026-11-23T00:46:06Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.565600 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2a | Windows | 0.303100 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.792700 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527800 | 2026-11-23T00:46:06Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-23T00:46:06Z |
