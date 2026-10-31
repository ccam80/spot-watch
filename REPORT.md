# Spot placement score log

Generated 2026-10-31 22:12 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 484 | 48% | 5.2 | 9 (10-31 22:12Z) |
| ap-northeast-1 | 484 | 15% | 2.7 | 8 (10-31 22:12Z) |
| ap-northeast-2 | 484 | 67% | 7.0 | 9 (10-31 22:12Z) |
| ap-south-1 | 484 | 2% | 1.7 | 1 (10-31 22:12Z) |
| ap-southeast-2 | 484 | 0% | 1.0 | 1 (10-31 22:12Z) |
| ap-southeast-3 | 484 | 26% | 3.3 | 9 (10-31 22:12Z) |
| us-east-1 | 484 | 10% | 2.6 | 1 (10-31 22:12Z) |
| us-east-2 | 484 | 29% | 3.6 | 1 (10-31 22:12Z) |
| us-west-2 | 484 | 9% | 2.1 | 1 (10-31 22:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        219999999999999999911111199911111999999999111999
ap-northeast-1   211111111111222287111124211144211111211879111478
ap-northeast-2   999999999999999999999999999999119999999999199999
ap-south-1       111111111111122111121111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111117867511111111111111111551254111839
us-east-1        123333333323322222222211122222222222221221111111
us-east-2        111112899129111111111111111111111199111211199911
us-west-2        222222111221111111111111111111111111194131111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 155 | 6% | 1.6 | 1 (10-31 18:15Z) |
| ap-east-1 ape1-az2 | 357 | 65% | 6.6 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az1 | 105 | 7% | 1.6 | 8 (10-31 22:12Z) |
| ap-northeast-1 apne1-az4 | 218 | 25% | 3.4 | 1 (10-31 22:12Z) |
| ap-northeast-2 apne2-az1 | 414 | 61% | 6.5 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az3 | 451 | 67% | 6.9 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az4 | 477 | 68% | 7.1 | 9 (10-31 22:12Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 131 | 5% | 2.4 | 1 (10-31 22:12Z) |
| ap-southeast-2 apse2-az1 | 92 | 2% | 1.2 | 1 (10-31 21:11Z) |
| ap-southeast-2 apse2-az2 | 60 | 0% | 1.0 | 1 (10-31 22:12Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 306 | 39% | 4.4 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 100 | 0% | 1.1 | 1 (10-31 21:11Z) |
| us-east-1 use1-az2 | 133 | 2% | 1.3 | 1 (10-31 17:11Z) |
| us-east-1 use1-az4 | 159 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-1 use1-az5 | 155 | 25% | 3.1 | 1 (10-31 20:13Z) |
| us-east-1 use1-az6 | 117 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-2 use2-az1 | 204 | 41% | 4.5 | 8 (10-31 20:13Z) |
| us-east-2 use2-az2 | 246 | 49% | 5.2 | 9 (10-31 20:13Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 151 | 25% | 3.3 | 1 (10-31 22:12Z) |
| us-west-2 usw2-az2 | 117 | 18% | 2.6 | 1 (10-31 21:11Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 484 | 68% | 7.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 | 484 | 72% | 7.0 | 9 (10-31 22:12Z) |
| ap-northeast-2 | 484 | 100% | 9.0 | 9 (10-31 22:12Z) |
| ap-south-1 | 484 | 62% | 6.3 | 9 (10-31 22:12Z) |
| ap-southeast-2 | 484 | 24% | 3.4 | 9 (10-31 22:12Z) |
| ap-southeast-3 | 484 | 26% | 3.3 | 9 (10-31 22:12Z) |
| us-east-1 | 484 | 70% | 6.4 | 9 (10-31 22:12Z) |
| us-east-2 | 484 | 67% | 6.6 | 9 (10-31 22:12Z) |
| us-west-2 | 484 | 51% | 5.6 | 9 (10-31 22:12Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   911111111113399999999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999991111111122111129999999999997999999999999999
ap-southeast-2   111111111111111111111111199999991113199999999999
ap-southeast-3   111111111111117867511111111111111111551254111839
us-east-1        466666999999999323233343393943999999999993229999
us-east-2        222249999999932222222222222289999999999999299919
us-west-2        344555933559999948443959312112332449995499929999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 310 | 83% | 8.0 | 9 (10-31 20:13Z) |
| ap-east-1 ape1-az2 | 271 | 85% | 8.1 | 9 (10-31 20:13Z) |
| ap-east-1 ape1-az3 | 299 | 85% | 8.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az1 | 203 | 95% | 8.7 | 9 (10-31 18:15Z) |
| ap-northeast-1 apne1-az2 | 174 | 84% | 8.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az4 | 257 | 99% | 8.9 | 9 (10-31 21:11Z) |
| ap-northeast-2 apne2-az1 | 396 | 100% | 9.0 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az2 | 104 | 85% | 8.0 | 9 (10-31 20:13Z) |
| ap-northeast-2 apne2-az3 | 417 | 100% | 9.0 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az4 | 313 | 85% | 8.1 | 9 (10-31 16:13Z) |
| ap-south-1 aps1-az1 | 168 | 87% | 8.2 | 9 (10-31 22:12Z) |
| ap-south-1 aps1-az2 | 181 | 80% | 7.7 | 9 (10-31 19:10Z) |
| ap-south-1 aps1-az3 | 187 | 89% | 8.4 | 9 (10-31 22:12Z) |
| ap-southeast-2 apse2-az1 | 58 | 83% | 7.9 | 9 (10-31 20:13Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 70 | 81% | 7.9 | 9 (10-31 22:12Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 26 | 50% | 5.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az2 | 103 | 100% | 9.0 | 9 (10-31 20:13Z) |
| us-east-1 use1-az4 | 134 | 91% | 8.4 | 9 (10-31 22:12Z) |
| us-east-1 use1-az5 | 99 | 98% | 8.8 | 9 (10-31 21:11Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 167 | 99% | 8.9 | 9 (10-31 20:13Z) |
| us-east-2 use2-az2 | 190 | 99% | 8.9 | 9 (10-31 19:10Z) |
| us-east-2 use2-az3 | 216 | 96% | 8.7 | 9 (10-31 19:10Z) |
| us-west-2 usw2-az1 | 91 | 98% | 8.8 | 9 (10-31 20:13Z) |
| us-west-2 usw2-az2 | 87 | 90% | 8.3 | 9 (10-31 21:11Z) |
| us-west-2 usw2-az3 | 122 | 89% | 8.3 | 9 (10-31 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.701200 | 2026-10-31T22:12:04Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T22:12:04Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.740900 | 2026-10-31T22:12:04Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.876200 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583600 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591000 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571100 | 2026-10-31T22:12:04Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T22:12:04Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.635200 | 2026-10-31T22:12:04Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T22:12:04Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.534900 | 2026-10-31T22:12:04Z |
| ap-south-1 | ap-south-1b | Windows | 0.380100 | 2026-10-31T22:12:04Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651400 | 2026-10-31T22:12:04Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T22:12:04Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655600 | 2026-10-31T22:12:04Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.556900 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.570000 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.503100 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500700 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.548100 | 2026-10-31T22:12:04Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559400 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547900 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-31T22:12:04Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553500 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2a | Windows | 0.313000 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.573100 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2b | Windows | 0.320700 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544400 | 2026-10-31T22:12:04Z |
| us-west-2 | us-west-2c | Windows | 0.313300 | 2026-10-31T22:12:04Z |
