# Spot placement score log

Generated 2026-11-28 18:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 599 | 46% | 5.0 | 9 (11-28 18:15Z) |
| ap-northeast-1 | 599 | 19% | 2.9 | 1 (11-28 18:15Z) |
| ap-northeast-2 | 599 | 68% | 6.9 | 9 (11-28 18:15Z) |
| ap-south-1 | 599 | 3% | 1.6 | 1 (11-28 18:15Z) |
| ap-southeast-2 | 599 | 1% | 1.1 | 2 (11-28 18:15Z) |
| ap-southeast-3 | 599 | 22% | 3.0 | 2 (11-28 18:15Z) |
| us-east-1 | 599 | 13% | 2.8 | 4 (11-28 18:15Z) |
| us-east-2 | 599 | 29% | 3.5 | 2 (11-28 18:15Z) |
| us-west-2 | 599 | 11% | 2.3 | 1 (11-28 18:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111119111111111911911111199999999
ap-northeast-1   112999991292111111912111619991111122121233999991
ap-northeast-2   991999911111199999119119998999999111151192111999
ap-south-1       111111911211221111212221111111111111111111112111
ap-southeast-2   111111111111111111111111111211111111111125591132
ap-southeast-3   111111111111111111111111111111111131111386687832
us-east-1        565667544654554445354343343333334443334233452444
us-east-2        111111111111111191111111111111111111111142272222
us-west-2        121115213191121211232113333979979999112999999911
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 7 | 4 | 5 | 7 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 4 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 4 | 4 | 4 | 4 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 7 | 7 | 7 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 3 | 4 | 5 | 6 | 4 | 5 | 6 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 187 | 5% | 1.5 | 1 (11-28 18:15Z) |
| ap-east-1 ape1-az2 | 415 | 66% | 6.6 | 9 (11-28 18:15Z) |
| ap-northeast-1 apne1-az1 | 154 | 10% | 2.0 | 2 (11-28 17:11Z) |
| ap-northeast-1 apne1-az4 | 284 | 30% | 3.7 | 1 (11-28 18:15Z) |
| ap-northeast-2 apne2-az1 | 487 | 64% | 6.6 | 9 (11-28 16:14Z) |
| ap-northeast-2 apne2-az3 | 536 | 67% | 6.8 | 9 (11-28 18:15Z) |
| ap-northeast-2 apne2-az4 | 564 | 70% | 7.1 | 9 (11-28 18:15Z) |
| ap-south-1 aps1-az1 | 184 | 2% | 1.3 | 1 (11-28 15:12Z) |
| ap-south-1 aps1-az3 | 170 | 7% | 2.3 | 1 (11-28 00:33Z) |
| ap-southeast-2 apse2-az1 | 132 | 4% | 1.3 | 2 (11-28 18:15Z) |
| ap-southeast-2 apse2-az2 | 91 | 0% | 1.0 | 1 (11-28 07:14Z) |
| ap-southeast-3 apse3-az1 | 112 | 0% | 1.0 | 1 (11-28 18:15Z) |
| ap-southeast-3 apse3-az3 | 352 | 36% | 4.2 | 2 (11-28 18:15Z) |
| us-east-1 use1-az1 | 136 | 0% | 1.0 | 1 (11-28 17:11Z) |
| us-east-1 use1-az2 | 158 | 3% | 1.3 | 1 (11-28 13:12Z) |
| us-east-1 use1-az4 | 218 | 17% | 2.7 | 2 (11-28 18:15Z) |
| us-east-1 use1-az5 | 192 | 22% | 2.9 | 1 (11-28 07:14Z) |
| us-east-1 use1-az6 | 162 | 19% | 2.7 | 1 (11-28 15:12Z) |
| us-east-2 use2-az1 | 253 | 41% | 4.5 | 1 (11-28 15:12Z) |
| us-east-2 use2-az2 | 299 | 49% | 5.1 | 1 (11-28 18:15Z) |
| us-east-2 use2-az3 | 319 | 47% | 5.0 | 2 (11-28 14:12Z) |
| us-west-2 usw2-az1 | 198 | 26% | 3.3 | 9 (11-28 16:14Z) |
| us-west-2 usw2-az2 | 148 | 16% | 2.4 | 6 (11-28 15:12Z) |
| us-west-2 usw2-az3 | 239 | 19% | 2.8 | 1 (11-28 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 599 | 74% | 7.5 | 9 (11-28 18:15Z) |
| ap-northeast-1 | 599 | 74% | 7.1 | 9 (11-28 18:15Z) |
| ap-northeast-2 | 599 | 100% | 9.0 | 9 (11-28 18:15Z) |
| ap-south-1 | 599 | 57% | 5.8 | 9 (11-28 18:15Z) |
| ap-southeast-2 | 599 | 31% | 3.9 | 9 (11-28 18:15Z) |
| ap-southeast-3 | 599 | 22% | 3.0 | 2 (11-28 18:15Z) |
| us-east-1 | 599 | 75% | 6.7 | 9 (11-28 18:15Z) |
| us-east-2 | 599 | 67% | 6.6 | 9 (11-28 18:15Z) |
| us-west-2 | 599 | 54% | 5.8 | 9 (11-28 18:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   919999999999992919919929999999999999999999999999
ap-northeast-2   999999999999999999999929999999999999999999999999
ap-south-1       111111911211221411512929999999999196811111124139
ap-southeast-2   911999991999191919119919999999999999999999999999
ap-southeast-3   111111111111111111111111111111111131111386687832
us-east-1        888999998999987888788987788787899999999999999999
us-east-2        199329111994939993399292212221112999999999999999
us-west-2        244449956999959699499999999999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 9 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 8 | 6 | 5 | 6 | 5 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | 4 | 3 | 3 | 3 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 7 | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 5 | 5 | 5 |
| us-west-2 | 6 | 5 | 4 | 5 | 6 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 6 | 5 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 392 | 86% | 8.2 | 9 (11-28 18:15Z) |
| ap-east-1 ape1-az2 | 347 | 88% | 8.3 | 9 (11-28 15:12Z) |
| ap-east-1 ape1-az3 | 386 | 89% | 8.3 | 9 (11-28 18:15Z) |
| ap-northeast-1 apne1-az1 | 240 | 95% | 8.7 | 9 (11-28 17:11Z) |
| ap-northeast-1 apne1-az2 | 226 | 88% | 8.3 | 9 (11-28 18:15Z) |
| ap-northeast-1 apne1-az4 | 312 | 99% | 8.9 | 9 (11-28 18:15Z) |
| ap-northeast-2 apne2-az1 | 475 | 100% | 9.0 | 9 (11-28 17:11Z) |
| ap-northeast-2 apne2-az2 | 131 | 88% | 8.2 | 9 (11-28 02:18Z) |
| ap-northeast-2 apne2-az3 | 499 | 100% | 9.0 | 9 (11-28 18:15Z) |
| ap-northeast-2 apne2-az4 | 387 | 88% | 8.3 | 9 (11-28 18:15Z) |
| ap-south-1 aps1-az1 | 188 | 88% | 8.3 | 9 (11-28 05:14Z) |
| ap-south-1 aps1-az2 | 191 | 81% | 7.8 | 9 (11-28 03:16Z) |
| ap-south-1 aps1-az3 | 212 | 90% | 8.4 | 9 (11-28 05:14Z) |
| ap-southeast-2 apse2-az1 | 92 | 89% | 8.3 | 9 (11-28 15:12Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 110 | 87% | 8.2 | 9 (11-28 17:11Z) |
| ap-southeast-3 apse3-az1 | 1 | 0% | 1.0 | 1 (11-26 04:56Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 37 | 59% | 6.1 | 9 (11-28 17:11Z) |
| us-east-1 use1-az2 | 135 | 99% | 9.0 | 9 (11-28 18:15Z) |
| us-east-1 use1-az4 | 169 | 90% | 8.3 | 9 (11-28 17:11Z) |
| us-east-1 use1-az5 | 119 | 98% | 8.9 | 9 (11-28 15:12Z) |
| us-east-1 use1-az6 | 156 | 94% | 8.5 | 9 (11-28 18:15Z) |
| us-east-2 use2-az1 | 216 | 99% | 8.9 | 9 (11-28 14:12Z) |
| us-east-2 use2-az2 | 229 | 99% | 8.9 | 9 (11-28 15:12Z) |
| us-east-2 use2-az3 | 260 | 97% | 8.8 | 9 (11-28 18:15Z) |
| us-west-2 usw2-az1 | 118 | 98% | 8.9 | 9 (11-28 15:12Z) |
| us-west-2 usw2-az2 | 117 | 92% | 8.5 | 9 (11-28 17:11Z) |
| us-west-2 usw2-az3 | 167 | 89% | 8.2 | 9 (11-28 18:15Z) |
| us-west-2 usw2-az4 | 1 | 100% | 9.0 | 9 (11-28 12:18Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709600 | 2026-11-28T18:15:20Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-28T18:15:20Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732400 | 2026-11-28T18:15:20Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.620900 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.630300 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.621200 | 2026-11-28T18:15:20Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-28T18:15:20Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.721100 | 2026-11-28T18:15:20Z |
| ap-south-1 | ap-south-1a | Windows | 0.386000 | 2026-11-28T18:15:20Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.681100 | 2026-11-28T18:15:20Z |
| ap-south-1 | ap-south-1b | Windows | 0.394600 | 2026-11-28T18:15:20Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.705400 | 2026-11-28T18:15:20Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.498100 | 2026-11-28T18:15:20Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.584000 | 2026-11-28T18:15:20Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.516700 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.785900 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.922300 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1b | Windows | 0.347600 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.890300 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1c | Windows | 0.287000 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.878600 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.881200 | 2026-11-28T18:15:20Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548800 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.562100 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-28T18:15:20Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.643100 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2a | Windows | 0.289600 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.905700 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.550000 | 2026-11-28T18:15:20Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-28T18:15:20Z |
