# Spot placement score log

Generated 2026-09-24 14:57 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 158 | 3% | 2.2 | 9 (09-24 14:57Z) |
| ap-northeast-1 | 158 | 0% | 1.9 | 2 (09-24 14:57Z) |
| ap-northeast-2 | 158 | 3% | 3.2 | 9 (09-24 14:57Z) |
| ap-south-1 | 158 | 0% | 1.9 | 1 (09-24 14:57Z) |
| ap-southeast-2 | 158 | 0% | 1.0 | 1 (09-24 14:57Z) |
| ap-southeast-3 | 158 | 3% | 2.7 | 9 (09-24 14:57Z) |
| us-east-1 | 158 | 0% | 2.0 | 3 (09-24 14:57Z) |
| us-east-2 | 158 | 1% | 1.9 | 1 (09-24 14:57Z) |
| us-west-2 | 158 | 0% | 1.7 | 2 (09-24 14:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333399999
ap-northeast-1   122221122221112212233223123221121221332222332222
ap-northeast-2   333333333333333333333333333333333333333333399999
ap-south-1       211221113333113121133333333332111111111111111111
ap-southeast-2   111111111111111111111111111111113111111111111111
ap-southeast-3   313333313131123333333333313333133313333333399689
us-east-1        131121232231231112131122333333331321223232222123
us-east-2        131313333333133113333123333331331111211311319291
us-west-2        211111131221311123333333333333331211222213222112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 3 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 48 | 0% | 1.4 | 1 (09-24 14:57Z) |
| ap-east-1 ape1-az2 | 100 | 5% | 2.8 | 9 (09-24 14:57Z) |
| ap-northeast-1 apne1-az1 | 20 | 0% | 1.1 | 2 (09-22 18:48Z) |
| ap-northeast-1 apne1-az4 | 72 | 0% | 2.2 | 1 (09-24 14:57Z) |
| ap-northeast-2 apne2-az1 | 141 | 4% | 3.2 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az3 | 140 | 4% | 3.1 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az4 | 155 | 3% | 3.2 | 9 (09-24 14:57Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 80 | 0% | 2.6 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 35 | 0% | 1.0 | 1 (09-24 14:57Z) |
| ap-southeast-3 apse3-az3 | 123 | 4% | 3.1 | 9 (09-24 14:57Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 54 | 0% | 1.3 | 1 (09-23 20:14Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 48 | 0% | 1.5 | 1 (09-23 23:37Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 52 | 2% | 1.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 66 | 2% | 2.1 | 1 (09-24 14:57Z) |
| us-east-2 use2-az3 | 87 | 2% | 2.4 | 1 (09-24 14:57Z) |
| us-west-2 usw2-az1 | 47 | 0% | 2.1 | 1 (09-23 20:14Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 158 | 3% | 3.2 | 9 (09-24 14:57Z) |
| ap-northeast-1 | 158 | 79% | 7.6 | 9 (09-24 14:57Z) |
| ap-northeast-2 | 158 | 100% | 9.0 | 9 (09-24 14:57Z) |
| ap-south-1 | 158 | 47% | 5.6 | 8 (09-24 14:57Z) |
| ap-southeast-2 | 158 | 8% | 2.7 | 9 (09-24 14:57Z) |
| ap-southeast-3 | 158 | 3% | 2.7 | 9 (09-24 14:57Z) |
| us-east-1 | 158 | 76% | 6.9 | 5 (09-24 14:57Z) |
| us-east-2 | 158 | 76% | 7.3 | 2 (09-24 14:57Z) |
| us-west-2 | 158 | 55% | 5.8 | 5 (09-24 14:57Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333399999
ap-northeast-1   249994199993399999999999999999999999999999999349
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992999939999239999999999999999919992499983999928
ap-southeast-2   223322233222233233333333333332233122222223351229
ap-southeast-3   313333313131123333333333313333133313333333399689
us-east-1        493955995699994549999999999999994999445999666995
us-east-2        299999999999999119999199999999993399599999949992
us-west-2        534413994459533459999999999999994319545499555955
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 5 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 3 | 4 | 2 | 4 | 3 | 3 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 8 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 4 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 58 | 7% | 3.4 | 9 (09-24 14:57Z) |
| ap-east-1 ape1-az2 | 44 | 7% | 3.4 | 9 (09-24 09:55Z) |
| ap-east-1 ape1-az3 | 48 | 8% | 3.5 | 9 (09-24 14:57Z) |
| ap-northeast-1 apne1-az1 | 85 | 91% | 8.4 | 9 (09-24 14:57Z) |
| ap-northeast-1 apne1-az2 | 28 | 7% | 3.4 | 9 (09-24 14:57Z) |
| ap-northeast-1 apne1-az4 | 107 | 100% | 9.0 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az1 | 143 | 100% | 9.0 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az2 | 16 | 19% | 4.1 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az3 | 144 | 100% | 9.0 | 9 (09-24 14:57Z) |
| ap-northeast-2 apne2-az4 | 52 | 10% | 3.6 | 9 (09-24 14:57Z) |
| ap-south-1 aps1-az1 | 51 | 57% | 6.4 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az2 | 38 | 5% | 3.3 | 9 (09-23 23:37Z) |
| ap-south-1 aps1-az3 | 68 | 74% | 7.4 | 9 (09-24 04:37Z) |
| ap-southeast-2 apse2-az1 | 13 | 23% | 4.2 | 3 (09-23 16:48Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 13 | 8% | 3.5 | 9 (09-24 14:57Z) |
| ap-southeast-3 apse3-az3 | 42 | 5% | 3.3 | 9 (09-23 23:37Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 65 | 97% | 8.8 | 9 (09-23 05:52Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 63 | 100% | 9.0 | 9 (09-24 04:37Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 83 | 90% | 8.3 | 9 (09-24 09:55Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 42 | 98% | 8.8 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 58 | 98% | 8.9 | 9 (09-23 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727600 | 2026-09-24T14:57:36Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.869900 | 2026-09-24T14:57:36Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.843600 | 2026-09-24T14:57:36Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.028600 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591600 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578800 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568500 | 2026-09-24T14:57:36Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-24T14:57:36Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.489400 | 2026-09-24T14:57:36Z |
| ap-south-1 | ap-south-1a | Windows | 0.332300 | 2026-09-24T14:57:36Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.472800 | 2026-09-24T14:57:36Z |
| ap-south-1 | ap-south-1b | Windows | 0.307000 | 2026-09-24T14:57:36Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.643100 | 2026-09-24T14:57:36Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.523100 | 2026-09-24T14:57:36Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.758600 | 2026-09-24T14:57:36Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.569500 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.747300 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1a | Windows | 0.336300 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.561800 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1b | Windows | 0.291100 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.441700 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.443400 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1d | Windows | 0.287900 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.429500 | 2026-09-24T14:57:36Z |
| us-east-1 | us-east-1f | Windows | 0.296100 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524800 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524600 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.511600 | 2026-09-24T14:57:36Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.517100 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2a | Windows | 0.333600 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.484100 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2b | Windows | 0.333300 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-24T14:57:36Z |
| us-west-2 | us-west-2c | Windows | 0.332400 | 2026-09-24T14:57:36Z |
