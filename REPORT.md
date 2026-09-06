# Spot placement score log

Generated 2026-09-06 04:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 53 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-northeast-1 | 53 | 0% | 1.7 | 3 (09-06 04:28Z) |
| ap-northeast-2 | 53 | 0% | 2.9 | 3 (09-06 04:28Z) |
| ap-south-1 | 53 | 0% | 2.4 | 3 (09-06 04:28Z) |
| ap-southeast-2 | 53 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-southeast-3 | 53 | 0% | 2.5 | 3 (09-06 04:28Z) |
| us-east-1 | 53 | 0% | 1.7 | 2 (09-06 04:28Z) |
| us-east-2 | 53 | 0% | 1.2 | 1 (09-06 04:28Z) |
| us-west-2 | 53 | 0% | 1.5 | 1 (09-06 04:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   133331331311113111111111311211112211311333311333
ap-northeast-2   333333333333333333333113333333333333333333333333
ap-south-1       133333331333311131113122213322113332233333323333
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333232321113211233333333333331313131333333331133
us-east-1        211113111111312111111111111112212333211313233332
us-east-2        311311113311111111111113111111111111111111311111
us-west-2        211311111313331111111111111211122222222222111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | · | 2 | 2 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 21 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-east-1 ape1-az2 | 13 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az1 | 10 | 0% | 1.2 | 1 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 33 | 0% | 2.1 | 3 (09-06 04:28Z) |
| ap-northeast-2 apne2-az1 | 49 | 0% | 3.0 | 3 (09-06 04:28Z) |
| ap-northeast-2 apne2-az3 | 49 | 0% | 2.9 | 3 (09-06 04:28Z) |
| ap-northeast-2 apne2-az4 | 52 | 0% | 3.0 | 3 (09-06 04:28Z) |
| ap-south-1 aps1-az1 | 23 | 0% | 1.8 | 1 (09-05 23:49Z) |
| ap-south-1 aps1-az3 | 37 | 0% | 2.8 | 3 (09-06 04:28Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 8 | 0% | 1.0 | 1 (09-05 08:59Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 42 | 0% | 2.9 | 3 (09-06 04:28Z) |
| us-east-1 use1-az1 | 9 | 0% | 1.0 | 1 (09-05 08:59Z) |
| us-east-1 use1-az2 | 21 | 0% | 1.1 | 1 (09-05 23:49Z) |
| us-east-1 use1-az4 | 10 | 0% | 1.4 | 1 (09-05 08:59Z) |
| us-east-1 use1-az5 | 17 | 0% | 1.2 | 1 (09-06 04:28Z) |
| us-east-1 use1-az6 | 24 | 0% | 1.2 | 1 (09-05 23:49Z) |
| us-east-2 use2-az1 | 10 | 0% | 1.2 | 1 (09-05 21:09Z) |
| us-east-2 use2-az2 | 17 | 0% | 1.1 | 1 (09-05 21:09Z) |
| us-east-2 use2-az3 | 16 | 0% | 1.7 | 1 (09-06 04:28Z) |
| us-west-2 usw2-az1 | 12 | 0% | 1.5 | 1 (09-06 04:28Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 25 | 0% | 1.3 | 1 (09-05 23:49Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 53 | 0% | 3.0 | 3 (09-06 04:28Z) |
| ap-northeast-1 | 53 | 81% | 7.5 | 9 (09-06 04:28Z) |
| ap-northeast-2 | 53 | 100% | 9.0 | 9 (09-06 04:28Z) |
| ap-south-1 | 53 | 0% | 2.8 | 3 (09-06 04:28Z) |
| ap-southeast-2 | 53 | 19% | 3.1 | 3 (09-06 04:28Z) |
| ap-southeast-3 | 53 | 0% | 2.5 | 3 (09-06 04:28Z) |
| us-east-1 | 53 | 70% | 6.1 | 9 (09-06 04:28Z) |
| us-east-2 | 53 | 60% | 6.2 | 9 (09-06 04:28Z) |
| us-west-2 | 53 | 42% | 5.1 | 9 (09-06 04:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999919911999911999921999912999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333313331133333333332233333333333333333
ap-southeast-2   197999999993111111231111131111333111331333333333
ap-southeast-3   333232321113211233333333333331313131333333331133
us-east-1        758999999999994119112199211399433565425659959999
us-east-2        929999919922191119999999911399333239338299999999
us-west-2        921922229999999129924492921242944344534544998589
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 2 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 6 | 1 | · | 5 | 2 | · | 3 | 2 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | · | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 5 | · | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 6 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 5 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 5 | 2 | 2 | 4 | 3 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 19 | 58% | 6.5 | 9 (09-05 23:49Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 40 | 100% | 9.0 | 9 (09-05 23:49Z) |
| ap-northeast-2 apne2-az1 | 51 | 100% | 9.0 | 9 (09-05 23:49Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 51 | 100% | 9.0 | 9 (09-06 04:28Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 3 | 100% | 8.0 | 9 (09-06 04:28Z) |
| us-east-1 use1-az2 | 16 | 100% | 8.9 | 9 (09-06 04:28Z) |
| us-east-1 use1-az4 | 17 | 100% | 9.0 | 9 (09-06 04:28Z) |
| us-east-1 use1-az5 | 19 | 100% | 8.9 | 9 (09-05 23:49Z) |
| us-east-1 use1-az6 | 17 | 100% | 9.0 | 9 (09-06 04:28Z) |
| us-east-2 use2-az1 | 19 | 100% | 8.9 | 9 (09-06 04:28Z) |
| us-east-2 use2-az2 | 29 | 93% | 8.5 | 9 (09-06 04:28Z) |
| us-east-2 use2-az3 | 16 | 62% | 6.5 | 9 (09-05 04:17Z) |
| us-west-2 usw2-az1 | 15 | 93% | 8.6 | 9 (09-06 04:28Z) |
| us-west-2 usw2-az2 | 12 | 100% | 9.0 | 9 (09-06 04:28Z) |
| us-west-2 usw2-az3 | 16 | 94% | 8.6 | 9 (09-06 04:28Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.753100 | 2026-09-06T04:28:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-06T04:28:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.782100 | 2026-09-06T04:28:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.932200 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591300 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.575300 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579900 | 2026-09-06T04:28:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-06T04:28:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.552300 | 2026-09-06T04:28:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.318800 | 2026-09-06T04:28:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.494800 | 2026-09-06T04:28:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.324100 | 2026-09-06T04:28:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746400 | 2026-09-06T04:28:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.479700 | 2026-09-06T04:28:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.930300 | 2026-09-06T04:28:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.382000 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.912900 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1a | Windows | 0.333100 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.662500 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1b | Windows | 0.318100 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.559800 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1c | Windows | 0.315000 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.468300 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1d | Windows | 0.316200 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.500400 | 2026-09-06T04:28:00Z |
| us-east-1 | us-east-1f | Windows | 0.314700 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.478300 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.493500 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.484100 | 2026-09-06T04:28:00Z |
| us-east-2 | us-east-2c | Windows | 0.636800 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.554600 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2a | Windows | 0.292500 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.517200 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2b | Windows | 0.298900 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.517200 | 2026-09-06T04:28:00Z |
| us-west-2 | us-west-2c | Windows | 0.334100 | 2026-09-06T04:28:00Z |
