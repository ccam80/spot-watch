# Spot placement score log

Generated 2026-11-01 00:41 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 486 | 49% | 5.2 | 9 (11-01 00:41Z) |
| ap-northeast-1 | 486 | 15% | 2.7 | 8 (11-01 00:41Z) |
| ap-northeast-2 | 486 | 67% | 7.0 | 9 (11-01 00:41Z) |
| ap-south-1 | 486 | 2% | 1.7 | 1 (11-01 00:41Z) |
| ap-southeast-2 | 486 | 0% | 1.0 | 1 (11-01 00:41Z) |
| ap-southeast-3 | 486 | 26% | 3.3 | 3 (11-01 00:41Z) |
| us-east-1 | 486 | 10% | 2.6 | 1 (11-01 00:41Z) |
| us-east-2 | 486 | 29% | 3.6 | 6 (11-01 00:41Z) |
| us-west-2 | 486 | 9% | 2.1 | 1 (11-01 00:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999991111119991111199999999911199999
ap-northeast-1   111111111122228711112421114421111121187911147888
ap-northeast-2   999999999999999999999999999911999999999919999999
ap-south-1       111111111112211112111111111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111786751111111111111111155125411183973
us-east-1        333333332332222222221112222222222222122111111111
us-east-2        111289912911111111111111111111119911121119991196
us-west-2        222211122111111111111111111111111119413111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
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
| ap-east-1 ape1-az2 | 359 | 65% | 6.6 | 9 (11-01 00:41Z) |
| ap-northeast-1 apne1-az1 | 107 | 8% | 1.7 | 6 (11-01 00:41Z) |
| ap-northeast-1 apne1-az4 | 219 | 25% | 3.4 | 1 (11-01 00:41Z) |
| ap-northeast-2 apne2-az1 | 416 | 61% | 6.5 | 9 (11-01 00:41Z) |
| ap-northeast-2 apne2-az3 | 453 | 68% | 6.9 | 9 (11-01 00:41Z) |
| ap-northeast-2 apne2-az4 | 479 | 68% | 7.1 | 9 (11-01 00:41Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 132 | 5% | 2.3 | 1 (11-01 00:41Z) |
| ap-southeast-2 apse2-az1 | 92 | 2% | 1.2 | 1 (10-31 21:11Z) |
| ap-southeast-2 apse2-az2 | 61 | 0% | 1.0 | 1 (11-01 00:41Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 308 | 39% | 4.4 | 3 (11-01 00:41Z) |
| us-east-1 use1-az1 | 100 | 0% | 1.1 | 1 (10-31 21:11Z) |
| us-east-1 use1-az2 | 133 | 2% | 1.3 | 1 (10-31 17:11Z) |
| us-east-1 use1-az4 | 159 | 23% | 3.0 | 1 (10-31 17:11Z) |
| us-east-1 use1-az5 | 155 | 25% | 3.1 | 1 (10-31 20:13Z) |
| us-east-1 use1-az6 | 118 | 23% | 2.9 | 1 (10-31 23:11Z) |
| us-east-2 use2-az1 | 205 | 41% | 4.5 | 9 (10-31 23:11Z) |
| us-east-2 use2-az2 | 247 | 49% | 5.2 | 9 (10-31 23:11Z) |
| us-east-2 use2-az3 | 274 | 46% | 5.0 | 9 (10-31 23:11Z) |
| us-west-2 usw2-az1 | 152 | 24% | 3.3 | 1 (11-01 00:41Z) |
| us-west-2 usw2-az2 | 117 | 18% | 2.6 | 1 (10-31 21:11Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 486 | 69% | 7.1 | 9 (11-01 00:41Z) |
| ap-northeast-1 | 486 | 72% | 7.0 | 9 (11-01 00:41Z) |
| ap-northeast-2 | 486 | 100% | 9.0 | 9 (11-01 00:41Z) |
| ap-south-1 | 486 | 62% | 6.3 | 9 (11-01 00:41Z) |
| ap-southeast-2 | 486 | 24% | 3.4 | 9 (11-01 00:41Z) |
| ap-southeast-3 | 486 | 26% | 3.3 | 3 (11-01 00:41Z) |
| us-east-1 | 486 | 70% | 6.4 | 9 (11-01 00:41Z) |
| us-east-2 | 486 | 67% | 6.6 | 9 (11-01 00:41Z) |
| us-west-2 | 486 | 52% | 5.6 | 9 (11-01 00:41Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111111111339999999999999999999999999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999111111112211112999999999999799999999999999999
ap-southeast-2   111111111111111111111119999999111319999999999999
ap-southeast-3   111111111111786751111111111111111155125411183973
us-east-1        666699999999932323334339394399999999999322999999
us-east-2        224999999993222222222222228999999999999929991999
us-west-2        455593355999994844395931211233244999549992999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
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
| ap-east-1 ape1-az1 | 311 | 83% | 8.0 | 9 (10-31 23:11Z) |
| ap-east-1 ape1-az2 | 271 | 85% | 8.1 | 9 (10-31 20:13Z) |
| ap-east-1 ape1-az3 | 299 | 85% | 8.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az1 | 204 | 95% | 8.7 | 9 (10-31 23:11Z) |
| ap-northeast-1 apne1-az2 | 174 | 84% | 8.1 | 9 (10-31 22:12Z) |
| ap-northeast-1 apne1-az4 | 259 | 99% | 8.9 | 9 (11-01 00:41Z) |
| ap-northeast-2 apne2-az1 | 398 | 100% | 9.0 | 9 (11-01 00:41Z) |
| ap-northeast-2 apne2-az2 | 104 | 85% | 8.0 | 9 (10-31 20:13Z) |
| ap-northeast-2 apne2-az3 | 417 | 100% | 9.0 | 9 (10-31 22:12Z) |
| ap-northeast-2 apne2-az4 | 314 | 85% | 8.1 | 9 (10-31 23:11Z) |
| ap-south-1 aps1-az1 | 169 | 87% | 8.2 | 9 (11-01 00:41Z) |
| ap-south-1 aps1-az2 | 182 | 80% | 7.7 | 9 (10-31 23:11Z) |
| ap-south-1 aps1-az3 | 188 | 89% | 8.4 | 9 (11-01 00:41Z) |
| ap-southeast-2 apse2-az1 | 58 | 83% | 7.9 | 9 (10-31 20:13Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 103 | 100% | 9.0 | 9 (10-31 20:13Z) |
| us-east-1 use1-az4 | 136 | 91% | 8.4 | 9 (11-01 00:41Z) |
| us-east-1 use1-az5 | 100 | 98% | 8.8 | 9 (11-01 00:41Z) |
| us-east-1 use1-az6 | 120 | 92% | 8.4 | 9 (10-31 12:17Z) |
| us-east-2 use2-az1 | 168 | 99% | 8.9 | 9 (10-31 23:11Z) |
| us-east-2 use2-az2 | 190 | 99% | 8.9 | 9 (10-31 19:10Z) |
| us-east-2 use2-az3 | 217 | 96% | 8.7 | 9 (10-31 23:11Z) |
| us-west-2 usw2-az1 | 91 | 98% | 8.8 | 9 (10-31 20:13Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 123 | 89% | 8.3 | 9 (11-01 00:41Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.701200 | 2026-11-01T00:41:27Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-01T00:41:27Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.740900 | 2026-11-01T00:41:27Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.876200 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.582600 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590700 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.571300 | 2026-11-01T00:41:27Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-01T00:41:27Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.635200 | 2026-11-01T00:41:27Z |
| ap-south-1 | ap-south-1a | Windows | 0.465600 | 2026-11-01T00:41:27Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.534900 | 2026-11-01T00:41:27Z |
| ap-south-1 | ap-south-1b | Windows | 0.380100 | 2026-11-01T00:41:27Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.651400 | 2026-11-01T00:41:27Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.512100 | 2026-11-01T00:41:27Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655600 | 2026-11-01T00:41:27Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.556900 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.570000 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.498000 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.500700 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.548100 | 2026-11-01T00:41:27Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559400 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2a | Windows | 0.638200 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547900 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545400 | 2026-11-01T00:41:27Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.553500 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2a | Windows | 0.313000 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.573100 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2b | Windows | 0.320700 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.543100 | 2026-11-01T00:41:27Z |
| us-west-2 | us-west-2c | Windows | 0.312600 | 2026-11-01T00:41:27Z |
