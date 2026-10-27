# Spot placement score log

Generated 2026-10-27 22:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 388 | 47% | 5.2 | 9 (10-27 22:14Z) |
| ap-northeast-1 | 388 | 17% | 2.9 | 2 (10-27 22:14Z) |
| ap-northeast-2 | 388 | 60% | 6.6 | 9 (10-27 22:14Z) |
| ap-south-1 | 388 | 3% | 1.8 | 1 (10-27 22:14Z) |
| ap-southeast-2 | 388 | 1% | 1.1 | 1 (10-27 22:14Z) |
| ap-southeast-3 | 388 | 28% | 3.6 | 4 (10-27 22:14Z) |
| us-east-1 | 388 | 12% | 2.8 | 3 (10-27 22:14Z) |
| us-east-2 | 388 | 32% | 3.9 | 9 (10-27 22:14Z) |
| us-west-2 | 388 | 11% | 2.3 | 1 (10-27 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111999999999999999919999999999999999999999999999
ap-northeast-1   112121112111128211249999949999192921122113122222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222221111111111114999111691111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   711365118991159911919112858742898861271118648854
us-east-1        213211212111512322223221991993997299921923322233
us-east-2        999111991119911119111199999919399199911196111999
us-west-2        111111312219512112212222222119191911121211111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 124 | 7% | 1.7 | 1 (10-26 23:47Z) |
| ap-east-1 ape1-az2 | 290 | 62% | 6.5 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az1 | 64 | 6% | 1.6 | 1 (10-27 19:14Z) |
| ap-northeast-1 apne1-az4 | 179 | 30% | 3.8 | 1 (10-27 18:18Z) |
| ap-northeast-2 apne2-az1 | 339 | 55% | 6.1 | 9 (10-27 22:14Z) |
| ap-northeast-2 apne2-az3 | 359 | 60% | 6.5 | 9 (10-27 22:14Z) |
| ap-northeast-2 apne2-az4 | 384 | 60% | 6.6 | 9 (10-27 22:14Z) |
| ap-south-1 aps1-az1 | 94 | 1% | 1.5 | 1 (10-27 21:13Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 62 | 3% | 1.3 | 1 (10-27 10:26Z) |
| ap-southeast-2 apse2-az2 | 40 | 0% | 1.0 | 1 (10-27 20:16Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 262 | 39% | 4.6 | 4 (10-27 22:14Z) |
| us-east-1 use1-az1 | 75 | 0% | 1.1 | 1 (10-27 20:16Z) |
| us-east-1 use1-az2 | 103 | 3% | 1.4 | 1 (10-27 21:13Z) |
| us-east-1 use1-az4 | 122 | 30% | 3.5 | 1 (10-27 22:14Z) |
| us-east-1 use1-az5 | 125 | 30% | 3.6 | 1 (10-27 18:18Z) |
| us-east-1 use1-az6 | 91 | 30% | 3.5 | 1 (10-27 16:28Z) |
| us-east-2 use2-az1 | 160 | 46% | 4.9 | 1 (10-27 22:14Z) |
| us-east-2 use2-az2 | 207 | 52% | 5.4 | 9 (10-27 22:14Z) |
| us-east-2 use2-az3 | 237 | 49% | 5.3 | 9 (10-27 22:14Z) |
| us-west-2 usw2-az1 | 135 | 27% | 3.5 | 1 (10-27 18:18Z) |
| us-west-2 usw2-az2 | 85 | 24% | 3.2 | 1 (10-27 10:26Z) |
| us-west-2 usw2-az3 | 146 | 21% | 3.2 | 1 (10-27 22:14Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 388 | 61% | 6.6 | 9 (10-27 22:14Z) |
| ap-northeast-1 | 388 | 74% | 7.2 | 9 (10-27 22:14Z) |
| ap-northeast-2 | 388 | 100% | 9.0 | 9 (10-27 22:14Z) |
| ap-south-1 | 388 | 64% | 6.5 | 9 (10-27 22:14Z) |
| ap-southeast-2 | 388 | 20% | 3.2 | 1 (10-27 22:14Z) |
| ap-southeast-3 | 388 | 28% | 3.6 | 4 (10-27 22:14Z) |
| us-east-1 | 388 | 71% | 6.5 | 6 (10-27 22:14Z) |
| us-east-2 | 388 | 72% | 7.0 | 9 (10-27 22:14Z) |
| us-west-2 | 388 | 52% | 5.7 | 3 (10-27 22:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   123999239992399923999999999999999991999119999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992228229999299999199999999999999999199112119999
ap-southeast-2   111111111111111111111111191999999111111111199111
ap-southeast-3   711365118991159911919112858742898861271118648854
us-east-1        456344436433924656456599999999999999943995544576
us-east-2        999529991299972219522699999919899399999999999999
us-west-2        439433914539993334545345999549999934944591133333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 238 | 77% | 7.6 | 9 (10-27 20:16Z) |
| ap-east-1 ape1-az2 | 200 | 80% | 7.8 | 9 (10-27 19:14Z) |
| ap-east-1 ape1-az3 | 213 | 79% | 7.8 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az1 | 172 | 94% | 8.6 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 219 | 99% | 8.9 | 9 (10-27 22:14Z) |
| ap-northeast-2 apne2-az1 | 309 | 100% | 9.0 | 9 (10-27 22:14Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 334 | 100% | 9.0 | 9 (10-27 22:14Z) |
| ap-northeast-2 apne2-az4 | 238 | 80% | 7.8 | 9 (10-27 20:16Z) |
| ap-south-1 aps1-az1 | 134 | 84% | 8.0 | 9 (10-27 22:14Z) |
| ap-south-1 aps1-az2 | 148 | 76% | 7.5 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az3 | 157 | 88% | 8.3 | 9 (10-27 22:14Z) |
| ap-southeast-2 apse2-az1 | 35 | 71% | 7.2 | 9 (10-27 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 114 | 95% | 8.6 | 9 (10-27 10:26Z) |
| us-east-1 use1-az5 | 82 | 98% | 8.8 | 9 (10-27 10:26Z) |
| us-east-1 use1-az6 | 101 | 96% | 8.7 | 9 (10-27 10:26Z) |
| us-east-2 use2-az1 | 138 | 99% | 8.9 | 9 (10-27 22:14Z) |
| us-east-2 use2-az2 | 171 | 99% | 8.9 | 9 (10-27 20:16Z) |
| us-east-2 use2-az3 | 180 | 96% | 8.7 | 9 (10-27 22:14Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703200 | 2026-10-27T22:14:00Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-27T22:14:00Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.778500 | 2026-10-27T22:14:00Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.959400 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585600 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.586200 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570600 | 2026-10-27T22:14:00Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-27T22:14:00Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.563100 | 2026-10-27T22:14:00Z |
| ap-south-1 | ap-south-1a | Windows | 0.451800 | 2026-10-27T22:14:00Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.642100 | 2026-10-27T22:14:00Z |
| ap-south-1 | ap-south-1b | Windows | 0.408000 | 2026-10-27T22:14:00Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.660600 | 2026-10-27T22:14:00Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.509700 | 2026-10-27T22:14:00Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660800 | 2026-10-27T22:14:00Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556900 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.600600 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.472100 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.511300 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.525800 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.536400 | 2026-10-27T22:14:00Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.563500 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548700 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-27T22:14:00Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.567200 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2a | Windows | 0.320300 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.587100 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2b | Windows | 0.327500 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.564000 | 2026-10-27T22:14:00Z |
| us-west-2 | us-west-2c | Windows | 0.319500 | 2026-10-27T22:14:00Z |
