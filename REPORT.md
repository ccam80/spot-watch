# Spot placement score log

Generated 2026-11-06 02:17 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 504 | 48% | 5.2 | 1 (11-06 02:17Z) |
| ap-northeast-1 | 504 | 15% | 2.7 | 1 (11-06 02:17Z) |
| ap-northeast-2 | 504 | 68% | 7.1 | 9 (11-06 02:17Z) |
| ap-south-1 | 504 | 3% | 1.7 | 2 (11-06 02:17Z) |
| ap-southeast-2 | 504 | 1% | 1.1 | 1 (11-06 02:17Z) |
| ap-southeast-3 | 504 | 25% | 3.2 | 1 (11-06 02:17Z) |
| us-east-1 | 504 | 10% | 2.6 | 3 (11-06 02:17Z) |
| us-east-2 | 504 | 30% | 3.6 | 1 (11-06 02:17Z) |
| us-west-2 | 504 | 9% | 2.1 | 1 (11-06 02:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111119991111199999999911199999999919191111299111
ap-northeast-1   112421114421111121187911147888195119119111221121
ap-northeast-2   999999999911999999999919999999999999999299999999
ap-south-1       111111111111111111111111111111169811111121112222
ap-southeast-2   111111111111111111111111111111111111111111711111
ap-southeast-3   111111111111111155125411183973138618111111111131
us-east-1        221112222222222222122111111111299991211233333223
us-east-2        111111111111119911121119991196999999119121119111
us-west-2        111111111111111119413111111111171112112221119111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 5 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | 7 | 5 | 7 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 2 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 160 | 6% | 1.6 | 1 (11-05 15:23Z) |
| ap-east-1 ape1-az2 | 370 | 66% | 6.6 | 9 (11-05 06:32Z) |
| ap-northeast-1 apne1-az1 | 110 | 8% | 1.7 | 1 (11-06 02:17Z) |
| ap-northeast-1 apne1-az4 | 225 | 26% | 3.5 | 1 (11-05 06:32Z) |
| ap-northeast-2 apne2-az1 | 433 | 62% | 6.6 | 9 (11-06 02:17Z) |
| ap-northeast-2 apne2-az3 | 469 | 68% | 7.0 | 8 (11-06 02:17Z) |
| ap-northeast-2 apne2-az4 | 497 | 69% | 7.1 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az1 | 145 | 1% | 1.3 | 1 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 138 | 7% | 2.4 | 1 (11-04 09:01Z) |
| ap-southeast-2 apse2-az1 | 99 | 3% | 1.3 | 1 (11-06 02:17Z) |
| ap-southeast-2 apse2-az2 | 67 | 0% | 1.0 | 1 (11-06 02:17Z) |
| ap-southeast-3 apse3-az1 | 88 | 0% | 1.0 | 1 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 313 | 39% | 4.4 | 1 (11-06 02:17Z) |
| us-east-1 use1-az1 | 105 | 0% | 1.1 | 1 (11-05 21:55Z) |
| us-east-1 use1-az2 | 139 | 3% | 1.4 | 1 (11-05 21:55Z) |
| us-east-1 use1-az4 | 165 | 23% | 3.0 | 1 (11-05 21:55Z) |
| us-east-1 use1-az5 | 161 | 25% | 3.2 | 1 (11-05 06:32Z) |
| us-east-1 use1-az6 | 122 | 25% | 3.1 | 1 (11-03 20:55Z) |
| us-east-2 use2-az1 | 217 | 42% | 4.5 | 1 (11-05 21:55Z) |
| us-east-2 use2-az2 | 257 | 50% | 5.3 | 1 (11-05 15:23Z) |
| us-east-2 use2-az3 | 283 | 47% | 5.1 | 1 (11-06 02:17Z) |
| us-west-2 usw2-az1 | 157 | 24% | 3.2 | 1 (11-04 09:01Z) |
| us-west-2 usw2-az2 | 121 | 17% | 2.6 | 1 (11-06 02:17Z) |
| us-west-2 usw2-az3 | 199 | 17% | 2.7 | 1 (11-05 21:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 504 | 70% | 7.2 | 9 (11-06 02:17Z) |
| ap-northeast-1 | 504 | 72% | 7.0 | 2 (11-06 02:17Z) |
| ap-northeast-2 | 504 | 100% | 9.0 | 9 (11-06 02:17Z) |
| ap-south-1 | 504 | 62% | 6.3 | 9 (11-06 02:17Z) |
| ap-southeast-2 | 504 | 24% | 3.4 | 1 (11-06 02:17Z) |
| ap-southeast-3 | 504 | 25% | 3.2 | 1 (11-06 02:17Z) |
| us-east-1 | 504 | 70% | 6.4 | 7 (11-06 02:17Z) |
| us-east-2 | 504 | 67% | 6.6 | 1 (11-06 02:17Z) |
| us-west-2 | 504 | 51% | 5.6 | 4 (11-06 02:17Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999999999999999999999999999929999921991992
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999799999999999999999999911911291192299
ap-southeast-2   111119999999111319999999999999199111119111919911
ap-southeast-3   111111111111111155125411183973138618111111111131
us-east-1        334339394399999999999322999999999994523469765557
us-east-2        222222228999999999999929991999999999199199129111
us-west-2        395931211233244999549992999999999449244543429494
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 5 | 6 | 6 | 7 | 8 | 7 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 6 | 4 | 5 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 4 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 5 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 326 | 83% | 8.0 | 9 (11-06 02:17Z) |
| ap-east-1 ape1-az2 | 285 | 86% | 8.1 | 9 (11-06 02:17Z) |
| ap-east-1 ape1-az3 | 314 | 86% | 8.2 | 9 (11-06 02:17Z) |
| ap-northeast-1 apne1-az1 | 209 | 95% | 8.7 | 9 (11-05 21:55Z) |
| ap-northeast-1 apne1-az2 | 184 | 85% | 8.1 | 9 (11-05 21:55Z) |
| ap-northeast-1 apne1-az4 | 267 | 99% | 8.9 | 9 (11-05 15:23Z) |
| ap-northeast-2 apne2-az1 | 413 | 100% | 9.0 | 9 (11-06 02:17Z) |
| ap-northeast-2 apne2-az2 | 107 | 85% | 8.0 | 9 (11-05 21:55Z) |
| ap-northeast-2 apne2-az3 | 431 | 100% | 9.0 | 9 (11-06 02:17Z) |
| ap-northeast-2 apne2-az4 | 328 | 86% | 8.1 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az1 | 175 | 87% | 8.2 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az2 | 186 | 80% | 7.8 | 9 (11-06 02:17Z) |
| ap-south-1 aps1-az3 | 196 | 90% | 8.4 | 9 (11-06 02:17Z) |
| ap-southeast-2 apse2-az1 | 63 | 84% | 8.0 | 9 (11-05 15:23Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 73 | 82% | 7.9 | 9 (11-05 15:23Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 104 | 98% | 8.9 | 9 (11-04 09:01Z) |
| us-east-1 use1-az6 | 125 | 92% | 8.4 | 9 (11-04 09:01Z) |
| us-east-2 use2-az1 | 177 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az2 | 194 | 99% | 8.9 | 9 (11-05 06:32Z) |
| us-east-2 use2-az3 | 223 | 96% | 8.7 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 89 | 90% | 8.3 | 9 (11-05 06:32Z) |
| us-west-2 usw2-az3 | 130 | 88% | 8.1 | 2 (11-06 02:17Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.718200 | 2026-11-06T02:17:10Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-06T02:17:10Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.734200 | 2026-11-06T02:17:10Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.580800 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.593700 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.573200 | 2026-11-06T02:17:10Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-06T02:17:10Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.600200 | 2026-11-06T02:17:10Z |
| ap-south-1 | ap-south-1a | Windows | 0.434100 | 2026-11-06T02:17:10Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.553300 | 2026-11-06T02:17:10Z |
| ap-south-1 | ap-south-1b | Windows | 0.357600 | 2026-11-06T02:17:10Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.576700 | 2026-11-06T02:17:10Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501800 | 2026-11-06T02:17:10Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.735100 | 2026-11-06T02:17:10Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.554600 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.543900 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.507300 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.485300 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.438500 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.526800 | 2026-11-06T02:17:10Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.549900 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2a | Windows | 0.638000 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.551300 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2b | Windows | 0.636900 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.547800 | 2026-11-06T02:17:10Z |
| us-east-2 | us-east-2c | Windows | 0.637000 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.557100 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2a | Windows | 0.303500 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.688400 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2b | Windows | 0.318100 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.594900 | 2026-11-06T02:17:10Z |
| us-west-2 | us-west-2c | Windows | 0.303800 | 2026-11-06T02:17:10Z |
