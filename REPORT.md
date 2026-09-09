# Spot placement score log

Generated 2026-09-09 18:30 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 74 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-northeast-1 | 74 | 0% | 1.8 | 2 (09-09 18:30Z) |
| ap-northeast-2 | 74 | 0% | 2.9 | 3 (09-09 18:30Z) |
| ap-south-1 | 74 | 0% | 2.0 | 1 (09-09 18:30Z) |
| ap-southeast-2 | 74 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-southeast-3 | 74 | 0% | 2.5 | 1 (09-09 18:30Z) |
| us-east-1 | 74 | 0% | 1.9 | 2 (09-09 18:30Z) |
| us-east-2 | 74 | 0% | 1.5 | 1 (09-09 18:30Z) |
| us-west-2 | 74 | 0% | 1.4 | 1 (09-09 18:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   111311211112211311333311333331221111222112322222
ap-northeast-2   113333333333333333333333333333333333333333333333
ap-south-1       122213322113332233333323333111211113111221111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333331313131333333331133333333133332123331131
us-east-1        111111112212333211313233332323233323223333211332
us-east-2        113111111111111111111311111331111311133331133331
us-west-2        111111211122222222222111111111111112133111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 3 | · | 3 | 2 | · | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | · | 1 | · | 2 | 2 | 1 | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 25 | 0% | 1.0 | 1 (09-09 14:29Z) |
| ap-east-1 ape1-az2 | 25 | 0% | 1.0 | 1 (09-09 09:37Z) |
| ap-northeast-1 apne1-az1 | 15 | 0% | 1.1 | 1 (09-09 09:37Z) |
| ap-northeast-1 apne1-az4 | 40 | 0% | 2.0 | 1 (09-09 14:29Z) |
| ap-northeast-2 apne2-az1 | 70 | 0% | 2.9 | 3 (09-09 18:30Z) |
| ap-northeast-2 apne2-az3 | 66 | 0% | 2.9 | 3 (09-09 18:30Z) |
| ap-northeast-2 apne2-az4 | 73 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-south-1 aps1-az1 | 30 | 0% | 1.7 | 1 (09-09 18:30Z) |
| ap-south-1 aps1-az3 | 44 | 0% | 2.5 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az1 | 17 | 0% | 1.0 | 1 (09-08 18:34Z) |
| ap-southeast-2 apse2-az2 | 14 | 0% | 1.0 | 1 (09-09 09:37Z) |
| ap-southeast-3 apse3-az1 | 15 | 0% | 1.0 | 1 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 58 | 0% | 2.9 | 3 (09-09 14:29Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 24 | 0% | 1.1 | 1 (09-09 18:30Z) |
| us-east-1 use1-az4 | 14 | 0% | 1.3 | 1 (09-09 18:30Z) |
| us-east-1 use1-az5 | 24 | 0% | 1.2 | 1 (09-09 14:29Z) |
| us-east-1 use1-az6 | 32 | 0% | 1.1 | 1 (09-09 18:30Z) |
| us-east-2 use2-az1 | 17 | 0% | 1.2 | 1 (09-09 18:30Z) |
| us-east-2 use2-az2 | 29 | 0% | 1.7 | 3 (09-09 14:29Z) |
| us-east-2 use2-az3 | 32 | 0% | 2.0 | 3 (09-09 14:29Z) |
| us-west-2 usw2-az1 | 17 | 0% | 1.5 | 1 (09-09 14:29Z) |
| us-west-2 usw2-az2 | 12 | 0% | 1.3 | 1 (09-09 09:37Z) |
| us-west-2 usw2-az3 | 35 | 0% | 1.3 | 1 (09-09 18:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 74 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-northeast-1 | 74 | 78% | 7.4 | 9 (09-09 18:30Z) |
| ap-northeast-2 | 74 | 100% | 9.0 | 9 (09-09 18:30Z) |
| ap-south-1 | 74 | 7% | 3.2 | 9 (09-09 18:30Z) |
| ap-southeast-2 | 74 | 14% | 2.8 | 3 (09-09 18:30Z) |
| ap-southeast-3 | 74 | 0% | 2.5 | 1 (09-09 18:30Z) |
| us-east-1 | 74 | 73% | 6.5 | 4 (09-09 18:30Z) |
| us-east-2 | 74 | 70% | 6.9 | 1 (09-09 18:30Z) |
| us-west-2 | 74 | 50% | 5.6 | 3 (09-09 18:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   911999921999912999999999999999999129994399993399
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333332233333333333333333333333333333339999229
ap-southeast-2   111131111333111331333333333333331113111133111133
ap-southeast-3   333333331313131333333331133333333133332123331131
us-east-1        199211399433565425659959999999999999999954459944
us-east-2        999911399333239338299999999999999999999999999991
us-west-2        492921242944344534544998589699997199999994429513
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 7 | 9 | · | 1 | 4 | · | 1 | · | 9 | 3 | 2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 4 | 3 | · | 3 | 4 | · | 1 | · | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 6 | 1 | 1 | 5 | 2 | 3 | 3 | 2 | 5 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | · | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 6 | 6 | 4 | 6 |
| us-west-2 | 4 | 2 | · | 2 | 6 | · | 9 | · | 6 | 5 | 9 | 9 | 9 | 9 | 7 | 9 | 7 | 2 | 5 | 6 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 31 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-east-1 ape1-az2 | 23 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-east-1 ape1-az3 | 24 | 0% | 3.0 | 3 (09-09 14:29Z) |
| ap-northeast-1 apne1-az1 | 32 | 75% | 7.5 | 9 (09-09 18:30Z) |
| ap-northeast-1 apne1-az2 | 17 | 0% | 3.0 | 3 (09-09 00:06Z) |
| ap-northeast-1 apne1-az4 | 54 | 100% | 9.0 | 9 (09-09 18:30Z) |
| ap-northeast-2 apne2-az1 | 70 | 100% | 9.0 | 9 (09-09 18:30Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 70 | 100% | 9.0 | 9 (09-09 18:30Z) |
| ap-northeast-2 apne2-az4 | 26 | 0% | 3.0 | 3 (09-09 09:37Z) |
| ap-south-1 aps1-az1 | 15 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-south-1 aps1-az2 | 24 | 0% | 3.0 | 3 (09-08 21:48Z) |
| ap-south-1 aps1-az3 | 15 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-southeast-2 apse2-az1 | 9 | 33% | 4.8 | 3 (09-09 18:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 9 | 0% | 3.0 | 3 (09-09 18:30Z) |
| ap-southeast-3 apse3-az3 | 23 | 0% | 3.0 | 3 (09-09 00:06Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 28 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az4 | 29 | 100% | 9.0 | 9 (09-09 04:36Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 32 | 100% | 9.0 | 9 (09-09 09:37Z) |
| us-east-2 use2-az1 | 29 | 100% | 9.0 | 9 (09-09 14:29Z) |
| us-east-2 use2-az2 | 47 | 96% | 8.7 | 9 (09-09 14:29Z) |
| us-east-2 use2-az3 | 28 | 71% | 7.1 | 9 (09-09 14:29Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.746700 | 2026-09-09T18:30:52Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.842700 | 2026-09-09T18:30:52Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.783300 | 2026-09-09T18:30:52Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.949900 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596000 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.583600 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574800 | 2026-09-09T18:30:52Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-09T18:30:52Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.540600 | 2026-09-09T18:30:52Z |
| ap-south-1 | ap-south-1a | Windows | 0.324800 | 2026-09-09T18:30:52Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.493500 | 2026-09-09T18:30:52Z |
| ap-south-1 | ap-south-1b | Windows | 0.327300 | 2026-09-09T18:30:52Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.754900 | 2026-09-09T18:30:52Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508900 | 2026-09-09T18:30:52Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.888500 | 2026-09-09T18:30:52Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.414700 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.909300 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1a | Windows | 0.357000 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.720200 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1b | Windows | 0.321500 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.604700 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1c | Windows | 0.320100 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520600 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1d | Windows | 0.325400 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.566800 | 2026-09-09T18:30:52Z |
| us-east-1 | us-east-1f | Windows | 0.321000 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548000 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2a | Windows | 0.641900 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545800 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.541500 | 2026-09-09T18:30:52Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.577800 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2a | Windows | 0.310400 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.553800 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2b | Windows | 0.317000 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.534500 | 2026-09-09T18:30:52Z |
| us-west-2 | us-west-2c | Windows | 0.342500 | 2026-09-09T18:30:52Z |
