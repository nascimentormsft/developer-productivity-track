# Slide / Storyline Outline

## Section 1: Introduction & Fundamentals

### Slide 1.1 – Title Slide
- **Title:** From Code to Confidence: Developer Productivity with GitHub Copilot
- **Key message:** Today you'll leave with techniques you can use tomorrow
- **Speaker notes:** Welcome everyone. This is a hands-on, demo-driven session. We'll move fast, show real workflows, and you'll get time to try it yourself.

### Slide 1.2 – What is GitHub Copilot (Practically)?
- **Title:** Your AI Pair Programmer
- **Key message:** Copilot is a context-aware coding assistant embedded in your IDE
- **Bullets:**
  - Understands your code, your files, your intent
  - Suggests completions, answers questions, generates code
  - Works across languages: Python, TypeScript, Java, C#, and more
- **Speaker notes:** Don't think of it as autocomplete on steroids. Think of it as a junior developer who's read every Stack Overflow answer but needs your guidance on what's appropriate for your codebase.

### Slide 1.3 – Where Copilot Helps in the SDLC
- **Title:** Across the Development Lifecycle
- **Key message:** Copilot isn't just for writing new code
- **Visual:** SDLC diagram with highlighted touch points: Plan → Code → Test → Debug → Document → Deploy
- **Speaker notes:** Most people think Copilot = code generation. But the biggest productivity gains often come from explanation, refactoring, and test generation. And for your workflow — think about how it helps with Terraform, CI/CD pipelines, and architecture docs too.

### Slide 1.4 – Agent, Ask, and Plan
- **Title:** Three Ways to Work with Copilot
- **Key message:** Choose the right mode for the complexity of your task
- **Bullets:**
  - **Ask:** Quick questions, explanations, one-shot code generation
  - **Agent:** Multi-step autonomous workflows — edits files, runs commands, iterates
  - **Plan:** Design a step-by-step approach before executing complex changes
- **Speaker notes:** Ask is your go-to for 80% of tasks. Agent is powerful when you need Copilot to act across multiple files — for example, scaffolding a Terraform module with variables, outputs, and a README. Plan is best when you want to review the approach before Copilot starts making changes.

### Slide 1.5 – Model Selection
- **Title:** How to Select a Model
- **Key message:** Different models excel at different tasks — pick the right one
- **Bullets:**
  - Model selector in the Copilot Chat panel
  - Faster models for quick edits and completions
  - More capable models for complex reasoning and multi-step tasks
  - Experiment and find what works best for your workflow
- **Speaker notes:** You can switch models directly in the chat. For a quick code explanation, a fast model works fine. For generating a complex Terraform module or refactoring a pipeline, you may want a more capable model.

### Slide 1.6 – Interaction Modes
- **Title:** How You Interact with Copilot
- **Key message:** Choose the right mode for the task
- **Bullets:**
  - **Inline completions:** Tab-to-accept as you type
  - **Chat panel:** Multi-turn conversations, ask questions
  - **Inline chat:** Quick edits in context (Ctrl+I)
- **Speaker notes:** We'll use all of these today. The key insight: inline completions for flow, chat for exploration and complex tasks.

### Slide 1.7 – 🎬 DEMO: Quick Win
- **Title:** [Live Demo]
- **Demo marker:** Generate function from comment + explain unfamiliar code
- **Speaker notes:** "Let me show you the simplest thing Copilot can do that saves time every single day."

---

## Section 2: Prompting Fundamentals

### Slide 2.1 – Why Prompting Matters
- **Title:** The Quality of Your Output Depends on Your Input
- **Key message:** Copilot responds to context—give it better context, get better code
- **Visual:** Input quality → Output quality gradient
- **Speaker notes:** This is the single most important skill you'll learn today. Everything else builds on this.

