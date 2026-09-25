# Spot placement score log

Generated 2026-09-25 07:41 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 162 | 6% | 2.4 | 9 (09-25 07:40Z) |
| ap-northeast-1 | 162 | 0% | 1.9 | 1 (09-25 07:40Z) |
| ap-northeast-2 | 162 | 6% | 3.3 | 9 (09-25 07:40Z) |
| ap-south-1 | 162 | 0% | 1.9 | 1 (09-25 07:40Z) |
| ap-southeast-2 | 162 | 0% | 1.0 | 1 (09-25 07:40Z) |
| ap-southeast-3 | 162 | 5% | 2.8 | 1 (09-25 07:40Z) |
| us-east-1 | 162 | 0% | 2.0 | 3 (09-25 07:40Z) |
| us-east-2 | 162 | 2% | 1.9 | 9 (09-25 07:40Z) |
| us-west-2 | 162 | 0% | 1.7 | 1 (09-25 07:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333999999999
ap-northeast-1   211222211122122332231232211212213322223322222211
ap-northeast-2   333333333333333333333333333333333333333999999999
ap-south-1       211133331131211333333333321111111111111111111121
ap-southeast-2   111111111111111111111111111131111111111111111111
ap-southeast-3   333131311233333333333133331333133333333996899951
us-east-1        212322312311121311223333333313212232322221232113
us-east-2        133333331331133331233333313311112113113192911219
us-west-2        111312213111233333333333333312112222132221122221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | · | 1 | 2 | 3 | 2 | 5 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 4 | · | 3 | 3 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 52 | 0% | 1.4 | 1 (09-25 07:40Z) |
| ap-east-1 ape1-az2 | 104 | 9% | 3.0 | 9 (09-25 07:40Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 76 | 0% | 2.1 | 1 (09-25 07:40Z) |
| ap-northeast-2 apne2-az1 | 145 | 6% | 3.3 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az3 | 144 | 6% | 3.3 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az4 | 159 | 6% | 3.3 | 9 (09-25 07:40Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 126 | 6% | 3.2 | 5 (09-25 01:25Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 55 | 0% | 1.3 | 1 (09-25 07:40Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 52 | 2% | 1.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 70 | 1% | 2.0 | 1 (09-25 07:40Z) |
| us-east-2 use2-az3 | 89 | 3% | 2.4 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az1 | 48 | 0% | 2.0 | 1 (09-25 07:40Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 162 | 6% | 3.3 | 9 (09-25 07:40Z) |
| ap-northeast-1 | 162 | 78% | 7.5 | 1 (09-25 07:40Z) |
| ap-northeast-2 | 162 | 100% | 9.0 | 9 (09-25 07:40Z) |
| ap-south-1 | 162 | 48% | 5.7 | 8 (09-25 07:40Z) |
| ap-southeast-2 | 162 | 8% | 2.7 | 2 (09-25 07:40Z) |
| ap-southeast-3 | 162 | 5% | 2.8 | 1 (09-25 07:40Z) |
| us-east-1 | 162 | 76% | 6.9 | 8 (09-25 07:40Z) |
| us-east-2 | 162 | 75% | 7.2 | 9 (09-25 07:40Z) |
| us-west-2 | 162 | 55% | 5.8 | 9 (09-25 07:40Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333999999999
ap-northeast-1   941999933999999999999999999999999999999993499921
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999399992399999999999999999199924999839999289998
ap-southeast-2   222332222332333333333333322331222222233512299222
ap-southeast-3   333131311233333333333133331333133333333996899951
us-east-1        559956999945499999999999999949994459996669954598
us-east-2        999999999991199991999999999933995999999499923489
us-west-2        139944595334599999999999999943195454995559554459
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 4 | · | 3 | 4 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 3 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 6 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 4 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 60 | 10% | 3.6 | 9 (09-25 07:40Z) |
| ap-east-1 ape1-az2 | 47 | 13% | 3.8 | 9 (09-25 07:40Z) |
| ap-east-1 ape1-az3 | 51 | 14% | 3.8 | 9 (09-25 07:40Z) |
| ap-northeast-1 apne1-az1 | 87 | 91% | 8.4 | 9 (09-24 22:18Z) |
| ap-northeast-1 apne1-az2 | 29 | 10% | 3.6 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az4 | 109 | 100% | 9.0 | 9 (09-24 22:18Z) |
| ap-northeast-2 apne2-az1 | 145 | 100% | 9.0 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az2 | 20 | 35% | 5.1 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az3 | 147 | 100% | 9.0 | 9 (09-25 07:40Z) |
| ap-northeast-2 apne2-az4 | 56 | 16% | 4.0 | 9 (09-25 07:40Z) |
| ap-south-1 aps1-az1 | 52 | 58% | 6.5 | 9 (09-24 22:18Z) |
| ap-south-1 aps1-az2 | 41 | 12% | 3.7 | 9 (09-25 01:25Z) |
| ap-south-1 aps1-az3 | 70 | 74% | 7.5 | 9 (09-25 01:25Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 14 | 14% | 3.9 | 9 (09-24 19:03Z) |
| ap-southeast-3 apse3-az3 | 44 | 9% | 3.5 | 9 (09-24 22:18Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 66 | 97% | 8.8 | 9 (09-25 01:25Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 64 | 100% | 9.0 | 9 (09-25 01:25Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 84 | 90% | 8.4 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 59 | 98% | 8.9 | 9 (09-25 07:40Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.726600 | 2026-09-25T07:40:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.866000 | 2026-09-25T07:40:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.832400 | 2026-09-25T07:40:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.019200 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591300 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578000 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568600 | 2026-09-25T07:40:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-25T07:40:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.499800 | 2026-09-25T07:40:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.330200 | 2026-09-25T07:40:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.483400 | 2026-09-25T07:40:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.309600 | 2026-09-25T07:40:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.641000 | 2026-09-25T07:40:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513000 | 2026-09-25T07:40:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.750900 | 2026-09-25T07:40:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.731300 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1a | Windows | 0.329100 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.540300 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1b | Windows | 0.290300 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.432300 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.431200 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1d | Windows | 0.285000 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.427200 | 2026-09-25T07:40:54Z |
| us-east-1 | us-east-1f | Windows | 0.291800 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.523900 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525400 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2b | Windows | 0.641200 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.512600 | 2026-09-25T07:40:54Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.515700 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2a | Windows | 0.333100 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.487700 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2b | Windows | 0.332900 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486700 | 2026-09-25T07:40:54Z |
| us-west-2 | us-west-2c | Windows | 0.331800 | 2026-09-25T07:40:54Z |
