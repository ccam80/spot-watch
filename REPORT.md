# Spot placement score log

Generated 2026-10-18 18:02 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 334 | 40% | 4.6 | 9 (10-18 18:01Z) |
| ap-northeast-1 | 334 | 15% | 2.8 | 1 (10-18 18:01Z) |
| ap-northeast-2 | 334 | 53% | 6.2 | 9 (10-18 18:01Z) |
| ap-south-1 | 334 | 2% | 1.8 | 2 (10-18 18:01Z) |
| ap-southeast-2 | 334 | 1% | 1.1 | 1 (10-18 18:01Z) |
| ap-southeast-3 | 334 | 23% | 3.4 | 4 (10-18 18:01Z) |
| us-east-1 | 334 | 10% | 2.6 | 9 (10-18 18:01Z) |
| us-east-2 | 334 | 29% | 3.7 | 9 (10-18 18:01Z) |
| us-west-2 | 334 | 11% | 2.3 | 1 (10-18 18:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111822929999999999999999999999999999999999999
ap-northeast-1   111911122221192212121114221142111132212932416591
ap-northeast-2   999991999999999999999999999999999999999999999999
ap-south-1       221111112222222222111112222222111222222222222222
ap-southeast-2   111111111111111111111111111111111111119119111111
ap-southeast-3   113891199979395151122111131151821438751867992474
us-east-1        113232333192233222113333232132312222233322192399
us-east-2        111111181199999911112991112911199911116199999919
us-west-2        111111999911111111111111111122111122211212121911
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 6 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 116 | 8% | 1.7 | 1 (10-17 04:14Z) |
| ap-east-1 ape1-az2 | 239 | 55% | 6.0 | 9 (10-18 18:01Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 157 | 25% | 3.6 | 8 (10-18 14:30Z) |
| ap-northeast-2 apne2-az1 | 293 | 50% | 5.8 | 6 (10-18 18:01Z) |
| ap-northeast-2 apne2-az3 | 306 | 54% | 6.1 | 9 (10-18 18:01Z) |
| ap-northeast-2 apne2-az4 | 331 | 54% | 6.2 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 69 | 0% | 1.0 | 1 (10-17 04:14Z) |
| ap-southeast-3 apse3-az3 | 226 | 33% | 4.3 | 7 (10-18 14:30Z) |
| us-east-1 use1-az1 | 64 | 0% | 1.1 | 1 (10-18 05:47Z) |
| us-east-1 use1-az2 | 93 | 3% | 1.5 | 2 (10-18 14:30Z) |
| us-east-1 use1-az4 | 101 | 29% | 3.5 | 9 (10-18 18:01Z) |
| us-east-1 use1-az5 | 106 | 25% | 3.3 | 9 (10-18 18:01Z) |
| us-east-1 use1-az6 | 76 | 22% | 3.0 | 9 (10-18 18:01Z) |
| us-east-2 use2-az1 | 132 | 41% | 4.6 | 9 (10-18 18:01Z) |
| us-east-2 use2-az2 | 173 | 46% | 5.0 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 204 | 44% | 5.0 | 9 (10-18 18:01Z) |
| us-west-2 usw2-az1 | 118 | 27% | 3.6 | 9 (10-18 10:55Z) |
| us-west-2 usw2-az2 | 71 | 25% | 3.4 | 9 (10-18 10:55Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 334 | 54% | 6.3 | 9 (10-18 18:01Z) |
| ap-northeast-1 | 334 | 74% | 7.2 | 9 (10-18 18:01Z) |
| ap-northeast-2 | 334 | 100% | 9.0 | 9 (10-18 18:01Z) |
| ap-south-1 | 334 | 62% | 6.4 | 9 (10-18 18:01Z) |
| ap-southeast-2 | 334 | 19% | 3.3 | 9 (10-18 18:01Z) |
| ap-southeast-3 | 334 | 23% | 3.4 | 4 (10-18 18:01Z) |
| us-east-1 | 334 | 71% | 6.6 | 9 (10-18 18:01Z) |
| us-east-2 | 334 | 71% | 6.9 | 9 (10-18 18:01Z) |
| us-west-2 | 334 | 52% | 5.7 | 9 (10-18 18:01Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   911999999999999992399239992199911999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       991499999999999299199912299229991299999999999999
ap-southeast-2   111189199999911111111111811111111111199999999999
ap-southeast-3   113891199979395151122111131151821438751867992474
us-east-1        546456998299999945426664355554679344659999999999
us-east-2        121211992299999911912991122911199931139999999999
us-west-2        133233999999359299442495343355433445443999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 203 | 73% | 7.4 | 9 (10-18 10:55Z) |
| ap-east-1 ape1-az2 | 170 | 76% | 7.6 | 9 (10-18 18:01Z) |
| ap-east-1 ape1-az3 | 170 | 74% | 7.4 | 9 (10-18 05:47Z) |
| ap-northeast-1 apne1-az1 | 154 | 93% | 8.5 | 9 (10-17 04:14Z) |
| ap-northeast-1 apne1-az2 | 98 | 72% | 7.3 | 9 (10-18 18:01Z) |
| ap-northeast-1 apne1-az4 | 190 | 98% | 8.9 | 9 (10-18 10:55Z) |
| ap-northeast-2 apne2-az1 | 261 | 100% | 9.0 | 9 (10-18 18:01Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 287 | 100% | 9.0 | 9 (10-18 18:01Z) |
| ap-northeast-2 apne2-az4 | 198 | 76% | 7.6 | 9 (10-18 14:30Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 120 | 70% | 7.2 | 9 (10-18 10:55Z) |
| ap-south-1 aps1-az3 | 137 | 86% | 8.2 | 9 (10-18 10:55Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 43 | 70% | 7.1 | 9 (10-18 14:30Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 83 | 100% | 9.0 | 9 (10-17 19:18Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 69 | 97% | 8.8 | 9 (10-18 18:01Z) |
| us-east-1 use1-az6 | 89 | 96% | 8.7 | 9 (10-18 05:47Z) |
| us-east-2 use2-az1 | 111 | 98% | 8.9 | 9 (10-18 05:47Z) |
| us-east-2 use2-az2 | 158 | 99% | 8.9 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 148 | 95% | 8.6 | 9 (10-18 10:55Z) |
| us-west-2 usw2-az1 | 78 | 97% | 8.8 | 9 (10-18 18:01Z) |
| us-west-2 usw2-az2 | 71 | 96% | 8.7 | 9 (10-18 05:47Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710000 | 2026-10-18T18:01:53Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-18T18:01:53Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.765200 | 2026-10-18T18:01:53Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.945100 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585600 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581800 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567600 | 2026-10-18T18:01:53Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741200 | 2026-10-18T18:01:53Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.551400 | 2026-10-18T18:01:53Z |
| ap-south-1 | ap-south-1a | Windows | 0.385500 | 2026-10-18T18:01:53Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.709400 | 2026-10-18T18:01:53Z |
| ap-south-1 | ap-south-1b | Windows | 0.353700 | 2026-10-18T18:01:53Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.708300 | 2026-10-18T18:01:53Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.520200 | 2026-10-18T18:01:53Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.638300 | 2026-10-18T18:01:53Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.567000 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.429800 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.531700 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.505500 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.433600 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.487800 | 2026-10-18T18:01:53Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.550000 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2a | Windows | 0.643400 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.541900 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2b | Windows | 0.639300 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.539600 | 2026-10-18T18:01:53Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.524800 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2a | Windows | 0.314700 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.500500 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2b | Windows | 0.331000 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.494000 | 2026-10-18T18:01:53Z |
| us-west-2 | us-west-2c | Windows | 0.314300 | 2026-10-18T18:01:53Z |
