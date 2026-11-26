# Spot placement score log

Generated 2026-11-26 15:01 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 572 | 46% | 5.0 | 9 (11-26 15:01Z) |
| ap-northeast-1 | 572 | 18% | 2.8 | 2 (11-26 15:01Z) |
| ap-northeast-2 | 572 | 68% | 7.0 | 9 (11-26 15:01Z) |
| ap-south-1 | 572 | 3% | 1.7 | 2 (11-26 15:01Z) |
| ap-southeast-2 | 572 | 1% | 1.0 | 1 (11-26 15:01Z) |
| ap-southeast-3 | 572 | 22% | 3.0 | 1 (11-26 15:01Z) |
| us-east-1 | 572 | 13% | 2.8 | 4 (11-26 15:01Z) |
| us-east-2 | 572 | 30% | 3.6 | 1 (11-26 15:01Z) |
| us-west-2 | 572 | 9% | 2.1 | 2 (11-26 15:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111991996113911911111111111111111111111119
ap-northeast-1   111211299959999911912112212112999991292111111912
ap-northeast-2   111111111999999997991716919991999911111199999119
ap-south-1       111111111111911111111111111111111911211221111212
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111112113111311111111111111111111111111111
us-east-1        232333442233237374654676546565667544654554445354
us-east-2        111111111199199199911199181111111111111111191111
us-west-2        211121221112191111211212121121115213191121211232
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 5 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 6 | 7 |
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
| ap-east-1 ape1-az1 | 176 | 5% | 1.5 | 1 (11-26 15:01Z) |
| ap-east-1 ape1-az2 | 403 | 66% | 6.6 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 140 | 11% | 1.9 | 1 (11-25 22:26Z) |
| ap-northeast-1 apne1-az4 | 270 | 29% | 3.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az1 | 475 | 63% | 6.6 | 1 (11-26 04:56Z) |
| ap-northeast-2 apne2-az3 | 521 | 68% | 6.9 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az4 | 552 | 70% | 7.2 | 9 (11-26 15:01Z) |
| ap-south-1 aps1-az1 | 171 | 2% | 1.4 | 1 (11-26 15:01Z) |
| ap-south-1 aps1-az3 | 166 | 7% | 2.3 | 1 (11-23 08:55Z) |
| ap-southeast-2 apse2-az1 | 119 | 3% | 1.2 | 1 (11-26 04:56Z) |
| ap-southeast-2 apse2-az2 | 86 | 0% | 1.0 | 1 (11-25 22:26Z) |
| ap-southeast-3 apse3-az1 | 104 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 338 | 36% | 4.2 | 1 (11-25 22:26Z) |
| us-east-1 use1-az1 | 129 | 0% | 1.0 | 1 (11-25 22:26Z) |
| us-east-1 use1-az2 | 149 | 3% | 1.4 | 1 (11-26 15:01Z) |
| us-east-1 use1-az4 | 199 | 19% | 2.8 | 1 (11-26 15:01Z) |
| us-east-1 use1-az5 | 183 | 23% | 3.0 | 1 (11-26 04:56Z) |
| us-east-1 use1-az6 | 149 | 21% | 2.8 | 1 (11-26 15:01Z) |
| us-east-2 use2-az1 | 246 | 42% | 4.5 | 1 (11-26 15:01Z) |
| us-east-2 use2-az2 | 288 | 51% | 5.3 | 9 (11-25 02:18Z) |
| us-east-2 use2-az3 | 313 | 48% | 5.1 | 1 (11-26 04:56Z) |
| us-west-2 usw2-az1 | 184 | 21% | 2.9 | 2 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 139 | 15% | 2.4 | 1 (11-25 22:26Z) |
| us-west-2 usw2-az3 | 220 | 16% | 2.6 | 1 (11-26 15:01Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 572 | 73% | 7.4 | 9 (11-26 15:01Z) |
| ap-northeast-1 | 572 | 73% | 7.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 | 572 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-south-1 | 572 | 57% | 5.9 | 2 (11-26 15:01Z) |
| ap-southeast-2 | 572 | 28% | 3.7 | 9 (11-26 15:01Z) |
| ap-southeast-3 | 572 | 22% | 3.0 | 1 (11-26 15:01Z) |
| us-east-1 | 572 | 74% | 6.6 | 8 (11-26 15:01Z) |
| us-east-2 | 572 | 68% | 6.7 | 9 (11-26 15:01Z) |
| us-west-2 | 572 | 52% | 5.7 | 9 (11-26 15:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   928942999999999922929919939919999999999992919919
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111191111119911111111111111111111911211221411512
ap-southeast-2   919911913299999111819119119911999991999191919119
ap-southeast-3   111111111112113111311111111111111111111111111111
us-east-1        689669789999979999988898888888999998999987888788
us-east-2        199999999999999199995899299199329111994939993399
us-west-2        334341942399399911599545353244449956999959699499
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 374 | 86% | 8.1 | 9 (11-26 15:01Z) |
| ap-east-1 ape1-az2 | 336 | 88% | 8.3 | 9 (11-26 04:56Z) |
| ap-east-1 ape1-az3 | 371 | 88% | 8.3 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az1 | 229 | 95% | 8.7 | 9 (11-25 22:26Z) |
| ap-northeast-1 apne1-az2 | 217 | 88% | 8.2 | 9 (11-26 15:01Z) |
| ap-northeast-1 apne1-az4 | 295 | 99% | 8.9 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az1 | 461 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az2 | 129 | 88% | 8.2 | 9 (11-23 21:14Z) |
| ap-northeast-2 apne2-az3 | 483 | 100% | 9.0 | 9 (11-26 15:01Z) |
| ap-northeast-2 apne2-az4 | 377 | 88% | 8.2 | 9 (11-25 22:26Z) |
| ap-south-1 aps1-az1 | 180 | 88% | 8.3 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az2 | 188 | 80% | 7.8 | 9 (11-21 17:22Z) |
| ap-south-1 aps1-az3 | 202 | 90% | 8.4 | 3 (11-25 22:26Z) |
| ap-southeast-2 apse2-az1 | 83 | 88% | 8.2 | 9 (11-24 17:31Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 96 | 85% | 8.1 | 9 (11-25 12:40Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 31 | 52% | 5.5 | 2 (11-26 04:56Z) |
| us-east-1 use1-az2 | 123 | 99% | 9.0 | 9 (11-23 08:55Z) |
| us-east-1 use1-az4 | 162 | 90% | 8.3 | 3 (11-26 04:56Z) |
| us-east-1 use1-az5 | 117 | 98% | 8.9 | 9 (11-23 00:46Z) |
| us-east-1 use1-az6 | 144 | 93% | 8.5 | 9 (11-23 00:46Z) |
| us-east-2 use2-az1 | 207 | 99% | 8.9 | 9 (11-26 15:01Z) |
| us-east-2 use2-az2 | 224 | 99% | 8.9 | 9 (11-26 15:01Z) |
| us-east-2 use2-az3 | 249 | 97% | 8.8 | 9 (11-26 15:01Z) |
| us-west-2 usw2-az1 | 112 | 98% | 8.9 | 9 (11-26 04:56Z) |
| us-west-2 usw2-az2 | 99 | 91% | 8.4 | 9 (11-25 12:40Z) |
| us-west-2 usw2-az3 | 153 | 88% | 8.2 | 9 (11-26 15:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.708300 | 2026-11-26T15:01:19Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-26T15:01:19Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732100 | 2026-11-26T15:01:19Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.611200 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.626800 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.607100 | 2026-11-26T15:01:19Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-26T15:01:19Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.748500 | 2026-11-26T15:01:19Z |
| ap-south-1 | ap-south-1a | Windows | 0.397500 | 2026-11-26T15:01:19Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.690600 | 2026-11-26T15:01:19Z |
| ap-south-1 | ap-south-1b | Windows | 0.410700 | 2026-11-26T15:01:19Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.688800 | 2026-11-26T15:01:19Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510100 | 2026-11-26T15:01:19Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.562800 | 2026-11-26T15:01:19Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.525300 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.815900 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.903900 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1b | Windows | 0.339300 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.841600 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.858700 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.862800 | 2026-11-26T15:01:19Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.540900 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550900 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-11-26T15:01:19Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.595700 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2a | Windows | 0.294500 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.901900 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.536100 | 2026-11-26T15:01:19Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-26T15:01:19Z |
