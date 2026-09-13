# Spot placement score log

Generated 2026-09-13 22:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 100 | 0% | 1.5 | 3 (09-13 22:21Z) |
| ap-northeast-1 | 100 | 0% | 1.9 | 3 (09-13 22:21Z) |
| ap-northeast-2 | 100 | 0% | 3.0 | 3 (09-13 22:21Z) |
| ap-south-1 | 100 | 0% | 2.0 | 3 (09-13 22:21Z) |
| ap-southeast-2 | 100 | 0% | 1.0 | 1 (09-13 22:21Z) |
| ap-southeast-3 | 100 | 0% | 2.6 | 3 (09-13 22:21Z) |
| us-east-1 | 100 | 0% | 2.0 | 3 (09-13 22:21Z) |
| us-east-2 | 100 | 0% | 1.6 | 3 (09-13 22:21Z) |
| us-west-2 | 100 | 0% | 1.5 | 3 (09-13 22:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111133333333333333333333333
ap-northeast-1   333122111122211232222221123221123323333333333333
ap-northeast-2   333333333333333333333333233333333333333333333333
ap-south-1       311121111311122111111111211313121111333333313333
ap-southeast-2   111111111111111111111111111111111311111111111111
ap-southeast-3   333333313333212333113133113333333333333333333333
us-east-1        232323332322333321133221221131131133223311323233
us-east-2        133111131113333113333111311111131311333333333333
us-west-2        111111111213311111111111111111111111133313313333
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
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 46 | 0% | 1.9 | 3 (09-13 22:21Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 55 | 0% | 2.3 | 3 (09-13 22:21Z) |
| ap-northeast-2 apne2-az1 | 94 | 0% | 2.9 | 3 (09-13 19:23Z) |
| ap-northeast-2 apne2-az3 | 90 | 0% | 2.9 | 3 (09-13 19:23Z) |
| ap-northeast-2 apne2-az4 | 97 | 0% | 3.0 | 3 (09-13 22:21Z) |
| ap-south-1 aps1-az1 | 42 | 0% | 1.6 | 3 (09-13 22:21Z) |
| ap-south-1 aps1-az3 | 56 | 0% | 2.6 | 3 (09-13 22:21Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 81 | 0% | 2.9 | 3 (09-13 22:21Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 27 | 0% | 1.1 | 3 (09-13 19:23Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 29 | 0% | 1.3 | 3 (09-13 19:23Z) |
| us-east-1 use1-az6 | 39 | 0% | 1.2 | 3 (09-13 19:23Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 43 | 0% | 1.8 | 3 (09-13 22:21Z) |
| us-east-2 use2-az3 | 48 | 0% | 2.2 | 3 (09-13 22:21Z) |
| us-west-2 usw2-az1 | 25 | 0% | 1.9 | 3 (09-13 19:23Z) |
| us-west-2 usw2-az2 | 19 | 0% | 1.7 | 3 (09-13 22:21Z) |
| us-west-2 usw2-az3 | 52 | 0% | 1.5 | 3 (09-13 22:21Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 100 | 0% | 3.0 | 3 (09-13 22:21Z) |
| ap-northeast-1 | 100 | 78% | 7.5 | 9 (09-13 22:21Z) |
| ap-northeast-2 | 100 | 100% | 9.0 | 9 (09-13 22:21Z) |
| ap-south-1 | 100 | 26% | 4.4 | 9 (09-13 22:21Z) |
| ap-southeast-2 | 100 | 10% | 2.7 | 2 (09-13 22:21Z) |
| ap-southeast-3 | 100 | 0% | 2.6 | 3 (09-13 22:21Z) |
| us-east-1 | 100 | 75% | 6.8 | 9 (09-13 22:21Z) |
| us-east-2 | 100 | 72% | 7.0 | 9 (09-13 22:21Z) |
| us-west-2 | 100 | 50% | 5.6 | 9 (09-13 22:21Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999912999439999339992249992349999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333999922999513339939999999999999999
ap-southeast-2   333333111311113311113322222311233333333333322332
ap-southeast-3   333333313333212333113133113333333333333333333333
us-east-1        999999999999995445994456993299992349999999999999
us-east-2        999999999999999999999199992333991919999999999999
us-west-2        969999719999999442951332313323423353999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 4 | · | 3 | 3 | 6 | 4 | 2 | 3 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 9 | 6 | 4 | 7 | 5 | 5 | 7 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 6 | 5 | 5 | 5 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 50 | 84% | 8.0 | 9 (09-13 22:21Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 70 | 100% | 9.0 | 9 (09-13 22:21Z) |
| ap-northeast-2 apne2-az1 | 91 | 100% | 9.0 | 9 (09-13 22:21Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 90 | 100% | 9.0 | 9 (09-13 06:01Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 31 | 45% | 5.7 | 9 (09-13 22:21Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 41 | 100% | 9.0 | 9 (09-13 22:21Z) |
| us-east-1 use1-az4 | 43 | 98% | 8.8 | 9 (09-13 22:21Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 43 | 100% | 9.0 | 9 (09-13 22:21Z) |
| us-east-2 use2-az1 | 38 | 100% | 9.0 | 9 (09-13 16:09Z) |
| us-east-2 use2-az2 | 65 | 97% | 8.8 | 9 (09-13 22:21Z) |
| us-east-2 use2-az3 | 41 | 80% | 7.7 | 9 (09-13 11:41Z) |
| us-west-2 usw2-az1 | 38 | 97% | 8.8 | 9 (09-13 22:21Z) |
| us-west-2 usw2-az2 | 23 | 96% | 8.8 | 9 (09-13 19:23Z) |
| us-west-2 usw2-az3 | 38 | 97% | 8.8 | 9 (09-13 22:21Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727100 | 2026-09-13T22:21:36Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-13T22:21:36Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790500 | 2026-09-13T22:21:36Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.975500 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592900 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580400 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567900 | 2026-09-13T22:21:36Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741300 | 2026-09-13T22:21:36Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.551500 | 2026-09-13T22:21:36Z |
| ap-south-1 | ap-south-1a | Windows | 0.313800 | 2026-09-13T22:21:36Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.506900 | 2026-09-13T22:21:36Z |
| ap-south-1 | ap-south-1b | Windows | 0.323800 | 2026-09-13T22:21:36Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.722100 | 2026-09-13T22:21:36Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508200 | 2026-09-13T22:21:36Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.818600 | 2026-09-13T22:21:36Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.472400 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.885000 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1a | Windows | 0.353900 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.689600 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1b | Windows | 0.336300 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.603300 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1c | Windows | 0.312500 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.560900 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1d | Windows | 0.323800 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.611000 | 2026-09-13T22:21:36Z |
| us-east-1 | us-east-1f | Windows | 0.332600 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534200 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2a | Windows | 0.642800 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.532700 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2b | Windows | 0.637500 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.524100 | 2026-09-13T22:21:36Z |
| us-east-2 | us-east-2c | Windows | 0.638300 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.591600 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2a | Windows | 0.337400 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.563800 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2b | Windows | 0.340300 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.541400 | 2026-09-13T22:21:36Z |
| us-west-2 | us-west-2c | Windows | 0.343400 | 2026-09-13T22:21:36Z |
