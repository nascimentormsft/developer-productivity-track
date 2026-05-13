---
description: "Generate a Terraform module following team conventions"
---
Create a Terraform module for {{resource_type}} with:

- **variables.tf**: All inputs with descriptions, types, and validation rules
- **main.tf**: Resource configuration following our naming convention: `{project}-{env}-{resource}`
- **outputs.tf**: Expose key attributes (id, name, connection strings where applicable)
- **README.md**: Usage example with required provider version

Requirements:
- Use `azurerm` provider
- Apply standard tags: `environment`, `team`, `cost-center`, `managed-by = "terraform"`
- Include variable validation (e.g., environment must be dev/staging/production)
- Use locals for computed naming
