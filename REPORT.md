# Spot placement score log

Generated 2026-09-23 00:22 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 150 | 0% | 2.0 | 3 (09-23 00:22Z) |
| ap-northeast-1 | 150 | 0% | 1.9 | 2 (09-23 00:22Z) |
| ap-northeast-2 | 150 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-south-1 | 150 | 0% | 2.0 | 1 (09-23 00:22Z) |
| ap-southeast-2 | 150 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 | 150 | 0% | 2.5 | 3 (09-23 00:22Z) |
| us-east-1 | 150 | 0% | 2.0 | 2 (09-23 00:22Z) |
| us-east-2 | 150 | 0% | 1.8 | 3 (09-23 00:22Z) |
| us-west-2 | 150 | 0% | 1.7 | 2 (09-23 00:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   332113221222211222211122122332231232211212213322
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333111112112211133331131211333333333321111111111
ap-southeast-2   111111111111111111111111111111111111111131111111
ap-southeast-3   313313133133333131311233333333333133331333133333
us-east-1        222212211311212322312311121311223333333313212232
us-east-2        311111111313133333331331133331233333313311112113
us-west-2        311121112111111312213111233333333333333312112222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 92 | 0% | 2.4 | 3 (09-23 00:22Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 133 | 0% | 2.9 | 3 (09-23 00:22Z) |
| ap-northeast-2 apne2-az3 | 132 | 0% | 2.9 | 3 (09-23 00:22Z) |
| ap-northeast-2 apne2-az4 | 147 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-south-1 aps1-az1 | 57 | 0% | 1.7 | 1 (09-22 22:01Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 30 | 0% | 1.0 | 1 (09-22 22:01Z) |
| ap-southeast-3 apse3-az3 | 115 | 0% | 2.9 | 3 (09-23 00:22Z) |
| us-east-1 use1-az1 | 18 | 0% | 1.3 | 1 (09-22 14:44Z) |
| us-east-1 use1-az2 | 51 | 0% | 1.4 | 1 (09-22 22:01Z) |
| us-east-1 use1-az4 | 34 | 0% | 1.7 | 1 (09-22 14:44Z) |
| us-east-1 use1-az5 | 46 | 0% | 1.6 | 1 (09-22 18:48Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 50 | 0% | 1.8 | 3 (09-23 00:22Z) |
| us-east-2 use2-az2 | 62 | 0% | 2.0 | 3 (09-23 00:22Z) |
| us-east-2 use2-az3 | 81 | 0% | 2.3 | 3 (09-23 00:22Z) |
| us-west-2 usw2-az1 | 45 | 0% | 2.1 | 1 (09-23 00:22Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 77 | 0% | 1.8 | 1 (09-22 22:01Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 150 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-northeast-1 | 150 | 79% | 7.6 | 9 (09-23 00:22Z) |
| ap-northeast-2 | 150 | 100% | 9.0 | 9 (09-23 00:22Z) |
| ap-south-1 | 150 | 45% | 5.6 | 9 (09-23 00:22Z) |
| ap-southeast-2 | 150 | 7% | 2.6 | 2 (09-23 00:22Z) |
| ap-southeast-3 | 150 | 0% | 2.5 | 3 (09-23 00:22Z) |
| us-east-1 | 150 | 75% | 6.9 | 9 (09-23 00:22Z) |
| us-east-2 | 150 | 76% | 7.3 | 9 (09-23 00:22Z) |
| us-west-2 | 150 | 53% | 5.7 | 4 (09-23 00:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999339992499941999933999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999918999929999399992399999999999999999199924999
ap-southeast-2   222222222233222332222332333333333333322331222222
ap-southeast-3   313313133133333131311233333333333133331333133333
us-east-1        436844324939559956999945499999999999999949994459
us-east-2        999999212999999999999991199991999999999933995999
us-west-2        934254335344139944595334599999999999999943195454
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 5 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 5 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 5 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-east-1 ape1-az2 | 40 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-east-1 ape1-az3 | 44 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az1 | 80 | 90% | 8.4 | 9 (09-22 22:01Z) |
| ap-northeast-1 apne1-az2 | 26 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az4 | 104 | 100% | 9.0 | 9 (09-23 00:22Z) |
| ap-northeast-2 apne2-az1 | 136 | 100% | 9.0 | 9 (09-23 00:22Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 136 | 100% | 9.0 | 9 (09-23 00:22Z) |
| ap-northeast-2 apne2-az4 | 47 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-south-1 aps1-az1 | 48 | 54% | 6.2 | 9 (09-23 00:22Z) |
| ap-south-1 aps1-az2 | 36 | 0% | 3.0 | 3 (09-22 18:48Z) |
| ap-south-1 aps1-az3 | 65 | 72% | 7.4 | 9 (09-23 00:22Z) |
| ap-southeast-2 apse2-az1 | 12 | 25% | 4.3 | 3 (09-21 19:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 3.0 | 3 (09-22 14:44Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 61 | 100% | 9.0 | 9 (09-22 09:52Z) |
| us-east-1 use1-az4 | 64 | 97% | 8.8 | 9 (09-22 09:52Z) |
| us-east-1 use1-az5 | 30 | 97% | 8.8 | 9 (09-23 00:22Z) |
| us-east-1 use1-az6 | 60 | 100% | 9.0 | 9 (09-22 09:52Z) |
| us-east-2 use2-az1 | 61 | 98% | 8.9 | 9 (09-23 00:22Z) |
| us-east-2 use2-az2 | 94 | 98% | 8.8 | 9 (09-23 00:22Z) |
| us-east-2 use2-az3 | 78 | 90% | 8.3 | 9 (09-23 00:22Z) |
| us-west-2 usw2-az1 | 50 | 98% | 8.9 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 40 | 98% | 8.8 | 9 (09-21 06:13Z) |
| us-west-2 usw2-az3 | 56 | 98% | 8.9 | 9 (09-22 09:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.728400 | 2026-09-23T00:22:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.859900 | 2026-09-23T00:22:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.855800 | 2026-09-23T00:22:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.038800 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592100 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580000 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568700 | 2026-09-23T00:22:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-23T00:22:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.478800 | 2026-09-23T00:22:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.329200 | 2026-09-23T00:22:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.450300 | 2026-09-23T00:22:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.310300 | 2026-09-23T00:22:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.663900 | 2026-09-23T00:22:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.534000 | 2026-09-23T00:22:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.781300 | 2026-09-23T00:22:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.799700 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1a | Windows | 0.345800 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.593000 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1b | Windows | 0.297800 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.471700 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1c | Windows | 0.287700 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.471500 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1d | Windows | 0.295300 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.454500 | 2026-09-23T00:22:37Z |
| us-east-1 | us-east-1f | Windows | 0.302000 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526100 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2a | Windows | 0.641100 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524700 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.512200 | 2026-09-23T00:22:37Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.516200 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2a | Windows | 0.336700 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.484600 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2b | Windows | 0.334800 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.484400 | 2026-09-23T00:22:37Z |
| us-west-2 | us-west-2c | Windows | 0.335100 | 2026-09-23T00:22:37Z |
