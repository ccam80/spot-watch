# Spot placement score log

Generated 2026-10-19 21:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 340 | 41% | 4.7 | 9 (10-19 20:59Z) |
| ap-northeast-1 | 340 | 16% | 2.8 | 8 (10-19 20:59Z) |
| ap-northeast-2 | 340 | 54% | 6.2 | 9 (10-19 20:59Z) |
| ap-south-1 | 340 | 2% | 1.8 | 2 (10-19 20:59Z) |
| ap-southeast-2 | 340 | 1% | 1.1 | 1 (10-19 20:59Z) |
| ap-southeast-3 | 340 | 24% | 3.4 | 8 (10-19 20:59Z) |
| us-east-1 | 340 | 11% | 2.7 | 1 (10-19 20:59Z) |
| us-east-2 | 340 | 30% | 3.7 | 1 (10-19 20:59Z) |
| us-west-2 | 340 | 11% | 2.3 | 1 (10-19 20:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        822929999999999999999999999999999999999999999999
ap-northeast-1   122221192212121114221142111132212932416591222198
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       112222222222111112222222111222222222222222222222
ap-southeast-2   111111111111111111111111111111119119111111111111
ap-southeast-3   199979395151122111131151821438751867992474881178
us-east-1        333192233222113333232132312222233322192399999911
us-east-2        181199999911112991112911199911116199999919999911
us-west-2        999911111111111111111122111122211212121911921121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 3 | 7 | 5 | 4 | 6 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 5 | 5 | 8 | 5 | 5 | 7 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 118 | 8% | 1.7 | 1 (10-19 20:59Z) |
| ap-east-1 ape1-az2 | 245 | 56% | 6.0 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 159 | 26% | 3.6 | 7 (10-19 20:59Z) |
| ap-northeast-2 apne2-az1 | 295 | 50% | 5.9 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az3 | 312 | 54% | 6.2 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az4 | 337 | 55% | 6.3 | 9 (10-19 20:59Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 112 | 3% | 2.3 | 1 (10-17 13:39Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 71 | 0% | 1.0 | 1 (10-19 20:59Z) |
| ap-southeast-3 apse3-az3 | 230 | 34% | 4.3 | 8 (10-19 20:59Z) |
| us-east-1 use1-az1 | 65 | 0% | 1.1 | 1 (10-19 07:40Z) |
| us-east-1 use1-az2 | 95 | 3% | 1.5 | 1 (10-19 20:59Z) |
| us-east-1 use1-az4 | 104 | 31% | 3.7 | 9 (10-19 01:08Z) |
| us-east-1 use1-az5 | 110 | 28% | 3.5 | 8 (10-19 07:40Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 136 | 43% | 4.7 | 9 (10-19 07:40Z) |
| us-east-2 use2-az2 | 177 | 47% | 5.1 | 9 (10-19 07:40Z) |
| us-east-2 use2-az3 | 208 | 45% | 5.1 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az1 | 122 | 27% | 3.5 | 1 (10-19 20:59Z) |
| us-west-2 usw2-az2 | 72 | 25% | 3.3 | 1 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 340 | 55% | 6.3 | 9 (10-19 20:59Z) |
| ap-northeast-1 | 340 | 74% | 7.2 | 9 (10-19 20:59Z) |
| ap-northeast-2 | 340 | 100% | 9.0 | 9 (10-19 20:59Z) |
| ap-south-1 | 340 | 62% | 6.5 | 9 (10-19 20:59Z) |
| ap-southeast-2 | 340 | 20% | 3.3 | 1 (10-19 20:59Z) |
| ap-southeast-3 | 340 | 24% | 3.4 | 8 (10-19 20:59Z) |
| us-east-1 | 340 | 71% | 6.6 | 6 (10-19 20:59Z) |
| us-east-2 | 340 | 71% | 6.9 | 3 (10-19 20:59Z) |
| us-west-2 | 340 | 53% | 5.8 | 3 (10-19 20:59Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999992399239992199911999999999999999993299
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999299199912299229991299999999999999999299
ap-southeast-2   199999911111111111811111111111199999999999911191
ap-southeast-3   199979395151122111131151821438751867992474881178
us-east-1        998299999945426664355554679344659999999999999946
us-east-2        992299999911912991122911199931139999999999999923
us-west-2        999999359299442495343355433445443999999999999953
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 6 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 7 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 208 | 74% | 7.4 | 9 (10-19 20:59Z) |
| ap-east-1 ape1-az2 | 172 | 76% | 7.6 | 9 (10-19 15:31Z) |
| ap-east-1 ape1-az3 | 175 | 75% | 7.5 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az1 | 157 | 93% | 8.6 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az2 | 99 | 73% | 7.3 | 9 (10-19 20:59Z) |
| ap-northeast-1 apne1-az4 | 194 | 98% | 8.9 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az1 | 265 | 100% | 9.0 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 293 | 100% | 9.0 | 9 (10-19 20:59Z) |
| ap-northeast-2 apne2-az4 | 203 | 77% | 7.6 | 9 (10-19 20:59Z) |
| ap-south-1 aps1-az1 | 118 | 81% | 7.9 | 9 (10-18 18:01Z) |
| ap-south-1 aps1-az2 | 124 | 71% | 7.2 | 9 (10-19 20:59Z) |
| ap-south-1 aps1-az3 | 140 | 86% | 8.2 | 9 (10-19 20:59Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 64 | 31% | 4.8 | 9 (10-17 22:13Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 85 | 100% | 9.0 | 9 (10-18 23:02Z) |
| us-east-1 use1-az4 | 104 | 94% | 8.6 | 9 (10-18 14:30Z) |
| us-east-1 use1-az5 | 70 | 97% | 8.8 | 9 (10-19 01:08Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 115 | 98% | 8.9 | 9 (10-19 07:40Z) |
| us-east-2 use2-az2 | 158 | 99% | 8.9 | 9 (10-18 18:01Z) |
| us-east-2 use2-az3 | 152 | 95% | 8.6 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az1 | 79 | 97% | 8.8 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az2 | 74 | 96% | 8.7 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 91 | 95% | 8.6 | 9 (10-18 18:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.709000 | 2026-10-19T20:59:54Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-19T20:59:54Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.764300 | 2026-10-19T20:59:54Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.947100 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584600 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581200 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566400 | 2026-10-19T20:59:54Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-10-19T20:59:54Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.558500 | 2026-10-19T20:59:54Z |
| ap-south-1 | ap-south-1a | Windows | 0.388200 | 2026-10-19T20:59:54Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.740800 | 2026-10-19T20:59:54Z |
| ap-south-1 | ap-south-1b | Windows | 0.359300 | 2026-10-19T20:59:54Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.700700 | 2026-10-19T20:59:54Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.508900 | 2026-10-19T20:59:54Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.663100 | 2026-10-19T20:59:54Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.550500 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.444600 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.525400 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.517000 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.453500 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.507500 | 2026-10-19T20:59:54Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.552700 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2a | Windows | 0.643400 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545200 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2b | Windows | 0.639400 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.542200 | 2026-10-19T20:59:54Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.534500 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2a | Windows | 0.316000 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.526500 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2b | Windows | 0.328000 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.511700 | 2026-10-19T20:59:54Z |
| us-west-2 | us-west-2c | Windows | 0.315400 | 2026-10-19T20:59:54Z |
