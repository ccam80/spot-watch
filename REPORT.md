# Spot placement score log

Generated 2026-09-13 11:42 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 97 | 0% | 1.4 | 3 (09-13 11:41Z) |
| ap-northeast-1 | 97 | 0% | 1.9 | 3 (09-13 11:41Z) |
| ap-northeast-2 | 97 | 0% | 2.9 | 3 (09-13 11:41Z) |
| ap-south-1 | 97 | 0% | 2.0 | 3 (09-13 11:41Z) |
| ap-southeast-2 | 97 | 0% | 1.0 | 1 (09-13 11:41Z) |
| ap-southeast-3 | 97 | 0% | 2.6 | 3 (09-13 11:41Z) |
| us-east-1 | 97 | 0% | 1.9 | 3 (09-13 11:41Z) |
| us-east-2 | 97 | 0% | 1.6 | 3 (09-13 11:41Z) |
| us-west-2 | 97 | 0% | 1.5 | 3 (09-13 11:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111133333333333333333333
ap-northeast-1   133333122111122211232222221123221123323333333333
ap-northeast-2   333333333333333333333333333233333333333333333333
ap-south-1       333311121111311122111111111211313121111333333313
ap-southeast-2   111111111111111111111111111111111111311111111111
ap-southeast-3   113333333313333212333113133113333333333333333333
us-east-1        333232323332322333321133221221131131133223311323
us-east-2        111133111131113333113333111311111131311333333333
us-west-2        111111111111213311111111111111111111111133313313
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
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 44 | 0% | 1.8 | 3 (09-13 06:01Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 53 | 0% | 2.3 | 3 (09-13 11:41Z) |
| ap-northeast-2 apne2-az1 | 92 | 0% | 2.9 | 3 (09-13 11:41Z) |
| ap-northeast-2 apne2-az3 | 88 | 0% | 2.9 | 3 (09-13 11:41Z) |
| ap-northeast-2 apne2-az4 | 95 | 0% | 3.0 | 3 (09-13 11:41Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 54 | 0% | 2.6 | 3 (09-13 11:41Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 78 | 0% | 2.9 | 3 (09-13 11:41Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 42 | 0% | 1.8 | 3 (09-13 06:01Z) |
| us-east-2 use2-az3 | 45 | 0% | 2.2 | 3 (09-13 11:41Z) |
| us-west-2 usw2-az1 | 23 | 0% | 1.8 | 3 (09-13 11:41Z) |
| us-west-2 usw2-az2 | 17 | 0% | 1.6 | 3 (09-13 11:41Z) |
| us-west-2 usw2-az3 | 50 | 0% | 1.4 | 3 (09-13 11:41Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 97 | 0% | 3.0 | 3 (09-13 11:41Z) |
| ap-northeast-1 | 97 | 77% | 7.4 | 9 (09-13 11:41Z) |
| ap-northeast-2 | 97 | 100% | 9.0 | 9 (09-13 11:41Z) |
| ap-south-1 | 97 | 24% | 4.2 | 9 (09-13 11:41Z) |
| ap-southeast-2 | 97 | 10% | 2.7 | 2 (09-13 11:41Z) |
| ap-southeast-3 | 97 | 0% | 2.6 | 3 (09-13 11:41Z) |
| us-east-1 | 97 | 74% | 6.7 | 9 (09-13 11:41Z) |
| us-east-2 | 97 | 71% | 7.0 | 9 (09-13 11:41Z) |
| us-west-2 | 97 | 48% | 5.5 | 9 (09-13 11:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999912999439999339992249992349999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333999922999513339939999999999999
ap-southeast-2   333333333111311113311113322222311233333333333322
ap-southeast-3   113333333313333212333113133113333333333333333333
us-east-1        999999999999999995445994456993299992349999999999
us-east-2        999999999999999999999999199992333991919999999999
us-west-2        858969999719999999442951332313323423353999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 4 | · | 3 | 3 | 6 | 4 | 2 | 3 | 3 | 3 | 4 | 6 | 5 | 5 | 3 | 4 | 5 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 9 | 6 | 4 | 6 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 47 | 83% | 8.0 | 9 (09-13 11:41Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 67 | 100% | 9.0 | 9 (09-13 11:41Z) |
| ap-northeast-2 apne2-az1 | 88 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 90 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 28 | 39% | 5.4 | 9 (09-13 11:41Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 38 | 100% | 9.0 | 9 (09-13 11:41Z) |
| us-east-1 use1-az4 | 41 | 98% | 8.8 | 9 (09-13 11:41Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 41 | 100% | 9.0 | 9 (09-13 06:01Z) |
| us-east-2 use2-az1 | 37 | 100% | 9.0 | 9 (09-13 06:01Z) |
| us-east-2 use2-az2 | 62 | 97% | 8.8 | 9 (09-13 11:41Z) |
| us-east-2 use2-az3 | 41 | 80% | 7.7 | 9 (09-13 11:41Z) |
| us-west-2 usw2-az1 | 35 | 97% | 8.8 | 9 (09-13 11:41Z) |
| us-west-2 usw2-az2 | 22 | 95% | 8.8 | 9 (09-13 06:01Z) |
| us-west-2 usw2-az3 | 35 | 97% | 8.8 | 9 (09-13 11:41Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.732100 | 2026-09-13T11:41:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-13T11:41:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.786600 | 2026-09-13T11:41:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.966200 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593400 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580900 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568700 | 2026-09-13T11:41:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-09-13T11:41:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548800 | 2026-09-13T11:41:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.315300 | 2026-09-13T11:41:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.499000 | 2026-09-13T11:41:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.323500 | 2026-09-13T11:41:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.738200 | 2026-09-13T11:41:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.505800 | 2026-09-13T11:41:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.813300 | 2026-09-13T11:41:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.453500 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.885400 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1a | Windows | 0.357600 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.698400 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1b | Windows | 0.337100 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.602000 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1c | Windows | 0.313700 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.559700 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1d | Windows | 0.324600 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.610800 | 2026-09-13T11:41:54Z |
| us-east-1 | us-east-1f | Windows | 0.329000 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.539700 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.535100 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2b | Windows | 0.637500 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526600 | 2026-09-13T11:41:54Z |
| us-east-2 | us-east-2c | Windows | 0.638500 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.587600 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2a | Windows | 0.333600 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562600 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2b | Windows | 0.337400 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.543900 | 2026-09-13T11:41:54Z |
| us-west-2 | us-west-2c | Windows | 0.343600 | 2026-09-13T11:41:54Z |
