# Prompt Template: Category Aggregations

Use this template when an aggregation task repeats the same structure with only small configuration changes.

## Reusable Prompt Template

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

Return only the final function code.
```

## Configurations For This Lab

### Configuration A
- `{function_name}`: `calculate_monthly_savings_by_category`
- `{input_parameters}`: `df: pd.DataFrame, year: int, month: int`
- `{time_scope}`: `specific year and month`
- `{group_by_column}`: `merchant_category`
- `{return_type}`: `dict[str, float]`
- `{output_schema}`: `{category: total_amount}`
- `{filter_logic}`: `timestamp year == year and timestamp month == month`

### Configuration B
- `{function_name}`: `calculate_yearly_category_trend`
- `{input_parameters}`: `df: pd.DataFrame, year: int`
- `{time_scope}`: `all months in a year`
- `{group_by_column}`: `merchant_category`
- `{return_type}`: `dict[str, float]`
- `{output_schema}`: `{category: total_amount}`
- `{filter_logic}`: `timestamp year == year`

### Configuration C
- `{function_name}`: `generate_category_report`
- `{input_parameters}`: `df: pd.DataFrame`
- `{time_scope}`: `all available years and months`
- `{group_by_column}`: `merchant_category`
- `{return_type}`: `pd.DataFrame`
- `{output_schema}`: `rows by year/month/category with aggregated total`
- `{filter_logic}`: `none`

## Usage Notes

- Keep this template fixed.
- For each new aggregation function, copy the template and change only placeholder values.
- If the structure is unchanged, do not rewrite instructions from scratch.

## Usage History

- [ ] Configuration A executed
- [ ] Configuration B executed
- [ ] Configuration C executed
