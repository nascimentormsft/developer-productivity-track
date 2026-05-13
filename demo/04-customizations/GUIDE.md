# Customizations: Scale Your Team's Expertise

**Time:** ~13 min  
**Goal:** Explore four types of Copilot customizations that replace repetitive tasks with reusable, shareable configuration.

**Setup:** Open the repository root as your workspace so Copilot can see the root `.github/` folder.

---

## Part A: Custom Prompts (3 min)

> Reusable prompt templates your entire team can invoke.

1. Open [`../../.github/prompts/terraform-module.prompt.md`](../../.github/prompts/terraform-module.prompt.md)
2. Read the structure: YAML frontmatter (`description`) + template body with `{{variables}}`
3. Open Copilot Chat and invoke the prompt:
   ```
   /terraform-module Azure Storage Account
   ```
4. Review the generated Terraform module (variables.tf, main.tf, outputs.tf)

**What to notice:**
- The naming convention (`{project}-{env}-{resource}`) is applied automatically
- Standard tags are included without you asking
- This prompt is now available to every team member who has this file

📖 **Learn more:** [Use prompt files in VS Code](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

---

## Part B: Custom Instructions (3 min)

> Invisible guardrails that shape every Copilot interaction.

1. Open [`../../.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
2. Read through the standards: Python conventions, Terraform rules, CI/CD requirements
3. Now ask Copilot Chat to write something:
   ```
   Write a function to calculate monthly interest on an account balance
   ```
4. Check the output against the instructions

**What to notice:**
- Does it use type hints? (instructions say: "Use Python type hints for all function signatures")
- Does it follow Google docstring style? (instructions say so)
- Does it use f-strings? (instructions say: "Prefer f-strings")

You didn't mention any of these in your prompt — the instructions applied automatically.

📖 **Learn more:** [Adding custom instructions for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)

---

## Part C: Skills (3 min)

> Domain-specific knowledge packs that make Copilot an expert in your area.

1. Open [`part-c-skill-demo/skill_context_demo.py`](part-c-skill-demo/skill_context_demo.py) and run it once.
2. Open [`part-c-skill-demo/financial_transactions_sample.csv`](part-c-skill-demo/financial_transactions_sample.csv) to inspect the data anomalies (duplicates, future timestamp, mixed currencies).
3. In Chat, ask a baseline request first:
   ```
   Using df, create a customer summary with transaction count and total amount.
   ```
4. Open [`../../.github/skills/pandas-analysis/SKILL.md`](../../.github/skills/pandas-analysis/SKILL.md) and read the domain rules.
5. Ask a second, skill-aligned request:
   ```
   Refactor the summary to follow the pandas-analysis skill exactly:
   - check duplicates first
   - convert USD/GBP to EUR (USD 0.92, GBP 1.17)
   - flag transactions > EUR 50,000
   - avoid iterrows and use vectorized operations
   - aggregate by customer, month, merchant category
   ```
6. Compare the baseline and skill-aligned outputs.

**What to notice:**
- Does it check for duplicate transaction IDs first?
- Does it convert to EUR using the specified rates (USD: 0.92, GBP: 1.17)?
- Does it use vectorized operations (not `iterrows()`)?
- Does it flag high-value transactions (> EUR 50,000)?
- Does it include customer-month-category aggregation?

This is your team's institutional knowledge — encoded, versioned, and shareable.

📖 **Learn more:** [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)

---

## Part D: Agents (4 min)

> Autonomous multi-step workflows that follow your standards.

1. Open [`../../.github/agents/pipeline-scaffolder.agent.md`](../../.github/agents/pipeline-scaffolder.agent.md)
2. Read the structure: description, tools, step-by-step instructions
3. Switch to **Agent mode** in Copilot Chat (click the mode selector)
4. Type:
   ```
   Create a CI/CD pipeline for the payments-api service
   ```
5. Watch Agent create the pipeline YAML

**What to notice:**
- Does it include GitHub Advanced Security for Azure DevOps scanning?
- Does it include Trivy container scanning?
- Does it add environment-specific deployment gates (dev → staging → production)?
- Does it follow the naming conventions from your instructions?

📖 **Learn more:** [Creating and using custom agents for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)

---

## Key Takeaways

| Customization | What it does | Effort to set up |
|---------------|-------------|-------------------|
| **Instructions** | Invisible guardrails for all interactions | 5 min |
| **Prompts** | Reusable templates with variables | 10 min each |
| **Skills** | Domain knowledge packs | 15 min each |
| **Agents** | Multi-step autonomous workflows | 20 min each |

**Start small:** Add a `copilot-instructions.md` to one of your repos today. That's a 5-minute investment that improves every Copilot interaction for your whole team.

**Think about your workflows:** What do you configure repeatedly in Azure DevOps, Terraform, or your CI/CD pipelines? That's your first prompt template.

---

## Further Reading

| Topic | Documentation |
|-------|---------------|
| Instructions | [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) |
| Customize Copilot CLI | [Overview of customizing GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview) |
