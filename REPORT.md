# Spot placement score log

Generated 2026-09-28 21:21 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 202 | 19% | 3.3 | 9 (09-28 21:20Z) |
| ap-northeast-1 | 202 | 7% | 2.3 | 9 (09-28 21:20Z) |
| ap-northeast-2 | 202 | 24% | 4.4 | 9 (09-28 21:20Z) |
| ap-south-1 | 202 | 3% | 2.0 | 1 (09-28 21:20Z) |
| ap-southeast-2 | 202 | 0% | 1.0 | 1 (09-28 21:20Z) |
| ap-southeast-3 | 202 | 18% | 3.4 | 8 (09-28 21:20Z) |
| us-east-1 | 202 | 6% | 2.4 | 1 (09-28 21:20Z) |
| us-east-2 | 202 | 16% | 2.9 | 1 (09-28 21:20Z) |
| us-west-2 | 202 | 11% | 2.4 | 1 (09-28 21:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999991191999199999988991139911149999999999999
ap-northeast-1   222222113432215553166444421111111111118989945589
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111211113114111159992791344111111111211111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   968999519891589999286999891111111153687867556688
us-east-1        212321131223322392332222999911999991999111111121
us-east-2        929112199289999999999999999999999999999111111111
us-west-2        211222211121995192991299999999999999991111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 2 | 2 | 5 | 4 | 3 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 4 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 65 | 0% | 1.5 | 1 (09-28 21:20Z) |
| ap-east-1 ape1-az2 | 134 | 28% | 4.3 | 9 (09-28 21:20Z) |
| ap-northeast-1 apne1-az1 | 26 | 0% | 1.3 | 1 (09-28 15:24Z) |
| ap-northeast-1 apne1-az4 | 90 | 8% | 2.6 | 8 (09-28 21:20Z) |
| ap-northeast-2 apne2-az1 | 180 | 24% | 4.4 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az3 | 184 | 27% | 4.5 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az4 | 199 | 25% | 4.5 | 9 (09-28 21:20Z) |
| ap-south-1 aps1-az1 | 61 | 2% | 1.8 | 1 (09-28 16:27Z) |
| ap-south-1 aps1-az3 | 88 | 3% | 2.7 | 1 (09-28 17:21Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 41 | 0% | 1.0 | 1 (09-28 20:22Z) |
| ap-southeast-3 apse3-az3 | 153 | 22% | 4.0 | 8 (09-28 21:20Z) |
| us-east-1 use1-az1 | 21 | 0% | 1.3 | 1 (09-28 15:24Z) |
| us-east-1 use1-az2 | 60 | 3% | 1.6 | 1 (09-28 21:20Z) |
| us-east-1 use1-az4 | 54 | 24% | 3.4 | 1 (09-28 16:27Z) |
| us-east-1 use1-az5 | 62 | 18% | 2.8 | 1 (09-28 20:22Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 70 | 23% | 3.3 | 1 (09-28 16:27Z) |
| us-east-2 use2-az2 | 102 | 27% | 3.8 | 1 (09-28 21:20Z) |
| us-east-2 use2-az3 | 120 | 26% | 3.9 | 1 (09-28 19:19Z) |
| us-west-2 usw2-az1 | 71 | 28% | 3.9 | 1 (09-28 21:20Z) |
| us-west-2 usw2-az2 | 42 | 26% | 3.7 | 1 (09-28 17:21Z) |
| us-west-2 usw2-az3 | 98 | 18% | 3.1 | 9 (09-28 11:22Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 202 | 24% | 4.5 | 9 (09-28 21:20Z) |
| ap-northeast-1 | 202 | 78% | 7.4 | 9 (09-28 21:20Z) |
| ap-northeast-2 | 202 | 100% | 9.0 | 9 (09-28 21:20Z) |
| ap-south-1 | 202 | 55% | 6.1 | 9 (09-28 21:20Z) |
| ap-southeast-2 | 202 | 17% | 3.3 | 2 (09-28 21:20Z) |
| ap-southeast-3 | 202 | 18% | 3.4 | 8 (09-28 21:20Z) |
| us-east-1 | 202 | 76% | 7.0 | 4 (09-28 21:20Z) |
| us-east-2 | 202 | 76% | 7.3 | 2 (09-28 21:20Z) |
| us-west-2 | 202 | 59% | 6.2 | 3 (09-28 21:20Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   934999219999999999999999991111111113899999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       992899989999999999999999999999999321122999999999
ap-southeast-2   122992229999999999999999222222222222427949999322
ap-southeast-3   968999519891589999286999891111111153687867556688
us-east-1        699545983479999999999999999999999999999221234454
us-east-2        999234899999999999999999999999999999999922333322
us-west-2        595544599343999999999999999999999999999999443433
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 7 | 5 | 6 | 6 | 8 | 7 | 8 | 7 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 94 | 43% | 5.6 | 9 (09-28 21:20Z) |
| ap-east-1 ape1-az2 | 71 | 42% | 5.5 | 9 (09-28 20:22Z) |
| ap-east-1 ape1-az3 | 68 | 35% | 5.1 | 9 (09-28 21:20Z) |
| ap-northeast-1 apne1-az1 | 99 | 92% | 8.5 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az2 | 37 | 30% | 4.8 | 9 (09-28 21:20Z) |
| ap-northeast-1 apne1-az4 | 124 | 100% | 9.0 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az1 | 157 | 100% | 9.0 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az2 | 40 | 68% | 7.0 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az3 | 179 | 100% | 9.0 | 9 (09-28 21:20Z) |
| ap-northeast-2 apne2-az4 | 87 | 46% | 5.8 | 9 (09-28 21:20Z) |
| ap-south-1 aps1-az1 | 58 | 62% | 6.7 | 9 (09-28 18:29Z) |
| ap-south-1 aps1-az2 | 65 | 45% | 5.7 | 9 (09-28 21:20Z) |
| ap-south-1 aps1-az3 | 82 | 78% | 7.7 | 9 (09-28 21:20Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 26 | 54% | 6.2 | 9 (09-28 17:21Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 84 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-east-1 use1-az5 | 46 | 98% | 8.8 | 9 (09-28 08:38Z) |
| us-east-1 use1-az6 | 73 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 74 | 99% | 8.9 | 9 (09-28 11:22Z) |
| us-east-2 use2-az2 | 108 | 98% | 8.9 | 9 (09-28 13:26Z) |
| us-east-2 use2-az3 | 99 | 92% | 8.5 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az1 | 62 | 98% | 8.9 | 9 (09-28 13:26Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 71 | 99% | 8.9 | 9 (09-28 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730400 | 2026-09-28T21:20:56Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.888900 | 2026-09-28T21:20:56Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.812400 | 2026-09-28T21:20:56Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.002900 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567700 | 2026-09-28T21:20:56Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T21:20:56Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.573700 | 2026-09-28T21:20:56Z |
| ap-south-1 | ap-south-1a | Windows | 0.345300 | 2026-09-28T21:20:56Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.598700 | 2026-09-28T21:20:56Z |
| ap-south-1 | ap-south-1b | Windows | 0.338100 | 2026-09-28T21:20:56Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.709900 | 2026-09-28T21:20:56Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497900 | 2026-09-28T21:20:56Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.655400 | 2026-09-28T21:20:56Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.627500 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1a | Windows | 0.309600 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.473400 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.435800 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.381100 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.430400 | 2026-09-28T21:20:56Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527800 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-09-28T21:20:56Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.512800 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.491700 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.488200 | 2026-09-28T21:20:56Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-28T21:20:56Z |
