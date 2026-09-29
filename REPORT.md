# Spot placement score log

Generated 2026-09-29 13:28 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 218 | 25% | 3.7 | 9 (09-29 13:28Z) |
| ap-northeast-1 | 218 | 7% | 2.3 | 8 (09-29 13:28Z) |
| ap-northeast-2 | 218 | 30% | 4.8 | 9 (09-29 13:28Z) |
| ap-south-1 | 218 | 3% | 2.0 | 1 (09-29 13:28Z) |
| ap-southeast-2 | 218 | 0% | 1.0 | 1 (09-29 13:28Z) |
| ap-southeast-3 | 218 | 19% | 3.4 | 8 (09-29 13:28Z) |
| us-east-1 | 218 | 6% | 2.3 | 1 (09-29 13:28Z) |
| us-east-2 | 218 | 18% | 3.0 | 1 (09-29 13:28Z) |
| us-west-2 | 218 | 10% | 2.3 | 1 (09-29 13:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999889911399111499999999999999999999999999999
ap-northeast-1   531664444211111111111189899455894122122211121148
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111599927913441111111112111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   992869998911111111536878675566888911111111154378
us-east-1        923322229999119999919991111111211111291111122111
us-east-2        999999999999999999999991111111111111111199999991
us-west-2        929912999999999999999911111111111111221111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 6 | 6 | 3 | 3 | 3 | 6 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 5 | 4 | 2 | 3 | 4 | 7 | 6 | 4 | 5 | 4 | 6 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 6 | 4 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 71 | 0% | 1.4 | 1 (09-29 07:30Z) |
| ap-east-1 ape1-az2 | 150 | 36% | 4.8 | 9 (09-29 13:28Z) |
| ap-northeast-1 apne1-az1 | 31 | 0% | 1.3 | 2 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 96 | 8% | 2.6 | 6 (09-29 13:28Z) |
| ap-northeast-2 apne2-az1 | 196 | 30% | 4.7 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az3 | 200 | 32% | 4.9 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az4 | 215 | 30% | 4.8 | 9 (09-29 13:28Z) |
| ap-south-1 aps1-az1 | 66 | 2% | 1.7 | 1 (09-29 13:28Z) |
| ap-south-1 aps1-az3 | 89 | 3% | 2.7 | 1 (09-29 01:00Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 20 | 0% | 1.0 | 1 (09-29 01:00Z) |
| ap-southeast-3 apse3-az1 | 42 | 0% | 1.0 | 1 (09-29 05:24Z) |
| ap-southeast-3 apse3-az3 | 162 | 24% | 4.0 | 8 (09-29 13:28Z) |
| us-east-1 use1-az1 | 29 | 0% | 1.2 | 1 (09-29 09:27Z) |
| us-east-1 use1-az2 | 63 | 3% | 1.5 | 1 (09-29 12:36Z) |
| us-east-1 use1-az4 | 64 | 20% | 3.0 | 1 (09-29 13:28Z) |
| us-east-1 use1-az5 | 65 | 17% | 2.8 | 1 (09-29 07:30Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 83 | 28% | 3.6 | 1 (09-29 13:28Z) |
| us-east-2 use2-az2 | 110 | 32% | 4.1 | 9 (09-29 12:36Z) |
| us-east-2 use2-az3 | 128 | 30% | 4.2 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az1 | 72 | 28% | 3.9 | 1 (09-29 06:39Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 101 | 18% | 3.0 | 1 (09-29 08:32Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 218 | 30% | 4.8 | 9 (09-29 13:28Z) |
| ap-northeast-1 | 218 | 75% | 7.3 | 9 (09-29 13:28Z) |
| ap-northeast-2 | 218 | 100% | 9.0 | 9 (09-29 13:28Z) |
| ap-south-1 | 218 | 56% | 6.1 | 5 (09-29 13:28Z) |
| ap-southeast-2 | 218 | 17% | 3.3 | 9 (09-29 13:28Z) |
| ap-southeast-3 | 218 | 19% | 3.4 | 8 (09-29 13:28Z) |
| us-east-1 | 218 | 76% | 7.0 | 4 (09-29 13:28Z) |
| us-east-2 | 218 | 75% | 7.3 | 3 (09-29 13:28Z) |
| us-west-2 | 218 | 56% | 6.0 | 4 (09-29 13:28Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999911111111138999999999999933352223338999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999993211229999999999999999942171115
ap-southeast-2   999999992222222222224279499993221222222222222229
ap-southeast-3   992869998911111111536878675566888911111111154378
us-east-1        999999999999999999999992212344543369895794899594
us-east-2        999999999999999999999999223333223322399999999993
us-west-2        999999999999999999999999994434332244442299224494
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 6 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 7 | 6 | 8 | 7 | 5 | 4 | 3 | 5 | 4 | 2 | 6 | 5 | 6 | 6 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 5 | 2 | 3 | 3 | 4 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 8 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 7 | 5 | 7 | 8 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 5 | 6 | 5 | 6 | 6 | 9 | 7 | 7 | 5 | 8 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 108 | 50% | 6.0 | 9 (09-29 13:28Z) |
| ap-east-1 ape1-az2 | 84 | 51% | 6.1 | 9 (09-29 12:36Z) |
| ap-east-1 ape1-az3 | 82 | 46% | 5.8 | 9 (09-29 13:28Z) |
| ap-northeast-1 apne1-az1 | 102 | 92% | 8.5 | 9 (09-29 13:28Z) |
| ap-northeast-1 apne1-az2 | 40 | 35% | 5.1 | 9 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 130 | 99% | 8.9 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az1 | 171 | 100% | 9.0 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az2 | 48 | 71% | 7.2 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az3 | 194 | 100% | 9.0 | 9 (09-29 13:28Z) |
| ap-northeast-2 apne2-az4 | 103 | 54% | 6.3 | 9 (09-29 13:28Z) |
| ap-south-1 aps1-az1 | 62 | 65% | 6.9 | 9 (09-29 03:28Z) |
| ap-south-1 aps1-az2 | 73 | 51% | 6.0 | 9 (09-29 05:24Z) |
| ap-south-1 aps1-az3 | 88 | 80% | 7.8 | 9 (09-29 04:27Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 27 | 56% | 6.3 | 9 (09-29 13:28Z) |
| ap-southeast-3 apse3-az3 | 50 | 20% | 4.1 | 5 (09-29 09:27Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 86 | 98% | 8.8 | 9 (09-29 10:24Z) |
| us-east-1 use1-az5 | 47 | 98% | 8.9 | 9 (09-29 03:28Z) |
| us-east-1 use1-az6 | 76 | 96% | 8.7 | 2 (09-29 08:32Z) |
| us-east-2 use2-az1 | 83 | 99% | 8.9 | 9 (09-29 11:21Z) |
| us-east-2 use2-az2 | 116 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-east-2 use2-az3 | 108 | 93% | 8.5 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 72 | 99% | 8.9 | 9 (09-29 12:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.729600 | 2026-09-29T13:28:26Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.879800 | 2026-09-29T13:28:26Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.800200 | 2026-09-29T13:28:26Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.989000 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594100 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567400 | 2026-09-29T13:28:26Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-29T13:28:26Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.586200 | 2026-09-29T13:28:26Z |
| ap-south-1 | ap-south-1a | Windows | 0.351300 | 2026-09-29T13:28:26Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.614200 | 2026-09-29T13:28:26Z |
| ap-south-1 | ap-south-1b | Windows | 0.340100 | 2026-09-29T13:28:26Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.710000 | 2026-09-29T13:28:26Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-09-29T13:28:26Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.640400 | 2026-09-29T13:28:26Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.616100 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1a | Windows | 0.307100 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.463600 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.445800 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.389400 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.437800 | 2026-09-29T13:28:26Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530300 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2b | Windows | 0.640700 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515300 | 2026-09-29T13:28:26Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.511100 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2a | Windows | 0.332300 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498300 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2b | Windows | 0.332400 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.483300 | 2026-09-29T13:28:26Z |
| us-west-2 | us-west-2c | Windows | 0.331200 | 2026-09-29T13:28:26Z |
