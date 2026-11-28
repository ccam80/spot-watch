# Spot placement score log

Generated 2026-11-28 06:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 587 | 45% | 4.9 | 1 (11-28 06:21Z) |
| ap-northeast-1 | 587 | 18% | 2.8 | 2 (11-28 06:21Z) |
| ap-northeast-2 | 587 | 68% | 7.0 | 1 (11-28 06:21Z) |
| ap-south-1 | 587 | 3% | 1.7 | 1 (11-28 06:21Z) |
| ap-southeast-2 | 587 | 1% | 1.0 | 1 (11-28 06:21Z) |
| ap-southeast-3 | 587 | 22% | 2.9 | 1 (11-28 06:21Z) |
| us-east-1 | 587 | 13% | 2.8 | 3 (11-28 06:21Z) |
| us-east-2 | 587 | 29% | 3.5 | 1 (11-28 06:21Z) |
| us-west-2 | 587 | 10% | 2.2 | 9 (11-28 06:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        113911911111111111111111111111119111111111911911
ap-northeast-1   911912112212112999991292111111912111619991111122
ap-northeast-2   997991716919991999911111199999119119998999999111
ap-south-1       111111111111111111911211221111212221111111111111
ap-southeast-2   111111111111111111111111111111111111111211111111
ap-southeast-3   111311111111111111111111111111111111111111111131
us-east-1        374654676546565667544654554445354343343333334443
us-east-2        199911199181111111111111111191111111111111111111
us-west-2        111211212121121115213191121211232113333979979999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 6 | 7 | 5 | 6 | 6 | 5 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 7 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 182 | 5% | 1.5 | 1 (11-28 06:21Z) |
| ap-east-1 ape1-az2 | 407 | 65% | 6.6 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az1 | 147 | 10% | 1.9 | 1 (11-28 02:18Z) |
| ap-northeast-1 apne1-az4 | 277 | 29% | 3.6 | 1 (11-28 01:15Z) |
| ap-northeast-2 apne2-az1 | 485 | 64% | 6.6 | 1 (11-28 04:15Z) |
| ap-northeast-2 apne2-az3 | 529 | 67% | 6.9 | 1 (11-28 06:21Z) |
| ap-northeast-2 apne2-az4 | 559 | 70% | 7.1 | 9 (11-28 01:15Z) |
| ap-south-1 aps1-az1 | 179 | 2% | 1.3 | 1 (11-28 06:21Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 125 | 2% | 1.2 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az2 | 90 | 0% | 1.0 | 1 (11-27 21:12Z) |
| ap-southeast-3 apse3-az1 | 109 | 0% | 1.0 | 1 (11-28 03:16Z) |
| ap-southeast-3 apse3-az3 | 342 | 35% | 4.1 | 3 (11-28 05:14Z) |
| us-east-1 use1-az1 | 134 | 0% | 1.0 | 1 (11-28 02:18Z) |
| us-east-1 use1-az2 | 155 | 3% | 1.3 | 1 (11-28 06:21Z) |
| us-east-1 use1-az4 | 207 | 18% | 2.7 | 2 (11-28 06:21Z) |
| us-east-1 use1-az5 | 191 | 22% | 2.9 | 1 (11-28 00:33Z) |
| us-east-1 use1-az6 | 156 | 20% | 2.8 | 1 (11-28 06:21Z) |
| us-east-2 use2-az1 | 249 | 42% | 4.5 | 1 (11-28 05:14Z) |
| us-east-2 use2-az2 | 294 | 50% | 5.2 | 1 (11-28 06:21Z) |
| us-east-2 use2-az3 | 317 | 47% | 5.1 | 1 (11-28 06:21Z) |
| us-west-2 usw2-az1 | 191 | 23% | 3.1 | 9 (11-28 06:21Z) |
| us-west-2 usw2-az2 | 146 | 15% | 2.4 | 8 (11-28 05:14Z) |
| us-west-2 usw2-az3 | 229 | 17% | 2.6 | 1 (11-28 06:21Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 587 | 74% | 7.4 | 9 (11-28 06:21Z) |
| ap-northeast-1 | 587 | 73% | 7.1 | 9 (11-28 06:21Z) |
| ap-northeast-2 | 587 | 100% | 9.0 | 9 (11-28 06:21Z) |
| ap-south-1 | 587 | 58% | 5.9 | 6 (11-28 06:21Z) |
| ap-southeast-2 | 587 | 30% | 3.8 | 9 (11-28 06:21Z) |
| ap-southeast-3 | 587 | 22% | 2.9 | 1 (11-28 06:21Z) |
| us-east-1 | 587 | 74% | 6.7 | 9 (11-28 06:21Z) |
| us-east-2 | 587 | 67% | 6.6 | 9 (11-28 06:21Z) |
| us-west-2 | 587 | 53% | 5.8 | 9 (11-28 06:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   922929919939919999999999992919919929999999999999
ap-northeast-2   999999999999999999999999999999999929999999999999
ap-south-1       111111111111111111911211221411512929999999999196
ap-southeast-2   111819119119911999991999191919119919999999999999
ap-southeast-3   111311111111111111111111111111111111111111111131
us-east-1        999988898888888999998999987888788987788787899999
us-east-2        199995899299199329111994939993399292212221112999
us-west-2        911599545353244449956999959699499999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 384 | 86% | 8.2 | 9 (11-28 04:15Z) |
| ap-east-1 ape1-az2 | 342 | 88% | 8.3 | 9 (11-28 06:21Z) |
| ap-east-1 ape1-az3 | 381 | 88% | 8.3 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az1 | 235 | 95% | 8.7 | 9 (11-28 05:14Z) |
| ap-northeast-1 apne1-az2 | 223 | 88% | 8.3 | 9 (11-28 04:15Z) |
| ap-northeast-1 apne1-az4 | 303 | 99% | 8.9 | 9 (11-28 05:14Z) |
| ap-northeast-2 apne2-az1 | 470 | 100% | 9.0 | 9 (11-28 05:14Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 492 | 100% | 9.0 | 9 (11-28 06:21Z) |
| ap-northeast-2 apne2-az4 | 382 | 88% | 8.3 | 9 (11-28 06:21Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 89 | 89% | 8.3 | 9 (11-28 02:18Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 104 | 87% | 8.2 | 9 (11-28 06:21Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 32 | 53% | 5.6 | 9 (11-28 06:21Z) |
| us-east-1 use1-az2 | 126 | 99% | 9.0 | 9 (11-28 06:21Z) |
| us-east-1 use1-az4 | 164 | 90% | 8.3 | 9 (11-28 05:14Z) |
| us-east-1 use1-az5 | 118 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-east-1 use1-az6 | 148 | 93% | 8.5 | 9 (11-28 06:21Z) |
| us-east-2 use2-az1 | 210 | 99% | 8.9 | 9 (11-28 06:21Z) |
| us-east-2 use2-az2 | 226 | 99% | 8.9 | 9 (11-28 06:21Z) |
| us-east-2 use2-az3 | 252 | 97% | 8.8 | 9 (11-28 06:21Z) |
| us-west-2 usw2-az1 | 117 | 98% | 8.9 | 9 (11-28 02:18Z) |
| us-west-2 usw2-az2 | 110 | 92% | 8.4 | 9 (11-28 05:14Z) |
| us-west-2 usw2-az3 | 162 | 89% | 8.2 | 9 (11-28 05:14Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T06:21:39Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T06:21:39Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.731800 | 2026-11-28T06:21:39Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.617700 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.629600 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.614800 | 2026-11-28T06:21:39Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T06:21:39Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.747400 | 2026-11-28T06:21:39Z |
| ap-south-1 | ap-south-1a | Windows | 0.389100 | 2026-11-28T06:21:39Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.685400 | 2026-11-28T06:21:39Z |
| ap-south-1 | ap-south-1b | Windows | 0.395500 | 2026-11-28T06:21:39Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.702500 | 2026-11-28T06:21:39Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.499600 | 2026-11-28T06:21:39Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.581200 | 2026-11-28T06:21:39Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.519700 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.791200 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.917300 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1b | Windows | 0.343000 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.881500 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1c | Windows | 0.286600 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.874800 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.876900 | 2026-11-28T06:21:39Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.545100 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552400 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.548500 | 2026-11-28T06:21:39Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.641400 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2a | Windows | 0.289300 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.908100 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.545000 | 2026-11-28T06:21:39Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T06:21:39Z |
