# Spot placement score log

Generated 2026-09-28 11:22 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 192 | 15% | 3.0 | 9 (09-28 11:22Z) |
| ap-northeast-1 | 192 | 3% | 2.0 | 1 (09-28 11:22Z) |
| ap-northeast-2 | 192 | 20% | 4.2 | 9 (09-28 11:22Z) |
| ap-south-1 | 192 | 3% | 2.1 | 1 (09-28 11:22Z) |
| ap-southeast-2 | 192 | 0% | 1.0 | 1 (09-28 11:22Z) |
| ap-southeast-3 | 192 | 14% | 3.2 | 8 (09-28 11:22Z) |
| us-east-1 | 192 | 6% | 2.4 | 9 (09-28 11:22Z) |
| us-east-2 | 192 | 17% | 3.0 | 9 (09-28 11:22Z) |
| us-west-2 | 192 | 11% | 2.5 | 9 (09-28 11:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333999999999119199919999998899113991114999
ap-northeast-1   213322223322222211343221555316644442111111111111
ap-northeast-2   333333333999999999999999999999999999999999999999
ap-south-1       111111111111111121111311411115999279134411111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   133333333996899951989158999928699989111111115368
us-east-1        212232322221232113122332239233222299991199999199
us-east-2        112113113192911219928999999999999999999999999999
us-west-2        112222132221122221112199519299129999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 2 | 2 | 5 | 4 | 3 | 4 | 3 | 1 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 2 | 5 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 4 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 56 | 0% | 1.4 | 1 (09-28 09:35Z) |
| ap-east-1 ape1-az2 | 124 | 23% | 3.9 | 9 (09-28 11:22Z) |
| ap-northeast-1 apne1-az1 | 23 | 0% | 1.3 | 2 (09-26 19:48Z) |
| ap-northeast-1 apne1-az4 | 80 | 0% | 2.1 | 3 (09-27 18:17Z) |
| ap-northeast-2 apne2-az1 | 170 | 19% | 4.1 | 9 (09-28 11:22Z) |
| ap-northeast-2 apne2-az3 | 174 | 22% | 4.3 | 9 (09-28 11:22Z) |
| ap-northeast-2 apne2-az4 | 189 | 21% | 4.2 | 9 (09-28 11:22Z) |
| ap-south-1 aps1-az1 | 60 | 2% | 1.8 | 7 (09-27 19:17Z) |
| ap-south-1 aps1-az3 | 87 | 3% | 2.7 | 1 (09-28 02:38Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 143 | 17% | 3.8 | 6 (09-28 10:26Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 59 | 3% | 1.6 | 9 (09-28 04:30Z) |
| us-east-1 use1-az4 | 49 | 24% | 3.4 | 9 (09-28 11:22Z) |
| us-east-1 use1-az5 | 60 | 17% | 2.8 | 9 (09-28 11:22Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 68 | 24% | 3.4 | 9 (09-28 08:38Z) |
| us-east-2 use2-az2 | 97 | 28% | 3.9 | 9 (09-28 11:22Z) |
| us-east-2 use2-az3 | 116 | 26% | 3.9 | 9 (09-28 11:22Z) |
| us-west-2 usw2-az1 | 70 | 29% | 3.9 | 9 (09-28 09:35Z) |
| us-west-2 usw2-az2 | 41 | 27% | 3.8 | 9 (09-28 06:50Z) |
| us-west-2 usw2-az3 | 98 | 18% | 3.1 | 9 (09-28 11:22Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 192 | 20% | 4.2 | 9 (09-28 11:22Z) |
| ap-northeast-1 | 192 | 77% | 7.4 | 9 (09-28 11:22Z) |
| ap-northeast-2 | 192 | 100% | 9.0 | 9 (09-28 11:22Z) |
| ap-south-1 | 192 | 54% | 6.0 | 2 (09-28 11:22Z) |
| ap-southeast-2 | 192 | 15% | 3.2 | 2 (09-28 11:22Z) |
| ap-southeast-3 | 192 | 14% | 3.2 | 8 (09-28 11:22Z) |
| us-east-1 | 192 | 79% | 7.2 | 9 (09-28 11:22Z) |
| us-east-2 | 192 | 79% | 7.5 | 9 (09-28 11:22Z) |
| us-west-2 | 192 | 60% | 6.2 | 9 (09-28 11:22Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333999999999999999999999999999999999999999
ap-northeast-1   999999999993499921999999999999999999111111111389
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       924999839999289998999999999999999999999999932112
ap-southeast-2   222222233512299222999999999999999922222222222242
ap-southeast-3   133333333996899951989158999928699989111111115368
us-east-1        994459996669954598347999999999999999999999999999
us-east-2        995999999499923489999999999999999999999999999999
us-west-2        195454995559554459934399999999999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 2 | 5 | 4 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 86 | 37% | 5.2 | 9 (09-28 11:22Z) |
| ap-east-1 ape1-az2 | 64 | 36% | 5.2 | 9 (09-28 10:26Z) |
| ap-east-1 ape1-az3 | 62 | 29% | 4.7 | 9 (09-28 11:22Z) |
| ap-northeast-1 apne1-az1 | 92 | 91% | 8.5 | 9 (09-27 18:17Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 117 | 100% | 9.0 | 9 (09-27 23:19Z) |
| ap-northeast-2 apne2-az1 | 151 | 100% | 9.0 | 9 (09-28 09:35Z) |
| ap-northeast-2 apne2-az2 | 32 | 59% | 6.6 | 9 (09-28 10:26Z) |
| ap-northeast-2 apne2-az3 | 169 | 100% | 9.0 | 9 (09-28 11:22Z) |
| ap-northeast-2 apne2-az4 | 77 | 39% | 5.3 | 9 (09-28 11:22Z) |
| ap-south-1 aps1-az1 | 55 | 60% | 6.6 | 9 (09-28 04:30Z) |
| ap-south-1 aps1-az2 | 59 | 39% | 5.3 | 9 (09-28 05:26Z) |
| ap-south-1 aps1-az3 | 77 | 77% | 7.6 | 9 (09-28 04:30Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 22 | 45% | 5.7 | 9 (09-27 18:17Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 83 | 98% | 8.8 | 9 (09-28 11:22Z) |
| us-east-1 use1-az5 | 46 | 98% | 8.8 | 9 (09-28 08:38Z) |
| us-east-1 use1-az6 | 73 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 74 | 99% | 8.9 | 9 (09-28 11:22Z) |
| us-east-2 use2-az2 | 106 | 98% | 8.9 | 9 (09-28 09:35Z) |
| us-east-2 use2-az3 | 98 | 92% | 8.4 | 9 (09-28 11:22Z) |
| us-west-2 usw2-az1 | 61 | 98% | 8.9 | 9 (09-28 08:38Z) |
| us-west-2 usw2-az2 | 56 | 98% | 8.8 | 9 (09-28 11:22Z) |
| us-west-2 usw2-az3 | 69 | 99% | 8.9 | 9 (09-28 10:26Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730700 | 2026-09-28T11:22:08Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.892000 | 2026-09-28T11:22:08Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.820600 | 2026-09-28T11:22:08Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.004600 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593700 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577600 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567800 | 2026-09-28T11:22:08Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T11:22:08Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.565400 | 2026-09-28T11:22:08Z |
| ap-south-1 | ap-south-1a | Windows | 0.346500 | 2026-09-28T11:22:08Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.586200 | 2026-09-28T11:22:08Z |
| ap-south-1 | ap-south-1b | Windows | 0.333400 | 2026-09-28T11:22:08Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.699100 | 2026-09-28T11:22:08Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.500800 | 2026-09-28T11:22:08Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.661300 | 2026-09-28T11:22:08Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.639400 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1a | Windows | 0.309700 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.480200 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.430900 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.384700 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.421100 | 2026-09-28T11:22:08Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529500 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2a | Windows | 0.641200 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524600 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2b | Windows | 0.641200 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.512500 | 2026-09-28T11:22:08Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.510500 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.489900 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2b | Windows | 0.332800 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.485100 | 2026-09-28T11:22:08Z |
| us-west-2 | us-west-2c | Windows | 0.332000 | 2026-09-28T11:22:08Z |
