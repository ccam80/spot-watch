# Spot placement score log

Generated 2026-09-21 23:13 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 144 | 0% | 1.9 | 3 (09-21 23:13Z) |
| ap-northeast-1 | 144 | 0% | 1.9 | 2 (09-21 23:13Z) |
| ap-northeast-2 | 144 | 0% | 3.0 | 3 (09-21 23:13Z) |
| ap-south-1 | 144 | 0% | 2.0 | 1 (09-21 23:13Z) |
| ap-southeast-2 | 144 | 0% | 1.0 | 1 (09-21 23:13Z) |
| ap-southeast-3 | 144 | 0% | 2.5 | 3 (09-21 23:13Z) |
| us-east-1 | 144 | 0% | 2.0 | 3 (09-21 23:13Z) |
| us-east-2 | 144 | 0% | 1.8 | 1 (09-21 23:13Z) |
| us-west-2 | 144 | 0% | 1.7 | 2 (09-21 23:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333322332113221222211222211122122332231232211212
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333333333111112112211133331131211333333333321111
ap-southeast-2   111111111111111111111111111111111111111111111131
ap-southeast-3   333331313313133133333131311233333333333133331333
us-east-1        323322222212211311212322312311121311223333333313
us-east-2        333333311111111313133333331331133331233333313311
us-west-2        333333311121112111111312213111233333333333333312
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 |
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
| ap-east-1 ape1-az2 | 86 | 0% | 2.4 | 3 (09-21 23:13Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 127 | 0% | 2.9 | 3 (09-21 23:13Z) |
| ap-northeast-2 apne2-az3 | 126 | 0% | 2.9 | 3 (09-21 23:13Z) |
| ap-northeast-2 apne2-az4 | 141 | 0% | 3.0 | 3 (09-21 23:13Z) |
| ap-south-1 aps1-az1 | 56 | 0% | 1.7 | 1 (09-21 23:13Z) |
| ap-south-1 aps1-az3 | 78 | 0% | 2.6 | 3 (09-20 21:28Z) |
| ap-southeast-2 apse2-az1 | 24 | 0% | 1.2 | 3 (09-21 19:19Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 28 | 0% | 1.0 | 1 (09-21 19:19Z) |
| ap-southeast-3 apse3-az3 | 109 | 0% | 2.9 | 3 (09-21 23:13Z) |
| us-east-1 use1-az1 | 17 | 0% | 1.4 | 3 (09-20 21:28Z) |
| us-east-1 use1-az2 | 48 | 0% | 1.4 | 1 (09-21 19:19Z) |
| us-east-1 use1-az4 | 33 | 0% | 1.7 | 3 (09-21 23:13Z) |
| us-east-1 use1-az5 | 43 | 0% | 1.6 | 3 (09-21 23:13Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 48 | 0% | 1.8 | 1 (09-21 23:13Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 77 | 0% | 2.3 | 1 (09-21 19:19Z) |
| us-west-2 usw2-az1 | 44 | 0% | 2.1 | 3 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 75 | 0% | 1.8 | 3 (09-21 06:13Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 144 | 0% | 3.0 | 3 (09-21 23:13Z) |
| ap-northeast-1 | 144 | 78% | 7.5 | 9 (09-21 23:13Z) |
| ap-northeast-2 | 144 | 100% | 9.0 | 9 (09-21 23:13Z) |
| ap-south-1 | 144 | 44% | 5.5 | 9 (09-21 23:13Z) |
| ap-southeast-2 | 144 | 7% | 2.6 | 1 (09-21 23:13Z) |
| ap-southeast-3 | 144 | 0% | 2.5 | 3 (09-21 23:13Z) |
| us-east-1 | 144 | 75% | 6.9 | 9 (09-21 23:13Z) |
| us-east-2 | 144 | 75% | 7.2 | 3 (09-21 23:13Z) |
| us-west-2 | 144 | 53% | 5.8 | 3 (09-21 23:13Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999964999339992499941999933999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999918999929999399992399999999999999999199
ap-southeast-2   233222222222222233222332222332333333333333322331
ap-southeast-3   333331313313133133333131311233333333333133331333
us-east-1        999999436844324939559956999945499999999999999949
us-east-2        999999999999212999999999999991199991999999999933
us-west-2        999999934254335344139944595334599999999999999943
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 7 | 5 | 3 | 3 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 5 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 51 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 39 | 0% | 3.0 | 3 (09-21 19:19Z) |
| ap-east-1 ape1-az3 | 43 | 0% | 3.0 | 3 (09-21 23:13Z) |
| ap-northeast-1 apne1-az1 | 75 | 89% | 8.3 | 9 (09-21 23:13Z) |
| ap-northeast-1 apne1-az2 | 25 | 0% | 3.0 | 3 (09-21 19:19Z) |
| ap-northeast-1 apne1-az4 | 98 | 100% | 9.0 | 9 (09-21 23:13Z) |
| ap-northeast-2 apne2-az1 | 130 | 100% | 9.0 | 9 (09-21 23:13Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 130 | 100% | 9.0 | 9 (09-21 23:13Z) |
| ap-northeast-2 apne2-az4 | 46 | 0% | 3.0 | 3 (09-21 13:58Z) |
| ap-south-1 aps1-az1 | 45 | 51% | 6.1 | 9 (09-21 23:13Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 61 | 70% | 7.2 | 9 (09-21 23:13Z) |
| ap-southeast-2 apse2-az1 | 12 | 25% | 4.3 | 3 (09-21 19:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 39 | 0% | 3.0 | 3 (09-21 19:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 60 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-1 use1-az4 | 62 | 97% | 8.8 | 9 (09-21 23:13Z) |
| us-east-1 use1-az5 | 29 | 97% | 8.8 | 9 (09-21 23:13Z) |
| us-east-1 use1-az6 | 58 | 100% | 9.0 | 9 (09-21 23:13Z) |
| us-east-2 use2-az1 | 56 | 100% | 9.0 | 9 (09-21 06:13Z) |
| us-east-2 use2-az2 | 89 | 98% | 8.8 | 9 (09-21 13:58Z) |
| us-east-2 use2-az3 | 74 | 89% | 8.3 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az1 | 50 | 98% | 8.9 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 40 | 98% | 8.8 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az3 | 55 | 98% | 8.9 | 9 (09-21 13:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725900 | 2026-09-21T23:13:21Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.848700 | 2026-09-21T23:13:21Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.844700 | 2026-09-21T23:13:21Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.029700 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591200 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579400 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567200 | 2026-09-21T23:13:21Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743000 | 2026-09-21T23:13:21Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.468000 | 2026-09-21T23:13:21Z |
| ap-south-1 | ap-south-1a | Windows | 0.307900 | 2026-09-21T23:13:21Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.445800 | 2026-09-21T23:13:21Z |
| ap-south-1 | ap-south-1b | Windows | 0.312200 | 2026-09-21T23:13:21Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.685900 | 2026-09-21T23:13:21Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.536100 | 2026-09-21T23:13:21Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.808000 | 2026-09-21T23:13:21Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.815800 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1a | Windows | 0.355000 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.614100 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1b | Windows | 0.303800 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.493300 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1c | Windows | 0.288600 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.485300 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1d | Windows | 0.300200 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.464900 | 2026-09-21T23:13:21Z |
| us-east-1 | us-east-1f | Windows | 0.306700 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525900 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2a | Windows | 0.641800 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525200 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2b | Windows | 0.641600 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-09-21T23:13:21Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.535200 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2a | Windows | 0.337400 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496800 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2b | Windows | 0.335400 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.499000 | 2026-09-21T23:13:21Z |
| us-west-2 | us-west-2c | Windows | 0.335900 | 2026-09-21T23:13:21Z |
