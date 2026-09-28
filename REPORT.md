# Spot placement score log

Generated 2026-09-28 16:27 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 197 | 17% | 3.1 | 9 (09-28 16:27Z) |
| ap-northeast-1 | 197 | 5% | 2.2 | 9 (09-28 16:27Z) |
| ap-northeast-2 | 197 | 22% | 4.3 | 9 (09-28 16:27Z) |
| ap-south-1 | 197 | 3% | 2.1 | 1 (09-28 16:27Z) |
| ap-southeast-2 | 197 | 0% | 1.0 | 1 (09-28 16:27Z) |
| ap-southeast-3 | 197 | 16% | 3.3 | 5 (09-28 16:27Z) |
| us-east-1 | 197 | 7% | 2.4 | 1 (09-28 16:27Z) |
| us-east-2 | 197 | 17% | 3.0 | 1 (09-28 16:27Z) |
| us-west-2 | 197 | 11% | 2.4 | 1 (09-28 16:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333399999999911919991999999889911399111499999999
ap-northeast-1   222332222221134322155531664444211111111111189899
ap-northeast-2   333399999999999999999999999999999999999999999999
ap-south-1       111111111112111131141111599927913441111111112111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   333399689995198915899992869998911111111536878675
us-east-1        232222123211312233223923322229999119999919991111
us-east-2        311319291121992899999999999999999999999999991111
us-west-2        213222112222111219951929912999999999999999911111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 2 | 2 | 5 | 4 | 3 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 4 | 2 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 3 | 3 | 6 | 6 | 3 | 4 | 3 | 4 | 4 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 3 | 1 | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 3 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 60 | 0% | 1.5 | 2 (09-28 16:27Z) |
| ap-east-1 ape1-az2 | 129 | 26% | 4.1 | 9 (09-28 16:27Z) |
| ap-northeast-1 apne1-az1 | 26 | 0% | 1.3 | 1 (09-28 15:24Z) |
| ap-northeast-1 apne1-az4 | 85 | 6% | 2.5 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az1 | 175 | 22% | 4.2 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az3 | 179 | 25% | 4.4 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az4 | 194 | 23% | 4.4 | 9 (09-28 16:27Z) |
| ap-south-1 aps1-az1 | 61 | 2% | 1.8 | 1 (09-28 16:27Z) |
| ap-south-1 aps1-az3 | 87 | 3% | 2.7 | 1 (09-28 02:38Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 148 | 20% | 3.9 | 5 (09-28 16:27Z) |
| us-east-1 use1-az1 | 21 | 0% | 1.3 | 1 (09-28 15:24Z) |
| us-east-1 use1-az2 | 59 | 3% | 1.6 | 9 (09-28 04:30Z) |
| us-east-1 use1-az4 | 54 | 24% | 3.4 | 1 (09-28 16:27Z) |
| us-east-1 use1-az5 | 61 | 18% | 2.9 | 9 (09-28 12:37Z) |
| us-east-1 use1-az6 | 53 | 9% | 2.1 | 9 (09-28 11:22Z) |
| us-east-2 use2-az1 | 70 | 23% | 3.3 | 1 (09-28 16:27Z) |
| us-east-2 use2-az2 | 98 | 29% | 3.9 | 9 (09-28 12:37Z) |
| us-east-2 use2-az3 | 117 | 26% | 4.0 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az1 | 70 | 29% | 3.9 | 9 (09-28 09:35Z) |
| us-west-2 usw2-az2 | 41 | 27% | 3.8 | 9 (09-28 06:50Z) |
| us-west-2 usw2-az3 | 98 | 18% | 3.1 | 9 (09-28 11:22Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 197 | 22% | 4.3 | 9 (09-28 16:27Z) |
| ap-northeast-1 | 197 | 77% | 7.4 | 9 (09-28 16:27Z) |
| ap-northeast-2 | 197 | 100% | 9.0 | 9 (09-28 16:27Z) |
| ap-south-1 | 197 | 54% | 6.1 | 9 (09-28 16:27Z) |
| ap-southeast-2 | 197 | 17% | 3.3 | 9 (09-28 16:27Z) |
| ap-southeast-3 | 197 | 16% | 3.3 | 5 (09-28 16:27Z) |
| us-east-1 | 197 | 77% | 7.1 | 2 (09-28 16:27Z) |
| us-east-2 | 197 | 78% | 7.5 | 3 (09-28 16:27Z) |
| us-west-2 | 197 | 61% | 6.2 | 4 (09-28 16:27Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333399999999999999999999999999999999999999999999
ap-northeast-1   999999349992199999999999999999911111111138999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       983999928999899999999999999999999999993211229999
ap-southeast-2   223351229922299999999999999992222222222224279499
ap-southeast-3   333399689995198915899992869998911111111536878675
us-east-1        999666995459834799999999999999999999999999992212
us-east-2        999949992348999999999999999999999999999999999223
us-west-2        499555955445993439999999999999999999999999999994
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 4 | 4 | 7 | 6 | 4 | 4 | 4 | 5 | 6 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 4 | 4 | 7 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 6 | 4 | 2 | 6 | 4 | 2 | 7 | 5 | 6 | 6 | 8 | 7 | 7 | 6 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 6 | 2 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 6 | 6 | 6 | 5 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 7 | 8 | 6 | 9 | 7 | 9 | 8 | 7 | 9 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 91 | 41% | 5.4 | 9 (09-28 16:27Z) |
| ap-east-1 ape1-az2 | 67 | 39% | 5.3 | 9 (09-28 16:27Z) |
| ap-east-1 ape1-az3 | 65 | 32% | 4.9 | 9 (09-28 15:24Z) |
| ap-northeast-1 apne1-az1 | 95 | 92% | 8.5 | 9 (09-28 16:27Z) |
| ap-northeast-1 apne1-az2 | 34 | 24% | 4.4 | 9 (09-28 15:24Z) |
| ap-northeast-1 apne1-az4 | 120 | 100% | 9.0 | 9 (09-28 15:24Z) |
| ap-northeast-2 apne2-az1 | 154 | 100% | 9.0 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az2 | 35 | 63% | 6.8 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az3 | 174 | 100% | 9.0 | 9 (09-28 16:27Z) |
| ap-northeast-2 apne2-az4 | 82 | 43% | 5.6 | 9 (09-28 16:27Z) |
| ap-south-1 aps1-az1 | 56 | 61% | 6.6 | 9 (09-28 16:27Z) |
| ap-south-1 aps1-az2 | 61 | 41% | 5.5 | 9 (09-28 16:27Z) |
| ap-south-1 aps1-az3 | 78 | 77% | 7.6 | 9 (09-28 15:24Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 25 | 52% | 6.1 | 9 (09-28 16:27Z) |
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
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730800 | 2026-09-28T16:27:28Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.892000 | 2026-09-28T16:27:28Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.819900 | 2026-09-28T16:27:28Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.002900 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593800 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577300 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567700 | 2026-09-28T16:27:28Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T16:27:28Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.565400 | 2026-09-28T16:27:28Z |
| ap-south-1 | ap-south-1a | Windows | 0.345300 | 2026-09-28T16:27:28Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.586600 | 2026-09-28T16:27:28Z |
| ap-south-1 | ap-south-1b | Windows | 0.336000 | 2026-09-28T16:27:28Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.699100 | 2026-09-28T16:27:28Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.498100 | 2026-09-28T16:27:28Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.661300 | 2026-09-28T16:27:28Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.639400 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1a | Windows | 0.309600 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.477900 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.435800 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.384000 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.423700 | 2026-09-28T16:27:28Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.527800 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.523800 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2b | Windows | 0.641000 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514600 | 2026-09-28T16:27:28Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.509300 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2a | Windows | 0.332900 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.489900 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2b | Windows | 0.332800 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.485900 | 2026-09-28T16:27:28Z |
| us-west-2 | us-west-2c | Windows | 0.331600 | 2026-09-28T16:27:28Z |
