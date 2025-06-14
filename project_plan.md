# RAP Brain - Project Plan

This document outlines the build of the RAP Brain project, focusing on a product-first approach and a song-centric data model. The core of this project is a sophisticated set of interconnected Notion databases to manage creative ideas.

---

### Core Principles

1.  **Creativity First**: The system must be intuitive and adapt to the creative workflow, not dictate it.
2.  **Song as the Core**: The central entity is the "Song," to which all other elements (ideas, bars, rhymes) connect.
3.  **Frictionless Capture**: There must be a simple, immediate way to capture fleeting ideas and thoughts into a central inbox.
4.  **Manual Rhyme Grouping**: Rhyme associations will be made manually by the user, allowing for creative and nuanced connections rather than automated phonetic analysis.

---

### Phase 1: Foundational Database Schema & Workflow
*Goal: Build a robust, interconnected database structure in Notion and define the primary user workflow for capturing and organizing ideas.*

- [ ] **Task 1.1: Unify and Create the Core Notion Databases**
    - **Action**: Based on the new unified schema, create the following databases in Notion.
        - `Songs`: The master container for each musical piece.
        - `Ideas`: A flexible "inbox" for all raw thoughts, lines, and concepts.
        - `Rhyme Groups`: To group words based on user-defined relationships.
        - `Words`: A dictionary of all unique words used.
        - `Bars`: To store individual lines or couplets.
    - **Action**: Establish all the necessary `Relation` fields between these databases to create a fully interconnected system.

- [ ] **Task 1.2: Design the "Idea Funnel" Workflow**
    - **Action**: Design the main project dashboard in Notion.
    - **Workflow Steps**:
        1.  **Capture**: User quickly adds a thought to the `Ideas` database. This is the central inbox.
        2.  **Triage**: From the inbox, the user processes ideas. An idea can be archived, deleted, or linked to a `Song`.
        3.  **Develop**: Within a `Song` page, the user develops the idea into `Bars`, creating new `Words` and linking them to `Rhyme Groups` as the song takes shape.

- [ ] **Task 1.3: Plan for a Quick Capture Mechanism**
    - **Action**: Research and define the simplest possible method for adding to the `Ideas` database from a mobile device (e.g., Notion mobile app, a custom iOS Shortcut, or a simple email-to-Notion integration).

---

### Future Direction: Advanced Tooling (Post-MVP)

- **Freestyle Capture Tool**: The concept of a background app to capture live freestyle sessions with a MIDI trigger is a powerful future extension. It will be revisited after the core database workflow is established and validated.
- **Automated Workflows**: Scripts to automate certain tasks, such as suggesting potential rhyme connections or analyzing song structure, can be explored in a later phase.

This plan provides a clear, phased approach to building the RAP Brain system from the ground up, ensuring the final product is both powerful and a joy to use. 