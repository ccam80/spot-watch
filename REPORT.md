# Spot placement score log

Generated 2026-09-30 03:29 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 232 | 29% | 4.0 | 9 (09-30 03:29Z) |
| ap-northeast-1 | 232 | 9% | 2.4 | 1 (09-30 03:29Z) |
| ap-northeast-2 | 232 | 34% | 5.0 | 9 (09-30 03:29Z) |
| ap-south-1 | 232 | 3% | 1.9 | 1 (09-30 03:29Z) |
| ap-southeast-2 | 232 | 0% | 1.0 | 1 (09-30 03:29Z) |
| ap-southeast-3 | 232 | 21% | 3.4 | 1 (09-30 03:29Z) |
| us-east-1 | 232 | 7% | 2.4 | 9 (09-30 03:29Z) |
| us-east-2 | 232 | 20% | 3.1 | 1 (09-30 03:29Z) |
| us-west-2 | 232 | 9% | 2.3 | 1 (09-30 03:29Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        911149999999999999999999999999999999999999999999
ap-northeast-1   111111118989945589412212221112114818821379612221
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111211111111111111111111111111111111112211
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   111153687867556688891111111115437887681111187111
us-east-1        999991999111111121111129111112211122111112912229
us-east-2        999999999111111111111111119999999111111916999911
us-west-2        999999991111111111111122111111111122222111112111
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 2 | 5 | 7 | 7 | 3 | 3 | 3 | 6 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 | 4 | 6 | 3 | 4 | 5 | 3 | 5 | 4 |
| ap-northeast-1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 4 | 3 | 5 | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 2 |
| ap-northeast-2 | 3 | 7 | 9 | 8 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 4 | 3 | 2 | 3 | 4 | 7 | 6 | 4 | 5 | 4 | 6 | 4 | 2 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 |
| us-west-2 | 2 | 3 | 4 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 80 | 0% | 1.5 | 1 (09-30 02:34Z) |
| ap-east-1 ape1-az2 | 164 | 41% | 5.2 | 9 (09-30 03:29Z) |
| ap-northeast-1 apne1-az1 | 31 | 0% | 1.3 | 2 (09-29 13:28Z) |
| ap-northeast-1 apne1-az4 | 104 | 12% | 2.7 | 1 (09-30 02:34Z) |
| ap-northeast-2 apne2-az1 | 210 | 35% | 5.0 | 9 (09-30 03:29Z) |
| ap-northeast-2 apne2-az3 | 214 | 37% | 5.1 | 9 (09-30 03:29Z) |
| ap-northeast-2 apne2-az4 | 229 | 34% | 5.1 | 9 (09-30 03:29Z) |
| ap-south-1 aps1-az1 | 69 | 1% | 1.7 | 1 (09-30 03:29Z) |
| ap-south-1 aps1-az3 | 91 | 3% | 2.6 | 1 (09-30 01:01Z) |
| ap-southeast-2 apse2-az1 | 31 | 0% | 1.1 | 1 (09-29 04:27Z) |
| ap-southeast-2 apse2-az2 | 21 | 0% | 1.0 | 1 (09-29 16:27Z) |
| ap-southeast-3 apse3-az1 | 45 | 0% | 1.0 | 1 (09-30 02:34Z) |
| ap-southeast-3 apse3-az3 | 172 | 26% | 4.1 | 7 (09-30 01:01Z) |
| us-east-1 use1-az1 | 33 | 0% | 1.2 | 1 (09-29 22:22Z) |
| us-east-1 use1-az2 | 68 | 3% | 1.5 | 1 (09-30 02:34Z) |
| us-east-1 use1-az4 | 70 | 20% | 2.9 | 9 (09-30 03:29Z) |
| us-east-1 use1-az5 | 69 | 19% | 2.9 | 9 (09-30 03:29Z) |
| us-east-1 use1-az6 | 54 | 11% | 2.2 | 9 (09-30 03:29Z) |
| us-east-2 use2-az1 | 91 | 31% | 3.8 | 1 (09-30 03:29Z) |
| us-east-2 use2-az2 | 117 | 33% | 4.2 | 1 (09-30 02:34Z) |
| us-east-2 use2-az3 | 136 | 31% | 4.2 | 1 (09-30 02:34Z) |
| us-west-2 usw2-az1 | 75 | 27% | 3.7 | 1 (09-30 01:40Z) |
| us-west-2 usw2-az2 | 43 | 26% | 3.6 | 1 (09-29 01:00Z) |
| us-west-2 usw2-az3 | 103 | 17% | 3.0 | 1 (09-30 03:29Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 232 | 34% | 5.0 | 9 (09-30 03:29Z) |
| ap-northeast-1 | 232 | 75% | 7.3 | 3 (09-30 03:29Z) |
| ap-northeast-2 | 232 | 100% | 9.0 | 9 (09-30 03:29Z) |
| ap-south-1 | 232 | 58% | 6.3 | 9 (09-30 03:29Z) |
| ap-southeast-2 | 232 | 17% | 3.2 | 2 (09-30 03:29Z) |
| ap-southeast-3 | 232 | 21% | 3.4 | 1 (09-30 03:29Z) |
| us-east-1 | 232 | 75% | 6.9 | 9 (09-30 03:29Z) |
| us-east-2 | 232 | 75% | 7.3 | 9 (09-30 03:29Z) |
| us-west-2 | 232 | 55% | 5.9 | 3 (09-30 03:29Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   111113899999999999993335222333899999999999992223
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999321122999999999999999994217111529999999999999
ap-southeast-2   222222427949999322122222222222222959229221122222
ap-southeast-3   111153687867556688891111111115437887681111187111
us-east-1        999999999221234454336989579489959445443595936559
us-east-2        999999999922333322332239999999999334333999999999
us-west-2        999999999999443433224444229922449453555322435333
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 7 | 9 | 8 | 4 | 5 | 4 | 7 | 7 | 5 | 5 | 4 | 6 | 6 | 4 | 5 | 4 | 6 | 4 | 5 | 6 | 4 | 5 | 5 |
| ap-northeast-1 | 6 | 5 | 2 | 2 | 4 | 5 | 4 | 4 | 6 | 4 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 7 | 5 | 4 | 3 | 5 | 4 | 2 | 6 | 4 | 7 | 7 | 8 | 7 | 8 | 7 | 6 | 8 | 6 |
| ap-southeast-2 | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 3 | 5 | 2 | 3 | 3 | 4 | 6 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 5 | 6 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 5 | 4 |
| us-east-1 | 6 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | 6 | 6 | 5 | 6 | 6 | 5 | 6 | 6 | 6 | 7 | 7 |
| us-east-2 | 6 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 5 | 6 | 7 | 6 | 7 | 6 | 6 | 6 | 7 |
| us-west-2 | 5 | 5 | 5 | 4 | 6 | 6 | 9 | 7 | 7 | 5 | 8 | 7 | 9 | 8 | 6 | 8 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 122 | 56% | 6.3 | 9 (09-30 03:29Z) |
| ap-east-1 ape1-az2 | 94 | 56% | 6.4 | 9 (09-30 02:34Z) |
| ap-east-1 ape1-az3 | 91 | 52% | 6.1 | 9 (09-30 03:29Z) |
| ap-northeast-1 apne1-az1 | 108 | 93% | 8.5 | 9 (09-29 22:22Z) |
| ap-northeast-1 apne1-az2 | 44 | 41% | 5.5 | 9 (09-29 21:21Z) |
| ap-northeast-1 apne1-az4 | 138 | 99% | 8.9 | 9 (09-29 22:22Z) |
| ap-northeast-2 apne2-az1 | 180 | 100% | 9.0 | 9 (09-30 02:34Z) |
| ap-northeast-2 apne2-az2 | 52 | 73% | 7.3 | 9 (09-30 01:01Z) |
| ap-northeast-2 apne2-az3 | 207 | 100% | 9.0 | 9 (09-30 03:29Z) |
| ap-northeast-2 apne2-az4 | 117 | 60% | 6.6 | 9 (09-30 03:29Z) |
| ap-south-1 aps1-az1 | 71 | 69% | 7.1 | 9 (09-30 02:34Z) |
| ap-south-1 aps1-az2 | 84 | 57% | 6.4 | 9 (09-30 03:29Z) |
| ap-south-1 aps1-az3 | 94 | 81% | 7.9 | 9 (09-30 01:01Z) |
| ap-southeast-2 apse2-az1 | 22 | 55% | 6.2 | 9 (09-27 21:19Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 51 | 22% | 4.2 | 8 (09-29 14:24Z) |
| us-east-1 use1-az1 | 12 | 100% | 8.8 | 9 (09-20 11:17Z) |
| us-east-1 use1-az2 | 75 | 100% | 9.0 | 9 (09-28 11:22Z) |
| us-east-1 use1-az4 | 87 | 98% | 8.8 | 9 (09-30 03:29Z) |
| us-east-1 use1-az5 | 48 | 98% | 8.9 | 9 (09-29 22:22Z) |
| us-east-1 use1-az6 | 77 | 96% | 8.7 | 9 (09-30 03:29Z) |
| us-east-2 use2-az1 | 87 | 99% | 8.9 | 9 (09-30 03:29Z) |
| us-east-2 use2-az2 | 123 | 98% | 8.9 | 9 (09-30 03:29Z) |
| us-east-2 use2-az3 | 114 | 93% | 8.5 | 9 (09-30 03:29Z) |
| us-west-2 usw2-az1 | 63 | 98% | 8.9 | 9 (09-29 12:36Z) |
| us-west-2 usw2-az2 | 57 | 98% | 8.8 | 9 (09-28 12:37Z) |
| us-west-2 usw2-az3 | 72 | 99% | 8.9 | 9 (09-29 12:36Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.731300 | 2026-09-30T03:29:33Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.868200 | 2026-09-30T03:29:33Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.792900 | 2026-09-30T03:29:33Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.979100 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.594600 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577500 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.566900 | 2026-09-30T03:29:33Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743300 | 2026-09-30T03:29:33Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.604100 | 2026-09-30T03:29:33Z |
| ap-south-1 | ap-south-1a | Windows | 0.351500 | 2026-09-30T03:29:33Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.634100 | 2026-09-30T03:29:33Z |
| ap-south-1 | ap-south-1b | Windows | 0.343000 | 2026-09-30T03:29:33Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.719800 | 2026-09-30T03:29:33Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.497900 | 2026-09-30T03:29:33Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.631800 | 2026-09-30T03:29:33Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.596300 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1a | Windows | 0.305200 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.459800 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.445700 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.398600 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.438300 | 2026-09-30T03:29:33Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.530800 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2a | Windows | 0.640800 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.524300 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2b | Windows | 0.640600 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515000 | 2026-09-30T03:29:33Z |
| us-east-2 | us-east-2c | Windows | 0.637700 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.513300 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2a | Windows | 0.332500 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.503800 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2b | Windows | 0.332400 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.486600 | 2026-09-30T03:29:33Z |
| us-west-2 | us-west-2c | Windows | 0.331200 | 2026-09-30T03:29:33Z |
