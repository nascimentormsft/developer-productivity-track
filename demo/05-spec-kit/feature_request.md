# Feature Request

## Background
Relationship managers currently review outbound transfer risk using manual checks and spreadsheet exports. This slows approvals and produces inconsistent rationale notes.

## Requested Capability
Create an internal "Transfer Guard" feature that flags risky transfers before submission and gives a clear explanation to the relationship manager.

## Scope
- Analyze outbound transfers for SME accounts.
- Assign a risk tier (`low`, `medium`, `high`).
- Provide a plain-language explanation for each flag.
- Return a list of recommended actions for manual review.

## Inputs
- Account profile (KYC status, tenure, customer segment)
- Transfer request (amount, currency, destination country, timestamp)
- Last 90 days of account transfer behavior

## Constraints
- Do not auto-block transfers in V1; this is decision support only.
- P95 response time should be under 300 ms.
- Explanations must be understandable by non-technical users.

## Success Criteria
- Risk tier + explanation produced for every request.
- False positive rate below 8% during pilot.
- Analysts can trace why a recommendation was produced.
