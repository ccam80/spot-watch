# Spot placement score log

Generated 2026-10-31 18:15 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 480 | 48% | 5.2 | 1 (10-31 18:15Z) |
| ap-northeast-1 | 480 | 15% | 2.7 | 1 (10-31 18:15Z) |
| ap-northeast-2 | 480 | 67% | 7.0 | 9 (10-31 18:15Z) |
| ap-south-1 | 480 | 2% | 1.7 | 1 (10-31 18:15Z) |
| ap-southeast-2 | 480 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 | 480 | 25% | 3.3 | 1 (10-31 18:15Z) |
| us-east-1 | 480 | 10% | 2.6 | 1 (10-31 18:15Z) |
| us-east-2 | 480 | 29% | 3.6 | 9 (10-31 18:15Z) |
| us-west-2 | 480 | 9% | 2.1 | 1 (10-31 18:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        212121999999999999999991111119991111199999999911
ap-northeast-1   122221111111111122228711112421114421111121187911
ap-northeast-2   999999999999999999999999999999999911999999999919
ap-south-1       111111111111111112211112111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111111111786751111111111111111155125411
us-east-1        211112333333332332222222221112222222222222122111
us-east-2        111111111289912911111111111111111111119911121119
us-west-2        122222222211122111111111111111111111111119413111
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
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 155 | 6% | 1.6 | 1 (10-31 18:15Z) |
| ap-east-1 ape1-az2 | 353 | 65% | 6.6 | 9 (10-31 16:13Z) |
| ap-northeast-1 apne1-az1 | 102 | 6% | 1.6 | 9 (10-31 16:13Z) |
| ap-northeast-1 apne1-az4 | 216 | 25% | 3.5 | 1 (10-31 18:15Z) |
| ap-northeast-2 apne2-az1 | 410 | 60% | 6.4 | 8 (10-31 18:15Z) |
| ap-northeast-2 apne2-az3 | 447 | 67% | 6.9 | 5 (10-31 18:15Z) |
| ap-northeast-2 apne2-az4 | 473 | 68% | 7.0 | 9 (10-31 18:15Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 129 | 5% | 2.4 | 1 (10-31 18:15Z) |
| ap-southeast-2 apse2-az1 | 90 | 2% | 1.2 | 1 (10-31 15:11Z) |
| ap-southeast-2 apse2-az2 | 57 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 302 | 39% | 4.4 | 4 (10-31 16:13Z) |
| us-east-1 use1-az1 | 99 | 0% | 1.1 | 1 (10-31 18:15Z) |
| us-east-1 use1-az2 | 133 | 2% | 1.3 | 1 (10-31 17:11Z) |
| us-east-1 use1-az4 | 159 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-1 use1-az5 | 154 | 25% | 3.1 | 1 (10-31 12:17Z) |
| us-east-1 use1-az6 | 117 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-2 use2-az1 | 202 | 41% | 4.5 | 1 (10-31 17:11Z) |
| us-east-2 use2-az2 | 244 | 48% | 5.1 | 1 (10-31 17:11Z) |
| us-east-2 use2-az3 | 273 | 45% | 5.0 | 9 (10-31 10:12Z) |
| us-west-2 usw2-az1 | 150 | 25% | 3.3 | 1 (10-31 18:15Z) |
| us-west-2 usw2-az2 | 116 | 18% | 2.7 | 9 (10-31 12:17Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 480 | 68% | 7.1 | 9 (10-31 18:15Z) |
| ap-northeast-1 | 480 | 72% | 7.0 | 9 (10-31 18:15Z) |
| ap-northeast-2 | 480 | 100% | 9.0 | 9 (10-31 18:15Z) |
| ap-south-1 | 480 | 62% | 6.3 | 9 (10-31 18:15Z) |
| ap-southeast-2 | 480 | 23% | 3.4 | 9 (10-31 18:15Z) |
| ap-southeast-3 | 480 | 25% | 3.3 | 1 (10-31 18:15Z) |
| us-east-1 | 480 | 69% | 6.4 | 2 (10-31 18:15Z) |
| us-east-2 | 480 | 67% | 6.6 | 9 (10-31 18:15Z) |
| us-west-2 | 480 | 51% | 5.6 | 2 (10-31 18:15Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999991111111111339999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999111111112211112999999999999799999999999
ap-southeast-2   911111111111111111111111111119999999111319999999
ap-southeast-3   111111111111111111786751111111111111111155125411
us-east-1        654546666699999999932323334339394399999999999322
us-east-2        121222224999999993222222222222228999999999999929
us-west-2        445534455593355999994844395931211233244999549992
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 309 | 83% | 8.0 | 9 (10-31 18:15Z) |
| ap-east-1 ape1-az2 | 269 | 85% | 8.1 | 9 (10-31 18:15Z) |
| ap-east-1 ape1-az3 | 296 | 85% | 8.1 | 9 (10-31 16:13Z) |
| ap-northeast-1 apne1-az1 | 203 | 95% | 8.7 | 9 (10-31 18:15Z) |
| ap-northeast-1 apne1-az2 | 172 | 84% | 8.0 | 9 (10-31 17:11Z) |
| ap-northeast-1 apne1-az4 | 256 | 99% | 8.9 | 9 (10-31 18:15Z) |
| ap-northeast-2 apne2-az1 | 394 | 100% | 9.0 | 9 (10-31 18:15Z) |
| ap-northeast-2 apne2-az2 | 102 | 84% | 8.0 | 9 (10-31 18:15Z) |
| ap-northeast-2 apne2-az3 | 416 | 100% | 9.0 | 9 (10-31 17:11Z) |
| ap-northeast-2 apne2-az4 | 313 | 85% | 8.1 | 9 (10-31 16:13Z) |
| ap-south-1 aps1-az1 | 165 | 87% | 8.2 | 9 (10-31 18:15Z) |
| ap-south-1 aps1-az2 | 180 | 79% | 7.7 | 9 (10-31 12:17Z) |
| ap-south-1 aps1-az3 | 184 | 89% | 8.4 | 9 (10-31 18:15Z) |
| ap-southeast-2 apse2-az1 | 57 | 82% | 7.9 | 9 (10-31 18:15Z) |
| ap-southeast-2 apse2-az2 | 2 | 50% | 6.0 | 9 (10-31 16:13Z) |
| ap-southeast-2 apse2-az3 | 67 | 81% | 7.8 | 9 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 26 | 50% | 5.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az2 | 102 | 100% | 9.0 | 9 (10-31 14:12Z) |
| us-east-1 use1-az4 | 131 | 91% | 8.4 | 9 (10-31 13:12Z) |
| us-east-1 use1-az5 | 97 | 98% | 8.8 | 9 (10-31 14:12Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 166 | 99% | 8.9 | 9 (10-31 14:12Z) |
| us-east-2 use2-az2 | 189 | 99% | 8.9 | 9 (10-31 14:12Z) |
| us-east-2 use2-az3 | 215 | 96% | 8.7 | 9 (10-31 16:13Z) |
| us-west-2 usw2-az1 | 90 | 98% | 8.8 | 9 (10-31 11:11Z) |
| us-west-2 usw2-az2 | 86 | 90% | 8.3 | 9 (10-31 16:13Z) |
| us-west-2 usw2-az3 | 120 | 89% | 8.2 | 9 (10-31 11:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700400 | 2026-10-31T18:15:20Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T18:15:20Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742400 | 2026-10-31T18:15:20Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.885800 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.583600 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.591000 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571100 | 2026-10-31T18:15:20Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T18:15:20Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.635200 | 2026-10-31T18:15:20Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-10-31T18:15:20Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.537600 | 2026-10-31T18:15:20Z |
| ap-south-1 | ap-south-1b | Windows | 0.380100 | 2026-10-31T18:15:20Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651700 | 2026-10-31T18:15:20Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-10-31T18:15:20Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656000 | 2026-10-31T18:15:20Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.562000 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.570300 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.503100 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500700 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.551200 | 2026-10-31T18:15:20Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559400 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548000 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545900 | 2026-10-31T18:15:20Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553500 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2a | Windows | 0.313700 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.573800 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2b | Windows | 0.321400 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.544400 | 2026-10-31T18:15:20Z |
| us-west-2 | us-west-2c | Windows | 0.313300 | 2026-10-31T18:15:20Z |
