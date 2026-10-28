# Spot placement score log

Generated 2026-10-28 04:19 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 394 | 46% | 5.1 | 1 (10-28 04:19Z) |
| ap-northeast-1 | 394 | 16% | 2.8 | 1 (10-28 04:19Z) |
| ap-northeast-2 | 394 | 60% | 6.6 | 9 (10-28 04:19Z) |
| ap-south-1 | 394 | 3% | 1.8 | 1 (10-28 04:19Z) |
| ap-southeast-2 | 394 | 1% | 1.1 | 1 (10-28 04:19Z) |
| ap-southeast-3 | 394 | 27% | 3.5 | 1 (10-28 04:19Z) |
| us-east-1 | 394 | 12% | 2.7 | 2 (10-28 04:19Z) |
| us-east-2 | 394 | 32% | 3.9 | 1 (10-28 04:19Z) |
| us-west-2 | 394 | 11% | 2.3 | 1 (10-28 04:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999919999999999999999999999999999111111
ap-northeast-1   112111128211249999949999192921122113122222211111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222221111111111114999111691111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   118991159911919112858742898861271118648854111111
us-east-1        212111512322223221991993997299921923322233311122
us-east-2        991119911119111199999919399199911196111999911191
us-west-2        312219512112212222222119191911121211111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 125 | 7% | 1.7 | 1 (10-28 01:18Z) |
| ap-east-1 ape1-az2 | 294 | 62% | 6.4 | 1 (10-28 04:19Z) |
| ap-northeast-1 apne1-az1 | 68 | 6% | 1.6 | 1 (10-28 04:19Z) |
| ap-northeast-1 apne1-az4 | 180 | 29% | 3.8 | 1 (10-28 02:22Z) |
| ap-northeast-2 apne2-az1 | 345 | 55% | 6.1 | 1 (10-28 04:19Z) |
| ap-northeast-2 apne2-az3 | 364 | 61% | 6.5 | 8 (10-28 04:19Z) |
| ap-northeast-2 apne2-az4 | 390 | 61% | 6.6 | 9 (10-28 04:19Z) |
| ap-south-1 aps1-az1 | 95 | 1% | 1.5 | 1 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 65 | 3% | 1.3 | 1 (10-28 04:19Z) |
| ap-southeast-2 apse2-az2 | 41 | 0% | 1.0 | 1 (10-28 03:19Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 265 | 39% | 4.5 | 1 (10-28 04:19Z) |
| us-east-1 use1-az1 | 75 | 0% | 1.1 | 1 (10-27 20:16Z) |
| us-east-1 use1-az2 | 104 | 3% | 1.4 | 1 (10-28 02:22Z) |
| us-east-1 use1-az4 | 124 | 29% | 3.5 | 1 (10-28 03:19Z) |
| us-east-1 use1-az5 | 129 | 29% | 3.6 | 1 (10-28 04:19Z) |
| us-east-1 use1-az6 | 92 | 29% | 3.5 | 1 (10-28 03:19Z) |
| us-east-2 use2-az1 | 162 | 46% | 4.9 | 4 (10-28 03:19Z) |
| us-east-2 use2-az2 | 210 | 52% | 5.4 | 9 (10-28 03:19Z) |
| us-east-2 use2-az3 | 242 | 49% | 5.3 | 1 (10-28 04:19Z) |
| us-west-2 usw2-az1 | 136 | 26% | 3.5 | 1 (10-28 02:22Z) |
| us-west-2 usw2-az2 | 89 | 22% | 3.1 | 1 (10-28 04:19Z) |
| us-west-2 usw2-az3 | 148 | 21% | 3.1 | 1 (10-28 03:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 394 | 61% | 6.7 | 9 (10-28 04:19Z) |
| ap-northeast-1 | 394 | 73% | 7.1 | 1 (10-28 04:19Z) |
| ap-northeast-2 | 394 | 100% | 9.0 | 9 (10-28 04:19Z) |
| ap-south-1 | 394 | 64% | 6.6 | 9 (10-28 04:19Z) |
| ap-southeast-2 | 394 | 19% | 3.2 | 1 (10-28 04:19Z) |
| ap-southeast-3 | 394 | 27% | 3.5 | 1 (10-28 04:19Z) |
| us-east-1 | 394 | 71% | 6.6 | 6 (10-28 04:19Z) |
| us-east-2 | 394 | 72% | 7.0 | 9 (10-28 04:19Z) |
| us-west-2 | 394 | 51% | 5.7 | 3 (10-28 04:19Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   239992399923999999999999999991999119999999922111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       229999299999199999999999999999199112119999999999
ap-southeast-2   111111111111111111191999999111111111199111111111
ap-southeast-3   118991159911919112858742898861271118648854111111
us-east-1        436433924656456599999999999999943995544576699696
us-east-2        991299972219522699999919899399999999999999999999
us-west-2        914539993334545345999549999934944591133333433333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 243 | 78% | 7.7 | 9 (10-28 04:19Z) |
| ap-east-1 ape1-az2 | 204 | 80% | 7.8 | 9 (10-28 04:19Z) |
| ap-east-1 ape1-az3 | 217 | 80% | 7.8 | 9 (10-28 04:19Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 315 | 100% | 9.0 | 9 (10-28 04:19Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 338 | 100% | 9.0 | 9 (10-28 04:19Z) |
| ap-northeast-2 apne2-az4 | 242 | 81% | 7.8 | 9 (10-28 04:19Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 35 | 71% | 7.2 | 9 (10-27 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 115 | 94% | 8.6 | 2 (10-28 04:19Z) |
| us-east-1 use1-az5 | 85 | 98% | 8.8 | 9 (10-28 03:19Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 142 | 99% | 8.9 | 9 (10-28 04:19Z) |
| us-east-2 use2-az2 | 175 | 99% | 8.9 | 9 (10-28 04:19Z) |
| us-east-2 use2-az3 | 185 | 96% | 8.7 | 9 (10-28 04:19Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703300 | 2026-10-28T04:19:28Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T04:19:28Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.781500 | 2026-10-28T04:19:28Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964500 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585000 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570600 | 2026-10-28T04:19:28Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T04:19:28Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.570800 | 2026-10-28T04:19:28Z |
| ap-south-1 | ap-south-1a | Windows | 0.451800 | 2026-10-28T04:19:28Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.632800 | 2026-10-28T04:19:28Z |
| ap-south-1 | ap-south-1b | Windows | 0.406100 | 2026-10-28T04:19:28Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656000 | 2026-10-28T04:19:28Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513100 | 2026-10-28T04:19:28Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660400 | 2026-10-28T04:19:28Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.595800 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.472100 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.519000 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.524500 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.536800 | 2026-10-28T04:19:28Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.564700 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548700 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-28T04:19:28Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.567200 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2a | Windows | 0.320000 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.587100 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2b | Windows | 0.327500 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.563600 | 2026-10-28T04:19:28Z |
| us-west-2 | us-west-2c | Windows | 0.319200 | 2026-10-28T04:19:28Z |
