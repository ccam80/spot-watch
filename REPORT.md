# Spot placement score log

Generated 2026-09-16 07:37 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 112 | 0% | 1.6 | 3 (09-16 07:37Z) |
| ap-northeast-1 | 112 | 0% | 1.9 | 2 (09-16 07:37Z) |
| ap-northeast-2 | 112 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-south-1 | 112 | 0% | 2.0 | 1 (09-16 07:37Z) |
| ap-southeast-2 | 112 | 0% | 1.0 | 1 (09-16 07:37Z) |
| ap-southeast-3 | 112 | 0% | 2.5 | 1 (09-16 07:37Z) |
| us-east-1 | 112 | 0% | 2.0 | 3 (09-16 07:37Z) |
| us-east-2 | 112 | 0% | 1.6 | 3 (09-16 07:37Z) |
| us-west-2 | 112 | 0% | 1.5 | 1 (09-16 07:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111133333333333333333333333333333333333
ap-northeast-1   211232222221123221123323333333333333223321132212
ap-northeast-2   333333333333233333333333333333333333333333333333
ap-south-1       122111111111211313121111333333313333333331111121
ap-southeast-2   111111111111111111111311111111111111111111111111
ap-southeast-3   212333113133113333333333333333333333313133131331
us-east-1        333321133221221131131133223311323233222222122113
us-east-2        333113333111311111131311333333333333333111111113
us-west-2        311111111111111111111111133313313333333111211121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 31 | 0% | 1.0 | 1 (09-16 01:21Z) |
| ap-east-1 ape1-az2 | 57 | 0% | 2.1 | 3 (09-16 07:37Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 60 | 0% | 2.3 | 1 (09-16 01:21Z) |
| ap-northeast-2 apne2-az1 | 104 | 0% | 2.9 | 3 (09-16 01:21Z) |
| ap-northeast-2 apne2-az3 | 101 | 0% | 2.9 | 1 (09-16 07:37Z) |
| ap-northeast-2 apne2-az4 | 109 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-south-1 aps1-az1 | 47 | 0% | 1.6 | 1 (09-16 07:37Z) |
| ap-south-1 aps1-az3 | 62 | 0% | 2.6 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 17 | 0% | 1.0 | 1 (09-15 22:08Z) |
| ap-southeast-3 apse3-az1 | 20 | 0% | 1.0 | 1 (09-16 07:37Z) |
| ap-southeast-3 apse3-az3 | 87 | 0% | 2.9 | 3 (09-16 01:21Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 31 | 0% | 1.1 | 1 (09-15 18:07Z) |
| us-east-1 use1-az4 | 19 | 0% | 1.2 | 1 (09-16 07:37Z) |
| us-east-1 use1-az5 | 32 | 0% | 1.3 | 1 (09-16 01:21Z) |
| us-east-1 use1-az6 | 43 | 0% | 1.2 | 1 (09-15 18:07Z) |
| us-east-2 use2-az1 | 34 | 0% | 1.5 | 1 (09-16 07:37Z) |
| us-east-2 use2-az2 | 48 | 0% | 1.8 | 1 (09-16 07:37Z) |
| us-east-2 use2-az3 | 56 | 0% | 2.2 | 3 (09-16 07:37Z) |
| us-west-2 usw2-az1 | 30 | 0% | 1.9 | 1 (09-16 01:21Z) |
| us-west-2 usw2-az2 | 23 | 0% | 1.8 | 1 (09-15 13:28Z) |
| us-west-2 usw2-az3 | 57 | 0% | 1.6 | 1 (09-16 07:37Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 112 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-northeast-1 | 112 | 76% | 7.3 | 4 (09-16 07:37Z) |
| ap-northeast-2 | 112 | 100% | 9.0 | 9 (09-16 07:37Z) |
| ap-south-1 | 112 | 33% | 4.8 | 9 (09-16 07:37Z) |
| ap-southeast-2 | 112 | 9% | 2.6 | 2 (09-16 07:37Z) |
| ap-southeast-3 | 112 | 0% | 2.5 | 1 (09-16 07:37Z) |
| us-east-1 | 112 | 71% | 6.7 | 9 (09-16 07:37Z) |
| us-east-2 | 112 | 72% | 7.0 | 9 (09-16 07:37Z) |
| us-west-2 | 112 | 49% | 5.5 | 3 (09-16 07:37Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   439999339992249992349999999999999999649993399924
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333999922999513339939999999999999999999999189999
ap-southeast-2   113311113322222311233333333333322332222222222222
ap-southeast-3   212333113133113333333333333333333333313133131331
us-east-1        995445994456993299992349999999999999994368443249
us-east-2        999999999199992333991919999999999999999999992129
us-west-2        999442951332313323423353999999999999999342543353
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 4 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 5 | 5 | 3 | 3 | 6 | 4 | 2 | 7 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 4 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 4 | 6 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 7 | 7 | 9 | 6 | 6 | 4 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 45 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-east-1 ape1-az2 | 35 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-east-1 ape1-az3 | 38 | 0% | 3.0 | 3 (09-16 01:21Z) |
| ap-northeast-1 apne1-az1 | 56 | 86% | 8.1 | 9 (09-15 22:08Z) |
| ap-northeast-1 apne1-az2 | 21 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az4 | 76 | 100% | 9.0 | 9 (09-15 22:08Z) |
| ap-northeast-2 apne2-az1 | 103 | 100% | 9.0 | 9 (09-16 07:37Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 102 | 100% | 9.0 | 9 (09-16 07:37Z) |
| ap-northeast-2 apne2-az4 | 41 | 0% | 3.0 | 3 (09-16 07:37Z) |
| ap-south-1 aps1-az1 | 26 | 15% | 3.9 | 9 (09-16 01:21Z) |
| ap-south-1 aps1-az2 | 31 | 0% | 3.0 | 3 (09-16 01:21Z) |
| ap-south-1 aps1-az3 | 41 | 56% | 6.4 | 4 (09-16 07:37Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 34 | 0% | 3.0 | 3 (09-16 01:21Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 45 | 96% | 8.7 | 2 (09-15 07:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 45 | 100% | 9.0 | 9 (09-16 07:37Z) |
| us-east-2 use2-az1 | 42 | 100% | 9.0 | 9 (09-16 07:37Z) |
| us-east-2 use2-az2 | 73 | 97% | 8.8 | 9 (09-16 07:37Z) |
| us-east-2 use2-az3 | 49 | 84% | 7.9 | 9 (09-16 07:37Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.719700 | 2026-09-16T07:37:16Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-16T07:37:16Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.797300 | 2026-09-16T07:37:16Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.977800 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590500 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579100 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565800 | 2026-09-16T07:37:16Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741900 | 2026-09-16T07:37:16Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.569600 | 2026-09-16T07:37:16Z |
| ap-south-1 | ap-south-1a | Windows | 0.327500 | 2026-09-16T07:37:16Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.478800 | 2026-09-16T07:37:16Z |
| ap-south-1 | ap-south-1b | Windows | 0.320000 | 2026-09-16T07:37:16Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686100 | 2026-09-16T07:37:16Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503300 | 2026-09-16T07:37:16Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.882500 | 2026-09-16T07:37:16Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.499000 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.875500 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1a | Windows | 0.343200 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.674100 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1b | Windows | 0.329900 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.577900 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1c | Windows | 0.307700 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.545800 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1d | Windows | 0.316900 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558500 | 2026-09-16T07:37:16Z |
| us-east-1 | us-east-1f | Windows | 0.324000 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527400 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2a | Windows | 0.640500 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528400 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.518600 | 2026-09-16T07:37:16Z |
| us-east-2 | us-east-2c | Windows | 0.638300 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568500 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2a | Windows | 0.344500 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.536200 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2b | Windows | 0.339000 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535600 | 2026-09-16T07:37:16Z |
| us-west-2 | us-west-2c | Windows | 0.338700 | 2026-09-16T07:37:16Z |
