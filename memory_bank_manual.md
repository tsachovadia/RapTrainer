# Memory Bank Manual

This document explains how to use the Adaptive Memory-Based Assistant System (AMBAS). This system is designed to maintain context, manage tasks, and streamline the development process across different phases of a project.

## Core Concepts

### 1. The Memory Bank

The Memory Bank is a collection of markdown files that serve as the project's long-term memory. It ensures that context is never lost, even across multiple sessions.

**File Structure:**
```
/memory_bank
├── projectbrief.md       # High-level project summary
├── productContext.md     # The "Why": User, problem, goals
├── techContext.md        # The "How": Tech stack, libraries
├── systemPatterns.md     # Architectural decisions and patterns
└── activeContext.md      # What we are focused on *right now*
/tasks.md                 # The single source of truth for all tasks
```

### 2. `tasks.md`

This is the most critical file for day-to-day work. It is the **single source of truth for all tasks**. The assistant will continuously update this file as tasks are defined, worked on, and completed.

### 3. The Development Modes

The assistant operates in distinct modes, each with a specific purpose. You can switch modes by issuing a command like `PLAN`, `IMPLEMENT`, etc.

---

## The Modes in Detail

### VAN (Vision, Analysis, Narrative)
- **Command**: `VAN`
- **Purpose**: To start a new project or a major new feature. The assistant analyzes all existing documents, code, and user notes to create a unified vision and a foundational project plan.
- **Process**:
    1.  The assistant checks for a Memory Bank and `tasks.md`.
    2.  It reads all relevant files to understand the project.
    3.  It populates the Memory Bank with its analysis.
    4.  It creates an initial `tasks.md`.
- **Outcome**: A fully populated Memory Bank and a clear task list to begin work.

### PLAN
- **Command**: `PLAN`
- **Purpose**: To break down large tasks from `tasks.md` into smaller, actionable steps.
- **Process**:
    1.  The assistant focuses on a high-level task.
    2.  It thinks through the technical requirements and dependencies.
    3.  It updates `tasks.md` with a detailed, step-by-step checklist for the chosen task.
- **Outcome**: A clear, low-level implementation plan that the `IMPLEMENT` mode can execute.

### CREATIVE
- **Command**: `CREATIVE`
- **Purpose**: To brainstorm, explore different approaches, and generate creative solutions for a task. This mode is for when the "how" is not yet clear.
- **Process**:
    1.  The assistant explores different solutions, weighing pros and cons.
    2.  It might suggest different libraries, architectures, or UI mockups.
    3.  It works with you to refine the best approach.
- **Outcome**: A well-defined approach, ready to be broken down in `PLAN` mode or executed in `IMPLEMENT` mode.

### IMPLEMENT
- **Command**: `IMPLEMENT`
- **Purpose**: To execute the plan. This is where code is written, files are edited, and commands are run.
- **Process**:
    1.  The assistant picks a specific, actionable task from `tasks.md`.
    2.  It uses its tools (`edit_file`, `run_terminal_cmd`, etc.) to complete the task.
    3.  It updates `tasks.md` by checking off the completed item.
- **Outcome**: Completed code, a new feature, or a fixed bug.

### QA (Quality Assurance)
- **Command**: `QA`
- **Purpose**: To test the implemented work, find bugs, and ensure quality.
- **Process**:
    1.  The assistant reviews the recently implemented code.
    2.  It can write and run tests, or perform linting.
    3.  It identifies issues and adds them as new tasks in `tasks.md`.
- **Outcome**: A more robust and bug-free codebase.

## How to Use the System

1.  **Start with `VAN`**: Begin your project by telling the assistant to `VAN that project`. Provide it with any notes, documents, or high-level ideas you have.
2.  **Move to `PLAN`**: Once the vision is clear, use `PLAN` to create a detailed roadmap for your first major feature.
3.  **`IMPLEMENT` the plan**: Execute the steps one by one. If you get stuck or need ideas, switch to `CREATIVE`.
4.  **`QA` your work**: Before moving on, run a `QA` cycle to ensure everything works as expected.
5.  **Repeat**: Continue the PLAN -> IMPLEMENT -> QA cycle until the project is complete.

The assistant will handle the Memory Bank updates in the background. Your main focus should be on `tasks.md`, which will always reflect the current state of the project. 