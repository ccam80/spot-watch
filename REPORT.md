# Spot placement score log

Generated 2026-10-25 11:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 371 | 44% | 5.0 | 9 (10-25 11:16Z) |
| ap-northeast-1 | 371 | 17% | 2.9 | 1 (10-25 11:16Z) |
| ap-northeast-2 | 371 | 58% | 6.5 | 9 (10-25 11:16Z) |
| ap-south-1 | 371 | 2% | 1.8 | 1 (10-25 11:16Z) |
| ap-southeast-2 | 371 | 1% | 1.1 | 1 (10-25 11:16Z) |
| ap-southeast-3 | 371 | 26% | 3.5 | 8 (10-25 11:16Z) |
| us-east-1 | 371 | 11% | 2.7 | 9 (10-25 11:16Z) |
| us-east-2 | 371 | 31% | 3.8 | 3 (10-25 11:16Z) |
| us-west-2 | 371 | 11% | 2.3 | 1 (10-25 11:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999991119999999999999999199999999999
ap-northeast-1   129324165912221981121211121111282112499999499991
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222222222222222222222222222211111111111149991
ap-southeast-2   191191111111111111111111111111111111111111111111
ap-southeast-3   518679924748811787113651189911599119191128587428
us-east-1        333221923999999112132112121115123222232219919939
us-east-2        161999999199999119991119911199111191111999999193
us-west-2        112121219119211211111113122195121122122222221191
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 5 | 7 | 5 | 4 | 4 | 7 | 4 | 5 | 7 | 4 | 7 | 6 | 5 | 5 | 4 | 7 | 5 | 5 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 4 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 8 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 6 | 6 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 123 | 7% | 1.7 | 1 (10-23 19:06Z) |
| ap-east-1 ape1-az2 | 273 | 60% | 6.3 | 9 (10-25 11:16Z) |
| ap-northeast-1 apne1-az1 | 62 | 6% | 1.7 | 1 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 172 | 30% | 3.9 | 9 (10-25 06:03Z) |
| ap-northeast-2 apne2-az1 | 323 | 53% | 6.0 | 1 (10-25 11:16Z) |
| ap-northeast-2 apne2-az3 | 342 | 58% | 6.4 | 9 (10-25 11:16Z) |
| ap-northeast-2 apne2-az4 | 367 | 58% | 6.5 | 9 (10-25 11:16Z) |
| ap-south-1 aps1-az1 | 89 | 1% | 1.5 | 1 (10-23 22:05Z) |
| ap-south-1 aps1-az3 | 118 | 4% | 2.4 | 9 (10-25 01:06Z) |
| ap-southeast-2 apse2-az1 | 60 | 3% | 1.3 | 1 (10-25 11:16Z) |
| ap-southeast-2 apse2-az2 | 37 | 0% | 1.0 | 1 (10-23 04:37Z) |
| ap-southeast-3 apse3-az1 | 76 | 0% | 1.0 | 1 (10-23 19:06Z) |
| ap-southeast-3 apse3-az3 | 249 | 37% | 4.5 | 8 (10-25 11:16Z) |
| us-east-1 use1-az1 | 74 | 0% | 1.1 | 1 (10-24 20:42Z) |
| us-east-1 use1-az2 | 99 | 3% | 1.5 | 1 (10-23 09:57Z) |
| us-east-1 use1-az4 | 117 | 30% | 3.6 | 9 (10-25 01:06Z) |
| us-east-1 use1-az5 | 118 | 29% | 3.5 | 1 (10-25 11:16Z) |
| us-east-1 use1-az6 | 85 | 26% | 3.3 | 9 (10-25 01:06Z) |
| us-east-2 use2-az1 | 153 | 46% | 4.9 | 9 (10-25 06:03Z) |
| us-east-2 use2-az2 | 196 | 50% | 5.3 | 9 (10-25 06:03Z) |
| us-east-2 use2-az3 | 226 | 48% | 5.3 | 1 (10-25 11:16Z) |
| us-west-2 usw2-az1 | 131 | 27% | 3.5 | 9 (10-25 06:03Z) |
| us-west-2 usw2-az2 | 83 | 23% | 3.1 | 1 (10-25 11:16Z) |
| us-west-2 usw2-az3 | 137 | 22% | 3.2 | 9 (10-25 06:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 371 | 59% | 6.5 | 9 (10-25 11:16Z) |
| ap-northeast-1 | 371 | 74% | 7.2 | 9 (10-25 11:16Z) |
| ap-northeast-2 | 371 | 100% | 9.0 | 9 (10-25 11:16Z) |
| ap-south-1 | 371 | 64% | 6.5 | 9 (10-25 11:16Z) |
| ap-southeast-2 | 371 | 19% | 3.2 | 9 (10-25 11:16Z) |
| ap-southeast-3 | 371 | 26% | 3.5 | 8 (10-25 11:16Z) |
| us-east-1 | 371 | 71% | 6.5 | 9 (10-25 11:16Z) |
| us-east-2 | 371 | 71% | 6.9 | 8 (10-25 11:16Z) |
| us-west-2 | 371 | 53% | 5.7 | 9 (10-25 11:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999932991239992399923999239999999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999992999922282299992999991999999999999
ap-southeast-2   999999999999111911111111111111111111111111919999
ap-southeast-3   518679924748811787113651189911599119191128587428
us-east-1        599999999999999464563444364339246564565999999999
us-east-2        399999999999999239995299912999722195226999999198
us-west-2        439999999999999534394339145399933345453459995499
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 6 | 6 | 6 | 8 | 8 | 6 | 8 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 6 | 5 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 4 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 5 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 229 | 76% | 7.6 | 9 (10-25 01:06Z) |
| ap-east-1 ape1-az2 | 192 | 79% | 7.7 | 9 (10-25 11:16Z) |
| ap-east-1 ape1-az3 | 199 | 78% | 7.7 | 9 (10-25 01:06Z) |
| ap-northeast-1 apne1-az1 | 168 | 93% | 8.6 | 9 (10-25 06:03Z) |
| ap-northeast-1 apne1-az2 | 114 | 76% | 7.6 | 9 (10-25 11:16Z) |
| ap-northeast-1 apne1-az4 | 211 | 99% | 8.9 | 9 (10-25 01:06Z) |
| ap-northeast-2 apne2-az1 | 295 | 100% | 9.0 | 9 (10-25 06:03Z) |
| ap-northeast-2 apne2-az2 | 77 | 79% | 7.7 | 9 (10-24 10:49Z) |
| ap-northeast-2 apne2-az3 | 318 | 100% | 9.0 | 9 (10-25 11:16Z) |
| ap-northeast-2 apne2-az4 | 226 | 79% | 7.8 | 9 (10-25 11:16Z) |
| ap-south-1 aps1-az1 | 129 | 83% | 8.0 | 9 (10-25 06:03Z) |
| ap-south-1 aps1-az2 | 142 | 75% | 7.4 | 9 (10-25 11:16Z) |
| ap-south-1 aps1-az3 | 153 | 88% | 8.3 | 9 (10-25 06:03Z) |
| ap-southeast-2 apse2-az1 | 33 | 70% | 7.1 | 9 (10-25 11:16Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 46 | 72% | 7.3 | 9 (10-25 06:03Z) |
| ap-southeast-3 apse3-az3 | 71 | 37% | 5.1 | 9 (10-23 22:05Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 91 | 100% | 9.0 | 9 (10-25 11:16Z) |
| us-east-1 use1-az4 | 110 | 95% | 8.6 | 9 (10-25 06:03Z) |
| us-east-1 use1-az5 | 77 | 97% | 8.8 | 9 (10-25 06:03Z) |
| us-east-1 use1-az6 | 95 | 96% | 8.7 | 9 (10-25 11:16Z) |
| us-east-2 use2-az1 | 126 | 98% | 8.9 | 9 (10-24 14:27Z) |
| us-east-2 use2-az2 | 166 | 99% | 8.9 | 9 (10-24 10:49Z) |
| us-east-2 use2-az3 | 166 | 95% | 8.7 | 9 (10-25 06:03Z) |
| us-west-2 usw2-az1 | 81 | 98% | 8.8 | 9 (10-25 11:16Z) |
| us-west-2 usw2-az2 | 76 | 96% | 8.7 | 9 (10-25 06:03Z) |
| us-west-2 usw2-az3 | 96 | 94% | 8.6 | 9 (10-25 11:16Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707200 | 2026-10-25T11:16:01Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-25T11:16:01Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.761100 | 2026-10-25T11:16:01Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.946200 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.588700 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.585100 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568800 | 2026-10-25T11:16:01Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740900 | 2026-10-25T11:16:01Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.529800 | 2026-10-25T11:16:01Z |
| ap-south-1 | ap-south-1a | Windows | 0.425400 | 2026-10-25T11:16:01Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.708100 | 2026-10-25T11:16:01Z |
| ap-south-1 | ap-south-1b | Windows | 0.409000 | 2026-10-25T11:16:01Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.662300 | 2026-10-25T11:16:01Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.469600 | 2026-10-25T11:16:01Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656200 | 2026-10-25T11:16:01Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.545400 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.596800 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.440900 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.487200 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.502500 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.522600 | 2026-10-25T11:16:01Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.572400 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2a | Windows | 0.640100 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550400 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2b | Windows | 0.638000 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547000 | 2026-10-25T11:16:01Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.549200 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2a | Windows | 0.317100 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.567100 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2b | Windows | 0.330300 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.539300 | 2026-10-25T11:16:01Z |
| us-west-2 | us-west-2c | Windows | 0.316800 | 2026-10-25T11:16:01Z |
