# Spot placement score log

Generated 2026-09-14 23:05 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 105 | 0% | 1.5 | 3 (09-14 23:05Z) |
| ap-northeast-1 | 105 | 0% | 2.0 | 2 (09-14 23:05Z) |
| ap-northeast-2 | 105 | 0% | 3.0 | 3 (09-14 23:05Z) |
| ap-south-1 | 105 | 0% | 2.1 | 3 (09-14 23:05Z) |
| ap-southeast-2 | 105 | 0% | 1.0 | 1 (09-14 23:05Z) |
| ap-southeast-3 | 105 | 0% | 2.6 | 3 (09-14 23:05Z) |
| us-east-1 | 105 | 0% | 2.0 | 2 (09-14 23:05Z) |
| us-east-2 | 105 | 0% | 1.7 | 1 (09-14 23:05Z) |
| us-west-2 | 105 | 0% | 1.5 | 1 (09-14 23:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111113333333333333333333333333333
ap-northeast-1   211112221123222222112322112332333333333333322332
ap-northeast-2   333333333333333333323333333333333333333333333333
ap-south-1       111131112211111111121131312111133333331333333333
ap-southeast-2   111111111111111111111111111131111111111111111111
ap-southeast-3   331333321233311313311333333333333333333333331313
us-east-1        333232233332113322122113113113322331132323322222
us-east-2        113111333311333311131111113131133333333333333311
us-west-2        111121331111111111111111111111113331331333333311
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 50 | 0% | 2.0 | 3 (09-14 23:05Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 58 | 0% | 2.3 | 1 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 99 | 0% | 2.9 | 3 (09-14 23:05Z) |
| ap-northeast-2 apne2-az3 | 95 | 0% | 2.9 | 3 (09-14 23:05Z) |
| ap-northeast-2 apne2-az4 | 102 | 0% | 3.0 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az1 | 45 | 0% | 1.7 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az3 | 61 | 0% | 2.6 | 3 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 17 | 0% | 1.0 | 1 (09-14 23:05Z) |
| ap-southeast-3 apse3-az3 | 83 | 0% | 2.9 | 3 (09-14 23:05Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 29 | 0% | 1.1 | 1 (09-14 23:05Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 29 | 0% | 1.3 | 3 (09-13 19:23Z) |
| us-east-1 use1-az6 | 39 | 0% | 1.2 | 3 (09-13 19:23Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 46 | 0% | 1.8 | 1 (09-14 19:16Z) |
| us-east-2 use2-az3 | 51 | 0% | 2.3 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 21 | 0% | 1.9 | 3 (09-14 06:08Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 105 | 0% | 3.0 | 3 (09-14 23:05Z) |
| ap-northeast-1 | 105 | 78% | 7.5 | 9 (09-14 23:05Z) |
| ap-northeast-2 | 105 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-south-1 | 105 | 30% | 4.6 | 9 (09-14 23:05Z) |
| ap-southeast-2 | 105 | 10% | 2.7 | 2 (09-14 23:05Z) |
| ap-southeast-3 | 105 | 0% | 2.6 | 3 (09-14 23:05Z) |
| us-east-1 | 105 | 74% | 6.8 | 6 (09-14 23:05Z) |
| us-east-2 | 105 | 73% | 7.1 | 9 (09-14 23:05Z) |
| us-west-2 | 105 | 50% | 5.7 | 4 (09-14 23:05Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   991299943999933999224999234999999999999999964999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333399992299951333993999999999999999999999
ap-southeast-2   311131111331111332222231123333333333332233222222
ap-southeast-3   331333321233311313311333333333333333333333331313
us-east-1        999999999544599445699329999234999999999999999436
us-east-2        999999999999999919999233399191999999999999999999
us-west-2        971999999944295133231332342335399999999999999934
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 6 | · | 3 | 4 | 8 | 5 | · | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 6 | · | 1 | 2 | 2 | 2 | · | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 32 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-east-1 ape1-az3 | 33 | 0% | 3.0 | 3 (09-14 23:05Z) |
| ap-northeast-1 apne1-az1 | 53 | 85% | 8.1 | 9 (09-14 23:05Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 73 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 96 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-northeast-2 apne2-az2 | 10 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 95 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-northeast-2 apne2-az4 | 35 | 0% | 3.0 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az1 | 22 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 36 | 53% | 6.2 | 9 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 30 | 0% | 3.0 | 3 (09-14 23:05Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 44 | 98% | 8.8 | 9 (09-14 00:58Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 40 | 100% | 9.0 | 9 (09-14 13:55Z) |
| us-east-2 use2-az2 | 70 | 97% | 8.8 | 9 (09-14 23:05Z) |
| us-east-2 use2-az3 | 46 | 83% | 7.8 | 9 (09-14 23:05Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725900 | 2026-09-14T23:05:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-14T23:05:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.796900 | 2026-09-14T23:05:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.977900 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591700 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580000 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567200 | 2026-09-14T23:05:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741500 | 2026-09-14T23:05:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.595800 | 2026-09-14T23:05:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.331200 | 2026-09-14T23:05:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.510200 | 2026-09-14T23:05:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.321700 | 2026-09-14T23:05:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700800 | 2026-09-14T23:05:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509400 | 2026-09-14T23:05:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.857900 | 2026-09-14T23:05:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.481700 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.880200 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1a | Windows | 0.346400 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.673600 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1b | Windows | 0.330100 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.588400 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1c | Windows | 0.310500 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.534600 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1d | Windows | 0.318700 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.580700 | 2026-09-14T23:05:14Z |
| us-east-1 | us-east-1f | Windows | 0.329900 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529400 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531100 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2b | Windows | 0.637200 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.520500 | 2026-09-14T23:05:14Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579900 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2a | Windows | 0.347500 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.551900 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2b | Windows | 0.340900 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547000 | 2026-09-14T23:05:14Z |
| us-west-2 | us-west-2c | Windows | 0.342000 | 2026-09-14T23:05:14Z |
