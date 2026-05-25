# Prompt Template: API Summary Endpoints

Generate FastAPI endpoints for transaction summary aggregation. Use this template with different configurations so each endpoint can be created by changing only the placeholders.

```text
---
description: "Generate a FastAPI endpoint for transaction summary aggregation"
---
Implement a Python endpoint in backend/routes/transactions.py using this configuration:

- Endpoint name: {endpoint_name}
- Route: {route}
- Input parameters: {input_parameters}
- Filter logic: {filter_logic}
- Group-by field: {group_by_field}
- Aggregate fields: {aggregate_fields}
- Return type: {return_type}
- Output schema: {output_schema}
- Error handling: {error_handling}

Requirements:
- Use FastAPI and Pydantic idioms
- Add complete type hints for parameters and return values
- Add a Google-style docstring
- Preserve existing behavior unless the config explicitly changes it
- Keep output deterministic and testable
- Follow team standards in track-b-instructions.md
```

Example configurations:

```text
### Configuration A
- `{endpoint_name}`: `get_summary_by_merchant`
- `{route}`: `/transactions/summary/by-merchant/{merchant_category}`
- `{input_parameters}`: `merchant_category: str`
- `{filter_logic}`: `merchant_category matches the route parameter`
- `{group_by_field}`: `merchant_category`
- `{aggregate_fields}`: `count, total_amount, average_amount`
- `{return_type}`: `SummaryResponse`
- `{output_schema}`: `{category, total_amount, transaction_count, average_amount}`
- `{error_handling}`: `return 404 when no transactions are found`

### Configuration B
- `{endpoint_name}`: `get_summary_by_date_range`
- `{route}`: `/transactions/summary/by-date-range`
- `{input_parameters}`: `start_date: date, end_date: date, group_by: str`
- `{filter_logic}`: `timestamp is between start_date and end_date`
- `{group_by_field}`: `day | week | month`
- `{aggregate_fields}`: `count, total_amount`
- `{return_type}`: `list[SummaryResponse]`
- `{output_schema}`: `summaries grouped by the selected time period`
- `{error_handling}`: `validate date format and return 400 for invalid ranges`

### Configuration C
- `{endpoint_name}`: `get_top_merchants`
- `{route}`: `/transactions/top-merchants`
- `{input_parameters}`: `limit: int = 10`
- `{filter_logic}`: `all transactions`
- `{group_by_field}`: `merchant_category`
- `{aggregate_fields}`: `count, total_amount`
- `{return_type}`: `list[MerchantSummary]`
- `{output_schema}`: `top merchants sorted by transaction count descending`
- `{error_handling}`: `return deterministic results even when multiple merchants tie`
```
