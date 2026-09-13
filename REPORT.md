# Spot placement score log

Generated 2026-09-13 06:01 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 96 | 0% | 1.4 | 3 (09-13 06:01Z) |
| ap-northeast-1 | 96 | 0% | 1.9 | 3 (09-13 06:01Z) |
| ap-northeast-2 | 96 | 0% | 2.9 | 3 (09-13 06:01Z) |
| ap-south-1 | 96 | 0% | 2.0 | 1 (09-13 06:01Z) |
| ap-southeast-2 | 96 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-southeast-3 | 96 | 0% | 2.6 | 3 (09-13 06:01Z) |
| us-east-1 | 96 | 0% | 1.9 | 2 (09-13 06:01Z) |
| us-east-2 | 96 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-west-2 | 96 | 0% | 1.4 | 1 (09-13 06:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111113333333333333333333
ap-northeast-1   113333312211112221123222222112322112332333333333
ap-northeast-2   333333333333333333333333333323333333333333333333
ap-south-1       233331112111131112211111111121131312111133333331
ap-southeast-2   111111111111111111111111111111111111131111111111
ap-southeast-3   311333333331333321233311313311333333333333333333
us-east-1        333323232333232233332113322122113113113322331132
us-east-2        111113311113111333311333311131111113131133333333
us-west-2        111111111111121331111111111111111111111113331331
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 44 | 0% | 1.8 | 3 (09-13 06:01Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 52 | 0% | 2.3 | 3 (09-13 06:01Z) |
| ap-northeast-2 apne2-az1 | 91 | 0% | 2.9 | 3 (09-13 06:01Z) |
| ap-northeast-2 apne2-az3 | 87 | 0% | 2.9 | 3 (09-13 06:01Z) |
| ap-northeast-2 apne2-az4 | 94 | 0% | 3.0 | 3 (09-13 06:01Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 53 | 0% | 2.6 | 3 (09-12 22:12Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 77 | 0% | 2.9 | 3 (09-13 06:01Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 42 | 0% | 1.8 | 3 (09-13 06:01Z) |
| us-east-2 use2-az3 | 44 | 0% | 2.2 | 3 (09-13 06:01Z) |
| us-west-2 usw2-az1 | 22 | 0% | 1.7 | 3 (09-13 00:53Z) |
| us-west-2 usw2-az2 | 16 | 0% | 1.5 | 3 (09-13 00:53Z) |
| us-west-2 usw2-az3 | 49 | 0% | 1.4 | 3 (09-12 22:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 96 | 0% | 3.0 | 3 (09-13 06:01Z) |
| ap-northeast-1 | 96 | 77% | 7.4 | 9 (09-13 06:01Z) |
| ap-northeast-2 | 96 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-south-1 | 96 | 23% | 4.2 | 9 (09-13 06:01Z) |
| ap-southeast-2 | 96 | 10% | 2.7 | 2 (09-13 06:01Z) |
| ap-southeast-3 | 96 | 0% | 2.6 | 3 (09-13 06:01Z) |
| us-east-1 | 96 | 74% | 6.7 | 9 (09-13 06:01Z) |
| us-east-2 | 96 | 71% | 6.9 | 9 (09-13 06:01Z) |
| us-west-2 | 96 | 48% | 5.5 | 9 (09-13 06:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999991299943999933999224999234999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333399992299951333993999999999999
ap-southeast-2   333333333311131111331111332222231123333333333332
ap-southeast-3   311333333331333321233311313311333333333333333333
us-east-1        599999999999999999544599445699329999234999999999
us-east-2        999999999999999999999999919999233399191999999999
us-west-2        985896999971999999944295133231332342335399999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 4 | · | 3 | 3 | 6 | 2 | 2 | 3 | 3 | 3 | 4 | 6 | 5 | 5 | 3 | 4 | 5 | 3 |
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
| ap-northeast-2 apne2-az1 | 88 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 90 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 27 | 37% | 5.2 | 9 (09-13 00:53Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 9 | 100% | 8.7 | 9 (09-13 00:53Z) |
| us-east-1 use1-az2 | 37 | 100% | 9.0 | 9 (09-13 06:01Z) |
| us-east-1 use1-az4 | 40 | 98% | 8.8 | 9 (09-13 00:53Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 41 | 100% | 9.0 | 9 (09-13 06:01Z) |
| us-east-2 use2-az1 | 37 | 100% | 9.0 | 9 (09-13 06:01Z) |
| us-east-2 use2-az2 | 61 | 97% | 8.8 | 9 (09-13 06:01Z) |
| us-east-2 use2-az3 | 40 | 80% | 7.7 | 9 (09-13 06:01Z) |
| us-west-2 usw2-az1 | 34 | 97% | 8.8 | 9 (09-13 06:01Z) |
| us-west-2 usw2-az2 | 22 | 95% | 8.8 | 9 (09-13 06:01Z) |
| us-west-2 usw2-az3 | 34 | 97% | 8.8 | 9 (09-13 06:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.732100 | 2026-09-13T06:01:09Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-13T06:01:09Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.787300 | 2026-09-13T06:01:09Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.968200 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593500 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580900 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568800 | 2026-09-13T06:01:09Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741000 | 2026-09-13T06:01:09Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.547600 | 2026-09-13T06:01:09Z |
| ap-south-1 | ap-south-1a | Windows | 0.316400 | 2026-09-13T06:01:09Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.491500 | 2026-09-13T06:01:09Z |
| ap-south-1 | ap-south-1b | Windows | 0.323400 | 2026-09-13T06:01:09Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746500 | 2026-09-13T06:01:09Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.505800 | 2026-09-13T06:01:09Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.812600 | 2026-09-13T06:01:09Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.452300 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.888800 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1a | Windows | 0.358500 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.700600 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1b | Windows | 0.334700 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.599900 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1c | Windows | 0.313700 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.561100 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1d | Windows | 0.324700 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.613400 | 2026-09-13T06:01:09Z |
| us-east-1 | us-east-1f | Windows | 0.326800 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542600 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536300 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2b | Windows | 0.637600 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526800 | 2026-09-13T06:01:09Z |
| us-east-2 | us-east-2c | Windows | 0.638500 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.582900 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2a | Windows | 0.331900 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562600 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2b | Windows | 0.337400 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544100 | 2026-09-13T06:01:09Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-13T06:01:09Z |
