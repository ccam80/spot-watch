# Spot placement score log

Generated 2026-09-10 22:29 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 81 | 0% | 1.1 | 3 (09-10 22:29Z) |
| ap-northeast-1 | 81 | 0% | 1.8 | 2 (09-10 22:29Z) |
| ap-northeast-2 | 81 | 0% | 2.9 | 3 (09-10 22:29Z) |
| ap-south-1 | 81 | 0% | 2.0 | 1 (09-10 22:29Z) |
| ap-southeast-2 | 81 | 0% | 1.0 | 1 (09-10 22:29Z) |
| ap-southeast-3 | 81 | 0% | 2.5 | 3 (09-10 22:29Z) |
| us-east-1 | 81 | 0% | 1.9 | 3 (09-10 22:29Z) |
| us-east-2 | 81 | 0% | 1.4 | 1 (09-10 22:29Z) |
| us-west-2 | 81 | 0% | 1.4 | 1 (09-10 22:29Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111113333
ap-northeast-1   111122113113333113333312211112221123222222112322
ap-northeast-2   333333333333333333333333333333333333333333323333
ap-south-1       221133322333333233331112111131112211111111121131
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   313131313333333311333333331333321233311313311333
us-east-1        122123332113132333323232333232233332113322122113
us-east-2        111111111111113111113311113111333311333311131111
us-west-2        111222222222221111111111111121331111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 1 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 2 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 3 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 1 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 1 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 3 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 30 | 0% | 1.3 | 3 (09-10 22:29Z) |
| ap-northeast-1 apne1-az1 | 16 | 0% | 1.1 | 1 (09-10 00:07Z) |
| ap-northeast-1 apne1-az4 | 41 | 0% | 2.1 | 3 (09-10 16:19Z) |
| ap-northeast-2 apne2-az1 | 76 | 0% | 2.9 | 3 (09-10 22:29Z) |
| ap-northeast-2 apne2-az3 | 73 | 0% | 2.9 | 3 (09-10 22:29Z) |
| ap-northeast-2 apne2-az4 | 79 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-south-1 aps1-az1 | 35 | 0% | 1.6 | 1 (09-10 22:29Z) |
| ap-south-1 aps1-az3 | 46 | 0% | 2.5 | 3 (09-10 19:35Z) |
| ap-southeast-2 apse2-az1 | 18 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-southeast-2 apse2-az2 | 14 | 0% | 1.0 | 1 (09-09 09:37Z) |
| ap-southeast-3 apse3-az1 | 15 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 64 | 0% | 2.8 | 3 (09-10 22:29Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 25 | 0% | 1.1 | 1 (09-10 22:29Z) |
| us-east-1 use1-az4 | 14 | 0% | 1.3 | 1 (09-09 18:30Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 36 | 0% | 1.2 | 3 (09-10 22:29Z) |
| us-east-2 use2-az1 | 21 | 0% | 1.3 | 1 (09-10 19:35Z) |
| us-east-2 use2-az2 | 33 | 0% | 1.6 | 1 (09-10 19:35Z) |
| us-east-2 use2-az3 | 36 | 0% | 2.0 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az1 | 18 | 0% | 1.4 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az2 | 13 | 0% | 1.3 | 1 (09-10 05:53Z) |
| us-west-2 usw2-az3 | 40 | 0% | 1.3 | 1 (09-10 22:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 81 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-northeast-1 | 81 | 77% | 7.3 | 9 (09-10 22:29Z) |
| ap-northeast-2 | 81 | 100% | 9.0 | 9 (09-10 22:29Z) |
| ap-south-1 | 81 | 10% | 3.4 | 3 (09-10 22:29Z) |
| ap-southeast-2 | 81 | 12% | 2.7 | 1 (09-10 22:29Z) |
| ap-southeast-3 | 81 | 0% | 2.5 | 3 (09-10 22:29Z) |
| us-east-1 | 81 | 73% | 6.5 | 9 (09-10 22:29Z) |
| us-east-2 | 81 | 69% | 6.8 | 3 (09-10 22:29Z) |
| us-west-2 | 81 | 46% | 5.3 | 2 (09-10 22:29Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   219999129999999999999999991299943999933999224999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       322333333333333333333333333333333399992299951333
ap-southeast-2   113331113313333333333333311131111331111332222231
ap-southeast-3   313131313333333311333333331333321233311313311333
us-east-1        994335654256599599999999999999999544599445699329
us-east-2        993332393382999999999999999999999999999919999233
us-west-2        429443445345449985896999971999999944295133231332
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 2 | 1 | · | 9 | 3 | 2 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 5 | 3 | · | 3 | 4 | 5 | 1 | · | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 1 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 5 | 1 | 2 | 5 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 1 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 5 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 8 | 1 | 5 | 7 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 1 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 9 | 4 | 7 | 6 | 7 | 4 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 3 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 2 | 5 | 5 | 5 | 5 | 2 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 35 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-east-1 ape1-az2 | 28 | 0% | 3.0 | 3 (09-10 19:35Z) |
| ap-east-1 ape1-az3 | 27 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-northeast-1 apne1-az1 | 36 | 78% | 7.6 | 9 (09-10 22:29Z) |
| ap-northeast-1 apne1-az2 | 18 | 0% | 3.0 | 3 (09-09 21:39Z) |
| ap-northeast-1 apne1-az4 | 58 | 100% | 9.0 | 9 (09-10 22:29Z) |
| ap-northeast-2 apne2-az1 | 77 | 100% | 9.0 | 9 (09-10 22:29Z) |
| ap-northeast-2 apne2-az2 | 8 | 0% | 3.0 | 3 (09-10 19:35Z) |
| ap-northeast-2 apne2-az3 | 77 | 100% | 9.0 | 9 (09-10 22:29Z) |
| ap-northeast-2 apne2-az4 | 32 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-south-1 aps1-az1 | 18 | 0% | 3.0 | 3 (09-10 19:35Z) |
| ap-south-1 aps1-az2 | 26 | 0% | 3.0 | 3 (09-10 22:29Z) |
| ap-south-1 aps1-az3 | 17 | 6% | 3.4 | 3 (09-10 16:19Z) |
| ap-southeast-2 apse2-az1 | 9 | 33% | 4.8 | 3 (09-09 18:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 10 | 0% | 3.0 | 3 (09-10 19:35Z) |
| ap-southeast-3 apse3-az3 | 26 | 0% | 3.0 | 3 (09-10 22:29Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 29 | 100% | 9.0 | 9 (09-10 05:53Z) |
| us-east-1 use1-az4 | 31 | 97% | 8.8 | 2 (09-10 11:10Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 34 | 100% | 9.0 | 9 (09-10 22:29Z) |
| us-east-2 use2-az1 | 32 | 100% | 9.0 | 9 (09-10 11:10Z) |
| us-east-2 use2-az2 | 51 | 96% | 8.7 | 9 (09-10 11:10Z) |
| us-east-2 use2-az3 | 32 | 75% | 7.3 | 9 (09-10 11:10Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.743700 | 2026-09-10T22:29:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.841300 | 2026-09-10T22:29:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783500 | 2026-09-10T22:29:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.961000 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596200 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582600 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572800 | 2026-09-10T22:29:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-10T22:29:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.539800 | 2026-09-10T22:29:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.321300 | 2026-09-10T22:29:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.496800 | 2026-09-10T22:29:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.326200 | 2026-09-10T22:29:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.753700 | 2026-09-10T22:29:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.505400 | 2026-09-10T22:29:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.857700 | 2026-09-10T22:29:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.420500 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.903800 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1a | Windows | 0.359300 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.720200 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1b | Windows | 0.321700 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.606300 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1c | Windows | 0.319500 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.538300 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1d | Windows | 0.324200 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.588600 | 2026-09-10T22:29:46Z |
| us-east-1 | us-east-1f | Windows | 0.320300 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.547900 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2a | Windows | 0.643200 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.539600 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.531300 | 2026-09-10T22:29:46Z |
| us-east-2 | us-east-2c | Windows | 0.638300 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.585100 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2a | Windows | 0.315800 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.554300 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2b | Windows | 0.324800 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535100 | 2026-09-10T22:29:46Z |
| us-west-2 | us-west-2c | Windows | 0.343100 | 2026-09-10T22:29:46Z |