### Slide 2.2 – Anatomy of a Good Prompt
- **Title:** Intent + Context + Constraints
- **Key message:** Three ingredients for effective prompts
- **Bullets:**
  - **Intent:** What do you want? (be specific)
  - **Context:** What does Copilot need to know? (files, libraries, patterns)
  - **Constraints:** What are the boundaries? (performance, style, error handling)
- **Speaker notes:** Think of it like briefing a colleague. You wouldn't say "fix it"—you'd say "refactor this function to use async/await, keeping the error handling pattern from our auth module."

### Slide 2.3 – References: @ Mentions and / Commands
- **Title:** Giving Copilot More Context
- **Key message:** Point Copilot at the right information
- **Bullets:**
  - `@workspace` – reference your project structure
  - `@file` – include specific file content
  - `#selection` – reference highlighted code
  - `/explain`, `/tests`, `/fix` – shortcut commands
- **Speaker notes:** These vary slightly by IDE version. The concept is universal: help Copilot see what you see.

### Slide 2.4 – 🎬 DEMO: Prompt Progression
- **Title:** [Live Demo] Bad → Better → Best
- **Demo marker:** Three prompt iterations showing quality improvement
- **Speaker notes:** Watch how the same task produces dramatically different results based on how we ask.

### Slide 2.5 – The Prompt Improvement Checklist
- **Title:** Before You Prompt, Ask Yourself:
- **Bullets:**
  - ✅ Is my intent specific?
  - ✅ Did I provide relevant context?
  - ✅ Did I state constraints (format, style, libraries)?
  - ✅ Am I referencing the right files/code?
  - ✅ Would a colleague understand what I'm asking?
- **Speaker notes:** Print this out, stick it on your monitor for a week. It becomes second nature.

---

## Section 3: Developer Productivity Patterns

### Slide 3.1 – Six Patterns for Daily Productivity
- **Title:** Practical Workflows You Can Use Tomorrow
- **Key message:** Each pattern = a specific scenario where Copilot saves you time
- **Visual:** Six pattern cards in a grid
- **Speaker notes:** I'm going to demo each of these quickly. Pay attention to the prompts, not just the outputs.

### Slide 3.2 – 🎬 DEMO: Code Explanation
- **Title:** [Live Demo] Understanding Unfamiliar Code
- **Key message:** "Explain this" is your fastest path to understanding
- **When to use:** Onboarding, code reviews, investigating bugs in unfamiliar modules
- **Speaker notes:** This is the #1 use case engineers report after adoption. Especially valuable in large codebases.

### Slide 3.3 – 🎬 DEMO: Refactoring
- **Title:** [Live Demo] Restructure with Confidence
- **Key message:** Describe the transformation, let Copilot handle the mechanics
- **When to use:** Reducing complexity, applying patterns, modernizing code
- **Speaker notes:** Copilot is excellent at mechanical transformations where the intent is clear.

### Slide 3.4 – 🎬 DEMO: Test Generation
- **Title:** [Live Demo] Bootstrap Tests Fast
- **Key message:** Generate the scaffolding, then refine the assertions
- **When to use:** Adding coverage to existing code, TDD scaffolding
- **Speaker notes:** Don't trust generated tests blindly—review assertions. But the scaffolding saves enormous time.

### Slide 3.5 – 🎬 DEMO: Debugging
- **Title:** [Live Demo] Find and Fix with AI
- **Key message:** Describe the symptom, provide the context, get a diagnosis
- **When to use:** Stack traces, unexpected behavior, performance issues
- **Speaker notes:** The `/fix` command is a great starting point. For complex bugs, use chat with full context.

### Slide 3.6 – 🎬 DEMO: Documentation
- **Title:** [Live Demo] Generate Docs That Don't Suck
- **Key message:** Copilot generates docs; you validate accuracy
- **When to use:** Docstrings, README sections, API documentation
- **Speaker notes:** Pro tip: provide an example of your doc style and Copilot will match it.

