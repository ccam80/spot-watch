# Spot placement score log

Generated 2026-09-27 08:02 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 173 | 9% | 2.6 | 9 (09-27 08:02Z) |
| ap-northeast-1 | 173 | 2% | 2.0 | 1 (09-27 08:02Z) |
| ap-northeast-2 | 173 | 12% | 3.7 | 9 (09-27 08:02Z) |
| ap-south-1 | 173 | 0% | 1.9 | 1 (09-27 08:02Z) |
| ap-southeast-2 | 173 | 0% | 1.0 | 1 (09-27 08:02Z) |
| ap-southeast-3 | 173 | 10% | 3.1 | 2 (09-27 08:02Z) |
| us-east-1 | 173 | 1% | 2.0 | 3 (09-27 08:02Z) |
| us-east-2 | 173 | 8% | 2.3 | 9 (09-27 08:02Z) |
| us-west-2 | 173 | 3% | 1.8 | 9 (09-27 08:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333399999999911919991999
ap-northeast-1   212233223123221121221332222332222221134322155531
ap-northeast-2   333333333333333333333333333399999999999999999999
ap-south-1       121133333333332111111111111111111112111131141111
ap-southeast-2   111111111111111113111111111111111111111111111111
ap-southeast-3   333333333313333133313333333399689995198915899992
us-east-1        112131122333333331321223232222123211312233223923
us-east-2        113333123333331331111211311319291121992899999999
us-west-2        123333333333333331211222213222112222111219951929
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | · | 1 | 2 | 3 | 2 | 6 | 4 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 4 | 2 | 3 | 3 | 1 | 4 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 5 | · | 3 | 3 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 4 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 3 | · | 1 | 2 | 2 | 2 | 6 | 4 | 3 | 2 | 2 | 2 | 4 | 2 | 2 | 2 | 4 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 3 | 4 | 1 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 55 | 0% | 1.4 | 3 (09-27 01:21Z) |
| ap-east-1 ape1-az2 | 111 | 14% | 3.4 | 9 (09-27 08:02Z) |
| ap-northeast-1 apne1-az1 | 23 | 0% | 1.3 | 2 (09-26 19:48Z) |
| ap-northeast-1 apne1-az4 | 79 | 0% | 2.1 | 2 (09-26 19:48Z) |
| ap-northeast-2 apne2-az1 | 156 | 13% | 3.7 | 9 (09-27 08:02Z) |
| ap-northeast-2 apne2-az3 | 155 | 13% | 3.7 | 9 (09-27 08:02Z) |
| ap-northeast-2 apne2-az4 | 170 | 12% | 3.7 | 9 (09-27 08:02Z) |
| ap-south-1 aps1-az1 | 59 | 0% | 1.7 | 1 (09-26 01:28Z) |
| ap-south-1 aps1-az3 | 83 | 0% | 2.5 | 2 (09-26 01:28Z) |
| ap-southeast-2 apse2-az1 | 27 | 0% | 1.1 | 1 (09-25 22:14Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 134 | 12% | 3.5 | 9 (09-27 01:21Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 57 | 0% | 1.3 | 1 (09-26 19:48Z) |
| us-east-1 use1-az4 | 38 | 3% | 1.8 | 1 (09-27 01:21Z) |
| us-east-1 use1-az5 | 51 | 2% | 1.7 | 9 (09-26 22:42Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 59 | 12% | 2.5 | 9 (09-27 08:02Z) |
| us-east-2 use2-az2 | 80 | 12% | 2.8 | 9 (09-27 08:02Z) |
| us-east-2 use2-az3 | 99 | 13% | 3.1 | 9 (09-27 08:02Z) |
| us-west-2 usw2-az1 | 55 | 9% | 2.6 | 9 (09-27 08:02Z) |
| us-west-2 usw2-az2 | 32 | 9% | 2.6 | 9 (09-27 08:02Z) |
| us-west-2 usw2-az3 | 83 | 4% | 2.0 | 9 (09-27 08:02Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 173 | 12% | 3.7 | 9 (09-27 08:02Z) |
| ap-northeast-1 | 173 | 80% | 7.6 | 9 (09-27 08:02Z) |
| ap-northeast-2 | 173 | 100% | 9.0 | 9 (09-27 08:02Z) |
| ap-south-1 | 173 | 51% | 5.9 | 9 (09-27 08:02Z) |
| ap-southeast-2 | 173 | 14% | 3.1 | 9 (09-27 08:02Z) |
| ap-southeast-3 | 173 | 10% | 3.1 | 2 (09-27 08:02Z) |
| us-east-1 | 173 | 76% | 7.0 | 9 (09-27 08:02Z) |
| us-east-2 | 173 | 77% | 7.4 | 9 (09-27 08:02Z) |
| us-west-2 | 173 | 56% | 5.9 | 9 (09-27 08:02Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333399999999999999999999
ap-northeast-1   999999999999999999999999999999349992199999999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999919992499983999928999899999999999
ap-southeast-2   233333333333332233122222223351229922299999999999
ap-southeast-3   333333333313333133313333333399689995198915899992
us-east-1        549999999999999994999445999666995459834799999999
us-east-2        119999199999999993399599999949992348999999999999
us-west-2        459999999999999994319545499555955445993439999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | · | 3 | 4 | 3 | 3 | 6 | 5 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 4 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 7 | 5 | 2 | 7 | 4 | 2 | 6 | 4 | 5 | 6 | 8 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 5 | · | 1 | 2 | 2 | 2 | 4 | 7 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 4 | 4 | 5 | 2 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 4 | · | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 3 | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 8 | 9 | 9 | 9 | 9 | 5 | 6 | 6 | 6 | 6 | 7 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 5 | · | 2 | 6 | 7 | 9 | 6 | 7 | 5 | 9 | 7 | 9 | 8 | 6 | 9 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 69 | 22% | 4.3 | 9 (09-27 08:02Z) |
| ap-east-1 ape1-az2 | 53 | 23% | 4.4 | 9 (09-27 08:02Z) |
| ap-east-1 ape1-az3 | 55 | 20% | 4.2 | 9 (09-26 22:42Z) |
| ap-northeast-1 apne1-az1 | 90 | 91% | 8.5 | 9 (09-26 19:48Z) |
| ap-northeast-1 apne1-az2 | 32 | 19% | 4.1 | 9 (09-26 07:34Z) |
| ap-northeast-1 apne1-az4 | 114 | 100% | 9.0 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az1 | 148 | 100% | 9.0 | 9 (09-26 07:34Z) |
| ap-northeast-2 apne2-az2 | 25 | 48% | 5.9 | 9 (09-26 22:42Z) |
| ap-northeast-2 apne2-az3 | 155 | 100% | 9.0 | 9 (09-27 08:02Z) |
| ap-northeast-2 apne2-az4 | 62 | 24% | 4.5 | 9 (09-27 08:02Z) |
| ap-south-1 aps1-az1 | 54 | 59% | 6.6 | 9 (09-26 01:28Z) |
| ap-south-1 aps1-az2 | 48 | 25% | 4.5 | 9 (09-27 08:02Z) |
| ap-south-1 aps1-az3 | 74 | 76% | 7.6 | 9 (09-26 13:00Z) |
| ap-southeast-2 apse2-az1 | 20 | 50% | 5.9 | 9 (09-27 08:02Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 20 | 40% | 5.4 | 9 (09-26 22:42Z) |
| ap-southeast-3 apse3-az3 | 48 | 17% | 4.0 | 9 (09-26 22:42Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 65 | 100% | 9.0 | 9 (09-27 08:02Z) |
| us-east-1 use1-az4 | 70 | 97% | 8.8 | 9 (09-26 22:42Z) |
| us-east-1 use1-az5 | 35 | 97% | 8.8 | 9 (09-27 08:02Z) |
| us-east-1 use1-az6 | 65 | 100% | 9.0 | 9 (09-26 07:34Z) |
| us-east-2 use2-az1 | 67 | 99% | 8.9 | 9 (09-27 08:02Z) |
| us-east-2 use2-az2 | 100 | 98% | 8.8 | 9 (09-27 01:21Z) |
| us-east-2 use2-az3 | 88 | 91% | 8.4 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az1 | 54 | 98% | 8.9 | 9 (09-27 08:02Z) |
| us-west-2 usw2-az2 | 45 | 98% | 8.8 | 9 (09-26 22:42Z) |
| us-west-2 usw2-az3 | 61 | 98% | 8.9 | 9 (09-26 17:05Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.728600 | 2026-09-27T08:02:10Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.858600 | 2026-09-27T08:02:10Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.825700 | 2026-09-27T08:02:10Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.008700 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592700 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.578000 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568100 | 2026-09-27T08:02:10Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-27T08:02:10Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.541200 | 2026-09-27T08:02:10Z |
| ap-south-1 | ap-south-1a | Windows | 0.342600 | 2026-09-27T08:02:10Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.544900 | 2026-09-27T08:02:10Z |
| ap-south-1 | ap-south-1b | Windows | 0.323600 | 2026-09-27T08:02:10Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.661000 | 2026-09-27T08:02:10Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.513700 | 2026-09-27T08:02:10Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.682100 | 2026-09-27T08:02:10Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.670400 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1a | Windows | 0.316300 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.499300 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.429100 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.405100 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.419600 | 2026-09-27T08:02:10Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.524200 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2a | Windows | 0.641000 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.526900 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2b | Windows | 0.641500 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.514900 | 2026-09-27T08:02:10Z |
| us-east-2 | us-east-2c | Windows | 0.638000 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.511300 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.483800 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2b | Windows | 0.332400 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.481400 | 2026-09-27T08:02:10Z |
| us-west-2 | us-west-2c | Windows | 0.331400 | 2026-09-27T08:02:10Z |
