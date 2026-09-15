# Spot placement score log

Generated 2026-09-15 13:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 108 | 0% | 1.6 | 3 (09-15 13:28Z) |
| ap-northeast-1 | 108 | 0% | 2.0 | 3 (09-15 13:28Z) |
| ap-northeast-2 | 108 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-south-1 | 108 | 0% | 2.1 | 1 (09-15 13:28Z) |
| ap-southeast-2 | 108 | 0% | 1.0 | 1 (09-15 13:28Z) |
| ap-southeast-3 | 108 | 0% | 2.5 | 3 (09-15 13:28Z) |
| us-east-1 | 108 | 0% | 2.0 | 2 (09-15 13:28Z) |
| us-east-2 | 108 | 0% | 1.6 | 1 (09-15 13:28Z) |
| us-west-2 | 108 | 0% | 1.5 | 1 (09-15 13:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111113333333333333333333333333333333
ap-northeast-1   112221123222222112322112332333333333333322332113
ap-northeast-2   333333333333333323333333333333333333333333333333
ap-south-1       131112211111111121131312111133333331333333333111
ap-southeast-2   111111111111111111111111131111111111111111111111
ap-southeast-3   333321233311313311333333333333333333333331313313
us-east-1        232233332113322122113113113322331132323322222212
us-east-2        111333311333311131111113131133333333333333311111
us-west-2        121331111111111111111111111113331331333333311121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 29 | 0% | 1.0 | 1 (09-15 07:38Z) |
| ap-east-1 ape1-az2 | 53 | 0% | 2.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 59 | 0% | 2.3 | 3 (09-15 13:28Z) |
| ap-northeast-2 apne2-az1 | 101 | 0% | 2.9 | 3 (09-15 13:28Z) |
| ap-northeast-2 apne2-az3 | 98 | 0% | 2.9 | 3 (09-15 13:28Z) |
| ap-northeast-2 apne2-az4 | 105 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-south-1 aps1-az1 | 45 | 0% | 1.7 | 3 (09-14 23:05Z) |
| ap-south-1 aps1-az3 | 61 | 0% | 2.6 | 3 (09-14 23:05Z) |
| ap-southeast-2 apse2-az1 | 21 | 0% | 1.1 | 1 (09-15 01:24Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 18 | 0% | 1.0 | 1 (09-15 07:38Z) |
| ap-southeast-3 apse3-az3 | 85 | 0% | 2.9 | 3 (09-15 13:28Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 30 | 0% | 1.1 | 1 (09-15 07:38Z) |
| us-east-1 use1-az4 | 18 | 0% | 1.2 | 1 (09-15 13:28Z) |
| us-east-1 use1-az5 | 30 | 0% | 1.3 | 1 (09-15 07:38Z) |
| us-east-1 use1-az6 | 42 | 0% | 1.2 | 1 (09-15 13:28Z) |
| us-east-2 use2-az1 | 33 | 0% | 1.5 | 1 (09-15 13:28Z) |
| us-east-2 use2-az2 | 47 | 0% | 1.8 | 1 (09-15 01:24Z) |
| us-east-2 use2-az3 | 52 | 0% | 2.2 | 1 (09-15 07:38Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 23 | 0% | 1.8 | 1 (09-15 13:28Z) |
| us-west-2 usw2-az3 | 56 | 0% | 1.6 | 1 (09-14 19:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 108 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 | 108 | 77% | 7.4 | 9 (09-15 13:28Z) |
| ap-northeast-2 | 108 | 100% | 9.0 | 9 (09-15 13:28Z) |
| ap-south-1 | 108 | 31% | 4.6 | 8 (09-15 13:28Z) |
| ap-southeast-2 | 108 | 9% | 2.7 | 2 (09-15 13:28Z) |
| ap-southeast-3 | 108 | 0% | 2.5 | 3 (09-15 13:28Z) |
| us-east-1 | 108 | 73% | 6.7 | 4 (09-15 13:28Z) |
| us-east-2 | 108 | 74% | 7.2 | 9 (09-15 13:28Z) |
| us-west-2 | 108 | 50% | 5.6 | 4 (09-15 13:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   299943999933999224999234999999999999999964999339
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333399992299951333993999999999999999999999918
ap-southeast-2   131111331111332222231123333333333332233222222222
ap-southeast-3   333321233311313311333333333333333333333331313313
us-east-1        999999544599445699329999234999999999999999436844
us-east-2        999999999999919999233399191999999999999999999999
us-west-2        999999944295133231332342335399999999999999934254
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 7 | · | 1 | 4 | 5 | 4 | 3 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 7 | · | 3 | 4 | 8 | 5 | 1 | 3 | 3 | 6 | 4 | 2 | 7 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | 4 | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | 5 | 6 | 5 | 9 | 6 | 9 | 7 | 7 | 9 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 42 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-east-1 ape1-az2 | 33 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-east-1 ape1-az3 | 36 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az1 | 54 | 85% | 8.1 | 9 (09-15 13:28Z) |
| ap-northeast-1 apne1-az2 | 21 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-northeast-1 apne1-az4 | 74 | 100% | 9.0 | 9 (09-15 13:28Z) |
| ap-northeast-2 apne2-az1 | 99 | 100% | 9.0 | 9 (09-15 13:28Z) |
| ap-northeast-2 apne2-az2 | 10 | 0% | 3.0 | 3 (09-14 19:16Z) |
| ap-northeast-2 apne2-az3 | 98 | 100% | 9.0 | 9 (09-15 13:28Z) |
| ap-northeast-2 apne2-az4 | 37 | 0% | 3.0 | 3 (09-15 07:38Z) |
| ap-south-1 aps1-az1 | 23 | 4% | 3.3 | 9 (09-15 01:24Z) |
| ap-south-1 aps1-az2 | 29 | 0% | 3.0 | 3 (09-15 13:28Z) |
| ap-south-1 aps1-az3 | 37 | 54% | 6.2 | 9 (09-15 01:24Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 32 | 0% | 3.0 | 3 (09-15 13:28Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 45 | 96% | 8.7 | 2 (09-15 07:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 41 | 100% | 9.0 | 9 (09-15 07:38Z) |
| us-east-2 use2-az2 | 72 | 97% | 8.8 | 9 (09-15 07:38Z) |
| us-east-2 use2-az3 | 48 | 83% | 7.9 | 9 (09-15 13:28Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.723300 | 2026-09-15T13:28:17Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-15T13:28:17Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.798300 | 2026-09-15T13:28:17Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.981000 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591100 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579500 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566300 | 2026-09-15T13:28:17Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741600 | 2026-09-15T13:28:17Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.595000 | 2026-09-15T13:28:17Z |
| ap-south-1 | ap-south-1a | Windows | 0.329200 | 2026-09-15T13:28:17Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.495700 | 2026-09-15T13:28:17Z |
| ap-south-1 | ap-south-1b | Windows | 0.319600 | 2026-09-15T13:28:17Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.694200 | 2026-09-15T13:28:17Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504000 | 2026-09-15T13:28:17Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.875400 | 2026-09-15T13:28:17Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.488600 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.880300 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1a | Windows | 0.343300 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.672000 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1b | Windows | 0.329300 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.586900 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1c | Windows | 0.308500 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.542700 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1d | Windows | 0.317900 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.565500 | 2026-09-15T13:28:17Z |
| us-east-1 | us-east-1f | Windows | 0.326500 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527400 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2a | Windows | 0.640600 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528700 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2b | Windows | 0.637200 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516800 | 2026-09-15T13:28:17Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.569700 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2a | Windows | 0.346600 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.544300 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2b | Windows | 0.339900 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.538100 | 2026-09-15T13:28:17Z |
| us-west-2 | us-west-2c | Windows | 0.340900 | 2026-09-15T13:28:17Z |
