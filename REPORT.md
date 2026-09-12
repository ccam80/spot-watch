# Spot placement score log

Generated 2026-09-12 01:03 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 88 | 0% | 1.2 | 3 (09-12 01:03Z) |
| ap-northeast-1 | 88 | 0% | 1.8 | 3 (09-12 01:03Z) |
| ap-northeast-2 | 88 | 0% | 2.9 | 3 (09-12 01:03Z) |
| ap-south-1 | 88 | 0% | 1.9 | 1 (09-12 01:03Z) |
| ap-southeast-2 | 88 | 0% | 1.0 | 1 (09-12 01:03Z) |
| ap-southeast-3 | 88 | 0% | 2.5 | 3 (09-12 01:03Z) |
| us-east-1 | 88 | 0% | 1.9 | 3 (09-12 01:03Z) |
| us-east-2 | 88 | 0% | 1.5 | 1 (09-12 01:03Z) |
| us-west-2 | 88 | 0% | 1.4 | 1 (09-12 01:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111111111111111111133333333333
ap-northeast-1   131133331133333122111122211232222221123221123323
ap-northeast-2   333333333333333333333333333333333333233333333333
ap-south-1       223333332333311121111311122111111111211313121111
ap-southeast-2   111111111111111111111111111111111111111111111311
ap-southeast-3   133333333113333333313333212333113133113333333333
us-east-1        321131323333232323332322333321133221221131131133
us-east-2        111111131111133111131113333113333111311111131311
us-west-2        222222211111111111111213311111111111111111111111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 2 | · | 1 | 1 | 2 | 1 | · | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | 1 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 2 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 1 | 2 | · | 3 | 2 | 2 | 1 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 1 | 1 | · | 1 | 2 | 2 | 1 | · | 2 | 2 | 1 | 2 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 27 | 0% | 1.0 | 1 (09-10 16:19Z) |
| ap-east-1 ape1-az2 | 37 | 0% | 1.6 | 3 (09-12 01:03Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 44 | 0% | 2.1 | 3 (09-12 01:03Z) |
| ap-northeast-2 apne2-az1 | 83 | 0% | 2.9 | 3 (09-12 01:03Z) |
| ap-northeast-2 apne2-az3 | 80 | 0% | 2.9 | 3 (09-12 01:03Z) |
| ap-northeast-2 apne2-az4 | 86 | 0% | 3.0 | 3 (09-12 01:03Z) |
| ap-south-1 aps1-az1 | 40 | 0% | 1.5 | 1 (09-12 01:03Z) |
| ap-south-1 aps1-az3 | 47 | 0% | 2.5 | 3 (09-11 00:59Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 71 | 0% | 2.9 | 3 (09-12 01:03Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 26 | 0% | 1.1 | 1 (09-11 05:52Z) |
| us-east-1 use1-az4 | 15 | 0% | 1.3 | 1 (09-11 22:30Z) |
| us-east-1 use1-az5 | 28 | 0% | 1.3 | 3 (09-10 22:29Z) |
| us-east-1 use1-az6 | 38 | 0% | 1.2 | 1 (09-11 22:30Z) |
| us-east-2 use2-az1 | 25 | 0% | 1.2 | 1 (09-12 01:03Z) |
| us-east-2 use2-az2 | 36 | 0% | 1.6 | 1 (09-12 01:03Z) |
| us-east-2 use2-az3 | 38 | 0% | 2.0 | 3 (09-11 19:36Z) |
| us-west-2 usw2-az1 | 18 | 0% | 1.4 | 1 (09-10 16:19Z) |
| us-west-2 usw2-az2 | 14 | 0% | 1.3 | 1 (09-11 00:59Z) |
| us-west-2 usw2-az3 | 45 | 0% | 1.3 | 1 (09-12 01:03Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 88 | 0% | 3.0 | 3 (09-12 01:03Z) |
| ap-northeast-1 | 88 | 75% | 7.3 | 9 (09-12 01:03Z) |
| ap-northeast-2 | 88 | 100% | 9.0 | 9 (09-12 01:03Z) |
| ap-south-1 | 88 | 16% | 3.8 | 9 (09-12 01:03Z) |
| ap-southeast-2 | 88 | 11% | 2.7 | 3 (09-12 01:03Z) |
| ap-southeast-3 | 88 | 0% | 2.5 | 3 (09-12 01:03Z) |
| us-east-1 | 88 | 72% | 6.5 | 9 (09-12 01:03Z) |
| us-east-2 | 88 | 68% | 6.8 | 9 (09-12 01:03Z) |
| us-west-2 | 88 | 43% | 5.1 | 3 (09-12 01:03Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   299999999999999999912999439999339992249992349999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333333333333333333999922999513339939999
ap-southeast-2   133133333333333333111311113311113322222311233333
ap-southeast-3   133333333113333333313333212333113133113333333333
us-east-1        542565995999999999999999995445994456993299992349
us-east-2        933829999999999999999999999999999199992333991919
us-west-2        453454499858969999719999999442951332313323423353
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 5 | 9 | · | 1 | 4 | 2 | 1 | · | 9 | 3 | 2 | 6 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 6 | 6 | · | 3 | 4 | 7 | 1 | · | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3 |
| ap-southeast-2 | 1 | 6 | · | 1 | 2 | 2 | 1 | · | 6 | 1 | 1 | 4 | 2 | 3 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 5 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 8 | 5 | 9 | 5 | 4 | 6 | 1 | 5 | 6 | 4 | 6 | 7 | 7 |
| us-east-2 | 4 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 3 | 6 |
| us-west-2 | 3 | 2 | · | 2 | 6 | 4 | 9 | · | 6 | 5 | 9 | 5 | 9 | 9 | 7 | 9 | 5 | 2 | 5 | 4 | 5 | 5 | 3 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 40 | 80% | 7.8 | 9 (09-12 01:03Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 62 | 100% | 9.0 | 9 (09-12 01:03Z) |
| ap-northeast-2 apne2-az1 | 84 | 100% | 9.0 | 9 (09-12 01:03Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 84 | 100% | 9.0 | 9 (09-12 01:03Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 22 | 23% | 4.4 | 9 (09-12 01:03Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 4 | 100% | 8.2 | 9 (09-06 09:20Z) |
| us-east-1 use1-az2 | 30 | 100% | 9.0 | 9 (09-12 01:03Z) |
| us-east-1 use1-az4 | 33 | 97% | 8.8 | 9 (09-12 01:03Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 37 | 100% | 9.0 | 9 (09-12 01:03Z) |
| us-east-2 use2-az1 | 35 | 100% | 9.0 | 9 (09-12 01:03Z) |
| us-east-2 use2-az2 | 53 | 96% | 8.7 | 9 (09-11 11:10Z) |
| us-east-2 use2-az3 | 36 | 78% | 7.5 | 9 (09-12 01:03Z) |
| us-west-2 usw2-az1 | 27 | 96% | 8.8 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az2 | 18 | 94% | 8.7 | 9 (09-09 04:36Z) |
| us-west-2 usw2-az3 | 27 | 96% | 8.7 | 9 (09-09 04:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.739500 | 2026-09-12T01:03:37Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.841000 | 2026-09-12T01:03:37Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.787200 | 2026-09-12T01:03:37Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.970200 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594300 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.581500 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.570000 | 2026-09-12T01:03:37Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.740700 | 2026-09-12T01:03:37Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.534300 | 2026-09-12T01:03:37Z |
| ap-south-1 | ap-south-1a | Windows | 0.320000 | 2026-09-12T01:03:37Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.495200 | 2026-09-12T01:03:37Z |
| ap-south-1 | ap-south-1b | Windows | 0.324700 | 2026-09-12T01:03:37Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.750200 | 2026-09-12T01:03:37Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.502000 | 2026-09-12T01:03:37Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.833800 | 2026-09-12T01:03:37Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.426400 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.901600 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1a | Windows | 0.358500 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.713900 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1b | Windows | 0.327400 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.599000 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1c | Windows | 0.317200 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.539200 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1d | Windows | 0.324000 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.587000 | 2026-09-12T01:03:37Z |
| us-east-1 | us-east-1f | Windows | 0.318100 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.544600 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2a | Windows | 0.643800 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.536500 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.526800 | 2026-09-12T01:03:37Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.585200 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2a | Windows | 0.323800 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.558700 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2b | Windows | 0.331800 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.548800 | 2026-09-12T01:03:37Z |
| us-west-2 | us-west-2c | Windows | 0.343700 | 2026-09-12T01:03:37Z |
