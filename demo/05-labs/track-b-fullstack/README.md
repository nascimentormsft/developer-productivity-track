# Track B: Full-Stack API Lab

Welcome to the Full-Stack API Lab! This lab will help you practice code exploration, debugging, refactoring, prompt engineering, and documentation automation using Copilot.

This track intentionally follows the same learning arc as Track A, but through a full-stack API instead of a pandas pipeline. The goal is the same: learn the same Copilot workflows in a different technical setting.

## Lab Phases

1. **Explore the codebase**: Use Copilot to explain the backend and frontend code, trace the request/response flow, and identify what is missing.
2. **Find and fix the bug**: There is a subtle logic bug in the code that affects the results. Use Copilot to help you debug and fix it.
3. **Refactor code smells**: Use the provided team instructions to refactor the code for clarity and maintainability.
4. **Implement a repetitive feature**: Use prompt engineering to automate repetitive endpoint creation from a reusable template.
5. **Create a documentation agent**: Build your own Copilot agent to generate a Mermaid diagram of the API architecture.
6. **Embed your diagram below**: Use the VS Code Mermaid extension to preview your diagram, then paste the Mermaid code here.

---

## Project Diagrams

Paste your generated Mermaid diagram here:

```
<!-- Example:
graph LR
    Client["Client Request"] --> API["FastAPI App"]
    API --> Route1["GET /transactions"]
    API --> Route2["POST /summary"]
    Route1 --> TransactionModel["Transaction Model"]
    Route2 --> SummaryModel["Summary Model"]
-->
```

## Parity Checklist

- Phase 1: Can explain the code structure and trace a request end to end
- Phase 2: Bug fixed; API returns correct summary statistics
- Phase 3: Config created; models have validation; routes have docstrings
- Phase 4: Reusable prompt template created and used for similar endpoints
- Phase 5: Custom agent generates valid Mermaid code
- Phase 6: Diagram embedded in README and displays correctly

---

## Recommended VS Code Extension
- [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview)

---

Happy learning!
