# Spot placement score log

Generated 2026-09-24 19:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 159 | 4% | 2.3 | 9 (09-24 19:03Z) |
| ap-northeast-1 | 159 | 0% | 1.9 | 2 (09-24 19:03Z) |
| ap-northeast-2 | 159 | 4% | 3.2 | 9 (09-24 19:03Z) |
| ap-south-1 | 159 | 0% | 1.9 | 1 (09-24 19:03Z) |
| ap-southeast-2 | 159 | 0% | 1.0 | 1 (09-24 19:03Z) |
| ap-southeast-3 | 159 | 4% | 2.8 | 9 (09-24 19:03Z) |
| us-east-1 | 159 | 0% | 2.0 | 2 (09-24 19:03Z) |
| us-east-2 | 159 | 1% | 1.9 | 1 (09-24 19:03Z) |
| us-west-2 | 159 | 0% | 1.7 | 2 (09-24 19:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333999999
ap-northeast-1   222211222211122122332231232211212213322223322222
ap-northeast-2   333333333333333333333333333333333333333333999999
ap-south-1       112211133331131211333333333321111111111111111111
ap-southeast-2   111111111111111111111111111111131111111111111111
ap-southeast-3   133333131311233333333333133331333133333333996899
us-east-1        311212322312311121311223333333313212232322221232
us-east-2        313133333331331133331233333313311112113113192911
us-west-2        111111312213111233333333333333312112222132221122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 49 | 0% | 1.4 | 1 (09-24 19:03Z) |
| ap-east-1 ape1-az2 | 101 | 6% | 2.8 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 73 | 0% | 2.2 | 1 (09-24 19:03Z) |
| ap-northeast-2 apne2-az1 | 142 | 4% | 3.2 | 9 (09-24 19:03Z) |
| ap-northeast-2 apne2-az3 | 141 | 4% | 3.2 | 9 (09-24 19:03Z) |
| ap-northeast-2 apne2-az4 | 156 | 4% | 3.2 | 9 (09-24 19:03Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 36 | 0% | 1.0 | 1 (09-24 19:03Z) |
| ap-southeast-3 apse3-az3 | 124 | 5% | 3.2 | 9 (09-24 19:03Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 54 | 0% | 1.3 | 1 (09-23 20:14Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 49 | 0% | 1.5 | 1 (09-24 19:03Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 52 | 2% | 1.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 67 | 1% | 2.0 | 1 (09-24 19:03Z) |
| us-east-2 use2-az3 | 87 | 2% | 2.4 | 1 (09-24 14:57Z) |
| us-west-2 usw2-az1 | 47 | 0% | 2.1 | 1 (09-23 20:14Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 159 | 4% | 3.2 | 9 (09-24 19:03Z) |
| ap-northeast-1 | 159 | 79% | 7.6 | 9 (09-24 19:03Z) |
| ap-northeast-2 | 159 | 100% | 9.0 | 9 (09-24 19:03Z) |
| ap-south-1 | 159 | 47% | 5.7 | 9 (09-24 19:03Z) |
| ap-southeast-2 | 159 | 8% | 2.7 | 9 (09-24 19:03Z) |
| ap-southeast-3 | 159 | 4% | 2.8 | 9 (09-24 19:03Z) |
| us-east-1 | 159 | 75% | 6.9 | 4 (09-24 19:03Z) |
| us-east-2 | 159 | 75% | 7.3 | 3 (09-24 19:03Z) |
| us-west-2 | 159 | 55% | 5.8 | 4 (09-24 19:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333999999
ap-northeast-1   499941999933999999999999999999999999999999993499
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       929999399992399999999999999999199924999839999289
ap-southeast-2   233222332222332333333333333322331222222233512299
ap-southeast-3   133333131311233333333333133331333133333333996899
us-east-1        939559956999945499999999999999949994459996669954
us-east-2        999999999999991199991999999999933995999999499923
us-west-2        344139944595334599999999999999943195454995559554
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 4 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 58 | 7% | 3.4 | 9 (09-24 14:57Z) |
| ap-east-1 ape1-az2 | 44 | 7% | 3.4 | 9 (09-24 09:55Z) |
| ap-east-1 ape1-az3 | 49 | 10% | 3.6 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az1 | 86 | 91% | 8.4 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az2 | 29 | 10% | 3.6 | 9 (09-24 19:03Z) |
| ap-northeast-1 apne1-az4 | 108 | 100% | 9.0 | 9 (09-24 19:03Z) |
| ap-northeast-2 apne2-az1 | 143 | 100% | 9.0 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az2 | 17 | 24% | 4.4 | 9 (09-24 19:03Z) |
| ap-northeast-2 apne2-az3 | 145 | 100% | 9.0 | 9 (09-24 19:03Z) |
| ap-northeast-2 apne2-az4 | 53 | 11% | 3.7 | 9 (09-24 19:03Z) |
| ap-south-1 aps1-az1 | 51 | 57% | 6.4 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az2 | 39 | 8% | 3.5 | 9 (09-24 19:03Z) |
| ap-south-1 aps1-az3 | 68 | 74% | 7.4 | 9 (09-24 04:37Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 14 | 14% | 3.9 | 9 (09-24 19:03Z) |
| ap-southeast-3 apse3-az3 | 43 | 7% | 3.4 | 9 (09-24 19:03Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 63 | 100% | 9.0 | 9 (09-24 04:37Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 83 | 90% | 8.3 | 9 (09-24 09:55Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727500 | 2026-09-24T19:03:28Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.869900 | 2026-09-24T19:03:28Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.845600 | 2026-09-24T19:03:28Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.028600 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591600 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578700 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568500 | 2026-09-24T19:03:28Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-24T19:03:28Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.492200 | 2026-09-24T19:03:28Z |
| ap-south-1 | ap-south-1a | Windows | 0.332900 | 2026-09-24T19:03:28Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.472800 | 2026-09-24T19:03:28Z |
| ap-south-1 | ap-south-1b | Windows | 0.307000 | 2026-09-24T19:03:28Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.640700 | 2026-09-24T19:03:28Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.518500 | 2026-09-24T19:03:28Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.756500 | 2026-09-24T19:03:28Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.737000 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1a | Windows | 0.333800 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.552300 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1b | Windows | 0.290900 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.436400 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.432400 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1d | Windows | 0.287900 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.429500 | 2026-09-24T19:03:28Z |
| us-east-1 | us-east-1f | Windows | 0.295000 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524100 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2a | Windows | 0.641300 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.525000 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.511600 | 2026-09-24T19:03:28Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.518100 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2a | Windows | 0.333400 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.485200 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2b | Windows | 0.332900 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-24T19:03:28Z |
| us-west-2 | us-west-2c | Windows | 0.332400 | 2026-09-24T19:03:28Z |
