# Spot placement score log

Generated 2026-09-24 04:37 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 156 | 2% | 2.1 | 9 (09-24 04:37Z) |
| ap-northeast-1 | 156 | 0% | 1.9 | 2 (09-24 04:37Z) |
| ap-northeast-2 | 156 | 2% | 3.1 | 9 (09-24 04:37Z) |
| ap-south-1 | 156 | 0% | 2.0 | 1 (09-24 04:37Z) |
| ap-southeast-2 | 156 | 0% | 1.0 | 1 (09-24 04:37Z) |
| ap-southeast-3 | 156 | 2% | 2.7 | 6 (09-24 04:37Z) |
| us-east-1 | 156 | 0% | 2.0 | 1 (09-24 04:37Z) |
| us-east-2 | 156 | 1% | 1.8 | 2 (09-24 04:37Z) |
| us-west-2 | 156 | 0% | 1.7 | 1 (09-24 04:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333999
ap-northeast-1   221222211222211122122332231232211212213322223322
ap-northeast-2   333333333333333333333333333333333333333333333999
ap-south-1       112112211133331131211333333333321111111111111111
ap-southeast-2   111111111111111111111111111111111131111111111111
ap-southeast-3   133133333131311233333333333133331333133333333996
us-east-1        211311212322312311121311223333333313212232322221
us-east-2        111313133333331331133331233333313311112113113192
us-west-2        112111111312213111233333333333333312112222132221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 46 | 0% | 1.5 | 1 (09-24 04:37Z) |
| ap-east-1 ape1-az2 | 98 | 3% | 2.7 | 9 (09-24 04:37Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 71 | 0% | 2.2 | 1 (09-24 04:37Z) |
| ap-northeast-2 apne2-az1 | 139 | 2% | 3.1 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az3 | 138 | 2% | 3.0 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az4 | 153 | 2% | 3.1 | 9 (09-24 04:37Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 33 | 0% | 1.0 | 1 (09-24 04:37Z) |
| ap-southeast-3 apse3-az3 | 121 | 2% | 3.0 | 6 (09-24 04:37Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 54 | 0% | 1.3 | 1 (09-23 20:14Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 48 | 0% | 1.5 | 1 (09-23 23:37Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 51 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-east-2 use2-az2 | 64 | 0% | 2.0 | 1 (09-24 04:37Z) |
| us-east-2 use2-az3 | 85 | 1% | 2.3 | 1 (09-24 04:37Z) |
| us-west-2 usw2-az1 | 47 | 0% | 2.1 | 1 (09-23 20:14Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 156 | 2% | 3.1 | 9 (09-24 04:37Z) |
| ap-northeast-1 | 156 | 79% | 7.6 | 3 (09-24 04:37Z) |
| ap-northeast-2 | 156 | 100% | 9.0 | 9 (09-24 04:37Z) |
| ap-south-1 | 156 | 47% | 5.6 | 9 (09-24 04:37Z) |
| ap-southeast-2 | 156 | 7% | 2.6 | 2 (09-24 04:37Z) |
| ap-southeast-3 | 156 | 2% | 2.7 | 6 (09-24 04:37Z) |
| us-east-1 | 156 | 76% | 6.9 | 9 (09-24 04:37Z) |
| us-east-2 | 156 | 76% | 7.3 | 9 (09-24 04:37Z) |
| us-west-2 | 156 | 54% | 5.8 | 9 (09-24 04:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333999
ap-northeast-1   992499941999933999999999999999999999999999999993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999929999399992399999999999999999199924999839999
ap-southeast-2   222233222332222332333333333333322331222222233512
ap-southeast-3   133133333131311233333333333133331333133333333996
us-east-1        324939559956999945499999999999999949994459996669
us-east-2        212999999999999991199991999999999933995999999499
us-west-2        335344139944595334599999999999999943195454995559
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 56 | 4% | 3.2 | 9 (09-24 04:37Z) |
| ap-east-1 ape1-az2 | 43 | 5% | 3.3 | 9 (09-23 23:37Z) |
| ap-east-1 ape1-az3 | 46 | 4% | 3.3 | 9 (09-24 04:37Z) |
| ap-northeast-1 apne1-az1 | 84 | 90% | 8.4 | 9 (09-23 23:37Z) |
| ap-northeast-1 apne1-az2 | 27 | 4% | 3.2 | 9 (09-23 20:14Z) |
| ap-northeast-1 apne1-az4 | 106 | 100% | 9.0 | 9 (09-23 16:48Z) |
| ap-northeast-2 apne2-az1 | 142 | 100% | 9.0 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az2 | 14 | 7% | 3.4 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az3 | 142 | 100% | 9.0 | 9 (09-24 04:37Z) |
| ap-northeast-2 apne2-az4 | 50 | 6% | 3.4 | 9 (09-24 04:37Z) |
| ap-south-1 aps1-az1 | 51 | 57% | 6.4 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az2 | 38 | 5% | 3.3 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az3 | 68 | 74% | 7.4 | 9 (09-24 04:37Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 42 | 5% | 3.3 | 9 (09-23 23:37Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 31 | 97% | 8.8 | 9 (09-24 04:37Z) |
| us-east-1 use1-az6 | 63 | 100% | 9.0 | 9 (09-24 04:37Z) |
| us-east-2 use2-az1 | 62 | 98% | 8.9 | 9 (09-24 04:37Z) |
| us-east-2 use2-az2 | 97 | 98% | 8.8 | 9 (09-23 16:48Z) |
| us-east-2 use2-az3 | 82 | 90% | 8.3 | 9 (09-23 23:37Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727400 | 2026-09-24T04:37:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.864900 | 2026-09-24T04:37:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.840600 | 2026-09-24T04:37:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.021500 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591700 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579000 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568600 | 2026-09-24T04:37:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-24T04:37:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.488500 | 2026-09-24T04:37:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.334200 | 2026-09-24T04:37:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.458000 | 2026-09-24T04:37:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.307000 | 2026-09-24T04:37:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.653300 | 2026-09-24T04:37:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.524500 | 2026-09-24T04:37:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.759900 | 2026-09-24T04:37:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.758100 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1a | Windows | 0.340400 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.565800 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1b | Windows | 0.292100 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.451100 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1c | Windows | 0.285400 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.450700 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1d | Windows | 0.289700 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.437400 | 2026-09-24T04:37:37Z |
| us-east-1 | us-east-1f | Windows | 0.296700 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525700 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2a | Windows | 0.641200 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524100 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.510700 | 2026-09-24T04:37:37Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.517500 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2a | Windows | 0.333900 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.482900 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2b | Windows | 0.333400 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-24T04:37:37Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-24T04:37:37Z |
