# Spot placement score log

Generated 2026-11-18 21:51 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 549 | 48% | 5.2 | 1 (11-18 21:51Z) |
| ap-northeast-1 | 549 | 17% | 2.8 | 2 (11-18 21:51Z) |
| ap-northeast-2 | 549 | 69% | 7.0 | 9 (11-18 21:51Z) |
| ap-south-1 | 549 | 3% | 1.7 | 1 (11-18 21:51Z) |
| ap-southeast-2 | 549 | 1% | 1.0 | 1 (11-18 21:51Z) |
| ap-southeast-3 | 549 | 23% | 3.1 | 1 (11-18 21:51Z) |
| us-east-1 | 549 | 11% | 2.7 | 5 (11-18 21:51Z) |
| us-east-2 | 549 | 31% | 3.7 | 1 (11-18 21:51Z) |
| us-west-2 | 549 | 9% | 2.1 | 1 (11-18 21:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111919999199981991912191111111119919961139119111
ap-northeast-1   121111919991991121111151112112999599999119121122
ap-northeast-2   999999999999999999999191111111119999999979917169
ap-south-1       222212221131191111221111111111111119111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   131111111111311111111131111111111121131113111111
us-east-1        223221322222232929332242323334422332373746546765
us-east-2        111111199991999911111111111111111991991999111991
us-west-2        111112292211121111121222111212211121911112112121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
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
| ap-northeast-1 apne1-az1 | 132 | 11% | 2.0 | 1 (11-17 13:10Z) |
| ap-northeast-1 apne1-az4 | 256 | 27% | 3.6 | 1 (11-18 21:51Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 503 | 69% | 7.0 | 1 (11-18 13:50Z) |
| ap-northeast-2 apne2-az4 | 534 | 70% | 7.2 | 9 (11-18 21:51Z) |
| ap-south-1 aps1-az1 | 159 | 1% | 1.3 | 1 (11-17 13:10Z) |
| ap-south-1 aps1-az3 | 160 | 7% | 2.3 | 1 (11-18 21:51Z) |
| ap-southeast-2 apse2-az1 | 113 | 3% | 1.2 | 1 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 80 | 0% | 1.0 | 1 (11-18 21:51Z) |
| ap-southeast-3 apse3-az1 | 98 | 0% | 1.0 | 1 (11-18 21:51Z) |
| ap-southeast-3 apse3-az3 | 331 | 37% | 4.2 | 1 (11-17 13:10Z) |
| us-east-1 use1-az1 | 119 | 0% | 1.1 | 1 (11-18 21:51Z) |
| us-east-1 use1-az2 | 144 | 3% | 1.4 | 1 (11-18 21:51Z) |
| us-east-1 use1-az4 | 179 | 21% | 2.9 | 2 (11-18 13:50Z) |
| us-east-1 use1-az5 | 175 | 24% | 3.1 | 1 (11-18 04:11Z) |
| us-east-1 use1-az6 | 135 | 23% | 2.9 | 2 (11-18 21:51Z) |
| us-east-2 use2-az1 | 241 | 43% | 4.6 | 9 (11-18 13:50Z) |
| us-east-2 use2-az2 | 281 | 51% | 5.3 | 9 (11-18 13:50Z) |
| us-east-2 use2-az3 | 307 | 48% | 5.1 | 9 (11-18 13:50Z) |
| us-west-2 usw2-az1 | 174 | 21% | 3.0 | 1 (11-18 21:51Z) |
| us-west-2 usw2-az2 | 128 | 16% | 2.5 | 1 (11-18 13:50Z) |
| us-west-2 usw2-az3 | 207 | 16% | 2.7 | 1 (11-18 13:50Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 549 | 72% | 7.3 | 9 (11-18 21:51Z) |
| ap-northeast-1 | 549 | 72% | 7.0 | 9 (11-18 21:51Z) |
| ap-northeast-2 | 549 | 100% | 9.0 | 9 (11-18 21:51Z) |
| ap-south-1 | 549 | 59% | 6.0 | 1 (11-18 21:51Z) |
| ap-southeast-2 | 549 | 27% | 3.6 | 1 (11-18 21:51Z) |
| ap-southeast-3 | 549 | 23% | 3.1 | 1 (11-18 21:51Z) |
| us-east-1 | 549 | 72% | 6.5 | 8 (11-18 21:51Z) |
| us-east-2 | 549 | 68% | 6.7 | 2 (11-18 21:51Z) |
| us-west-2 | 549 | 51% | 5.6 | 3 (11-18 21:51Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   992299999999999392299299289429999999999229299199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299219921791199139229111111911111199111111111111
ap-southeast-2   911999999991991191191199199119132999991118191191
ap-southeast-3   131111111111311111111131111111111121131113111111
us-east-1        557957999999999959966996896697899999799999888988
us-east-2        111911999999999911991991999999999999991999958992
us-west-2        494419595599999949433493343419423993999115995453
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
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 6 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 353 | 85% | 8.1 | 9 (11-18 21:51Z) |
| ap-east-1 ape1-az2 | 323 | 87% | 8.2 | 9 (11-18 21:51Z) |
| ap-east-1 ape1-az3 | 352 | 88% | 8.2 | 9 (11-18 21:51Z) |
| ap-northeast-1 apne1-az1 | 221 | 95% | 8.7 | 9 (11-18 21:51Z) |
| ap-northeast-1 apne1-az2 | 206 | 87% | 8.2 | 9 (11-18 21:51Z) |
| ap-northeast-1 apne1-az4 | 283 | 99% | 8.9 | 9 (11-18 21:51Z) |
| ap-northeast-2 apne2-az1 | 444 | 100% | 9.0 | 9 (11-18 21:51Z) |
| ap-northeast-2 apne2-az2 | 123 | 87% | 8.2 | 9 (11-18 21:51Z) |
| ap-northeast-2 apne2-az3 | 461 | 100% | 9.0 | 9 (11-18 21:51Z) |
| ap-northeast-2 apne2-az4 | 360 | 87% | 8.2 | 9 (11-18 21:51Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 74 | 86% | 8.1 | 9 (11-18 13:50Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 88 | 84% | 8.0 | 9 (11-17 13:10Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 158 | 91% | 8.4 | 3 (11-18 04:11Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 139 | 93% | 8.5 | 9 (11-18 04:11Z) |
| us-east-2 use2-az1 | 196 | 99% | 8.9 | 9 (11-18 13:50Z) |
| us-east-2 use2-az2 | 216 | 99% | 8.9 | 9 (11-18 13:50Z) |
| us-east-2 use2-az3 | 242 | 97% | 8.8 | 9 (11-18 13:50Z) |
| us-west-2 usw2-az1 | 105 | 98% | 8.9 | 9 (11-17 13:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702800 | 2026-11-18T21:51:11Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-18T21:51:11Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.723800 | 2026-11-18T21:51:11Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.615400 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.629000 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.612400 | 2026-11-18T21:51:11Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-18T21:51:11Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.716500 | 2026-11-18T21:51:11Z |
| ap-south-1 | ap-south-1a | Windows | 0.430800 | 2026-11-18T21:51:11Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.686600 | 2026-11-18T21:51:11Z |
| ap-south-1 | ap-south-1b | Windows | 0.410700 | 2026-11-18T21:51:11Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.649600 | 2026-11-18T21:51:11Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510300 | 2026-11-18T21:51:11Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.462800 | 2026-11-18T21:51:11Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.548100 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.874200 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.893600 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1b | Windows | 0.288900 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.637100 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.713000 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.595500 | 2026-11-18T21:51:11Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535800 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.546300 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.536000 | 2026-11-18T21:51:11Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.634100 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2a | Windows | 0.323800 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.663600 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.613500 | 2026-11-18T21:51:11Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-18T21:51:11Z |
