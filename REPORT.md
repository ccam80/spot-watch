# Spot placement score log

Generated 2026-09-26 13:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 168 | 7% | 2.5 | 9 (09-26 13:00Z) |
| ap-northeast-1 | 168 | 0% | 2.0 | 1 (09-26 13:00Z) |
| ap-northeast-2 | 168 | 9% | 3.5 | 9 (09-26 13:00Z) |
| ap-south-1 | 168 | 0% | 1.9 | 1 (09-26 13:00Z) |
| ap-southeast-2 | 168 | 0% | 1.0 | 1 (09-26 13:00Z) |
| ap-southeast-3 | 168 | 8% | 3.0 | 8 (09-26 13:00Z) |
| us-east-1 | 168 | 0% | 2.0 | 2 (09-26 13:00Z) |
| us-east-2 | 168 | 5% | 2.1 | 9 (09-26 13:00Z) |
| us-west-2 | 168 | 1% | 1.8 | 9 (09-26 13:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333999999999119199
ap-northeast-1   211122122332231232211212213322223322222211343221
ap-northeast-2   333333333333333333333333333333333999999999999999
ap-south-1       331131211333333333321111111111111111111121111311
ap-southeast-2   111111111111111111111131111111111111111111111111
ap-southeast-3   311233333333333133331333133333333996899951989158
us-east-1        312311121311223333333313212232322221232113122332
us-east-2        331331133331233333313311112113113192911219928999
us-west-2        213111233333333333333312112222132221122221112199
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 6 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 5 | · | 3 | 3 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 2 | · | 1 | 2 | 2 | 2 | 6 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 3 | 2 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 1.4 | 1 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 107 | 11% | 3.2 | 9 (09-26 13:00Z) |
| ap-northeast-1 apne1-az1 | 22 | 0% | 1.2 | 2 (09-25 22:14Z) |
| ap-northeast-1 apne1-az4 | 77 | 0% | 2.1 | 1 (09-25 18:30Z) |
| ap-northeast-2 apne2-az1 | 151 | 10% | 3.5 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az3 | 150 | 10% | 3.5 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az4 | 165 | 9% | 3.5 | 9 (09-26 13:00Z) |
| ap-south-1 aps1-az1 | 59 | 0% | 1.7 | 1 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 83 | 0% | 2.5 | 2 (09-26 01:28Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 130 | 9% | 3.4 | 8 (09-26 13:00Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 56 | 0% | 1.3 | 1 (09-25 18:30Z) |
| us-east-1 use1-az4 | 36 | 0% | 1.7 | 1 (09-26 01:28Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 55 | 5% | 2.2 | 9 (09-26 07:34Z) |
| us-east-2 use2-az2 | 75 | 7% | 2.4 | 9 (09-26 13:00Z) |
| us-east-2 use2-az3 | 94 | 9% | 2.8 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az1 | 52 | 4% | 2.3 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az2 | 31 | 6% | 2.4 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az3 | 82 | 2% | 1.9 | 9 (09-26 13:00Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 168 | 9% | 3.5 | 9 (09-26 13:00Z) |
| ap-northeast-1 | 168 | 79% | 7.6 | 9 (09-26 13:00Z) |
| ap-northeast-2 | 168 | 100% | 9.0 | 9 (09-26 13:00Z) |
| ap-south-1 | 168 | 50% | 5.8 | 9 (09-26 13:00Z) |
| ap-southeast-2 | 168 | 11% | 2.9 | 9 (09-26 13:00Z) |
| ap-southeast-3 | 168 | 8% | 3.0 | 8 (09-26 13:00Z) |
| us-east-1 | 168 | 76% | 6.9 | 9 (09-26 13:00Z) |
| us-east-2 | 168 | 76% | 7.3 | 9 (09-26 13:00Z) |
| us-west-2 | 168 | 55% | 5.8 | 9 (09-26 13:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333999999999999999
ap-northeast-1   933999999999999999999999999999999993499921999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992399999999999999999199924999839999289998999999
ap-southeast-2   222332333333333333322331222222233512299222999999
ap-southeast-3   311233333333333133331333133333333996899951989158
us-east-1        999945499999999999999949994459996669954598347999
us-east-2        999991199991999999999933995999999499923489999999
us-west-2        595334599999999999999943195454995559554459934399
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | · | 3 | 4 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 7 | 3 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 7 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 4 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 65 | 17% | 4.0 | 9 (09-26 13:00Z) |
| ap-east-1 ape1-az2 | 51 | 20% | 4.2 | 9 (09-26 13:00Z) |
| ap-east-1 ape1-az3 | 53 | 17% | 4.0 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az1 | 88 | 91% | 8.4 | 9 (09-25 13:39Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 111 | 100% | 9.0 | 9 (09-26 07:34Z) |
| ap-northeast-2 apne2-az1 | 148 | 100% | 9.0 | 9 (09-26 07:34Z) |
| ap-northeast-2 apne2-az2 | 23 | 43% | 5.6 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az3 | 153 | 100% | 9.0 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az4 | 58 | 19% | 4.1 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 43 | 16% | 4.0 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 74 | 76% | 7.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az1 | 18 | 44% | 5.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 17 | 29% | 4.8 | 9 (09-25 22:14Z) |
| ap-southeast-3 apse3-az3 | 45 | 11% | 3.7 | 9 (09-25 13:39Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 63 | 100% | 9.0 | 9 (09-26 13:00Z) |
| us-east-1 use1-az4 | 67 | 97% | 8.8 | 9 (09-26 01:28Z) |
| us-east-1 use1-az5 | 33 | 97% | 8.8 | 9 (09-26 13:00Z) |
| us-east-1 use1-az6 | 65 | 100% | 9.0 | 9 (09-26 07:34Z) |
| us-east-2 use2-az1 | 66 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-east-2 use2-az2 | 99 | 98% | 8.8 | 9 (09-26 01:28Z) |
| us-east-2 use2-az3 | 86 | 91% | 8.4 | 9 (09-25 22:14Z) |
| us-west-2 usw2-az1 | 52 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 60 | 98% | 8.9 | 9 (09-25 13:39Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727200 | 2026-09-26T13:00:33Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.855900 | 2026-09-26T13:00:33Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.828400 | 2026-09-26T13:00:33Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.009400 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592300 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577800 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568000 | 2026-09-26T13:00:33Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-09-26T13:00:33Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.528900 | 2026-09-26T13:00:33Z |
| ap-south-1 | ap-south-1a | Windows | 0.343800 | 2026-09-26T13:00:33Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.519500 | 2026-09-26T13:00:33Z |
| ap-south-1 | ap-south-1b | Windows | 0.316000 | 2026-09-26T13:00:33Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651300 | 2026-09-26T13:00:33Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515300 | 2026-09-26T13:00:33Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.724000 | 2026-09-26T13:00:33Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.689200 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1a | Windows | 0.322000 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.510300 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1b | Windows | 0.287700 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.433100 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.409700 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.424600 | 2026-09-26T13:00:33Z |
| us-east-1 | us-east-1f | Windows | 0.286300 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525500 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527300 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2b | Windows | 0.641700 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513900 | 2026-09-26T13:00:33Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513700 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.485500 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2b | Windows | 0.332300 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.484100 | 2026-09-26T13:00:33Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-26T13:00:33Z |
