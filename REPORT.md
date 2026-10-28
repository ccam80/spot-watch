# Spot placement score log

Generated 2026-10-28 05:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 395 | 46% | 5.1 | 9 (10-28 05:16Z) |
| ap-northeast-1 | 395 | 16% | 2.8 | 1 (10-28 05:16Z) |
| ap-northeast-2 | 395 | 61% | 6.6 | 9 (10-28 05:16Z) |
| ap-south-1 | 395 | 3% | 1.8 | 1 (10-28 05:16Z) |
| ap-southeast-2 | 395 | 1% | 1.1 | 1 (10-28 05:16Z) |
| ap-southeast-3 | 395 | 27% | 3.5 | 1 (10-28 05:16Z) |
| us-east-1 | 395 | 12% | 2.7 | 1 (10-28 05:16Z) |
| us-east-2 | 395 | 32% | 3.9 | 1 (10-28 05:16Z) |
| us-west-2 | 395 | 11% | 2.3 | 1 (10-28 05:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999199999999999999999999999999991111119
ap-northeast-1   121111282112499999499991929211221131222222111111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222211111111111149991116911111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   189911599119191128587428988612711186488541111111
us-east-1        121115123222232219919939972999219233222333111221
us-east-2        911199111191111999999193991999111961119999111911
us-west-2        122195121122122222221191919111212111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 7 | 5 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 125 | 7% | 1.7 | 1 (10-28 01:18Z) |
| ap-east-1 ape1-az2 | 295 | 62% | 6.4 | 9 (10-28 05:16Z) |
| ap-northeast-1 apne1-az1 | 68 | 6% | 1.6 | 1 (10-28 04:19Z) |
| ap-northeast-1 apne1-az4 | 181 | 29% | 3.8 | 1 (10-28 05:16Z) |
| ap-northeast-2 apne2-az1 | 346 | 55% | 6.1 | 6 (10-28 05:16Z) |
| ap-northeast-2 apne2-az3 | 365 | 61% | 6.5 | 6 (10-28 05:16Z) |
| ap-northeast-2 apne2-az4 | 391 | 61% | 6.6 | 9 (10-28 05:16Z) |
| ap-south-1 aps1-az1 | 95 | 1% | 1.5 | 1 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 65 | 3% | 1.3 | 1 (10-28 04:19Z) |
| ap-southeast-2 apse2-az2 | 41 | 0% | 1.0 | 1 (10-28 03:19Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 265 | 39% | 4.5 | 1 (10-28 04:19Z) |
| us-east-1 use1-az1 | 75 | 0% | 1.1 | 1 (10-27 20:16Z) |
| us-east-1 use1-az2 | 105 | 3% | 1.4 | 1 (10-28 05:16Z) |
| us-east-1 use1-az4 | 124 | 29% | 3.5 | 1 (10-28 03:19Z) |
| us-east-1 use1-az5 | 130 | 29% | 3.5 | 1 (10-28 05:16Z) |
| us-east-1 use1-az6 | 92 | 29% | 3.5 | 1 (10-28 03:19Z) |
| us-east-2 use2-az1 | 162 | 46% | 4.9 | 4 (10-28 03:19Z) |
| us-east-2 use2-az2 | 210 | 52% | 5.4 | 9 (10-28 03:19Z) |
| us-east-2 use2-az3 | 243 | 49% | 5.3 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az1 | 137 | 26% | 3.5 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az2 | 90 | 22% | 3.0 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az3 | 148 | 21% | 3.1 | 1 (10-28 03:19Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 395 | 61% | 6.7 | 9 (10-28 05:16Z) |
| ap-northeast-1 | 395 | 73% | 7.1 | 1 (10-28 05:16Z) |
| ap-northeast-2 | 395 | 100% | 9.0 | 9 (10-28 05:16Z) |
| ap-south-1 | 395 | 64% | 6.5 | 1 (10-28 05:16Z) |
| ap-southeast-2 | 395 | 19% | 3.2 | 1 (10-28 05:16Z) |
| ap-southeast-3 | 395 | 27% | 3.5 | 1 (10-28 05:16Z) |
| us-east-1 | 395 | 71% | 6.6 | 5 (10-28 05:16Z) |
| us-east-2 | 395 | 72% | 7.0 | 9 (10-28 05:16Z) |
| us-west-2 | 395 | 51% | 5.6 | 3 (10-28 05:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399923999239999999999999999919991199999999221111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       299992999991999999999999999991991121199999999991
ap-southeast-2   111111111111111111919999991111111111991111111111
ap-southeast-3   189911599119191128587428988612711186488541111111
us-east-1        364339246564565999999999999999439955445766996965
us-east-2        912999722195226999999198993999999999999999999999
us-west-2        145399933345453459995499999349445911333334333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 5 | 3 | 5 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 4 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 244 | 78% | 7.7 | 9 (10-28 05:16Z) |
| ap-east-1 ape1-az2 | 205 | 80% | 7.8 | 9 (10-28 05:16Z) |
| ap-east-1 ape1-az3 | 218 | 80% | 7.8 | 9 (10-28 05:16Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 316 | 100% | 9.0 | 9 (10-28 05:16Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 339 | 100% | 9.0 | 9 (10-28 05:16Z) |
| ap-northeast-2 apne2-az4 | 243 | 81% | 7.8 | 9 (10-28 05:16Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 35 | 71% | 7.2 | 9 (10-27 19:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 115 | 94% | 8.6 | 2 (10-28 04:19Z) |
| us-east-1 use1-az5 | 85 | 98% | 8.8 | 9 (10-28 03:19Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 143 | 99% | 8.9 | 9 (10-28 05:16Z) |
| us-east-2 use2-az2 | 176 | 99% | 8.9 | 9 (10-28 05:16Z) |
| us-east-2 use2-az3 | 186 | 96% | 8.7 | 9 (10-28 05:16Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703300 | 2026-10-28T05:16:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T05:16:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.781500 | 2026-10-28T05:16:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.964500 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.585000 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585800 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570600 | 2026-10-28T05:16:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T05:16:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.570800 | 2026-10-28T05:16:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.455600 | 2026-10-28T05:16:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.632800 | 2026-10-28T05:16:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.406100 | 2026-10-28T05:16:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656000 | 2026-10-28T05:16:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513100 | 2026-10-28T05:16:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660400 | 2026-10-28T05:16:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.595800 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.472100 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.519000 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520500 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.536800 | 2026-10-28T05:16:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.564700 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.548700 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-28T05:16:49Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566700 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2a | Windows | 0.320000 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2b | Windows | 0.327500 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.563600 | 2026-10-28T05:16:49Z |
| us-west-2 | us-west-2c | Windows | 0.319200 | 2026-10-28T05:16:49Z |
