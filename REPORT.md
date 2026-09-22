# Spot placement score log

Generated 2026-09-22 09:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 146 | 0% | 1.9 | 3 (09-22 09:52Z) |
| ap-northeast-1 | 146 | 0% | 1.9 | 1 (09-22 09:52Z) |
| ap-northeast-2 | 146 | 0% | 3.0 | 3 (09-22 09:52Z) |
| ap-south-1 | 146 | 0% | 2.0 | 1 (09-22 09:52Z) |
| ap-southeast-2 | 146 | 0% | 1.0 | 1 (09-22 09:52Z) |
| ap-southeast-3 | 146 | 0% | 2.5 | 3 (09-22 09:52Z) |
| us-east-1 | 146 | 0% | 2.0 | 1 (09-22 09:52Z) |
| us-east-2 | 146 | 0% | 1.8 | 1 (09-22 09:52Z) |
| us-west-2 | 146 | 0% | 1.7 | 1 (09-22 09:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   332233211322122221122221112212233223123221121221
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333333311111211221113333113121133333333332111111
ap-southeast-2   111111111111111111111111111111111111111111113111
ap-southeast-3   333131331313313333313131123333333333313333133313
us-east-1        332222221221131121232231231112131122333333331321
us-east-2        333331111111131313333333133113333123333331331111
us-west-2        333331112111211111131221311123333333333333331211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 |
| ap-northeast-1 | 1 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 88 | 0% | 2.4 | 3 (09-22 09:52Z) |
| ap-northeast-1 apne1-az1 | 19 | 0% | 1.1 | 1 (09-22 09:52Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 129 | 0% | 2.9 | 3 (09-22 09:52Z) |
| ap-northeast-2 apne2-az3 | 128 | 0% | 2.9 | 3 (09-22 09:52Z) |
| ap-northeast-2 apne2-az4 | 143 | 0% | 3.0 | 3 (09-22 09:52Z) |
| ap-south-1 aps1-az1 | 56 | 0% | 1.7 | 1 (09-21 23:13Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 28 | 0% | 1.0 | 1 (09-21 19:19Z) |
| ap-southeast-3 apse3-az3 | 111 | 0% | 2.9 | 3 (09-22 09:52Z) |
| us-east-1 use1-az1 | 17 | 0% | 1.4 | 3 (09-20 21:28Z) |
| us-east-1 use1-az2 | 48 | 0% | 1.4 | 1 (09-21 19:19Z) |
| us-east-1 use1-az4 | 33 | 0% | 1.7 | 3 (09-21 23:13Z) |
| us-east-1 use1-az5 | 45 | 0% | 1.6 | 1 (09-22 09:52Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 48 | 0% | 1.8 | 1 (09-21 23:13Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 79 | 0% | 2.3 | 1 (09-22 09:52Z) |
| us-west-2 usw2-az1 | 44 | 0% | 2.1 | 3 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 75 | 0% | 1.8 | 3 (09-21 06:13Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 146 | 0% | 3.0 | 3 (09-22 09:52Z) |
| ap-northeast-1 | 146 | 79% | 7.6 | 9 (09-22 09:52Z) |
| ap-northeast-2 | 146 | 100% | 9.0 | 9 (09-22 09:52Z) |
| ap-south-1 | 146 | 45% | 5.5 | 2 (09-22 09:52Z) |
| ap-southeast-2 | 146 | 7% | 2.6 | 2 (09-22 09:52Z) |
| ap-southeast-3 | 146 | 0% | 2.5 | 3 (09-22 09:52Z) |
| us-east-1 | 146 | 75% | 6.9 | 9 (09-22 09:52Z) |
| us-east-2 | 146 | 75% | 7.2 | 9 (09-22 09:52Z) |
| us-west-2 | 146 | 53% | 5.8 | 9 (09-22 09:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   996499933999249994199993399999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999991899992999939999239999999999999999919992
ap-southeast-2   322222222222223322233222233233333333333332233122
ap-southeast-3   333131331313313333313131123333333333313333133313
us-east-1        999943684432493955995699994549999999999999994999
us-east-2        999999999921299999999999999119999199999999993399
us-west-2        999993425433534413994459533459999999999999994319
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 5 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 5 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 5 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 51 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 39 | 0% | 3.0 | 3 (09-21 19:19Z) |
| ap-east-1 ape1-az3 | 43 | 0% | 3.0 | 3 (09-21 23:13Z) |
| ap-northeast-1 apne1-az1 | 77 | 90% | 8.4 | 9 (09-22 09:52Z) |
| ap-northeast-1 apne1-az2 | 25 | 0% | 3.0 | 3 (09-21 19:19Z) |
| ap-northeast-1 apne1-az4 | 100 | 100% | 9.0 | 9 (09-22 09:52Z) |
| ap-northeast-2 apne2-az1 | 132 | 100% | 9.0 | 9 (09-22 09:52Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 132 | 100% | 9.0 | 9 (09-22 09:52Z) |
| ap-northeast-2 apne2-az4 | 46 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-south-1 aps1-az1 | 45 | 51% | 6.1 | 9 (09-21 23:13Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 62 | 71% | 7.3 | 9 (09-22 04:44Z) |
| ap-southeast-2 apse2-az1 | 12 | 25% | 4.3 | 3 (09-21 19:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 39 | 0% | 3.0 | 3 (09-21 19:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 61 | 100% | 9.0 | 9 (09-22 09:52Z) |
| us-east-1 use1-az4 | 64 | 97% | 8.8 | 9 (09-22 09:52Z) |
| us-east-1 use1-az5 | 29 | 97% | 8.8 | 9 (09-21 23:13Z) |
| us-east-1 use1-az6 | 60 | 100% | 9.0 | 9 (09-22 09:52Z) |
| us-east-2 use2-az1 | 58 | 100% | 9.0 | 9 (09-22 09:52Z) |
| us-east-2 use2-az2 | 91 | 98% | 8.8 | 9 (09-22 09:52Z) |
| us-east-2 use2-az3 | 75 | 89% | 8.3 | 9 (09-22 04:44Z) |
| us-west-2 usw2-az1 | 50 | 98% | 8.9 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 40 | 98% | 8.8 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az3 | 56 | 98% | 8.9 | 9 (09-22 09:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727200 | 2026-09-22T09:52:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.853100 | 2026-09-22T09:52:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.850800 | 2026-09-22T09:52:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.031700 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591700 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579400 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568000 | 2026-09-22T09:52:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743100 | 2026-09-22T09:52:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.473700 | 2026-09-22T09:52:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.317900 | 2026-09-22T09:52:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.455800 | 2026-09-22T09:52:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.312200 | 2026-09-22T09:52:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.668900 | 2026-09-22T09:52:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.536100 | 2026-09-22T09:52:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.790400 | 2026-09-22T09:52:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.814300 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1a | Windows | 0.352100 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.602200 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1b | Windows | 0.299900 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.477600 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1c | Windows | 0.287300 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.482200 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1d | Windows | 0.296000 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.464600 | 2026-09-22T09:52:35Z |
| us-east-1 | us-east-1f | Windows | 0.305400 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.528400 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2a | Windows | 0.641500 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527700 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2b | Windows | 0.641500 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516600 | 2026-09-22T09:52:35Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.528400 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2a | Windows | 0.337300 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.495700 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2b | Windows | 0.335300 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.491200 | 2026-09-22T09:52:35Z |
| us-west-2 | us-west-2c | Windows | 0.335500 | 2026-09-22T09:52:35Z |
