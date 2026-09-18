# Spot placement score log

Generated 2026-09-18 21:36 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 126 | 0% | 1.8 | 3 (09-18 21:36Z) |
| ap-northeast-1 | 126 | 0% | 1.9 | 2 (09-18 21:36Z) |
| ap-northeast-2 | 126 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-south-1 | 126 | 0% | 2.0 | 1 (09-18 21:36Z) |
| ap-southeast-2 | 126 | 0% | 1.0 | 1 (09-18 21:36Z) |
| ap-southeast-3 | 126 | 0% | 2.5 | 3 (09-18 21:36Z) |
| us-east-1 | 126 | 0% | 1.9 | 1 (09-18 21:36Z) |
| us-east-2 | 126 | 0% | 1.7 | 1 (09-18 21:36Z) |
| us-west-2 | 126 | 0% | 1.5 | 1 (09-18 21:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   322112332333333333333322332113221222211222211122
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       131312111133333331333333333111112112211133331131
ap-southeast-2   111111131111111111111111111111111111111111111111
ap-southeast-3   333333333333333333333331313313133133333131311233
us-east-1        113113113322331132323322222212211311212322312311
us-east-2        111113131133333333333333311111111313133333331331
us-west-2        111111111113331331333333311121112111111312213111
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
| ap-east-1 ape1-az2 | 71 | 0% | 2.3 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 64 | 0% | 2.2 | 1 (09-18 21:36Z) |
| ap-northeast-2 apne2-az1 | 114 | 0% | 2.9 | 3 (09-18 21:36Z) |
| ap-northeast-2 apne2-az3 | 112 | 0% | 2.9 | 3 (09-18 21:36Z) |
| ap-northeast-2 apne2-az4 | 123 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-south-1 aps1-az1 | 52 | 0% | 1.7 | 2 (09-18 18:21Z) |
| ap-south-1 aps1-az3 | 68 | 0% | 2.5 | 1 (09-18 21:36Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 97 | 0% | 2.9 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 39 | 0% | 1.1 | 1 (09-18 21:36Z) |
| us-east-1 use1-az4 | 24 | 0% | 1.3 | 3 (09-17 23:31Z) |
| us-east-1 use1-az5 | 36 | 0% | 1.4 | 1 (09-18 09:38Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 40 | 0% | 1.6 | 3 (09-18 04:33Z) |
| us-east-2 use2-az2 | 58 | 0% | 2.0 | 2 (09-18 18:21Z) |
| us-east-2 use2-az3 | 69 | 0% | 2.3 | 1 (09-18 21:36Z) |
| us-west-2 usw2-az1 | 33 | 0% | 1.8 | 1 (09-18 21:36Z) |
| us-west-2 usw2-az2 | 25 | 0% | 1.9 | 3 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 61 | 0% | 1.6 | 1 (09-18 09:38Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 126 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 | 126 | 75% | 7.3 | 9 (09-18 21:36Z) |
| ap-northeast-2 | 126 | 100% | 9.0 | 9 (09-18 21:36Z) |
| ap-south-1 | 126 | 37% | 5.1 | 9 (09-18 21:36Z) |
| ap-southeast-2 | 126 | 8% | 2.6 | 2 (09-18 21:36Z) |
| ap-southeast-3 | 126 | 0% | 2.5 | 3 (09-18 21:36Z) |
| us-east-1 | 126 | 73% | 6.7 | 5 (09-18 21:36Z) |
| us-east-2 | 126 | 75% | 7.2 | 1 (09-18 21:36Z) |
| us-west-2 | 126 | 48% | 5.5 | 4 (09-18 21:36Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999234999999999999999964999339992499941999933999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333993999999999999999999999918999929999399992399
ap-southeast-2   231123333333333332233222222222222233222332222332
ap-southeast-3   333333333333333333333331313313133133333131311233
us-east-1        329999234999999999999999436844324939559956999945
us-east-2        233399191999999999999999999999212999999999999991
us-west-2        332342335399999999999999934254335344139944595334
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 4 | 5 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 7 | 6 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 6 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 49 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 65 | 88% | 8.2 | 9 (09-18 21:36Z) |
| ap-northeast-1 apne1-az2 | 23 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az4 | 84 | 100% | 9.0 | 9 (09-18 21:36Z) |
| ap-northeast-2 apne2-az1 | 117 | 100% | 9.0 | 9 (09-18 21:36Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 116 | 100% | 9.0 | 9 (09-18 21:36Z) |
| ap-northeast-2 apne2-az4 | 44 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-south-1 aps1-az1 | 35 | 37% | 5.2 | 9 (09-18 21:36Z) |
| ap-south-1 aps1-az2 | 34 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-south-1 aps1-az3 | 51 | 65% | 6.9 | 9 (09-18 21:36Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710500 | 2026-09-18T21:36:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-18T21:36:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.841400 | 2026-09-18T21:36:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.022300 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589300 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579200 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566000 | 2026-09-18T21:36:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742500 | 2026-09-18T21:36:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.518100 | 2026-09-18T21:36:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.312700 | 2026-09-18T21:36:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.462000 | 2026-09-18T21:36:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.318400 | 2026-09-18T21:36:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686600 | 2026-09-18T21:36:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.510500 | 2026-09-18T21:36:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.874100 | 2026-09-18T21:36:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556700 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.843100 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1a | Windows | 0.344500 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.627200 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1b | Windows | 0.320700 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.517500 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1c | Windows | 0.297600 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.532300 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1d | Windows | 0.310000 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.525200 | 2026-09-18T21:36:35Z |
| us-east-1 | us-east-1f | Windows | 0.318800 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521800 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.522700 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2b | Windows | 0.638600 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515600 | 2026-09-18T21:36:35Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.570100 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2a | Windows | 0.340300 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.527100 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2b | Windows | 0.337700 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526800 | 2026-09-18T21:36:35Z |
| us-west-2 | us-west-2c | Windows | 0.338100 | 2026-09-18T21:36:35Z |
