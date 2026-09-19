# Spot placement score log

Generated 2026-09-19 14:20 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 130 | 0% | 1.8 | 3 (09-19 14:20Z) |
| ap-northeast-1 | 130 | 0% | 1.9 | 3 (09-19 14:20Z) |
| ap-northeast-2 | 130 | 0% | 3.0 | 3 (09-19 14:20Z) |
| ap-south-1 | 130 | 0% | 2.0 | 3 (09-19 14:20Z) |
| ap-southeast-2 | 130 | 0% | 1.0 | 1 (09-19 14:20Z) |
| ap-southeast-3 | 130 | 0% | 2.5 | 3 (09-19 14:20Z) |
| us-east-1 | 130 | 0% | 1.9 | 3 (09-19 14:20Z) |
| us-east-2 | 130 | 0% | 1.8 | 3 (09-19 14:20Z) |
| us-west-2 | 130 | 0% | 1.5 | 3 (09-19 14:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   123323333333333333223321132212222112222111221223
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       121111333333313333333331111121122111333311312113
ap-southeast-2   111311111111111111111111111111111111111111111111
ap-southeast-3   333333333333333333313133131331333331313112333333
us-east-1        131133223311323233222222122113112123223123111213
us-east-2        131311333333333333333111111113131333333313311333
us-west-2        111111133313313333333111211121111113122131112333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 35 | 0% | 1.2 | 3 (09-19 14:20Z) |
| ap-east-1 ape1-az2 | 74 | 0% | 2.3 | 3 (09-19 10:50Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 64 | 0% | 2.2 | 1 (09-18 21:36Z) |
| ap-northeast-2 apne2-az1 | 118 | 0% | 2.9 | 3 (09-19 14:20Z) |
| ap-northeast-2 apne2-az3 | 116 | 0% | 2.9 | 3 (09-19 14:20Z) |
| ap-northeast-2 apne2-az4 | 127 | 0% | 3.0 | 3 (09-19 14:20Z) |
| ap-south-1 aps1-az1 | 53 | 0% | 1.7 | 2 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 69 | 0% | 2.6 | 3 (09-19 14:20Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 100 | 0% | 2.9 | 3 (09-19 14:20Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 39 | 0% | 1.1 | 1 (09-18 21:36Z) |
| us-east-1 use1-az4 | 26 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az5 | 37 | 0% | 1.4 | 3 (09-19 14:20Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 43 | 0% | 1.7 | 3 (09-19 10:50Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 71 | 0% | 2.3 | 3 (09-19 10:50Z) |
| us-west-2 usw2-az1 | 36 | 0% | 1.9 | 3 (09-19 14:20Z) |
| us-west-2 usw2-az2 | 25 | 0% | 1.9 | 3 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 65 | 0% | 1.6 | 3 (09-19 14:20Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 130 | 0% | 3.0 | 3 (09-19 14:20Z) |
| ap-northeast-1 | 130 | 76% | 7.4 | 9 (09-19 14:20Z) |
| ap-northeast-2 | 130 | 100% | 9.0 | 9 (09-19 14:20Z) |
| ap-south-1 | 130 | 39% | 5.2 | 9 (09-19 14:20Z) |
| ap-southeast-2 | 130 | 8% | 2.6 | 3 (09-19 14:20Z) |
| ap-southeast-3 | 130 | 0% | 2.5 | 3 (09-19 14:20Z) |
| us-east-1 | 130 | 73% | 6.7 | 9 (09-19 14:20Z) |
| us-east-2 | 130 | 75% | 7.2 | 9 (09-19 14:20Z) |
| us-west-2 | 130 | 49% | 5.5 | 9 (09-19 14:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   349999999999999999649993399924999419999339999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       939999999999999999999999189999299993999923999999
ap-southeast-2   233333333333322332222222222222332223322223323333
ap-southeast-3   333333333333333333313133131331333331313112333333
us-east-1        992349999999999999994368443249395599569999454999
us-east-2        991919999999999999999999992129999999999999911999
us-west-2        423353999999999999999342543353441399445953345999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 3 | 4 | 9 | 3 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 3 | 6 | 6 | 6 | 6 | 4 | 5 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 5 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 7 | 6 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 66 | 88% | 8.3 | 9 (09-19 00:13Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 86 | 100% | 9.0 | 9 (09-19 14:20Z) |
| ap-northeast-2 apne2-az1 | 119 | 100% | 9.0 | 9 (09-19 14:20Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 120 | 100% | 9.0 | 9 (09-19 14:20Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 38 | 42% | 5.5 | 9 (09-19 10:50Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 52 | 65% | 6.9 | 9 (09-19 00:13Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 50 | 100% | 9.0 | 9 (09-19 14:20Z) |
| us-east-1 use1-az4 | 53 | 96% | 8.7 | 9 (09-19 14:20Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 51 | 100% | 9.0 | 9 (09-19 14:20Z) |
| us-east-2 use2-az1 | 52 | 100% | 9.0 | 9 (09-19 10:50Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 65 | 88% | 8.2 | 9 (09-19 14:20Z) |
| us-west-2 usw2-az1 | 43 | 98% | 8.9 | 9 (09-19 14:20Z) |
| us-west-2 usw2-az2 | 32 | 97% | 8.7 | 9 (09-19 14:20Z) |
| us-west-2 usw2-az3 | 44 | 98% | 8.8 | 9 (09-19 14:20Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.712700 | 2026-09-19T14:20:36Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-19T14:20:36Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.841400 | 2026-09-19T14:20:36Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.024300 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588600 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579000 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565800 | 2026-09-19T14:20:36Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742700 | 2026-09-19T14:20:36Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.503100 | 2026-09-19T14:20:36Z |
| ap-south-1 | ap-south-1a | Windows | 0.310000 | 2026-09-19T14:20:36Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.456300 | 2026-09-19T14:20:36Z |
| ap-south-1 | ap-south-1b | Windows | 0.317100 | 2026-09-19T14:20:36Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.687700 | 2026-09-19T14:20:36Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509600 | 2026-09-19T14:20:36Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.856400 | 2026-09-19T14:20:36Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556200 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.840100 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1a | Windows | 0.347300 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.624300 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1b | Windows | 0.315900 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.507100 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1c | Windows | 0.294700 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.526300 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1d | Windows | 0.309100 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.513700 | 2026-09-19T14:20:36Z |
| us-east-1 | us-east-1f | Windows | 0.318400 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.521600 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2a | Windows | 0.641500 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.521700 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2b | Windows | 0.640000 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515600 | 2026-09-19T14:20:36Z |
| us-east-2 | us-east-2c | Windows | 0.638300 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.569600 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2a | Windows | 0.339800 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.525900 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2b | Windows | 0.336400 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.526400 | 2026-09-19T14:20:36Z |
| us-west-2 | us-west-2c | Windows | 0.337200 | 2026-09-19T14:20:36Z |
