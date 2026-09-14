# Spot placement score log

Generated 2026-09-14 13:55 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 103 | 0% | 1.5 | 3 (09-14 13:55Z) |
| ap-northeast-1 | 103 | 0% | 2.0 | 3 (09-14 13:55Z) |
| ap-northeast-2 | 103 | 0% | 3.0 | 3 (09-14 13:55Z) |
| ap-south-1 | 103 | 0% | 2.1 | 3 (09-14 13:55Z) |
| ap-southeast-2 | 103 | 0% | 1.0 | 1 (09-14 13:55Z) |
| ap-southeast-3 | 103 | 0% | 2.6 | 3 (09-14 13:55Z) |
| us-east-1 | 103 | 0% | 2.0 | 2 (09-14 13:55Z) |
| us-east-2 | 103 | 0% | 1.7 | 3 (09-14 13:55Z) |
| us-west-2 | 103 | 0% | 1.5 | 3 (09-14 13:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        111111111111111111111133333333333333333333333333
ap-northeast-1   122111122211232222221123221123323333333333333223
ap-northeast-2   333333333333333333333233333333333333333333333333
ap-south-1       121111311122111111111211313121111333333313333333
ap-southeast-2   111111111111111111111111111111311111111111111111
ap-southeast-3   333313333212333113133113333333333333333333333313
us-east-1        323332322333321133221221131131133223311323233222
us-east-2        111131113333113333111311111131311333333333333333
us-west-2        111111213311111111111111111111111133313313333333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 2 | · | 1 | 1 | 2 | 2 | · | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| ap-northeast-1 | 2 | 3 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | · | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | 1 | 2 | · | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 28 | 0% | 1.0 | 1 (09-13 06:01Z) |
| ap-east-1 ape1-az2 | 48 | 0% | 1.9 | 3 (09-14 13:55Z) |
| ap-northeast-1 apne1-az1 | 17 | 0% | 1.1 | 1 (09-11 00:59Z) |
| ap-northeast-1 apne1-az4 | 56 | 0% | 2.3 | 3 (09-14 13:55Z) |
| ap-northeast-2 apne2-az1 | 97 | 0% | 2.9 | 3 (09-14 13:55Z) |
| ap-northeast-2 apne2-az3 | 93 | 0% | 2.9 | 3 (09-14 13:55Z) |
| ap-northeast-2 apne2-az4 | 100 | 0% | 3.0 | 3 (09-14 13:55Z) |
| ap-south-1 aps1-az1 | 43 | 0% | 1.6 | 3 (09-14 00:58Z) |
| ap-south-1 aps1-az3 | 59 | 0% | 2.6 | 3 (09-14 13:55Z) |
| ap-southeast-2 apse2-az1 | 20 | 0% | 1.1 | 3 (09-11 19:36Z) |
| ap-southeast-2 apse2-az2 | 16 | 0% | 1.0 | 1 (09-11 22:30Z) |
| ap-southeast-3 apse3-az1 | 16 | 0% | 1.0 | 1 (09-11 05:52Z) |
| ap-southeast-3 apse3-az3 | 82 | 0% | 2.9 | 3 (09-14 00:58Z) |
| us-east-1 use1-az1 | 13 | 0% | 1.0 | 1 (09-11 22:30Z) |
| us-east-1 use1-az2 | 27 | 0% | 1.1 | 3 (09-13 19:23Z) |
| us-east-1 use1-az4 | 16 | 0% | 1.2 | 1 (09-12 19:13Z) |
| us-east-1 use1-az5 | 29 | 0% | 1.3 | 3 (09-13 19:23Z) |
| us-east-1 use1-az6 | 39 | 0% | 1.2 | 3 (09-13 19:23Z) |
| us-east-2 use2-az1 | 31 | 0% | 1.6 | 3 (09-13 06:01Z) |
| us-east-2 use2-az2 | 45 | 0% | 1.9 | 3 (09-14 13:55Z) |
| us-east-2 use2-az3 | 51 | 0% | 2.3 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az1 | 28 | 0% | 2.0 | 3 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 21 | 0% | 1.9 | 3 (09-14 06:08Z) |
| us-west-2 usw2-az3 | 55 | 0% | 1.6 | 3 (09-14 13:55Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 103 | 0% | 3.0 | 3 (09-14 13:55Z) |
| ap-northeast-1 | 103 | 78% | 7.4 | 9 (09-14 13:55Z) |
| ap-northeast-2 | 103 | 100% | 9.0 | 9 (09-14 13:55Z) |
| ap-south-1 | 103 | 28% | 4.5 | 9 (09-14 13:55Z) |
| ap-southeast-2 | 103 | 10% | 2.7 | 2 (09-14 13:55Z) |
| ap-southeast-3 | 103 | 0% | 2.6 | 3 (09-14 13:55Z) |
| us-east-1 | 103 | 75% | 6.8 | 4 (09-14 13:55Z) |
| us-east-2 | 103 | 73% | 7.1 | 9 (09-14 13:55Z) |
| us-west-2 | 103 | 51% | 5.7 | 9 (09-14 13:55Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333333333333333
ap-northeast-1   999912999439999339992249992349999999999999999649
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       333333333333999922999513339939999999999999999999
ap-southeast-2   333111311113311113322222311233333333333322332222
ap-southeast-3   333313333212333113133113333333333333333333333313
us-east-1        999999999995445994456993299992349999999999999994
us-east-2        999999999999999999199992333991919999999999999999
us-west-2        999719999999442951332313323423353999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 4 | 5 | 4 | · | 9 | 3 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 7 | 6 | · | 3 | 4 | 8 | 5 | · | 3 | 3 | 6 | 4 | 2 | 6 | 3 | 3 | 5 | 6 | 5 | 6 | 3 | 4 | 6 | 3 |
| ap-southeast-2 | 2 | 6 | · | 1 | 2 | 2 | 2 | · | 6 | 1 | 2 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | 4 | 4 | 1 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 2 | · | 3 | 2 | 2 | 2 | · | 2 | 2 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| us-east-1 | 6 | 9 | · | 6 | 8 | 9 | 9 | · | 9 | 8 | 9 | 9 | 5 | 6 | 6 | 4 | 7 | 5 | 5 | 7 | 4 | 6 | 7 | 7 |
| us-east-2 | 6 | 5 | · | 9 | 8 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 5 | 6 | 9 | 4 | 8 | 6 | 7 | 5 | 6 |
| us-west-2 | 5 | 2 | · | 2 | 6 | 5 | 9 | · | 6 | 5 | 9 | 6 | 9 | 9 | 7 | 9 | 6 | 6 | 5 | 6 | 5 | 5 | 5 | 6 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 39 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az2 | 31 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-east-1 ape1-az3 | 32 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-1 apne1-az1 | 51 | 84% | 8.0 | 9 (09-14 13:55Z) |
| ap-northeast-1 apne1-az2 | 20 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-northeast-1 apne1-az4 | 71 | 100% | 9.0 | 9 (09-14 13:55Z) |
| ap-northeast-2 apne2-az1 | 94 | 100% | 9.0 | 9 (09-14 13:55Z) |
| ap-northeast-2 apne2-az2 | 9 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-northeast-2 apne2-az3 | 93 | 100% | 9.0 | 9 (09-14 13:55Z) |
| ap-northeast-2 apne2-az4 | 34 | 0% | 3.0 | 3 (09-11 11:10Z) |
| ap-south-1 aps1-az1 | 21 | 0% | 3.0 | 3 (09-11 22:30Z) |
| ap-south-1 aps1-az2 | 27 | 0% | 3.0 | 3 (09-11 00:59Z) |
| ap-south-1 aps1-az3 | 34 | 50% | 6.0 | 9 (09-14 13:55Z) |
| ap-southeast-2 apse2-az1 | 10 | 30% | 4.6 | 3 (09-11 22:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 12 | 0% | 3.0 | 3 (09-11 19:36Z) |
| ap-southeast-3 apse3-az3 | 29 | 0% | 3.0 | 3 (09-11 16:23Z) |
| us-east-1 use1-az1 | 10 | 100% | 8.7 | 9 (09-13 11:41Z) |
| us-east-1 use1-az2 | 43 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-1 use1-az4 | 44 | 98% | 8.8 | 9 (09-14 00:58Z) |
| us-east-1 use1-az5 | 23 | 96% | 8.7 | 3 (09-11 05:52Z) |
| us-east-1 use1-az6 | 44 | 100% | 9.0 | 9 (09-14 06:08Z) |
| us-east-2 use2-az1 | 40 | 100% | 9.0 | 9 (09-14 13:55Z) |
| us-east-2 use2-az2 | 68 | 97% | 8.8 | 9 (09-14 13:55Z) |
| us-east-2 use2-az3 | 44 | 82% | 7.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az1 | 41 | 98% | 8.9 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az2 | 26 | 96% | 8.8 | 9 (09-14 13:55Z) |
| us-west-2 usw2-az3 | 39 | 97% | 8.8 | 9 (09-14 00:58Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725800 | 2026-09-14T13:55:21Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-09-14T13:55:21Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.793600 | 2026-09-14T13:55:21Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.969600 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592400 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.580600 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.567800 | 2026-09-14T13:55:21Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.741300 | 2026-09-14T13:55:21Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.590000 | 2026-09-14T13:55:21Z |
| ap-south-1 | ap-south-1a | Windows | 0.319800 | 2026-09-14T13:55:21Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.513400 | 2026-09-14T13:55:21Z |
| ap-south-1 | ap-south-1b | Windows | 0.321700 | 2026-09-14T13:55:21Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.713500 | 2026-09-14T13:55:21Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.507100 | 2026-09-14T13:55:21Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.849300 | 2026-09-14T13:55:21Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.482800 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.870300 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1a | Windows | 0.347400 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.678500 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1b | Windows | 0.331300 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.595700 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1c | Windows | 0.310500 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.540500 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1d | Windows | 0.319000 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.594400 | 2026-09-14T13:55:21Z |
| us-east-1 | us-east-1f | Windows | 0.330300 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.532100 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2a | Windows | 0.641700 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.532800 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2b | Windows | 0.637400 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.522700 | 2026-09-14T13:55:21Z |
| us-east-2 | us-east-2c | Windows | 0.638200 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.588500 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2a | Windows | 0.343400 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.564600 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2b | Windows | 0.341200 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.543400 | 2026-09-14T13:55:21Z |
| us-west-2 | us-west-2c | Windows | 0.342700 | 2026-09-14T13:55:21Z |
