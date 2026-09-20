# Spot placement score log

Generated 2026-09-20 15:58 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 137 | 0% | 1.9 | 3 (09-20 15:58Z) |
| ap-northeast-1 | 137 | 0% | 1.9 | 3 (09-20 15:58Z) |
| ap-northeast-2 | 137 | 0% | 3.0 | 3 (09-20 15:58Z) |
| ap-south-1 | 137 | 0% | 2.1 | 3 (09-20 15:58Z) |
| ap-southeast-2 | 137 | 0% | 1.0 | 1 (09-20 15:58Z) |
| ap-southeast-3 | 137 | 0% | 2.5 | 3 (09-20 15:58Z) |
| us-east-1 | 137 | 0% | 1.9 | 3 (09-20 15:58Z) |
| us-east-2 | 137 | 0% | 1.8 | 3 (09-20 15:58Z) |
| us-west-2 | 137 | 0% | 1.6 | 3 (09-20 15:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333333333332233211322122221122221112212233223123
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333333133333333311111211221113333113121133333333
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333333131331313313333313131123333333333313
us-east-1        233113232332222221221131121232231231112131122333
us-east-2        333333333333331111111131313333333133113333123333
us-west-2        333133133333331112111211111131221311123333333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 40 | 0% | 1.4 | 3 (09-20 15:58Z) |
| ap-east-1 ape1-az2 | 80 | 0% | 2.4 | 3 (09-20 15:58Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 123 | 0% | 2.9 | 3 (09-20 11:17Z) |
| ap-northeast-2 apne2-az3 | 121 | 0% | 2.9 | 3 (09-20 11:17Z) |
| ap-northeast-2 apne2-az4 | 134 | 0% | 3.0 | 3 (09-20 15:58Z) |
| ap-south-1 aps1-az1 | 54 | 0% | 1.7 | 3 (09-19 22:55Z) |
| ap-south-1 aps1-az3 | 76 | 0% | 2.6 | 3 (09-20 15:58Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 104 | 0% | 2.9 | 3 (09-20 06:06Z) |
| us-east-1 use1-az1 | 16 | 0% | 1.2 | 3 (09-20 11:17Z) |
| us-east-1 use1-az2 | 42 | 0% | 1.2 | 3 (09-20 15:58Z) |
| us-east-1 use1-az4 | 28 | 0% | 1.5 | 3 (09-20 11:17Z) |
| us-east-1 use1-az5 | 39 | 0% | 1.5 | 3 (09-20 15:58Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 44 | 0% | 1.7 | 3 (09-20 01:00Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 74 | 0% | 2.3 | 3 (09-20 15:58Z) |
| us-west-2 usw2-az1 | 41 | 0% | 2.1 | 3 (09-20 15:58Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 72 | 0% | 1.8 | 3 (09-20 15:58Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 137 | 0% | 3.0 | 3 (09-20 15:58Z) |
| ap-northeast-1 | 137 | 77% | 7.5 | 9 (09-20 15:58Z) |
| ap-northeast-2 | 137 | 100% | 9.0 | 9 (09-20 15:58Z) |
| ap-south-1 | 137 | 42% | 5.4 | 9 (09-20 15:58Z) |
| ap-southeast-2 | 137 | 7% | 2.6 | 3 (09-20 15:58Z) |
| ap-southeast-3 | 137 | 0% | 2.5 | 3 (09-20 15:58Z) |
| us-east-1 | 137 | 74% | 6.8 | 9 (09-20 15:58Z) |
| us-east-2 | 137 | 75% | 7.2 | 9 (09-20 15:58Z) |
| us-west-2 | 137 | 52% | 5.7 | 9 (09-20 15:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999996499933999249994199993399999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999991899992999939999239999999999999
ap-southeast-2   333333223322222222222223322233222233233333333333
ap-southeast-3   333333333333131331313313333313131123333333333313
us-east-1        999999999999943684432493955995699994549999999999
us-east-2        999999999999999999921299999999999999119999199999
us-west-2        999999999999993425433534413994459533459999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 4 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 5 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 6 | 7 | 9 | 6 | 7 | 4 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 69 | 88% | 8.3 | 9 (09-20 11:17Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 93 | 100% | 9.0 | 9 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 124 | 100% | 9.0 | 9 (09-20 15:58Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 124 | 100% | 9.0 | 9 (09-20 15:58Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 41 | 46% | 5.8 | 9 (09-20 11:17Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 56 | 68% | 7.1 | 9 (09-20 15:58Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 56 | 100% | 9.0 | 9 (09-20 11:17Z) |
| us-east-1 use1-az4 | 58 | 97% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az5 | 25 | 96% | 8.7 | 9 (09-20 15:58Z) |
| us-east-1 use1-az6 | 55 | 100% | 9.0 | 9 (09-20 15:58Z) |
| us-east-2 use2-az1 | 54 | 100% | 9.0 | 9 (09-20 15:58Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 70 | 89% | 8.2 | 9 (09-20 15:58Z) |
| us-west-2 usw2-az1 | 47 | 98% | 8.9 | 9 (09-20 11:17Z) |
| us-west-2 usw2-az2 | 39 | 97% | 8.8 | 9 (09-20 15:58Z) |
| us-west-2 usw2-az3 | 51 | 98% | 8.9 | 9 (09-20 15:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.717600 | 2026-09-20T15:58:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-20T15:58:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.846100 | 2026-09-20T15:58:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.026700 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589700 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579900 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566200 | 2026-09-20T15:58:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742800 | 2026-09-20T15:58:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.484600 | 2026-09-20T15:58:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.305800 | 2026-09-20T15:58:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.442500 | 2026-09-20T15:58:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.315300 | 2026-09-20T15:58:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.685700 | 2026-09-20T15:58:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523400 | 2026-09-20T15:58:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.841800 | 2026-09-20T15:58:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574100 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.836100 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1a | Windows | 0.357200 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.622300 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1b | Windows | 0.310100 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.511000 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1c | Windows | 0.291300 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.508000 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1d | Windows | 0.305800 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.497600 | 2026-09-20T15:58:32Z |
| us-east-1 | us-east-1f | Windows | 0.314200 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.522800 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.522900 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2b | Windows | 0.642100 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515400 | 2026-09-20T15:58:32Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.563200 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2a | Windows | 0.338900 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.524500 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2b | Windows | 0.336100 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527500 | 2026-09-20T15:58:32Z |
| us-west-2 | us-west-2c | Windows | 0.336500 | 2026-09-20T15:58:32Z |
