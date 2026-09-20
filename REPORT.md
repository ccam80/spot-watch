# Spot placement score log

Generated 2026-09-20 11:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 136 | 0% | 1.9 | 3 (09-20 11:17Z) |
| ap-northeast-1 | 136 | 0% | 1.9 | 2 (09-20 11:17Z) |
| ap-northeast-2 | 136 | 0% | 3.0 | 3 (09-20 11:17Z) |
| ap-south-1 | 136 | 0% | 2.1 | 3 (09-20 11:17Z) |
| ap-southeast-2 | 136 | 0% | 1.0 | 1 (09-20 11:17Z) |
| ap-southeast-3 | 136 | 0% | 2.5 | 1 (09-20 11:17Z) |
| us-east-1 | 136 | 0% | 1.9 | 3 (09-20 11:17Z) |
| us-east-2 | 136 | 0% | 1.8 | 3 (09-20 11:17Z) |
| us-west-2 | 136 | 0% | 1.6 | 3 (09-20 11:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   333333333333223321132212222112222111221223322312
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       333333313333333331111121122111333311312113333333
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333333333333313133131331333331313112333333333331
us-east-1        223311323233222222122113112123223123111213112233
us-east-2        333333333333333111111113131333333313311333312333
us-west-2        133313313333333111211121111113122131112333333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 1.4 | 3 (09-20 01:00Z) |
| ap-east-1 ape1-az2 | 79 | 0% | 2.3 | 3 (09-20 11:17Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 66 | 0% | 2.2 | 3 (09-20 01:00Z) |
| ap-northeast-2 apne2-az1 | 123 | 0% | 2.9 | 3 (09-20 11:17Z) |
| ap-northeast-2 apne2-az3 | 121 | 0% | 2.9 | 3 (09-20 11:17Z) |
| ap-northeast-2 apne2-az4 | 133 | 0% | 3.0 | 3 (09-20 11:17Z) |
| ap-south-1 aps1-az1 | 54 | 0% | 1.7 | 3 (09-19 22:55Z) |
| ap-south-1 aps1-az3 | 75 | 0% | 2.6 | 3 (09-20 11:17Z) |
| ap-southeast-2 apse2-az1 | 23 | 0% | 1.1 | 1 (09-18 18:21Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 104 | 0% | 2.9 | 3 (09-20 06:06Z) |
| us-east-1 use1-az1 | 16 | 0% | 1.2 | 3 (09-20 11:17Z) |
| us-east-1 use1-az2 | 41 | 0% | 1.2 | 3 (09-20 11:17Z) |
| us-east-1 use1-az4 | 28 | 0% | 1.5 | 3 (09-20 11:17Z) |
| us-east-1 use1-az5 | 38 | 0% | 1.5 | 3 (09-20 06:06Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 44 | 0% | 1.7 | 3 (09-20 01:00Z) |
| us-east-2 use2-az2 | 60 | 0% | 2.0 | 3 (09-19 10:50Z) |
| us-east-2 use2-az3 | 73 | 0% | 2.3 | 3 (09-20 01:00Z) |
| us-west-2 usw2-az1 | 40 | 0% | 2.0 | 3 (09-20 11:17Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 71 | 0% | 1.7 | 3 (09-20 11:17Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 136 | 0% | 3.0 | 3 (09-20 11:17Z) |
| ap-northeast-1 | 136 | 77% | 7.5 | 9 (09-20 11:17Z) |
| ap-northeast-2 | 136 | 100% | 9.0 | 9 (09-20 11:17Z) |
| ap-south-1 | 136 | 42% | 5.3 | 9 (09-20 11:17Z) |
| ap-southeast-2 | 136 | 7% | 2.6 | 3 (09-20 11:17Z) |
| ap-southeast-3 | 136 | 0% | 2.5 | 1 (09-20 11:17Z) |
| us-east-1 | 136 | 74% | 6.8 | 9 (09-20 11:17Z) |
| us-east-2 | 136 | 75% | 7.2 | 9 (09-20 11:17Z) |
| us-west-2 | 136 | 51% | 5.7 | 9 (09-20 11:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999999999999649993399924999419999339999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999189999299993999923999999999999
ap-southeast-2   333333322332222222222222332223322223323333333333
ap-southeast-3   333333333333313133131331333331313112333333333331
us-east-1        999999999999994368443249395599569999454999999999
us-east-2        999999999999999999992129999999999999911999919999
us-west-2        999999999999999342543353441399445953345999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 4 | 4 | 9 | 3 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 7 | 4 | 2 | 6 | 4 | 3 | 6 | 7 | 6 | 6 | 5 | 5 | 7 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 5 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 5 | 8 | 6 | 6 | 5 | 7 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 6 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 6 | 7 | 9 | 6 | 7 | 4 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 50 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-east-1 ape1-az2 | 38 | 0% | 3.0 | 3 (09-18 14:24Z) |
| ap-east-1 ape1-az3 | 42 | 0% | 3.0 | 3 (09-18 21:36Z) |
| ap-northeast-1 apne1-az1 | 69 | 88% | 8.3 | 9 (09-20 11:17Z) |
| ap-northeast-1 apne1-az2 | 24 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-northeast-1 apne1-az4 | 92 | 100% | 9.0 | 9 (09-20 11:17Z) |
| ap-northeast-2 apne2-az1 | 123 | 100% | 9.0 | 9 (09-20 01:00Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 123 | 100% | 9.0 | 9 (09-20 06:06Z) |
| ap-northeast-2 apne2-az4 | 45 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az1 | 41 | 46% | 5.8 | 9 (09-20 11:17Z) |
| ap-south-1 aps1-az2 | 35 | 0% | 3.0 | 3 (09-19 00:13Z) |
| ap-south-1 aps1-az3 | 55 | 67% | 7.1 | 9 (09-20 01:00Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 38 | 0% | 3.0 | 3 (09-18 21:36Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 56 | 100% | 9.0 | 9 (09-20 11:17Z) |
| us-east-1 use1-az4 | 58 | 97% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az5 | 24 | 96% | 8.7 | 9 (09-20 01:00Z) |
| us-east-1 use1-az6 | 54 | 100% | 9.0 | 9 (09-20 06:06Z) |
| us-east-2 use2-az1 | 53 | 100% | 9.0 | 9 (09-20 06:06Z) |
| us-east-2 use2-az2 | 87 | 98% | 8.8 | 9 (09-19 10:50Z) |
| us-east-2 use2-az3 | 69 | 88% | 8.2 | 9 (09-20 11:17Z) |
| us-west-2 usw2-az1 | 47 | 98% | 8.9 | 9 (09-20 11:17Z) |
| us-west-2 usw2-az2 | 38 | 97% | 8.8 | 9 (09-20 11:17Z) |
| us-west-2 usw2-az3 | 50 | 98% | 8.9 | 9 (09-20 11:17Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.717600 | 2026-09-20T11:17:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-20T11:17:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.846100 | 2026-09-20T11:17:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.026700 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589300 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579900 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566100 | 2026-09-20T11:17:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742800 | 2026-09-20T11:17:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.485400 | 2026-09-20T11:17:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.305800 | 2026-09-20T11:17:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.442500 | 2026-09-20T11:17:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.316200 | 2026-09-20T11:17:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686000 | 2026-09-20T11:17:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.520000 | 2026-09-20T11:17:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.844000 | 2026-09-20T11:17:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.559100 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.836100 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1a | Windows | 0.357200 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.622500 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1b | Windows | 0.312200 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.513400 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1c | Windows | 0.291800 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.508000 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1d | Windows | 0.305800 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.501900 | 2026-09-20T11:17:37Z |
| us-east-1 | us-east-1f | Windows | 0.315200 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.522800 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2a | Windows | 0.641700 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.522600 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2b | Windows | 0.642000 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514900 | 2026-09-20T11:17:37Z |
| us-east-2 | us-east-2c | Windows | 0.638100 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568900 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2a | Windows | 0.338900 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526400 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2b | Windows | 0.336100 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527500 | 2026-09-20T11:17:37Z |
| us-west-2 | us-west-2c | Windows | 0.336500 | 2026-09-20T11:17:37Z |
