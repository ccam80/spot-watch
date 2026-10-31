# Spot placement score log

Generated 2026-10-31 02:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 464 | 48% | 5.2 | 9 (10-31 02:17Z) |
| ap-northeast-1 | 464 | 14% | 2.6 | 1 (10-31 02:17Z) |
| ap-northeast-2 | 464 | 66% | 7.0 | 9 (10-31 02:17Z) |
| ap-south-1 | 464 | 2% | 1.7 | 1 (10-31 02:17Z) |
| ap-southeast-2 | 464 | 0% | 1.0 | 1 (10-31 02:17Z) |
| ap-southeast-3 | 464 | 26% | 3.3 | 1 (10-31 02:17Z) |
| us-east-1 | 464 | 10% | 2.6 | 2 (10-31 02:17Z) |
| us-east-2 | 464 | 29% | 3.6 | 1 (10-31 02:17Z) |
| us-west-2 | 464 | 9% | 2.2 | 1 (10-31 02:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999971111112214421212199999999999999999111111999
ap-northeast-1   111111112222111112222111111111112222871111242111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111111111111111111221111211111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111233211111111111111111178675111111111
us-east-1        122223333323333221111233333333233222222222111222
us-east-2        111141111111111111111111128991291111111111111111
us-west-2        222222111121111112222222221112211111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 6 | 7 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 6 | 8 | 5 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 151 | 6% | 1.6 | 1 (10-31 01:14Z) |
| ap-east-1 ape1-az2 | 343 | 64% | 6.6 | 9 (10-31 02:17Z) |
| ap-northeast-1 apne1-az1 | 98 | 4% | 1.4 | 1 (10-31 02:17Z) |
| ap-northeast-1 apne1-az4 | 208 | 26% | 3.5 | 1 (10-31 00:33Z) |
| ap-northeast-2 apne2-az1 | 402 | 60% | 6.4 | 9 (10-31 02:17Z) |
| ap-northeast-2 apne2-az3 | 433 | 66% | 6.9 | 9 (10-31 02:17Z) |
| ap-northeast-2 apne2-az4 | 460 | 67% | 7.0 | 9 (10-31 02:17Z) |
| ap-south-1 aps1-az1 | 131 | 1% | 1.4 | 1 (10-30 23:11Z) |
| ap-south-1 aps1-az3 | 125 | 6% | 2.4 | 1 (10-31 00:33Z) |
| ap-southeast-2 apse2-az1 | 87 | 2% | 1.2 | 1 (10-31 02:17Z) |
| ap-southeast-2 apse2-az2 | 55 | 0% | 1.0 | 1 (10-31 00:33Z) |
| ap-southeast-3 apse3-az1 | 81 | 0% | 1.0 | 1 (10-31 01:14Z) |
| ap-southeast-3 apse3-az3 | 296 | 39% | 4.4 | 1 (10-30 23:11Z) |
| us-east-1 use1-az1 | 91 | 0% | 1.1 | 1 (10-31 02:17Z) |
| us-east-1 use1-az2 | 124 | 2% | 1.4 | 1 (10-31 01:14Z) |
| us-east-1 use1-az4 | 152 | 24% | 3.0 | 1 (10-31 02:17Z) |
| us-east-1 use1-az5 | 151 | 25% | 3.2 | 1 (10-31 00:33Z) |
| us-east-1 use1-az6 | 109 | 25% | 3.1 | 1 (10-31 01:14Z) |
| us-east-2 use2-az1 | 192 | 42% | 4.6 | 1 (10-31 02:17Z) |
| us-east-2 use2-az2 | 237 | 49% | 5.2 | 1 (10-30 20:12Z) |
| us-east-2 use2-az3 | 271 | 45% | 5.0 | 1 (10-30 22:12Z) |
| us-west-2 usw2-az1 | 146 | 25% | 3.3 | 1 (10-31 00:33Z) |
| us-west-2 usw2-az2 | 114 | 18% | 2.6 | 1 (10-31 02:17Z) |
| us-west-2 usw2-az3 | 183 | 17% | 2.7 | 1 (10-30 23:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 464 | 67% | 7.0 | 9 (10-31 02:17Z) |
| ap-northeast-1 | 464 | 71% | 6.9 | 9 (10-31 02:17Z) |
| ap-northeast-2 | 464 | 100% | 9.0 | 9 (10-31 02:17Z) |
| ap-south-1 | 464 | 61% | 6.2 | 9 (10-31 02:17Z) |
| ap-southeast-2 | 464 | 21% | 3.2 | 9 (10-31 02:17Z) |
| ap-southeast-3 | 464 | 26% | 3.3 | 1 (10-31 02:17Z) |
| us-east-1 | 464 | 69% | 6.3 | 9 (10-31 02:17Z) |
| us-east-2 | 464 | 66% | 6.6 | 2 (10-31 02:17Z) |
| us-west-2 | 464 | 51% | 5.6 | 1 (10-31 02:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111111119999999999999111111111133999999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       971111111111112999999999911111111221111299999999
ap-southeast-2   111111439999999991111111111111111111111111111999
ap-southeast-3   111111111111233211111111111111111178675111111111
us-east-1        666657799565655565454666669999999993232333433939
us-east-2        222299222991222212122222499999999322222222222222
us-west-2        559995544999933444553445559335599999484439593121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 6 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 3 | 5 | 4 | 2 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 6 | 5 | 6 | 7 | 8 | 8 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 6 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 299 | 82% | 7.9 | 9 (10-31 02:17Z) |
| ap-east-1 ape1-az2 | 258 | 84% | 8.0 | 9 (10-31 01:14Z) |
| ap-east-1 ape1-az3 | 285 | 85% | 8.1 | 9 (10-31 02:17Z) |
| ap-northeast-1 apne1-az1 | 198 | 94% | 8.6 | 9 (10-31 00:33Z) |
| ap-northeast-1 apne1-az2 | 164 | 84% | 8.0 | 9 (10-31 02:17Z) |
| ap-northeast-1 apne1-az4 | 248 | 99% | 8.9 | 9 (10-31 02:17Z) |
| ap-northeast-2 apne2-az1 | 382 | 100% | 9.0 | 9 (10-31 02:17Z) |
| ap-northeast-2 apne2-az2 | 96 | 83% | 7.9 | 9 (10-31 01:14Z) |
| ap-northeast-2 apne2-az3 | 407 | 100% | 9.0 | 9 (10-31 02:17Z) |
| ap-northeast-2 apne2-az4 | 305 | 85% | 8.1 | 9 (10-31 02:17Z) |
| ap-south-1 aps1-az1 | 161 | 86% | 8.2 | 9 (10-31 02:17Z) |
| ap-south-1 aps1-az2 | 172 | 78% | 7.7 | 9 (10-31 02:17Z) |
| ap-south-1 aps1-az3 | 178 | 89% | 8.3 | 9 (10-31 01:14Z) |
| ap-southeast-2 apse2-az1 | 53 | 81% | 7.8 | 9 (10-31 01:14Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 61 | 79% | 7.7 | 9 (10-31 02:17Z) |
| ap-southeast-3 apse3-az3 | 73 | 38% | 5.1 | 7 (10-30 16:17Z) |
| us-east-1 use1-az1 | 25 | 48% | 5.2 | 2 (10-29 10:16Z) |
| us-east-1 use1-az2 | 97 | 100% | 9.0 | 9 (10-30 10:16Z) |
| us-east-1 use1-az4 | 127 | 91% | 8.3 | 9 (10-30 11:13Z) |
| us-east-1 use1-az5 | 95 | 98% | 8.8 | 9 (10-30 13:17Z) |
| us-east-1 use1-az6 | 114 | 91% | 8.4 | 9 (10-30 11:13Z) |
| us-east-2 use2-az1 | 158 | 99% | 8.9 | 9 (10-30 11:13Z) |
| us-east-2 use2-az2 | 185 | 99% | 8.9 | 9 (10-30 08:21Z) |
| us-east-2 use2-az3 | 205 | 96% | 8.7 | 9 (10-30 11:13Z) |
| us-west-2 usw2-az1 | 89 | 98% | 8.8 | 9 (10-30 05:16Z) |
| us-west-2 usw2-az2 | 85 | 89% | 8.2 | 9 (10-30 12:24Z) |
| us-west-2 usw2-az3 | 119 | 89% | 8.2 | 9 (10-30 22:12Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.700500 | 2026-10-31T02:17:44Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-31T02:17:44Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.742700 | 2026-10-31T02:17:44Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.908200 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584400 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590200 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572000 | 2026-10-31T02:17:44Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-10-31T02:17:44Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.617700 | 2026-10-31T02:17:44Z |
| ap-south-1 | ap-south-1a | Windows | 0.463000 | 2026-10-31T02:17:44Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.551000 | 2026-10-31T02:17:44Z |
| ap-south-1 | ap-south-1b | Windows | 0.384300 | 2026-10-31T02:17:44Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.652100 | 2026-10-31T02:17:44Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515500 | 2026-10-31T02:17:44Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656600 | 2026-10-31T02:17:44Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.558000 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.571800 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.553500 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.515700 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.509500 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.558300 | 2026-10-31T02:17:44Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554800 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547800 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2b | Windows | 0.637300 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.545100 | 2026-10-31T02:17:44Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.556800 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2a | Windows | 0.314700 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.572900 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2b | Windows | 0.323000 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.547300 | 2026-10-31T02:17:44Z |
| us-west-2 | us-west-2c | Windows | 0.315600 | 2026-10-31T02:17:44Z |
