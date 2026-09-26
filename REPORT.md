# Spot placement score log

Generated 2026-09-26 22:42 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 171 | 8% | 2.5 | 9 (09-26 22:42Z) |
| ap-northeast-1 | 171 | 2% | 2.0 | 5 (09-26 22:42Z) |
| ap-northeast-2 | 171 | 11% | 3.6 | 9 (09-26 22:42Z) |
| ap-south-1 | 171 | 0% | 1.9 | 1 (09-26 22:42Z) |
| ap-southeast-2 | 171 | 0% | 1.0 | 1 (09-26 22:42Z) |
| ap-southeast-3 | 171 | 9% | 3.1 | 9 (09-26 22:42Z) |
| us-east-1 | 171 | 1% | 2.0 | 9 (09-26 22:42Z) |
| us-east-2 | 171 | 6% | 2.2 | 9 (09-26 22:42Z) |
| us-west-2 | 171 | 2% | 1.8 | 9 (09-26 22:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333999999999119199919
ap-northeast-1   122122332231232211212213322223322222211343221555
ap-northeast-2   333333333333333333333333333333999999999999999999
ap-south-1       131211333333333321111111111111111111121111311411
ap-southeast-2   111111111111111111131111111111111111111111111111
ap-southeast-3   233333333333133331333133333333996899951989158999
us-east-1        311121311223333333313212232322221232113122332239
us-east-2        331133331233333313311112113113192911219928999999
us-west-2        111233333333333333312112222132221122221112199519
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | · | 1 | 2 | 3 | 2 | 6 | 1 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 4 | 2 | 3 | 3 | 1 | 4 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 5 | · | 3 | 3 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 2 | · | 1 | 2 | 2 | 2 | 6 | 2 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 2 | 4 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 3 | 2 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 1.4 | 1 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 109 | 13% | 3.3 | 9 (09-26 22:42Z) |
| ap-northeast-1 apne1-az1 | 23 | 0% | 1.3 | 2 (09-26 19:48Z) |
| ap-northeast-1 apne1-az4 | 79 | 0% | 2.1 | 2 (09-26 19:48Z) |
| ap-northeast-2 apne2-az1 | 154 | 12% | 3.6 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az3 | 153 | 12% | 3.6 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az4 | 168 | 11% | 3.6 | 9 (09-26 22:42Z) |
| ap-south-1 aps1-az1 | 59 | 0% | 1.7 | 1 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 83 | 0% | 2.5 | 2 (09-26 01:28Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 133 | 11% | 3.5 | 9 (09-26 22:42Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 57 | 0% | 1.3 | 1 (09-26 19:48Z) |
| us-east-1 use1-az4 | 37 | 3% | 1.9 | 9 (09-26 22:42Z) |
| us-east-1 use1-az5 | 51 | 2% | 1.7 | 9 (09-26 22:42Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 57 | 9% | 2.3 | 5 (09-26 19:48Z) |
| us-east-2 use2-az2 | 78 | 10% | 2.6 | 9 (09-26 22:42Z) |
| us-east-2 use2-az3 | 97 | 11% | 3.0 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az1 | 54 | 7% | 2.4 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az2 | 31 | 6% | 2.4 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az3 | 82 | 2% | 1.9 | 9 (09-26 13:00Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 171 | 11% | 3.6 | 9 (09-26 22:42Z) |
| ap-northeast-1 | 171 | 80% | 7.6 | 9 (09-26 22:42Z) |
| ap-northeast-2 | 171 | 100% | 9.0 | 9 (09-26 22:42Z) |
| ap-south-1 | 171 | 51% | 5.9 | 9 (09-26 22:42Z) |
| ap-southeast-2 | 171 | 13% | 3.0 | 9 (09-26 22:42Z) |
| ap-southeast-3 | 171 | 9% | 3.1 | 9 (09-26 22:42Z) |
| us-east-1 | 171 | 76% | 6.9 | 9 (09-26 22:42Z) |
| us-east-2 | 171 | 77% | 7.3 | 9 (09-26 22:42Z) |
| us-west-2 | 171 | 56% | 5.8 | 9 (09-26 22:42Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333999999999999999999
ap-northeast-1   999999999999999999999999999999993499921999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       399999999999999999199924999839999289998999999999
ap-southeast-2   332333333333333322331222222233512299222999999999
ap-southeast-3   233333333333133331333133333333996899951989158999
us-east-1        945499999999999999949994459996669954598347999999
us-east-2        991199991999999999933995999999499923489999999999
us-west-2        334599999999999999943195454995559554459934399999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | · | 3 | 4 | 3 | 3 | 6 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 7 | 3 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 4 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 4 | 4 | 5 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 67 | 19% | 4.2 | 9 (09-26 22:42Z) |
| ap-east-1 ape1-az2 | 51 | 20% | 4.2 | 9 (09-26 13:00Z) |
| ap-east-1 ape1-az3 | 55 | 20% | 4.2 | 9 (09-26 22:42Z) |
| ap-northeast-1 apne1-az1 | 90 | 91% | 8.5 | 9 (09-26 19:48Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 114 | 100% | 9.0 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az1 | 148 | 100% | 9.0 | 9 (09-26 07:34Z) |
| ap-northeast-2 apne2-az2 | 25 | 48% | 5.9 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az3 | 153 | 100% | 9.0 | 9 (09-26 13:00Z) |
| ap-northeast-2 apne2-az4 | 60 | 22% | 4.3 | 9 (09-26 19:48Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 46 | 22% | 4.3 | 9 (09-26 22:42Z) |
| ap-south-1 aps1-az3 | 74 | 76% | 7.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az1 | 18 | 44% | 5.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 20 | 40% | 5.4 | 9 (09-26 22:42Z) |
| ap-southeast-3 apse3-az3 | 48 | 17% | 4.0 | 9 (09-26 22:42Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 63 | 100% | 9.0 | 9 (09-26 13:00Z) |
| us-east-1 use1-az4 | 70 | 97% | 8.8 | 9 (09-26 22:42Z) |
| us-east-1 use1-az5 | 33 | 97% | 8.8 | 9 (09-26 13:00Z) |
| us-east-1 use1-az6 | 65 | 100% | 9.0 | 9 (09-26 07:34Z) |
| us-east-2 use2-az1 | 66 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-east-2 use2-az2 | 99 | 98% | 8.8 | 9 (09-26 01:28Z) |
| us-east-2 use2-az3 | 88 | 91% | 8.4 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az1 | 52 | 98% | 8.9 | 9 (09-26 13:00Z) |
| us-west-2 usw2-az2 | 45 | 98% | 8.8 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az3 | 61 | 98% | 8.9 | 9 (09-26 17:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.727200 | 2026-09-26T22:42:03Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.852700 | 2026-09-26T22:42:03Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.826500 | 2026-09-26T22:42:03Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.995500 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592500 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577900 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568100 | 2026-09-26T22:42:03Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-09-26T22:42:03Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.536000 | 2026-09-26T22:42:03Z |
| ap-south-1 | ap-south-1a | Windows | 0.343900 | 2026-09-26T22:42:03Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.528400 | 2026-09-26T22:42:03Z |
| ap-south-1 | ap-south-1b | Windows | 0.321800 | 2026-09-26T22:42:03Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.650300 | 2026-09-26T22:42:03Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.514700 | 2026-09-26T22:42:03Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.701000 | 2026-09-26T22:42:03Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.570600 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.685800 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1a | Windows | 0.318900 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.500100 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1b | Windows | 0.285200 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.432500 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.407500 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.423300 | 2026-09-26T22:42:03Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524300 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.527100 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2b | Windows | 0.641300 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513900 | 2026-09-26T22:42:03Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.511300 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2a | Windows | 0.332600 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.484800 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2b | Windows | 0.332500 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.482800 | 2026-09-26T22:42:03Z |
| us-west-2 | us-west-2c | Windows | 0.331500 | 2026-09-26T22:42:03Z |
