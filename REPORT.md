# Spot placement score log

Generated 2026-09-12 17:02 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 92 | 0% | 1.3 | 3 (09-12 17:02Z) |
| ap-northeast-1 | 92 | 0% | 1.8 | 3 (09-12 17:02Z) |
| ap-northeast-2 | 92 | 0% | 2.9 | 3 (09-12 17:02Z) |
| ap-south-1 | 92 | 0% | 2.0 | 3 (09-12 17:02Z) |
| ap-southeast-2 | 92 | 0% | 1.0 | 1 (09-12 17:02Z) |
| ap-southeast-3 | 92 | 0% | 2.5 | 3 (09-12 17:02Z) |
| us-east-1 | 92 | 0% | 1.9 | 3 (09-12 17:02Z) |
| us-east-2 | 92 | 0% | 1.5 | 3 (09-12 17:02Z) |
| us-west-2 | 92 | 0% | 1.4 | 3 (09-12 17:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111333333333333333
ap-northeast-1   333311333331221111222112322222211232211233233333
ap-northeast-2   333333333333333333333333333333332333333333333333
ap-south-1       333323333111211113111221111111112113131211113333
ap-southeast-2   111111111111111111111111111111111111111113111111
ap-southeast-3   333331133333333133332123331131331133333333333333
us-east-1        313233332323233323223333211332212211311311332233
us-east-2        111311111331111311133331133331113111111313113333
us-west-2        222111111111111112133111111111111111111111111333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 41 | 0% | 1.7 | 3 (09-12 17:02Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 48 | 0% | 2.2 | 3 (09-12 17:02Z) |
| ap-northeast-2 apne2-az1 | 87 | 0% | 2.9 | 3 (09-12 17:02Z) |
| ap-northeast-2 apne2-az3 | 83 | 0% | 2.9 | 3 (09-12 17:02Z) |
| ap-northeast-2 apne2-az4 | 90 | 0% | 3.0 | 3 (09-12 17:02Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 51 | 0% | 2.5 | 3 (09-12 17:02Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 74 | 0% | 2.9 | 3 (09-12 17:02Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 15 | 0% | 1.3 | 1 (09-11 22:30Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 28 | 0% | 1.4 | 3 (09-12 14:02Z) |
| us-east-2 use2-az2 | 38 | 0% | 1.7 | 3 (09-12 14:02Z) |
| us-east-2 use2-az3 | 41 | 0% | 2.1 | 3 (09-12 17:02Z) |
| us-west-2 usw2-az1 | 20 | 0% | 1.6 | 3 (09-12 17:02Z) |
| us-west-2 usw2-az2 | 15 | 0% | 1.4 | 3 (09-12 10:38Z) |
| us-west-2 usw2-az3 | 48 | 0% | 1.4 | 3 (09-12 17:02Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 92 | 0% | 3.0 | 3 (09-12 17:02Z) |
| ap-northeast-1 | 92 | 76% | 7.3 | 9 (09-12 17:02Z) |
| ap-northeast-2 | 92 | 100% | 9.0 | 9 (09-12 17:02Z) |
| ap-south-1 | 92 | 20% | 4.0 | 9 (09-12 17:02Z) |
| ap-southeast-2 | 92 | 11% | 2.7 | 3 (09-12 17:02Z) |
| ap-southeast-3 | 92 | 0% | 2.5 | 3 (09-12 17:02Z) |
| us-east-1 | 92 | 73% | 6.6 | 9 (09-12 17:02Z) |
| us-east-2 | 92 | 70% | 6.8 | 9 (09-12 17:02Z) |
| us-west-2 | 92 | 46% | 5.3 | 9 (09-12 17:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999129994399993399922499923499999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333333339999229995133399399999999
ap-southeast-2   333333333333331113111133111133222223112333333333
ap-southeast-3   333331133333333133332123331131331133333333333333
us-east-1        659959999999999999999954459944569932999923499999
us-east-2        299999999999999999999999999991999923339919199999
us-west-2        544998589699997199999994429513323133234233539999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 4 | 5 | 1 | · | 9 | 3 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 1 | · | 3 | 3 | 6 | 2 | 2 | 3 | 3 | 3 | 4 | 6 | 5 | 4 | 3 | 4 | 4 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 5 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 6 | 4 | 6 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 3 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 6 | 5 | 4 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 44 | 82% | 7.9 | 9 (09-12 17:02Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 65 | 100% | 9.0 | 9 (09-12 17:02Z) |
| ap-northeast-2 apne2-az1 | 85 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 87 | 100% | 9.0 | 9 (09-12 14:02Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 25 | 32% | 4.9 | 9 (09-12 17:02Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 7 | 100% | 8.6 | 9 (09-12 17:02Z) |
| us-east-1 use1-az2 | 33 | 100% | 9.0 | 9 (09-12 17:02Z) |
| us-east-1 use1-az4 | 37 | 97% | 8.8 | 9 (09-12 17:02Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 39 | 100% | 9.0 | 9 (09-12 14:02Z) |
| us-east-2 use2-az1 | 36 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az2 | 57 | 96% | 8.7 | 9 (09-12 17:02Z) |
| us-east-2 use2-az3 | 38 | 79% | 7.6 | 9 (09-12 17:02Z) |
| us-west-2 usw2-az1 | 30 | 97% | 8.8 | 9 (09-12 17:02Z) |
| us-west-2 usw2-az2 | 19 | 95% | 8.7 | 9 (09-12 10:38Z) |
| us-west-2 usw2-az3 | 30 | 97% | 8.8 | 9 (09-12 17:02Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.736400 | 2026-09-12T17:02:30Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-12T17:02:30Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.786300 | 2026-09-12T17:02:30Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.972200 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593800 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581100 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569200 | 2026-09-12T17:02:30Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-12T17:02:30Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.535100 | 2026-09-12T17:02:30Z |
| ap-south-1 | ap-south-1a | Windows | 0.319400 | 2026-09-12T17:02:30Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.490200 | 2026-09-12T17:02:30Z |
| ap-south-1 | ap-south-1b | Windows | 0.324000 | 2026-09-12T17:02:30Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.749400 | 2026-09-12T17:02:30Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504300 | 2026-09-12T17:02:30Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.817100 | 2026-09-12T17:02:30Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.439300 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.892800 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1a | Windows | 0.356700 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.705200 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1b | Windows | 0.332600 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.607800 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1c | Windows | 0.315700 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.557400 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1d | Windows | 0.324900 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.608700 | 2026-09-12T17:02:30Z |
| us-east-1 | us-east-1f | Windows | 0.324700 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.543200 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536200 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2b | Windows | 0.637500 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526400 | 2026-09-12T17:02:30Z |
| us-east-2 | us-east-2c | Windows | 0.638400 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.584100 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2a | Windows | 0.328400 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562400 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2b | Windows | 0.334700 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.545400 | 2026-09-12T17:02:30Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-12T17:02:30Z |
