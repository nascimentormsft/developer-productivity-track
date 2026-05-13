# Prompt Library

A reusable collection of prompts organized by workflow pattern. Use these as starting points and adapt to your specific context.

---

## Pandas & Data Engineering

### Dataset Exploration
```
I have a pandas DataFrame `df` loaded from [source] with columns:
[list columns with types].

Provide a data quality assessment:
- Missing values per column (count and percentage)
- Data type mismatches
- Statistical outliers (IQR method) for numeric columns
- Cardinality of categorical columns
- Date range and gaps in time series columns

Format the output as a summary dictionary.
```

### Data Transformation
```
Transform DataFrame `df` with these steps:
1. [specific transformation with business rule]
2. [specific transformation with business rule]
3. [specific transformation with business rule]

Constraints:
- Use method chaining where possible
- Don't modify the original DataFrame
- Handle missing values by [strategy]
- Add inline comments explaining business logic
- Raise ValueError if [validation condition]
```

### Feature Engineering
```
Create the following features from DataFrame `df` for [use case]:
1. [feature name]: [calculation logic]
2. [feature name]: [calculation logic]
3. [feature name]: [calculation logic]

Handle edge cases:
- [specific edge case and expected behavior]
- [specific edge case and expected behavior]

Use vectorized operations (no iterrows). Include type hints.
```

### Aggregation / Reporting
```
Build a [frequency] summary report from `df`:
- Group by: [columns]
- Metrics: [list of aggregations with names]
- Add: [calculated metrics like ratios or growth]
- Sort by: [column and direction]
- Filter: [any post-aggregation filtering]

Reset index and ensure column names are descriptive.
```

### Pipeline Function
```
Refactor this data processing code into a production-ready function:
- Function name: [name]
- Input: pd.DataFrame with schema [columns and types]
- Output: pd.DataFrame with schema [columns and types]
- Validate input: [validation rules]
- Add logging for: [key events]
- Type hints and Google-style docstring
- Single responsibility: this function only does [scope]
```

---

## Refactoring

### Reduce Complexity
```
Refactor this function to reduce cyclomatic complexity:
- Use early returns to eliminate nesting
- Extract [specific logic] into a helper function
- Replace magic numbers with named constants
- Keep the same external behavior (inputs/outputs unchanged)
- Maintain all existing edge case handling
```

### Modernize Code
```
Modernize this Python code:
- Replace [old pattern] with [new pattern]
- Use f-strings instead of .format() or %
- Use pathlib instead of os.path
- Use dataclass/TypedDict for [data structure]
- Maintain backward compatibility with [requirement]
```

### Extract Pattern
```
This code has a repeated pattern across [N] functions: [describe pattern].

Extract it into a reusable [decorator/base class/utility function] that:
- Accepts [parameters]
- Handles [shared concern]
- Can be applied to all [N] existing call sites
- Follows [naming convention]

Show the extracted code and one example of applying it.
```

### Improve Error Handling
```
Add error handling to this function for a financial services context:
- Validate inputs: [list validation rules]
- Handle expected failures: [list scenarios]
- Use custom exception classes for domain errors
- Log errors with context (don't swallow them)
- Ensure [resource] is cleaned up in all paths
- Don't catch generic Exception unless re-raising
```

---

## Test Generation

### Unit Tests
```
Generate pytest tests for `[function_name]`:
- Happy path with typical input
- Boundary values: [list boundaries]
- Invalid inputs: [list invalid cases]
- Edge cases: [list edge cases]

Use:
- pytest.fixture for shared test data
- pytest.parametrize for [parameterizable cases]
- pytest.raises for expected exceptions
- Descriptive test names (test_[scenario]_[expected_result])
```

### Data Pipeline Tests
```
Generate tests for the data transformation function `[name]`:
- Input: DataFrame with schema [columns]
- Test with valid data (verify output shape, columns, values)
- Test with missing values in [columns]
- Test with empty DataFrame
- Test with duplicate rows
- Test boundary values for [numeric columns]
- Use small, explicit DataFrames (3-5 rows) for clarity
- Assert specific values, not just shapes
```

