# Spot placement score log

Generated 2026-09-05 18:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 50 | 0% | 1.0 | 1 (09-05 18:11Z) |
| ap-northeast-1 | 50 | 0% | 1.7 | 1 (09-05 18:11Z) |
| ap-northeast-2 | 50 | 0% | 2.9 | 3 (09-05 18:11Z) |
| ap-south-1 | 50 | 0% | 2.3 | 3 (09-05 18:11Z) |
| ap-southeast-2 | 50 | 0% | 1.0 | 1 (09-05 18:11Z) |
| ap-southeast-3 | 50 | 0% | 2.5 | 1 (09-05 18:11Z) |
| us-east-1 | 50 | 0% | 1.7 | 3 (09-05 18:11Z) |
| us-east-2 | 50 | 0% | 1.2 | 1 (09-05 18:11Z) |
| us-west-2 | 50 | 0% | 1.5 | 1 (09-05 18:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   131133331331311113111111111311211112211311333311
ap-northeast-2   333333333333333333333333113333333333333333333333
ap-south-1       313133333331333311131113122213322113332233333323
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333232321113211233333333333331313131333333331
us-east-1        333211113111111312111111111111112212333211313233
us-east-2        111311311113311111111111113111111111111111111311
us-west-2        122211311111313331111111111111211122222222222111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 20 | 0% | 1.0 | 1 (09-05 18:11Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 30 | 0% | 2.0 | 3 (09-05 12:37Z) |
| ap-northeast-2 apne2-az1 | 46 | 0% | 3.0 | 3 (09-05 18:11Z) |
| ap-northeast-2 apne2-az3 | 46 | 0% | 2.9 | 3 (09-05 18:11Z) |
| ap-northeast-2 apne2-az4 | 49 | 0% | 3.0 | 3 (09-05 18:11Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 1.9 | 1 (09-05 18:11Z) |
| ap-south-1 aps1-az3 | 34 | 0% | 2.7 | 3 (09-05 18:11Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 8 | 0% | 1.0 | 1 (09-05 08:59Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 2.9 | 3 (09-05 15:59Z) |
| us-east-1 use1-az1 | 9 | 0% | 1.0 | 1 (09-05 08:59Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 10 | 0% | 1.4 | 1 (09-05 08:59Z) |
| us-east-1 use1-az5 | 16 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-east-1 use1-az6 | 22 | 0% | 1.2 | 1 (09-05 18:11Z) |
| us-east-2 use2-az1 | 9 | 0% | 1.2 | 1 (09-05 18:11Z) |
| us-east-2 use2-az2 | 16 | 0% | 1.1 | 1 (09-05 18:11Z) |
| us-east-2 use2-az3 | 15 | 0% | 1.7 | 3 (09-05 12:37Z) |
| us-west-2 usw2-az1 | 11 | 0% | 1.5 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 23 | 0% | 1.3 | 1 (09-05 18:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 50 | 0% | 3.0 | 3 (09-05 18:11Z) |
| ap-northeast-1 | 50 | 80% | 7.4 | 9 (09-05 18:11Z) |
| ap-northeast-2 | 50 | 100% | 9.0 | 9 (09-05 18:11Z) |
| ap-south-1 | 50 | 0% | 2.8 | 3 (09-05 18:11Z) |
| ap-southeast-2 | 50 | 20% | 3.1 | 3 (09-05 18:11Z) |
| ap-southeast-3 | 50 | 0% | 2.5 | 1 (09-05 18:11Z) |
| us-east-1 | 50 | 68% | 5.9 | 9 (09-05 18:11Z) |
| us-east-2 | 50 | 58% | 6.0 | 9 (09-05 18:11Z) |
| us-west-2 | 50 | 38% | 5.0 | 8 (09-05 18:11Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   199999999999999919911999911999921999912999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       313333333333333313331133333333332233333333333333
ap-southeast-2   111197999999993111111231111131111333111331333333
ap-southeast-3   333333232321113211233333333333331313131333333331
us-east-1        678758999999999994119112199211399433565425659959
us-east-2        991929999919922191119999999911399333239338299999
us-west-2        243921922229999999129924492921242944344534544998
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 2 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 6 | 1 | · | 5 | 2 | · | 3 | 2 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 7 | · | 9 | · | 9 | 8 | · | 8 | 5 | · | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 6 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 5 | 2 | 2 | 4 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 17 | 53% | 6.2 | 9 (09-05 18:11Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 38 | 100% | 9.0 | 9 (09-05 18:11Z) |
| ap-northeast-2 apne2-az1 | 49 | 100% | 9.0 | 9 (09-05 18:11Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 48 | 100% | 9.0 | 9 (09-05 18:11Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 13 | 100% | 8.9 | 9 (09-05 18:11Z) |
| us-east-1 use1-az4 | 14 | 100% | 9.0 | 9 (09-05 18:11Z) |
| us-east-1 use1-az5 | 17 | 100% | 8.9 | 9 (09-05 18:11Z) |
| us-east-1 use1-az6 | 14 | 100% | 9.0 | 9 (09-05 18:11Z) |
| us-east-2 use2-az1 | 16 | 100% | 8.9 | 9 (09-05 18:11Z) |
| us-east-2 use2-az2 | 26 | 92% | 8.4 | 9 (09-05 18:11Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 14 | 93% | 8.6 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az2 | 11 | 100% | 9.0 | 9 (09-05 15:59Z) |
| us-west-2 usw2-az3 | 15 | 93% | 8.5 | 9 (09-05 15:59Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.752900 | 2026-09-05T18:11:56Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-05T18:11:56Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.780400 | 2026-09-05T18:11:56Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.927900 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.577600 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.571400 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.575800 | 2026-09-05T18:11:56Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-05T18:11:56Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.555500 | 2026-09-05T18:11:56Z |
| ap-south-1 | ap-south-1a | Windows | 0.314600 | 2026-09-05T18:11:56Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500000 | 2026-09-05T18:11:56Z |
| ap-south-1 | ap-south-1b | Windows | 0.318600 | 2026-09-05T18:11:56Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747100 | 2026-09-05T18:11:56Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.479700 | 2026-09-05T18:11:56Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.934800 | 2026-09-05T18:11:56Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.379500 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.915800 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1a | Windows | 0.332600 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.667100 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1b | Windows | 0.318800 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.562900 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1c | Windows | 0.315600 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.469300 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1d | Windows | 0.316500 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.504400 | 2026-09-05T18:11:56Z |
| us-east-1 | us-east-1f | Windows | 0.315200 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.469100 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.473500 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.476200 | 2026-09-05T18:11:56Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.559800 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2a | Windows | 0.291600 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.518000 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2b | Windows | 0.294500 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.519300 | 2026-09-05T18:11:56Z |
| us-west-2 | us-west-2c | Windows | 0.333400 | 2026-09-05T18:11:56Z |
