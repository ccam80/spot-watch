# Spot placement score log

Generated 2026-11-13 22:31 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 532 | 48% | 5.2 | 1 (11-13 22:31Z) |
| ap-northeast-1 | 532 | 16% | 2.7 | 9 (11-13 22:31Z) |
| ap-northeast-2 | 532 | 68% | 7.0 | 1 (11-13 22:31Z) |
| ap-south-1 | 532 | 3% | 1.7 | 1 (11-13 22:31Z) |
| ap-southeast-2 | 532 | 1% | 1.0 | 1 (11-13 22:31Z) |
| ap-southeast-3 | 532 | 24% | 3.1 | 1 (11-13 22:31Z) |
| us-east-1 | 532 | 10% | 2.6 | 4 (11-13 22:31Z) |
| us-east-2 | 532 | 30% | 3.6 | 1 (11-13 22:31Z) |
| us-west-2 | 532 | 9% | 2.1 | 2 (11-13 22:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999191911112991119199991999819919121911111111
ap-northeast-1   881951191191112211211119199919911211111511121129
ap-northeast-2   999999999992999999999999999999999999991911111111
ap-south-1       111698111111211122222122211311911112211111111111
ap-southeast-2   111111111111117111111111111111111111111111111111
ap-southeast-3   731386181111111111311111111113111111111311111111
us-east-1        112999912112333332232213222222329293322423233344
us-east-2        969999991191211191111111999919999111111111111111
us-west-2        111711121122211191111122922111211111212221112122
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
| ap-northeast-1 apne1-az1 | 124 | 10% | 1.9 | 2 (11-13 22:31Z) |
| ap-northeast-1 apne1-az4 | 243 | 26% | 3.5 | 9 (11-13 22:31Z) |
| ap-northeast-2 apne2-az1 | 455 | 63% | 6.6 | 1 (11-13 22:31Z) |
| ap-northeast-2 apne2-az3 | 491 | 69% | 7.0 | 1 (11-13 22:31Z) |
| ap-northeast-2 apne2-az4 | 520 | 70% | 7.1 | 1 (11-13 00:11Z) |
| ap-south-1 aps1-az1 | 155 | 1% | 1.3 | 1 (11-13 16:10Z) |
| ap-south-1 aps1-az3 | 154 | 6% | 2.3 | 1 (11-13 07:49Z) |
| ap-southeast-2 apse2-az1 | 109 | 3% | 1.2 | 1 (11-13 16:10Z) |
| ap-southeast-2 apse2-az2 | 75 | 0% | 1.0 | 1 (11-13 22:31Z) |
| ap-southeast-3 apse3-az1 | 93 | 0% | 1.0 | 1 (11-13 00:11Z) |
| ap-southeast-3 apse3-az3 | 323 | 37% | 4.3 | 1 (11-13 16:10Z) |
| us-east-1 use1-az1 | 112 | 0% | 1.1 | 1 (11-13 22:31Z) |
| us-east-1 use1-az2 | 140 | 3% | 1.4 | 1 (11-13 07:49Z) |
| us-east-1 use1-az4 | 170 | 22% | 2.9 | 1 (11-13 22:31Z) |
| us-east-1 use1-az5 | 172 | 24% | 3.1 | 1 (11-13 07:49Z) |
| us-east-1 use1-az6 | 129 | 24% | 3.0 | 1 (11-13 22:31Z) |
| us-east-2 use2-az1 | 231 | 42% | 4.5 | 1 (11-13 22:31Z) |
| us-east-2 use2-az2 | 268 | 51% | 5.3 | 1 (11-12 02:52Z) |
| us-east-2 use2-az3 | 300 | 47% | 5.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az1 | 169 | 22% | 3.0 | 1 (11-13 00:11Z) |
| us-west-2 usw2-az2 | 125 | 17% | 2.5 | 1 (11-13 16:10Z) |
| us-west-2 usw2-az3 | 204 | 17% | 2.7 | 1 (11-13 22:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 532 | 71% | 7.3 | 9 (11-13 22:31Z) |
| ap-northeast-1 | 532 | 72% | 7.0 | 9 (11-13 22:31Z) |
| ap-northeast-2 | 532 | 100% | 9.0 | 9 (11-13 22:31Z) |
| ap-south-1 | 532 | 60% | 6.2 | 1 (11-13 22:31Z) |
| ap-southeast-2 | 532 | 26% | 3.6 | 1 (11-13 22:31Z) |
| ap-southeast-3 | 532 | 24% | 3.1 | 1 (11-13 22:31Z) |
| us-east-1 | 532 | 72% | 6.5 | 8 (11-13 22:31Z) |
| us-east-2 | 532 | 67% | 6.6 | 9 (11-13 22:31Z) |
| us-west-2 | 532 | 51% | 5.6 | 4 (11-13 22:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999299999219919922999999999993922992992894299
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999119112911922992199217911991392291111119111
ap-southeast-2   991991111191119199119999999919911911911991991191
ap-southeast-3   731386181111111111311111111113111111111311111111
us-east-1        999999945234697655579579999999999599669968966978
us-east-2        999999991991991291119119999999999119919919999999
us-west-2        999994492445434294944195955999999494334933434194
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
| ap-east-1 ape1-az1 | 343 | 84% | 8.1 | 9 (11-13 22:31Z) |
| ap-east-1 ape1-az2 | 309 | 87% | 8.2 | 9 (11-13 22:31Z) |
| ap-east-1 ape1-az3 | 340 | 87% | 8.2 | 9 (11-13 22:31Z) |
| ap-northeast-1 apne1-az1 | 214 | 95% | 8.7 | 9 (11-13 16:10Z) |
| ap-northeast-1 apne1-az2 | 196 | 86% | 8.2 | 9 (11-13 22:31Z) |
| ap-northeast-1 apne1-az4 | 276 | 99% | 8.9 | 9 (11-13 16:10Z) |
| ap-northeast-2 apne2-az1 | 431 | 100% | 9.0 | 9 (11-13 22:31Z) |
| ap-northeast-2 apne2-az2 | 116 | 86% | 8.1 | 9 (11-13 22:31Z) |
| ap-northeast-2 apne2-az3 | 449 | 100% | 9.0 | 9 (11-13 22:31Z) |
| ap-northeast-2 apne2-az4 | 350 | 87% | 8.2 | 9 (11-13 22:31Z) |
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
| us-east-2 use2-az1 | 188 | 99% | 8.9 | 9 (11-13 22:31Z) |
| us-east-2 use2-az2 | 208 | 99% | 8.9 | 9 (11-13 16:10Z) |
| us-east-2 use2-az3 | 234 | 97% | 8.7 | 9 (11-13 22:31Z) |
| us-west-2 usw2-az1 | 98 | 98% | 8.8 | 9 (11-13 16:10Z) |
| us-west-2 usw2-az2 | 97 | 91% | 8.3 | 9 (11-11 14:05Z) |
| us-west-2 usw2-az3 | 138 | 88% | 8.1 | 9 (11-13 16:10Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.707100 | 2026-11-13T22:31:32Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-13T22:31:32Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.708600 | 2026-11-13T22:31:32Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.584200 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.604000 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.583400 | 2026-11-13T22:31:32Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-13T22:31:32Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.620200 | 2026-11-13T22:31:32Z |
| ap-south-1 | ap-south-1a | Windows | 0.393200 | 2026-11-13T22:31:32Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.593100 | 2026-11-13T22:31:32Z |
| ap-south-1 | ap-south-1b | Windows | 0.374800 | 2026-11-13T22:31:32Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.621600 | 2026-11-13T22:31:32Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.490400 | 2026-11-13T22:31:32Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.573400 | 2026-11-13T22:31:32Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.540900 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.793600 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.754100 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.566700 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.555500 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.509000 | 2026-11-13T22:31:32Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.548600 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2a | Windows | 0.636700 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.567000 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2b | Windows | 0.636700 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549100 | 2026-11-13T22:31:32Z |
| us-east-2 | us-east-2c | Windows | 0.636700 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.619700 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2a | Windows | 0.333100 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.579900 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2b | Windows | 0.295000 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.597700 | 2026-11-13T22:31:32Z |
| us-west-2 | us-west-2c | Windows | 0.284600 | 2026-11-13T22:31:32Z |