### Integration Test Scaffold
```
Create a pytest integration test structure for [component]:
- Setup: [describe test environment/fixtures needed]
- Test: [describe the workflow to validate]
- Teardown: [describe cleanup needed]
- Mark with @pytest.mark.integration
- Use [mock/real] for [external dependency]
- Timeout: [reasonable timeout for this test]
```

---

## Debugging

### Diagnose Unexpected Behavior
```
This function is producing incorrect results.

Expected behavior: [describe expected]
Actual behavior: [describe actual]
Input that triggers the issue: [provide example]

The function:
[paste or reference the function]

Identify the bug and explain:
1. Why it happens
2. How to fix it
3. How to prevent it (test case suggestion)
```

### Performance Issue
```
This code is running slowly on [data size]:
[paste or reference the code]

Analyze for performance issues:
- Identify O(n²) or worse operations
- Find unnecessary copies or allocations
- Suggest vectorized alternatives for loops
- Recommend appropriate data structures

Prioritize suggestions by likely impact.
```

### Error Trace Analysis
```
I'm getting this error:
[paste full traceback]

Context:
- This happens when [trigger condition]
- The input data looks like [describe]
- It worked before [recent change]

Diagnose the root cause and provide a fix.
```

---

## Documentation

### Function Docstring
```
Generate a Google-style docstring for this function:
- Describe what it does (one-line summary + details)
- Document all parameters with types and constraints
- Document return value with type
- Document exceptions that can be raised
- Include a usage example
- Note any side effects or assumptions
```

### Module README
```
Generate a README section for this module:
- Purpose: one paragraph
- Key functions/classes with one-line descriptions
- Usage example (common workflow)
- Dependencies
- Configuration (if any)

Keep it concise—developers will read code for details.
```

### API Documentation
```
Document this API endpoint:
- HTTP method and path
- Purpose (one sentence)
- Request parameters/body with types and validation
- Response format (success and error)
- Example request and response
- Error codes and their meaning
- Authentication requirements

Use [OpenAPI/Markdown/your format] style.
```

---

## Multi-step Tasks

### Feature Implementation
```
I need to implement [feature name].

Context:
- Existing code: [reference files/architecture]
- Requirements: [list requirements]
- Constraints: [technical constraints]

Please provide a step-by-step implementation plan:
1. What to create/modify
2. In what order (considering dependencies)
3. Key implementation details for each step
4. Tests needed

Start with step 1.
```

### Code Migration
```
Migrate this code from [old approach] to [new approach]:
- Current implementation: [describe or reference]
- Target: [describe desired state]
- Constraints:
  - Must maintain backward compatibility during transition
  - Must not break existing tests
  - [other constraints]

Provide the migration in phases:
1. [first safe change]
2. [next change building on previous]
3. [final cleanup]
```

---

## Infrastructure as Code (Terraform)

### Terraform Module Generation
```
Create a Terraform module for [resource_type] (Azure) with:
- variables.tf: all inputs with descriptions, types, and validation rules
- main.tf: resource configuration using naming convention {project}-{env}-{resource}
- outputs.tf: expose key attributes (id, name, connection strings where applicable)
- Provider: azurerm
- Apply standard tags: environment, team, cost-center, managed-by = "terraform"
- Include a README.md with usage example and required provider version
```

### Terraform Variable Validation
```
Add validation blocks to these Terraform variables:
- environment: must be one of [dev, staging, production]
- resource_group_name: must match Azure naming rules (alphanumeric, hyphens, 1-90 chars)
- location: must be one of [westeurope, northeurope]
- [custom variable]: [validation rule]

Include meaningful error messages that help the user fix the issue.
```

### Terraform Refactoring
```
Refactor this Terraform configuration:
- Extract repeated resource blocks into a module
- Use for_each instead of count where resources have unique identifiers
- Move hardcoded values to variables with sensible defaults
- Add lifecycle rules where appropriate
- Ensure state won't be destroyed during refactor (use moved blocks if needed)
```

---

## CI/CD Pipelines (Azure DevOps)

