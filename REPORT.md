# Spot placement score log

Generated 2026-10-22 23:16 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 356 | 42% | 4.8 | 9 (10-22 23:16Z) |
| ap-northeast-1 | 356 | 15% | 2.7 | 2 (10-22 23:16Z) |
| ap-northeast-2 | 356 | 56% | 6.3 | 9 (10-22 23:16Z) |
| ap-south-1 | 356 | 2% | 1.8 | 1 (10-22 23:16Z) |
| ap-southeast-2 | 356 | 1% | 1.1 | 1 (10-22 23:16Z) |
| ap-southeast-3 | 356 | 26% | 3.4 | 9 (10-22 23:16Z) |
| us-east-1 | 356 | 10% | 2.6 | 3 (10-22 23:16Z) |
| us-east-2 | 356 | 30% | 3.8 | 1 (10-22 23:16Z) |
| us-west-2 | 356 | 11% | 2.3 | 1 (10-22 23:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999991119999999999999
ap-northeast-1   142211421111322129324165912221981121211121111282
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       122222221112222222222222222222222222222222222211
ap-southeast-2   111111111111111191191111111111111111111111111111
ap-southeast-3   111311518214387518679924748811787113651189911599
us-east-1        332321323122222333221923999999112132112121115123
us-east-2        911129111999111161999999199999119991119911199111
us-west-2        111111221111222112121219119211211111113122195121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 5 | 7 | 4 | 4 | 4 | 7 | 4 | 5 | 6 | 4 | 7 | 6 | 4 | 5 | 4 | 7 | 5 | 5 | 6 | 3 | 5 | 5 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 5 | 7 | 9 | 8 | 5 | 6 | 5 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 7 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 1 | 6 | 2 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-2 | 3 | 5 | 4 | 3 | 3 | 5 | 5 | 8 | 5 | 5 | 7 | 5 | 6 | 4 | 2 | 2 | 1 | 5 | 3 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 122 | 7% | 1.7 | 1 (10-22 15:10Z) |
| ap-east-1 ape1-az2 | 259 | 58% | 6.2 | 9 (10-22 23:16Z) |
| ap-northeast-1 apne1-az1 | 59 | 7% | 1.7 | 1 (10-22 23:16Z) |
| ap-northeast-1 apne1-az4 | 163 | 26% | 3.6 | 8 (10-22 19:59Z) |
| ap-northeast-2 apne2-az1 | 310 | 51% | 5.9 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az3 | 328 | 57% | 6.3 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az4 | 353 | 57% | 6.4 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az1 | 85 | 1% | 1.6 | 1 (10-22 23:16Z) |
| ap-south-1 aps1-az3 | 116 | 3% | 2.3 | 1 (10-22 15:10Z) |
| ap-southeast-2 apse2-az1 | 57 | 4% | 1.4 | 1 (10-22 19:59Z) |
| ap-southeast-2 apse2-az2 | 36 | 0% | 1.0 | 1 (10-21 23:14Z) |
| ap-southeast-3 apse3-az1 | 75 | 0% | 1.0 | 1 (10-21 10:02Z) |
| ap-southeast-3 apse3-az3 | 241 | 36% | 4.4 | 9 (10-22 23:16Z) |
| us-east-1 use1-az1 | 69 | 0% | 1.1 | 1 (10-22 04:32Z) |
| us-east-1 use1-az2 | 98 | 3% | 1.5 | 1 (10-20 20:29Z) |
| us-east-1 use1-az4 | 109 | 29% | 3.6 | 1 (10-22 23:16Z) |
| us-east-1 use1-az5 | 113 | 27% | 3.4 | 1 (10-22 15:10Z) |
| us-east-1 use1-az6 | 81 | 25% | 3.2 | 1 (10-21 23:14Z) |
| us-east-2 use2-az1 | 144 | 44% | 4.8 | 1 (10-22 23:16Z) |
| us-east-2 use2-az2 | 186 | 48% | 5.2 | 7 (10-22 10:03Z) |
| us-east-2 use2-az3 | 216 | 47% | 5.2 | 1 (10-22 19:59Z) |
| us-west-2 usw2-az1 | 130 | 26% | 3.5 | 1 (10-22 15:10Z) |
| us-west-2 usw2-az2 | 78 | 23% | 3.2 | 1 (10-22 19:59Z) |
| us-west-2 usw2-az3 | 132 | 22% | 3.2 | 1 (10-22 23:16Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 356 | 57% | 6.4 | 9 (10-22 23:16Z) |
| ap-northeast-1 | 356 | 73% | 7.1 | 9 (10-22 23:16Z) |
| ap-northeast-2 | 356 | 100% | 9.0 | 9 (10-22 23:16Z) |
| ap-south-1 | 356 | 62% | 6.4 | 9 (10-22 23:16Z) |
| ap-southeast-2 | 356 | 19% | 3.2 | 1 (10-22 23:16Z) |
| ap-southeast-3 | 356 | 26% | 3.4 | 9 (10-22 23:16Z) |
| us-east-1 | 356 | 70% | 6.5 | 6 (10-22 23:16Z) |
| us-east-2 | 356 | 71% | 6.9 | 2 (10-22 23:16Z) |
| us-west-2 | 356 | 52% | 5.7 | 3 (10-22 23:16Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   399921999119999999999999999932991239992399923999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       122992299912999999999999999992999922282299992999
ap-southeast-2   118111111111111999999999999111911111111111111111
ap-southeast-3   111311518214387518679924748811787113651189911599
us-east-1        643555546793446599999999999999464563444364339246
us-east-2        911229111999311399999999999999239995299912999722
us-west-2        953433554334454439999999999999534394339145399933
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 5 | 8 | 9 | 8 | 5 | 6 | 6 | 8 | 8 | 6 | 7 | 5 | 8 | 7 | 5 | 8 | 6 | 8 | 6 | 6 | 7 | 6 | 6 | 6 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 9 | 6 | 4 | 4 | 3 | 4 | 3 | 4 | 6 | 4 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 3 | 4 | 5 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 8 | 8 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 7 | 9 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 5 | 5 | 7 | 6 | 7 | 5 | 6 | 6 | 6 |
| us-west-2 | 6 | 5 | 4 | 4 | 6 | 6 | 8 | 7 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 220 | 75% | 7.5 | 9 (10-22 23:16Z) |
| ap-east-1 ape1-az2 | 184 | 78% | 7.7 | 9 (10-22 15:10Z) |
| ap-east-1 ape1-az3 | 190 | 77% | 7.6 | 9 (10-22 23:16Z) |
| ap-northeast-1 apne1-az1 | 160 | 93% | 8.6 | 9 (10-21 15:08Z) |
| ap-northeast-1 apne1-az2 | 107 | 75% | 7.5 | 9 (10-22 23:16Z) |
| ap-northeast-1 apne1-az4 | 202 | 99% | 8.9 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az1 | 281 | 100% | 9.0 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az2 | 75 | 80% | 7.7 | 9 (10-21 23:14Z) |
| ap-northeast-2 apne2-az3 | 309 | 100% | 9.0 | 9 (10-22 23:16Z) |
| ap-northeast-2 apne2-az4 | 218 | 78% | 7.7 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az1 | 123 | 82% | 7.9 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az2 | 131 | 73% | 7.3 | 9 (10-22 23:16Z) |
| ap-south-1 aps1-az3 | 144 | 87% | 8.2 | 9 (10-22 04:32Z) |
| ap-southeast-2 apse2-az1 | 31 | 68% | 7.0 | 9 (10-18 18:01Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 44 | 70% | 7.2 | 9 (10-19 15:31Z) |
| ap-southeast-3 apse3-az3 | 69 | 35% | 5.0 | 9 (10-22 23:16Z) |
| us-east-1 use1-az1 | 22 | 55% | 5.7 | 2 (10-21 10:02Z) |
| us-east-1 use1-az2 | 86 | 100% | 9.0 | 9 (10-22 10:03Z) |
| us-east-1 use1-az4 | 105 | 94% | 8.6 | 9 (10-22 10:03Z) |
| us-east-1 use1-az5 | 71 | 97% | 8.8 | 9 (10-22 10:03Z) |
| us-east-1 use1-az6 | 91 | 96% | 8.7 | 9 (10-19 01:08Z) |
| us-east-2 use2-az1 | 123 | 98% | 8.9 | 9 (10-22 04:32Z) |
| us-east-2 use2-az2 | 164 | 99% | 8.9 | 9 (10-22 10:03Z) |
| us-east-2 use2-az3 | 161 | 95% | 8.7 | 9 (10-22 10:03Z) |
| us-west-2 usw2-az1 | 80 | 98% | 8.8 | 9 (10-20 11:25Z) |
| us-west-2 usw2-az2 | 75 | 96% | 8.7 | 9 (10-22 04:32Z) |
| us-west-2 usw2-az3 | 93 | 95% | 8.6 | 9 (10-22 04:32Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.711900 | 2026-10-22T23:16:14Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-22T23:16:14Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.757600 | 2026-10-22T23:16:14Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.938500 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.586600 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580300 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566100 | 2026-10-22T23:16:14Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741000 | 2026-10-22T23:16:14Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.540800 | 2026-10-22T23:16:14Z |
| ap-south-1 | ap-south-1a | Windows | 0.389200 | 2026-10-22T23:16:14Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.757100 | 2026-10-22T23:16:14Z |
| ap-south-1 | ap-south-1b | Windows | 0.375800 | 2026-10-22T23:16:14Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.670100 | 2026-10-22T23:16:14Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.479500 | 2026-10-22T23:16:14Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.656000 | 2026-10-22T23:16:14Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.539500 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.535700 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.466900 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.490400 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.497300 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.492300 | 2026-10-22T23:16:14Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.553500 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2a | Windows | 0.640300 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.546400 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2b | Windows | 0.638500 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.543800 | 2026-10-22T23:16:14Z |
| us-east-2 | us-east-2c | Windows | 0.637200 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.547900 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2a | Windows | 0.316800 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.547300 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2b | Windows | 0.330300 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.527200 | 2026-10-22T23:16:14Z |
| us-west-2 | us-west-2c | Windows | 0.316500 | 2026-10-22T23:16:14Z |
