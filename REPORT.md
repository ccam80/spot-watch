# Spot placement score log

Generated 2026-10-28 11:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 401 | 47% | 5.2 | 9 (10-28 11:16Z) |
| ap-northeast-1 | 401 | 16% | 2.8 | 2 (10-28 11:16Z) |
| ap-northeast-2 | 401 | 61% | 6.6 | 9 (10-28 11:16Z) |
| ap-south-1 | 401 | 3% | 1.8 | 1 (10-28 11:16Z) |
| ap-southeast-2 | 401 | 0% | 1.0 | 1 (10-28 11:16Z) |
| ap-southeast-3 | 401 | 27% | 3.5 | 1 (10-28 11:16Z) |
| us-east-1 | 401 | 12% | 2.7 | 3 (10-28 11:16Z) |
| us-east-2 | 401 | 33% | 3.9 | 1 (10-28 11:16Z) |
| us-west-2 | 401 | 11% | 2.3 | 2 (10-28 11:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999199999999999999999999999999991111119999999
ap-northeast-1   282112499999499991929211221131222222111111111112
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       211111111111149991116911111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   599119191128587428988612711186488541111111111111
us-east-1        123222232219919939972999219233222333111221112233
us-east-2        111191111999999193991999111961119999111911199991
us-west-2        121122122222221191919111212111111111111111211112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 5 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 4 | 5 | 3 | 4 | 3 | 5 | 6 | 8 | 5 | 5 | 8 | 4 | 7 | 4 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 128 | 7% | 1.7 | 1 (10-28 11:16Z) |
| ap-east-1 ape1-az2 | 301 | 62% | 6.4 | 9 (10-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 70 | 6% | 1.6 | 1 (10-28 08:21Z) |
| ap-northeast-1 apne1-az4 | 182 | 29% | 3.8 | 1 (10-28 11:16Z) |
| ap-northeast-2 apne2-az1 | 349 | 54% | 6.1 | 2 (10-28 08:21Z) |
| ap-northeast-2 apne2-az3 | 370 | 61% | 6.5 | 9 (10-28 11:16Z) |
| ap-northeast-2 apne2-az4 | 397 | 61% | 6.7 | 9 (10-28 11:16Z) |
| ap-south-1 aps1-az1 | 99 | 1% | 1.5 | 1 (10-28 11:16Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 68 | 3% | 1.3 | 1 (10-28 08:21Z) |
| ap-southeast-2 apse2-az2 | 42 | 0% | 1.0 | 1 (10-28 06:26Z) |
| ap-southeast-3 apse3-az1 | 77 | 0% | 1.0 | 1 (10-28 11:16Z) |
| ap-southeast-3 apse3-az3 | 265 | 39% | 4.5 | 1 (10-28 04:19Z) |
| us-east-1 use1-az1 | 76 | 0% | 1.1 | 1 (10-28 06:26Z) |
| us-east-1 use1-az2 | 105 | 3% | 1.4 | 1 (10-28 05:16Z) |
| us-east-1 use1-az4 | 125 | 29% | 3.5 | 1 (10-28 06:26Z) |
| us-east-1 use1-az5 | 131 | 29% | 3.5 | 1 (10-28 08:21Z) |
| us-east-1 use1-az6 | 95 | 28% | 3.4 | 1 (10-28 11:16Z) |
| us-east-2 use2-az1 | 166 | 47% | 5.0 | 9 (10-28 10:17Z) |
| us-east-2 use2-az2 | 215 | 53% | 5.5 | 1 (10-28 11:16Z) |
| us-east-2 use2-az3 | 247 | 49% | 5.3 | 9 (10-28 10:17Z) |
| us-west-2 usw2-az1 | 137 | 26% | 3.5 | 1 (10-28 05:16Z) |
| us-west-2 usw2-az2 | 93 | 22% | 3.0 | 1 (10-28 08:21Z) |
| us-west-2 usw2-az3 | 151 | 21% | 3.1 | 1 (10-28 11:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 401 | 62% | 6.7 | 9 (10-28 11:16Z) |
| ap-northeast-1 | 401 | 72% | 7.0 | 7 (10-28 11:16Z) |
| ap-northeast-2 | 401 | 100% | 9.0 | 9 (10-28 11:16Z) |
| ap-south-1 | 401 | 63% | 6.5 | 1 (10-28 11:16Z) |
| ap-southeast-2 | 401 | 20% | 3.2 | 9 (10-28 11:16Z) |
| ap-southeast-3 | 401 | 27% | 3.5 | 1 (10-28 11:16Z) |
| us-east-1 | 401 | 71% | 6.5 | 5 (10-28 11:16Z) |
| us-east-2 | 401 | 73% | 7.0 | 9 (10-28 11:16Z) |
| us-west-2 | 401 | 51% | 5.6 | 9 (10-28 11:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999239999999999999999919991199999999221111112227
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999991999999999999999991991121199999999991111111
ap-southeast-2   111111111111919999991111111111991111111111111999
ap-southeast-3   599119191128587428988612711186488541111111111111
us-east-1        246564565999999999999999439955445766996965445965
us-east-2        722195226999999198993999999999999999999999999999
us-west-2        933345453459995499999349445911333334333333559439
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 3 | 4 | 3 | 4 | 4 | 3 | 6 | 4 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 6 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 249 | 78% | 7.7 | 9 (10-28 11:16Z) |
| ap-east-1 ape1-az2 | 210 | 80% | 7.8 | 9 (10-28 10:17Z) |
| ap-east-1 ape1-az3 | 224 | 80% | 7.8 | 9 (10-28 11:16Z) |
| ap-northeast-1 apne1-az1 | 173 | 94% | 8.6 | 9 (10-27 23:13Z) |
| ap-northeast-1 apne1-az2 | 125 | 78% | 7.7 | 9 (10-27 22:14Z) |
| ap-northeast-1 apne1-az4 | 220 | 99% | 8.9 | 9 (10-27 23:13Z) |
| ap-northeast-2 apne2-az1 | 322 | 100% | 9.0 | 9 (10-28 11:16Z) |
| ap-northeast-2 apne2-az2 | 80 | 80% | 7.7 | 9 (10-27 19:14Z) |
| ap-northeast-2 apne2-az3 | 345 | 100% | 9.0 | 9 (10-28 11:16Z) |
| ap-northeast-2 apne2-az4 | 249 | 81% | 7.9 | 9 (10-28 11:16Z) |
| ap-south-1 aps1-az1 | 138 | 84% | 8.0 | 9 (10-28 03:19Z) |
| ap-south-1 aps1-az2 | 151 | 76% | 7.5 | 9 (10-28 01:18Z) |
| ap-south-1 aps1-az3 | 162 | 88% | 8.3 | 9 (10-28 03:19Z) |
| ap-southeast-2 apse2-az1 | 36 | 72% | 7.3 | 9 (10-28 09:18Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 47 | 72% | 7.3 | 9 (10-28 10:17Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 23 | 52% | 5.5 | 2 (10-28 05:16Z) |
| us-east-1 use1-az2 | 95 | 100% | 9.0 | 9 (10-28 03:19Z) |
| us-east-1 use1-az4 | 116 | 94% | 8.6 | 9 (10-28 09:18Z) |
| us-east-1 use1-az5 | 86 | 98% | 8.8 | 9 (10-28 09:18Z) |
| us-east-1 use1-az6 | 102 | 96% | 8.7 | 9 (10-28 00:41Z) |
| us-east-2 use2-az1 | 148 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az2 | 182 | 99% | 8.9 | 9 (10-28 11:16Z) |
| us-east-2 use2-az3 | 192 | 96% | 8.7 | 9 (10-28 11:16Z) |
| us-west-2 usw2-az1 | 84 | 98% | 8.8 | 9 (10-28 08:21Z) |
| us-west-2 usw2-az2 | 78 | 96% | 8.7 | 9 (10-28 11:16Z) |
| us-west-2 usw2-az3 | 101 | 92% | 8.4 | 9 (10-28 11:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703500 | 2026-10-28T11:16:24Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-28T11:16:24Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.790600 | 2026-10-28T11:16:24Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.973600 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584700 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585700 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-28T11:16:24Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-28T11:16:24Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.571500 | 2026-10-28T11:16:24Z |
| ap-south-1 | ap-south-1a | Windows | 0.456800 | 2026-10-28T11:16:24Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.625500 | 2026-10-28T11:16:24Z |
| ap-south-1 | ap-south-1b | Windows | 0.402700 | 2026-10-28T11:16:24Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.656200 | 2026-10-28T11:16:24Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517700 | 2026-10-28T11:16:24Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.660700 | 2026-10-28T11:16:24Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.560300 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.595800 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.475100 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.524700 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.520500 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.542100 | 2026-10-28T11:16:24Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.564600 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2a | Windows | 0.638800 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.549100 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-10-28T11:16:24Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566000 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2a | Windows | 0.319200 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.586900 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2b | Windows | 0.327200 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.562900 | 2026-10-28T11:16:24Z |
| us-west-2 | us-west-2c | Windows | 0.318800 | 2026-10-28T11:16:24Z |
