# Track B: Full-Stack API Lab

Welcome to the Full-Stack API Lab! This lab will help you practice code exploration, debugging, refactoring, prompt engineering, and documentation automation using Copilot.

## Lab Phases

1. **Explore the codebase**: Use Copilot to explain the backend and frontend code, and identify what is missing.
2. **Find and fix the bug**: There is a subtle logic bug in the code that affects the results. Use Copilot to help you debug and fix it.
3. **Refactor code smells**: Use the provided team instructions to refactor the code for clarity and maintainability.
4. **Implement a repetitive feature**: Use prompt engineering to automate repetitive endpoint creation.
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

---

## Recommended VS Code Extension
- [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview)

---

Happy learning!
