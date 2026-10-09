# Spot placement score log

Generated 2026-10-09 08:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 289 | 32% | 4.1 | 1 (10-09 08:55Z) |
| ap-northeast-1 | 289 | 16% | 2.8 | 1 (10-09 08:55Z) |
| ap-northeast-2 | 289 | 46% | 5.8 | 9 (10-09 08:55Z) |
| ap-south-1 | 289 | 2% | 1.8 | 1 (10-09 08:55Z) |
| ap-southeast-2 | 289 | 0% | 1.0 | 1 (10-09 08:55Z) |
| ap-southeast-3 | 289 | 20% | 3.2 | 3 (10-09 08:55Z) |
| us-east-1 | 289 | 10% | 2.5 | 3 (10-09 08:55Z) |
| us-east-2 | 289 | 26% | 3.5 | 1 (10-09 08:55Z) |
| us-west-2 | 289 | 11% | 2.4 | 1 (10-09 08:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        899999111111993991191199998121111111111111111111
ap-northeast-1   189912799812129821999999999999119111151197111111
ap-northeast-2   999999999999999999999999999999914999999999999999
ap-south-1       111111111111111121111111111122222222222222111221
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   147651611111199911411111111111111111111388111113
us-east-1        222223222221192292223311991999992111121111222113
us-east-2        111181712189999999911999999999991118111111111111
us-west-2        222222221211122212129999999919911211212111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 5 | 7 | 3 | 4 | 4 | 6 | 4 | 4 | 6 | 4 | 6 | 5 | 4 | 4 | 3 | 6 | 3 | 4 | 5 | 3 | 4 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 1 | 6 | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 2 | 4 | 5 | 7 | 5 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 1 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 3 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 95 | 0% | 1.4 | 1 (10-08 08:51Z) |
| ap-east-1 ape1-az2 | 200 | 46% | 5.4 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az1 | 47 | 9% | 1.8 | 1 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 139 | 26% | 3.6 | 1 (10-08 08:51Z) |
| ap-northeast-2 apne2-az1 | 251 | 43% | 5.5 | 9 (10-09 08:55Z) |
| ap-northeast-2 apne2-az3 | 263 | 48% | 5.8 | 9 (10-09 08:55Z) |
| ap-northeast-2 apne2-az4 | 286 | 47% | 5.8 | 9 (10-09 08:55Z) |
| ap-south-1 aps1-az1 | 75 | 1% | 1.6 | 1 (10-09 08:55Z) |
| ap-south-1 aps1-az3 | 108 | 3% | 2.4 | 1 (10-08 16:24Z) |
| ap-southeast-2 apse2-az1 | 45 | 0% | 1.1 | 1 (10-09 08:55Z) |
| ap-southeast-2 apse2-az2 | 29 | 0% | 1.0 | 1 (10-09 08:55Z) |
| ap-southeast-3 apse3-az1 | 57 | 0% | 1.0 | 1 (10-09 02:03Z) |
| ap-southeast-3 apse3-az3 | 196 | 28% | 4.0 | 3 (10-09 08:55Z) |
| us-east-1 use1-az1 | 48 | 0% | 1.1 | 1 (10-09 08:55Z) |
| us-east-1 use1-az2 | 79 | 4% | 1.6 | 1 (10-09 02:03Z) |
| us-east-1 use1-az4 | 89 | 28% | 3.5 | 1 (10-08 22:00Z) |
| us-east-1 use1-az5 | 92 | 25% | 3.3 | 1 (10-08 16:24Z) |
| us-east-1 use1-az6 | 73 | 21% | 2.9 | 1 (10-09 02:03Z) |
| us-east-2 use2-az1 | 114 | 38% | 4.3 | 1 (10-09 02:03Z) |
| us-east-2 use2-az2 | 150 | 43% | 4.8 | 1 (10-08 08:51Z) |
| us-east-2 use2-az3 | 175 | 41% | 4.8 | 1 (10-09 08:55Z) |
| us-west-2 usw2-az1 | 99 | 28% | 3.7 | 1 (10-08 16:24Z) |
| us-west-2 usw2-az2 | 59 | 24% | 3.3 | 1 (10-09 08:55Z) |
| us-west-2 usw2-az3 | 121 | 21% | 3.2 | 1 (10-09 02:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 289 | 47% | 5.8 | 9 (10-09 08:55Z) |
| ap-northeast-1 | 289 | 73% | 7.1 | 1 (10-09 08:55Z) |
| ap-northeast-2 | 289 | 100% | 9.0 | 9 (10-09 08:55Z) |
| ap-south-1 | 289 | 60% | 6.3 | 1 (10-09 08:55Z) |
| ap-southeast-2 | 289 | 16% | 3.1 | 1 (10-09 08:55Z) |
| ap-southeast-3 | 289 | 20% | 3.2 | 3 (10-09 08:55Z) |
| us-east-1 | 289 | 71% | 6.6 | 6 (10-09 08:55Z) |
| us-east-2 | 289 | 73% | 7.1 | 1 (10-09 08:55Z) |
| us-west-2 | 289 | 52% | 5.7 | 3 (10-09 08:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999992249922999999999999919923991399119911
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111119929999929999999999999999922992999299919991
ap-southeast-2   222222222222222222222222292999229111111191111111
ap-southeast-3   147651611111199911411111111111111111111388111113
us-east-1        433344333445594498557634999999995545334333663546
us-east-2        329299835999999999939999999999992399332121211121
us-west-2        554444454443393449959999999999994323544132333133
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 6 | 7 | 8 | 5 | 7 | 5 | 7 | 6 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 | 6 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 4 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 7 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 6 | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 9 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 5 | 8 | 6 | 7 | 5 | 6 | 6 | 7 |
| us-west-2 | 6 | 5 | 4 | 4 | 5 | 6 | 8 | 7 | 5 | 5 | 7 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 172 | 69% | 7.1 | 9 (10-09 08:55Z) |
| ap-east-1 ape1-az2 | 142 | 71% | 7.3 | 9 (10-09 08:55Z) |
| ap-east-1 ape1-az3 | 138 | 68% | 7.1 | 9 (10-09 08:55Z) |
| ap-northeast-1 apne1-az1 | 136 | 92% | 8.5 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az2 | 71 | 63% | 6.8 | 9 (10-08 22:00Z) |
| ap-northeast-1 apne1-az4 | 164 | 99% | 8.9 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az1 | 225 | 100% | 9.0 | 9 (10-09 08:55Z) |
| ap-northeast-2 apne2-az2 | 65 | 78% | 7.6 | 9 (10-08 22:00Z) |
| ap-northeast-2 apne2-az3 | 249 | 100% | 9.0 | 9 (10-09 08:55Z) |
| ap-northeast-2 apne2-az4 | 163 | 71% | 7.3 | 9 (10-09 08:55Z) |
| ap-south-1 aps1-az1 | 98 | 78% | 7.7 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az2 | 104 | 65% | 6.9 | 9 (10-09 02:03Z) |
| ap-south-1 aps1-az3 | 115 | 84% | 8.1 | 9 (10-09 02:03Z) |
| ap-southeast-2 apse2-az1 | 24 | 58% | 6.4 | 9 (10-07 16:22Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 33 | 61% | 6.6 | 1 (10-07 08:33Z) |
| ap-southeast-3 apse3-az3 | 56 | 23% | 4.3 | 3 (10-09 08:55Z) |
| us-east-1 use1-az1 | 18 | 67% | 6.5 | 2 (10-09 02:03Z) |
| us-east-1 use1-az2 | 79 | 100% | 9.0 | 9 (10-04 21:19Z) |
| us-east-1 use1-az4 | 98 | 95% | 8.6 | 2 (10-09 08:55Z) |
| us-east-1 use1-az5 | 59 | 97% | 8.7 | 1 (10-08 08:51Z) |
| us-east-1 use1-az6 | 80 | 95% | 8.7 | 2 (10-09 08:55Z) |
| us-east-2 use2-az1 | 103 | 98% | 8.9 | 1 (10-09 08:55Z) |
| us-east-2 use2-az2 | 147 | 99% | 8.9 | 9 (10-06 10:07Z) |
| us-east-2 use2-az3 | 130 | 94% | 8.6 | 9 (10-06 10:07Z) |
| us-west-2 usw2-az1 | 72 | 97% | 8.8 | 1 (10-08 08:51Z) |
| us-west-2 usw2-az2 | 65 | 95% | 8.6 | 9 (10-04 21:19Z) |
| us-west-2 usw2-az3 | 83 | 95% | 8.7 | 9 (10-04 06:47Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706200 | 2026-10-09T08:55:45Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-09T08:55:45Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.761100 | 2026-10-09T08:55:45Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.944100 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.600500 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580100 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.574600 | 2026-10-09T08:55:45Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.742900 | 2026-10-09T08:55:45Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.614700 | 2026-10-09T08:55:45Z |
| ap-south-1 | ap-south-1a | Windows | 0.376800 | 2026-10-09T08:55:45Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.687800 | 2026-10-09T08:55:45Z |
| ap-south-1 | ap-south-1b | Windows | 0.353500 | 2026-10-09T08:55:45Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.718200 | 2026-10-09T08:55:45Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502500 | 2026-10-09T08:55:45Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.438300 | 2026-10-09T08:55:45Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.574100 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.566900 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.488300 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.478600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.411500 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.488600 | 2026-10-09T08:55:45Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534200 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2a | Windows | 0.640000 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.529000 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2b | Windows | 0.640400 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.516600 | 2026-10-09T08:55:45Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.529200 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2a | Windows | 0.322800 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.490800 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2b | Windows | 0.324700 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.496800 | 2026-10-09T08:55:45Z |
| us-west-2 | us-west-2c | Windows | 0.322900 | 2026-10-09T08:55:45Z |
