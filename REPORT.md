# Spot placement score log

Generated 2026-09-23 05:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 151 | 0% | 2.0 | 3 (09-23 05:52Z) |
| ap-northeast-1 | 151 | 0% | 1.9 | 2 (09-23 05:52Z) |
| ap-northeast-2 | 151 | 0% | 3.0 | 3 (09-23 05:52Z) |
| ap-south-1 | 151 | 0% | 2.0 | 1 (09-23 05:52Z) |
| ap-southeast-2 | 151 | 0% | 1.0 | 1 (09-23 05:52Z) |
| ap-southeast-3 | 151 | 0% | 2.5 | 3 (09-23 05:52Z) |
| us-east-1 | 151 | 0% | 2.0 | 3 (09-23 05:52Z) |
| us-east-2 | 151 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-west-2 | 151 | 0% | 1.7 | 1 (09-23 05:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   321132212222112222111221223322312322112122133222
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       331111121122111333311312113333333333211111111111
ap-southeast-2   111111111111111111111111111111111111111311111111
ap-southeast-3   133131331333331313112333333333331333313331333333
us-east-1        222122113112123223123111213112233333333132122323
us-east-2        111111113131333333313311333312333333133111121131
us-west-2        111211121111113122131112333333333333333121122221
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 1 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 93 | 0% | 2.4 | 3 (09-23 05:52Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 67 | 0% | 2.3 | 3 (09-20 15:58Z) |
| ap-northeast-2 apne2-az1 | 134 | 0% | 2.9 | 3 (09-23 05:52Z) |
| ap-northeast-2 apne2-az3 | 133 | 0% | 2.9 | 3 (09-23 05:52Z) |
| ap-northeast-2 apne2-az4 | 148 | 0% | 3.0 | 3 (09-23 05:52Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 30 | 0% | 1.0 | 1 (09-22 22:01Z) |
| ap-southeast-3 apse3-az3 | 116 | 0% | 2.9 | 3 (09-23 05:52Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 51 | 0% | 1.4 | 1 (09-22 22:01Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 46 | 0% | 1.6 | 1 (09-22 18:48Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 51 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-east-2 use2-az2 | 62 | 0% | 2.0 | 3 (09-23 00:22Z) |
| us-east-2 use2-az3 | 81 | 0% | 2.3 | 3 (09-23 00:22Z) |
| us-west-2 usw2-az1 | 45 | 0% | 2.1 | 1 (09-23 00:22Z) |
| us-west-2 usw2-az2 | 27 | 0% | 2.0 | 3 (09-19 20:33Z) |
| us-west-2 usw2-az3 | 78 | 0% | 1.8 | 1 (09-23 05:52Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 151 | 0% | 3.0 | 3 (09-23 05:52Z) |
| ap-northeast-1 | 151 | 79% | 7.6 | 9 (09-23 05:52Z) |
| ap-northeast-2 | 151 | 100% | 9.0 | 9 (09-23 05:52Z) |
| ap-south-1 | 151 | 46% | 5.6 | 8 (09-23 05:52Z) |
| ap-southeast-2 | 151 | 7% | 2.6 | 2 (09-23 05:52Z) |
| ap-southeast-3 | 151 | 0% | 2.5 | 3 (09-23 05:52Z) |
| us-east-1 | 151 | 75% | 6.9 | 9 (09-23 05:52Z) |
| us-east-2 | 151 | 76% | 7.3 | 9 (09-23 05:52Z) |
| us-west-2 | 151 | 53% | 5.8 | 9 (09-23 05:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   993399924999419999339999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999189999299993999923999999999999999991999249998
ap-southeast-2   222222222332223322223323333333333333223312222222
ap-southeast-3   133131331333331313112333333333331333313331333333
us-east-1        368443249395599569999454999999999999999499944599
us-east-2        999992129999999999999911999919999999999339959999
us-west-2        342543353441399445953345999999999999999431954549
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 5 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 5 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 6 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 5 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 7 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 3.0 | 3 (09-23 00:22Z) |
| ap-east-1 ape1-az2 | 40 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-east-1 ape1-az3 | 44 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az1 | 81 | 90% | 8.4 | 9 (09-23 05:52Z) |
| ap-northeast-1 apne1-az2 | 26 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az4 | 104 | 100% | 9.0 | 9 (09-23 00:22Z) |
| ap-northeast-2 apne2-az1 | 137 | 100% | 9.0 | 9 (09-23 05:52Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 137 | 100% | 9.0 | 9 (09-23 05:52Z) |
| ap-northeast-2 apne2-az4 | 47 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-south-1 aps1-az1 | 48 | 54% | 6.2 | 9 (09-23 00:22Z) |
| ap-south-1 aps1-az2 | 36 | 0% | 3.0 | 3 (09-22 18:48Z) |
| ap-south-1 aps1-az3 | 65 | 72% | 7.4 | 9 (09-23 00:22Z) |
| ap-southeast-2 apse2-az1 | 12 | 25% | 4.3 | 3 (09-21 19:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 40 | 0% | 3.0 | 3 (09-22 14:44Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 30 | 97% | 8.8 | 9 (09-23 00:22Z) |
| us-east-1 use1-az6 | 61 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-2 use2-az1 | 61 | 98% | 8.9 | 9 (09-23 00:22Z) |
| us-east-2 use2-az2 | 95 | 98% | 8.8 | 9 (09-23 05:52Z) |
| us-east-2 use2-az3 | 79 | 90% | 8.3 | 9 (09-23 05:52Z) |
| us-west-2 usw2-az1 | 50 | 98% | 8.9 | 9 (09-21 13:58Z) |
| us-west-2 usw2-az2 | 41 | 98% | 8.8 | 9 (09-23 05:52Z) |
| us-west-2 usw2-az3 | 57 | 98% | 8.9 | 9 (09-23 05:52Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.728100 | 2026-09-23T05:52:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.863900 | 2026-09-23T05:52:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.853800 | 2026-09-23T05:52:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.036800 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592000 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579600 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.569000 | 2026-09-23T05:52:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-23T05:52:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.483500 | 2026-09-23T05:52:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.334200 | 2026-09-23T05:52:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.452600 | 2026-09-23T05:52:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.310300 | 2026-09-23T05:52:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.663900 | 2026-09-23T05:52:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.534000 | 2026-09-23T05:52:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.781300 | 2026-09-23T05:52:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.787600 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1a | Windows | 0.345800 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.586300 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1b | Windows | 0.295800 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.471700 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1c | Windows | 0.287600 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.462800 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1d | Windows | 0.294000 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.454500 | 2026-09-23T05:52:46Z |
| us-east-1 | us-east-1f | Windows | 0.301300 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526000 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2a | Windows | 0.641100 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524600 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.511900 | 2026-09-23T05:52:46Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.516200 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2a | Windows | 0.336400 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.481200 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2b | Windows | 0.334400 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.483600 | 2026-09-23T05:52:46Z |
| us-west-2 | us-west-2c | Windows | 0.335100 | 2026-09-23T05:52:46Z |
