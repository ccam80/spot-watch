# spot-watch

Hourly log of EC2 Spot placement scores and spot prices for the instance types in `config.json`; see [REPORT.md](REPORT.md).

- `collect.py`: appends one sample to `data/scores.csv` and `data/prices.csv`.
- `report.py`: renders `REPORT.md` and `report/heatmap-*.svg`.
- `.github/workflows/collect.yml`: runs both hourly and commits the result.

Single-type score sets are scored low by EC2; use the trio set as the reference.

## AWS setup

The workflow assumes an IAM role through the account's GitHub OIDC provider.

- Trust: `token.actions.githubusercontent.com`, `aud` = `sts.amazonaws.com`, `sub` matching `repo:ccam80@63381855/spot-watch@1347813897:*` (GitHub issues immutable owner@id/repo@id subjects here).

- Permissions: `ec2:GetSpotPlacementScores` and `ec2:DescribeSpotPriceHistory` on `*`.

- Secret `AWS_SPOT_WATCH_ROLE`: the role's full ARN, `arn:aws:iam::<account>:role/<name>`.

## Local run

```bash
pip install boto3
AWS_PROFILE=cubie-fleet AWS_REGION=us-east-2 python collect.py
python report.py
```
