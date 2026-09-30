# Spot placement score log

Generated 2026-09-30 20:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 249 | 33% | 4.3 | 1 (09-30 20:24Z) |
| ap-northeast-1 | 249 | 10% | 2.5 | 9 (09-30 20:24Z) |
| ap-northeast-2 | 249 | 39% | 5.3 | 9 (09-30 20:24Z) |
| ap-south-1 | 249 | 2% | 1.8 | 1 (09-30 20:24Z) |
| ap-southeast-2 | 249 | 0% | 1.0 | 1 (09-30 20:24Z) |
| ap-southeast-3 | 249 | 21% | 3.3 | 1 (09-30 20:24Z) |
| us-east-1 | 249 | 8% | 2.4 | 2 (09-30 20:24Z) |
| us-east-2 | 249 | 22% | 3.2 | 1 (09-30 20:24Z) |
| us-west-2 | 249 | 9% | 2.2 | 2 (09-30 20:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999989999911
ap-northeast-1   941221222111211481882137961222122222211118991279
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111221111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   889111111111543788768111118711111111111114765161
us-east-1        111112911111221112211111291222999913222222222322
us-east-2        111111111999999911111191699991119999999111118171
us-west-2        111112211111111112222211111211111121122222222222
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 7 | 7 | 3 | 4 | 4 | 6 | 6 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 4 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 4 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 1 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 4 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 85 | 0% | 1.4 | 1 (09-30 20:24Z) |
| ap-east-1 ape1-az2 | 179 | 46% | 5.5 | 9 (09-30 18:27Z) |
| ap-northeast-1 apne1-az1 | 35 | 0% | 1.3 | 1 (09-30 18:27Z) |
| ap-northeast-1 apne1-az4 | 112 | 15% | 2.9 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az1 | 223 | 38% | 5.2 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az3 | 231 | 42% | 5.4 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az4 | 246 | 39% | 5.3 | 9 (09-30 20:24Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 97 | 3% | 2.5 | 1 (09-30 20:24Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 24 | 0% | 1.0 | 1 (09-30 20:24Z) |
| ap-southeast-3 apse3-az1 | 47 | 0% | 1.0 | 1 (09-30 16:27Z) |
| ap-southeast-3 apse3-az3 | 182 | 27% | 4.0 | 1 (09-30 20:24Z) |
| us-east-1 use1-az1 | 38 | 0% | 1.2 | 1 (09-30 13:26Z) |
| us-east-1 use1-az2 | 72 | 3% | 1.5 | 1 (09-30 19:21Z) |
| us-east-1 use1-az4 | 77 | 22% | 3.1 | 1 (09-30 14:26Z) |
| us-east-1 use1-az5 | 75 | 21% | 3.1 | 1 (09-30 20:24Z) |
| us-east-1 use1-az6 | 57 | 14% | 2.4 | 1 (09-30 19:21Z) |
| us-east-2 use2-az1 | 99 | 31% | 3.9 | 1 (09-30 14:26Z) |
| us-east-2 use2-az2 | 125 | 37% | 4.4 | 1 (09-30 19:21Z) |
| us-east-2 use2-az3 | 146 | 35% | 4.5 | 5 (09-30 19:21Z) |
| us-west-2 usw2-az1 | 78 | 26% | 3.6 | 1 (09-30 20:24Z) |
| us-west-2 usw2-az2 | 48 | 23% | 3.4 | 1 (09-30 18:27Z) |
| us-west-2 usw2-az3 | 106 | 17% | 2.9 | 1 (09-30 19:21Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 249 | 39% | 5.3 | 9 (09-30 20:24Z) |
| ap-northeast-1 | 249 | 74% | 7.2 | 9 (09-30 20:24Z) |
| ap-northeast-2 | 249 | 100% | 9.0 | 9 (09-30 20:24Z) |
| ap-south-1 | 249 | 56% | 6.0 | 2 (09-30 20:24Z) |
| ap-southeast-2 | 249 | 16% | 3.2 | 2 (09-30 20:24Z) |
| ap-southeast-3 | 249 | 21% | 3.3 | 1 (09-30 20:24Z) |
| us-east-1 | 249 | 72% | 6.7 | 3 (09-30 20:24Z) |
| us-east-2 | 249 | 75% | 7.3 | 3 (09-30 20:24Z) |
| us-west-2 | 249 | 54% | 5.8 | 5 (09-30 20:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999333522233389999999999999222332234437999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999421711152999999999999999111111111111992
ap-southeast-2   212222222222222295922922112222222222222222222222
ap-southeast-3   889111111111543788768111118711111111111114765161
us-east-1        433698957948995944544359593655999936554443334433
us-east-2        233223999999999933433399999999999999999832929983
us-west-2        322444422992244945355532243533324253455455444445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 6 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 3 | 6 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 6 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 4 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 139 | 61% | 6.7 | 9 (09-30 20:24Z) |
| ap-east-1 ape1-az2 | 110 | 63% | 6.8 | 9 (09-30 20:24Z) |
| ap-east-1 ape1-az3 | 107 | 59% | 6.5 | 9 (09-30 20:24Z) |
| ap-northeast-1 apne1-az1 | 119 | 92% | 8.5 | 9 (09-30 20:24Z) |
| ap-northeast-1 apne1-az2 | 53 | 51% | 6.1 | 9 (09-30 20:24Z) |
| ap-northeast-1 apne1-az4 | 147 | 99% | 9.0 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az1 | 194 | 100% | 9.0 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 224 | 100% | 9.0 | 9 (09-30 20:24Z) |
| ap-northeast-2 apne2-az4 | 133 | 65% | 6.9 | 9 (09-30 20:24Z) |
| ap-south-1 aps1-az1 | 72 | 69% | 7.2 | 9 (09-30 04:28Z) |
| ap-south-1 aps1-az2 | 87 | 59% | 6.5 | 9 (09-30 19:21Z) |
| ap-south-1 aps1-az3 | 96 | 81% | 7.9 | 9 (09-30 19:21Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 52 | 21% | 4.2 | 4 (09-30 14:26Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 90 | 97% | 8.8 | 2 (09-30 08:33Z) |
| us-east-1 use1-az5 | 51 | 98% | 8.9 | 9 (09-30 06:39Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 94 | 99% | 8.9 | 9 (09-30 11:20Z) |
| us-east-2 use2-az2 | 131 | 98% | 8.9 | 9 (09-30 15:25Z) |
| us-east-2 use2-az3 | 121 | 93% | 8.6 | 9 (09-30 11:20Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 59 | 95% | 8.6 | 2 (09-30 12:38Z) |
| us-west-2 usw2-az3 | 75 | 95% | 8.6 | 2 (09-30 13:26Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.731100 | 2026-09-30T20:24:33Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.852600 | 2026-09-30T20:24:33Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.774000 | 2026-09-30T20:24:33Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.962800 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593100 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.576900 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566200 | 2026-09-30T20:24:33Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-09-30T20:24:33Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.617600 | 2026-09-30T20:24:33Z |
| ap-south-1 | ap-south-1a | Windows | 0.354000 | 2026-09-30T20:24:33Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.654100 | 2026-09-30T20:24:33Z |
| ap-south-1 | ap-south-1b | Windows | 0.351100 | 2026-09-30T20:24:33Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729100 | 2026-09-30T20:24:33Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-09-30T20:24:33Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.613900 | 2026-09-30T20:24:33Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.580200 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1a | Windows | 0.303200 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.450800 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.450600 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.396300 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438800 | 2026-09-30T20:24:33Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529400 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2a | Windows | 0.640700 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523200 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2b | Windows | 0.640500 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514500 | 2026-09-30T20:24:33Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.511800 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.502800 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2b | Windows | 0.332300 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-30T20:24:33Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-30T20:24:33Z |
