# Spot placement score log

Generated 2026-11-15 01:47 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 537 | 48% | 5.2 | 9 (11-15 01:47Z) |
| ap-northeast-1 | 537 | 17% | 2.8 | 9 (11-15 01:47Z) |
| ap-northeast-2 | 537 | 68% | 7.0 | 9 (11-15 01:47Z) |
| ap-south-1 | 537 | 3% | 1.7 | 9 (11-15 01:47Z) |
| ap-southeast-2 | 537 | 1% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 | 537 | 24% | 3.1 | 1 (11-15 01:47Z) |
| us-east-1 | 537 | 10% | 2.6 | 2 (11-15 01:47Z) |
| us-east-2 | 537 | 30% | 3.6 | 1 (11-15 01:47Z) |
| us-west-2 | 537 | 9% | 2.1 | 1 (11-15 01:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        919191111299111919999199981991912191111111119919
ap-northeast-1   119119111221121111919991991121111151112112999599
ap-northeast-2   999999299999999999999999999999999191111111119999
ap-south-1       811111121112222212221131191111221111111111111119
ap-southeast-2   111111111711111111111111111111111111111111111111
ap-southeast-3   618111111111131111111111311111111131111111111121
us-east-1        991211233333223221322222232929332242323334422332
us-east-2        999119121119111111199991999911111111111111111991
us-west-2        112112221119111112292211121111121222111212211121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 3 | 5 | 5 |
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
| ap-east-1 ape1-az2 | 393 | 66% | 6.6 | 9 (11-15 01:47Z) |
| ap-northeast-1 apne1-az1 | 127 | 10% | 1.9 | 9 (11-15 01:47Z) |
| ap-northeast-1 apne1-az4 | 248 | 27% | 3.5 | 9 (11-15 01:47Z) |
| ap-northeast-2 apne2-az1 | 458 | 63% | 6.6 | 9 (11-15 01:47Z) |
| ap-northeast-2 apne2-az3 | 496 | 69% | 7.0 | 9 (11-15 01:47Z) |
| ap-northeast-2 apne2-az4 | 524 | 70% | 7.2 | 9 (11-15 01:47Z) |
| ap-south-1 aps1-az1 | 157 | 1% | 1.4 | 3 (11-15 01:47Z) |
| ap-south-1 aps1-az3 | 155 | 7% | 2.3 | 7 (11-15 01:47Z) |
| ap-southeast-2 apse2-az1 | 110 | 3% | 1.2 | 1 (11-14 03:05Z) |
| ap-southeast-2 apse2-az2 | 79 | 0% | 1.0 | 1 (11-15 01:47Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 327 | 37% | 4.3 | 2 (11-14 21:23Z) |
| us-east-1 use1-az1 | 114 | 0% | 1.1 | 1 (11-15 01:47Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 170 | 22% | 2.9 | 1 (11-13 22:31Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 132 | 23% | 3.0 | 1 (11-14 16:59Z) |
| us-east-2 use2-az1 | 235 | 42% | 4.5 | 9 (11-14 21:23Z) |
| us-east-2 use2-az2 | 272 | 51% | 5.3 | 9 (11-14 21:23Z) |
| us-east-2 use2-az3 | 302 | 47% | 5.1 | 9 (11-14 21:23Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 204 | 17% | 2.7 | 1 (11-13 22:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 537 | 72% | 7.3 | 9 (11-15 01:47Z) |
| ap-northeast-1 | 537 | 72% | 7.0 | 9 (11-15 01:47Z) |
| ap-northeast-2 | 537 | 100% | 9.0 | 9 (11-15 01:47Z) |
| ap-south-1 | 537 | 60% | 6.1 | 9 (11-15 01:47Z) |
| ap-southeast-2 | 537 | 26% | 3.6 | 9 (11-15 01:47Z) |
| ap-southeast-3 | 537 | 24% | 3.1 | 1 (11-15 01:47Z) |
| us-east-1 | 537 | 72% | 6.5 | 9 (11-15 01:47Z) |
| us-east-2 | 537 | 68% | 6.7 | 9 (11-15 01:47Z) |
| us-west-2 | 537 | 51% | 5.6 | 3 (11-15 01:47Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   929999921991992299999999999392299299289429999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       911911291192299219921791199139229111111911111199
ap-southeast-2   111119111919911999999991991191191199199119132999
ap-southeast-3   618111111111131111111111311111111131111111111121
us-east-1        994523469765557957999999999959966996896697899999
us-east-2        999199199129111911999999999911991991999999999999
us-west-2        449244543429494419595599999949433493343419423993
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
| us-east-2 | 7 | 6 | 6 | 8 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 6 | 5 | 6 | 7 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 6 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 344 | 84% | 8.1 | 9 (11-14 03:05Z) |
| ap-east-1 ape1-az2 | 311 | 87% | 8.2 | 9 (11-14 21:23Z) |
| ap-east-1 ape1-az3 | 343 | 87% | 8.2 | 9 (11-15 01:47Z) |
| ap-northeast-1 apne1-az1 | 216 | 95% | 8.7 | 9 (11-14 16:59Z) |
| ap-northeast-1 apne1-az2 | 199 | 86% | 8.2 | 9 (11-15 01:47Z) |
| ap-northeast-1 apne1-az4 | 277 | 99% | 8.9 | 9 (11-14 03:05Z) |
| ap-northeast-2 apne2-az1 | 435 | 100% | 9.0 | 9 (11-15 01:47Z) |
| ap-northeast-2 apne2-az2 | 118 | 86% | 8.1 | 9 (11-14 16:59Z) |
| ap-northeast-2 apne2-az3 | 451 | 100% | 9.0 | 9 (11-15 01:47Z) |
| ap-northeast-2 apne2-az4 | 353 | 87% | 8.2 | 9 (11-15 01:47Z) |
| ap-south-1 aps1-az1 | 179 | 88% | 8.3 | 9 (11-13 00:11Z) |
| ap-south-1 aps1-az2 | 187 | 80% | 7.8 | 9 (11-10 23:11Z) |
| ap-south-1 aps1-az3 | 201 | 90% | 8.4 | 9 (11-14 21:23Z) |
| ap-southeast-2 apse2-az1 | 72 | 86% | 8.1 | 9 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 85 | 84% | 8.0 | 9 (11-15 01:47Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 30 | 53% | 5.6 | 9 (11-14 16:59Z) |
| us-east-1 use1-az2 | 116 | 99% | 8.9 | 9 (11-15 01:47Z) |
| us-east-1 use1-az4 | 155 | 92% | 8.4 | 9 (11-15 01:47Z) |
| us-east-1 use1-az5 | 111 | 98% | 8.9 | 9 (11-14 21:23Z) |
| us-east-1 use1-az6 | 136 | 93% | 8.5 | 9 (11-15 01:47Z) |
| us-east-2 use2-az1 | 190 | 99% | 8.9 | 9 (11-14 21:23Z) |
| us-east-2 use2-az2 | 210 | 99% | 8.9 | 9 (11-14 10:14Z) |
| us-east-2 use2-az3 | 237 | 97% | 8.8 | 9 (11-15 01:47Z) |
| us-west-2 usw2-az1 | 100 | 98% | 8.8 | 9 (11-14 21:23Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 140 | 88% | 8.2 | 9 (11-14 21:23Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.706900 | 2026-11-15T01:47:53Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-15T01:47:53Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.710500 | 2026-11-15T01:47:53Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.596100 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.612400 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.594600 | 2026-11-15T01:47:53Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-15T01:47:53Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.662800 | 2026-11-15T01:47:53Z |
| ap-south-1 | ap-south-1a | Windows | 0.385700 | 2026-11-15T01:47:53Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.618800 | 2026-11-15T01:47:53Z |
| ap-south-1 | ap-south-1b | Windows | 0.379300 | 2026-11-15T01:47:53Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.641700 | 2026-11-15T01:47:53Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.504700 | 2026-11-15T01:47:53Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.544000 | 2026-11-15T01:47:53Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.542300 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.854600 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.806800 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.569800 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.578200 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.508700 | 2026-11-15T01:47:53Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548000 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.585400 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549400 | 2026-11-15T01:47:53Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.653300 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2a | Windows | 0.329400 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.565100 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2b | Windows | 0.288000 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.593700 | 2026-11-15T01:47:53Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-15T01:47:53Z |
