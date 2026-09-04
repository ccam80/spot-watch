# Spot placement score log

Generated 2026-09-04 23:58 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 45 | 0% | 1.0 | 1 (09-04 23:58Z) |
| ap-northeast-1 | 45 | 0% | 1.6 | 3 (09-04 23:58Z) |
| ap-northeast-2 | 45 | 0% | 2.9 | 3 (09-04 23:58Z) |
| ap-south-1 | 45 | 0% | 2.3 | 3 (09-04 23:58Z) |
| ap-southeast-2 | 45 | 0% | 1.0 | 1 (09-04 23:58Z) |
| ap-southeast-3 | 45 | 0% | 2.5 | 3 (09-04 23:58Z) |
| us-east-1 | 45 | 0% | 1.6 | 3 (09-04 23:58Z) |
| us-east-2 | 45 | 0% | 1.2 | 1 (09-04 23:58Z) |
| us-west-2 | 45 | 0% | 1.6 | 2 (09-04 23:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1           111111111111111111111111111111111111111111111
ap-northeast-1      111311333313313111131111111113112111122113113
ap-northeast-2      333333333333333333333333331133333333333333333
ap-south-1          333131333333313333111311131222133221133322333
ap-southeast-2      111111111111111111111111111111111111111111111
ap-southeast-3      333333332323211132112333333333333313131313333
us-east-1           323332111131111113121111111111111122123332113
us-east-2           111113113111133111111111111131111111111111111
us-west-2           221222113111113133311111111111112111222222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
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
| ap-northeast-1 apne1-az4 | 27 | 0% | 1.9 | 3 (09-04 23:58Z) |
| ap-northeast-2 apne2-az1 | 41 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-2 apne2-az3 | 41 | 0% | 2.9 | 3 (09-04 23:58Z) |
| ap-northeast-2 apne2-az4 | 44 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 17 | 0% | 1.8 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az3 | 29 | 0% | 2.7 | 3 (09-04 23:58Z) |
| ap-southeast-2 apse2-az1 | 11 | 0% | 1.0 | 1 (09-04 18:19Z) |
| ap-southeast-2 apse2-az2 | 7 | 0% | 1.0 | 1 (09-04 23:58Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 36 | 0% | 2.8 | 3 (09-04 23:58Z) |
| us-east-1 use1-az1 | 8 | 0% | 1.0 | 1 (09-04 23:58Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 9 | 0% | 1.4 | 1 (09-04 23:58Z) |
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
| ap-east-1 | 45 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 | 45 | 78% | 7.3 | 9 (09-04 23:58Z) |
| ap-northeast-2 | 45 | 100% | 9.0 | 9 (09-04 23:58Z) |
| ap-south-1 | 45 | 0% | 2.8 | 3 (09-04 23:58Z) |
| ap-southeast-2 | 45 | 22% | 3.2 | 3 (09-04 23:58Z) |
| ap-southeast-3 | 45 | 0% | 2.5 | 3 (09-04 23:58Z) |
| us-east-1 | 45 | 64% | 5.8 | 6 (09-04 23:58Z) |
| us-east-2 | 45 | 53% | 5.7 | 2 (09-04 23:58Z) |
| us-west-2 | 45 | 36% | 4.8 | 5 (09-04 23:58Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1           333333333333333333333333333333333333333333333
ap-northeast-1      991999999999999999199119999119999219999129999
ap-northeast-2      999999999999999999999999999999999999999999999
ap-south-1          333133333333333333133311333333333322333333333
ap-southeast-2      111111979999999931111112311111311113331113313
ap-southeast-3      333333332323211132112333333333333313131313333
us-east-1           766787589999999999941191121992113994335654256
us-east-2           929919299999199221911199999999113993332393382
us-west-2           442439219222299999991299244929212429443445345
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 3 | 1 | 9 | 3 | 4 | 9 | 1 | 2 | 6 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 1 | · | 5 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 1 | 9 | 9 | 2 | 9 | 5 | 5 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 9 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 4 | 2 | 2 | 4 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-east-1 ape1-az2 | 17 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-east-1 ape1-az3 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az1 | 12 | 33% | 5.0 | 3 (09-04 23:58Z) |
| ap-northeast-1 apne1-az2 | 16 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-northeast-1 apne1-az4 | 33 | 100% | 9.0 | 9 (09-04 23:58Z) |
| ap-northeast-2 apne2-az1 | 44 | 100% | 9.0 | 9 (09-04 23:58Z) |
| ap-northeast-2 apne2-az2 | 5 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az3 | 44 | 100% | 9.0 | 9 (09-04 23:58Z) |
| ap-northeast-2 apne2-az4 | 23 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az1 | 10 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-south-1 aps1-az2 | 21 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-south-1 aps1-az3 | 12 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 5 | 0% | 3.0 | 3 (09-04 23:58Z) |
| ap-southeast-3 apse3-az3 | 20 | 0% | 3.0 | 3 (09-04 23:58Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.754400 | 2026-09-04T23:58:16Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-04T23:58:16Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.803900 | 2026-09-04T23:58:16Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.896200 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.556700 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.556700 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.556700 | 2026-09-04T23:58:16Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-04T23:58:16Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.557600 | 2026-09-04T23:58:16Z |
| ap-south-1 | ap-south-1a | Windows | 0.311900 | 2026-09-04T23:58:16Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.500400 | 2026-09-04T23:58:16Z |
| ap-south-1 | ap-south-1b | Windows | 0.316700 | 2026-09-04T23:58:16Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747000 | 2026-09-04T23:58:16Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.470000 | 2026-09-04T23:58:16Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.933500 | 2026-09-04T23:58:16Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378700 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.925000 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1a | Windows | 0.333700 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.681900 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1b | Windows | 0.319900 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.569300 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1c | Windows | 0.317000 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.472600 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1d | Windows | 0.317700 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.505200 | 2026-09-04T23:58:16Z |
| us-east-1 | us-east-1f | Windows | 0.316400 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.452700 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.459700 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.452700 | 2026-09-04T23:58:16Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561200 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2a | Windows | 0.286300 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.520100 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2b | Windows | 0.288500 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.521800 | 2026-09-04T23:58:16Z |
| us-west-2 | us-west-2c | Windows | 0.332900 | 2026-09-04T23:58:16Z |
