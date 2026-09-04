# Spot placement score log

Generated 2026-09-04 14:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 42 | 0% | 1.0 | 1 (09-04 14:16Z) |
| ap-northeast-1 | 42 | 0% | 1.6 | 3 (09-04 14:16Z) |
| ap-northeast-2 | 42 | 0% | 2.9 | 3 (09-04 14:16Z) |
| ap-south-1 | 42 | 0% | 2.2 | 2 (09-04 14:16Z) |
| ap-southeast-2 | 42 | 0% | 1.0 | 1 (09-04 14:16Z) |
| ap-southeast-3 | 42 | 0% | 2.5 | 3 (09-04 14:16Z) |
| us-east-1 | 42 | 0% | 1.6 | 2 (09-04 14:16Z) |
| us-east-2 | 42 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-west-2 | 42 | 0% | 1.5 | 2 (09-04 14:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1              111111111111111111111111111111111111111111
ap-northeast-1         111311333313313111131111111113112111122113
ap-northeast-2         333333333333333333333333331133333333333333
ap-south-1             333131333333313333111311131222133221133322
ap-southeast-2         111111111111111111111111111111111111111111
ap-southeast-3         333333332323211132112333333333333313131313
us-east-1              323332111131111113121111111111111122123332
us-east-2              111113113111133111111111111131111111111111
us-west-2              221222113111113133311111111111112111222222
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
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 18 | 0% | 1.0 | 1 (09-04 04:22Z) |
| ap-east-1 ape1-az2 | 12 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-northeast-1 apne1-az1 | 9 | 0% | 1.2 | 1 (09-04 09:32Z) |
| ap-northeast-1 apne1-az4 | 25 | 0% | 1.9 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az1 | 38 | 0% | 2.9 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az3 | 38 | 0% | 2.9 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az4 | 41 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-south-1 aps1-az1 | 15 | 0% | 1.7 | 1 (09-04 14:16Z) |
| ap-south-1 aps1-az3 | 26 | 0% | 2.7 | 1 (09-04 09:32Z) |
| ap-southeast-2 apse2-az1 | 10 | 0% | 1.0 | 1 (09-04 09:32Z) |
| ap-southeast-2 apse2-az2 | 6 | 0% | 1.0 | 1 (09-03 21:40Z) |
| ap-southeast-3 apse3-az1 | 13 | 0% | 1.0 | 1 (09-03 23:59Z) |
| ap-southeast-3 apse3-az3 | 33 | 0% | 2.8 | 3 (09-04 14:16Z) |
| us-east-1 use1-az1 | 7 | 0% | 1.0 | 1 (09-03 14:26Z) |
| us-east-1 use1-az2 | 20 | 0% | 1.1 | 1 (09-03 23:59Z) |
| us-east-1 use1-az4 | 8 | 0% | 1.5 | 1 (09-03 14:26Z) |
| us-east-1 use1-az5 | 14 | 0% | 1.3 | 1 (09-04 09:32Z) |
| us-east-1 use1-az6 | 19 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-east-2 use2-az1 | 6 | 0% | 1.3 | 1 (09-04 14:16Z) |
| us-east-2 use2-az2 | 13 | 0% | 1.2 | 1 (09-04 14:16Z) |
| us-east-2 use2-az3 | 13 | 0% | 1.7 | 1 (09-04 09:32Z) |
| us-west-2 usw2-az1 | 10 | 0% | 1.6 | 1 (09-04 04:22Z) |
| us-west-2 usw2-az2 | 8 | 0% | 1.2 | 1 (09-03 21:40Z) |
| us-west-2 usw2-az3 | 18 | 0% | 1.4 | 1 (09-04 14:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 42 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-northeast-1 | 42 | 76% | 7.1 | 9 (09-04 14:16Z) |
| ap-northeast-2 | 42 | 100% | 9.0 | 9 (09-04 14:16Z) |
| ap-south-1 | 42 | 0% | 2.8 | 3 (09-04 14:16Z) |
| ap-southeast-2 | 42 | 24% | 3.2 | 3 (09-04 14:16Z) |
| ap-southeast-3 | 42 | 0% | 2.5 | 3 (09-04 14:16Z) |
| us-east-1 | 42 | 64% | 5.9 | 4 (09-04 14:16Z) |
| us-east-2 | 42 | 55% | 5.8 | 3 (09-04 14:16Z) |
| us-west-2 | 42 | 36% | 4.9 | 5 (09-04 14:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1              333333333333333333333333333333333333333333
ap-northeast-1         991999999999999999199119999119999219999129
ap-northeast-2         999999999999999999999999999999999999999999
ap-south-1             333133333333333333133311333333333322333333
ap-southeast-2         111111979999999931111112311111311113331113
ap-southeast-3         333333332323211132112333333333333313131313
us-east-1              766787589999999999941191121992113994335654
us-east-2              929919299999199221911199999999113993332393
us-west-2              442439219222299999991299244929212429443445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 3 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 2 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 3 | 1 | 9 | 3 | 5 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 2 | · | 2 | 3 | · | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 8 | · | 8 | 1 | · | 5 | 4 | 9 | 1 | 4 | 9 | 2 | 5 | 7 | 5 |
| us-east-2 | 2 | 1 | · | 9 | 8 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 7 | 1 | 9 | 9 | 2 | 9 | 5 | 4 | 4 | 4 |
| us-west-2 | 4 | 2 | · | 2 | 4 | · | 9 | · | 9 | 3 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 5 | 2 | 2 | 4 | 3 | 3 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 25 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-east-1 ape1-az2 | 17 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-east-1 ape1-az3 | 18 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-northeast-1 apne1-az1 | 10 | 40% | 5.4 | 3 (09-04 14:16Z) |
| ap-northeast-1 apne1-az2 | 15 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-northeast-1 apne1-az4 | 30 | 100% | 9.0 | 9 (09-04 14:16Z) |
| ap-northeast-2 apne2-az1 | 41 | 100% | 9.0 | 9 (09-04 14:16Z) |
| ap-northeast-2 apne2-az2 | 5 | 0% | 3.0 | 3 (09-04 14:16Z) |
| ap-northeast-2 apne2-az3 | 41 | 100% | 9.0 | 9 (09-04 14:16Z) |
| ap-northeast-2 apne2-az4 | 21 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-south-1 aps1-az1 | 9 | 0% | 3.0 | 3 (09-04 04:22Z) |
| ap-south-1 aps1-az2 | 19 | 0% | 3.0 | 3 (09-04 09:32Z) |
| ap-south-1 aps1-az3 | 11 | 0% | 3.0 | 3 (09-04 04:22Z) |
| ap-southeast-2 apse2-az1 | 8 | 38% | 5.0 | 3 (09-04 14:16Z) |
| ap-southeast-2 apse2-az3 | 3 | 0% | 3.0 | 3 (09-04 14:16Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.754400 | 2026-09-04T14:16:43Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-04T14:16:43Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.811000 | 2026-09-04T14:16:43Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.893100 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.556700 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.556700 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.556700 | 2026-09-04T14:16:43Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-04T14:16:43Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.548900 | 2026-09-04T14:16:43Z |
| ap-south-1 | ap-south-1a | Windows | 0.310500 | 2026-09-04T14:16:43Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.497300 | 2026-09-04T14:16:43Z |
| ap-south-1 | ap-south-1b | Windows | 0.312700 | 2026-09-04T14:16:43Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.746500 | 2026-09-04T14:16:43Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.474000 | 2026-09-04T14:16:43Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.937100 | 2026-09-04T14:16:43Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.378200 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.927700 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1a | Windows | 0.333800 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.683400 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1b | Windows | 0.319900 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.570700 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1c | Windows | 0.317200 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.474200 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1d | Windows | 0.317900 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.508900 | 2026-09-04T14:16:43Z |
| us-east-1 | us-east-1f | Windows | 0.316400 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.452700 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.452700 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.452700 | 2026-09-04T14:16:43Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.561600 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.521900 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2b | Windows | 0.286500 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.522300 | 2026-09-04T14:16:43Z |
| us-west-2 | us-west-2c | Windows | 0.332700 | 2026-09-04T14:16:43Z |
