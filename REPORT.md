# Spot placement score log

Generated 2026-11-02 23:26 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 493 | 49% | 5.2 | 1 (11-02 23:26Z) |
| ap-northeast-1 | 493 | 16% | 2.7 | 1 (11-02 23:26Z) |
| ap-northeast-2 | 493 | 68% | 7.0 | 9 (11-02 23:26Z) |
| ap-south-1 | 493 | 3% | 1.7 | 1 (11-02 23:26Z) |
| ap-southeast-2 | 493 | 0% | 1.0 | 1 (11-02 23:26Z) |
| ap-southeast-3 | 493 | 26% | 3.3 | 1 (11-02 23:26Z) |
| us-east-1 | 493 | 11% | 2.6 | 2 (11-02 23:26Z) |
| us-east-2 | 493 | 30% | 3.7 | 1 (11-02 23:26Z) |
| us-west-2 | 493 | 9% | 2.1 | 1 (11-02 23:26Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999911111199911111999999999111999999999191
ap-northeast-1   111222287111124211144211111211879111478881951191
ap-northeast-2   999999999999999999999119999999999199999999999999
ap-south-1       111122111121111111111111111111111111111111698111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111117867511111111111111111551254111839731386181
us-east-1        323322222222211122222222222221221111111112999912
us-east-2        129111111111111111111111199111211199911969999991
us-west-2        221111111111111111111111111194131111111111711121
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 6 | 6 | 6 | 5 | 5 | 5 | 7 | 5 | 6 | 7 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 3 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 6 | 8 | 9 | 8 | 6 | 7 | 6 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 3 | 3 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 3 | 4 | 3 | 3 | 2 | 5 | 5 | 7 | 4 | 5 | 7 | 4 | 5 | 3 | 2 | 2 | 2 | 4 | 3 | 4 | 3 | 3 | 3 | 4 |
| us-west-2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 156 | 6% | 1.6 | 2 (11-02 15:37Z) |
| ap-east-1 ape1-az2 | 365 | 66% | 6.6 | 1 (11-02 23:26Z) |
| ap-northeast-1 apne1-az1 | 108 | 8% | 1.7 | 1 (11-02 23:26Z) |
| ap-northeast-1 apne1-az4 | 221 | 26% | 3.5 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az1 | 423 | 62% | 6.5 | 9 (11-02 23:26Z) |
| ap-northeast-2 apne2-az3 | 460 | 68% | 7.0 | 9 (11-02 23:26Z) |
| ap-northeast-2 apne2-az4 | 486 | 69% | 7.1 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az1 | 139 | 1% | 1.3 | 1 (10-31 17:11Z) |
| ap-south-1 aps1-az3 | 134 | 7% | 2.4 | 8 (11-01 23:31Z) |
| ap-southeast-2 apse2-az1 | 94 | 2% | 1.2 | 1 (11-02 23:26Z) |
| ap-southeast-2 apse2-az2 | 62 | 0% | 1.0 | 1 (11-02 23:26Z) |
| ap-southeast-3 apse3-az1 | 87 | 0% | 1.0 | 1 (10-31 18:15Z) |
| ap-southeast-3 apse3-az3 | 310 | 39% | 4.4 | 1 (11-02 23:26Z) |
| us-east-1 use1-az1 | 102 | 0% | 1.1 | 1 (11-02 23:26Z) |
| us-east-1 use1-az2 | 134 | 3% | 1.4 | 9 (11-01 14:59Z) |
| us-east-1 use1-az4 | 161 | 24% | 3.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 158 | 26% | 3.2 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 121 | 25% | 3.1 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 211 | 43% | 4.6 | 9 (11-02 15:37Z) |
| us-east-2 use2-az2 | 253 | 50% | 5.3 | 9 (11-02 15:37Z) |
| us-east-2 use2-az3 | 280 | 47% | 5.1 | 9 (11-02 15:37Z) |
| us-west-2 usw2-az1 | 153 | 24% | 3.2 | 1 (11-02 05:51Z) |
| us-west-2 usw2-az2 | 119 | 18% | 2.6 | 1 (11-02 23:26Z) |
| us-west-2 usw2-az3 | 193 | 17% | 2.7 | 1 (10-31 17:11Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 493 | 69% | 7.1 | 9 (11-02 23:26Z) |
| ap-northeast-1 | 493 | 72% | 7.0 | 9 (11-02 23:26Z) |
| ap-northeast-2 | 493 | 100% | 9.0 | 9 (11-02 23:26Z) |
| ap-south-1 | 493 | 62% | 6.3 | 9 (11-02 23:26Z) |
| ap-southeast-2 | 493 | 24% | 3.4 | 1 (11-02 23:26Z) |
| ap-southeast-3 | 493 | 26% | 3.3 | 1 (11-02 23:26Z) |
| us-east-1 | 493 | 70% | 6.4 | 5 (11-02 23:26Z) |
| us-east-2 | 493 | 67% | 6.7 | 1 (11-02 23:26Z) |
| us-west-2 | 493 | 52% | 5.7 | 2 (11-02 23:26Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   113399999999999999999999999999999999999999999299
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111122111129999999999997999999999999999999999119
ap-southeast-2   111111111111111199999991113199999999999991991111
ap-southeast-3   111117867511111111111111111551254111839731386181
us-east-1        999999323233343393943999999999993229999999999945
us-east-2        999932222222222222289999999999999299919999999991
us-west-2        559999948443959312112332449995499929999999994492
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 6 | 8 | 9 | 8 | 6 | 7 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 7 | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 |
| ap-northeast-1 | 7 | 4 | 2 | 3 | 4 | 5 | 4 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 7 | 6 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 8 |
| ap-southeast-2 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 6 | 4 | 5 | 4 | 4 | 6 | 5 | 3 | 3 | 3 | 2 |
| ap-southeast-3 | 3 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 5 |
| us-east-1 | 7 | 7 | 6 | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| us-east-2 | 6 | 6 | 6 | 7 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 5 | 5 | 6 | 6 | 6 | 5 | 5 | 5 | 6 |
| us-west-2 | 5 | 5 | 4 | 4 | 5 | 6 | 8 | 6 | 6 | 5 | 7 | 7 | 8 | 7 | 7 | 7 | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 316 | 83% | 8.0 | 9 (11-02 23:26Z) |
| ap-east-1 ape1-az2 | 274 | 85% | 8.1 | 9 (11-02 05:51Z) |
| ap-east-1 ape1-az3 | 303 | 85% | 8.1 | 9 (11-02 23:26Z) |
| ap-northeast-1 apne1-az1 | 205 | 95% | 8.7 | 9 (11-01 07:25Z) |
| ap-northeast-1 apne1-az2 | 177 | 85% | 8.1 | 9 (11-02 23:26Z) |
| ap-northeast-1 apne1-az4 | 262 | 99% | 8.9 | 9 (11-02 23:26Z) |
| ap-northeast-2 apne2-az1 | 403 | 100% | 9.0 | 9 (11-02 23:26Z) |
| ap-northeast-2 apne2-az2 | 106 | 85% | 8.0 | 9 (11-02 15:37Z) |
| ap-northeast-2 apne2-az3 | 421 | 100% | 9.0 | 9 (11-02 23:26Z) |
| ap-northeast-2 apne2-az4 | 318 | 85% | 8.1 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az1 | 172 | 87% | 8.2 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az2 | 183 | 80% | 7.7 | 9 (11-02 23:26Z) |
| ap-south-1 aps1-az3 | 192 | 90% | 8.4 | 9 (11-02 23:26Z) |
| ap-southeast-2 apse2-az1 | 59 | 83% | 7.9 | 9 (11-01 14:59Z) |
| ap-southeast-2 apse2-az2 | 3 | 67% | 7.0 | 9 (10-31 19:10Z) |
| ap-southeast-2 apse2-az3 | 72 | 82% | 7.9 | 9 (11-01 00:41Z) |
| ap-southeast-3 apse3-az3 | 74 | 39% | 5.2 | 9 (10-31 22:12Z) |
| us-east-1 use1-az1 | 27 | 52% | 5.5 | 9 (11-01 00:41Z) |
| us-east-1 use1-az2 | 105 | 100% | 9.0 | 9 (11-02 05:51Z) |
| us-east-1 use1-az4 | 140 | 91% | 8.4 | 9 (11-02 05:51Z) |
| us-east-1 use1-az5 | 103 | 98% | 8.9 | 9 (11-02 05:51Z) |
| us-east-1 use1-az6 | 124 | 92% | 8.4 | 9 (11-02 05:51Z) |
| us-east-2 use2-az1 | 174 | 99% | 8.9 | 9 (11-02 15:37Z) |
| us-east-2 use2-az2 | 192 | 99% | 8.9 | 9 (11-02 05:51Z) |
| us-east-2 use2-az3 | 219 | 96% | 8.7 | 9 (11-02 15:37Z) |
| us-west-2 usw2-az1 | 92 | 98% | 8.8 | 9 (11-01 14:59Z) |
| us-west-2 usw2-az2 | 88 | 90% | 8.3 | 9 (11-01 00:41Z) |
| us-west-2 usw2-az3 | 126 | 90% | 8.3 | 9 (11-02 15:37Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.722500 | 2026-11-02T23:26:31Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-11-02T23:26:31Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.732600 | 2026-11-02T23:26:31Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.840600 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.579700 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.590800 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.572800 | 2026-11-02T23:26:31Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-11-02T23:26:31Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.640300 | 2026-11-02T23:26:31Z |
| ap-south-1 | ap-south-1a | Windows | 0.458100 | 2026-11-02T23:26:31Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.504500 | 2026-11-02T23:26:31Z |
| ap-south-1 | ap-south-1b | Windows | 0.376100 | 2026-11-02T23:26:31Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.631000 | 2026-11-02T23:26:31Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513300 | 2026-11-02T23:26:31Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.712300 | 2026-11-02T23:26:31Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.555700 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.523300 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1a | Windows | 0.284600 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.563000 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.493700 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.504300 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.571700 | 2026-11-02T23:26:31Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.571600 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2a | Windows | 0.638300 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.550400 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2b | Windows | 0.637100 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.549800 | 2026-11-02T23:26:31Z |
| us-east-2 | us-east-2c | Windows | 0.637100 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.564500 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2a | Windows | 0.309100 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.614900 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2b | Windows | 0.319500 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.573700 | 2026-11-02T23:26:31Z |
| us-west-2 | us-west-2c | Windows | 0.308600 | 2026-11-02T23:26:31Z |
