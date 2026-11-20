# Spot placement score log

Generated 2026-11-20 20:01 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 555 | 48% | 5.1 | 1 (11-20 20:01Z) |
| ap-northeast-1 | 555 | 17% | 2.8 | 9 (11-20 20:01Z) |
| ap-northeast-2 | 555 | 69% | 7.0 | 9 (11-20 20:01Z) |
| ap-south-1 | 555 | 3% | 1.7 | 1 (11-20 20:01Z) |
| ap-southeast-2 | 555 | 1% | 1.0 | 1 (11-20 20:01Z) |
| ap-southeast-3 | 555 | 23% | 3.1 | 1 (11-20 20:01Z) |
| us-east-1 | 555 | 12% | 2.7 | 6 (11-20 20:01Z) |
| us-east-2 | 555 | 30% | 3.6 | 1 (11-20 20:01Z) |
| us-west-2 | 555 | 9% | 2.1 | 1 (11-20 20:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999199981991912191111111119919961139119111111111
ap-northeast-1   919991991121111151112112999599999119121122121129
ap-northeast-2   999999999999999191111111119999999979917169199919
ap-south-1       221131191111221111111111111119111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111311111111131111111111121131113111111111111
us-east-1        322222232929332242323334422332373746546765465656
us-east-2        199991999911111111111111111991991999111991811111
us-west-2        292211121111121222111212211121911112112121211211
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
| ap-northeast-1 apne1-az4 | 259 | 27% | 3.6 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az1 | 465 | 63% | 6.6 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az3 | 509 | 69% | 7.0 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az4 | 538 | 71% | 7.2 | 9 (11-20 20:01Z) |
| ap-south-1 aps1-az1 | 162 | 1% | 1.3 | 1 (11-20 20:01Z) |
| ap-south-1 aps1-az3 | 162 | 7% | 2.3 | 1 (11-20 03:02Z) |
| ap-southeast-2 apse2-az1 | 114 | 3% | 1.2 | 1 (11-20 11:24Z) |
| ap-southeast-2 apse2-az2 | 81 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az1 | 99 | 0% | 1.0 | 1 (11-19 03:15Z) |
| ap-southeast-3 apse3-az3 | 333 | 36% | 4.2 | 1 (11-20 11:24Z) |
| us-east-1 use1-az1 | 122 | 0% | 1.0 | 1 (11-20 20:01Z) |
| us-east-1 use1-az2 | 144 | 3% | 1.4 | 1 (11-18 21:51Z) |
| us-east-1 use1-az4 | 185 | 21% | 2.8 | 1 (11-20 20:01Z) |
| us-east-1 use1-az5 | 177 | 24% | 3.0 | 1 (11-20 03:02Z) |
| us-east-1 use1-az6 | 141 | 22% | 2.9 | 2 (11-20 20:01Z) |
| us-east-2 use2-az1 | 242 | 43% | 4.6 | 1 (11-19 03:15Z) |
| us-east-2 use2-az2 | 283 | 51% | 5.3 | 9 (11-19 12:52Z) |
| us-east-2 use2-az3 | 310 | 48% | 5.1 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az1 | 177 | 21% | 2.9 | 1 (11-20 03:02Z) |
| us-west-2 usw2-az2 | 131 | 16% | 2.5 | 1 (11-20 20:01Z) |
| us-west-2 usw2-az3 | 210 | 16% | 2.6 | 1 (11-20 20:01Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 555 | 72% | 7.3 | 9 (11-20 20:01Z) |
| ap-northeast-1 | 555 | 72% | 7.0 | 9 (11-20 20:01Z) |
| ap-northeast-2 | 555 | 100% | 9.0 | 9 (11-20 20:01Z) |
| ap-south-1 | 555 | 58% | 6.0 | 1 (11-20 20:01Z) |
| ap-southeast-2 | 555 | 27% | 3.6 | 9 (11-20 20:01Z) |
| ap-southeast-3 | 555 | 23% | 3.1 | 1 (11-20 20:01Z) |
| us-east-1 | 555 | 73% | 6.6 | 9 (11-20 20:01Z) |
| us-east-2 | 555 | 68% | 6.7 | 3 (11-20 20:01Z) |
| us-west-2 | 555 | 51% | 5.6 | 4 (11-20 20:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999392299299289429999999999229299199399199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       921791199139229111111911111199111111111111111111
ap-southeast-2   999991991191191199199119132999991118191191199119
ap-southeast-3   111111311111111131111111111121131113111111111111
us-east-1        999999999959966996896697899999799999888988888889
us-east-2        999999999911991991999999999999991999958992991993
us-west-2        595599999949433493343419423993999115995453532444
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
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 359 | 85% | 8.1 | 9 (11-20 20:01Z) |
| ap-east-1 ape1-az2 | 328 | 88% | 8.2 | 9 (11-20 20:01Z) |
| ap-east-1 ape1-az3 | 357 | 88% | 8.3 | 9 (11-20 20:01Z) |
| ap-northeast-1 apne1-az1 | 223 | 95% | 8.7 | 9 (11-20 20:01Z) |
| ap-northeast-1 apne1-az2 | 209 | 87% | 8.2 | 9 (11-20 20:01Z) |
| ap-northeast-1 apne1-az4 | 286 | 99% | 8.9 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az1 | 450 | 100% | 9.0 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az2 | 126 | 87% | 8.2 | 9 (11-20 11:24Z) |
| ap-northeast-2 apne2-az3 | 467 | 100% | 9.0 | 9 (11-20 20:01Z) |
| ap-northeast-2 apne2-az4 | 366 | 87% | 8.2 | 9 (11-20 20:01Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 77 | 87% | 8.2 | 9 (11-20 20:01Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.705200 | 2026-11-20T20:01:05Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-20T20:01:05Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.726300 | 2026-11-20T20:01:05Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.613000 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.629200 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.607300 | 2026-11-20T20:01:05Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-20T20:01:05Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.677600 | 2026-11-20T20:01:05Z |
| ap-south-1 | ap-south-1a | Windows | 0.425900 | 2026-11-20T20:01:05Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.736500 | 2026-11-20T20:01:05Z |
| ap-south-1 | ap-south-1b | Windows | 0.425100 | 2026-11-20T20:01:05Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.631000 | 2026-11-20T20:01:05Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.540100 | 2026-11-20T20:01:05Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.495400 | 2026-11-20T20:01:05Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.553900 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.865300 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.892900 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1b | Windows | 0.297500 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.683000 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.788300 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.660200 | 2026-11-20T20:01:05Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532400 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.537900 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.530500 | 2026-11-20T20:01:05Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.627600 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2a | Windows | 0.311600 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.716100 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.572900 | 2026-11-20T20:01:05Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-20T20:01:05Z |
