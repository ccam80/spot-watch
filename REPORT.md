# Spot placement score log

Generated 2026-10-13 01:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 304 | 34% | 4.2 | 9 (10-13 01:16Z) |
| ap-northeast-1 | 304 | 15% | 2.8 | 2 (10-13 01:16Z) |
| ap-northeast-2 | 304 | 49% | 5.9 | 9 (10-13 01:16Z) |
| ap-south-1 | 304 | 2% | 1.8 | 2 (10-13 01:16Z) |
| ap-southeast-2 | 304 | 0% | 1.0 | 1 (10-13 01:16Z) |
| ap-southeast-3 | 304 | 22% | 3.3 | 1 (10-13 01:16Z) |
| us-east-1 | 304 | 10% | 2.6 | 2 (10-13 01:16Z) |
| us-east-2 | 304 | 27% | 3.6 | 1 (10-13 01:16Z) |
| us-west-2 | 304 | 12% | 2.4 | 1 (10-13 01:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        991191199998121111111111111111111111822929999999
ap-northeast-1   821999999999999119111151197111111911122221192212
ap-northeast-2   999999999999999914999999999999999991999999999999
ap-south-1       121111111111122222222222222111221111112222222222
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   911411111111111111111111388111113891199979395151
us-east-1        292223311991999992111121111222113232333192233222
us-east-2        999911999999999991118111111111111111181199999911
us-west-2        212129999999919911211212111111111111999911111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 7 | 5 | 4 | 4 | 3 | 6 | 4 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 6 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 5 | 6 | 4 | 6 | 4 | 2 | 3 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 105 | 8% | 1.8 | 5 (10-13 01:16Z) |
| ap-east-1 ape1-az2 | 209 | 48% | 5.5 | 9 (10-13 01:16Z) |
| ap-northeast-1 apne1-az1 | 51 | 8% | 1.8 | 1 (10-12 09:04Z) |
| ap-northeast-1 apne1-az4 | 145 | 26% | 3.6 | 1 (10-12 01:14Z) |
| ap-northeast-2 apne2-az1 | 264 | 46% | 5.6 | 9 (10-13 01:16Z) |
| ap-northeast-2 apne2-az3 | 276 | 50% | 5.9 | 9 (10-13 01:16Z) |
| ap-northeast-2 apne2-az4 | 301 | 49% | 5.9 | 9 (10-13 01:16Z) |
| ap-south-1 aps1-az1 | 79 | 1% | 1.6 | 1 (10-13 01:16Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 48 | 0% | 1.1 | 1 (10-13 01:16Z) |
| ap-southeast-2 apse2-az2 | 32 | 0% | 1.0 | 1 (10-13 01:16Z) |
| ap-southeast-3 apse3-az1 | 58 | 0% | 1.0 | 1 (10-12 18:57Z) |
| ap-southeast-3 apse3-az3 | 207 | 31% | 4.2 | 5 (10-12 18:57Z) |
| us-east-1 use1-az1 | 58 | 0% | 1.1 | 1 (10-13 01:16Z) |
| us-east-1 use1-az2 | 80 | 4% | 1.6 | 1 (10-10 01:42Z) |
| us-east-1 use1-az4 | 95 | 27% | 3.4 | 1 (10-12 09:04Z) |
| us-east-1 use1-az5 | 95 | 25% | 3.3 | 9 (10-11 05:37Z) |
| us-east-1 use1-az6 | 74 | 20% | 2.9 | 1 (10-12 18:57Z) |
| us-east-2 use2-az1 | 123 | 38% | 4.4 | 1 (10-12 18:57Z) |
| us-east-2 use2-az2 | 155 | 45% | 4.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az3 | 184 | 42% | 4.9 | 9 (10-12 09:04Z) |
| us-west-2 usw2-az1 | 103 | 30% | 3.9 | 9 (10-10 23:28Z) |
| us-west-2 usw2-az2 | 65 | 26% | 3.5 | 1 (10-13 01:16Z) |
| us-west-2 usw2-az3 | 125 | 22% | 3.3 | 9 (10-10 23:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 304 | 50% | 6.0 | 9 (10-13 01:16Z) |
| ap-northeast-1 | 304 | 74% | 7.2 | 2 (10-13 01:16Z) |
| ap-northeast-2 | 304 | 100% | 9.0 | 9 (10-13 01:16Z) |
| ap-south-1 | 304 | 61% | 6.4 | 9 (10-13 01:16Z) |
| ap-southeast-2 | 304 | 17% | 3.2 | 1 (10-13 01:16Z) |
| ap-southeast-3 | 304 | 22% | 3.3 | 1 (10-13 01:16Z) |
| us-east-1 | 304 | 71% | 6.6 | 5 (10-13 01:16Z) |
| us-east-2 | 304 | 72% | 7.0 | 1 (10-13 01:16Z) |
| us-west-2 | 304 | 53% | 5.8 | 9 (10-13 01:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   922999999999999919923991399119911999999999999992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999922992999299919991499999999999299
ap-southeast-2   222222222292999229111111191111111189199999911111
ap-southeast-3   911411111111111111111111388111113891199979395151
us-east-1        498557634999999995545334333663546456998299999945
us-east-2        999939999999999992399332121211121211992299999911
us-west-2        449959999999999994323544132333133233999999359299
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 8 | 9 | 8 | 5 | 6 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 179 | 70% | 7.2 | 9 (10-13 01:16Z) |
| ap-east-1 ape1-az2 | 150 | 73% | 7.4 | 9 (10-13 01:16Z) |
| ap-east-1 ape1-az3 | 149 | 70% | 7.2 | 9 (10-13 01:16Z) |
| ap-northeast-1 apne1-az1 | 143 | 92% | 8.5 | 9 (10-12 09:04Z) |
| ap-northeast-1 apne1-az2 | 81 | 68% | 7.1 | 9 (10-12 18:57Z) |
| ap-northeast-1 apne1-az4 | 172 | 99% | 8.9 | 9 (10-12 18:57Z) |
| ap-northeast-2 apne2-az1 | 239 | 100% | 9.0 | 9 (10-13 01:16Z) |
| ap-northeast-2 apne2-az2 | 66 | 79% | 7.7 | 9 (10-11 05:37Z) |
| ap-northeast-2 apne2-az3 | 259 | 100% | 9.0 | 9 (10-13 01:16Z) |
| ap-northeast-2 apne2-az4 | 173 | 73% | 7.4 | 9 (10-13 01:16Z) |
| ap-south-1 aps1-az1 | 107 | 79% | 7.8 | 9 (10-13 01:16Z) |
| ap-south-1 aps1-az2 | 107 | 66% | 7.0 | 9 (10-12 18:57Z) |
| ap-south-1 aps1-az3 | 124 | 85% | 8.1 | 9 (10-13 01:16Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 38 | 66% | 6.9 | 9 (10-11 12:40Z) |
| ap-southeast-3 apse3-az3 | 61 | 30% | 4.7 | 9 (10-11 21:50Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 80 | 100% | 9.0 | 9 (10-11 05:37Z) |
| us-east-1 use1-az4 | 101 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-1 use1-az5 | 62 | 97% | 8.8 | 9 (10-11 21:50Z) |
| us-east-1 use1-az6 | 83 | 95% | 8.7 | 9 (10-12 01:14Z) |
| us-east-2 use2-az1 | 105 | 98% | 8.9 | 9 (10-12 01:14Z) |
| us-east-2 use2-az2 | 149 | 99% | 8.9 | 9 (10-11 05:37Z) |
| us-east-2 use2-az3 | 137 | 94% | 8.6 | 9 (10-12 09:04Z) |
| us-west-2 usw2-az1 | 75 | 97% | 8.8 | 9 (10-13 01:16Z) |
| us-west-2 usw2-az2 | 69 | 96% | 8.7 | 9 (10-11 05:37Z) |
| us-west-2 usw2-az3 | 88 | 95% | 8.7 | 9 (10-13 01:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718100 | 2026-10-13T01:16:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-13T01:16:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.770400 | 2026-10-13T01:16:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.952100 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594000 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.588200 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.578900 | 2026-10-13T01:16:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742200 | 2026-10-13T01:16:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.547000 | 2026-10-13T01:16:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.357300 | 2026-10-13T01:16:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.680100 | 2026-10-13T01:16:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.342900 | 2026-10-13T01:16:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.725200 | 2026-10-13T01:16:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.520000 | 2026-10-13T01:16:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.463400 | 2026-10-13T01:16:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.601300 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.500100 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.488500 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.469200 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.405600 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.462700 | 2026-10-13T01:16:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.537400 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.531600 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2b | Windows | 0.640500 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.524500 | 2026-10-13T01:16:45Z |
| us-east-2 | us-east-2c | Windows | 0.637300 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.544400 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2a | Windows | 0.318700 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.507700 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2b | Windows | 0.329100 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.508900 | 2026-10-13T01:16:45Z |
| us-west-2 | us-west-2c | Windows | 0.318600 | 2026-10-13T01:16:45Z |
