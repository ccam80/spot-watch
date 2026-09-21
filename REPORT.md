# Spot placement score log

Generated 2026-09-21 00:10 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 140 | 0% | 1.9 | 3 (09-21 00:10Z) |
| ap-northeast-1 | 140 | 0% | 1.9 | 1 (09-21 00:10Z) |
| ap-northeast-2 | 140 | 0% | 3.0 | 3 (09-21 00:10Z) |
| ap-south-1 | 140 | 0% | 2.1 | 2 (09-21 00:10Z) |
| ap-southeast-2 | 140 | 0% | 1.0 | 1 (09-21 00:10Z) |
| ap-southeast-3 | 140 | 0% | 2.5 | 3 (09-21 00:10Z) |
| us-east-1 | 140 | 0% | 2.0 | 3 (09-21 00:10Z) |
| us-east-2 | 140 | 0% | 1.8 | 1 (09-21 00:10Z) |
| us-west-2 | 140 | 0% | 1.6 | 3 (09-21 00:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333333332233211322122221122221112212233223123221
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333133333333311111211221113333113121133333333332
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333131331313313333313131123333333333313333
us-east-1        113232332222221221131121232231231112131122333333
us-east-2        333333333331111111131313333333133113333123333331
us-west-2        133133333331112111211111131221311123333333333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 42 | 0% | 1.5 | 3 (09-21 00:10Z) |
| ap-east-1 ape1-az2 | 82 | 0% | 2.4 | 3 (09-21 00:10Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 124 | 0% | 2.9 | 3 (09-20 18:43Z) |
| ap-northeast-2 apne2-az3 | 123 | 0% | 2.9 | 3 (09-20 21:28Z) |
| ap-northeast-2 apne2-az4 | 137 | 0% | 3.0 | 3 (09-21 00:10Z) |
| ap-south-1 aps1-az1 | 55 | 0% | 1.7 | 3 (09-20 18:43Z) |
| ap-south-1 aps1-az3 | 78 | 0% | 2.6 | 3 (09-20 21:28Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 106 | 0% | 2.9 | 3 (09-21 00:10Z) |
| us-east-1 use1-az1 | 17 | 0% | 1.4 | 3 (09-20 21:28Z) |
| us-east-1 use1-az2 | 45 | 0% | 1.4 | 3 (09-21 00:10Z) |
| us-east-1 use1-az4 | 31 | 0% | 1.6 | 3 (09-21 00:10Z) |
| us-east-1 use1-az5 | 40 | 0% | 1.6 | 3 (09-21 00:10Z) |
| us-east-1 use1-az6 | 46 | 0% | 1.3 | 3 (09-21 00:10Z) |
| us-east-2 use2-az1 | 46 | 0% | 1.8 | 3 (09-20 21:28Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 74 | 0% | 2.3 | 3 (09-20 15:58Z) |
| us-west-2 usw2-az1 | 42 | 0% | 2.1 | 3 (09-21 00:10Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 74 | 0% | 1.8 | 3 (09-21 00:10Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 140 | 0% | 3.0 | 3 (09-21 00:10Z) |
| ap-northeast-1 | 140 | 78% | 7.5 | 9 (09-21 00:10Z) |
| ap-northeast-2 | 140 | 100% | 9.0 | 9 (09-21 00:10Z) |
| ap-south-1 | 140 | 44% | 5.5 | 9 (09-21 00:10Z) |
| ap-southeast-2 | 140 | 7% | 2.6 | 2 (09-21 00:10Z) |
| ap-southeast-3 | 140 | 0% | 2.5 | 3 (09-21 00:10Z) |
| us-east-1 | 140 | 75% | 6.9 | 9 (09-21 00:10Z) |
| us-east-2 | 140 | 76% | 7.3 | 9 (09-21 00:10Z) |
| us-west-2 | 140 | 53% | 5.8 | 9 (09-21 00:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999996499933999249994199993399999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999991899992999939999239999999999999999
ap-southeast-2   333223322222222222223322233222233233333333333332
ap-southeast-3   333333333131331313313333313131123333333333313333
us-east-1        999999999943684432493955995699994549999999999999
us-east-2        999999999999999921299999999999999119999199999999
us-west-2        999999999993425433534413994459533459999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 4 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 6 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 72 | 89% | 8.3 | 9 (09-21 00:10Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 94 | 100% | 9.0 | 9 (09-21 00:10Z) |
| ap-northeast-2 apne2-az1 | 126 | 100% | 9.0 | 9 (09-21 00:10Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 126 | 100% | 9.0 | 9 (09-20 21:28Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 43 | 49% | 5.9 | 9 (09-21 00:10Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 59 | 69% | 7.2 | 9 (09-21 00:10Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 59 | 100% | 9.0 | 9 (09-21 00:10Z) |
| us-east-1 use1-az4 | 61 | 97% | 8.8 | 9 (09-21 00:10Z) |
| us-east-1 use1-az5 | 27 | 96% | 8.7 | 9 (09-20 21:28Z) |
| us-east-1 use1-az6 | 56 | 100% | 9.0 | 9 (09-20 18:43Z) |
| us-east-2 use2-az1 | 55 | 100% | 9.0 | 9 (09-20 21:28Z) |
| us-east-2 use2-az2 | 88 | 98% | 8.8 | 9 (09-20 21:28Z) |
| us-east-2 use2-az3 | 72 | 89% | 8.2 | 9 (09-21 00:10Z) |
| us-west-2 usw2-az1 | 49 | 98% | 8.9 | 9 (09-21 00:10Z) |
| us-west-2 usw2-az2 | 39 | 97% | 8.8 | 9 (09-20 15:58Z) |
| us-west-2 usw2-az3 | 53 | 98% | 8.9 | 9 (09-21 00:10Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.719200 | 2026-09-21T00:10:38Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-21T00:10:38Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.841600 | 2026-09-21T00:10:38Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.024600 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590300 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579800 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566200 | 2026-09-21T00:10:38Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742800 | 2026-09-21T00:10:38Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.483600 | 2026-09-21T00:10:38Z |
| ap-south-1 | ap-south-1a | Windows | 0.304900 | 2026-09-21T00:10:38Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.444300 | 2026-09-21T00:10:38Z |
| ap-south-1 | ap-south-1b | Windows | 0.314600 | 2026-09-21T00:10:38Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.685700 | 2026-09-21T00:10:38Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523400 | 2026-09-21T00:10:38Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.827900 | 2026-09-21T00:10:38Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.575200 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.833800 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1a | Windows | 0.356300 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.617000 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1b | Windows | 0.307500 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.510600 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1c | Windows | 0.290400 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.502200 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1d | Windows | 0.304500 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.489700 | 2026-09-21T00:10:38Z |
| us-east-1 | us-east-1f | Windows | 0.313300 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.523800 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523400 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2b | Windows | 0.642000 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-09-21T00:10:38Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.558000 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2a | Windows | 0.338500 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.515900 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2b | Windows | 0.336000 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.519000 | 2026-09-21T00:10:38Z |
| us-west-2 | us-west-2c | Windows | 0.336400 | 2026-09-21T00:10:38Z |
