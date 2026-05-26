# Team Coding Standards for Track B (API)

- Use Pydantic field validation (e.g., Field(gt=0) for positive integers)
- Move hardcoded values to config.py
- Use clear, verb-based names for routes, models, and helpers
- All routes must include Google-style docstrings with parameters and responses
- Prefer deterministic outputs for summaries and tests
- Keep repeated endpoint logic configurable instead of copy/pasting variations
- Use f-strings for formatting
