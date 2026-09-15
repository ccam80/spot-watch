# Spot placement score log

Generated 2026-09-15 18:07 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 109 | 0% | 1.6 | 3 (09-15 18:07Z) |
| ap-northeast-1 | 109 | 0% | 2.0 | 2 (09-15 18:07Z) |
| ap-northeast-2 | 109 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-south-1 | 109 | 0% | 2.1 | 1 (09-15 18:07Z) |
| ap-southeast-2 | 109 | 0% | 1.0 | 1 (09-15 18:07Z) |
| ap-southeast-3 | 109 | 0% | 2.5 | 1 (09-15 18:07Z) |
| us-east-1 | 109 | 0% | 2.0 | 2 (09-15 18:07Z) |
| us-east-2 | 109 | 0% | 1.6 | 1 (09-15 18:07Z) |
| us-west-2 | 109 | 0% | 1.5 | 1 (09-15 18:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111133333333333333333333333333333333
ap-northeast-1   122211232222221123221123323333333333333223321132
ap-northeast-2   333333333333333233333333333333333333333333333333
ap-south-1       311122111111111211313121111333333313333333331111
ap-southeast-2   111111111111111111111111311111111111111111111111
ap-southeast-3   333212333113133113333333333333333333333313133131
us-east-1        322333321133221221131131133223311323233222222122
us-east-2        113333113333111311111131311333333333333333111111
us-west-2        213311111111111111111111111133313313333333111211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 30 | 0% | 1.0 | 1 (09-15 18:07Z) |
| ap-east-1 ape1-az2 | 54 | 0% | 2.0 | 3 (09-15 18:07Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 59 | 0% | 2.3 | 3 (09-15 13:28Z) |
| ap-northeast-2 apne2-az1 | 102 | 0% | 2.9 | 3 (09-15 18:07Z) |
| ap-northeast-2 apne2-az3 | 98 | 0% | 2.9 | 3 (09-15 13:28Z) |
| ap-northeast-2 apne2-az4 | 106 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-south-1 aps1-az1 | 46 | 0% | 1.7 | 1 (09-15 18:07Z) |
| ap-south-1 aps1-az3 | 61 | 0% | 2.6 | 3 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 21 | 0% | 1.1 | 1 (09-15 01:24Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 19 | 0% | 1.0 | 1 (09-15 18:07Z) |
| ap-southeast-3 apse3-az3 | 85 | 0% | 2.9 | 3 (09-15 13:28Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 31 | 0% | 1.1 | 1 (09-15 18:07Z) |
| us-east-1 use1-az4 | 18 | 0% | 1.2 | 1 (09-15 13:28Z) |
| us-east-1 use1-az5 | 31 | 0% | 1.3 | 1 (09-15 18:07Z) |
| us-east-1 use1-az6 | 43 | 0% | 1.2 | 1 (09-15 18:07Z) |
| us-east-2 use2-az1 | 33 | 0% | 1.5 | 1 (09-15 13:28Z) |
| us-east-2 use2-az2 | 47 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-east-2 use2-az3 | 53 | 0% | 2.2 | 1 (09-15 18:07Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 23 | 0% | 1.8 | 1 (09-15 13:28Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 109 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-northeast-1 | 109 | 77% | 7.4 | 9 (09-15 18:07Z) |
| ap-northeast-2 | 109 | 100% | 9.0 | 9 (09-15 18:07Z) |
| ap-south-1 | 109 | 31% | 4.7 | 9 (09-15 18:07Z) |
| ap-southeast-2 | 109 | 9% | 2.7 | 2 (09-15 18:07Z) |
| ap-southeast-3 | 109 | 0% | 2.5 | 1 (09-15 18:07Z) |
| us-east-1 | 109 | 72% | 6.7 | 3 (09-15 18:07Z) |
| us-east-2 | 109 | 73% | 7.1 | 2 (09-15 18:07Z) |
| us-west-2 | 109 | 50% | 5.6 | 3 (09-15 18:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999439999339992249992349999999999999999649993399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333999922999513339939999999999999999999999189
ap-southeast-2   311113311113322222311233333333333322332222222222
ap-southeast-3   333212333113133113333333333333333333333313133131
us-east-1        999995445994456993299992349999999999999994368443
us-east-2        999999999999199992333991919999999999999999999992
us-west-2        999999442951332313323423353999999999999999342543
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 7 | · | 1 | 4 | 5 | 4 | 3 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 7 | · | 3 | 4 | 8 | 5 | 1 | 3 | 3 | 6 | 4 | 2 | 7 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | 4 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 4 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | 5 | 6 | 5 | 9 | 6 | 9 | 7 | 7 | 9 | 6 | 6 | 4 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-east-1 ape1-az2 | 33 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-east-1 ape1-az3 | 36 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az1 | 55 | 85% | 8.1 | 9 (09-15 18:07Z) |
| ap-northeast-1 apne1-az2 | 21 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az4 | 75 | 100% | 9.0 | 9 (09-15 18:07Z) |
| ap-northeast-2 apne2-az1 | 100 | 100% | 9.0 | 9 (09-15 18:07Z) |
| ap-northeast-2 apne2-az2 | 11 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-northeast-2 apne2-az3 | 99 | 100% | 9.0 | 9 (09-15 18:07Z) |
| ap-northeast-2 apne2-az4 | 38 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-south-1 aps1-az1 | 24 | 8% | 3.5 | 9 (09-15 18:07Z) |
| ap-south-1 aps1-az2 | 30 | 0% | 3.0 | 3 (09-15 18:07Z) |
| ap-south-1 aps1-az3 | 38 | 55% | 6.3 | 9 (09-15 18:07Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 32 | 0% | 3.0 | 3 (09-15 13:28Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 45 | 96% | 8.7 | 2 (09-15 07:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 41 | 100% | 9.0 | 9 (09-15 07:38Z) |
| us-east-2 use2-az2 | 72 | 97% | 8.8 | 9 (09-15 07:38Z) |
| us-east-2 use2-az3 | 48 | 83% | 7.9 | 9 (09-15 13:28Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722000 | 2026-09-15T18:07:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-15T18:07:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.798000 | 2026-09-15T18:07:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.981000 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590900 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579500 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566300 | 2026-09-15T18:07:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741700 | 2026-09-15T18:07:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.590500 | 2026-09-15T18:07:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.329100 | 2026-09-15T18:07:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.495700 | 2026-09-15T18:07:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.320100 | 2026-09-15T18:07:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.692800 | 2026-09-15T18:07:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503600 | 2026-09-15T18:07:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.875400 | 2026-09-15T18:07:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.492100 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.879400 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1a | Windows | 0.343300 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.673200 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1b | Windows | 0.332200 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.586900 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1c | Windows | 0.308400 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.549000 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1d | Windows | 0.317900 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.565500 | 2026-09-15T18:07:50Z |
| us-east-1 | us-east-1f | Windows | 0.326500 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527500 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2a | Windows | 0.640500 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529100 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2b | Windows | 0.637200 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.518600 | 2026-09-15T18:07:50Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.569700 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2a | Windows | 0.345300 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.541500 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2b | Windows | 0.339900 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.538100 | 2026-09-15T18:07:50Z |
| us-west-2 | us-west-2c | Windows | 0.340900 | 2026-09-15T18:07:50Z |
