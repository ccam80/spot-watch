# spot-watch

Hourly log of EC2 Spot placement scores and spot prices for the instance types in `config.json`; see [REPORT.md](REPORT.md).

- `collect.py`: appends one sample to `data/scores.csv` and `data/prices.csv`.
- `report.py`: renders `REPORT.md` and `report/heatmap-*.svg`.
- `.github/workflows/collect.yml`: runs both hourly and commits the result.

Single-type score sets are scored low by EC2; use the trio set as the reference.

## AWS setup

Create the OIDC role once in CloudShell, then store its ARN as the repository secret `AWS_SPOT_WATCH_ROLE`.

```bash
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
cat > trust.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Federated": "arn:aws:iam::${ACCOUNT}:oidc-provider/token.actions.githubusercontent.com"},
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {"token.actions.githubusercontent.com:aud": "sts.amazonaws.com"},
      "StringLike": {"token.actions.githubusercontent.com:sub": "repo:ccam80/spot-watch:*"}
    }
  }]
}
EOF
cat > policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["ec2:GetSpotPlacementScores", "ec2:DescribeSpotPriceHistory"],
    "Resource": "*"
  }]
}
EOF
aws iam create-role --role-name spot-watch --assume-role-policy-document file://trust.json
aws iam put-role-policy --role-name spot-watch --policy-name spot-watch-read --policy-document file://policy.json
aws iam get-role --role-name spot-watch --query Role.Arn --output text
```

```bash
gh secret set AWS_SPOT_WATCH_ROLE --repo ccam80/spot-watch --body "<role arn>"
gh workflow run collect.yml --repo ccam80/spot-watch
```

## Local run

```bash
pip install boto3
AWS_PROFILE=cubie-fleet AWS_REGION=us-east-2 python collect.py
python report.py
```
