# Spot placement score log

Generated 2026-11-13 16:11 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 531 | 48% | 5.2 | 1 (11-13 16:10Z) |
| ap-northeast-1 | 531 | 16% | 2.7 | 2 (11-13 16:10Z) |
| ap-northeast-2 | 531 | 68% | 7.0 | 1 (11-13 16:10Z) |
| ap-south-1 | 531 | 3% | 1.7 | 1 (11-13 16:10Z) |
| ap-southeast-2 | 531 | 1% | 1.0 | 1 (11-13 16:10Z) |
| ap-southeast-3 | 531 | 24% | 3.1 | 1 (11-13 16:10Z) |
| us-east-1 | 531 | 10% | 2.6 | 4 (11-13 16:10Z) |
| us-east-2 | 531 | 30% | 3.6 | 1 (11-13 16:10Z) |
| us-west-2 | 531 | 9% | 2.1 | 2 (11-13 16:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999919191111299111919999199981991912191111111
ap-northeast-1   888195119119111221121111919991991121111151112112
ap-northeast-2   999999999999299999999999999999999999999191111111
ap-south-1       111169811111121112222212221131191111221111111111
ap-southeast-2   111111111111111711111111111111111111111111111111
ap-southeast-3   973138618111111111131111111111311111111131111111
us-east-1        111299991211233333223221322222232929332242323334
us-east-2        196999999119121119111111199991999911111111111111
us-west-2        111171112112221119111112292211121111121222111212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 8 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 168 | 5% | 1.5 | 1 (11-13 07:49Z) |
| ap-east-1 ape1-az2 | 390 | 66% | 6.6 | 1 (11-13 16:10Z) |
| ap-northeast-1 apne1-az1 | 123 | 10% | 1.9 | 2 (11-13 16:10Z) |
| ap-northeast-1 apne1-az4 | 242 | 26% | 3.5 | 1 (11-13 07:49Z) |
| ap-northeast-2 apne2-az1 | 454 | 63% | 6.6 | 1 (11-13 00:11Z) |
| ap-northeast-2 apne2-az3 | 490 | 69% | 7.0 | 1 (11-13 16:10Z) |
| ap-northeast-2 apne2-az4 | 520 | 70% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 155 | 1% | 1.3 | 1 (11-13 16:10Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 109 | 3% | 1.2 | 1 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 74 | 0% | 1.0 | 1 (11-12 10:55Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 323 | 37% | 4.3 | 1 (11-13 16:10Z) |
| us-east-1 use1-az1 | 111 | 0% | 1.1 | 1 (11-13 16:10Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 169 | 22% | 2.9 | 1 (11-13 16:10Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 128 | 24% | 3.0 | 1 (11-12 10:55Z) |
| us-east-2 use2-az1 | 230 | 42% | 4.6 | 1 (11-13 16:10Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 203 | 17% | 2.7 | 1 (11-13 07:49Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 531 | 71% | 7.3 | 9 (11-13 16:10Z) |
| ap-northeast-1 | 531 | 72% | 7.0 | 9 (11-13 16:10Z) |
| ap-northeast-2 | 531 | 100% | 9.0 | 9 (11-13 16:10Z) |
| ap-south-1 | 531 | 60% | 6.2 | 1 (11-13 16:10Z) |
| ap-southeast-2 | 531 | 26% | 3.6 | 9 (11-13 16:10Z) |
| ap-southeast-3 | 531 | 24% | 3.1 | 1 (11-13 16:10Z) |
| us-east-1 | 531 | 72% | 6.5 | 7 (11-13 16:10Z) |
| us-east-2 | 531 | 67% | 6.6 | 9 (11-13 16:10Z) |
| us-west-2 | 531 | 51% | 5.6 | 9 (11-13 16:10Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999929999921991992299999999999392299299289429
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999911911291192299219921791199139229111111911
ap-southeast-2   999199111119111919911999999991991191191199199119
ap-southeast-3   973138618111111111131111111111311111111131111111
us-east-1        999999994523469765557957999999999959966996896697
us-east-2        999999999199199129111911999999999911991991999999
us-west-2        999999449244543429494419595599999949433493343419
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 8 | 8 | 6 | 6 | 5 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 7 | 8 | 7 | 7 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 6 | 5 | 6 | 5 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 342 | 84% | 8.1 | 9 (11-13 16:10Z) |
| ap-east-1 ape1-az2 | 308 | 87% | 8.2 | 9 (11-13 16:10Z) |
| ap-east-1 ape1-az3 | 339 | 87% | 8.2 | 9 (11-13 07:49Z) |
| ap-northeast-1 apne1-az1 | 214 | 95% | 8.7 | 9 (11-13 16:10Z) |
| ap-northeast-1 apne1-az2 | 195 | 86% | 8.2 | 9 (11-12 18:50Z) |
| ap-northeast-1 apne1-az4 | 276 | 99% | 8.9 | 9 (11-13 16:10Z) |
| ap-northeast-2 apne2-az1 | 430 | 100% | 9.0 | 8 (11-13 07:49Z) |
| ap-northeast-2 apne2-az2 | 115 | 86% | 8.1 | 9 (11-12 18:50Z) |
| ap-northeast-2 apne2-az3 | 448 | 100% | 9.0 | 9 (11-13 16:10Z) |
| ap-northeast-2 apne2-az4 | 349 | 87% | 8.2 | 9 (11-13 16:10Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 28 | 50% | 5.4 | 1 (11-12 02:52Z) |
| us-east-1 use1-az2 | 113 | 99% | 8.9 | 4 (11-10 09:39Z) |
| us-east-1 use1-az4 | 152 | 91% | 8.4 | 9 (11-13 07:49Z) |
| us-east-1 use1-az5 | 108 | 98% | 8.9 | 9 (11-10 01:27Z) |
| us-east-1 use1-az6 | 134 | 93% | 8.5 | 9 (11-13 07:49Z) |
| us-east-2 use2-az1 | 187 | 99% | 8.9 | 9 (11-13 07:49Z) |
| us-east-2 use2-az2 | 208 | 99% | 8.9 | 9 (11-13 16:10Z) |
| us-east-2 use2-az3 | 233 | 97% | 8.7 | 9 (11-13 07:49Z) |
| us-west-2 usw2-az1 | 98 | 98% | 8.8 | 9 (11-13 16:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 138 | 88% | 8.1 | 9 (11-13 16:10Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707100 | 2026-11-13T16:10:59Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-13T16:10:59Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.707800 | 2026-11-13T16:10:59Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.581700 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.599000 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.582700 | 2026-11-13T16:10:59Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-13T16:10:59Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.620200 | 2026-11-13T16:10:59Z |
| ap-south-1 | ap-south-1a | Windows | 0.393500 | 2026-11-13T16:10:59Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.579600 | 2026-11-13T16:10:59Z |
| ap-south-1 | ap-south-1b | Windows | 0.374800 | 2026-11-13T16:10:59Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.604500 | 2026-11-13T16:10:59Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.488100 | 2026-11-13T16:10:59Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.583200 | 2026-11-13T16:10:59Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.536500 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.769300 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.738900 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.566300 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.549600 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509900 | 2026-11-13T16:10:59Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548600 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.554700 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549500 | 2026-11-13T16:10:59Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.618600 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2a | Windows | 0.330300 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.585900 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2b | Windows | 0.295900 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.606000 | 2026-11-13T16:10:59Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-13T16:10:59Z |
