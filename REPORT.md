# Spot placement score log

Generated 2026-09-06 23:47 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 59 | 0% | 1.0 | 1 (09-06 23:47Z) |
| ap-northeast-1 | 59 | 0% | 1.8 | 1 (09-06 23:47Z) |
| ap-northeast-2 | 59 | 0% | 2.9 | 3 (09-06 23:47Z) |
| ap-south-1 | 59 | 0% | 2.2 | 1 (09-06 23:47Z) |
| ap-southeast-2 | 59 | 0% | 1.0 | 1 (09-06 23:47Z) |
| ap-southeast-3 | 59 | 0% | 2.5 | 3 (09-06 23:47Z) |
| us-east-1 | 59 | 0% | 1.8 | 3 (09-06 23:47Z) |
| us-east-2 | 59 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-west-2 | 59 | 0% | 1.5 | 1 (09-06 23:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111111111111111
ap-northeast-1   331311113111111111311211112211311333311333331221
ap-northeast-2   333333333333333113333333333333333333333333333333
ap-south-1       331333311131113122213322113332233333323333111211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   321113211233333333333331313131333333331133333333
us-east-1        111111312111111111111112212333211313233332323233
us-east-2        113311111111111113111111111111111111311111331111
us-west-2        111313331111111111111211122222222222111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 2 | 2 | · | 2 | 2 | 3 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 2 | 2 | · | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 2 | · | 1 | · | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 2 | 2 | · | 3 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 2 | 1 | · | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 21 | 0% | 1.0 | 1 (09-06 04:28Z) |
| ap-east-1 ape1-az2 | 17 | 0% | 1.0 | 1 (09-06 23:47Z) |
| ap-northeast-1 apne1-az1 | 11 | 0% | 1.2 | 1 (09-06 09:20Z) |
| ap-northeast-1 apne1-az4 | 35 | 0% | 2.1 | 3 (09-06 13:37Z) |
| ap-northeast-2 apne2-az1 | 55 | 0% | 3.0 | 3 (09-06 23:47Z) |
| ap-northeast-2 apne2-az3 | 55 | 0% | 2.9 | 3 (09-06 23:47Z) |
| ap-northeast-2 apne2-az4 | 58 | 0% | 3.0 | 3 (09-06 23:47Z) |
| ap-south-1 aps1-az1 | 24 | 0% | 1.8 | 1 (09-06 21:17Z) |
| ap-south-1 aps1-az3 | 38 | 0% | 2.7 | 1 (09-06 13:37Z) |
| ap-southeast-2 apse2-az1 | 12 | 0% | 1.0 | 1 (09-06 13:37Z) |
| ap-southeast-2 apse2-az2 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 48 | 0% | 2.9 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 12 | 0% | 1.0 | 1 (09-06 23:47Z) |
| us-east-1 use1-az2 | 21 | 0% | 1.1 | 1 (09-05 23:49Z) |
| us-east-1 use1-az4 | 13 | 0% | 1.3 | 1 (09-06 23:47Z) |
| us-east-1 use1-az5 | 17 | 0% | 1.2 | 1 (09-06 04:28Z) |
| us-east-1 use1-az6 | 28 | 0% | 1.1 | 1 (09-06 23:47Z) |
| us-east-2 use2-az1 | 11 | 0% | 1.2 | 1 (09-06 21:17Z) |
| us-east-2 use2-az2 | 20 | 0% | 1.3 | 1 (09-06 21:17Z) |
| us-east-2 use2-az3 | 19 | 0% | 1.8 | 1 (09-06 21:17Z) |
| us-west-2 usw2-az1 | 12 | 0% | 1.5 | 1 (09-06 04:28Z) |
| us-west-2 usw2-az2 | 9 | 0% | 1.2 | 1 (09-06 09:20Z) |
| us-west-2 usw2-az3 | 29 | 0% | 1.3 | 1 (09-06 23:47Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 59 | 0% | 3.0 | 3 (09-06 23:47Z) |
| ap-northeast-1 | 59 | 83% | 7.7 | 9 (09-06 23:47Z) |
| ap-northeast-2 | 59 | 100% | 9.0 | 9 (09-06 23:47Z) |
| ap-south-1 | 59 | 0% | 2.8 | 3 (09-06 23:47Z) |
| ap-southeast-2 | 59 | 17% | 3.1 | 1 (09-06 23:47Z) |
| ap-southeast-3 | 59 | 0% | 2.5 | 3 (09-06 23:47Z) |
| us-east-1 | 59 | 73% | 6.4 | 9 (09-06 23:47Z) |
| us-east-2 | 59 | 64% | 6.5 | 9 (09-06 23:47Z) |
| us-west-2 | 59 | 47% | 5.4 | 7 (09-06 23:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999919911999911999921999912999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333313331133333333332233333333333333333333333
ap-southeast-2   999993111111231111131111333111331333333333333331
ap-southeast-3   321113211233333333333331313131333333331133333333
us-east-1        999999994119112199211399433565425659959999999999
us-east-2        919922191119999999911399333239338299999999999999
us-west-2        229999999129924492921242944344534544998589699997
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 3 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 3 | · | 1 | · | 6 | 2 | · | 5 | 2 | 3 | 3 | 2 | 6 | 3 | 4 | 6 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 2 | 2 | · | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 5 | 9 | 5 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 6 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 7 | 5 | 9 | 9 | 4 | 9 | 5 | 6 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 6 | 4 | · | 9 | 9 | 9 | 7 | 9 | 6 | 2 | 5 | 6 | 2 | 5 | 3 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 18 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 24 | 67% | 7.0 | 9 (09-06 23:47Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 46 | 100% | 9.0 | 9 (09-06 23:47Z) |
| ap-northeast-2 apne2-az1 | 56 | 100% | 9.0 | 9 (09-06 23:47Z) |
| ap-northeast-2 apne2-az2 | 6 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-northeast-2 apne2-az3 | 56 | 100% | 9.0 | 9 (09-06 23:47Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 11 | 0% | 3.0 | 3 (09-05 15:59Z) |
| ap-south-1 aps1-az2 | 22 | 0% | 3.0 | 3 (09-05 04:17Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 21 | 0% | 3.0 | 3 (09-06 23:47Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 21 | 100% | 9.0 | 9 (09-06 23:47Z) |
| us-east-1 use1-az4 | 22 | 100% | 9.0 | 9 (09-06 21:17Z) |
| us-east-1 use1-az5 | 22 | 100% | 9.0 | 9 (09-06 16:56Z) |
| us-east-1 use1-az6 | 23 | 100% | 9.0 | 9 (09-06 23:47Z) |
| us-east-2 use2-az1 | 22 | 100% | 9.0 | 9 (09-06 23:47Z) |
| us-east-2 use2-az2 | 35 | 94% | 8.6 | 9 (09-06 23:47Z) |
| us-east-2 use2-az3 | 17 | 59% | 6.3 | 3 (09-06 23:47Z) |
| us-west-2 usw2-az1 | 19 | 95% | 8.7 | 9 (09-06 21:17Z) |
| us-west-2 usw2-az2 | 13 | 100% | 9.0 | 9 (09-06 21:17Z) |
| us-west-2 usw2-az3 | 19 | 95% | 8.6 | 9 (09-06 19:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.751900 | 2026-09-06T23:47:48Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-06T23:47:48Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.782100 | 2026-09-06T23:47:48Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.954000 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.598300 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.584200 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.579500 | 2026-09-06T23:47:48Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-06T23:47:48Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.550400 | 2026-09-06T23:47:48Z |
| ap-south-1 | ap-south-1a | Windows | 0.325700 | 2026-09-06T23:47:48Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.486700 | 2026-09-06T23:47:48Z |
| ap-south-1 | ap-south-1b | Windows | 0.325000 | 2026-09-06T23:47:48Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.739100 | 2026-09-06T23:47:48Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.484400 | 2026-09-06T23:47:48Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.920900 | 2026-09-06T23:47:48Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.392500 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.910700 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1a | Windows | 0.335100 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.654400 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1b | Windows | 0.318100 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.554100 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1c | Windows | 0.315000 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.468600 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1d | Windows | 0.316100 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.502700 | 2026-09-06T23:47:48Z |
| us-east-1 | us-east-1f | Windows | 0.314800 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.497600 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.501800 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2b | Windows | 0.636800 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.511400 | 2026-09-06T23:47:48Z |
| us-east-2 | us-east-2c | Windows | 0.636900 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.552100 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2a | Windows | 0.296800 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.519100 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2b | Windows | 0.304000 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.517200 | 2026-09-06T23:47:48Z |
| us-west-2 | us-west-2c | Windows | 0.334900 | 2026-09-06T23:47:48Z |
