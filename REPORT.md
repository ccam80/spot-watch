# Spot placement score log

Generated 2026-09-29 05:24 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 210 | 22% | 3.5 | 9 (09-29 05:24Z) |
| ap-northeast-1 | 210 | 7% | 2.3 | 2 (09-29 05:24Z) |
| ap-northeast-2 | 210 | 27% | 4.6 | 9 (09-29 05:24Z) |
| ap-south-1 | 210 | 3% | 2.0 | 1 (09-29 05:24Z) |
| ap-southeast-2 | 210 | 0% | 1.0 | 1 (09-29 05:24Z) |
| ap-southeast-3 | 210 | 19% | 3.4 | 1 (09-29 05:24Z) |
| us-east-1 | 210 | 7% | 2.4 | 1 (09-29 05:24Z) |
| us-east-2 | 210 | 16% | 2.8 | 1 (09-29 05:24Z) |
| us-west-2 | 210 | 10% | 2.4 | 1 (09-29 05:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        119199919999998899113991114999999999999999999999
ap-northeast-1   343221555316644442111111111111898994558941221222
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111311411115999279134411111111121111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   989158999928699989111111115368786755668889111111
us-east-1        122332239233222299991199999199911111112111112911
us-east-2        928999999999999999999999999999911111111111111111
us-west-2        112199519299129999999999999999111111111111112211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | 6 | 6 | 3 | 3 | 2 | 5 | 4 | 3 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 2 | 3 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 5 | 4 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 4 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 6 | 4 | 2 | 2 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 69 | 0% | 1.4 | 1 (09-29 05:24Z) |
| ap-east-1 ape1-az2 | 142 | 32% | 4.6 | 9 (09-29 05:24Z) |
| ap-northeast-1 apne1-az1 | 30 | 0% | 1.2 | 1 (09-29 04:27Z) |
| ap-northeast-1 apne1-az4 | 92 | 8% | 2.6 | 1 (09-29 05:24Z) |
| ap-northeast-2 apne2-az1 | 188 | 27% | 4.6 | 9 (09-29 05:24Z) |
| ap-northeast-2 apne2-az3 | 192 | 30% | 4.7 | 9 (09-29 05:24Z) |
| ap-northeast-2 apne2-az4 | 207 | 28% | 4.6 | 9 (09-29 05:24Z) |
| ap-south-1 aps1-az1 | 63 | 2% | 1.7 | 1 (09-29 03:28Z) |
| ap-south-1 aps1-az3 | 89 | 3% | 2.7 | 1 (09-29 01:00Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 20 | 0% | 1.0 | 1 (09-29 01:00Z) |
| ap-southeast-3 apse3-az1 | 42 | 0% | 1.0 | 1 (09-29 05:24Z) |
| ap-southeast-3 apse3-az3 | 157 | 23% | 4.0 | 1 (09-29 04:27Z) |
| us-east-1 use1-az1 | 28 | 0% | 1.2 | 1 (09-29 04:27Z) |
| us-east-1 use1-az2 | 61 | 3% | 1.6 | 1 (09-29 05:24Z) |
| us-east-1 use1-az4 | 60 | 22% | 3.1 | 1 (09-29 04:27Z) |
| us-east-1 use1-az5 | 63 | 17% | 2.8 | 1 (09-29 01:00Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 75 | 21% | 3.2 | 1 (09-29 04:27Z) |
| us-east-2 use2-az2 | 103 | 27% | 3.8 | 1 (09-29 05:24Z) |
| us-east-2 use2-az3 | 121 | 26% | 3.9 | 1 (09-29 05:24Z) |
| us-west-2 usw2-az1 | 71 | 28% | 3.9 | 1 (09-28 21:20Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 100 | 18% | 3.0 | 1 (09-29 03:28Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 210 | 27% | 4.6 | 9 (09-29 05:24Z) |
| ap-northeast-1 | 210 | 76% | 7.3 | 2 (09-29 05:24Z) |
| ap-northeast-2 | 210 | 100% | 9.0 | 9 (09-29 05:24Z) |
| ap-south-1 | 210 | 57% | 6.3 | 9 (09-29 05:24Z) |
| ap-southeast-2 | 210 | 17% | 3.3 | 2 (09-29 05:24Z) |
| ap-southeast-3 | 210 | 19% | 3.4 | 1 (09-29 05:24Z) |
| us-east-1 | 210 | 76% | 7.0 | 7 (09-29 05:24Z) |
| us-east-2 | 210 | 75% | 7.2 | 9 (09-29 05:24Z) |
| us-west-2 | 210 | 57% | 6.0 | 2 (09-29 05:24Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999111111111389999999999999333522
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999999999999932112299999999999999999
ap-southeast-2   999999999999999922222222222242794999932212222222
ap-southeast-3   989158999928699989111111115368786755668889111111
us-east-1        347999999999999999999999999999922123445433698957
us-east-2        999999999999999999999999999999992233332233223999
us-west-2        934399999999999999999999999999999944343322444422
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 7 | 4 | 5 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 7 | 6 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 7 | 5 | 6 | 6 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 5 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 8 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 6 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 6 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 8 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 5 | 6 | 5 | 6 | 6 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 101 | 47% | 5.8 | 9 (09-29 05:24Z) |
| ap-east-1 ape1-az2 | 77 | 47% | 5.8 | 9 (09-29 05:24Z) |
| ap-east-1 ape1-az3 | 75 | 41% | 5.5 | 9 (09-29 05:24Z) |
| ap-northeast-1 apne1-az1 | 99 | 92% | 8.5 | 9 (09-28 20:22Z) |
| ap-northeast-1 apne1-az2 | 39 | 33% | 5.0 | 9 (09-28 23:21Z) |
| ap-northeast-1 apne1-az4 | 126 | 100% | 9.0 | 9 (09-28 23:21Z) |
| ap-northeast-2 apne2-az1 | 164 | 100% | 9.0 | 9 (09-29 05:24Z) |
| ap-northeast-2 apne2-az2 | 45 | 69% | 7.0 | 9 (09-29 04:27Z) |
| ap-northeast-2 apne2-az3 | 187 | 100% | 9.0 | 9 (09-29 05:24Z) |
| ap-northeast-2 apne2-az4 | 95 | 51% | 6.0 | 9 (09-29 05:24Z) |
| ap-south-1 aps1-az1 | 62 | 65% | 6.9 | 9 (09-29 03:28Z) |
| ap-south-1 aps1-az2 | 73 | 51% | 6.0 | 9 (09-29 05:24Z) |
| ap-south-1 aps1-az3 | 88 | 80% | 7.8 | 9 (09-29 04:27Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 26 | 54% | 6.2 | 9 (09-28 17:21Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 85 | 98% | 8.8 | 9 (09-29 03:28Z) |
| us-east-1 use1-az5 | 47 | 98% | 8.9 | 9 (09-29 03:28Z) |
| us-east-1 use1-az6 | 74 | 99% | 8.9 | 2 (09-29 01:00Z) |
| us-east-2 use2-az1 | 77 | 99% | 8.9 | 9 (09-29 05:24Z) |
| us-east-2 use2-az2 | 110 | 98% | 8.9 | 9 (09-29 05:24Z) |
| us-east-2 use2-az3 | 101 | 92% | 8.5 | 9 (09-29 05:24Z) |
| us-west-2 usw2-az1 | 62 | 98% | 8.9 | 9 (09-28 13:26Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 71 | 99% | 8.9 | 9 (09-28 14:27Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.729500 | 2026-09-29T05:24:13Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.881800 | 2026-09-29T05:24:13Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.803300 | 2026-09-29T05:24:13Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.994800 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594100 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577400 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567700 | 2026-09-29T05:24:13Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-29T05:24:13Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.585300 | 2026-09-29T05:24:13Z |
| ap-south-1 | ap-south-1a | Windows | 0.351400 | 2026-09-29T05:24:13Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.604800 | 2026-09-29T05:24:13Z |
| ap-south-1 | ap-south-1b | Windows | 0.338500 | 2026-09-29T05:24:13Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.709700 | 2026-09-29T05:24:13Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.496800 | 2026-09-29T05:24:13Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.640400 | 2026-09-29T05:24:13Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.622800 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1a | Windows | 0.308900 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.465500 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.446300 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.389500 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.440100 | 2026-09-29T05:24:13Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.529800 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524300 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2b | Windows | 0.640900 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514800 | 2026-09-29T05:24:13Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.509600 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2a | Windows | 0.332600 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.498100 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.487100 | 2026-09-29T05:24:13Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-29T05:24:13Z |
