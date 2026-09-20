# Spot placement score log

Generated 2026-09-20 01:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 134 | 0% | 1.9 | 3 (09-20 01:00Z) |
| ap-northeast-1 | 134 | 0% | 1.9 | 3 (09-20 01:00Z) |
| ap-northeast-2 | 134 | 0% | 3.0 | 3 (09-20 01:00Z) |
| ap-south-1 | 134 | 0% | 2.0 | 3 (09-20 01:00Z) |
| ap-southeast-2 | 134 | 0% | 1.0 | 1 (09-20 01:00Z) |
| ap-southeast-3 | 134 | 0% | 2.5 | 3 (09-20 01:00Z) |
| us-east-1 | 134 | 0% | 1.9 | 2 (09-20 01:00Z) |
| us-east-2 | 134 | 0% | 1.8 | 3 (09-20 01:00Z) |
| us-west-2 | 134 | 0% | 1.6 | 3 (09-20 01:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   233333333333332233211322122221122221112212233223
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       113333333133333333311111211221113333113121133333
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333333333131331313313333313131123333333333
us-east-1        332233113232332222221221131121232231231112131122
us-east-2        113333333333333331111111131313333333133113333123
us-west-2        111333133133333331112111211111131221311123333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 1.4 | 3 (09-20 01:00Z) |
| ap-east-1 ape1-az2 | 78 | 0% | 2.3 | 3 (09-20 01:00Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 66 | 0% | 2.2 | 3 (09-20 01:00Z) |
| ap-northeast-2 apne2-az1 | 122 | 0% | 2.9 | 3 (09-20 01:00Z) |
| ap-northeast-2 apne2-az3 | 119 | 0% | 2.9 | 3 (09-20 01:00Z) |
| ap-northeast-2 apne2-az4 | 131 | 0% | 3.0 | 3 (09-20 01:00Z) |
| ap-south-1 aps1-az1 | 54 | 0% | 1.7 | 3 (09-19 22:55Z) |
| ap-south-1 aps1-az3 | 73 | 0% | 2.6 | 3 (09-20 01:00Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 103 | 0% | 2.9 | 3 (09-19 22:55Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 39 | 0% | 1.1 | 1 (09-18 21:36Z) |
| us-east-1 use1-az4 | 26 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az5 | 37 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 44 | 0% | 1.7 | 3 (09-20 01:00Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 73 | 0% | 2.3 | 3 (09-20 01:00Z) |
| us-west-2 usw2-az1 | 38 | 0% | 2.0 | 3 (09-19 22:55Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 69 | 0% | 1.7 | 3 (09-20 01:00Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 134 | 0% | 3.0 | 3 (09-20 01:00Z) |
| ap-northeast-1 | 134 | 77% | 7.4 | 9 (09-20 01:00Z) |
| ap-northeast-2 | 134 | 100% | 9.0 | 9 (09-20 01:00Z) |
| ap-south-1 | 134 | 41% | 5.3 | 9 (09-20 01:00Z) |
| ap-southeast-2 | 134 | 7% | 2.6 | 3 (09-20 01:00Z) |
| ap-southeast-3 | 134 | 0% | 2.5 | 3 (09-20 01:00Z) |
| us-east-1 | 134 | 74% | 6.8 | 9 (09-20 01:00Z) |
| us-east-2 | 134 | 75% | 7.2 | 9 (09-20 01:00Z) |
| us-west-2 | 134 | 51% | 5.6 | 9 (09-20 01:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999996499933999249994199993399999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999991899992999939999239999999999
ap-southeast-2   333333333223322222222222223322233222233233333333
ap-southeast-3   333333333333333131331313313333313131123333333333
us-east-1        499999999999999943684432493955995699994549999999
us-east-2        199999999999999999999921299999999999999119999199
us-west-2        539999999999999993425433534413994459533459999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 3 | 4 | 9 | 3 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 3 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 5 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 7 | 4 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 68 | 88% | 8.3 | 9 (09-19 20:33Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 90 | 100% | 9.0 | 9 (09-20 01:00Z) |
| ap-northeast-2 apne2-az1 | 123 | 100% | 9.0 | 9 (09-20 01:00Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 122 | 100% | 9.0 | 9 (09-20 01:00Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 40 | 45% | 5.7 | 9 (09-19 20:33Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 55 | 67% | 7.1 | 9 (09-20 01:00Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 54 | 100% | 9.0 | 9 (09-20 01:00Z) |
| us-east-1 use1-az4 | 56 | 96% | 8.8 | 9 (09-19 22:55Z) |
| us-east-1 use1-az5 | 24 | 96% | 8.7 | 9 (09-20 01:00Z) |
| us-east-1 use1-az6 | 53 | 100% | 9.0 | 9 (09-20 01:00Z) |
| us-east-2 use2-az1 | 52 | 100% | 9.0 | 9 (09-19 10:50Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 67 | 88% | 8.2 | 9 (09-20 01:00Z) |
| us-west-2 usw2-az1 | 46 | 98% | 8.9 | 9 (09-19 22:55Z) |
| us-west-2 usw2-az2 | 36 | 97% | 8.8 | 9 (09-20 01:00Z) |
| us-west-2 usw2-az3 | 48 | 98% | 8.9 | 9 (09-20 01:00Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.715800 | 2026-09-20T01:00:48Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-20T01:00:48Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.844700 | 2026-09-20T01:00:48Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.025700 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588800 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579500 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565900 | 2026-09-20T01:00:48Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-09-20T01:00:48Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.497500 | 2026-09-20T01:00:48Z |
| ap-south-1 | ap-south-1a | Windows | 0.308300 | 2026-09-20T01:00:48Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.452000 | 2026-09-20T01:00:48Z |
| ap-south-1 | ap-south-1b | Windows | 0.316600 | 2026-09-20T01:00:48Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.683700 | 2026-09-20T01:00:48Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513100 | 2026-09-20T01:00:48Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.847200 | 2026-09-20T01:00:48Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559100 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.841000 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1a | Windows | 0.348300 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.623100 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1b | Windows | 0.314100 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.507200 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1c | Windows | 0.293900 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.516500 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1d | Windows | 0.308000 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509000 | 2026-09-20T01:00:48Z |
| us-east-1 | us-east-1f | Windows | 0.315500 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521600 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2a | Windows | 0.641300 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.522600 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2b | Windows | 0.642000 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514900 | 2026-09-20T01:00:48Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.570800 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2a | Windows | 0.339200 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526100 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2b | Windows | 0.336300 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528100 | 2026-09-20T01:00:48Z |
| us-west-2 | us-west-2c | Windows | 0.336800 | 2026-09-20T01:00:48Z |
