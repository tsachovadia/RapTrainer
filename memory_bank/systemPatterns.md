# System Patterns: RapTrainer

## Core Pattern: The Notion-as-a-Backend Model

- **Description**: This pattern treats Notion as the complete user interface, database, and application backend. The entire creative workflow is contained within Notion pages and databases. Any external code (Python scripts) would be for one-off automation or data migration tasks, not for core application logic.
- **Workflow**:
    1.  **Capture**: The user creates a new entry directly in the `Ideas` database in Notion (this is the "quick capture").
    2.  **Triage & Develop**: The user works entirely within Notion, using its UI to link `Ideas` to `Songs`, create `Bars`, and manually associate `Words` with `Rhyme Groups` using `Relation` fields.
- **Components**:
    -   **Notion Databases**: Serve as the Model, View, and Controller. They store the data, display it to the user, and provide the tools (relations, rollups, templates) to manipulate it.
- **Use Case**: This is the foundational pattern for the entire Rap Trainer system.

## Future Pattern: The Background Service Model

- **Description**: This pattern describes a long-running background application (a service or daemon) that listens for system-wide events (like a MIDI trigger) to perform an action.
- **Status**: **On Hold**. This pattern will be revisited if the project proceeds with the "Freestyle Capture" tool after the core Notion system is validated.
- **Use Case**: The "Freestyle Capture" tool. 