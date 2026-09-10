# Spot placement score log

Generated 2026-09-10 16:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 79 | 0% | 1.1 | 3 (09-10 16:19Z) |
| ap-northeast-1 | 79 | 0% | 1.8 | 3 (09-10 16:19Z) |
| ap-northeast-2 | 79 | 0% | 2.9 | 3 (09-10 16:19Z) |
| ap-south-1 | 79 | 0% | 2.0 | 1 (09-10 16:19Z) |
| ap-southeast-2 | 79 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-southeast-3 | 79 | 0% | 2.5 | 3 (09-10 16:19Z) |
| us-east-1 | 79 | 0% | 1.9 | 1 (09-10 16:19Z) |
| us-east-2 | 79 | 0% | 1.5 | 1 (09-10 16:19Z) |
| us-west-2 | 79 | 0% | 1.4 | 1 (09-10 16:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111133
ap-northeast-1   121111221131133331133333122111122211232222221123
ap-northeast-2   333333333333333333333333333333333333333333333233
ap-south-1       332211333223333332333311121111311122111111111211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333131313133333333113333333313333212333113133113
us-east-1        111221233321131323333232323332322333321133221221
us-east-2        111111111111111131111133111131113333113333111311
us-west-2        121112222222222211111111111111213311111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 1 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 2 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 3 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 1 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 1 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 3 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 28 | 0% | 1.1 | 3 (09-10 16:19Z) |
| ap-northeast-1 apne1-az1 | 16 | 0% | 1.1 | 1 (09-10 00:07Z) |
| ap-northeast-1 apne1-az4 | 41 | 0% | 2.1 | 3 (09-10 16:19Z) |
| ap-northeast-2 apne2-az1 | 74 | 0% | 2.9 | 3 (09-10 16:19Z) |
| ap-northeast-2 apne2-az3 | 71 | 0% | 2.9 | 3 (09-10 16:19Z) |
| ap-northeast-2 apne2-az4 | 77 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-south-1 aps1-az1 | 33 | 0% | 1.6 | 1 (09-10 11:10Z) |
| ap-south-1 aps1-az3 | 45 | 0% | 2.5 | 1 (09-10 00:07Z) |
| ap-southeast-2 apse2-az1 | 18 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-southeast-2 apse2-az2 | 14 | 0% | 1.0 | 1 (09-09 09:37Z) |
| ap-southeast-3 apse3-az1 | 15 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 62 | 0% | 2.8 | 3 (09-10 16:19Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 24 | 0% | 1.1 | 1 (09-09 18:30Z) |
| us-east-1 use1-az4 | 14 | 0% | 1.3 | 1 (09-09 18:30Z) |
| us-east-1 use1-az5 | 27 | 0% | 1.2 | 1 (09-10 16:19Z) |
| us-east-1 use1-az6 | 35 | 0% | 1.1 | 1 (09-10 11:10Z) |
| us-east-2 use2-az1 | 20 | 0% | 1.3 | 1 (09-10 11:10Z) |
| us-east-2 use2-az2 | 32 | 0% | 1.7 | 1 (09-10 11:10Z) |
| us-east-2 use2-az3 | 36 | 0% | 2.0 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az1 | 18 | 0% | 1.4 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az2 | 13 | 0% | 1.3 | 1 (09-10 05:53Z) |
| us-west-2 usw2-az3 | 38 | 0% | 1.3 | 1 (09-10 11:10Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 79 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-northeast-1 | 79 | 76% | 7.3 | 9 (09-10 16:19Z) |
| ap-northeast-2 | 79 | 100% | 9.0 | 9 (09-10 16:19Z) |
| ap-south-1 | 79 | 10% | 3.4 | 3 (09-10 16:19Z) |
| ap-southeast-2 | 79 | 13% | 2.7 | 2 (09-10 16:19Z) |
| ap-southeast-3 | 79 | 0% | 2.5 | 3 (09-10 16:19Z) |
| us-east-1 | 79 | 73% | 6.5 | 3 (09-10 16:19Z) |
| us-east-2 | 79 | 71% | 6.9 | 2 (09-10 16:19Z) |
| us-west-2 | 79 | 47% | 5.4 | 3 (09-10 16:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   992199991299999999999999999912999439999339992249
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333223333333333333333333333333333333999922999513
ap-southeast-2   111133311133133333333333333111311113311113322222
ap-southeast-3   333131313133333333113333333313333212333113133113
us-east-1        139943356542565995999999999999999995445994456993
us-east-2        139933323933829999999999999999999999999999199992
us-west-2        124294434453454499858969999719999999442951332313
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 2 | 1 | · | 9 | 3 | 2 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 5 | 3 | · | 3 | 4 | 5 | 1 | · | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 1 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 1 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 5 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 8 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 1 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 9 | 4 | 9 | 6 | 7 | 4 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 3 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 34 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 27 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-east-1 ape1-az3 | 26 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-northeast-1 apne1-az1 | 34 | 76% | 7.6 | 9 (09-10 16:19Z) |
| ap-northeast-1 apne1-az2 | 18 | 0% | 3.0 | 3 (09-09 21:39Z) |
| ap-northeast-1 apne1-az4 | 56 | 100% | 9.0 | 9 (09-10 16:19Z) |
| ap-northeast-2 apne2-az1 | 75 | 100% | 9.0 | 9 (09-10 16:19Z) |
| ap-northeast-2 apne2-az2 | 7 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-northeast-2 apne2-az3 | 75 | 100% | 9.0 | 9 (09-10 16:19Z) |
| ap-northeast-2 apne2-az4 | 30 | 0% | 3.0 | 3 (09-10 11:10Z) |
| ap-south-1 aps1-az1 | 17 | 0% | 3.0 | 3 (09-10 16:19Z) |
| ap-south-1 aps1-az2 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az3 | 17 | 6% | 3.4 | 3 (09-10 16:19Z) |
| ap-southeast-2 apse2-az1 | 9 | 33% | 4.8 | 3 (09-09 18:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 9 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 25 | 0% | 3.0 | 3 (09-10 00:07Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 29 | 100% | 9.0 | 9 (09-10 05:53Z) |
| us-east-1 use1-az4 | 31 | 97% | 8.8 | 2 (09-10 11:10Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 33 | 100% | 9.0 | 9 (09-10 05:53Z) |
| us-east-2 use2-az1 | 32 | 100% | 9.0 | 9 (09-10 11:10Z) |
| us-east-2 use2-az2 | 51 | 96% | 8.7 | 9 (09-10 11:10Z) |
| us-east-2 use2-az3 | 32 | 75% | 7.3 | 9 (09-10 11:10Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.744300 | 2026-09-10T16:19:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-10T16:19:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783500 | 2026-09-10T16:19:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.955900 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596400 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.582900 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573500 | 2026-09-10T16:19:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-10T16:19:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.545100 | 2026-09-10T16:19:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.322700 | 2026-09-10T16:19:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.494600 | 2026-09-10T16:19:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.326500 | 2026-09-10T16:19:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.755800 | 2026-09-10T16:19:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.505400 | 2026-09-10T16:19:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.871200 | 2026-09-10T16:19:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.420500 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.905500 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1a | Windows | 0.359000 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.721700 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1b | Windows | 0.321700 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.606900 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1c | Windows | 0.319900 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.538300 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1d | Windows | 0.324900 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.588700 | 2026-09-10T16:19:24Z |
| us-east-1 | us-east-1f | Windows | 0.321100 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549100 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2a | Windows | 0.643200 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.546600 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.531900 | 2026-09-10T16:19:24Z |
| us-east-2 | us-east-2c | Windows | 0.638300 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.580300 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2a | Windows | 0.315400 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.554600 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2b | Windows | 0.320100 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.535100 | 2026-09-10T16:19:24Z |
| us-west-2 | us-west-2c | Windows | 0.343100 | 2026-09-10T16:19:24Z |
