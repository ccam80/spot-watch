# Spot placement score log

Generated 2026-09-10 00:08 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 76 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-northeast-1 | 76 | 0% | 1.8 | 1 (09-10 00:07Z) |
| ap-northeast-2 | 76 | 0% | 2.9 | 3 (09-10 00:07Z) |
| ap-south-1 | 76 | 0% | 2.0 | 1 (09-10 00:07Z) |
| ap-southeast-2 | 76 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-southeast-3 | 76 | 0% | 2.5 | 3 (09-10 00:07Z) |
| us-east-1 | 76 | 0% | 1.9 | 1 (09-10 00:07Z) |
| us-east-2 | 76 | 0% | 1.4 | 1 (09-10 00:07Z) |
| us-west-2 | 76 | 0% | 1.4 | 1 (09-10 00:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   131121111221131133331133333122111122211232222221
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       221332211333223333332333311121111311122111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333131313133333333113333333313333212333113133
us-east-1        111111221233321131323333232323332322333321133221
us-east-2        311111111111111111131111133111131113333113333111
us-west-2        111121112222222222211111111111111213311111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 25 | 0% | 1.0 | 1 (09-09 14:29Z) |
| ap-east-1 ape1-az2 | 26 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-northeast-1 apne1-az1 | 16 | 0% | 1.1 | 1 (09-10 00:07Z) |
| ap-northeast-1 apne1-az4 | 40 | 0% | 2.0 | 1 (09-09 14:29Z) |
| ap-northeast-2 apne2-az1 | 72 | 0% | 2.9 | 3 (09-10 00:07Z) |
| ap-northeast-2 apne2-az3 | 68 | 0% | 2.9 | 3 (09-10 00:07Z) |
| ap-northeast-2 apne2-az4 | 75 | 0% | 3.0 | 3 (09-10 00:07Z) |
| ap-south-1 aps1-az1 | 31 | 0% | 1.6 | 1 (09-09 21:39Z) |
| ap-south-1 aps1-az3 | 45 | 0% | 2.5 | 1 (09-10 00:07Z) |
| ap-southeast-2 apse2-az1 | 18 | 0% | 1.0 | 1 (09-10 00:07Z) |
| ap-southeast-2 apse2-az2 | 14 | 0% | 1.0 | 1 (09-09 09:37Z) |
| ap-southeast-3 apse3-az1 | 15 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 60 | 0% | 2.9 | 3 (09-10 00:07Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 24 | 0% | 1.1 | 1 (09-09 18:30Z) |
| us-east-1 use1-az4 | 14 | 0% | 1.3 | 1 (09-09 18:30Z) |
| us-east-1 use1-az5 | 25 | 0% | 1.2 | 1 (09-10 00:07Z) |
| us-east-1 use1-az6 | 33 | 0% | 1.1 | 1 (09-09 21:39Z) |
| us-east-2 use2-az1 | 18 | 0% | 1.2 | 1 (09-09 21:39Z) |
| us-east-2 use2-az2 | 30 | 0% | 1.6 | 1 (09-09 21:39Z) |
| us-east-2 use2-az3 | 34 | 0% | 2.0 | 1 (09-10 00:07Z) |
| us-west-2 usw2-az1 | 17 | 0% | 1.5 | 1 (09-09 14:29Z) |
| us-west-2 usw2-az2 | 12 | 0% | 1.3 | 1 (09-09 09:37Z) |
| us-west-2 usw2-az3 | 36 | 0% | 1.3 | 1 (09-09 21:39Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 76 | 0% | 3.0 | 3 (09-10 00:07Z) |
| ap-northeast-1 | 76 | 78% | 7.4 | 2 (09-10 00:07Z) |
| ap-northeast-2 | 76 | 100% | 9.0 | 9 (09-10 00:07Z) |
| ap-south-1 | 76 | 9% | 3.4 | 9 (09-10 00:07Z) |
| ap-southeast-2 | 76 | 13% | 2.8 | 2 (09-10 00:07Z) |
| ap-southeast-3 | 76 | 0% | 2.5 | 3 (09-10 00:07Z) |
| us-east-1 | 76 | 74% | 6.5 | 6 (09-10 00:07Z) |
| us-east-2 | 76 | 71% | 6.9 | 9 (09-10 00:07Z) |
| us-west-2 | 76 | 49% | 5.5 | 2 (09-10 00:07Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   199992199991299999999999999999912999439999339992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333223333333333333333333333333333333999922999
ap-southeast-2   113111133311133133333333333333111311113311113322
ap-southeast-3   333333131313133333333113333333313333212333113133
us-east-1        921139943356542565995999999999999999995445994456
us-east-2        991139933323933829999999999999999999999999999199
us-west-2        292124294434453454499858969999719999999442951332
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 5 | 3 | · | 3 | 4 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 5 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 5 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 7 | 4 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 7 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 3.0 | 3 (09-10 00:07Z) |
| ap-east-1 ape1-az2 | 24 | 0% | 3.0 | 3 (09-09 21:39Z) |
| ap-east-1 ape1-az3 | 24 | 0% | 3.0 | 3 (09-09 14:29Z) |
| ap-northeast-1 apne1-az1 | 33 | 76% | 7.5 | 9 (09-09 21:39Z) |
| ap-northeast-1 apne1-az2 | 18 | 0% | 3.0 | 3 (09-09 21:39Z) |
| ap-northeast-1 apne1-az4 | 55 | 100% | 9.0 | 9 (09-09 21:39Z) |
| ap-northeast-2 apne2-az1 | 72 | 100% | 9.0 | 9 (09-10 00:07Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 72 | 100% | 9.0 | 9 (09-10 00:07Z) |
| ap-northeast-2 apne2-az4 | 28 | 0% | 3.0 | 3 (09-10 00:07Z) |
| ap-south-1 aps1-az1 | 16 | 0% | 3.0 | 3 (09-10 00:07Z) |
| ap-south-1 aps1-az2 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az3 | 16 | 6% | 3.4 | 9 (09-10 00:07Z) |
| ap-southeast-2 apse2-az1 | 9 | 33% | 4.8 | 3 (09-09 18:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 9 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 25 | 0% | 3.0 | 3 (09-10 00:07Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 28 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az4 | 29 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 32 | 100% | 9.0 | 9 (09-09 09:37Z) |
| us-east-2 use2-az1 | 30 | 100% | 9.0 | 9 (09-10 00:07Z) |
| us-east-2 use2-az2 | 49 | 96% | 8.7 | 9 (09-10 00:07Z) |
| us-east-2 use2-az3 | 30 | 73% | 7.2 | 9 (09-10 00:07Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.747000 | 2026-09-10T00:07:55Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.844400 | 2026-09-10T00:07:55Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783300 | 2026-09-10T00:07:55Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956900 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596300 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.583200 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574600 | 2026-09-10T00:07:55Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-10T00:07:55Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.539900 | 2026-09-10T00:07:55Z |
| ap-south-1 | ap-south-1a | Windows | 0.324000 | 2026-09-10T00:07:55Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.492000 | 2026-09-10T00:07:55Z |
| ap-south-1 | ap-south-1b | Windows | 0.326700 | 2026-09-10T00:07:55Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.754900 | 2026-09-10T00:07:55Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.506600 | 2026-09-10T00:07:55Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.883100 | 2026-09-10T00:07:55Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.417000 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.908200 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1a | Windows | 0.359500 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.721200 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1b | Windows | 0.322300 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.604300 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1c | Windows | 0.320200 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.532000 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1d | Windows | 0.325400 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.571000 | 2026-09-10T00:07:55Z |
| us-east-1 | us-east-1f | Windows | 0.321200 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554200 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.546900 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.539500 | 2026-09-10T00:07:55Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.578400 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2a | Windows | 0.310400 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.554900 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2b | Windows | 0.317600 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.532900 | 2026-09-10T00:07:55Z |
| us-west-2 | us-west-2c | Windows | 0.342800 | 2026-09-10T00:07:55Z |
