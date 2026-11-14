# Spot placement score log

Generated 2026-11-14 10:14 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 534 | 48% | 5.2 | 9 (11-14 10:14Z) |
| ap-northeast-1 | 534 | 16% | 2.7 | 9 (11-14 10:14Z) |
| ap-northeast-2 | 534 | 68% | 7.0 | 9 (11-14 10:14Z) |
| ap-south-1 | 534 | 3% | 1.7 | 1 (11-14 10:14Z) |
| ap-southeast-2 | 534 | 1% | 1.0 | 1 (11-14 10:14Z) |
| ap-southeast-3 | 534 | 24% | 3.1 | 1 (11-14 10:14Z) |
| us-east-1 | 534 | 10% | 2.6 | 2 (11-14 10:14Z) |
| us-east-2 | 534 | 30% | 3.6 | 1 (11-14 10:14Z) |
| us-west-2 | 534 | 9% | 2.1 | 1 (11-14 10:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999919191111299111919999199981991912191111111119
ap-northeast-1   195119119111221121111919991991121111151112112999
ap-northeast-2   999999999299999999999999999999999999191111111119
ap-south-1       169811111121112222212221131191111221111111111111
ap-southeast-2   111111111111711111111111111111111111111111111111
ap-southeast-3   138618111111111131111111111311111111131111111111
us-east-1        299991211233333223221322222232929332242323334422
us-east-2        999999119121119111111199991999911111111111111111
us-west-2        171112112221119111112292211121111121222111212211
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 8 | 7 | 6 | 6 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 6 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 168 | 5% | 1.5 | 1 (11-13 07:49Z) |
| ap-east-1 ape1-az2 | 391 | 66% | 6.6 | 9 (11-14 10:14Z) |
| ap-northeast-1 apne1-az1 | 126 | 10% | 1.9 | 1 (11-14 10:14Z) |
| ap-northeast-1 apne1-az4 | 245 | 27% | 3.5 | 8 (11-14 10:14Z) |
| ap-northeast-2 apne2-az1 | 455 | 63% | 6.6 | 1 (11-13 22:31Z) |
| ap-northeast-2 apne2-az3 | 493 | 69% | 7.0 | 9 (11-14 10:14Z) |
| ap-northeast-2 apne2-az4 | 521 | 70% | 7.1 | 9 (11-14 10:14Z) |
| ap-south-1 aps1-az1 | 156 | 1% | 1.3 | 1 (11-14 03:05Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 110 | 3% | 1.2 | 1 (11-14 03:05Z) |
| ap-southeast-2 apse2-az2 | 77 | 0% | 1.0 | 1 (11-14 10:14Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 325 | 37% | 4.3 | 1 (11-14 10:14Z) |
| us-east-1 use1-az1 | 112 | 0% | 1.1 | 1 (11-13 22:31Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 170 | 22% | 2.9 | 1 (11-13 22:31Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 131 | 24% | 3.0 | 1 (11-14 10:14Z) |
| us-east-2 use2-az1 | 233 | 42% | 4.5 | 1 (11-14 10:14Z) |
| us-east-2 use2-az2 | 270 | 50% | 5.3 | 1 (11-14 10:14Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 204 | 17% | 2.7 | 1 (11-13 22:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 534 | 71% | 7.3 | 9 (11-14 10:14Z) |
| ap-northeast-1 | 534 | 72% | 7.0 | 9 (11-14 10:14Z) |
| ap-northeast-2 | 534 | 100% | 9.0 | 9 (11-14 10:14Z) |
| ap-south-1 | 534 | 60% | 6.1 | 1 (11-14 10:14Z) |
| ap-southeast-2 | 534 | 26% | 3.6 | 2 (11-14 10:14Z) |
| ap-southeast-3 | 534 | 24% | 3.1 | 1 (11-14 10:14Z) |
| us-east-1 | 534 | 72% | 6.5 | 9 (11-14 10:14Z) |
| us-east-2 | 534 | 68% | 6.7 | 9 (11-14 10:14Z) |
| us-west-2 | 534 | 51% | 5.6 | 3 (11-14 10:14Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999929999921991992299999999999392299299289429999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999911911291192299219921791199139229111111911111
ap-southeast-2   199111119111919911999999991991191191199199119132
ap-southeast-3   138618111111111131111111111311111111131111111111
us-east-1        999994523469765557957999999999959966996896697899
us-east-2        999999199199129111911999999999911991991999999999
us-west-2        999449244543429494419595599999949433493343419423
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
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 344 | 84% | 8.1 | 9 (11-14 03:05Z) |
| ap-east-1 ape1-az2 | 310 | 87% | 8.2 | 9 (11-14 10:14Z) |
| ap-east-1 ape1-az3 | 341 | 87% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az1 | 215 | 95% | 8.7 | 9 (11-14 10:14Z) |
| ap-northeast-1 apne1-az2 | 197 | 86% | 8.2 | 9 (11-14 03:05Z) |
| ap-northeast-1 apne1-az4 | 277 | 99% | 8.9 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az1 | 433 | 100% | 9.0 | 9 (11-14 10:14Z) |
| ap-northeast-2 apne2-az2 | 117 | 86% | 8.1 | 9 (11-14 10:14Z) |
| ap-northeast-2 apne2-az3 | 450 | 100% | 9.0 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az4 | 351 | 87% | 8.2 | 9 (11-14 03:05Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 200 | 90% | 8.4 | 9 (11-13 00:11Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 83 | 83% | 7.9 | 9 (11-12 18:50Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 29 | 52% | 5.5 | 9 (11-14 10:14Z) |
| us-east-1 use1-az2 | 114 | 99% | 8.9 | 9 (11-14 10:14Z) |
| us-east-1 use1-az4 | 153 | 92% | 8.4 | 9 (11-14 10:14Z) |
| us-east-1 use1-az5 | 109 | 98% | 8.9 | 9 (11-14 10:14Z) |
| us-east-1 use1-az6 | 134 | 93% | 8.5 | 9 (11-13 07:49Z) |
| us-east-2 use2-az1 | 189 | 99% | 8.9 | 9 (11-14 03:05Z) |
| us-east-2 use2-az2 | 210 | 99% | 8.9 | 9 (11-14 10:14Z) |
| us-east-2 use2-az3 | 236 | 97% | 8.8 | 9 (11-14 10:14Z) |
| us-west-2 usw2-az1 | 98 | 98% | 8.8 | 9 (11-13 16:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 138 | 88% | 8.1 | 9 (11-13 16:10Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707000 | 2026-11-14T10:14:49Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-14T10:14:49Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.708900 | 2026-11-14T10:14:49Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.590500 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.608900 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.590800 | 2026-11-14T10:14:49Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-14T10:14:49Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.641400 | 2026-11-14T10:14:49Z |
| ap-south-1 | ap-south-1a | Windows | 0.386700 | 2026-11-14T10:14:49Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.601800 | 2026-11-14T10:14:49Z |
| ap-south-1 | ap-south-1b | Windows | 0.379300 | 2026-11-14T10:14:49Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.630300 | 2026-11-14T10:14:49Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.492300 | 2026-11-14T10:14:49Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.554200 | 2026-11-14T10:14:49Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.805400 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.758300 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.568100 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.570600 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509000 | 2026-11-14T10:14:49Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548100 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.567900 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549000 | 2026-11-14T10:14:49Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.632900 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2a | Windows | 0.333600 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.570400 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2b | Windows | 0.290700 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.593700 | 2026-11-14T10:14:49Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-14T10:14:49Z |
