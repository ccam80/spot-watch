# Spot placement score log

Generated 2026-09-15 01:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 106 | 0% | 1.5 | 3 (09-15 01:24Z) |
| ap-northeast-1 | 106 | 0% | 2.0 | 1 (09-15 01:24Z) |
| ap-northeast-2 | 106 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-south-1 | 106 | 0% | 2.1 | 1 (09-15 01:24Z) |
| ap-southeast-2 | 106 | 0% | 1.0 | 1 (09-15 01:24Z) |
| ap-southeast-3 | 106 | 0% | 2.6 | 3 (09-15 01:24Z) |
| us-east-1 | 106 | 0% | 2.0 | 2 (09-15 01:24Z) |
| us-east-2 | 106 | 0% | 1.7 | 1 (09-15 01:24Z) |
| us-west-2 | 106 | 0% | 1.5 | 1 (09-15 01:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111133333333333333333333333333333
ap-northeast-1   111122211232222221123221123323333333333333223321
ap-northeast-2   333333333333333333233333333333333333333333333333
ap-south-1       111311122111111111211313121111333333313333333331
ap-southeast-2   111111111111111111111111111311111111111111111111
ap-southeast-3   313333212333113133113333333333333333333333313133
us-east-1        332322333321133221221131131133223311323233222222
us-east-2        131113333113333111311111131311333333333333333111
us-west-2        111213311111111111111111111111133313313333333111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 51 | 0% | 2.0 | 3 (09-15 01:24Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 58 | 0% | 2.3 | 1 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 99 | 0% | 2.9 | 3 (09-14 23:05Z) |
| ap-northeast-2 apne2-az3 | 96 | 0% | 2.9 | 1 (09-15 01:24Z) |
| ap-northeast-2 apne2-az4 | 103 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-south-1 aps1-az1 | 45 | 0% | 1.7 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az3 | 61 | 0% | 2.6 | 3 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 21 | 0% | 1.1 | 1 (09-15 01:24Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 17 | 0% | 1.0 | 1 (09-14 23:05Z) |
| ap-southeast-3 apse3-az3 | 84 | 0% | 2.9 | 3 (09-15 01:24Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 29 | 0% | 1.1 | 1 (09-14 23:05Z) |
| us-east-1 use1-az4 | 17 | 0% | 1.2 | 1 (09-15 01:24Z) |
| us-east-1 use1-az5 | 29 | 0% | 1.3 | 3 (09-13 19:23Z) |
| us-east-1 use1-az6 | 40 | 0% | 1.2 | 1 (09-15 01:24Z) |
| us-east-2 use2-az1 | 32 | 0% | 1.6 | 1 (09-15 01:24Z) |
| us-east-2 use2-az2 | 47 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-east-2 use2-az3 | 51 | 0% | 2.3 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 22 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 106 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-northeast-1 | 106 | 77% | 7.4 | 3 (09-15 01:24Z) |
| ap-northeast-2 | 106 | 100% | 9.0 | 9 (09-15 01:24Z) |
| ap-south-1 | 106 | 30% | 4.6 | 9 (09-15 01:24Z) |
| ap-southeast-2 | 106 | 9% | 2.7 | 2 (09-15 01:24Z) |
| ap-southeast-3 | 106 | 0% | 2.6 | 3 (09-15 01:24Z) |
| us-east-1 | 106 | 75% | 6.8 | 8 (09-15 01:24Z) |
| us-east-2 | 106 | 74% | 7.1 | 9 (09-15 01:24Z) |
| us-west-2 | 106 | 50% | 5.6 | 2 (09-15 01:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   912999439999339992249992349999999999999999649993
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333999922999513339939999999999999999999999
ap-southeast-2   111311113311113322222311233333333333322332222222
ap-southeast-3   313333212333113133113333333333333333333333313133
us-east-1        999999995445994456993299992349999999999999994368
us-east-2        999999999999999199992333991919999999999999999999
us-west-2        719999999442951332313323423353999999999999999342
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 7 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 7 | · | 3 | 4 | 8 | 5 | · | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | · | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 40 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-east-1 ape1-az2 | 32 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-east-1 ape1-az3 | 34 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-northeast-1 apne1-az1 | 53 | 85% | 8.1 | 9 (09-14 23:05Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 73 | 100% | 9.0 | 9 (09-14 23:05Z) |
| ap-northeast-2 apne2-az1 | 97 | 100% | 9.0 | 9 (09-15 01:24Z) |
| ap-northeast-2 apne2-az2 | 10 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 96 | 100% | 9.0 | 9 (09-15 01:24Z) |
| ap-northeast-2 apne2-az4 | 36 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-south-1 aps1-az1 | 23 | 4% | 3.3 | 9 (09-15 01:24Z) |
| ap-south-1 aps1-az2 | 28 | 0% | 3.0 | 3 (09-15 01:24Z) |
| ap-south-1 aps1-az3 | 37 | 54% | 6.2 | 9 (09-15 01:24Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 31 | 0% | 3.0 | 3 (09-15 01:24Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 44 | 98% | 8.8 | 9 (09-14 00:58Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 40 | 100% | 9.0 | 9 (09-14 13:55Z) |
| us-east-2 use2-az2 | 71 | 97% | 8.8 | 9 (09-15 01:24Z) |
| us-east-2 use2-az3 | 46 | 83% | 7.8 | 9 (09-14 23:05Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725900 | 2026-09-15T01:24:06Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-15T01:24:06Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.797800 | 2026-09-15T01:24:06Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.977900 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591700 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580000 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567200 | 2026-09-15T01:24:06Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741600 | 2026-09-15T01:24:06Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.595800 | 2026-09-15T01:24:06Z |
| ap-south-1 | ap-south-1a | Windows | 0.331200 | 2026-09-15T01:24:06Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.502200 | 2026-09-15T01:24:06Z |
| ap-south-1 | ap-south-1b | Windows | 0.320100 | 2026-09-15T01:24:06Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.694500 | 2026-09-15T01:24:06Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507300 | 2026-09-15T01:24:06Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.857900 | 2026-09-15T01:24:06Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.481700 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.880200 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1a | Windows | 0.344300 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.670900 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1b | Windows | 0.329300 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.588400 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1c | Windows | 0.308800 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.534500 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1d | Windows | 0.318700 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.580700 | 2026-09-15T01:24:06Z |
| us-east-1 | us-east-1f | Windows | 0.329600 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529400 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531100 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2b | Windows | 0.637200 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.520500 | 2026-09-15T01:24:06Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.579500 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2a | Windows | 0.347500 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.551900 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2b | Windows | 0.340900 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.546000 | 2026-09-15T01:24:06Z |
| us-west-2 | us-west-2c | Windows | 0.342000 | 2026-09-15T01:24:06Z |
