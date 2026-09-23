# Spot placement score log

Generated 2026-09-23 11:25 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 152 | 0% | 2.0 | 3 (09-23 11:25Z) |
| ap-northeast-1 | 152 | 0% | 1.9 | 2 (09-23 11:25Z) |
| ap-northeast-2 | 152 | 0% | 3.0 | 3 (09-23 11:25Z) |
| ap-south-1 | 152 | 0% | 2.0 | 1 (09-23 11:25Z) |
| ap-southeast-2 | 152 | 0% | 1.0 | 1 (09-23 11:25Z) |
| ap-southeast-3 | 152 | 0% | 2.6 | 3 (09-23 11:25Z) |
| us-east-1 | 152 | 0% | 2.0 | 2 (09-23 11:25Z) |
| us-east-2 | 152 | 0% | 1.8 | 1 (09-23 11:25Z) |
| us-west-2 | 152 | 0% | 1.7 | 3 (09-23 11:25Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   211322122221122221112212233223123221121221332222
ap-northeast-2   333333333333333333333333333333333333333333333333
ap-south-1       311111211221113333113121133333333332111111111111
ap-southeast-2   111111111111111111111111111111111111113111111111
ap-southeast-3   331313313333313131123333333333313333133313333333
us-east-1        221221131121232231231112131122333333331321223232
us-east-2        111111131313333333133113333123333331331111211311
us-west-2        112111211111131221311123333333333333331211222213
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
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 43 | 0% | 1.5 | 2 (09-21 13:58Z) |
| ap-east-1 ape1-az2 | 94 | 0% | 2.4 | 3 (09-23 11:25Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 68 | 0% | 2.2 | 1 (09-23 11:25Z) |
| ap-northeast-2 apne2-az1 | 135 | 0% | 2.9 | 3 (09-23 11:25Z) |
| ap-northeast-2 apne2-az3 | 134 | 0% | 2.9 | 3 (09-23 11:25Z) |
| ap-northeast-2 apne2-az4 | 149 | 0% | 3.0 | 3 (09-23 11:25Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 30 | 0% | 1.0 | 1 (09-22 22:01Z) |
| ap-southeast-3 apse3-az3 | 117 | 0% | 2.9 | 3 (09-23 11:25Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 52 | 0% | 1.3 | 1 (09-23 11:25Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 46 | 0% | 1.6 | 1 (09-22 18:48Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 51 | 0% | 1.8 | 1 (09-23 05:52Z) |
| us-east-2 use2-az2 | 62 | 0% | 2.0 | 3 (09-23 00:22Z) |
| us-east-2 use2-az3 | 82 | 0% | 2.3 | 1 (09-23 11:25Z) |
| us-west-2 usw2-az1 | 46 | 0% | 2.1 | 1 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 78 | 0% | 1.8 | 1 (09-23 05:52Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 152 | 0% | 3.0 | 3 (09-23 11:25Z) |
| ap-northeast-1 | 152 | 80% | 7.6 | 9 (09-23 11:25Z) |
| ap-northeast-2 | 152 | 100% | 9.0 | 9 (09-23 11:25Z) |
| ap-south-1 | 152 | 45% | 5.6 | 3 (09-23 11:25Z) |
| ap-southeast-2 | 152 | 7% | 2.6 | 3 (09-23 11:25Z) |
| ap-southeast-3 | 152 | 0% | 2.6 | 3 (09-23 11:25Z) |
| us-east-1 | 152 | 75% | 6.9 | 9 (09-23 11:25Z) |
| us-east-2 | 152 | 76% | 7.3 | 9 (09-23 11:25Z) |
| us-west-2 | 152 | 53% | 5.8 | 9 (09-23 11:25Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   933999249994199993399999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       991899992999939999239999999999999999919992499983
ap-southeast-2   222222223322233222233233333333333332233122222223
ap-southeast-3   331313313333313131123333333333313333133313333333
us-east-1        684432493955995699994549999999999999994999445999
us-east-2        999921299999999999999119999199999999993399599999
us-west-2        425433534413994459533459999999999999994319545499
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
| ap-northeast-1 apne1-az1 | 82 | 90% | 8.4 | 9 (09-23 11:25Z) |
| ap-northeast-1 apne1-az2 | 26 | 0% | 3.0 | 3 (09-22 14:44Z) |
| ap-northeast-1 apne1-az4 | 105 | 100% | 9.0 | 9 (09-23 11:25Z) |
| ap-northeast-2 apne2-az1 | 138 | 100% | 9.0 | 9 (09-23 11:25Z) |
| ap-northeast-2 apne2-az2 | 13 | 0% | 3.0 | 3 (09-18 18:21Z) |
| ap-northeast-2 apne2-az3 | 138 | 100% | 9.0 | 9 (09-23 11:25Z) |
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
| us-east-1 use1-az6 | 62 | 100% | 9.0 | 9 (09-23 11:25Z) |
| us-east-2 use2-az1 | 61 | 98% | 8.9 | 9 (09-23 00:22Z) |
| us-east-2 use2-az2 | 96 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-east-2 use2-az3 | 80 | 90% | 8.3 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727800 | 2026-09-23T11:25:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.864900 | 2026-09-23T11:25:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.852700 | 2026-09-23T11:25:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.035700 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591800 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579600 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568800 | 2026-09-23T11:25:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743200 | 2026-09-23T11:25:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.483500 | 2026-09-23T11:25:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.334200 | 2026-09-23T11:25:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.454500 | 2026-09-23T11:25:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.309000 | 2026-09-23T11:25:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.655100 | 2026-09-23T11:25:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.529000 | 2026-09-23T11:25:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.778200 | 2026-09-23T11:25:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.570600 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.786700 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1a | Windows | 0.343600 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.586100 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1b | Windows | 0.295100 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.464400 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1c | Windows | 0.287600 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.457200 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1d | Windows | 0.292800 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.446000 | 2026-09-23T11:25:49Z |
| us-east-1 | us-east-1f | Windows | 0.301300 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526400 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2a | Windows | 0.641100 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524600 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.511800 | 2026-09-23T11:25:49Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.515900 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2a | Windows | 0.335900 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.481800 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2b | Windows | 0.333900 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.483600 | 2026-09-23T11:25:49Z |
| us-west-2 | us-west-2c | Windows | 0.334500 | 2026-09-23T11:25:49Z |
