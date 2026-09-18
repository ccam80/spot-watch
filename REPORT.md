# Spot placement score log

Generated 2026-09-18 18:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 125 | 0% | 1.8 | 3 (09-18 18:21Z) |
| ap-northeast-1 | 125 | 0% | 1.9 | 2 (09-18 18:21Z) |
| ap-northeast-2 | 125 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-south-1 | 125 | 0% | 2.0 | 3 (09-18 18:21Z) |
| ap-southeast-2 | 125 | 0% | 1.0 | 1 (09-18 18:21Z) |
| ap-southeast-3 | 125 | 0% | 2.5 | 3 (09-18 18:21Z) |
| us-east-1 | 125 | 0% | 1.9 | 1 (09-18 18:21Z) |
| us-east-2 | 125 | 0% | 1.7 | 3 (09-18 18:21Z) |
| us-west-2 | 125 | 0% | 1.5 | 1 (09-18 18:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   232211233233333333333332233211322122221122221112
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       113131211113333333133333333311111211221113333113
ap-southeast-2   111111113111111111111111111111111111111111111111
ap-southeast-3   133333333333333333333333131331313313333313131123
us-east-1        211311311332233113232332222221221131121232231231
us-east-2        111111313113333333333333331111111131313333333133
us-west-2        111111111111333133133333331112111211111131221311
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 70 | 0% | 2.3 | 3 (09-18 18:21Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 63 | 0% | 2.2 | 1 (09-18 14:24Z) |
| ap-northeast-2 apne2-az1 | 113 | 0% | 2.9 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 111 | 0% | 2.9 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az4 | 122 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-south-1 aps1-az1 | 52 | 0% | 1.7 | 2 (09-18 18:21Z) |
| ap-south-1 aps1-az3 | 67 | 0% | 2.6 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 96 | 0% | 2.9 | 3 (09-18 18:21Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 38 | 0% | 1.1 | 1 (09-18 14:24Z) |
| us-east-1 use1-az4 | 24 | 0% | 1.3 | 3 (09-17 23:31Z) |
| us-east-1 use1-az5 | 36 | 0% | 1.4 | 1 (09-18 09:38Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 40 | 0% | 1.6 | 3 (09-18 04:33Z) |
| us-east-2 use2-az2 | 58 | 0% | 2.0 | 2 (09-18 18:21Z) |
| us-east-2 use2-az3 | 68 | 0% | 2.3 | 3 (09-18 18:21Z) |
| us-west-2 usw2-az1 | 32 | 0% | 1.9 | 1 (09-18 14:24Z) |
| us-west-2 usw2-az2 | 25 | 0% | 1.9 | 3 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 61 | 0% | 1.6 | 1 (09-18 09:38Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 125 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-1 | 125 | 75% | 7.3 | 9 (09-18 18:21Z) |
| ap-northeast-2 | 125 | 100% | 9.0 | 9 (09-18 18:21Z) |
| ap-south-1 | 125 | 37% | 5.0 | 9 (09-18 18:21Z) |
| ap-southeast-2 | 125 | 8% | 2.6 | 3 (09-18 18:21Z) |
| ap-southeast-3 | 125 | 0% | 2.5 | 3 (09-18 18:21Z) |
| us-east-1 | 125 | 73% | 6.7 | 4 (09-18 18:21Z) |
| us-east-2 | 125 | 75% | 7.2 | 9 (09-18 18:21Z) |
| us-west-2 | 125 | 48% | 5.5 | 3 (09-18 18:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   499923499999999999999996499933999249994199993399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       133399399999999999999999999991899992999939999239
ap-southeast-2   223112333333333333223322222222222223322233222233
ap-southeast-3   133333333333333333333333131331313313333313131123
us-east-1        932999923499999999999999943684432493955995699994
us-east-2        923339919199999999999999999999921299999999999999
us-west-2        133234233539999999999999993425433534413994459533
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 4 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 7 | 7 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 6 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 49 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 41 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-northeast-1 apne1-az1 | 64 | 88% | 8.2 | 9 (09-18 18:21Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 83 | 100% | 9.0 | 9 (09-18 18:21Z) |
| ap-northeast-2 apne2-az1 | 116 | 100% | 9.0 | 9 (09-18 18:21Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 115 | 100% | 9.0 | 9 (09-18 18:21Z) |
| ap-northeast-2 apne2-az4 | 44 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-south-1 aps1-az1 | 34 | 35% | 5.1 | 9 (09-18 18:21Z) |
| ap-south-1 aps1-az2 | 33 | 0% | 3.0 | 3 (09-17 20:14Z) |
| ap-south-1 aps1-az3 | 50 | 64% | 6.9 | 9 (09-18 18:21Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 37 | 0% | 3.0 | 3 (09-18 18:21Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 47 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-1 use1-az4 | 50 | 96% | 8.7 | 9 (09-18 09:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 48 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-2 use2-az1 | 50 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-2 use2-az2 | 85 | 98% | 8.8 | 9 (09-18 18:21Z) |
| us-east-2 use2-az3 | 62 | 87% | 8.1 | 9 (09-18 18:21Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 29 | 97% | 8.7 | 5 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710500 | 2026-09-18T18:21:08Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-18T18:21:08Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.839300 | 2026-09-18T18:21:08Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.022300 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589400 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579200 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565700 | 2026-09-18T18:21:08Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742500 | 2026-09-18T18:21:08Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.518100 | 2026-09-18T18:21:08Z |
| ap-south-1 | ap-south-1a | Windows | 0.314800 | 2026-09-18T18:21:08Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.462300 | 2026-09-18T18:21:08Z |
| ap-south-1 | ap-south-1b | Windows | 0.318400 | 2026-09-18T18:21:08Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686600 | 2026-09-18T18:21:08Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509400 | 2026-09-18T18:21:08Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.874100 | 2026-09-18T18:21:08Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.554400 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.843100 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1a | Windows | 0.344800 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.627200 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1b | Windows | 0.320700 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.526600 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1c | Windows | 0.297600 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.532300 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1d | Windows | 0.310000 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.528400 | 2026-09-18T18:21:08Z |
| us-east-1 | us-east-1f | Windows | 0.319800 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.519800 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523000 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2b | Windows | 0.638000 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516900 | 2026-09-18T18:21:08Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.570100 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2a | Windows | 0.340700 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.527100 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2b | Windows | 0.337900 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.531600 | 2026-09-18T18:21:08Z |
| us-west-2 | us-west-2c | Windows | 0.338100 | 2026-09-18T18:21:08Z |
