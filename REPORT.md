# Spot placement score log

Generated 2026-10-27 16:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 382 | 46% | 5.1 | 9 (10-27 16:28Z) |
| ap-northeast-1 | 382 | 17% | 2.9 | 3 (10-27 16:28Z) |
| ap-northeast-2 | 382 | 59% | 6.5 | 9 (10-27 16:28Z) |
| ap-south-1 | 382 | 3% | 1.8 | 1 (10-27 16:28Z) |
| ap-southeast-2 | 382 | 1% | 1.1 | 1 (10-27 16:28Z) |
| ap-southeast-3 | 382 | 27% | 3.5 | 8 (10-27 16:28Z) |
| us-east-1 | 382 | 13% | 2.8 | 3 (10-27 16:28Z) |
| us-east-2 | 382 | 32% | 3.9 | 6 (10-27 16:28Z) |
| us-west-2 | 382 | 11% | 2.3 | 1 (10-27 16:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999111999999999999999919999999999999999999999
ap-northeast-1   222198112121112111128211249999949999192921122113
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222221111111111114999111691111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   881178711365118991159911919112858742898861271118
us-east-1        999911213211212111512322223221991993997299921923
us-east-2        999911999111991119911119111199999919399199911196
us-west-2        921121111111312219512112212222222119191911121211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 5 | 3 | 3 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 124 | 7% | 1.7 | 1 (10-26 23:47Z) |
| ap-east-1 ape1-az2 | 284 | 62% | 6.4 | 9 (10-27 16:28Z) |
| ap-northeast-1 apne1-az1 | 63 | 6% | 1.7 | 1 (10-27 10:26Z) |
| ap-northeast-1 apne1-az4 | 177 | 30% | 3.9 | 2 (10-27 16:28Z) |
| ap-northeast-2 apne2-az1 | 333 | 54% | 6.1 | 9 (10-27 16:28Z) |
| ap-northeast-2 apne2-az3 | 353 | 59% | 6.5 | 9 (10-27 16:28Z) |
| ap-northeast-2 apne2-az4 | 378 | 60% | 6.6 | 9 (10-27 16:28Z) |
| ap-south-1 aps1-az1 | 91 | 1% | 1.5 | 1 (10-27 16:28Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 62 | 3% | 1.3 | 1 (10-27 10:26Z) |
| ap-southeast-2 apse2-az2 | 39 | 0% | 1.0 | 1 (10-27 04:53Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 256 | 39% | 4.6 | 8 (10-27 16:28Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 100 | 3% | 1.5 | 1 (10-26 19:12Z) |
| us-east-1 use1-az4 | 119 | 30% | 3.6 | 1 (10-27 04:53Z) |
| us-east-1 use1-az5 | 124 | 31% | 3.7 | 9 (10-27 04:53Z) |
| us-east-1 use1-az6 | 91 | 30% | 3.5 | 1 (10-27 16:28Z) |
| us-east-2 use2-az1 | 158 | 47% | 5.0 | 8 (10-27 10:26Z) |
| us-east-2 use2-az2 | 203 | 51% | 5.4 | 2 (10-27 16:28Z) |
| us-east-2 use2-az3 | 233 | 49% | 5.3 | 9 (10-27 10:26Z) |
| us-west-2 usw2-az1 | 134 | 27% | 3.5 | 1 (10-26 23:47Z) |
| us-west-2 usw2-az2 | 85 | 24% | 3.2 | 1 (10-27 10:26Z) |
| us-west-2 usw2-az3 | 142 | 22% | 3.2 | 1 (10-27 16:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 382 | 60% | 6.6 | 9 (10-27 16:28Z) |
| ap-northeast-1 | 382 | 74% | 7.2 | 9 (10-27 16:28Z) |
| ap-northeast-2 | 382 | 100% | 9.0 | 9 (10-27 16:28Z) |
| ap-south-1 | 382 | 64% | 6.5 | 2 (10-27 16:28Z) |
| ap-southeast-2 | 382 | 19% | 3.2 | 1 (10-27 16:28Z) |
| ap-southeast-3 | 382 | 27% | 3.5 | 8 (10-27 16:28Z) |
| us-east-1 | 382 | 71% | 6.6 | 5 (10-27 16:28Z) |
| us-east-2 | 382 | 71% | 6.9 | 9 (10-27 16:28Z) |
| us-west-2 | 382 | 53% | 5.7 | 1 (10-27 16:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   993299123999239992399923999999999999999991999119
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999299992228229999299999199999999999999999199112
ap-southeast-2   911191111111111111111111111111191999999111111111
ap-southeast-3   881178711365118991159911919112858742898861271118
us-east-1        999946456344436433924656456599999999999999943995
us-east-2        999923999529991299972219522699999919899399999999
us-west-2        999953439433914539993334545345999549999934944591
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 8 | 8 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 235 | 77% | 7.6 | 9 (10-27 16:28Z) |
| ap-east-1 ape1-az2 | 197 | 79% | 7.8 | 9 (10-27 16:28Z) |
| ap-east-1 ape1-az3 | 207 | 79% | 7.7 | 9 (10-27 16:28Z) |
| ap-northeast-1 apne1-az1 | 169 | 93% | 8.6 | 9 (10-26 19:12Z) |
| ap-northeast-1 apne1-az2 | 120 | 78% | 7.6 | 9 (10-27 16:28Z) |
| ap-northeast-1 apne1-az4 | 214 | 99% | 8.9 | 9 (10-27 16:28Z) |
| ap-northeast-2 apne2-az1 | 304 | 100% | 9.0 | 9 (10-27 16:28Z) |
| ap-northeast-2 apne2-az2 | 79 | 80% | 7.7 | 9 (10-26 19:12Z) |
| ap-northeast-2 apne2-az3 | 328 | 100% | 9.0 | 9 (10-27 16:28Z) |
| ap-northeast-2 apne2-az4 | 234 | 80% | 7.8 | 9 (10-27 16:28Z) |
| ap-south-1 aps1-az1 | 132 | 83% | 8.0 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az2 | 148 | 76% | 7.5 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 114 | 95% | 8.6 | 9 (10-27 10:26Z) |
| us-east-1 use1-az5 | 82 | 98% | 8.8 | 9 (10-27 10:26Z) |
| us-east-1 use1-az6 | 101 | 96% | 8.7 | 9 (10-27 10:26Z) |
| us-east-2 use2-az1 | 133 | 98% | 8.9 | 9 (10-27 16:28Z) |
| us-east-2 use2-az2 | 168 | 99% | 8.9 | 9 (10-27 04:53Z) |
| us-east-2 use2-az3 | 174 | 95% | 8.7 | 9 (10-27 16:28Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703200 | 2026-10-27T16:28:34Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-27T16:28:34Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.774500 | 2026-10-27T16:28:34Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.959400 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.586300 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570400 | 2026-10-27T16:28:34Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-27T16:28:34Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.563100 | 2026-10-27T16:28:34Z |
| ap-south-1 | ap-south-1a | Windows | 0.449300 | 2026-10-27T16:28:34Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.653100 | 2026-10-27T16:28:34Z |
| ap-south-1 | ap-south-1b | Windows | 0.408600 | 2026-10-27T16:28:34Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.661600 | 2026-10-27T16:28:34Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509700 | 2026-10-27T16:28:34Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660800 | 2026-10-27T16:28:34Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556900 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.603100 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.468800 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.500300 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.525800 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.539600 | 2026-10-27T16:28:34Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.563500 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548500 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547700 | 2026-10-27T16:28:34Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.567600 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2a | Windows | 0.320300 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.581300 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2b | Windows | 0.327600 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.564500 | 2026-10-27T16:28:34Z |
| us-west-2 | us-west-2c | Windows | 0.319700 | 2026-10-27T16:28:34Z |
