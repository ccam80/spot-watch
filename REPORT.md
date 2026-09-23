# Spot placement score log

Generated 2026-09-23 16:49 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 153 | 0% | 2.0 | 3 (09-23 16:48Z) |
| ap-northeast-1 | 153 | 0% | 1.9 | 3 (09-23 16:48Z) |
| ap-northeast-2 | 153 | 0% | 3.0 | 3 (09-23 16:48Z) |
| ap-south-1 | 153 | 0% | 2.0 | 1 (09-23 16:48Z) |
| ap-southeast-2 | 153 | 0% | 1.0 | 1 (09-23 16:48Z) |
| ap-southeast-3 | 153 | 0% | 2.6 | 3 (09-23 16:48Z) |
| us-east-1 | 153 | 0% | 2.0 | 2 (09-23 16:48Z) |
| us-east-2 | 153 | 0% | 1.8 | 3 (09-23 16:48Z) |
| us-west-2 | 153 | 0% | 1.7 | 2 (09-23 16:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   113221222211222211122122332231232211212213322223
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       111112112211133331131211333333333321111111111111
ap-southeast-2   111111111111111111111111111111111111131111111111
ap-southeast-3   313133133333131311233333333333133331333133333333
us-east-1        212211311212322312311121311223333333313212232322
us-east-2        111111313133333331331133331233333313311112113113
us-west-2        121112111111312213111233333333333333312112222132
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 95 | 0% | 2.5 | 3 (09-23 16:48Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 68 | 0% | 2.2 | 1 (09-23 11:25Z) |
| ap-northeast-2 apne2-az1 | 136 | 0% | 2.9 | 3 (09-23 16:48Z) |
| ap-northeast-2 apne2-az3 | 135 | 0% | 2.9 | 3 (09-23 16:48Z) |
| ap-northeast-2 apne2-az4 | 150 | 0% | 3.0 | 3 (09-23 16:48Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 31 | 0% | 1.0 | 1 (09-23 16:48Z) |
| ap-southeast-3 apse3-az3 | 118 | 0% | 2.9 | 3 (09-23 16:48Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 53 | 0% | 1.3 | 1 (09-23 16:48Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 47 | 0% | 1.6 | 1 (09-23 16:48Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 51 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-east-2 use2-az2 | 62 | 0% | 2.0 | 3 (09-23 00:22Z) |
| us-east-2 use2-az3 | 83 | 0% | 2.3 | 3 (09-23 16:48Z) |
| us-west-2 usw2-az1 | 46 | 0% | 2.1 | 1 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 153 | 0% | 3.0 | 3 (09-23 16:48Z) |
| ap-northeast-1 | 153 | 80% | 7.6 | 9 (09-23 16:48Z) |
| ap-northeast-2 | 153 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-south-1 | 153 | 46% | 5.6 | 9 (09-23 16:48Z) |
| ap-southeast-2 | 153 | 7% | 2.6 | 3 (09-23 16:48Z) |
| ap-southeast-3 | 153 | 0% | 2.6 | 3 (09-23 16:48Z) |
| us-east-1 | 153 | 75% | 6.9 | 6 (09-23 16:48Z) |
| us-east-2 | 153 | 76% | 7.3 | 9 (09-23 16:48Z) |
| us-west-2 | 153 | 54% | 5.8 | 5 (09-23 16:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   339992499941999933999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       918999929999399992399999999999999999199924999839
ap-southeast-2   222222233222332222332333333333333322331222222233
ap-southeast-3   313133133333131311233333333333133331333133333333
us-east-1        844324939559956999945499999999999999949994459996
us-east-2        999212999999999999991199991999999999933995999999
us-west-2        254335344139944595334599999999999999943195454995
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 5 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 5 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 5 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-east-1 ape1-az2 | 41 | 0% | 3.0 | 3 (09-23 16:48Z) |
| ap-east-1 ape1-az3 | 44 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az1 | 83 | 90% | 8.4 | 9 (09-23 16:48Z) |
| ap-northeast-1 apne1-az2 | 26 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az4 | 106 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az1 | 139 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 139 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az4 | 47 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-south-1 aps1-az1 | 49 | 55% | 6.3 | 9 (09-23 16:48Z) |
| ap-south-1 aps1-az2 | 36 | 0% | 3.0 | 3 (09-22 18:48Z) |
| ap-south-1 aps1-az3 | 66 | 73% | 7.4 | 9 (09-23 16:48Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 3.0 | 3 (09-22 14:44Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 30 | 97% | 8.8 | 9 (09-23 00:22Z) |
| us-east-1 use1-az6 | 62 | 100% | 9.0 | 9 (09-23 11:25Z) |
| us-east-2 use2-az1 | 61 | 98% | 8.9 | 9 (09-23 00:22Z) |
| us-east-2 use2-az2 | 97 | 98% | 8.8 | 9 (09-23 16:48Z) |
| us-east-2 use2-az3 | 81 | 90% | 8.3 | 9 (09-23 16:48Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727600 | 2026-09-23T16:48:58Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.865900 | 2026-09-23T16:48:58Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.852700 | 2026-09-23T16:48:58Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.032700 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591900 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579400 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568800 | 2026-09-23T16:48:58Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-23T16:48:58Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.484100 | 2026-09-23T16:48:58Z |
| ap-south-1 | ap-south-1a | Windows | 0.334200 | 2026-09-23T16:48:58Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.454500 | 2026-09-23T16:48:58Z |
| ap-south-1 | ap-south-1b | Windows | 0.307200 | 2026-09-23T16:48:58Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.655100 | 2026-09-23T16:48:58Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.524700 | 2026-09-23T16:48:58Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.772200 | 2026-09-23T16:48:58Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.781300 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1a | Windows | 0.342600 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.586100 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1b | Windows | 0.295100 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.463100 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1c | Windows | 0.286700 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.457200 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1d | Windows | 0.292800 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.446000 | 2026-09-23T16:48:58Z |
| us-east-1 | us-east-1f | Windows | 0.299400 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526000 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2a | Windows | 0.641100 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523600 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.510700 | 2026-09-23T16:48:58Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.515900 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2a | Windows | 0.334700 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.483700 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2b | Windows | 0.333900 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.487200 | 2026-09-23T16:48:58Z |
| us-west-2 | us-west-2c | Windows | 0.333500 | 2026-09-23T16:48:58Z |