### Azure DevOps Pipeline Generation
```
Create an Azure DevOps pipeline YAML (azure-pipelines.yml) for a [language/framework] service:
- Trigger: main branch + PR validation
- Stages: build, test, security-scan, deploy-dev, deploy-staging, deploy-production
- Security scanning:
  - GitHub Advanced Security for Azure DevOps (code scanning, dependency scanning)
  - Trivy container image scanning (if containerized)
- Deploy to Azure [App Service / AKS / Container Apps]
- Use environment approvals for staging and production
- Include variable groups for secrets
- Cache dependencies for faster builds
```

### Pipeline Debugging
```
This Azure DevOps pipeline is failing with the following error:
[paste error]

Pipeline context:
- Stage: [stage name]
- Agent pool: [pool]
- Recent changes: [what changed]

Diagnose the root cause and suggest a fix.
```

### Security Scanning Stage
```
Add a security scanning stage to this Azure DevOps pipeline:
- GitHub Advanced Security for Azure DevOps:
  - Code scanning (CodeQL)
  - Dependency scanning
  - Secret scanning
- Trivy:
  - Container image scan (fail on CRITICAL/HIGH)
  - IaC scan for Terraform files
- Fail the pipeline if critical vulnerabilities are found
- Publish scan results as pipeline artifacts
```

---

## Architecture Documentation

### Architecture Decision Record (ADR)
```
Generate an Architecture Decision Record (ADR) for:
- Decision: [describe the architectural decision]
- Context: [what problem are we solving]
- Options considered: [list at least 3 options]
- Decision outcome: [which option and why]

Follow the ADR template:
# Title
## Status
## Context
## Decision
## Consequences
## Alternatives Considered
```

### Architecture Diagram Description
```
Based on the code in this repository, generate a description of the system architecture:
- List all services/components and their responsibilities
- Describe the data flow between components
- Identify external dependencies (Azure services, APIs, databases)
- Note communication patterns (sync/async, protocols)
- Format as a Mermaid diagram that can be embedded in the README

Focus on the deployment architecture in Azure.
```

### Technical Documentation
```
Generate technical documentation for this [service/module/component]:
- Overview: what it does and why it exists
- Architecture: how it fits in the larger system
- Key design decisions with rationale
- API surface (if applicable)
- Configuration and environment variables
- Deployment: how it's deployed via [CI/CD pipeline]
- Monitoring and observability
- Runbook: common operational tasks

Target audience: new team member onboarding.
```

---

## Customizations

### Writing Custom Instructions
```
I want to create a copilot-instructions.md for my team. Our conventions are:
- Language: [Python/TypeScript/etc.]
- Style: [Google style / PEP 8 / team standard]
- Patterns: [describe preferred patterns]
- Testing: [pytest / jest / etc.]
- Infrastructure: [Terraform / Bicep / etc.]
- Documentation: [docstring style, README requirements]

Generate the instructions file content.
```

### Writing a Custom Prompt File
```
Create a .prompt.md file for [task description].
The prompt should:
- Have a clear description in the frontmatter
- Accept variables via {{variable_name}} syntax
- Include specific constraints relevant to our team
- Follow our [coding/infrastructure/documentation] standards
- Be reusable across different instances of this task
```

### Writing a Skill File
```
Create a SKILL.md file for [domain/workflow]:
- When to use this skill (triggers)
- When NOT to use this skill
- Domain-specific knowledge and rules
- Common patterns and examples
- Edge cases and how to handle them

The skill should help Copilot produce better results for [specific use case].
```

---

## Tips for Using This Library

1. **Always customize** – Replace bracketed placeholders with your specific context
2. **Add file references** – Use `@file` or `#selection` to point Copilot at relevant code
3. **Team workflows** – Adapt the Terraform, CI/CD, and documentation prompts to your team's specific Azure DevOps setup
3. **Iterate** – If the first output isn't right, refine your prompt rather than fixing the code manually
4. **Combine patterns** – "Refactor this, then generate tests for the refactored version"
5. **Save your best prompts** – Build your own team-specific prompt library over time
