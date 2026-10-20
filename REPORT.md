# Spot placement score log

Generated 2026-10-20 23:48 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 346 | 41% | 4.7 | 9 (10-20 23:48Z) |
| ap-northeast-1 | 346 | 15% | 2.8 | 1 (10-20 23:48Z) |
| ap-northeast-2 | 346 | 55% | 6.3 | 9 (10-20 23:48Z) |
| ap-south-1 | 346 | 2% | 1.8 | 2 (10-20 23:48Z) |
| ap-southeast-2 | 346 | 1% | 1.1 | 1 (10-20 23:48Z) |
| ap-southeast-3 | 346 | 25% | 3.4 | 5 (10-20 23:48Z) |
| us-east-1 | 346 | 10% | 2.6 | 1 (10-20 23:48Z) |
| us-east-2 | 346 | 30% | 3.7 | 1 (10-20 23:48Z) |
| us-west-2 | 346 | 11% | 2.3 | 1 (10-20 23:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999111999
ap-northeast-1   192212121114221142111132212932416591222198112121
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222111112222222111222222222222222222222222222
ap-southeast-2   111111111111111111111111119119111111111111111111
ap-southeast-3   395151122111131151821438751867992474881178711365
us-east-1        233222113333232132312222233322192399999911213211
us-east-2        999911112991112911199911116199999919999911999111
us-west-2        111111111111111122111122211212121911921121111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 4 | 7 | 5 | 4 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 121 | 7% | 1.7 | 1 (10-20 20:29Z) |
| ap-east-1 ape1-az2 | 249 | 56% | 6.0 | 9 (10-20 23:48Z) |
| ap-northeast-1 apne1-az1 | 55 | 7% | 1.7 | 1 (10-20 23:48Z) |
| ap-northeast-1 apne1-az4 | 160 | 26% | 3.6 | 1 (10-20 05:56Z) |
| ap-northeast-2 apne2-az1 | 300 | 50% | 5.9 | 9 (10-20 23:48Z) |
| ap-northeast-2 apne2-az3 | 318 | 55% | 6.2 | 9 (10-20 23:48Z) |
| ap-northeast-2 apne2-az4 | 343 | 55% | 6.3 | 9 (10-20 23:48Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 114 | 3% | 2.3 | 1 (10-20 23:48Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 34 | 0% | 1.0 | 1 (10-20 23:48Z) |
| ap-southeast-3 apse3-az1 | 74 | 0% | 1.0 | 1 (10-20 20:29Z) |
| ap-southeast-3 apse3-az3 | 235 | 34% | 4.3 | 5 (10-20 23:48Z) |
| us-east-1 use1-az1 | 67 | 0% | 1.1 | 1 (10-20 23:48Z) |
| us-east-1 use1-az2 | 98 | 3% | 1.5 | 1 (10-20 20:29Z) |
| us-east-1 use1-az4 | 105 | 30% | 3.7 | 1 (10-20 11:25Z) |
| us-east-1 use1-az5 | 110 | 28% | 3.5 | 8 (10-19 07:40Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 139 | 44% | 4.8 | 9 (10-20 11:25Z) |
| us-east-2 use2-az2 | 182 | 47% | 5.1 | 1 (10-20 20:29Z) |
| us-east-2 use2-az3 | 211 | 46% | 5.1 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az1 | 126 | 26% | 3.5 | 1 (10-20 20:29Z) |
| us-west-2 usw2-az2 | 74 | 24% | 3.3 | 1 (10-20 23:48Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 346 | 56% | 6.3 | 9 (10-20 23:48Z) |
| ap-northeast-1 | 346 | 73% | 7.2 | 9 (10-20 23:48Z) |
| ap-northeast-2 | 346 | 100% | 9.0 | 9 (10-20 23:48Z) |
| ap-south-1 | 346 | 62% | 6.4 | 8 (10-20 23:48Z) |
| ap-southeast-2 | 346 | 19% | 3.3 | 1 (10-20 23:48Z) |
| ap-southeast-3 | 346 | 25% | 3.4 | 5 (10-20 23:48Z) |
| us-east-1 | 346 | 71% | 6.6 | 4 (10-20 23:48Z) |
| us-east-2 | 346 | 71% | 6.9 | 9 (10-20 23:48Z) |
| us-west-2 | 346 | 52% | 5.7 | 3 (10-20 23:48Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999992399239992199911999999999999999993299123999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999299199912299229991299999999999999999299992228
ap-southeast-2   911111111111811111111111199999999999911191111111
ap-southeast-3   395151122111131151821438751867992474881178711365
us-east-1        999945426664355554679344659999999999999946456344
us-east-2        999911912991122911199931139999999999999923999529
us-west-2        359299442495343355433445443999999999999953439433
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 213 | 75% | 7.5 | 9 (10-20 23:48Z) |
| ap-east-1 ape1-az2 | 177 | 77% | 7.6 | 9 (10-20 23:48Z) |
| ap-east-1 ape1-az3 | 181 | 76% | 7.5 | 9 (10-20 23:48Z) |
| ap-northeast-1 apne1-az1 | 159 | 93% | 8.6 | 9 (10-20 20:29Z) |
| ap-northeast-1 apne1-az2 | 102 | 74% | 7.4 | 9 (10-20 23:48Z) |
| ap-northeast-1 apne1-az4 | 197 | 98% | 8.9 | 9 (10-20 23:48Z) |
| ap-northeast-2 apne2-az1 | 271 | 100% | 9.0 | 9 (10-20 23:48Z) |
| ap-northeast-2 apne2-az2 | 73 | 79% | 7.7 | 9 (10-20 20:29Z) |
| ap-northeast-2 apne2-az3 | 299 | 100% | 9.0 | 9 (10-20 23:48Z) |
| ap-northeast-2 apne2-az4 | 209 | 78% | 7.7 | 9 (10-20 23:48Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 125 | 71% | 7.3 | 9 (10-20 00:15Z) |
| ap-south-1 aps1-az3 | 142 | 87% | 8.2 | 9 (10-20 05:56Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 65 | 31% | 4.7 | 3 (10-20 16:52Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 119 | 98% | 8.9 | 9 (10-20 23:48Z) |
| us-east-2 use2-az2 | 161 | 99% | 8.9 | 9 (10-20 11:25Z) |
| us-east-2 use2-az3 | 156 | 95% | 8.6 | 9 (10-20 23:48Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 74 | 96% | 8.7 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 92 | 95% | 8.6 | 9 (10-20 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.710800 | 2026-10-20T23:48:16Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-20T23:48:16Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.772200 | 2026-10-20T23:48:16Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.955100 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584800 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581200 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565500 | 2026-10-20T23:48:16Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-10-20T23:48:16Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.561400 | 2026-10-20T23:48:16Z |
| ap-south-1 | ap-south-1a | Windows | 0.390700 | 2026-10-20T23:48:16Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.775500 | 2026-10-20T23:48:16Z |
| ap-south-1 | ap-south-1b | Windows | 0.368000 | 2026-10-20T23:48:16Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.681400 | 2026-10-20T23:48:16Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.489600 | 2026-10-20T23:48:16Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.662600 | 2026-10-20T23:48:16Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.543000 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.479200 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.507800 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.504000 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.444600 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.490100 | 2026-10-20T23:48:16Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.560100 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2a | Windows | 0.641300 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545600 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2b | Windows | 0.639100 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.543200 | 2026-10-20T23:48:16Z |
| us-east-2 | us-east-2c | Windows | 0.637400 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.551700 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2a | Windows | 0.315700 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.543900 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2b | Windows | 0.329400 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528400 | 2026-10-20T23:48:16Z |
| us-west-2 | us-west-2c | Windows | 0.315000 | 2026-10-20T23:48:16Z |
