# Spot placement score log

Generated 2026-09-04 21:23 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 44 | 0% | 1.0 | 1 (09-04 21:23Z) |
| ap-northeast-1 | 44 | 0% | 1.6 | 1 (09-04 21:23Z) |
| ap-northeast-2 | 44 | 0% | 2.9 | 3 (09-04 21:23Z) |
| ap-south-1 | 44 | 0% | 2.2 | 3 (09-04 21:23Z) |
| ap-southeast-2 | 44 | 0% | 1.0 | 1 (09-04 21:23Z) |
| ap-southeast-3 | 44 | 0% | 2.5 | 3 (09-04 21:23Z) |
| us-east-1 | 44 | 0% | 1.6 | 1 (09-04 21:23Z) |
| us-east-2 | 44 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-west-2 | 44 | 0% | 1.5 | 2 (09-04 21:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1            11111111111111111111111111111111111111111111
ap-northeast-1       11131133331331311113111111111311211112211311
ap-northeast-2       33333333333333333333333333113333333333333333
ap-south-1           33313133333331333311131113122213322113332233
ap-southeast-2       11111111111111111111111111111111111111111111
ap-southeast-3       33333333232321113211233333333333331313131333
us-east-1            32333211113111111312111111111111112212333211
us-east-2            11111311311113311111111111113111111111111111
us-west-2            22122211311111313331111111111111211122222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | 2 | · | 3 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 19 | 0% | 1.0 | 1 (09-04 21:23Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 26 | 0% | 1.8 | 1 (09-04 21:23Z) |
| ap-northeast-2 apne2-az1 | 40 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-northeast-2 apne2-az3 | 40 | 0% | 2.9 | 3 (09-04 21:23Z) |
| ap-northeast-2 apne2-az4 | 43 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-south-1 aps1-az1 | 16 | 0% | 1.8 | 2 (09-04 18:19Z) |
| ap-south-1 aps1-az3 | 28 | 0% | 2.7 | 3 (09-04 21:23Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 6 | 0% | 1.0 | 1 (09-03 21:40Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 35 | 0% | 2.8 | 3 (09-04 21:23Z) |
| us-east-1 use1-az1 | 7 | 0% | 1.0 | 1 (09-03 14:26Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 8 | 0% | 1.5 | 1 (09-03 14:26Z) |
| us-east-1 use1-az5 | 16 | 0% | 1.2 | 1 (09-04 21:23Z) |
| us-east-1 use1-az6 | 19 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-east-2 use2-az1 | 6 | 0% | 1.3 | 1 (09-04 14:16Z) |
| us-east-2 use2-az2 | 13 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-east-2 use2-az3 | 14 | 0% | 1.6 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az1 | 11 | 0% | 1.5 | 1 (09-04 21:23Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 18 | 0% | 1.4 | 1 (09-04 14:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 44 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-northeast-1 | 44 | 77% | 7.2 | 9 (09-04 21:23Z) |
| ap-northeast-2 | 44 | 100% | 9.0 | 9 (09-04 21:23Z) |
| ap-south-1 | 44 | 0% | 2.8 | 3 (09-04 21:23Z) |
| ap-southeast-2 | 44 | 23% | 3.2 | 1 (09-04 21:23Z) |
| ap-southeast-3 | 44 | 0% | 2.5 | 3 (09-04 21:23Z) |
| us-east-1 | 44 | 64% | 5.8 | 5 (09-04 21:23Z) |
| us-east-2 | 44 | 55% | 5.8 | 8 (09-04 21:23Z) |
| us-west-2 | 44 | 34% | 4.8 | 4 (09-04 21:23Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1            33333333333333333333333333333333333333333333
ap-northeast-1       99199999999999999919911999911999921999912999
ap-northeast-2       99999999999999999999999999999999999999999999
ap-south-1           33313333333333333313331133333333332233333333
ap-southeast-2       11111197999999993111111231111131111333111331
ap-southeast-3       33333333232321113211233333333333331313131333
us-east-1            76678758999999999994119112199211399433565425
us-east-2            92991929999919922191119999999911399333239338
us-west-2            44243921922229999999129924492921242944344534
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 3 | 1 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 1 | · | 5 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 1 | 9 | 9 | 2 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 9 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 4 | 2 | 2 | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 26 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-east-1 ape1-az2 | 17 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-east-1 ape1-az3 | 20 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-northeast-1 apne1-az1 | 11 | 36% | 5.2 | 3 (09-04 21:23Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 32 | 100% | 9.0 | 9 (09-04 21:23Z) |
| ap-northeast-2 apne2-az1 | 43 | 100% | 9.0 | 9 (09-04 21:23Z) |
| ap-northeast-2 apne2-az2 | 5 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az3 | 43 | 100% | 9.0 | 9 (09-04 21:23Z) |
| ap-northeast-2 apne2-az4 | 22 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-south-1 aps1-az1 | 10 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-south-1 aps1-az2 | 20 | 0% | 3.0 | 3 (09-04 21:23Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 4 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-3 apse3-az3 | 19 | 0% | 3.0 | 3 (09-04 21:23Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 11 | 100% | 8.9 | 8 (09-03 04:19Z) |
| us-east-1 use1-az4 | 11 | 100% | 9.0 | 9 (09-03 09:40Z) |
| us-east-1 use1-az5 | 14 | 100% | 8.9 | 8 (09-03 09:40Z) |
| us-east-1 use1-az6 | 12 | 100% | 9.0 | 9 (09-03 04:19Z) |
| us-east-2 use2-az1 | 11 | 100% | 8.9 | 9 (09-02 14:23Z) |
| us-east-2 use2-az2 | 21 | 90% | 8.3 | 9 (09-04 09:32Z) |
| us-east-2 use2-az3 | 15 | 60% | 6.3 | 3 (09-04 21:23Z) |
| us-west-2 usw2-az1 | 12 | 92% | 8.5 | 9 (09-03 14:26Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 13 | 92% | 8.5 | 2 (09-04 09:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.754400 | 2026-09-04T21:23:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-04T21:23:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.803900 | 2026-09-04T21:23:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.896200 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.556700 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.556700 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.556700 | 2026-09-04T21:23:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-04T21:23:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.557600 | 2026-09-04T21:23:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.311900 | 2026-09-04T21:23:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500400 | 2026-09-04T21:23:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.314700 | 2026-09-04T21:23:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747000 | 2026-09-04T21:23:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.470000 | 2026-09-04T21:23:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.936400 | 2026-09-04T21:23:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378700 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.925000 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1a | Windows | 0.333700 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.681900 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1b | Windows | 0.319900 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.569300 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1c | Windows | 0.317000 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.472600 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1d | Windows | 0.317700 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.505500 | 2026-09-04T21:23:14Z |
| us-east-1 | us-east-1f | Windows | 0.316400 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.452700 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.459700 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.452700 | 2026-09-04T21:23:14Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561200 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2a | Windows | 0.286300 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.521000 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2b | Windows | 0.286500 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.521800 | 2026-09-04T21:23:14Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-04T21:23:14Z |
