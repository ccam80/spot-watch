# Spot placement score log

Generated 2026-09-28 04:30 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 185 | 14% | 2.9 | 9 (09-28 04:30Z) |
| ap-northeast-1 | 185 | 3% | 2.1 | 1 (09-28 04:30Z) |
| ap-northeast-2 | 185 | 17% | 4.0 | 9 (09-28 04:30Z) |
| ap-south-1 | 185 | 3% | 2.1 | 1 (09-28 04:30Z) |
| ap-southeast-2 | 185 | 0% | 1.0 | 1 (09-28 04:30Z) |
| ap-southeast-3 | 185 | 13% | 3.2 | 1 (09-28 04:30Z) |
| us-east-1 | 185 | 3% | 2.2 | 9 (09-28 04:30Z) |
| us-east-2 | 185 | 14% | 2.8 | 9 (09-28 04:30Z) |
| us-west-2 | 185 | 8% | 2.2 | 9 (09-28 04:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333399999999911919991999999889911399
ap-northeast-1   221121221332222332222221134322155531664444211111
ap-northeast-2   333333333333333399999999999999999999999999999999
ap-south-1       332111111111111111111112111131141111599927913441
ap-southeast-2   111113111111111111111111111111111111111111111111
ap-southeast-3   333133313333333399689995198915899992869998911111
us-east-1        333331321223232222123211312233223923322229999119
us-east-2        331331111211311319291121992899999999999999999999
us-west-2        333331211222213222112222111219951929912999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 3 | 3 | 5 | 3 | 3 | 2 | 6 | 4 | 2 | 2 | 2 | 1 | 4 | 2 | 2 | 2 | 4 | 2 | 4 | 4 | 2 | 4 | 3 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 2 |
| ap-northeast-2 | 3 | 6 | 9 | 6 | 4 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-south-1 | 2 | 2 | 4 | 4 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 2 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 4 | 9 | 5 | 2 | 2 | 2 | 6 | 4 | 3 | 2 | 2 | 2 | 5 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 9 | 5 | 2 | 1 | 2 | 3 | 4 | 1 | 2 | 2 | 1 | 4 | 2 | 2 | 2 | 3 | 1 | 1 | 3 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 55 | 0% | 1.4 | 3 (09-27 01:21Z) |
| ap-east-1 ape1-az2 | 121 | 21% | 3.8 | 9 (09-28 04:30Z) |
| ap-northeast-1 apne1-az1 | 23 | 0% | 1.3 | 2 (09-26 19:48Z) |
| ap-northeast-1 apne1-az4 | 80 | 0% | 2.1 | 3 (09-27 18:17Z) |
| ap-northeast-2 apne2-az1 | 165 | 17% | 4.0 | 8 (09-28 03:32Z) |
| ap-northeast-2 apne2-az3 | 167 | 19% | 4.1 | 9 (09-28 04:30Z) |
| ap-northeast-2 apne2-az4 | 182 | 18% | 4.0 | 9 (09-28 04:30Z) |
| ap-south-1 aps1-az1 | 60 | 2% | 1.8 | 7 (09-27 19:17Z) |
| ap-south-1 aps1-az3 | 87 | 3% | 2.7 | 1 (09-28 02:38Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 140 | 16% | 3.8 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 59 | 3% | 1.6 | 9 (09-28 04:30Z) |
| us-east-1 use1-az4 | 43 | 14% | 2.7 | 9 (09-28 04:30Z) |
| us-east-1 use1-az5 | 54 | 7% | 2.1 | 9 (09-28 01:42Z) |
| us-east-1 use1-az6 | 50 | 4% | 1.7 | 9 (09-28 04:30Z) |
| us-east-2 use2-az1 | 66 | 21% | 3.2 | 9 (09-28 04:30Z) |
| us-east-2 use2-az2 | 90 | 22% | 3.5 | 9 (09-28 04:30Z) |
| us-east-2 use2-az3 | 109 | 21% | 3.6 | 9 (09-28 03:32Z) |
| us-west-2 usw2-az1 | 65 | 23% | 3.6 | 9 (09-28 04:30Z) |
| us-west-2 usw2-az2 | 39 | 23% | 3.5 | 6 (09-28 03:32Z) |
| us-west-2 usw2-az3 | 92 | 13% | 2.7 | 9 (09-28 04:30Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 185 | 17% | 4.0 | 9 (09-28 04:30Z) |
| ap-northeast-1 | 185 | 78% | 7.5 | 1 (09-28 04:30Z) |
| ap-northeast-2 | 185 | 100% | 9.0 | 9 (09-28 04:30Z) |
| ap-south-1 | 185 | 55% | 6.1 | 9 (09-28 04:30Z) |
| ap-southeast-2 | 185 | 16% | 3.2 | 2 (09-28 04:30Z) |
| ap-southeast-3 | 185 | 13% | 3.2 | 1 (09-28 04:30Z) |
| us-east-1 | 185 | 78% | 7.1 | 9 (09-28 04:30Z) |
| us-east-2 | 185 | 78% | 7.5 | 9 (09-28 04:30Z) |
| us-west-2 | 185 | 59% | 6.1 | 9 (09-28 04:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333399999999999999999999999999999999
ap-northeast-1   999999999999999999349992199999999999999999911111
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999919992499983999928999899999999999999999999999
ap-southeast-2   332233122222223351229922299999999999999992222222
ap-southeast-3   333133313333333399689995198915899992869998911111
us-east-1        999994999445999666995459834799999999999999999999
us-east-2        999993399599999949992348999999999999999999999999
us-west-2        999994319545499555955445993439999999999999999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 6 | 9 | 6 | 4 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 6 | 5 | 1 | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | 9 | 6 | 5 | 8 | 7 | 7 | 5 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 6 | 7 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 4 | 7 | 2 | 2 | 3 | 2 | 5 | 4 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 5 | 4 |
| us-east-1 | 6 | 8 | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 6 | 9 | 6 | 6 | 7 | 9 | 6 | 7 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 81 | 33% | 5.0 | 9 (09-28 04:30Z) |
| ap-east-1 ape1-az2 | 59 | 31% | 4.8 | 9 (09-28 04:30Z) |
| ap-east-1 ape1-az3 | 59 | 25% | 4.5 | 9 (09-28 03:32Z) |
| ap-northeast-1 apne1-az1 | 92 | 91% | 8.5 | 9 (09-27 18:17Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 117 | 100% | 9.0 | 9 (09-27 23:19Z) |
| ap-northeast-2 apne2-az1 | 149 | 100% | 9.0 | 9 (09-28 01:03Z) |
| ap-northeast-2 apne2-az2 | 31 | 58% | 6.5 | 9 (09-28 04:30Z) |
| ap-northeast-2 apne2-az3 | 163 | 100% | 9.0 | 9 (09-28 04:30Z) |
| ap-northeast-2 apne2-az4 | 70 | 33% | 5.0 | 9 (09-28 03:32Z) |
| ap-south-1 aps1-az1 | 55 | 60% | 6.6 | 9 (09-28 04:30Z) |
| ap-south-1 aps1-az2 | 58 | 38% | 5.3 | 9 (09-28 03:32Z) |
| ap-south-1 aps1-az3 | 77 | 77% | 7.6 | 9 (09-28 04:30Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 22 | 45% | 5.7 | 9 (09-27 18:17Z) |
| ap-southeast-3 apse3-az3 | 49 | 18% | 4.1 | 9 (09-27 23:19Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 72 | 100% | 9.0 | 9 (09-28 04:30Z) |
| us-east-1 use1-az4 | 76 | 97% | 8.8 | 9 (09-28 03:32Z) |
| us-east-1 use1-az5 | 42 | 98% | 8.8 | 9 (09-28 04:30Z) |
| us-east-1 use1-az6 | 70 | 100% | 9.0 | 9 (09-28 03:32Z) |
| us-east-2 use2-az1 | 71 | 99% | 8.9 | 9 (09-28 04:30Z) |
| us-east-2 use2-az2 | 102 | 98% | 8.9 | 9 (09-27 22:21Z) |
| us-east-2 use2-az3 | 94 | 91% | 8.4 | 9 (09-28 03:32Z) |
| us-west-2 usw2-az1 | 58 | 98% | 8.9 | 9 (09-28 04:30Z) |
| us-west-2 usw2-az2 | 52 | 98% | 8.8 | 9 (09-28 03:32Z) |
| us-west-2 usw2-az3 | 64 | 98% | 8.9 | 9 (09-28 02:38Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.730700 | 2026-09-28T04:30:25Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.877800 | 2026-09-28T04:30:25Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.825300 | 2026-09-28T04:30:25Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.004600 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593500 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578100 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568100 | 2026-09-28T04:30:25Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-28T04:30:25Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.560700 | 2026-09-28T04:30:25Z |
| ap-south-1 | ap-south-1a | Windows | 0.345700 | 2026-09-28T04:30:25Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.586200 | 2026-09-28T04:30:25Z |
| ap-south-1 | ap-south-1b | Windows | 0.330900 | 2026-09-28T04:30:25Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.693300 | 2026-09-28T04:30:25Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.503900 | 2026-09-28T04:30:25Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.664900 | 2026-09-28T04:30:25Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.650100 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1a | Windows | 0.311900 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.483500 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.430700 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.390700 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.422000 | 2026-09-28T04:30:25Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.526900 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2a | Windows | 0.640900 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524400 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2b | Windows | 0.641100 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.512900 | 2026-09-28T04:30:25Z |
| us-east-2 | us-east-2c | Windows | 0.637800 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.506000 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2a | Windows | 0.333000 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.487600 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2b | Windows | 0.332900 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.482100 | 2026-09-28T04:30:25Z |
| us-west-2 | us-west-2c | Windows | 0.331900 | 2026-09-28T04:30:25Z |
