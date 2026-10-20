# Spot placement score log

Generated 2026-10-20 16:52 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 344 | 40% | 4.7 | 9 (10-20 16:52Z) |
| ap-northeast-1 | 344 | 15% | 2.8 | 1 (10-20 16:52Z) |
| ap-northeast-2 | 344 | 55% | 6.3 | 9 (10-20 16:52Z) |
| ap-south-1 | 344 | 2% | 1.8 | 2 (10-20 16:52Z) |
| ap-southeast-2 | 344 | 1% | 1.1 | 1 (10-20 16:52Z) |
| ap-southeast-3 | 344 | 24% | 3.4 | 3 (10-20 16:52Z) |
| us-east-1 | 344 | 10% | 2.6 | 2 (10-20 16:52Z) |
| us-east-2 | 344 | 30% | 3.8 | 1 (10-20 16:52Z) |
| us-west-2 | 344 | 11% | 2.3 | 1 (10-20 16:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        299999999999999999999999999999999999999999991119
ap-northeast-1   211922121211142211421111322129324165912221981121
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       222222221111122222221112222222222222222222222222
ap-southeast-2   111111111111111111111111111191191111111111111111
ap-southeast-3   793951511221111311518214387518679924748811787113
us-east-1        922332221133332321323122222333221923999999112132
us-east-2        999999111129911129111999111161999999199999119991
us-west-2        111111111111111111221111222112121219119211211111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 4 | 4 | 7 | 5 | 4 | 6 | 3 | 5 | 4 |
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
| ap-east-1 ape1-az1 | 120 | 8% | 1.7 | 1 (10-20 16:52Z) |
| ap-east-1 ape1-az2 | 247 | 56% | 6.0 | 9 (10-20 16:52Z) |
| ap-northeast-1 apne1-az1 | 54 | 7% | 1.8 | 1 (10-17 09:13Z) |
| ap-northeast-1 apne1-az4 | 160 | 26% | 3.6 | 1 (10-20 05:56Z) |
| ap-northeast-2 apne2-az1 | 298 | 50% | 5.9 | 9 (10-20 16:52Z) |
| ap-northeast-2 apne2-az3 | 316 | 55% | 6.2 | 9 (10-20 16:52Z) |
| ap-northeast-2 apne2-az4 | 341 | 55% | 6.3 | 9 (10-20 16:52Z) |
| ap-south-1 aps1-az1 | 84 | 1% | 1.6 | 1 (10-17 04:14Z) |
| ap-south-1 aps1-az3 | 113 | 3% | 2.3 | 1 (10-20 05:56Z) |
| ap-southeast-2 apse2-az1 | 54 | 4% | 1.4 | 9 (10-17 19:18Z) |
| ap-southeast-2 apse2-az2 | 33 | 0% | 1.0 | 1 (10-14 13:38Z) |
| ap-southeast-3 apse3-az1 | 73 | 0% | 1.0 | 1 (10-20 16:52Z) |
| ap-southeast-3 apse3-az3 | 233 | 34% | 4.3 | 3 (10-20 16:52Z) |
| us-east-1 use1-az1 | 66 | 0% | 1.1 | 1 (10-20 11:25Z) |
| us-east-1 use1-az2 | 97 | 3% | 1.5 | 1 (10-20 16:52Z) |
| us-east-1 use1-az4 | 105 | 30% | 3.7 | 1 (10-20 11:25Z) |
| us-east-1 use1-az5 | 110 | 28% | 3.5 | 8 (10-19 07:40Z) |
| us-east-1 use1-az6 | 79 | 25% | 3.2 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 139 | 44% | 4.8 | 9 (10-20 11:25Z) |
| us-east-2 use2-az2 | 181 | 48% | 5.1 | 1 (10-20 16:52Z) |
| us-east-2 use2-az3 | 211 | 46% | 5.1 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az1 | 125 | 26% | 3.5 | 1 (10-20 16:52Z) |
| us-west-2 usw2-az2 | 73 | 25% | 3.3 | 1 (10-20 11:25Z) |
| us-west-2 usw2-az3 | 128 | 23% | 3.3 | 9 (10-18 10:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 344 | 56% | 6.3 | 9 (10-20 16:52Z) |
| ap-northeast-1 | 344 | 73% | 7.1 | 9 (10-20 16:52Z) |
| ap-northeast-2 | 344 | 100% | 9.0 | 9 (10-20 16:52Z) |
| ap-south-1 | 344 | 62% | 6.4 | 2 (10-20 16:52Z) |
| ap-southeast-2 | 344 | 19% | 3.3 | 1 (10-20 16:52Z) |
| ap-southeast-3 | 344 | 24% | 3.4 | 3 (10-20 16:52Z) |
| us-east-1 | 344 | 71% | 6.6 | 3 (10-20 16:52Z) |
| us-east-2 | 344 | 71% | 6.9 | 5 (10-20 16:52Z) |
| us-west-2 | 344 | 53% | 5.8 | 4 (10-20 16:52Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999923992399921999119999999999999999932991239
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999992991999122992299912999999999999999992999922
ap-southeast-2   999111111111118111111111111999999999999111911111
ap-southeast-3   793951511221111311518214387518679924748811787113
us-east-1        999999454266643555546793446599999999999999464563
us-east-2        999999119129911229111999311399999999999999239995
us-west-2        993592994424953433554334454439999999999999534394
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
| ap-east-1 ape1-az1 | 211 | 74% | 7.5 | 9 (10-20 16:52Z) |
| ap-east-1 ape1-az2 | 175 | 77% | 7.6 | 9 (10-20 16:52Z) |
| ap-east-1 ape1-az3 | 179 | 75% | 7.5 | 9 (10-20 16:52Z) |
| ap-northeast-1 apne1-az1 | 158 | 93% | 8.6 | 9 (10-20 16:52Z) |
| ap-northeast-1 apne1-az2 | 100 | 73% | 7.4 | 9 (10-20 16:52Z) |
| ap-northeast-1 apne1-az4 | 195 | 98% | 8.9 | 9 (10-20 16:52Z) |
| ap-northeast-2 apne2-az1 | 269 | 100% | 9.0 | 9 (10-20 16:52Z) |
| ap-northeast-2 apne2-az2 | 72 | 79% | 7.7 | 9 (10-17 22:13Z) |
| ap-northeast-2 apne2-az3 | 297 | 100% | 9.0 | 9 (10-20 16:52Z) |
| ap-northeast-2 apne2-az4 | 207 | 77% | 7.6 | 9 (10-20 16:52Z) |
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
| us-east-2 use2-az1 | 118 | 98% | 8.9 | 9 (10-20 11:25Z) |
| us-east-2 use2-az2 | 161 | 99% | 8.9 | 9 (10-20 11:25Z) |
| us-east-2 use2-az3 | 155 | 95% | 8.6 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 74 | 96% | 8.7 | 9 (10-19 07:40Z) |
| us-west-2 usw2-az3 | 92 | 95% | 8.6 | 9 (10-20 11:25Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711200 | 2026-10-20T16:52:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-20T16:52:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.772200 | 2026-10-20T16:52:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.955100 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584800 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580900 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565600 | 2026-10-20T16:52:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741100 | 2026-10-20T16:52:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.561500 | 2026-10-20T16:52:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.393200 | 2026-10-20T16:52:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.758900 | 2026-10-20T16:52:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.370600 | 2026-10-20T16:52:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.687200 | 2026-10-20T16:52:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.495600 | 2026-10-20T16:52:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.663000 | 2026-10-20T16:52:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.541900 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.468100 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.509600 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.508300 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.441900 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.490700 | 2026-10-20T16:52:46Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.554200 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.545900 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2b | Windows | 0.639100 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.543400 | 2026-10-20T16:52:46Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.549700 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2a | Windows | 0.316000 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.543900 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2b | Windows | 0.329000 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528400 | 2026-10-20T16:52:46Z |
| us-west-2 | us-west-2c | Windows | 0.315300 | 2026-10-20T16:52:46Z |
