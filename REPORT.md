# Spot placement score log

Generated 2026-10-04 18:06 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 270 | 34% | 4.3 | 2 (10-04 18:06Z) |
| ap-northeast-1 | 270 | 15% | 2.8 | 9 (10-04 18:06Z) |
| ap-northeast-2 | 270 | 43% | 5.6 | 9 (10-04 18:06Z) |
| ap-south-1 | 270 | 2% | 1.8 | 2 (10-04 18:06Z) |
| ap-southeast-2 | 270 | 0% | 1.0 | 1 (10-04 18:06Z) |
| ap-southeast-3 | 270 | 20% | 3.3 | 1 (10-04 18:06Z) |
| us-east-1 | 270 | 9% | 2.5 | 9 (10-04 18:06Z) |
| us-east-2 | 270 | 27% | 3.6 | 9 (10-04 18:06Z) |
| us-west-2 | 270 | 11% | 2.4 | 1 (10-04 18:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999989999911111199399119119999812
ap-northeast-1   137961222122222211118991279981212982199999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111221111111111111111111111111112111111111112
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111118711111111111114765161111119991141111111111
us-east-1        111291222999913222222222322222119229222331199199
us-east-2        191699991119999999111118171218999999991199999999
us-west-2        211111211111121122222222222121112221212999999991
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 4 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 90 | 0% | 1.4 | 2 (10-04 18:06Z) |
| ap-east-1 ape1-az2 | 191 | 48% | 5.6 | 8 (10-04 06:47Z) |
| ap-northeast-1 apne1-az1 | 41 | 7% | 1.8 | 2 (10-03 17:12Z) |
| ap-northeast-1 apne1-az4 | 130 | 25% | 3.6 | 8 (10-04 18:06Z) |
| ap-northeast-2 apne2-az1 | 239 | 42% | 5.4 | 6 (10-04 06:47Z) |
| ap-northeast-2 apne2-az3 | 251 | 46% | 5.7 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az4 | 267 | 44% | 5.6 | 9 (10-04 18:06Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 52 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 83 | 27% | 3.4 | 9 (10-04 18:06Z) |
| us-east-1 use1-az5 | 85 | 24% | 3.2 | 9 (10-04 18:06Z) |
| us-east-1 use1-az6 | 65 | 20% | 2.9 | 9 (10-04 18:06Z) |
| us-east-2 use2-az1 | 108 | 37% | 4.3 | 9 (10-04 18:06Z) |
| us-east-2 use2-az2 | 141 | 43% | 4.9 | 9 (10-04 18:06Z) |
| us-east-2 use2-az3 | 165 | 41% | 4.9 | 9 (10-04 18:06Z) |
| us-west-2 usw2-az1 | 88 | 30% | 3.9 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az2 | 53 | 26% | 3.6 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az3 | 113 | 20% | 3.2 | 9 (10-04 13:09Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 270 | 43% | 5.6 | 9 (10-04 18:06Z) |
| ap-northeast-1 | 270 | 74% | 7.2 | 9 (10-04 18:06Z) |
| ap-northeast-2 | 270 | 100% | 9.0 | 9 (10-04 18:06Z) |
| ap-south-1 | 270 | 59% | 6.2 | 9 (10-04 18:06Z) |
| ap-southeast-2 | 270 | 16% | 3.1 | 9 (10-04 18:06Z) |
| ap-southeast-3 | 270 | 20% | 3.3 | 1 (10-04 18:06Z) |
| us-east-1 | 270 | 72% | 6.7 | 9 (10-04 18:06Z) |
| us-east-2 | 270 | 76% | 7.4 | 9 (10-04 18:06Z) |
| us-west-2 | 270 | 54% | 5.8 | 9 (10-04 18:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999222332234437999999999999224992299999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999111111111111992999992999999999999999
ap-southeast-2   922112222222222222222222222222222222222222229299
ap-southeast-3   111118711111111111114765161111119991141111111111
us-east-1        359593655999936554443334433344559449855763499999
us-east-2        399999999999999999832929983599999999993999999999
us-west-2        532243533324253455455444445444339344995999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 6 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 154 | 65% | 6.9 | 9 (10-04 18:06Z) |
| ap-east-1 ape1-az2 | 124 | 67% | 7.0 | 9 (10-04 06:47Z) |
| ap-east-1 ape1-az3 | 120 | 63% | 6.8 | 9 (10-04 13:09Z) |
| ap-northeast-1 apne1-az1 | 128 | 92% | 8.5 | 9 (10-04 18:06Z) |
| ap-northeast-1 apne1-az2 | 64 | 59% | 6.6 | 9 (10-04 06:47Z) |
| ap-northeast-1 apne1-az4 | 156 | 99% | 9.0 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az1 | 209 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az2 | 60 | 77% | 7.5 | 9 (10-04 18:06Z) |
| ap-northeast-2 apne2-az3 | 234 | 100% | 9.0 | 9 (10-04 06:47Z) |
| ap-northeast-2 apne2-az4 | 147 | 68% | 7.1 | 9 (10-04 18:06Z) |
| ap-south-1 aps1-az1 | 88 | 75% | 7.5 | 9 (10-04 18:06Z) |
| ap-south-1 aps1-az2 | 95 | 62% | 6.7 | 9 (10-04 18:06Z) |
| ap-south-1 aps1-az3 | 106 | 83% | 8.0 | 9 (10-04 06:47Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 31 | 61% | 6.7 | 9 (10-04 18:06Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 78 | 100% | 9.0 | 9 (10-04 18:06Z) |
| us-east-1 use1-az4 | 95 | 97% | 8.8 | 9 (10-04 13:09Z) |
| us-east-1 use1-az5 | 56 | 98% | 8.9 | 9 (10-04 06:47Z) |
| us-east-1 use1-az6 | 79 | 96% | 8.7 | 9 (10-04 06:47Z) |
| us-east-2 use2-az1 | 98 | 99% | 8.9 | 9 (10-04 06:47Z) |
| us-east-2 use2-az2 | 144 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-east-2 use2-az3 | 126 | 94% | 8.6 | 9 (10-04 18:06Z) |
| us-west-2 usw2-az1 | 70 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-west-2 usw2-az2 | 64 | 95% | 8.6 | 9 (10-04 13:09Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.721100 | 2026-10-04T18:06:31Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-04T18:06:31Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.773800 | 2026-10-04T18:06:31Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.956800 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594200 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565300 | 2026-10-04T18:06:31Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743600 | 2026-10-04T18:06:31Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.655600 | 2026-10-04T18:06:31Z |
| ap-south-1 | ap-south-1a | Windows | 0.370100 | 2026-10-04T18:06:31Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.712300 | 2026-10-04T18:06:31Z |
| ap-south-1 | ap-south-1b | Windows | 0.361300 | 2026-10-04T18:06:31Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.723300 | 2026-10-04T18:06:31Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.500300 | 2026-10-04T18:06:31Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.514800 | 2026-10-04T18:06:31Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.573000 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1a | Windows | 0.286500 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.443600 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.479200 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.412000 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.499500 | 2026-10-04T18:06:31Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.535000 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2a | Windows | 0.641200 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.528000 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515800 | 2026-10-04T18:06:31Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.503900 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2a | Windows | 0.331300 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491800 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.480800 | 2026-10-04T18:06:31Z |
| us-west-2 | us-west-2c | Windows | 0.329900 | 2026-10-04T18:06:31Z |