### Slide 3.7 – 🎬 DEMO: Multi-step Tasks
- **Title:** [Live Demo] Breaking Down Complex Work
- **Key message:** Complex tasks need decomposition—prompt in steps
- **When to use:** Feature implementation, migrations, multi-file changes
- **Speaker notes:** Don't ask Copilot to "build me a payment processing system." Ask it to build one piece at a time.

### Slide 3.8 – Pattern Summary
- **Title:** When to Use What
- **Visual:** Quick reference table: Pattern → Best mode → Prompt tip
- **Speaker notes:** You'll find this in the prompt library handout.

---

## Section 4: Customizations

### Slide 4.1 – Why Customizations Matter
- **Title:** Stop Repeating Yourself — Teach Copilot Your Workflow
- **Key message:** Customizations turn one-off prompts into reusable team assets
- **Bullets:**
  - Every team has repetitive tasks: Terraform modules, pipeline YAML, architecture docs
  - Copilot customizations let you encode that knowledge once and reuse it
  - Four levels: prompts, instructions, skills, agents
- **Speaker notes:** Think about the tasks your team does over and over. Writing Terraform for a new microservice. Configuring a CI/CD pipeline in Azure DevOps. Generating architecture documentation. What if Copilot already knew your team's conventions?

### Slide 4.2 – 🎬 DEMO: Custom Prompts
- **Title:** [Live Demo] Reusable Prompt Files (`.prompt.md`)
- **Key message:** Save your best prompts as reusable files the whole team can use
- **Demo marker:** Create a `.prompt.md` file for generating a Terraform module with team conventions
- **Speaker notes:** Show creating a prompt file that generates a Terraform module following the team's naming conventions, tagging standards, and variable structure. Anyone on the team can invoke this prompt instead of writing it from scratch each time.

### Slide 4.3 – 🎬 DEMO: Custom Instructions
- **Title:** [Live Demo] Teaching Copilot Your Standards
- **Key message:** Define team conventions once, apply everywhere
- **Bullets:**
  - `.github/copilot-instructions.md` — project-wide instructions
  - `.instructions.md` files — scoped to specific folders or file types
  - Coding standards, naming conventions, preferred patterns
- **Demo marker:** Set up instructions for Azure DevOps work item format, coding standards, and Terraform conventions
- **Speaker notes:** If your team has a style guide, encode it as instructions. Copilot will follow it consistently. Show how to set up instructions that enforce your Terraform naming conventions and ensure CI/CD pipeline YAML follows your org's template.

### Slide 4.4 – 🎬 DEMO: Skills
- **Title:** [Live Demo] Domain-Specific Knowledge Packs
- **Key message:** Package domain knowledge into reusable skills
- **Bullets:**
  - Markdown files that describe how to perform domain-specific tasks
  - Copilot uses them as reference when relevant
  - Example: pandas analysis skill for financial data workflows
- **Demo marker:** Show a pandas analysis skill and how it improves Copilot's data engineering suggestions
- **Speaker notes:** Skills are like giving Copilot a runbook. For your team, this could be a skill for financial data quality checks, or one for setting up a new microservice's Terraform + pipeline.

### Slide 4.5 – 🎬 DEMO: Agents
- **Title:** [Live Demo] Multi-Step Autonomous Workflows
- **Key message:** Agents orchestrate complex, multi-file tasks end to end
- **Bullets:**
  - Custom agent modes with specific tools and instructions
  - Example: CI/CD pipeline scaffolding agent
  - Agent creates files, runs commands, iterates on errors
- **Demo marker:** Show an agent that scaffolds a CI/CD pipeline YAML for Azure DevOps with GHAzDO security scanning and Trivy integration
- **Speaker notes:** This is the most powerful customization. Imagine an agent that, given a service name, creates the full Azure DevOps pipeline YAML with your standard stages, security scanning (GHAzDO + Trivy), and deployment gates. That's what we'll demo.

