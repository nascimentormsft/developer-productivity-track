# Plan Prompt for `/speckit.plan`

Use this content as the input prompt when running `/speckit.plan` after `/speckit.specify`.

## Architecture and Stack Constraints

- Backend: Python + FastAPI
- Data: PostgreSQL
- Messaging: none in v1
- Hosting target: Azure App Service
- Authentication: Microsoft Entra ID (OIDC)
- Observability: structured logs + request IDs

## Design Constraints

- Keep v1 as decision support only (no auto-blocking transfers).
- P95 latency for risk evaluation under 300 ms.
- Risk explanations must be plain language and auditable.
- Avoid overfitting to static thresholds; make thresholds configurable.

## Implementation Preferences

- Start with modular service boundaries:
	- `risk_scoring`
	- `explanations`
	- `recommendations`
- Add unit tests for scoring and explanation generation before integration wiring.
- Add API contract tests for request/response schemas.

## Delivery Expectations

- Produce phased implementation plan with milestones.
- Include explicit testing strategy per milestone.
- Call out rollout and rollback considerations.
