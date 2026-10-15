# Spot placement score log

Generated 2026-10-15 01:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 313 | 35% | 4.3 | 9 (10-15 01:24Z) |
| ap-northeast-1 | 313 | 15% | 2.7 | 1 (10-15 01:24Z) |
| ap-northeast-2 | 313 | 50% | 6.0 | 9 (10-15 01:24Z) |
| ap-south-1 | 313 | 2% | 1.8 | 2 (10-15 01:24Z) |
| ap-southeast-2 | 313 | 0% | 1.0 | 1 (10-15 01:24Z) |
| ap-southeast-3 | 313 | 21% | 3.2 | 1 (10-15 01:24Z) |
| us-east-1 | 313 | 9% | 2.5 | 2 (10-15 01:24Z) |
| us-east-2 | 313 | 27% | 3.5 | 2 (10-15 01:24Z) |
| us-west-2 | 313 | 12% | 2.4 | 1 (10-15 01:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        998121111111111111111111111822929999999999999999
ap-northeast-1   999999119111151197111111911122221192212121114221
ap-northeast-2   999999914999999999999999991999999999999999999999
ap-south-1       111122222222222222111221111112222222222111112222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111111111111111388111113891199979395151122111131
us-east-1        991999992111121111222113232333192233222113333232
us-east-2        999999991118111111111111111181199999911112991112
us-west-2        999919911211212111111111111999911111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 5 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 4 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 108 | 8% | 1.8 | 1 (10-14 18:31Z) |
| ap-east-1 ape1-az2 | 218 | 50% | 5.7 | 9 (10-15 01:24Z) |
| ap-northeast-1 apne1-az1 | 53 | 8% | 1.8 | 3 (10-14 13:38Z) |
| ap-northeast-1 apne1-az4 | 148 | 26% | 3.6 | 1 (10-15 01:24Z) |
| ap-northeast-2 apne2-az1 | 273 | 48% | 5.7 | 9 (10-15 01:24Z) |
| ap-northeast-2 apne2-az3 | 285 | 51% | 6.0 | 9 (10-15 01:24Z) |
| ap-northeast-2 apne2-az4 | 310 | 51% | 6.0 | 9 (10-15 01:24Z) |
| ap-south-1 aps1-az1 | 83 | 1% | 1.6 | 1 (10-14 18:31Z) |
| ap-south-1 aps1-az3 | 109 | 3% | 2.4 | 1 (10-14 22:14Z) |
| ap-southeast-2 apse2-az1 | 50 | 0% | 1.1 | 1 (10-15 01:24Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 60 | 0% | 1.0 | 1 (10-15 01:24Z) |
| ap-southeast-3 apse3-az3 | 210 | 30% | 4.2 | 3 (10-14 22:14Z) |
| us-east-1 use1-az1 | 62 | 0% | 1.1 | 1 (10-14 13:38Z) |
| us-east-1 use1-az2 | 83 | 4% | 1.5 | 1 (10-14 22:14Z) |
| us-east-1 use1-az4 | 98 | 27% | 3.4 | 1 (10-14 07:30Z) |
| us-east-1 use1-az5 | 98 | 24% | 3.2 | 1 (10-15 01:24Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 126 | 39% | 4.4 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 158 | 44% | 4.9 | 1 (10-14 22:14Z) |
| us-east-2 use2-az3 | 189 | 42% | 4.9 | 1 (10-15 01:24Z) |
| us-west-2 usw2-az1 | 108 | 29% | 3.7 | 1 (10-15 01:24Z) |
| us-west-2 usw2-az2 | 67 | 25% | 3.4 | 1 (10-14 13:38Z) |
| us-west-2 usw2-az3 | 127 | 22% | 3.3 | 1 (10-14 07:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 313 | 51% | 6.1 | 9 (10-15 01:24Z) |
| ap-northeast-1 | 313 | 73% | 7.1 | 2 (10-15 01:24Z) |
| ap-northeast-2 | 313 | 100% | 9.0 | 9 (10-15 01:24Z) |
| ap-south-1 | 313 | 61% | 6.4 | 9 (10-15 01:24Z) |
| ap-southeast-2 | 313 | 17% | 3.2 | 1 (10-15 01:24Z) |
| ap-southeast-3 | 313 | 21% | 3.2 | 1 (10-15 01:24Z) |
| us-east-1 | 313 | 71% | 6.5 | 5 (10-15 01:24Z) |
| us-east-2 | 313 | 71% | 7.0 | 2 (10-15 01:24Z) |
| us-west-2 | 313 | 52% | 5.7 | 3 (10-15 01:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999919923991399119911999999999999992399239992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999922992999299919991499999999999299199912299
ap-southeast-2   292999229111111191111111189199999911111111111811
ap-southeast-3   111111111111111388111113891199979395151122111131
us-east-1        999999995545334333663546456998299999945426664355
us-east-2        999999992399332121211121211992299999911912991122
us-west-2        999999994323544132333133233999999359299442495343
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 7 | 7 | 5 | 7 | 6 | 7 | 6 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 4 | 4 | 2 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 6 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 188 | 71% | 7.3 | 9 (10-15 01:24Z) |
| ap-east-1 ape1-az2 | 157 | 74% | 7.4 | 9 (10-15 01:24Z) |
| ap-east-1 ape1-az3 | 158 | 72% | 7.3 | 9 (10-15 01:24Z) |
| ap-northeast-1 apne1-az1 | 148 | 93% | 8.5 | 9 (10-14 22:14Z) |
| ap-northeast-1 apne1-az2 | 87 | 69% | 7.1 | 1 (10-15 01:24Z) |
| ap-northeast-1 apne1-az4 | 178 | 98% | 8.9 | 9 (10-14 22:14Z) |
| ap-northeast-2 apne2-az1 | 247 | 100% | 9.0 | 9 (10-15 01:24Z) |
| ap-northeast-2 apne2-az2 | 68 | 78% | 7.6 | 9 (10-14 18:31Z) |
| ap-northeast-2 apne2-az3 | 268 | 100% | 9.0 | 9 (10-15 01:24Z) |
| ap-northeast-2 apne2-az4 | 182 | 74% | 7.5 | 9 (10-15 01:24Z) |
| ap-south-1 aps1-az1 | 109 | 80% | 7.8 | 9 (10-14 01:49Z) |
| ap-south-1 aps1-az2 | 111 | 68% | 7.0 | 9 (10-15 01:24Z) |
| ap-south-1 aps1-az3 | 128 | 85% | 8.1 | 3 (10-15 01:24Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 21 | 57% | 5.9 | 2 (10-15 01:24Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 106 | 98% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az2 | 151 | 99% | 8.9 | 9 (10-14 07:30Z) |
| us-east-2 use2-az3 | 140 | 94% | 8.6 | 9 (10-14 07:30Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 89 | 94% | 8.6 | 2 (10-13 09:19Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.716100 | 2026-10-15T01:24:30Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-15T01:24:30Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.760800 | 2026-10-15T01:24:30Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.943800 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590800 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585600 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-10-15T01:24:30Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741700 | 2026-10-15T01:24:30Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.552200 | 2026-10-15T01:24:30Z |
| ap-south-1 | ap-south-1a | Windows | 0.381500 | 2026-10-15T01:24:30Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.703400 | 2026-10-15T01:24:30Z |
| ap-south-1 | ap-south-1b | Windows | 0.332400 | 2026-10-15T01:24:30Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.724900 | 2026-10-15T01:24:30Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.524900 | 2026-10-15T01:24:30Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.512900 | 2026-10-15T01:24:30Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.611000 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.474100 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.504500 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.463800 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.420000 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.465000 | 2026-10-15T01:24:30Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.542100 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2a | Windows | 0.644200 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.533000 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2b | Windows | 0.640600 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.525900 | 2026-10-15T01:24:30Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.533700 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2a | Windows | 0.316500 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496600 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2b | Windows | 0.332000 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.498000 | 2026-10-15T01:24:30Z |
| us-west-2 | us-west-2c | Windows | 0.316000 | 2026-10-15T01:24:30Z |
