# Spot placement score log

Generated 2026-09-04 09:32 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 41 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-northeast-1 | 41 | 0% | 1.6 | 1 (09-04 09:32Z) |
| ap-northeast-2 | 41 | 0% | 2.9 | 3 (09-04 09:32Z) |
| ap-south-1 | 41 | 0% | 2.2 | 2 (09-04 09:32Z) |
| ap-southeast-2 | 41 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-southeast-3 | 41 | 0% | 2.4 | 1 (09-04 09:32Z) |
| us-east-1 | 41 | 0% | 1.6 | 3 (09-04 09:32Z) |
| us-east-2 | 41 | 0% | 1.2 | 1 (09-04 09:32Z) |
| us-west-2 | 41 | 0% | 1.5 | 2 (09-04 09:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1               11111111111111111111111111111111111111111
ap-northeast-1          11131133331331311113111111111311211112211
ap-northeast-2          33333333333333333333333333113333333333333
ap-south-1              33313133333331333311131113122213322113332
ap-southeast-2          11111111111111111111111111111111111111111
ap-southeast-3          33333333232321113211233333333333331313131
us-east-1               32333211113111111312111111111111112212333
us-east-2               11111311311113311111111111113111111111111
us-west-2               22122211311111313331111111111111211122222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 2 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | 2 | · | 3 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 18 | 0% | 1.0 | 1 (09-04 04:22Z) |
| ap-east-1 ape1-az2 | 12 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-northeast-1 apne1-az1 | 9 | 0% | 1.2 | 1 (09-04 09:32Z) |
| ap-northeast-1 apne1-az4 | 24 | 0% | 1.8 | 1 (09-04 04:22Z) |
| ap-northeast-2 apne2-az1 | 37 | 0% | 2.9 | 3 (09-04 09:32Z) |
| ap-northeast-2 apne2-az3 | 37 | 0% | 2.9 | 3 (09-04 09:32Z) |
| ap-northeast-2 apne2-az4 | 40 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-south-1 aps1-az1 | 14 | 0% | 1.8 | 1 (09-03 23:59Z) |
| ap-south-1 aps1-az3 | 26 | 0% | 2.7 | 1 (09-04 09:32Z) |
| ap-southeast-2 apse2-az1 | 10 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-southeast-2 apse2-az2 | 6 | 0% | 1.0 | 1 (09-03 21:40Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 32 | 0% | 2.8 | 1 (09-04 09:32Z) |
| us-east-1 use1-az1 | 7 | 0% | 1.0 | 1 (09-03 14:26Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 8 | 0% | 1.5 | 1 (09-03 14:26Z) |
| us-east-1 use1-az5 | 14 | 0% | 1.3 | 1 (09-04 09:32Z) |
| us-east-1 use1-az6 | 18 | 0% | 1.2 | 1 (09-03 23:59Z) |
| us-east-2 use2-az1 | 5 | 0% | 1.4 | 1 (09-03 23:59Z) |
| us-east-2 use2-az2 | 12 | 0% | 1.2 | 1 (09-03 09:40Z) |
| us-east-2 use2-az3 | 13 | 0% | 1.7 | 1 (09-04 09:32Z) |
| us-west-2 usw2-az1 | 10 | 0% | 1.6 | 1 (09-04 04:22Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 17 | 0% | 1.5 | 1 (09-03 23:59Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 41 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-northeast-1 | 41 | 76% | 7.1 | 2 (09-04 09:32Z) |
| ap-northeast-2 | 41 | 100% | 9.0 | 9 (09-04 09:32Z) |
| ap-south-1 | 41 | 0% | 2.8 | 3 (09-04 09:32Z) |
| ap-southeast-2 | 41 | 24% | 3.2 | 1 (09-04 09:32Z) |
| ap-southeast-3 | 41 | 0% | 2.4 | 1 (09-04 09:32Z) |
| us-east-1 | 41 | 66% | 5.9 | 5 (09-04 09:32Z) |
| us-east-2 | 41 | 56% | 5.9 | 9 (09-04 09:32Z) |
| us-west-2 | 41 | 34% | 4.9 | 4 (09-04 09:32Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1               33333333333333333333333333333333333333333
ap-northeast-1          99199999999999999919911999911999921999912
ap-northeast-2          99999999999999999999999999999999999999999
ap-south-1              33313333333333333313331133333333332233333
ap-southeast-2          11111197999999993111111231111131111333111
ap-southeast-3          33333333232321113211233333333333331313131
us-east-1               76678758999999999994119112199211399433565
us-east-2               92991929999919922191119999999911399333239
us-west-2               44243921922229999999129924492921242944344
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 4 | 1 | 9 | 3 | 5 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 1 | · | 6 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 8 | 1 | 9 | 9 | 2 | 9 | 5 | 4 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 9 | 3 | · | 9 | 9 | · | 8 | 9 | 2 | 2 | 5 | 2 | 2 | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 24 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-east-1 ape1-az2 | 16 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-east-1 ape1-az3 | 18 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-northeast-1 apne1-az1 | 9 | 44% | 5.7 | 3 (09-03 21:40Z) |
| ap-northeast-1 apne1-az2 | 14 | 0% | 3.0 | 3 (09-03 23:59Z) |
| ap-northeast-1 apne1-az4 | 29 | 100% | 9.0 | 9 (09-03 23:59Z) |
| ap-northeast-2 apne2-az1 | 40 | 100% | 9.0 | 9 (09-04 09:32Z) |
| ap-northeast-2 apne2-az2 | 4 | 0% | 3.0 | 3 (09-04 04:22Z) |
| ap-northeast-2 apne2-az3 | 40 | 100% | 9.0 | 9 (09-04 09:32Z) |
| ap-northeast-2 apne2-az4 | 21 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-south-1 aps1-az1 | 9 | 0% | 3.0 | 3 (09-04 04:22Z) |
| ap-south-1 aps1-az2 | 19 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-south-1 aps1-az3 | 11 | 0% | 3.0 | 3 (09-04 04:22Z) |
| ap-southeast-2 apse2-az1 | 7 | 43% | 5.3 | 3 (09-03 21:40Z) |
| ap-southeast-2 apse2-az3 | 2 | 0% | 3.0 | 3 (09-03 18:33Z) |
| ap-southeast-3 apse3-az3 | 17 | 0% | 3.0 | 3 (09-03 14:26Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 11 | 100% | 8.9 | 8 (09-03 04:19Z) |
| us-east-1 use1-az4 | 11 | 100% | 9.0 | 9 (09-03 09:40Z) |
| us-east-1 use1-az5 | 14 | 100% | 8.9 | 8 (09-03 09:40Z) |
| us-east-1 use1-az6 | 12 | 100% | 9.0 | 9 (09-03 04:19Z) |
| us-east-2 use2-az1 | 11 | 100% | 8.9 | 9 (09-02 14:23Z) |
| us-east-2 use2-az2 | 21 | 90% | 8.3 | 9 (09-04 09:32Z) |
| us-east-2 use2-az3 | 14 | 64% | 6.6 | 9 (09-04 09:32Z) |
| us-west-2 usw2-az1 | 12 | 92% | 8.5 | 9 (09-03 14:26Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 13 | 92% | 8.5 | 2 (09-04 09:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.755900 | 2026-09-04T09:32:50Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-04T09:32:50Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.819300 | 2026-09-04T09:32:50Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.888600 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.556700 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.556700 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.556700 | 2026-09-04T09:32:50Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-04T09:32:50Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548900 | 2026-09-04T09:32:50Z |
| ap-south-1 | ap-south-1a | Windows | 0.308100 | 2026-09-04T09:32:50Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.485800 | 2026-09-04T09:32:50Z |
| ap-south-1 | ap-south-1b | Windows | 0.308300 | 2026-09-04T09:32:50Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746100 | 2026-09-04T09:32:50Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.474000 | 2026-09-04T09:32:50Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.937300 | 2026-09-04T09:32:50Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378200 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.929500 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1a | Windows | 0.333800 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.689300 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1b | Windows | 0.320200 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.572700 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1c | Windows | 0.317200 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.476200 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1d | Windows | 0.317900 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.508900 | 2026-09-04T09:32:50Z |
| us-east-1 | us-east-1f | Windows | 0.316600 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.452700 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.452700 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.452700 | 2026-09-04T09:32:50Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.562800 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.521900 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.525200 | 2026-09-04T09:32:50Z |
| us-west-2 | us-west-2c | Windows | 0.332300 | 2026-09-04T09:32:50Z |
