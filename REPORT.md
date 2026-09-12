# Spot placement score log

Generated 2026-09-12 22:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 94 | 0% | 1.4 | 3 (09-12 22:12Z) |
| ap-northeast-1 | 94 | 0% | 1.9 | 3 (09-12 22:12Z) |
| ap-northeast-2 | 94 | 0% | 2.9 | 3 (09-12 22:12Z) |
| ap-south-1 | 94 | 0% | 2.0 | 3 (09-12 22:12Z) |
| ap-southeast-2 | 94 | 0% | 1.0 | 1 (09-12 22:12Z) |
| ap-southeast-3 | 94 | 0% | 2.5 | 3 (09-12 22:12Z) |
| us-east-1 | 94 | 0% | 1.9 | 1 (09-12 22:12Z) |
| us-east-2 | 94 | 0% | 1.6 | 3 (09-12 22:12Z) |
| us-west-2 | 94 | 0% | 1.4 | 3 (09-12 22:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111133333333333333333
ap-northeast-1   331133333122111122211232222221123221123323333333
ap-northeast-2   333333333333333333333333333333233333333333333333
ap-south-1       332333311121111311122111111111211313121111333333
ap-southeast-2   111111111111111111111111111111111111111311111111
ap-southeast-3   333113333333313333212333113133113333333333333333
us-east-1        323333232323332322333321133221221131131133223311
us-east-2        131111133111131113333113333111311111131311333333
us-west-2        211111111111111213311111111111111111111111133313
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 43 | 0% | 1.8 | 3 (09-12 22:12Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 50 | 0% | 2.2 | 3 (09-12 22:12Z) |
| ap-northeast-2 apne2-az1 | 89 | 0% | 2.9 | 3 (09-12 22:12Z) |
| ap-northeast-2 apne2-az3 | 85 | 0% | 2.9 | 3 (09-12 22:12Z) |
| ap-northeast-2 apne2-az4 | 92 | 0% | 3.0 | 3 (09-12 22:12Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 53 | 0% | 2.6 | 3 (09-12 22:12Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 75 | 0% | 2.9 | 3 (09-12 19:13Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 29 | 0% | 1.5 | 3 (09-12 22:12Z) |
| us-east-2 use2-az2 | 40 | 0% | 1.7 | 3 (09-12 22:12Z) |
| us-east-2 use2-az3 | 42 | 0% | 2.1 | 3 (09-12 19:13Z) |
| us-west-2 usw2-az1 | 21 | 0% | 1.7 | 3 (09-12 22:12Z) |
| us-west-2 usw2-az2 | 15 | 0% | 1.4 | 3 (09-12 10:38Z) |
| us-west-2 usw2-az3 | 49 | 0% | 1.4 | 3 (09-12 22:12Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 94 | 0% | 3.0 | 3 (09-12 22:12Z) |
| ap-northeast-1 | 94 | 77% | 7.4 | 9 (09-12 22:12Z) |
| ap-northeast-2 | 94 | 100% | 9.0 | 9 (09-12 22:12Z) |
| ap-south-1 | 94 | 21% | 4.1 | 9 (09-12 22:12Z) |
| ap-southeast-2 | 94 | 11% | 2.7 | 3 (09-12 22:12Z) |
| ap-southeast-3 | 94 | 0% | 2.5 | 3 (09-12 22:12Z) |
| us-east-1 | 94 | 73% | 6.7 | 9 (09-12 22:12Z) |
| us-east-2 | 94 | 70% | 6.9 | 9 (09-12 22:12Z) |
| us-west-2 | 94 | 47% | 5.4 | 9 (09-12 22:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999912999439999339992249992349999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333333999922999513339939999999999
ap-southeast-2   333333333333111311113311113322222311233333333333
ap-southeast-3   333113333333313333212333113133113333333333333333
us-east-1        995999999999999999995445994456993299992349999999
us-east-2        999999999999999999999999999199992333991919999999
us-west-2        499858969999719999999442951332313323423353999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 4 | 5 | 1 | · | 9 | 3 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 8 | 1 | · | 3 | 3 | 6 | 2 | 2 | 3 | 3 | 3 | 4 | 6 | 5 | 5 | 3 | 4 | 5 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 2 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 6 | 4 | 6 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 4 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 45 | 82% | 7.9 | 9 (09-12 19:13Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 65 | 100% | 9.0 | 9 (09-12 17:02Z) |
| ap-northeast-2 apne2-az1 | 86 | 100% | 9.0 | 9 (09-12 22:12Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 89 | 100% | 9.0 | 9 (09-12 22:12Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 26 | 35% | 5.1 | 9 (09-12 19:13Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 8 | 100% | 8.6 | 9 (09-12 19:13Z) |
| us-east-1 use1-az2 | 35 | 100% | 9.0 | 9 (09-12 22:12Z) |
| us-east-1 use1-az4 | 39 | 97% | 8.8 | 9 (09-12 22:12Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 40 | 100% | 9.0 | 9 (09-12 22:12Z) |
| us-east-2 use2-az1 | 36 | 100% | 9.0 | 9 (09-12 05:42Z) |
| us-east-2 use2-az2 | 59 | 97% | 8.7 | 9 (09-12 22:12Z) |
| us-east-2 use2-az3 | 39 | 79% | 7.6 | 9 (09-12 22:12Z) |
| us-west-2 usw2-az1 | 32 | 97% | 8.8 | 9 (09-12 22:12Z) |
| us-west-2 usw2-az2 | 21 | 95% | 8.8 | 9 (09-12 22:12Z) |
| us-west-2 usw2-az3 | 32 | 97% | 8.8 | 9 (09-12 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.734400 | 2026-09-12T22:12:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-12T22:12:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.786300 | 2026-09-12T22:12:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.970300 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593700 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581000 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569200 | 2026-09-12T22:12:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-09-12T22:12:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.534600 | 2026-09-12T22:12:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.317200 | 2026-09-12T22:12:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.488200 | 2026-09-12T22:12:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.323900 | 2026-09-12T22:12:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746600 | 2026-09-12T22:12:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509100 | 2026-09-12T22:12:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.810200 | 2026-09-12T22:12:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.444100 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.892800 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1a | Windows | 0.356700 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.702100 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1b | Windows | 0.334400 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.607200 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1c | Windows | 0.315300 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.557400 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1d | Windows | 0.325500 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.614900 | 2026-09-12T22:12:14Z |
| us-east-1 | us-east-1f | Windows | 0.325600 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542800 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536200 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2b | Windows | 0.637600 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526400 | 2026-09-12T22:12:14Z |
| us-east-2 | us-east-2c | Windows | 0.638400 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.582900 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2a | Windows | 0.330000 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.562900 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2b | Windows | 0.336200 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544300 | 2026-09-12T22:12:14Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-12T22:12:14Z |
