# Spot placement score log

Generated 2026-09-13 00:54 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 95 | 0% | 1.4 | 3 (09-13 00:53Z) |
| ap-northeast-1 | 95 | 0% | 1.9 | 3 (09-13 00:53Z) |
| ap-northeast-2 | 95 | 0% | 2.9 | 3 (09-13 00:53Z) |
| ap-south-1 | 95 | 0% | 2.0 | 3 (09-13 00:53Z) |
| ap-southeast-2 | 95 | 0% | 1.0 | 1 (09-13 00:53Z) |
| ap-southeast-3 | 95 | 0% | 2.5 | 3 (09-13 00:53Z) |
| us-east-1 | 95 | 0% | 1.9 | 3 (09-13 00:53Z) |
| us-east-2 | 95 | 0% | 1.6 | 3 (09-13 00:53Z) |
| us-west-2 | 95 | 0% | 1.4 | 3 (09-13 00:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111333333333333333333
ap-northeast-1   311333331221111222112322222211232211233233333333
ap-northeast-2   333333333333333333333333333332333333333333333333
ap-south-1       323333111211113111221111111112113131211113333333
ap-southeast-2   111111111111111111111111111111111111113111111111
ap-southeast-3   331133333333133332123331131331133333333333333333
us-east-1        233332323233323223333211332212211311311332233113
us-east-2        311111331111311133331133331113111111313113333333
us-west-2        111111111111112133111111111111111111111111333133
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 43 | 0% | 1.8 | 3 (09-12 22:12Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 51 | 0% | 2.3 | 3 (09-13 00:53Z) |
| ap-northeast-2 apne2-az1 | 90 | 0% | 2.9 | 3 (09-13 00:53Z) |
| ap-northeast-2 apne2-az3 | 86 | 0% | 2.9 | 3 (09-13 00:53Z) |
| ap-northeast-2 apne2-az4 | 93 | 0% | 3.0 | 3 (09-13 00:53Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 53 | 0% | 2.6 | 3 (09-12 22:12Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 76 | 0% | 2.9 | 3 (09-13 00:53Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 30 | 0% | 1.5 | 3 (09-13 00:53Z) |
| us-east-2 use2-az2 | 41 | 0% | 1.8 | 3 (09-13 00:53Z) |
| us-east-2 use2-az3 | 43 | 0% | 2.1 | 3 (09-13 00:53Z) |
| us-west-2 usw2-az1 | 22 | 0% | 1.7 | 3 (09-13 00:53Z) |
| us-west-2 usw2-az2 | 16 | 0% | 1.5 | 3 (09-13 00:53Z) |
| us-west-2 usw2-az3 | 49 | 0% | 1.4 | 3 (09-12 22:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 95 | 0% | 3.0 | 3 (09-13 00:53Z) |
| ap-northeast-1 | 95 | 77% | 7.4 | 9 (09-13 00:53Z) |
| ap-northeast-2 | 95 | 100% | 9.0 | 9 (09-13 00:53Z) |
| ap-south-1 | 95 | 22% | 4.1 | 9 (09-13 00:53Z) |
| ap-southeast-2 | 95 | 11% | 2.7 | 3 (09-13 00:53Z) |
| ap-southeast-3 | 95 | 0% | 2.5 | 3 (09-13 00:53Z) |
| us-east-1 | 95 | 74% | 6.7 | 9 (09-13 00:53Z) |
| us-east-2 | 95 | 71% | 6.9 | 9 (09-13 00:53Z) |
| us-west-2 | 95 | 47% | 5.4 | 9 (09-13 00:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999129994399993399922499923499999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333339999229995133399399999999999
ap-southeast-2   333333333331113111133111133222223112333333333333
ap-southeast-3   331133333333133332123331131331133333333333333333
us-east-1        959999999999999999954459944569932999923499999999
us-east-2        999999999999999999999999991999923339919199999999
us-west-2        998589699997199999994429513323133234233539999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 1 | · | 9 | 3 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 1 | · | 3 | 3 | 6 | 2 | 2 | 3 | 3 | 3 | 4 | 6 | 5 | 5 | 3 | 4 | 5 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 6 | 4 | 6 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 46 | 83% | 7.9 | 9 (09-13 00:53Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 66 | 100% | 9.0 | 9 (09-13 00:53Z) |
| ap-northeast-2 apne2-az1 | 87 | 100% | 9.0 | 9 (09-13 00:53Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 89 | 100% | 9.0 | 9 (09-12 22:12Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 27 | 37% | 5.2 | 9 (09-13 00:53Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 9 | 100% | 8.7 | 9 (09-13 00:53Z) |
| us-east-1 use1-az2 | 36 | 100% | 9.0 | 9 (09-13 00:53Z) |
| us-east-1 use1-az4 | 40 | 98% | 8.8 | 9 (09-13 00:53Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 40 | 100% | 9.0 | 9 (09-12 22:12Z) |
| us-east-2 use2-az1 | 36 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az2 | 60 | 97% | 8.8 | 9 (09-13 00:53Z) |
| us-east-2 use2-az3 | 39 | 79% | 7.6 | 9 (09-12 22:12Z) |
| us-west-2 usw2-az1 | 33 | 97% | 8.8 | 9 (09-13 00:53Z) |
| us-west-2 usw2-az2 | 21 | 95% | 8.8 | 9 (09-12 22:12Z) |
| us-west-2 usw2-az3 | 33 | 97% | 8.8 | 9 (09-13 00:53Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.734400 | 2026-09-13T00:53:55Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-13T00:53:55Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.787300 | 2026-09-13T00:53:55Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.970300 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593700 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581000 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569100 | 2026-09-13T00:53:55Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-09-13T00:53:55Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.534600 | 2026-09-13T00:53:55Z |
| ap-south-1 | ap-south-1a | Windows | 0.317100 | 2026-09-13T00:53:55Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.488200 | 2026-09-13T00:53:55Z |
| ap-south-1 | ap-south-1b | Windows | 0.323900 | 2026-09-13T00:53:55Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746500 | 2026-09-13T00:53:55Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509100 | 2026-09-13T00:53:55Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.810200 | 2026-09-13T00:53:55Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.444100 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.888800 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1a | Windows | 0.356700 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.702100 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1b | Windows | 0.334400 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.607200 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1c | Windows | 0.315300 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.557400 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1d | Windows | 0.325500 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.614900 | 2026-09-13T00:53:55Z |
| us-east-1 | us-east-1f | Windows | 0.326800 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542800 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536200 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2b | Windows | 0.637600 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526400 | 2026-09-13T00:53:55Z |
| us-east-2 | us-east-2c | Windows | 0.638400 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.582900 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2a | Windows | 0.331900 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562900 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2b | Windows | 0.336200 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544300 | 2026-09-13T00:53:55Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-13T00:53:55Z |
