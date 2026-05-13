# Team Coding Standards

## Python
- Use Python type hints for all function signatures
- Follow Google docstring style
- Use `pathlib` instead of `os.path`
- Prefer f-strings over `.format()` or `%` formatting
- Use `dataclass` for data containers with 3+ fields

## Terraform
- All resources must include standard tags: environment, team, cost-center, managed-by
- Naming convention: `{project}-{env}-{resource}` (e.g., `payments-prod-storage`)
- Variables must have descriptions and type constraints
- Use `azurerm` provider

## CI/CD (Azure DevOps)
- Pipeline YAML must include security scanning stages (GHAzDO + Trivy)
- All deployments require environment approvals for staging and production
- Artifacts must be published for traceability

## Git
- Commit messages follow Conventional Commits format: `type(scope): description`
- Types: feat, fix, docs, refactor, test, ci, chore
