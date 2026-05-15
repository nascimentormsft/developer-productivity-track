
# Track A: Pandas Data Pipeline Lab

Welcome to the Pandas Data Pipeline Lab! This lab is designed to help you practice code exploration, debugging, refactoring, prompt engineering, and documentation automation using Copilot.

## Quick Reference: The 6 Phases

| Phase | Goal | Time | Key Activity |
|-------|------|------|--------------|
| 1 | Explain the codebase | 5 min | Use Copilot to understand the code flow |
| 2 | Find & fix the bug | 8-12 min | Debug and fix subtle logic error |
| 3 | Refactor code smells | 10-15 min | Apply team instructions to improve code quality |
| 4 | Implement repetitive feature | 12-18 min | Create custom prompt to automate aggregation |
| 5 | Create documentation agent | 10-15 min | Build your own Mermaid diagram agent |
| 6 | Embed diagram in README | 5 min | Paste diagram and verify |

---

## Setup

1. Open [lab_exercise.py](lab_exercise.py) in VS Code.
2. Confirm [financial_transactions.csv](financial_transactions.csv) exists in the same folder.
3. Install dependencies:

```bash
pip install pandas
```

4. Run the exercise file to confirm it loads:

```bash
python lab_exercise.py
```

5. Open Copilot Chat (`Ctrl+Shift+I` or `Ctrl+Alt+B`) and ensure you're in **agent mode**.

---

## Phase 1: Explore the Codebase (5 min)

### Goal
Understand what the code does and identify what's missing or unclear.

### Your Tasks

1. **Explain the current code structure:**

In Copilot Chat, copy/paste this prompt:

```text
Explain the code structure in lab_exercise.py. Walk me through:
- What the main data loading does
- What each function (part_1, part_2, part_3, transform_transactions) is supposed to do
- What code is implemented vs. what is still TODO

Be concise.
```

2. **Understand the data:**

```text
I have a financial transactions dataset with columns:
transaction_id, customer_id, amount, currency, transaction_type,
merchant_category, timestamp, is_flagged, account_balance

What does each column represent? Which ones are most important for analysis?
```

### Expected Outcome
You understand the lab structure and what each function should accomplish.

---

## Phase 2: Find & Fix the Bug (8-12 min)

### Goal
There is a **subtle logic bug** in the code that produces incorrect results. Find and fix it using Copilot.

### Your Tasks

1. **Run the code and observe the behavior:**

```bash
python lab_exercise.py
```

Look at the output. The first part runs, but notice the `part_2_data_transformation` function is already implemented. Ask Copilot:

```text
In lab_exercise.py, run part_2_data_transformation(df) on the loaded data.
What does the output show? Are there any issues with the currency conversion or data transformation?
```

2. **Identify the bug:**

In Copilot, ask:

```text
In the part_2_data_transformation function in lab_exercise.py, there's a subtle logic bug.
The code converts amounts but may be applying conversions incorrectly.
Run the function mentally and compare input vs. output.
What rows are being incorrectly processed?
Debug this issue and tell me what the bug is.
```

3. **Fix the bug:**

Once you identify the issue, ask Copilot:

```text
Fix the bug in part_2_data_transformation in lab_exercise.py.
The issue is: [describe what you found]
Implement the fix while keeping all other logic the same.
```

### Expected Outcome
The `part_2_data_transformation` function runs correctly without the logic error.

---

## Phase 3: Refactor Code Smells (10-15 min)

### Goal
Improve code quality by applying team standards from [track-a-instructions.md](track-a-instructions.md).

### Team Standards to Apply

From [track-a-instructions.md](track-a-instructions.md):
- ✅ All functions must have Python type hints
- ✅ Use clear, verb-based function names
- ✅ Extract magic numbers into named constants
- ✅ Use Google docstring style
- ✅ Prefer f-strings for formatting

### Your Tasks

1. **Review the code smells:**

```text
In lab_exercise.py, identify code quality issues:
- Missing or incomplete type hints
- Hardcoded values (like currency rates, clipping bounds)
- Function names that aren't clear
- Missing or incomplete docstrings

List the issues you find.
```

2. **Apply team instructions to fix code smells:**

```text
Refactor lab_exercise.py to match these team standards from track-a-instructions.md:
- All functions must have type hints on parameters and return values
- Extract hardcoded currency rates (0.92, 1.17) into CURRENCY_RATES constant at module level
- Extract hardcoded clipping bound (500000) into MAX_AMOUNT constant
- Add Google-style docstrings to part_2_data_transformation and transform_transactions
- Use clear function names

Apply these changes while preserving the bug fix from Phase 2.
```

3. **Verify the code still works:**

```bash
python lab_exercise.py
```

### Expected Outcome
Code follows team standards. Type hints are present. Magic numbers are constants. Docstrings are clear and Google-style.

---

## Phase 4: Implement Repetitive Feature Using Custom Prompt (12-18 min)

### Goal
Use prompt engineering to turn repetitive coding into a reusable prompt template you can invoke with small configuration changes.

### Your Tasks

1. **Spot the repetitive pattern (same vs. variable):**

You need to implement three functions that all follow the same aggregation structure.

Before writing the prompt, identify:
- What stays the same: filtering by time, grouping by `merchant_category`, aggregating `amount`, and returning structured output
- What changes: function name, time scope (month/year/all), and return type (`dict` or `DataFrame`)

