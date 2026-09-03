# Spot placement score log

Generated 2026-09-03 00:07 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 33 | 0% | 1.0 | 1 (09-03 00:06Z) |
| ap-northeast-1 | 33 | 0% | 1.6 | 2 (09-03 00:06Z) |
| ap-northeast-2 | 33 | 0% | 2.9 | 3 (09-03 00:06Z) |
| ap-south-1 | 33 | 0% | 2.2 | 3 (09-03 00:06Z) |
| ap-southeast-2 | 33 | 0% | 1.0 | 1 (09-03 00:06Z) |
| ap-southeast-3 | 33 | 0% | 2.5 | 3 (09-03 00:06Z) |
| us-east-1 | 33 | 0% | 1.5 | 1 (09-03 00:06Z) |
| us-east-2 | 33 | 0% | 1.3 | 1 (09-03 00:06Z) |
| us-west-2 | 33 | 0% | 1.5 | 2 (09-03 00:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                       111111111111111111111111111111111
ap-northeast-1                  111311333313313111131111111113112
ap-northeast-2                  333333333333333333333333331133333
ap-south-1                      333131333333313333111311131222133
ap-southeast-2                  111111111111111111111111111111111
ap-southeast-3                  333333332323211132112333333333333
us-east-1                       323332111131111113121111111111111
us-east-2                       111113113111133111111111111131111
us-west-2                       221222113111113133311111111111112
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-northeast-1 | 1 | 3 | · | 1 | 2 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| ap-northeast-2 | 3 | 3 | · | 3 | 2 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| ap-south-1 | 3 | 3 | · | 3 | 2 | · | 1 | · | 1 | 2 | · | 2 | 1 | · | 2 | 1 | 3 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 1 | 1 | · | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 3 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 2 | 1 | · | 3 | 1 | · | 1 | · | 1 | 1 | · | 2 | 1 | · | 2 | 2 | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 2 |
| us-east-2 | 1 | 1 | · | 1 | 1 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| us-west-2 | 2 | 1 | · | 1 | 1 | · | 2 | · | 1 | 1 | · | 2 | 1 | · | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 15 | 0% | 1.0 | 1 (09-02 14:23Z) |
| ap-east-1 ape1-az2 | 7 | 0% | 1.0 | 1 (09-03 00:06Z) |
| ap-northeast-1 apne1-az1 | 7 | 0% | 1.3 | 1 (09-03 00:06Z) |
| ap-northeast-1 apne1-az4 | 21 | 0% | 2.0 | 3 (09-02 14:23Z) |
| ap-northeast-2 apne2-az1 | 29 | 0% | 2.9 | 3 (09-03 00:06Z) |
| ap-northeast-2 apne2-az3 | 29 | 0% | 2.9 | 3 (09-03 00:06Z) |
| ap-northeast-2 apne2-az4 | 32 | 0% | 2.9 | 3 (09-03 00:06Z) |
| ap-south-1 aps1-az1 | 12 | 0% | 1.9 | 1 (09-02 04:21Z) |
| ap-south-1 aps1-az3 | 22 | 0% | 2.7 | 3 (09-03 00:06Z) |
| ap-southeast-2 apse2-az1 | 7 | 0% | 1.0 | 1 (09-03 00:06Z) |
| ap-southeast-2 apse2-az2 | 4 | 0% | 1.0 | 1 (09-03 00:06Z) |
| ap-southeast-3 apse3-az1 | 11 | 0% | 1.0 | 1 (09-02 09:31Z) |
| ap-southeast-3 apse3-az3 | 27 | 0% | 2.9 | 3 (09-03 00:06Z) |
| us-east-1 use1-az1 | 6 | 0% | 1.0 | 1 (09-02 21:46Z) |
| us-east-1 use1-az2 | 18 | 0% | 1.1 | 1 (09-02 14:23Z) |
| us-east-1 use1-az4 | 7 | 0% | 1.6 | 1 (09-02 21:46Z) |
| us-east-1 use1-az5 | 10 | 0% | 1.4 | 1 (09-02 18:36Z) |
| us-east-1 use1-az6 | 15 | 0% | 1.3 | 1 (09-02 14:23Z) |
| us-east-2 use2-az1 | 3 | 0% | 1.7 | 3 (08-29 11:36Z) |
| us-east-2 use2-az2 | 11 | 0% | 1.2 | 1 (09-02 14:23Z) |
| us-east-2 use2-az3 | 9 | 0% | 2.0 | 1 (09-02 18:36Z) |
| us-west-2 usw2-az1 | 8 | 0% | 1.8 | 1 (09-01 23:15Z) |
| us-west-2 usw2-az2 | 6 | 0% | 1.3 | 1 (09-03 00:06Z) |
| us-west-2 usw2-az3 | 14 | 0% | 1.6 | 1 (09-02 21:46Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 33 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-northeast-1 | 33 | 82% | 7.5 | 9 (09-03 00:06Z) |
| ap-northeast-2 | 33 | 100% | 9.0 | 9 (09-03 00:06Z) |
| ap-south-1 | 33 | 0% | 2.8 | 3 (09-03 00:06Z) |
| ap-southeast-2 | 33 | 30% | 3.6 | 1 (09-03 00:06Z) |
| ap-southeast-3 | 33 | 0% | 2.5 | 3 (09-03 00:06Z) |
| us-east-1 | 33 | 67% | 6.0 | 3 (09-03 00:06Z) |
| us-east-2 | 33 | 61% | 6.0 | 3 (09-03 00:06Z) |
| us-west-2 | 33 | 39% | 5.0 | 2 (09-03 00:06Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1                       333333333333333333333333333333333
ap-northeast-1                  991999999999999999199119999119999
ap-northeast-2                  999999999999999999999999999999999
ap-south-1                      333133333333333333133311333333333
ap-southeast-2                  111111979999999931111112311111311
ap-southeast-3                  333333332323211132112333333333333
us-east-1                       766787589999999999941191121992113
us-east-2                       929919299999199221911199999999113
us-west-2                       442439219222299999991299244929212
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 3 | · | 3 | 3 | · | 3 | · | 3 | 3 | · | 3 | 3 | · | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-northeast-1 | 6 | 9 | · | 1 | 5 | · | 1 | · | 9 | 1 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 3 | 3 | · | 3 | 3 | · | 1 | · | 3 | 3 | · | 3 | 1 | · | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| ap-southeast-2 | 1 | 9 | · | 1 | 4 | · | 1 | · | 9 | 1 | · | 5 | 2 | · | 4 | 1 | 9 | 3 | 6 | 9 | 1 | 2 | 6 | 1 |
| ap-southeast-3 | 3 | 2 | · | 3 | 3 | · | 2 | · | 1 | 3 | · | 2 | 3 | · | 2 | 1 | 3 | 3 | 2 | 2 | 2 | 3 | 3 | 3 |
| us-east-1 | 4 | 9 | · | 6 | 8 | · | 9 | · | 9 | 9 | · | 8 | 1 | · | 6 | 4 | 9 | 1 | 5 | 9 | 2 | 6 | 7 | 4 |
| us-east-2 | 2 | 1 | · | 9 | 9 | · | 9 | · | 9 | 9 | · | 9 | 9 | · | 9 | 1 | 9 | 9 | 2 | 9 | 5 | 4 | 4 | 5 |
| us-west-2 | 4 | 2 | · | 2 | 5 | · | 9 | · | 9 | 2 | · | 9 | 9 | · | 7 | 9 | 2 | 2 | 6 | 2 | 2 | 5 | 3 | 4 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 17 | 0% | 3.0 | 3 (09-02 21:46Z) |
| ap-east-1 ape1-az2 | 11 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-east-1 ape1-az3 | 12 | 0% | 3.0 | 3 (09-02 21:46Z) |
| ap-northeast-1 apne1-az1 | 7 | 57% | 6.4 | 3 (09-02 21:46Z) |
| ap-northeast-1 apne1-az2 | 12 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-northeast-1 apne1-az4 | 25 | 100% | 9.0 | 9 (09-03 00:06Z) |
| ap-northeast-2 apne2-az1 | 32 | 100% | 9.0 | 9 (09-03 00:06Z) |
| ap-northeast-2 apne2-az2 | 1 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-northeast-2 apne2-az3 | 32 | 100% | 9.0 | 9 (09-03 00:06Z) |
| ap-northeast-2 apne2-az4 | 16 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-south-1 aps1-az1 | 5 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-south-1 aps1-az2 | 16 | 0% | 3.0 | 3 (09-02 21:46Z) |
| ap-south-1 aps1-az3 | 8 | 0% | 3.0 | 3 (09-03 00:06Z) |
| ap-southeast-2 apse2-az1 | 4 | 75% | 7.0 | 3 (08-30 01:12Z) |
| ap-southeast-2 apse2-az3 | 1 | 0% | 3.0 | 3 (09-02 18:36Z) |
| ap-southeast-3 apse3-az3 | 15 | 0% | 3.0 | 3 (09-03 00:06Z) |
| us-east-1 use1-az1 | 2 | 100% | 7.5 | 6 (08-29 19:41Z) |
| us-east-1 use1-az2 | 10 | 100% | 9.0 | 9 (09-02 04:21Z) |
| us-east-1 use1-az4 | 9 | 100% | 9.0 | 9 (09-02 04:21Z) |
| us-east-1 use1-az5 | 12 | 100% | 9.0 | 9 (09-02 09:31Z) |
| us-east-1 use1-az6 | 11 | 100% | 9.0 | 9 (08-31 06:58Z) |
| us-east-2 use2-az1 | 11 | 100% | 8.9 | 9 (09-02 14:23Z) |
| us-east-2 use2-az2 | 18 | 89% | 8.2 | 9 (09-02 14:23Z) |
| us-east-2 use2-az3 | 11 | 73% | 7.0 | 3 (09-02 09:31Z) |
| us-west-2 usw2-az1 | 11 | 91% | 8.5 | 9 (09-02 14:23Z) |
| us-west-2 usw2-az2 | 9 | 100% | 9.0 | 9 (09-01 06:12Z) |
| us-west-2 usw2-az3 | 12 | 100% | 9.0 | 9 (09-02 14:23Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.752500 | 2026-09-03T00:06:57Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.329900 | 2026-09-03T00:06:57Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.835200 | 2026-09-03T00:06:57Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.376500 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.353200 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.307700 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.289600 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.307700 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.275100 | 2026-09-03T00:06:57Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.307700 | 2026-09-03T00:06:57Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.535200 | 2026-09-03T00:06:57Z |
| ap-south-1 | ap-south-1a | Windows | 0.304800 | 2026-09-03T00:06:57Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.476000 | 2026-09-03T00:06:57Z |
| ap-south-1 | ap-south-1b | Windows | 0.304800 | 2026-09-03T00:06:57Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.747600 | 2026-09-03T00:06:57Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.475700 | 2026-09-03T00:06:57Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.917000 | 2026-09-03T00:06:57Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.377100 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.937100 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1a | Windows | 0.339300 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.708800 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1b | Windows | 0.321500 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.590700 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1c | Windows | 0.318700 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.491800 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1d | Windows | 0.323100 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.522400 | 2026-09-03T00:06:57Z |
| us-east-1 | us-east-1f | Windows | 0.318100 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.370400 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2a | Windows | 0.284600 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.361200 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2b | Windows | 0.284600 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.352200 | 2026-09-03T00:06:57Z |
| us-east-2 | us-east-2c | Windows | 0.284600 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.566700 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2a | Windows | 0.284600 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.527200 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2b | Windows | 0.284600 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.528800 | 2026-09-03T00:06:57Z |
| us-west-2 | us-west-2c | Windows | 0.331800 | 2026-09-03T00:06:57Z |
