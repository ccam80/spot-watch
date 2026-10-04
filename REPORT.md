# Spot placement score log

Generated 2026-10-04 00:32 UTC. Scores are 1–10; a region counts as available at ≥ 5. The single-type set is scored low by design (EC2 wants three or more instance types); read it relative to itself over time and use the trio set as the calibrated reference.

## g5.xlarge (g5.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 267 | 34% | 4.3 | 9 (10-04 00:31Z) |
| ap-northeast-1 | 267 | 14% | 2.7 | 9 (10-04 00:31Z) |
| ap-northeast-2 | 267 | 43% | 5.5 | 9 (10-04 00:31Z) |
| ap-south-1 | 267 | 2% | 1.8 | 1 (10-04 00:31Z) |
| ap-southeast-2 | 267 | 0% | 1.0 | 1 (10-04 00:31Z) |
| ap-southeast-3 | 267 | 21% | 3.3 | 1 (10-04 00:31Z) |
| us-east-1 | 267 | 9% | 2.5 | 9 (10-04 00:31Z) |
| us-east-2 | 267 | 26% | 3.5 | 9 (10-04 00:31Z) |
| us-west-2 | 267 | 10% | 2.3 | 9 (10-04 00:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999989999911111199399119119999
ap-northeast-1   882137961222122222211118991279981212982199999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       111111111221111111111111111111111111112111111111
ap-southeast-2   111111111111111111111111111111111111111111111111
ap-southeast-3   768111118711111111111114765161111119991141111111
us-east-1        211111291222999913222222222322222119229222331199
us-east-2        111191699991119999999111118171218999999991199999
us-west-2        222211111211111121122222222222121112221212999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 3 | 5 | 8 | 7 | 3 | 4 | 3 | 6 | 5 | 4 | 6 | 4 | 6 | 5 | 4 | 5 | 4 | 6 | 3 | 4 | 5 | 4 | 5 | 4 |
| ap-northeast-1 | 3 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 4 | 4 | 3 | 6 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 2 |
| ap-northeast-2 | 4 | 7 | 9 | 8 | 4 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-south-1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| ap-southeast-2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 2 | 3 | 2 | 6 | 3 | 4 | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| us-east-2 | 2 | 5 | 5 | 3 | 2 | 4 | 5 | 7 | 7 | 4 | 6 | 4 | 5 | 4 | 2 | 2 | 2 | 5 | 2 | 4 | 2 | 3 | 3 | 3 |
| us-west-2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 2 | 2 |

![g5.xlarge heatmap](report/heatmap-g5.xlarge.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 89 | 0% | 1.4 | 1 (10-02 08:24Z) |
| ap-east-1 ape1-az2 | 190 | 48% | 5.6 | 9 (10-03 21:08Z) |
| ap-northeast-1 apne1-az1 | 41 | 7% | 1.8 | 2 (10-03 17:12Z) |
| ap-northeast-1 apne1-az4 | 127 | 23% | 3.4 | 9 (10-04 00:31Z) |
| ap-northeast-2 apne2-az1 | 238 | 42% | 5.4 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az3 | 249 | 46% | 5.7 | 9 (10-04 00:31Z) |
| ap-northeast-2 apne2-az4 | 264 | 43% | 5.6 | 9 (10-04 00:31Z) |
| ap-south-1 aps1-az1 | 72 | 1% | 1.7 | 1 (09-30 14:26Z) |
| ap-south-1 aps1-az3 | 100 | 3% | 2.5 | 1 (10-02 20:39Z) |
| ap-southeast-2 apse2-az1 | 37 | 0% | 1.1 | 1 (10-03 00:24Z) |
| ap-southeast-2 apse2-az2 | 28 | 0% | 1.0 | 1 (10-03 00:24Z) |
| ap-southeast-3 apse3-az1 | 52 | 0% | 1.0 | 1 (10-03 17:12Z) |
| ap-southeast-3 apse3-az3 | 188 | 28% | 4.1 | 1 (10-03 00:24Z) |
| us-east-1 use1-az1 | 40 | 0% | 1.1 | 1 (10-02 20:39Z) |
| us-east-1 use1-az2 | 73 | 3% | 1.5 | 1 (09-30 21:21Z) |
| us-east-1 use1-az4 | 81 | 25% | 3.3 | 9 (10-03 21:08Z) |
| us-east-1 use1-az5 | 84 | 23% | 3.1 | 9 (10-04 00:31Z) |
| us-east-1 use1-az6 | 63 | 17% | 2.7 | 9 (10-04 00:31Z) |
| us-east-2 use2-az1 | 106 | 36% | 4.2 | 9 (10-04 00:31Z) |
| us-east-2 use2-az2 | 138 | 42% | 4.8 | 9 (10-04 00:31Z) |
| us-east-2 use2-az3 | 162 | 40% | 4.8 | 9 (10-04 00:31Z) |
| us-west-2 usw2-az1 | 86 | 28% | 3.8 | 9 (10-04 00:31Z) |
| us-west-2 usw2-az2 | 51 | 24% | 3.4 | 9 (10-03 12:27Z) |
| us-west-2 usw2-az3 | 111 | 19% | 3.1 | 9 (10-04 00:31Z) |

## g-xlarge-trio (g5.xlarge, g4dn.xlarge, g6.xlarge)

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 | 267 | 43% | 5.6 | 9 (10-04 00:31Z) |
| ap-northeast-1 | 267 | 74% | 7.2 | 9 (10-04 00:31Z) |
| ap-northeast-2 | 267 | 100% | 9.0 | 9 (10-04 00:31Z) |
| ap-south-1 | 267 | 58% | 6.2 | 9 (10-04 00:31Z) |
| ap-southeast-2 | 267 | 15% | 3.1 | 9 (10-04 00:31Z) |
| ap-southeast-3 | 267 | 21% | 3.3 | 1 (10-04 00:31Z) |
| us-east-1 | 267 | 72% | 6.7 | 9 (10-04 00:31Z) |
| us-east-2 | 267 | 76% | 7.3 | 9 (10-04 00:31Z) |
| us-west-2 | 267 | 54% | 5.8 | 9 (10-04 00:31Z) |

### Last 48 samples

```
region           oldest → newest (48 h, one char per sample)
ap-east-1        999999999999999999999999999999999999999999999999
ap-northeast-1   999999999222332234437999999999999224992299999999
ap-northeast-2   999999999999999999999999999999999999999999999999
ap-south-1       999999999999999111111111111992999992999999999999
ap-southeast-2   922922112222222222222222222222222222222222222229
ap-southeast-3   768111118711111111111114765161111119991141111111
us-east-1        544359593655999936554443334433344559449855763499
us-east-2        433399999999999999999832929983599999999993999999
us-west-2        355532243533324253455455444445444339344995999999
```

### Mean score by UTC hour

| region | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ap-east-1 | 4 | 7 | 9 | 8 | 5 | 5 | 5 | 7 | 7 | 5 | 6 | 5 | 7 | 6 | 5 | 6 | 5 | 7 | 5 | 6 | 6 | 5 | 5 | 5 |
| ap-northeast-1 | 7 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 5 | 4 | 6 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-northeast-2 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| ap-south-1 | 8 | 9 | 9 | 8 | 6 | 8 | 6 | 5 | 4 | 3 | 4 | 3 | 3 | 6 | 4 | 6 | 6 | 7 | 7 | 8 | 7 | 7 | 8 | 6 |
| ap-southeast-2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 2 |
| ap-southeast-3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 4 |
| us-east-1 | 7 | 8 | 7 | 8 | 8 | 9 | 9 | 7 | 8 | 8 | 8 | 8 | 6 | 5 | 5 | 5 | 6 | 5 | 5 | 6 | 6 | 6 | 7 | 6 |
| us-east-2 | 6 | 7 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 6 | 6 | 6 | 8 | 6 | 7 | 5 | 7 | 6 | 7 |
| us-west-2 | 6 | 5 | 5 | 4 | 5 | 6 | 8 | 7 | 6 | 5 | 8 | 7 | 8 | 7 | 6 | 7 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

![g-xlarge-trio heatmap](report/heatmap-g-xlarge-trio.svg)

### Best single AZ per sample

| region | samples | hours ≥ 5 | mean score | latest |
|---|---|---|---|---|
| ap-east-1 ape1-az1 | 152 | 64% | 6.9 | 9 (10-03 17:12Z) |
| ap-east-1 ape1-az2 | 123 | 67% | 7.0 | 9 (10-03 12:27Z) |
| ap-east-1 ape1-az3 | 119 | 63% | 6.8 | 9 (10-04 00:31Z) |
| ap-northeast-1 apne1-az1 | 126 | 92% | 8.5 | 9 (10-03 17:12Z) |
| ap-northeast-1 apne1-az2 | 63 | 59% | 6.5 | 9 (10-03 21:08Z) |
| ap-northeast-1 apne1-az4 | 154 | 99% | 9.0 | 9 (10-03 17:12Z) |
| ap-northeast-2 apne2-az1 | 208 | 100% | 9.0 | 9 (10-03 12:27Z) |
| ap-northeast-2 apne2-az2 | 58 | 76% | 7.5 | 9 (10-04 00:31Z) |
| ap-northeast-2 apne2-az3 | 233 | 100% | 9.0 | 9 (10-03 12:27Z) |
| ap-northeast-2 apne2-az4 | 145 | 68% | 7.1 | 9 (10-03 17:12Z) |
| ap-south-1 aps1-az1 | 87 | 75% | 7.5 | 9 (10-04 00:31Z) |
| ap-south-1 aps1-az2 | 94 | 62% | 6.7 | 9 (10-02 08:24Z) |
| ap-south-1 aps1-az3 | 105 | 83% | 8.0 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az1 | 23 | 57% | 6.3 | 9 (10-04 00:31Z) |
| ap-southeast-2 apse2-az2 | 1 | 0% | 3.0 | 3 (09-04 18:19Z) |
| ap-southeast-2 apse2-az3 | 29 | 59% | 6.5 | 9 (09-29 18:29Z) |
| ap-southeast-3 apse3-az3 | 54 | 24% | 4.4 | 9 (10-01 17:00Z) |
| us-east-1 use1-az1 | 13 | 92% | 8.2 | 2 (09-30 20:24Z) |
| us-east-1 use1-az2 | 76 | 100% | 9.0 | 9 (09-30 04:28Z) |
| us-east-1 use1-az4 | 94 | 97% | 8.8 | 9 (10-04 00:31Z) |
| us-east-1 use1-az5 | 55 | 98% | 8.9 | 9 (10-04 00:31Z) |
| us-east-1 use1-az6 | 78 | 96% | 8.7 | 9 (09-30 05:24Z) |
| us-east-2 use2-az1 | 97 | 99% | 8.9 | 9 (10-03 06:23Z) |
| us-east-2 use2-az2 | 144 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-east-2 use2-az3 | 125 | 94% | 8.6 | 9 (10-02 08:24Z) |
| us-west-2 usw2-az1 | 70 | 99% | 8.9 | 9 (10-04 00:31Z) |
| us-west-2 usw2-az2 | 62 | 95% | 8.6 | 9 (10-03 17:12Z) |
| us-west-2 usw2-az3 | 82 | 95% | 8.7 | 9 (10-04 00:31Z) |

## Latest spot prices

| region | az | product | $/h | sampled |
|---|---|---|---|---|
| ap-northeast-1 | ap-northeast-1a | Linux/UNIX | 0.725000 | 2026-10-04T00:31:56Z |
| ap-northeast-1 | ap-northeast-1a | Windows | 0.840600 | 2026-10-04T00:31:56Z |
| ap-northeast-1 | ap-northeast-1c | Linux/UNIX | 0.779100 | 2026-10-04T00:31:56Z |
| ap-northeast-1 | ap-northeast-1c | Windows | 0.961000 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2a | Linux/UNIX | 0.593200 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2a | Windows | 0.740700 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2c | Linux/UNIX | 0.577400 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2c | Windows | 0.740700 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2d | Linux/UNIX | 0.565300 | 2026-10-04T00:31:56Z |
| ap-northeast-2 | ap-northeast-2d | Windows | 0.743600 | 2026-10-04T00:31:56Z |
| ap-south-1 | ap-south-1a | Linux/UNIX | 0.649500 | 2026-10-04T00:31:56Z |
| ap-south-1 | ap-south-1a | Windows | 0.367500 | 2026-10-04T00:31:56Z |
| ap-south-1 | ap-south-1b | Linux/UNIX | 0.702700 | 2026-10-04T00:31:56Z |
| ap-south-1 | ap-south-1b | Windows | 0.361700 | 2026-10-04T00:31:56Z |
| ap-southeast-2 | ap-southeast-2a | Linux/UNIX | 0.728300 | 2026-10-04T00:31:56Z |
| ap-southeast-2 | ap-southeast-2a | Windows | 0.494500 | 2026-10-04T00:31:56Z |
| ap-southeast-2 | ap-southeast-2c | Linux/UNIX | 0.535000 | 2026-10-04T00:31:56Z |
| ap-southeast-2 | ap-southeast-2c | Windows | 0.572900 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1a | Linux/UNIX | 0.576500 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1a | Windows | 0.289700 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1b | Linux/UNIX | 0.445000 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1b | Windows | 0.284600 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1c | Linux/UNIX | 0.480500 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1c | Windows | 0.284600 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1d | Linux/UNIX | 0.413200 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1d | Windows | 0.284600 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1f | Linux/UNIX | 0.498600 | 2026-10-04T00:31:56Z |
| us-east-1 | us-east-1f | Windows | 0.284600 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2a | Linux/UNIX | 0.534700 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2a | Windows | 0.641400 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2b | Linux/UNIX | 0.526300 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2b | Windows | 0.641200 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2c | Linux/UNIX | 0.515600 | 2026-10-04T00:31:56Z |
| us-east-2 | us-east-2c | Windows | 0.637500 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2a | Linux/UNIX | 0.503000 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2a | Windows | 0.332200 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2b | Linux/UNIX | 0.496200 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2b | Windows | 0.331800 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2c | Linux/UNIX | 0.481600 | 2026-10-04T00:31:56Z |
| us-west-2 | us-west-2c | Windows | 0.331000 | 2026-10-04T00:31:56Z |
