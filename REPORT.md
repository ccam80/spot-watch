# Spot placement score log

Generated 2026-11-17 03:43 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 544 | 48% | 5.2 | 1 (11-17 03:43Z) |
| ap-northeast-1 | 544 | 17% | 2.8 | 1 (11-17 03:43Z) |
| ap-northeast-2 | 544 | 69% | 7.1 | 9 (11-17 03:43Z) |
| ap-south-1 | 544 | 3% | 1.7 | 1 (11-17 03:43Z) |
| ap-southeast-2 | 544 | 1% | 1.0 | 1 (11-17 03:43Z) |
| ap-southeast-3 | 544 | 24% | 3.1 | 1 (11-17 03:43Z) |
| us-east-1 | 544 | 11% | 2.7 | 5 (11-17 03:43Z) |
| us-east-2 | 544 | 31% | 3.7 | 1 (11-17 03:43Z) |
| us-west-2 | 544 | 9% | 2.1 | 1 (11-17 03:43Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        112991119199991999819919121911111111199199611391
ap-northeast-1   112211211119199919911211111511121129995999991191
ap-northeast-2   999999999999999999999999991911111111199999999799
ap-south-1       211122222122211311911112211111111111111191111111
ap-southeast-2   117111111111111111111111111111111111111111111111
ap-southeast-3   111111311111111113111111111311111111111211311131
us-east-1        333332232213222222329293322423233344223323737465
us-east-2        211191111111999919999111111111111111119919919991
us-west-2        211191111122922111211111212221112122111219111121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 5 | 3 | 2 | 3 | 4 | 5 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 170 | 5% | 1.5 | 1 (11-17 03:43Z) |
| ap-east-1 ape1-az2 | 397 | 66% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az1 | 131 | 11% | 2.0 | 5 (11-16 20:20Z) |
| ap-northeast-1 apne1-az4 | 253 | 28% | 3.6 | 1 (11-17 03:43Z) |
| ap-northeast-2 apne2-az1 | 462 | 63% | 6.6 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 501 | 69% | 7.0 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az4 | 531 | 70% | 7.2 | 9 (11-17 03:43Z) |
| ap-south-1 aps1-az1 | 158 | 1% | 1.3 | 1 (11-16 09:29Z) |
| ap-south-1 aps1-az3 | 157 | 7% | 2.3 | 1 (11-17 03:43Z) |
| ap-southeast-2 apse2-az1 | 112 | 3% | 1.2 | 1 (11-17 03:43Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 95 | 0% | 1.0 | 1 (11-17 03:43Z) |
| ap-southeast-3 apse3-az3 | 330 | 37% | 4.2 | 3 (11-16 20:20Z) |
| us-east-1 use1-az1 | 116 | 0% | 1.1 | 1 (11-16 01:54Z) |
| us-east-1 use1-az2 | 143 | 3% | 1.4 | 1 (11-16 20:20Z) |
| us-east-1 use1-az4 | 175 | 22% | 2.9 | 2 (11-17 03:43Z) |
| us-east-1 use1-az5 | 173 | 24% | 3.1 | 1 (11-17 03:43Z) |
| us-east-1 use1-az6 | 133 | 23% | 3.0 | 1 (11-16 09:29Z) |
| us-east-2 use2-az1 | 238 | 43% | 4.6 | 9 (11-16 09:29Z) |
| us-east-2 use2-az2 | 278 | 51% | 5.3 | 1 (11-17 03:43Z) |
| us-east-2 use2-az3 | 305 | 48% | 5.1 | 9 (11-16 09:29Z) |
| us-west-2 usw2-az1 | 171 | 22% | 3.0 | 1 (11-17 03:43Z) |
| us-west-2 usw2-az2 | 126 | 17% | 2.5 | 1 (11-15 21:41Z) |
| us-west-2 usw2-az3 | 206 | 17% | 2.7 | 1 (11-16 09:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 544 | 72% | 7.3 | 9 (11-17 03:43Z) |
| ap-northeast-1 | 544 | 72% | 7.0 | 2 (11-17 03:43Z) |
| ap-northeast-2 | 544 | 100% | 9.0 | 9 (11-17 03:43Z) |
| ap-south-1 | 544 | 59% | 6.1 | 1 (11-17 03:43Z) |
| ap-southeast-2 | 544 | 27% | 3.6 | 1 (11-17 03:43Z) |
| ap-southeast-3 | 544 | 24% | 3.1 | 1 (11-17 03:43Z) |
| us-east-1 | 544 | 72% | 6.5 | 8 (11-17 03:43Z) |
| us-east-2 | 544 | 68% | 6.7 | 9 (11-17 03:43Z) |
| us-west-2 | 544 | 51% | 5.6 | 9 (11-17 03:43Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   219919922999999999993922992992894299999999992292
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911922992199217911991392291111119111111991111111
ap-southeast-2   119199119999999919911911911991991191329999911181
ap-southeast-3   111111311111111113111111111311111111111211311131
us-east-1        697655579579999999999599669968966978999997999998
us-east-2        991291119119999999999119919919999999999999919999
us-west-2        434294944195955999999494334933434194239939991159
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 7 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 8 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 349 | 85% | 8.1 | 9 (11-17 03:43Z) |
| ap-east-1 ape1-az2 | 318 | 87% | 8.2 | 9 (11-17 03:43Z) |
| ap-east-1 ape1-az3 | 347 | 87% | 8.2 | 9 (11-16 09:29Z) |
| ap-northeast-1 apne1-az1 | 218 | 95% | 8.7 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az2 | 203 | 87% | 8.2 | 9 (11-16 20:20Z) |
| ap-northeast-1 apne1-az4 | 280 | 99% | 8.9 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az1 | 441 | 100% | 9.0 | 9 (11-17 03:43Z) |
| ap-northeast-2 apne2-az2 | 120 | 87% | 8.1 | 9 (11-16 20:20Z) |
| ap-northeast-2 apne2-az3 | 456 | 100% | 9.0 | 9 (11-17 03:43Z) |
| ap-northeast-2 apne2-az4 | 356 | 87% | 8.2 | 9 (11-17 03:43Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 87 | 84% | 8.0 | 9 (11-15 16:59Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 118 | 99% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az4 | 157 | 92% | 8.4 | 9 (11-16 09:29Z) |
| us-east-1 use1-az5 | 114 | 98% | 8.9 | 9 (11-16 09:29Z) |
| us-east-1 use1-az6 | 138 | 93% | 8.5 | 9 (11-16 01:54Z) |
| us-east-2 use2-az1 | 194 | 99% | 8.9 | 9 (11-17 03:43Z) |
| us-east-2 use2-az2 | 214 | 99% | 8.9 | 9 (11-17 03:43Z) |
| us-east-2 use2-az3 | 240 | 97% | 8.8 | 9 (11-17 03:43Z) |
| us-west-2 usw2-az1 | 104 | 98% | 8.9 | 9 (11-17 03:43Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 143 | 88% | 8.2 | 9 (11-17 03:43Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.702100 | 2026-11-17T03:43:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-17T03:43:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.719300 | 2026-11-17T03:43:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.609100 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.622200 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.608300 | 2026-11-17T03:43:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-17T03:43:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.685500 | 2026-11-17T03:43:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.399200 | 2026-11-17T03:43:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.656200 | 2026-11-17T03:43:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.400600 | 2026-11-17T03:43:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.649000 | 2026-11-17T03:43:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.517900 | 2026-11-17T03:43:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.496400 | 2026-11-17T03:43:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.877700 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.860800 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.607000 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.627900 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.532800 | 2026-11-17T03:43:46Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.537600 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.558500 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.540700 | 2026-11-17T03:43:46Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.683300 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2a | Windows | 0.330500 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.606300 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.643000 | 2026-11-17T03:43:46Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-17T03:43:46Z |
