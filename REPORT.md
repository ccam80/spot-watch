# Spot placement score log

Generated 2026-11-17 22:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 546 | 48% | 5.2 | 9 (11-17 22:13Z) |
| ap-northeast-1 | 546 | 17% | 2.8 | 1 (11-17 22:13Z) |
| ap-northeast-2 | 546 | 69% | 7.0 | 7 (11-17 22:13Z) |
| ap-south-1 | 546 | 3% | 1.7 | 1 (11-17 22:13Z) |
| ap-southeast-2 | 546 | 1% | 1.0 | 1 (11-17 22:13Z) |
| ap-southeast-3 | 546 | 23% | 3.1 | 1 (11-17 22:13Z) |
| us-east-1 | 546 | 11% | 2.7 | 6 (11-17 22:13Z) |
| us-east-2 | 546 | 30% | 3.6 | 1 (11-17 22:13Z) |
| us-west-2 | 546 | 9% | 2.1 | 2 (11-17 22:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        299111919999199981991912191111111119919961139119
ap-northeast-1   221121111919991991121111151112112999599999119121
ap-northeast-2   999999999999999999999999191111111119999999979917
ap-south-1       112222212221131191111221111111111111119111111111
ap-southeast-2   711111111111111111111111111111111111111111111111
ap-southeast-3   111131111111111311111111131111111111121131113111
us-east-1        333223221322222232929332242323334422332373746546
us-east-2        119111111199991999911111111111111111991991999111
us-west-2        119111112292211121111121222111212211121911112112
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
| ap-east-1 ape1-az1 | 171 | 5% | 1.5 | 1 (11-17 22:13Z) |
| ap-east-1 ape1-az2 | 399 | 66% | 6.6 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 132 | 11% | 2.0 | 1 (11-17 13:10Z) |
| ap-northeast-1 apne1-az4 | 254 | 28% | 3.6 | 1 (11-17 22:13Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 502 | 69% | 7.0 | 1 (11-17 13:10Z) |
| ap-northeast-2 apne2-az4 | 532 | 70% | 7.2 | 7 (11-17 22:13Z) |
| ap-south-1 aps1-az1 | 159 | 1% | 1.3 | 1 (11-17 13:10Z) |
| ap-south-1 aps1-az3 | 158 | 7% | 2.3 | 1 (11-17 22:13Z) |
| ap-southeast-2 apse2-az1 | 113 | 3% | 1.2 | 1 (11-17 13:10Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 96 | 0% | 1.0 | 1 (11-17 22:13Z) |
| ap-southeast-3 apse3-az3 | 331 | 37% | 4.2 | 1 (11-17 13:10Z) |
| us-east-1 use1-az1 | 117 | 0% | 1.1 | 1 (11-17 13:10Z) |
| us-east-1 use1-az2 | 143 | 3% | 1.4 | 1 (11-16 20:20Z) |
| us-east-1 use1-az4 | 177 | 21% | 2.9 | 2 (11-17 22:13Z) |
| us-east-1 use1-az5 | 174 | 24% | 3.1 | 1 (11-17 22:13Z) |
| us-east-1 use1-az6 | 133 | 23% | 3.0 | 1 (11-16 09:29Z) |
| us-east-2 use2-az1 | 239 | 43% | 4.6 | 1 (11-17 13:10Z) |
| us-east-2 use2-az2 | 279 | 51% | 5.3 | 1 (11-17 22:13Z) |
| us-east-2 use2-az3 | 305 | 48% | 5.1 | 9 (11-16 09:29Z) |
| us-west-2 usw2-az1 | 172 | 22% | 3.0 | 1 (11-17 22:13Z) |
| us-west-2 usw2-az2 | 127 | 17% | 2.5 | 1 (11-17 13:10Z) |
| us-west-2 usw2-az3 | 206 | 17% | 2.7 | 1 (11-16 09:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 546 | 72% | 7.3 | 9 (11-17 22:13Z) |
| ap-northeast-1 | 546 | 72% | 7.0 | 9 (11-17 22:13Z) |
| ap-northeast-2 | 546 | 100% | 9.0 | 9 (11-17 22:13Z) |
| ap-south-1 | 546 | 59% | 6.0 | 1 (11-17 22:13Z) |
| ap-southeast-2 | 546 | 27% | 3.6 | 1 (11-17 22:13Z) |
| ap-southeast-3 | 546 | 23% | 3.1 | 1 (11-17 22:13Z) |
| us-east-1 | 546 | 72% | 6.5 | 8 (11-17 22:13Z) |
| us-east-2 | 546 | 68% | 6.7 | 8 (11-17 22:13Z) |
| us-west-2 | 546 | 51% | 5.6 | 5 (11-17 22:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   991992299999999999392299299289429999999999229299
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       192299219921791199139229111111911111199111111111
ap-southeast-2   919911999999991991191191199199119132999991118191
ap-southeast-3   111131111111111311111111131111111111121131113111
us-east-1        765557957999999999959966996896697899999799999888
us-east-2        129111911999999999911991991999999999999991999958
us-west-2        429494419595599999949433493343419423993999115995
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
| ap-east-1 ape1-az1 | 350 | 85% | 8.1 | 9 (11-17 22:13Z) |
| ap-east-1 ape1-az2 | 320 | 87% | 8.2 | 9 (11-17 22:13Z) |
| ap-east-1 ape1-az3 | 349 | 87% | 8.2 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az1 | 220 | 95% | 8.7 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az2 | 205 | 87% | 8.2 | 9 (11-17 22:13Z) |
| ap-northeast-1 apne1-az4 | 281 | 99% | 8.9 | 9 (11-17 22:13Z) |
| ap-northeast-2 apne2-az1 | 442 | 100% | 9.0 | 9 (11-17 22:13Z) |
| ap-northeast-2 apne2-az2 | 122 | 87% | 8.2 | 9 (11-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 458 | 100% | 9.0 | 9 (11-17 22:13Z) |
| ap-northeast-2 apne2-az4 | 358 | 87% | 8.2 | 9 (11-17 22:13Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.701600 | 2026-11-17T22:13:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-17T22:13:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.723400 | 2026-11-17T22:13:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.614100 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.627400 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.611500 | 2026-11-17T22:13:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-17T22:13:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.702400 | 2026-11-17T22:13:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.413200 | 2026-11-17T22:13:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.664000 | 2026-11-17T22:13:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.398200 | 2026-11-17T22:13:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.648400 | 2026-11-17T22:13:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517300 | 2026-11-17T22:13:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.480200 | 2026-11-17T22:13:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.873000 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.877800 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.619700 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.663900 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558700 | 2026-11-17T22:13:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535500 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.552000 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.537100 | 2026-11-17T22:13:00Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.644700 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2a | Windows | 0.326600 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.643400 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.643500 | 2026-11-17T22:13:00Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-17T22:13:00Z |
