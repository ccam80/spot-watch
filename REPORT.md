# Spot placement score log

Generated 2026-10-27 04:53 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 380 | 46% | 5.1 | 9 (10-27 04:53Z) |
| ap-northeast-1 | 380 | 17% | 2.9 | 1 (10-27 04:53Z) |
| ap-northeast-2 | 380 | 59% | 6.5 | 9 (10-27 04:53Z) |
| ap-south-1 | 380 | 3% | 1.8 | 1 (10-27 04:53Z) |
| ap-southeast-2 | 380 | 1% | 1.1 | 1 (10-27 04:53Z) |
| ap-southeast-3 | 380 | 27% | 3.5 | 1 (10-27 04:53Z) |
| us-east-1 | 380 | 13% | 2.8 | 9 (10-27 04:53Z) |
| us-east-2 | 380 | 32% | 3.9 | 1 (10-27 04:53Z) |
| us-west-2 | 380 | 11% | 2.3 | 2 (10-27 04:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991119999999999999999199999999999999999999
ap-northeast-1   912221981121211121111282112499999499991929211221
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222211111111111149991116911111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   748811787113651189911599119191128587428988612711
us-east-1        999999112132112121115123222232219919939972999219
us-east-2        199999119991119911199111191111999999193991999111
us-west-2        119211211111113122195121122122222221191919111212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
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
| ap-east-1 ape1-az2 | 282 | 61% | 6.4 | 9 (10-27 04:53Z) |
| ap-northeast-1 apne1-az1 | 62 | 6% | 1.7 | 1 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 176 | 30% | 3.9 | 1 (10-26 23:47Z) |
| ap-northeast-2 apne2-az1 | 331 | 54% | 6.1 | 9 (10-27 04:53Z) |
| ap-northeast-2 apne2-az3 | 351 | 59% | 6.5 | 9 (10-27 04:53Z) |
| ap-northeast-2 apne2-az4 | 376 | 59% | 6.5 | 9 (10-27 04:53Z) |
| ap-south-1 aps1-az1 | 90 | 1% | 1.5 | 1 (10-25 18:58Z) |
| ap-south-1 aps1-az3 | 121 | 6% | 2.5 | 1 (10-26 23:47Z) |
| ap-southeast-2 apse2-az1 | 61 | 3% | 1.3 | 1 (10-26 12:49Z) |
| ap-southeast-2 apse2-az2 | 39 | 0% | 1.0 | 1 (10-27 04:53Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 255 | 38% | 4.5 | 7 (10-26 19:12Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 100 | 3% | 1.5 | 1 (10-26 19:12Z) |
| us-east-1 use1-az4 | 119 | 30% | 3.6 | 1 (10-27 04:53Z) |
| us-east-1 use1-az5 | 124 | 31% | 3.7 | 9 (10-27 04:53Z) |
| us-east-1 use1-az6 | 90 | 30% | 3.5 | 9 (10-27 04:53Z) |
| us-east-2 use2-az1 | 157 | 46% | 5.0 | 1 (10-27 04:53Z) |
| us-east-2 use2-az2 | 201 | 51% | 5.4 | 9 (10-26 12:49Z) |
| us-east-2 use2-az3 | 232 | 49% | 5.3 | 1 (10-26 19:12Z) |
| us-west-2 usw2-az1 | 134 | 27% | 3.5 | 1 (10-26 23:47Z) |
| us-west-2 usw2-az2 | 84 | 24% | 3.2 | 9 (10-25 21:41Z) |
| us-west-2 usw2-az3 | 141 | 22% | 3.2 | 1 (10-27 04:53Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 380 | 60% | 6.6 | 9 (10-27 04:53Z) |
| ap-northeast-1 | 380 | 74% | 7.2 | 1 (10-27 04:53Z) |
| ap-northeast-2 | 380 | 100% | 9.0 | 9 (10-27 04:53Z) |
| ap-south-1 | 380 | 64% | 6.5 | 1 (10-27 04:53Z) |
| ap-southeast-2 | 380 | 19% | 3.2 | 1 (10-27 04:53Z) |
| ap-southeast-3 | 380 | 27% | 3.5 | 1 (10-27 04:53Z) |
| us-east-1 | 380 | 71% | 6.6 | 9 (10-27 04:53Z) |
| us-east-2 | 380 | 71% | 6.9 | 9 (10-27 04:53Z) |
| us-west-2 | 380 | 53% | 5.7 | 5 (10-27 04:53Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999932991239992399923999239999999999999999919991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999992999922282299992999991999999999999999991991
ap-southeast-2   999111911111111111111111111111111919999991111111
ap-southeast-3   748811787113651189911599119191128587428988612711
us-east-1        999999464563444364339246564565999999999999999439
us-east-2        999999239995299912999722195226999999198993999999
us-west-2        999999534394339145399933345453459995499999349445
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
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
| ap-east-1 ape1-az1 | 233 | 77% | 7.6 | 9 (10-27 04:53Z) |
| ap-east-1 ape1-az2 | 196 | 79% | 7.7 | 9 (10-26 23:47Z) |
| ap-east-1 ape1-az3 | 205 | 79% | 7.7 | 9 (10-27 04:53Z) |
| ap-northeast-1 apne1-az1 | 169 | 93% | 8.6 | 9 (10-26 19:12Z) |
| ap-northeast-1 apne1-az2 | 119 | 77% | 7.6 | 9 (10-26 23:47Z) |
| ap-northeast-1 apne1-az4 | 213 | 99% | 8.9 | 9 (10-25 18:58Z) |
| ap-northeast-2 apne2-az1 | 302 | 100% | 9.0 | 9 (10-27 04:53Z) |
| ap-northeast-2 apne2-az2 | 79 | 80% | 7.7 | 9 (10-26 19:12Z) |
| ap-northeast-2 apne2-az3 | 326 | 100% | 9.0 | 9 (10-27 04:53Z) |
| ap-northeast-2 apne2-az4 | 232 | 80% | 7.8 | 9 (10-27 04:53Z) |
| ap-south-1 aps1-az1 | 132 | 83% | 8.0 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az2 | 148 | 76% | 7.5 | 9 (10-26 23:47Z) |
| ap-south-1 aps1-az3 | 155 | 88% | 8.3 | 9 (10-25 21:41Z) |
| ap-southeast-2 apse2-az1 | 34 | 71% | 7.2 | 9 (10-25 16:03Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 94 | 100% | 9.0 | 9 (10-26 00:11Z) |
| us-east-1 use1-az4 | 113 | 95% | 8.6 | 9 (10-26 12:49Z) |
| us-east-1 use1-az5 | 81 | 98% | 8.8 | 9 (10-27 04:53Z) |
| us-east-1 use1-az6 | 100 | 96% | 8.7 | 9 (10-27 04:53Z) |
| us-east-2 use2-az1 | 131 | 98% | 8.9 | 9 (10-27 04:53Z) |
| us-east-2 use2-az2 | 168 | 99% | 8.9 | 9 (10-27 04:53Z) |
| us-east-2 use2-az3 | 172 | 95% | 8.7 | 9 (10-27 04:53Z) |
| us-west-2 usw2-az1 | 83 | 98% | 8.8 | 9 (10-26 00:11Z) |
| us-west-2 usw2-az2 | 77 | 96% | 8.7 | 9 (10-25 18:58Z) |
| us-west-2 usw2-az3 | 98 | 94% | 8.6 | 9 (10-26 00:11Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.703500 | 2026-10-27T04:53:23Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-27T04:53:23Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.780600 | 2026-10-27T04:53:23Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.961500 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.586700 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585300 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570300 | 2026-10-27T04:53:23Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740800 | 2026-10-27T04:53:23Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.556400 | 2026-10-27T04:53:23Z |
| ap-south-1 | ap-south-1a | Windows | 0.443000 | 2026-10-27T04:53:23Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.664000 | 2026-10-27T04:53:23Z |
| ap-south-1 | ap-south-1b | Windows | 0.410000 | 2026-10-27T04:53:23Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.661700 | 2026-10-27T04:53:23Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507400 | 2026-10-27T04:53:23Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.661000 | 2026-10-27T04:53:23Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.556900 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.599600 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.456300 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.486700 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.514100 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.524900 | 2026-10-27T04:53:23Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.559700 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2a | Windows | 0.639500 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.547600 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2b | Windows | 0.637800 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.546200 | 2026-10-27T04:53:23Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.564700 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2a | Windows | 0.320000 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.577500 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2b | Windows | 0.327200 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.552300 | 2026-10-27T04:53:23Z |
| us-west-2 | us-west-2c | Windows | 0.319500 | 2026-10-27T04:53:23Z |
