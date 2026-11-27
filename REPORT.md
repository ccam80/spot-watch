# Spot placement score log

Generated 2026-11-27 18:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 575 | 46% | 5.0 | 1 (11-27 18:52Z) |
| ap-northeast-1 | 575 | 18% | 2.8 | 1 (11-27 18:52Z) |
| ap-northeast-2 | 575 | 68% | 7.0 | 9 (11-27 18:52Z) |
| ap-south-1 | 575 | 3% | 1.7 | 1 (11-27 18:52Z) |
| ap-southeast-2 | 575 | 1% | 1.0 | 1 (11-27 18:52Z) |
| ap-southeast-3 | 575 | 22% | 3.0 | 1 (11-27 18:52Z) |
| us-east-1 | 575 | 13% | 2.8 | 3 (11-27 18:52Z) |
| us-east-2 | 575 | 30% | 3.6 | 1 (11-27 18:52Z) |
| us-west-2 | 575 | 9% | 2.1 | 3 (11-27 18:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111991996113911911111111111111111111111119111
ap-northeast-1   211299959999911912112212112999991292111111912111
ap-northeast-2   111111999999997991716919991999911111199999119119
ap-south-1       111111111911111111111111111111911211221111212221
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111112113111311111111111111111111111111111111
us-east-1        333442233237374654676546565667544654554445354343
us-east-2        111111199199199911199181111111111111111191111111
us-west-2        121221112191111211212121121115213191121211232113
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
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
| ap-east-1 ape1-az1 | 177 | 5% | 1.5 | 1 (11-27 08:12Z) |
| ap-east-1 ape1-az2 | 403 | 66% | 6.6 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 142 | 11% | 1.9 | 1 (11-27 18:52Z) |
| ap-northeast-1 apne1-az4 | 270 | 29% | 3.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az1 | 476 | 63% | 6.6 | 9 (11-27 18:52Z) |
| ap-northeast-2 apne2-az3 | 524 | 68% | 6.9 | 1 (11-27 18:52Z) |
| ap-northeast-2 apne2-az4 | 554 | 70% | 7.1 | 1 (11-27 18:52Z) |
| ap-south-1 aps1-az1 | 172 | 2% | 1.4 | 1 (11-27 08:12Z) |
| ap-south-1 aps1-az3 | 168 | 7% | 2.3 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az1 | 122 | 2% | 1.2 | 1 (11-27 18:52Z) |
| ap-southeast-2 apse2-az2 | 88 | 0% | 1.0 | 1 (11-27 18:52Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 339 | 36% | 4.2 | 1 (11-26 23:45Z) |
| us-east-1 use1-az1 | 131 | 0% | 1.0 | 1 (11-27 18:52Z) |
| us-east-1 use1-az2 | 150 | 3% | 1.4 | 1 (11-27 08:12Z) |
| us-east-1 use1-az4 | 199 | 19% | 2.8 | 1 (11-26 15:01Z) |
| us-east-1 use1-az5 | 186 | 23% | 2.9 | 1 (11-27 18:52Z) |
| us-east-1 use1-az6 | 150 | 21% | 2.8 | 1 (11-27 08:12Z) |
| us-east-2 use2-az1 | 246 | 42% | 4.5 | 1 (11-26 15:01Z) |
| us-east-2 use2-az2 | 289 | 51% | 5.2 | 1 (11-27 08:12Z) |
| us-east-2 use2-az3 | 314 | 47% | 5.1 | 1 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 141 | 15% | 2.4 | 1 (11-27 18:52Z) |
| us-west-2 usw2-az3 | 221 | 16% | 2.6 | 1 (11-27 08:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 575 | 73% | 7.4 | 9 (11-27 18:52Z) |
| ap-northeast-1 | 575 | 73% | 7.0 | 9 (11-27 18:52Z) |
| ap-northeast-2 | 575 | 100% | 9.0 | 9 (11-27 18:52Z) |
| ap-south-1 | 575 | 57% | 5.9 | 9 (11-27 18:52Z) |
| ap-southeast-2 | 575 | 28% | 3.7 | 9 (11-27 18:52Z) |
| ap-southeast-3 | 575 | 22% | 3.0 | 1 (11-27 18:52Z) |
| us-east-1 | 575 | 74% | 6.6 | 7 (11-27 18:52Z) |
| us-east-2 | 575 | 67% | 6.6 | 2 (11-27 18:52Z) |
| us-west-2 | 575 | 52% | 5.7 | 9 (11-27 18:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   942999999999922929919939919999999999992919919929
ap-northeast-2   999999999999999999999999999999999999999999999929
ap-south-1       191111119911111111111111111111911211221411512929
ap-southeast-2   911913299999111819119119911999991999191919119919
ap-southeast-3   111111112113111311111111111111111111111111111111
us-east-1        669789999979999988898888888999998999987888788987
us-east-2        999999999999199995899299199329111994939993399292
us-west-2        341942399399911599545353244449956999959699499999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 377 | 86% | 8.1 | 9 (11-27 18:52Z) |
| ap-east-1 ape1-az2 | 337 | 88% | 8.3 | 9 (11-27 08:12Z) |
| ap-east-1 ape1-az3 | 373 | 88% | 8.3 | 9 (11-27 08:12Z) |
| ap-northeast-1 apne1-az1 | 230 | 95% | 8.7 | 9 (11-27 18:52Z) |
| ap-northeast-1 apne1-az2 | 219 | 88% | 8.2 | 9 (11-27 18:52Z) |
| ap-northeast-1 apne1-az4 | 297 | 99% | 8.9 | 9 (11-27 18:52Z) |
| ap-northeast-2 apne2-az1 | 462 | 100% | 9.0 | 9 (11-27 18:52Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 483 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az4 | 378 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az1 | 181 | 88% | 8.3 | 9 (11-27 18:52Z) |
| ap-south-1 aps1-az2 | 189 | 80% | 7.8 | 9 (11-26 23:45Z) |
| ap-south-1 aps1-az3 | 204 | 90% | 8.4 | 9 (11-27 18:52Z) |
| ap-southeast-2 apse2-az1 | 84 | 88% | 8.2 | 9 (11-26 23:45Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 97 | 86% | 8.1 | 9 (11-27 18:52Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 163 | 90% | 8.3 | 2 (11-27 08:12Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 145 | 93% | 8.5 | 9 (11-26 23:45Z) |
| us-east-2 use2-az1 | 208 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az2 | 225 | 99% | 8.9 | 9 (11-27 08:12Z) |
| us-east-2 use2-az3 | 250 | 97% | 8.8 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az1 | 113 | 98% | 8.9 | 9 (11-27 08:12Z) |
| us-west-2 usw2-az2 | 102 | 91% | 8.4 | 9 (11-27 18:52Z) |
| us-west-2 usw2-az3 | 155 | 88% | 8.2 | 9 (11-27 18:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707800 | 2026-11-27T18:52:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-27T18:52:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731300 | 2026-11-27T18:52:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.611800 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626900 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612000 | 2026-11-27T18:52:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-27T18:52:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.764300 | 2026-11-27T18:52:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.390800 | 2026-11-27T18:52:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.698400 | 2026-11-27T18:52:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.400400 | 2026-11-27T18:52:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700800 | 2026-11-27T18:52:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504900 | 2026-11-27T18:52:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.574400 | 2026-11-27T18:52:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.520300 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.792800 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.910500 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881000 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.867600 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.872400 | 2026-11-27T18:52:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545200 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.554600 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549200 | 2026-11-27T18:52:00Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.635800 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2a | Windows | 0.290100 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.904200 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-11-27T18:52:00Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-27T18:52:00Z |
