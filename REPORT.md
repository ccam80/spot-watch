# Spot placement score log

Generated 2026-09-18 09:38 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 123 | 0% | 1.7 | 3 (09-18 09:38Z) |
| ap-northeast-1 | 123 | 0% | 1.9 | 1 (09-18 09:38Z) |
| ap-northeast-2 | 123 | 0% | 3.0 | 3 (09-18 09:38Z) |
| ap-south-1 | 123 | 0% | 2.0 | 1 (09-18 09:38Z) |
| ap-southeast-2 | 123 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 | 123 | 0% | 2.5 | 1 (09-18 09:38Z) |
| us-east-1 | 123 | 0% | 1.9 | 2 (09-18 09:38Z) |
| us-east-2 | 123 | 0% | 1.7 | 1 (09-18 09:38Z) |
| us-west-2 | 123 | 0% | 1.5 | 3 (09-18 09:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        113333333333333333333333333333333333333333333333
ap-northeast-1   112322112332333333333333322332113221222211222211
ap-northeast-2   323333333333333333333333333333333333333333333333
ap-south-1       121131312111133333331333333333111112112211133331
ap-southeast-2   111111111131111111111111111111111111111111111111
ap-southeast-3   311333333333333333333333331313313133133333131311
us-east-1        122113113113322331132323322222212211311212322312
us-east-2        131111113131133333333333333311111111313133333331
us-west-2        111111111111113331331333333311121112111111312213
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 32 | 0% | 1.0 | 1 (09-17 00:25Z) |
| ap-east-1 ape1-az2 | 68 | 0% | 2.2 | 3 (09-18 09:38Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 62 | 0% | 2.3 | 1 (09-17 00:25Z) |
| ap-northeast-2 apne2-az1 | 111 | 0% | 2.9 | 3 (09-18 09:38Z) |
| ap-northeast-2 apne2-az3 | 109 | 0% | 2.9 | 3 (09-18 09:38Z) |
| ap-northeast-2 apne2-az4 | 120 | 0% | 3.0 | 3 (09-18 09:38Z) |
| ap-south-1 aps1-az1 | 51 | 0% | 1.7 | 3 (09-17 23:31Z) |
| ap-south-1 aps1-az3 | 66 | 0% | 2.6 | 3 (09-18 04:33Z) |
| ap-southeast-2 apse2-az1 | 22 | 0% | 1.1 | 1 (09-15 22:08Z) |
| ap-southeast-2 apse2-az2 | 18 | 0% | 1.0 | 1 (09-16 18:09Z) |
| ap-southeast-3 apse3-az1 | 26 | 0% | 1.0 | 1 (09-18 09:38Z) |
| ap-southeast-3 apse3-az3 | 94 | 0% | 2.9 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 14 | 0% | 1.0 | 1 (09-17 06:03Z) |
| us-east-1 use1-az2 | 37 | 0% | 1.1 | 1 (09-18 09:38Z) |
| us-east-1 use1-az4 | 24 | 0% | 1.3 | 3 (09-17 23:31Z) |
| us-east-1 use1-az5 | 36 | 0% | 1.4 | 1 (09-18 09:38Z) |
| us-east-1 use1-az6 | 44 | 0% | 1.2 | 3 (09-17 11:34Z) |
| us-east-2 use2-az1 | 40 | 0% | 1.6 | 3 (09-18 04:33Z) |
| us-east-2 use2-az2 | 56 | 0% | 1.9 | 3 (09-18 04:33Z) |
| us-east-2 use2-az3 | 66 | 0% | 2.3 | 1 (09-18 09:38Z) |
| us-west-2 usw2-az1 | 31 | 0% | 1.9 | 1 (09-16 18:09Z) |
| us-west-2 usw2-az2 | 25 | 0% | 1.9 | 3 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 61 | 0% | 1.6 | 1 (09-18 09:38Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 123 | 0% | 3.0 | 3 (09-18 09:38Z) |
| ap-northeast-1 | 123 | 75% | 7.3 | 3 (09-18 09:38Z) |
| ap-northeast-2 | 123 | 100% | 9.0 | 9 (09-18 09:38Z) |
| ap-south-1 | 123 | 37% | 5.0 | 2 (09-18 09:38Z) |
| ap-southeast-2 | 123 | 8% | 2.6 | 2 (09-18 09:38Z) |
| ap-southeast-3 | 123 | 0% | 2.5 | 1 (09-18 09:38Z) |
| us-east-1 | 123 | 73% | 6.7 | 9 (09-18 09:38Z) |
| us-east-2 | 123 | 75% | 7.2 | 9 (09-18 09:38Z) |
| us-west-2 | 123 | 49% | 5.5 | 5 (09-18 09:38Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   224999234999999999999999964999339992499941999933
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       951333993999999999999999999999918999929999399992
ap-southeast-2   222231123333333333332233222222222222233222332222
ap-southeast-3   311333333333333333333333331313313133133333131311
us-east-1        699329999234999999999999999436844324939559956999
us-east-2        999233399191999999999999999999999212999999999999
us-west-2        231332342335399999999999999934254335344139944595
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 5 | 3 | 4 | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 8 | · | 3 | 4 | 8 | 6 | 5 | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 6 | 6 | 6 | 6 | 4 | 4 | 6 | 4 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 6 | 9 | 8 | 9 | 9 | 5 | 5 | 6 | 4 | 7 | 5 | 5 | 6 | 4 | 6 | 6 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 7 | 9 | 4 | 8 | 7 | 7 | 5 | 7 |
| us-west-2 | 5 | 3 | · | 2 | 6 | 5 | 9 | 4 | 6 | 5 | 9 | 6 | 9 | 6 | 7 | 9 | 6 | 6 | 4 | 5 | 4 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 48 | 0% | 3.0 | 3 (09-18 09:38Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 3.0 | 3 (09-17 00:25Z) |
| ap-east-1 ape1-az3 | 40 | 0% | 3.0 | 3 (09-17 23:31Z) |
| ap-northeast-1 apne1-az1 | 62 | 87% | 8.2 | 9 (09-17 20:14Z) |
| ap-northeast-1 apne1-az2 | 22 | 0% | 3.0 | 3 (09-16 13:26Z) |
| ap-northeast-1 apne1-az4 | 81 | 100% | 9.0 | 9 (09-17 20:14Z) |
| ap-northeast-2 apne2-az1 | 114 | 100% | 9.0 | 9 (09-18 09:38Z) |
| ap-northeast-2 apne2-az2 | 12 | 0% | 3.0 | 3 (09-15 22:08Z) |
| ap-northeast-2 apne2-az3 | 113 | 100% | 9.0 | 9 (09-18 09:38Z) |
| ap-northeast-2 apne2-az4 | 43 | 0% | 3.0 | 3 (09-17 16:52Z) |
| ap-south-1 aps1-az1 | 33 | 33% | 5.0 | 9 (09-18 04:33Z) |
| ap-south-1 aps1-az2 | 33 | 0% | 3.0 | 3 (09-17 20:14Z) |
| ap-south-1 aps1-az3 | 49 | 63% | 6.8 | 9 (09-18 04:33Z) |
| ap-southeast-2 apse2-az1 | 11 | 27% | 4.5 | 3 (09-16 18:09Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 36 | 0% | 3.0 | 3 (09-17 23:31Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 47 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-1 use1-az4 | 50 | 96% | 8.7 | 9 (09-18 09:38Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 48 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-2 use2-az1 | 50 | 100% | 9.0 | 9 (09-18 09:38Z) |
| us-east-2 use2-az2 | 83 | 98% | 8.8 | 9 (09-18 09:38Z) |
| us-east-2 use2-az3 | 60 | 87% | 8.1 | 9 (09-18 09:38Z) |
| us-west-2 usw2-az1 | 42 | 98% | 8.9 | 9 (09-17 11:34Z) |
| us-west-2 usw2-az2 | 29 | 97% | 8.7 | 5 (09-18 09:38Z) |
| us-west-2 usw2-az3 | 41 | 98% | 8.8 | 9 (09-17 11:34Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710400 | 2026-09-18T09:38:35Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-18T09:38:35Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.833200 | 2026-09-18T09:38:35Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.016200 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.589800 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.579100 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565300 | 2026-09-18T09:38:35Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742400 | 2026-09-18T09:38:35Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.518200 | 2026-09-18T09:38:35Z |
| ap-south-1 | ap-south-1a | Windows | 0.316800 | 2026-09-18T09:38:35Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.462800 | 2026-09-18T09:38:35Z |
| ap-south-1 | ap-south-1b | Windows | 0.318500 | 2026-09-18T09:38:35Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.686600 | 2026-09-18T09:38:35Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507100 | 2026-09-18T09:38:35Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.898900 | 2026-09-18T09:38:35Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.554400 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.851200 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1a | Windows | 0.343600 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.644200 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1b | Windows | 0.322400 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.539400 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1c | Windows | 0.299800 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.542800 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1d | Windows | 0.310200 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.533900 | 2026-09-18T09:38:35Z |
| us-east-1 | us-east-1f | Windows | 0.319500 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.531000 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2a | Windows | 0.641600 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529300 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2b | Windows | 0.638200 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.521600 | 2026-09-18T09:38:35Z |
| us-east-2 | us-east-2c | Windows | 0.638400 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.568400 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2a | Windows | 0.341100 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.530900 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2b | Windows | 0.337900 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.533500 | 2026-09-18T09:38:35Z |
| us-west-2 | us-west-2c | Windows | 0.338400 | 2026-09-18T09:38:35Z |
