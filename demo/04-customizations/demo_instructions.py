"""
Demo 4: Customizations - Replacing Repetitive Tasks with Reusable Config

INSTRUCTIONS FOR PRESENTER:
This demo showcases four types of Copilot customizations using the team's
real workflow scenarios: Terraform, CI/CD pipelines, Azure DevOps.

SETUP:
- Open this folder (04-customizations/) as your workspace root
- Ensure Copilot can see .github/ and .vscode/ folders

DEMO FLOW (13 min total):

────────────────────────────────────────────
PART A: CUSTOM PROMPTS (3 min)
────────────────────────────────────────────
1. Show the folder structure: .github/prompts/
2. Open .github/prompts/terraform-module.prompt.md
3. Walk through the structure: frontmatter + template with {{variables}}
4. Invoke the prompt from Copilot Chat:
   - Type: @prompt terraform-module
   - When asked for resource_type, say: "Azure Storage Account"
5. Show the generated Terraform module (variables.tf, main.tf, outputs.tf)
6. Key point: "This is now available to every team member."

────────────────────────────────────────────
PART B: CUSTOM INSTRUCTIONS (3 min)
────────────────────────────────────────────
1. Open .github/copilot-instructions.md
2. Point out: Python standards, Terraform rules, CI/CD requirements
3. Now create a quick Python function with Copilot Chat:
   "Write a function to calculate monthly interest on an account balance"
4. Show that it automatically includes:
   - Type hints (because instructions say so)
   - Google docstring style (because instructions say so)
5. Key point: "Instructions are invisible guardrails. Set them once, 
   forget about them."

────────────────────────────────────────────
PART C: SKILLS (3 min)
────────────────────────────────────────────
1. Open .vscode/skills/pandas-analysis/SKILL.md
2. Walk through: when to use, domain rules, standard checks
3. Now ask Copilot to analyze data:
   "Analyze the financial transactions in df and create a customer summary"
4. Show that it follows the skill's rules:
   - Checks for duplicates first
   - Converts to EUR
   - Uses vectorized operations
5. Key point: "This is institutional knowledge, encoded and shareable."

────────────────────────────────────────────
PART D: AGENTS (4 min)
────────────────────────────────────────────
1. Open .vscode/agents/pipeline-scaffolder.agent.md
2. Walk through: description, tools, step-by-step instructions
3. Switch to Agent mode in Copilot Chat
4. Type: "Create a CI/CD pipeline for the payments-api service"
5. Watch Agent:
   - Create azure-pipelines.yml
   - Include GHAzDO security scanning
   - Include Trivy container scanning
   - Add environment-specific deployment gates
6. Key point: "A 30-minute task in 30 seconds — following your standards 
   every time."

────────────────────────────────────────────
KEY TAKEAWAYS
────────────────────────────────────────────
- "Customizations scale your team's expertise."
- "Start with instructions (5 min to set up). Add prompts next."
- "Think about your Azure DevOps workflows — what do you configure repeatedly?"
"""