### Slide 4.6 – Customizations Summary
- **Title:** Which Customization When?
- **Visual:** Quick reference table: Customization → Use case → Team benefit
- **Bullets:**
  - **Prompts:** Reusable templates for common tasks (Terraform, pipelines)
  - **Instructions:** Enforce standards automatically (coding style, naming)
  - **Skills:** Domain knowledge for specialized workflows (data analysis)
  - **Agents:** End-to-end automation for complex multi-step tasks (CI/CD setup)
- **Speaker notes:** Start with instructions — they're the easiest to adopt and have the biggest immediate impact. Then add prompts for your most common tasks. Skills and agents come as your team matures.

---

## Section 5: Hands-on Labs — Choose Your Adventure

### Slide 5.1 – Choose Your Track
- **Title:** Your Turn: Choose Your Adventure
- **Key message:** Pick the lab that matches your daily work — or do both if you're fast
- **Bullets:**
  - **Track A: Pandas & Financial Data** — explore, transform, aggregate financial transactions; practice prompt progression
  - **Track B: Full-Stack Application** — add a feature across a backend API and frontend; use Agent mode for multi-file changes
  - Time: ~22 minutes of hands-on work + 3 min debrief
  - Help: Raise your hand or check the hint prompts
  - Fast finishers: start the other track!
- **Visual:** Two-track diagram with audience profile suggestions
- **Speaker notes:** Present both tracks in 2 minutes. Data engineers and analysts → Track A. App developers and full-stack engineers → Track B. Ambitious attendees can try both. Walk the room and support both tracks.

### Slide 5.2 – Track A: Pandas Lab Overview
- **Title:** Track A: Financial Transaction Analysis
- **Key message:** Practice prompt progression on real data engineering tasks
- **Bullets:**
  - Dataset: 10K synthetic financial transactions
  - Tasks: explore → transform → feature engineering → aggregate → refactor → test
  - Technique: naive prompt → contextual → constrained
  - Stretch goal: anomaly detection or time intelligence
- **Speaker notes:** Brief orientation slide — attendees following Track A can reference this. Move on quickly.

### Slide 5.3 – Track B: Full-Stack Lab Overview
- **Title:** Track B: Frontend + Backend with Copilot
- **Key message:** Use Agent mode for multi-file, cross-layer changes
- **Bullets:**
  - App: Python API backend + frontend that consumes it
  - Tasks: understand API → add endpoint → connect frontend → generate tests
  - Technique: Agent mode for orchestrating multi-file changes
  - Stretch goal: add error handling and integration tests
- **Speaker notes:** Brief orientation slide — attendees following Track B can reference this. Move on quickly.

### Slide 5.4 – Joint Debrief
- **Title:** What Did You Learn?
- **Key message:** Different tasks, same core skills — prompting and context matter everywhere
- **Bullets:**
  - Track A: What prompting strategy worked for data tasks?
  - Track B: How did Agent mode help with cross-layer changes?
  - Both: What surprised you? What will you use tomorrow?
- **Speaker notes:** 3-minute joint debrief. Ask one person from each track to share. Reinforce that the techniques transfer across domains.

---

## Section 6: Wrap-up

### Slide 6.1 – 5 Productivity Habits
- **Title:** Start Tomorrow With These 5 Habits
- **Bullets:**
  1. Always provide context in your prompts
  2. Use `/explain` before diving into unfamiliar code
  3. Generate tests immediately after writing functions
  4. Iterate on prompts—don't accept the first suggestion blindly
  5. Use inline chat (Ctrl+I) for quick, in-context edits
- **Speaker notes:** These are the habits that separate casual users from power users.

### Slide 6.2 – Next Steps
- **Title:** Continue Your Journey
- **Bullets:**
  - Practice daily: pick one workflow per week to Copilot-ify
  - Set up custom instructions for your team
  - Create reusable prompts for Terraform modules and pipeline configs
  - Explore GitHub Copilot documentation
  - Join your internal Copilot champions community
- **Speaker notes:** Thank everyone. Remind them the materials will be shared. Emphasize that the customizations they saw today are something they can start building for their own team's Azure DevOps and Terraform workflows immediately.