This is the key habit: when a pattern repeats, build a reusable prompt template instead of rewriting instructions.

2. **Create a parameterized prompt called category-aggregations.prompt.md within ./github/prompts.

Use the existing template so it uses placeholders that can be swapped quickly. 
```text
   Implement a Python function in lab_exercise.py using this configuration:

   - Function name: {function_name}
   - Input parameters: {input_parameters}
   - Time scope: {time_scope}
   - Group-by column: {group_by_column}
   - Aggregate column: amount
   - Return type: {return_type}
   - Output schema: {output_schema}
   - Filter logic: {filter_logic}

   Requirements:
   - Use pandas idioms and readable transformations
   - Add complete type hints for parameters and return value
   - Add a Google-style docstring
   - Avoid magic numbers (promote constants when needed)
   - Keep output deterministic and testable
   - Follow team standards in track-a-instructions.md
```

Make sure the template also enforces team standards from [track-a-instructions.md](track-a-instructions.md): type hints, clear names, constants, and Google-style docstrings.

3. **Call the prompt with different configurations:**

Run the same template three times by changing only placeholder values:
- Config A: `calculate_monthly_savings_by_category`
   ```text
      ### Configuration A
      - `{function_name}`: `calculate_monthly_savings_by_category`
      - `{input_parameters}`: `df: pd.DataFrame, year: int, month: int`
      - `{time_scope}`: `specific year and month`
      - `{group_by_column}`: `merchant_category`
      - `{return_type}`: `dict[str, float]`
      - `{output_schema}`: `{category: total_amount}`
      - `{filter_logic}`: `timestamp year == year and timestamp month == month`
   ```
- Config B: `calculate_yearly_category_trend`
   ```text
      ### Configuration B
      - `{function_name}`: `calculate_yearly_category_trend`
      - `{input_parameters}`: `df: pd.DataFrame, year: int`
      - `{time_scope}`: `all months in a year`
      - `{group_by_column}`: `merchant_category`
      - `{return_type}`: `dict[str, float]`
      - `{output_schema}`: `{category: total_amount}`
      - `{filter_logic}`: `timestamp year == year`
   ```
- Config C: `generate_category_report`
   ```text
      ### Configuration C
      - `{function_name}`: `generate_category_report`
      - `{input_parameters}`: `df: pd.DataFrame`
      - `{time_scope}`: `all available years and months`
      - `{group_by_column}`: `merchant_category`
      - `{return_type}`: `pd.DataFrame`
      - `{output_schema}`: `rows by year/month/category with aggregated total`
      - `{filter_logic}`: `none`
   ```

This simulates real-world reuse: save one prompt, adjust config, generate faster.

---

## Phase 5: Create Your Own Documentation Agent (10-15 min)

### Goal
Build a custom Copilot agent that generates Mermaid diagrams of your data pipeline.

### Your Tasks

1. **Create your agent file:**

Create a new file: `agents/data_flow_agent.md`

2. **Define the agent with clear instructions:**

Ask Copilot to help you create the agent:

```text
I want to create a Copilot agent called "Data Pipeline Documentarian" that:
1. Analyzes Pandas pipelines and creates Mermaid flowchart documentation
2. Identifies input data sources, transformation steps, and outputs
3. Generates ONLY Mermaid syntax (no explanations)

Create agents/data_flow_agent.md with clear instructions for this agent.
Include an example Mermaid flowchart for a simple pipeline.
```

3. **Test your agent:**

In Copilot Chat, reference your agent:

```text
@agents/data_flow_agent.md
Diagram the complete data pipeline in lab_exercise.py showing all transformations from financial_transactions.csv to final outputs.
```

Copilot should generate a Mermaid diagram.

### Expected Outcome
Your agent generates valid Mermaid flowchart code documenting the data pipeline.

---

## Phase 6: Embed Diagram in README (5 min)

### Goal
Add your generated diagram to the project README.

### Your Tasks

1. **Generate the final diagram:**

Use your agent to generate one final comprehensive diagram of the entire pipeline.

2. **Edit [README.md](README.md):**

Find the section:

```
## Project Diagrams

Paste your generated Mermaid diagram here:
```

Replace with your actual Mermaid code.

3. **Preview in VS Code:**

Install: [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview)

Open README.md and verify your diagram displays correctly.

### Expected Outcome
README contains your Mermaid diagram rendering correctly.

---

## Verification Checklist

- [ ] Phase 1: Can explain the code structure clearly
- [ ] Phase 2: Bug fixed; `python lab_exercise.py` runs without errors
- [ ] Phase 3: Code follows team standards (type hints, constants, docstrings)
- [ ] Phase 4: `pytest tests/test_customer_summary.py -v` passes
- [ ] Phase 5: Custom agent generates valid Mermaid code
- [ ] Phase 6: Diagram embedded in README and displays correctly

---

## Key Takeaways

- **Copilot Explain**: Use to understand unfamiliar code quickly
- **Copilot Debug**: Use specific prompts describing the issue to find bugs
- **Copilot Refactor**: Reference team instructions to automate quality improvements
- **Custom Prompts**: Save effective prompts for reuse on similar tasks
- **Custom Agents**: Define agent behavior to automate specialized tasks

Happy learning!
