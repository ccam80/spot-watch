# Spot placement score log

Generated 2026-09-12 10:38 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 90 | 0% | 1.3 | 3 (09-12 10:38Z) |
| ap-northeast-1 | 90 | 0% | 1.8 | 3 (09-12 10:38Z) |
| ap-northeast-2 | 90 | 0% | 2.9 | 3 (09-12 10:38Z) |
| ap-south-1 | 90 | 0% | 2.0 | 3 (09-12 10:38Z) |
| ap-southeast-2 | 90 | 0% | 1.0 | 1 (09-12 10:38Z) |
| ap-southeast-3 | 90 | 0% | 2.5 | 3 (09-12 10:38Z) |
| us-east-1 | 90 | 0% | 1.9 | 2 (09-12 10:38Z) |
| us-east-2 | 90 | 0% | 1.5 | 3 (09-12 10:38Z) |
| us-west-2 | 90 | 0% | 1.4 | 3 (09-12 10:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111113333333333333
ap-northeast-1   113333113333312211112221123222222112322112332333
ap-northeast-2   333333333333333333333333333333333323333333333333
ap-south-1       333333233331112111131112211111111121131312111133
ap-southeast-2   111111111111111111111111111111111111111111131111
ap-southeast-3   333333311333333331333321233311313311333333333333
us-east-1        113132333323232333232233332113322122113113113322
us-east-2        111113111113311113111333311333311131111113131133
us-west-2        222221111111111111121331111111111111111111111113
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 39 | 0% | 1.7 | 3 (09-12 10:38Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 46 | 0% | 2.2 | 3 (09-12 10:38Z) |
| ap-northeast-2 apne2-az1 | 85 | 0% | 2.9 | 3 (09-12 10:38Z) |
| ap-northeast-2 apne2-az3 | 81 | 0% | 2.9 | 3 (09-12 05:42Z) |
| ap-northeast-2 apne2-az4 | 88 | 0% | 3.0 | 3 (09-12 10:38Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 49 | 0% | 2.5 | 3 (09-12 10:38Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 73 | 0% | 2.9 | 3 (09-12 10:38Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 15 | 0% | 1.3 | 1 (09-11 22:30Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 27 | 0% | 1.4 | 3 (09-12 10:38Z) |
| us-east-2 use2-az2 | 37 | 0% | 1.6 | 3 (09-12 05:42Z) |
| us-east-2 use2-az3 | 40 | 0% | 2.1 | 3 (09-12 10:38Z) |
| us-west-2 usw2-az1 | 18 | 0% | 1.4 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az2 | 15 | 0% | 1.4 | 3 (09-12 10:38Z) |
| us-west-2 usw2-az3 | 46 | 0% | 1.3 | 3 (09-12 10:38Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 90 | 0% | 3.0 | 3 (09-12 10:38Z) |
| ap-northeast-1 | 90 | 76% | 7.3 | 9 (09-12 10:38Z) |
| ap-northeast-2 | 90 | 100% | 9.0 | 9 (09-12 10:38Z) |
| ap-south-1 | 90 | 18% | 3.9 | 9 (09-12 10:38Z) |
| ap-southeast-2 | 90 | 11% | 2.7 | 3 (09-12 10:38Z) |
| ap-southeast-3 | 90 | 0% | 2.5 | 3 (09-12 10:38Z) |
| us-east-1 | 90 | 72% | 6.6 | 9 (09-12 10:38Z) |
| us-east-2 | 90 | 69% | 6.8 | 9 (09-12 10:38Z) |
| us-west-2 | 90 | 44% | 5.2 | 9 (09-12 10:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999999991299943999933999224999234999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333333333399992299951333993999999
ap-southeast-2   313333333333333311131111331111332222231123333333
ap-southeast-3   333333311333333331333321233311313311333333333333
us-east-1        256599599999999999999999544599445699329999234999
us-east-2        382999999999999999999999999999919999233399191999
us-west-2        345449985896999971999999944295133231332342335399
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 4 | 5 | 1 | · | 9 | 3 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 1 | · | 3 | 3 | 6 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 5 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 6 | 1 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 3 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 2 | 5 | 4 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 42 | 81% | 7.8 | 9 (09-12 10:38Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 63 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az1 | 85 | 100% | 9.0 | 9 (09-12 05:42Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 86 | 100% | 9.0 | 9 (09-12 10:38Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 23 | 26% | 4.6 | 9 (09-12 10:38Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 5 | 100% | 8.4 | 9 (09-12 10:38Z) |
| us-east-1 use1-az2 | 32 | 100% | 9.0 | 9 (09-12 10:38Z) |
| us-east-1 use1-az4 | 35 | 97% | 8.8 | 9 (09-12 10:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 38 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az1 | 36 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az2 | 55 | 96% | 8.7 | 9 (09-12 10:38Z) |
| us-east-2 use2-az3 | 37 | 78% | 7.6 | 9 (09-12 05:42Z) |
| us-west-2 usw2-az1 | 28 | 96% | 8.8 | 9 (09-12 10:38Z) |
| us-west-2 usw2-az2 | 19 | 95% | 8.7 | 9 (09-12 10:38Z) |
| us-west-2 usw2-az3 | 28 | 96% | 8.8 | 9 (09-12 10:38Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.737700 | 2026-09-12T10:38:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-12T10:38:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.789300 | 2026-09-12T10:38:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.972200 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594100 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581300 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569700 | 2026-09-12T10:38:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-12T10:38:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.539600 | 2026-09-12T10:38:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.319700 | 2026-09-12T10:38:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.492900 | 2026-09-12T10:38:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.324400 | 2026-09-12T10:38:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.749400 | 2026-09-12T10:38:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502500 | 2026-09-12T10:38:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.830100 | 2026-09-12T10:38:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.435700 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.897800 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1a | Windows | 0.358500 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.705600 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1b | Windows | 0.329800 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.606600 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1c | Windows | 0.315700 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.539800 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1d | Windows | 0.322000 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.599700 | 2026-09-12T10:38:46Z |
| us-east-1 | us-east-1f | Windows | 0.321300 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.544200 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2a | Windows | 0.643800 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536400 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526800 | 2026-09-12T10:38:46Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.584500 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2a | Windows | 0.327800 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562700 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2b | Windows | 0.334500 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548400 | 2026-09-12T10:38:46Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-12T10:38:46Z |
