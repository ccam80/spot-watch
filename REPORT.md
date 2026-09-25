# Spot placement score log

Generated 2026-09-25 18:30 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 164 | 5% | 2.4 | 1 (09-25 18:30Z) |
| ap-northeast-1 | 164 | 0% | 2.0 | 4 (09-25 18:30Z) |
| ap-northeast-2 | 164 | 7% | 3.4 | 9 (09-25 18:30Z) |
| ap-south-1 | 164 | 0% | 1.9 | 1 (09-25 18:30Z) |
| ap-southeast-2 | 164 | 0% | 1.0 | 1 (09-25 18:30Z) |
| ap-southeast-3 | 164 | 6% | 2.9 | 8 (09-25 18:30Z) |
| us-east-1 | 164 | 0% | 2.0 | 2 (09-25 18:30Z) |
| us-east-2 | 164 | 2% | 2.0 | 2 (09-25 18:30Z) |
| us-west-2 | 164 | 0% | 1.7 | 1 (09-25 18:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333399999999911
ap-northeast-1   122221112212233223123221121221332222332222221134
ap-northeast-2   333333333333333333333333333333333333399999999999
ap-south-1       113333113121133333333332111111111111111111112111
ap-southeast-2   111111111111111111111111113111111111111111111111
ap-southeast-3   313131123333333333313333133313333333399689995198
us-east-1        232231231112131122333333331321223232222123211312
us-east-2        333333133113333123333331331111211311319291121992
us-west-2        131221311123333333333333331211222213222112222111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 4 | · | 1 | 2 | 3 | 2 | 5 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 1 | 3 | 2 |
| ap-northeast-1 | 2 | 2 | · | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-northeast-2 | 3 | 4 | · | 3 | 3 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 3 |
| ap-south-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | · | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 2 | 2 | · | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |
| us-east-2 | 2 | 1 | · | 1 | 2 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| us-west-2 | 2 | 2 | · | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 54 | 0% | 1.4 | 1 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 104 | 9% | 3.0 | 9 (09-25 07:40Z) |
| ap-northeast-1 apne1-az1 | 21 | 0% | 1.2 | 2 (09-25 13:39Z) |
| ap-northeast-1 apne1-az4 | 77 | 0% | 2.1 | 1 (09-25 18:30Z) |
| ap-northeast-2 apne2-az1 | 147 | 7% | 3.4 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az3 | 146 | 8% | 3.4 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az4 | 161 | 7% | 3.4 | 9 (09-25 18:30Z) |
| ap-south-1 aps1-az1 | 58 | 0% | 1.7 | 1 (09-23 05:52Z) |
| ap-south-1 aps1-az3 | 81 | 0% | 2.5 | 1 (09-25 18:30Z) |
| ap-southeast-2 apse2-az1 | 26 | 0% | 1.2 | 1 (09-22 09:52Z) |
| ap-southeast-2 apse2-az2 | 19 | 0% | 1.0 | 1 (09-23 00:22Z) |
| ap-southeast-3 apse3-az1 | 38 | 0% | 1.0 | 1 (09-25 01:25Z) |
| ap-southeast-3 apse3-az3 | 128 | 8% | 3.3 | 8 (09-25 18:30Z) |
| us-east-1 use1-az1 | 19 | 0% | 1.3 | 1 (09-23 05:52Z) |
| us-east-1 use1-az2 | 56 | 0% | 1.3 | 1 (09-25 18:30Z) |
| us-east-1 use1-az4 | 35 | 0% | 1.7 | 1 (09-23 05:52Z) |
| us-east-1 use1-az5 | 50 | 0% | 1.5 | 1 (09-25 01:25Z) |
| us-east-1 use1-az6 | 48 | 0% | 1.4 | 3 (09-21 23:13Z) |
| us-east-2 use2-az1 | 53 | 4% | 2.1 | 9 (09-25 13:39Z) |
| us-east-2 use2-az2 | 72 | 3% | 2.1 | 1 (09-25 18:30Z) |
| us-east-2 use2-az3 | 90 | 4% | 2.5 | 9 (09-25 13:39Z) |
| us-west-2 usw2-az1 | 50 | 0% | 2.0 | 1 (09-25 18:30Z) |
| us-west-2 usw2-az2 | 28 | 0% | 2.0 | 3 (09-23 11:25Z) |
| us-west-2 usw2-az3 | 79 | 0% | 1.8 | 1 (09-23 16:48Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 164 | 7% | 3.4 | 9 (09-25 18:30Z) |
| ap-northeast-1 | 164 | 79% | 7.6 | 9 (09-25 18:30Z) |
| ap-northeast-2 | 164 | 100% | 9.0 | 9 (09-25 18:30Z) |
| ap-south-1 | 164 | 49% | 5.8 | 9 (09-25 18:30Z) |
| ap-southeast-2 | 164 | 9% | 2.8 | 9 (09-25 18:30Z) |
| ap-southeast-3 | 164 | 6% | 2.9 | 8 (09-25 18:30Z) |
| us-east-1 | 164 | 75% | 6.9 | 4 (09-25 18:30Z) |
| us-east-2 | 164 | 76% | 7.3 | 9 (09-25 18:30Z) |
| us-west-2 | 164 | 55% | 5.8 | 3 (09-25 18:30Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        333333333333333333333333333333333333399999999999
ap-northeast-1   199993399999999999999999999999999999999349992199
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       939999239999999999999999919992499983999928999899
ap-southeast-2   233222233233333333333332233122222223351229922299
ap-southeast-3   313131123333333333313333133313333333399689995198
us-east-1        995699994549999999999999994999445999666995459834
us-east-2        999999999119999199999999993399599999949992348999
us-west-2        994459533459999999999999994319545499555955445993
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 4 | · | 3 | 4 | 3 | 3 | 5 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 |
| ap-northeast-1 | 6 | 6 | · | 1 | 4 | 6 | 5 | 3 | 9 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | · | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 8 | · | 3 | 5 | 8 | 7 | 6 | 3 | 2 | 7 | 4 | 2 | 5 | 4 | 5 | 6 | 7 | 7 | 7 | 6 | 5 | 7 | 5 |
| ap-southeast-2 | 2 | 4 | · | 1 | 2 | 2 | 2 | 2 | 6 | 2 | 2 | 3 | 2 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 2 | 2 | 3 | 2 |
| ap-southeast-3 | 3 | 3 | · | 3 | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 |
| us-east-1 | 6 | 8 | · | 6 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 9 | 5 | 5 | 6 | 6 | 6 | 6 | 5 | 6 | 6 | 6 | 6 | 7 |
| us-east-2 | 6 | 6 | · | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 6 | 7 | 9 | 6 | 7 | 6 | 6 | 6 | 6 |
| us-west-2 | 5 | 4 | · | 2 | 6 | 7 | 9 | 6 | 6 | 5 | 9 | 7 | 9 | 7 | 6 | 9 | 6 | 7 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 62 | 13% | 3.8 | 9 (09-25 18:30Z) |
| ap-east-1 ape1-az2 | 48 | 15% | 3.9 | 9 (09-25 13:39Z) |
| ap-east-1 ape1-az3 | 52 | 15% | 3.9 | 9 (09-25 18:30Z) |
| ap-northeast-1 apne1-az1 | 88 | 91% | 8.4 | 9 (09-25 13:39Z) |
| ap-northeast-1 apne1-az2 | 30 | 13% | 3.8 | 9 (09-25 18:30Z) |
| ap-northeast-1 apne1-az4 | 110 | 100% | 9.0 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az1 | 146 | 100% | 9.0 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az2 | 22 | 41% | 5.5 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az3 | 149 | 100% | 9.0 | 9 (09-25 18:30Z) |
| ap-northeast-2 apne2-az4 | 56 | 16% | 4.0 | 9 (09-25 07:40Z) |
| ap-south-1 aps1-az1 | 52 | 58% | 6.5 | 9 (09-24 22:18Z) |
| ap-south-1 aps1-az2 | 42 | 14% | 3.9 | 9 (09-25 13:39Z) |
| ap-south-1 aps1-az3 | 71 | 75% | 7.5 | 9 (09-25 18:30Z) |
| ap-southeast-2 apse2-az1 | 14 | 29% | 4.6 | 9 (09-25 18:30Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 16 | 25% | 4.5 | 9 (09-25 18:30Z) |
| ap-southeast-3 apse3-az3 | 45 | 11% | 3.7 | 9 (09-25 13:39Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 62 | 100% | 9.0 | 9 (09-23 05:52Z) |
| us-east-1 use1-az4 | 66 | 97% | 8.8 | 9 (09-25 01:25Z) |
| us-east-1 use1-az5 | 32 | 97% | 8.8 | 9 (09-24 09:55Z) |
| us-east-1 use1-az6 | 64 | 100% | 9.0 | 9 (09-25 01:25Z) |
| us-east-2 use2-az1 | 63 | 98% | 8.9 | 9 (09-24 09:55Z) |
| us-east-2 use2-az2 | 98 | 98% | 8.8 | 9 (09-24 09:55Z) |
| us-east-2 use2-az3 | 85 | 91% | 8.4 | 9 (09-25 13:39Z) |
| us-west-2 usw2-az1 | 51 | 98% | 8.9 | 9 (09-23 11:25Z) |
| us-west-2 usw2-az2 | 43 | 98% | 8.8 | 9 (09-25 07:40Z) |
| us-west-2 usw2-az3 | 60 | 98% | 8.9 | 9 (09-25 13:39Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.726400 | 2026-09-25T18:30:46Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.858900 | 2026-09-25T18:30:46Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.832400 | 2026-09-25T18:30:46Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 1.016500 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.591200 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577700 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.568000 | 2026-09-25T18:30:46Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-25T18:30:46Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.519700 | 2026-09-25T18:30:46Z |
| ap-south-1 | ap-south-1a | Windows | 0.330200 | 2026-09-25T18:30:46Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.501700 | 2026-09-25T18:30:46Z |
| ap-south-1 | ap-south-1b | Windows | 0.311800 | 2026-09-25T18:30:46Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.642800 | 2026-09-25T18:30:46Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.515300 | 2026-09-25T18:30:46Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.741600 | 2026-09-25T18:30:46Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.571800 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.716700 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1a | Windows | 0.326300 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.523800 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1b | Windows | 0.289900 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.435000 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.423100 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.429200 | 2026-09-25T18:30:46Z |
| us-east-1 | us-east-1f | Windows | 0.289700 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.525900 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2a | Windows | 0.640700 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.526700 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2b | Windows | 0.642400 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513100 | 2026-09-25T18:30:46Z |
| us-east-2 | us-east-2c | Windows | 0.637900 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513400 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2a | Windows | 0.332800 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.485700 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2b | Windows | 0.332700 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486500 | 2026-09-25T18:30:46Z |
| us-west-2 | us-west-2c | Windows | 0.331700 | 2026-09-25T18:30:46Z |
