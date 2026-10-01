# Spot placement score log

Generated 2026-10-01 17:00 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 256 | 33% | 4.3 | 3 (10-01 17:00Z) |
| ap-northeast-1 | 256 | 11% | 2.5 | 9 (10-01 17:00Z) |
| ap-northeast-2 | 256 | 40% | 5.4 | 9 (10-01 17:00Z) |
| ap-south-1 | 256 | 2% | 1.8 | 1 (10-01 17:00Z) |
| ap-southeast-2 | 256 | 0% | 1.0 | 1 (10-01 17:00Z) |
| ap-southeast-3 | 256 | 21% | 3.3 | 9 (10-01 17:00Z) |
| us-east-1 | 256 | 8% | 2.4 | 2 (10-01 17:00Z) |
| us-east-2 | 256 | 23% | 3.3 | 9 (10-01 17:00Z) |
| us-west-2 | 256 | 9% | 2.2 | 2 (10-01 17:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999899999111111993
ap-northeast-1   221112114818821379612221222222111189912799812129
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111111111111112211111111111111111111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111115437887681111187111111111111147651611111199
us-east-1        111112211122111112912229999132222222223222221192
us-east-2        119999999111111916999911199999991111181712189999
us-west-2        111111111122222111112111111211222222222221211122
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 8 | 7 | 3 | 4 | 4 | 6 | 6 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 4 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 1 | 2 | 4 | 2 | 4 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 88 | 0% | 1.4 | 1 (10-01 01:09Z) |
| ap-east-1 ape1-az2 | 184 | 46% | 5.4 | 2 (10-01 17:00Z) |
| ap-northeast-1 apne1-az1 | 36 | 0% | 1.3 | 2 (10-01 17:00Z) |
| ap-northeast-1 apne1-az4 | 117 | 17% | 3.0 | 8 (10-01 17:00Z) |
| ap-northeast-2 apne2-az1 | 230 | 40% | 5.3 | 9 (10-01 17:00Z) |
| ap-northeast-2 apne2-az3 | 238 | 43% | 5.5 | 9 (10-01 17:00Z) |
| ap-northeast-2 apne2-az4 | 253 | 41% | 5.4 | 9 (10-01 17:00Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 98 | 3% | 2.5 | 1 (09-30 23:20Z) |
| ap-southeast-2 apse2-az1 | 36 | 0% | 1.1 | 1 (09-30 18:27Z) |
| ap-southeast-2 apse2-az2 | 25 | 0% | 1.0 | 1 (09-30 23:20Z) |
| ap-southeast-3 apse3-az1 | 51 | 0% | 1.0 | 1 (10-01 02:39Z) |
| ap-southeast-3 apse3-az3 | 184 | 28% | 4.1 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 38 | 0% | 1.2 | 1 (09-30 13:26Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 78 | 23% | 3.1 | 9 (10-01 10:01Z) |
| us-east-1 use1-az5 | 79 | 20% | 2.9 | 1 (10-01 01:09Z) |
| us-east-1 use1-az6 | 60 | 15% | 2.5 | 9 (10-01 10:01Z) |
| us-east-2 use2-az1 | 101 | 33% | 4.0 | 9 (10-01 10:01Z) |
| us-east-2 use2-az2 | 130 | 38% | 4.6 | 9 (10-01 17:00Z) |
| us-east-2 use2-az3 | 153 | 37% | 4.6 | 9 (10-01 17:00Z) |
| us-west-2 usw2-az1 | 81 | 25% | 3.5 | 1 (10-01 02:39Z) |
| us-west-2 usw2-az2 | 49 | 22% | 3.3 | 1 (10-01 17:00Z) |
| us-west-2 usw2-az3 | 106 | 17% | 2.9 | 1 (09-30 19:21Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 256 | 40% | 5.4 | 9 (10-01 17:00Z) |
| ap-northeast-1 | 256 | 73% | 7.2 | 9 (10-01 17:00Z) |
| ap-northeast-2 | 256 | 100% | 9.0 | 9 (10-01 17:00Z) |
| ap-south-1 | 256 | 57% | 6.1 | 9 (10-01 17:00Z) |
| ap-southeast-2 | 256 | 15% | 3.1 | 2 (10-01 17:00Z) |
| ap-southeast-3 | 256 | 21% | 3.3 | 9 (10-01 17:00Z) |
| us-east-1 | 256 | 71% | 6.7 | 4 (10-01 17:00Z) |
| us-east-2 | 256 | 75% | 7.3 | 9 (10-01 17:00Z) |
| us-west-2 | 256 | 53% | 5.7 | 3 (10-01 17:00Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   222333899999999999992223322344379999999999992249
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       994217111529999999999999991111111111119929999929
ap-southeast-2   222222222959229221122222222222222222222222222222
ap-southeast-3   111115437887681111187111111111111147651611111199
us-east-1        579489959445443595936559999365544433344333445594
us-east-2        999999999334333999999999999999998329299835999999
us-west-2        229922449453555322435333242534554554444454443393
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 6 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 6 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 3 | 3 | 4 | 3 | 2 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 6 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 4 | 3 | 4 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 4 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 145 | 63% | 6.8 | 9 (10-01 17:00Z) |
| ap-east-1 ape1-az2 | 117 | 65% | 6.9 | 9 (10-01 17:00Z) |
| ap-east-1 ape1-az3 | 112 | 61% | 6.6 | 9 (10-01 02:39Z) |
| ap-northeast-1 apne1-az1 | 121 | 92% | 8.5 | 9 (10-01 17:00Z) |
| ap-northeast-1 apne1-az2 | 56 | 54% | 6.2 | 9 (09-30 23:20Z) |
| ap-northeast-1 apne1-az4 | 151 | 99% | 9.0 | 9 (10-01 17:00Z) |
| ap-northeast-2 apne2-az1 | 200 | 100% | 9.0 | 9 (10-01 10:01Z) |
| ap-northeast-2 apne2-az2 | 54 | 74% | 7.4 | 9 (09-30 17:22Z) |
| ap-northeast-2 apne2-az3 | 229 | 100% | 9.0 | 9 (10-01 10:01Z) |
| ap-northeast-2 apne2-az4 | 139 | 66% | 7.0 | 9 (10-01 17:00Z) |
| ap-south-1 aps1-az1 | 77 | 71% | 7.3 | 9 (10-01 17:00Z) |
| ap-south-1 aps1-az2 | 92 | 61% | 6.6 | 9 (10-01 17:00Z) |
| ap-south-1 aps1-az3 | 100 | 82% | 7.9 | 9 (10-01 17:00Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 91 | 97% | 8.8 | 9 (10-01 10:01Z) |
| us-east-1 use1-az5 | 52 | 98% | 8.9 | 9 (10-01 10:01Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 95 | 99% | 8.9 | 9 (10-01 02:39Z) |
| us-east-2 use2-az2 | 134 | 99% | 8.9 | 9 (10-01 10:01Z) |
| us-east-2 use2-az3 | 123 | 93% | 8.6 | 9 (10-01 17:00Z) |
| us-west-2 usw2-az1 | 64 | 98% | 8.9 | 9 (10-01 10:01Z) |
| us-west-2 usw2-az2 | 59 | 95% | 8.6 | 2 (09-30 12:38Z) |
| us-west-2 usw2-az3 | 76 | 95% | 8.6 | 9 (10-01 10:01Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.733700 | 2026-10-01T17:00:01Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.869700 | 2026-10-01T17:00:01Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.792400 | 2026-10-01T17:00:01Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.975500 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.592100 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.576600 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565400 | 2026-10-01T17:00:01Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743400 | 2026-10-01T17:00:01Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.638300 | 2026-10-01T17:00:01Z |
| ap-south-1 | ap-south-1a | Windows | 0.353900 | 2026-10-01T17:00:01Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.692300 | 2026-10-01T17:00:01Z |
| ap-south-1 | ap-south-1b | Windows | 0.356600 | 2026-10-01T17:00:01Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.729700 | 2026-10-01T17:00:01Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.501400 | 2026-10-01T17:00:01Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.595700 | 2026-10-01T17:00:01Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.557500 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1a | Windows | 0.299800 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.442100 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.446900 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.397100 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.441700 | 2026-10-01T17:00:01Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.531600 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2a | Windows | 0.641800 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.522300 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2b | Windows | 0.641200 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.513600 | 2026-10-01T17:00:01Z |
| us-east-2 | us-east-2c | Windows | 0.637600 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.509900 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2a | Windows | 0.332300 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.500300 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2b | Windows | 0.332000 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486200 | 2026-10-01T17:00:01Z |
| us-west-2 | us-west-2c | Windows | 0.331200 | 2026-10-01T17:00:01Z |
