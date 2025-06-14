# Unified Database Schema

```mermaid
graph TD
    subgraph "Core Databases"
        S[🎵 Songs]
        I[💡 Ideas (Inbox)]
        B[🎤 Bars]
        W[📝 Words]
        RG[🗃️ Rhyme Groups]
    end

    subgraph "Workflow"
        direction LR
        Capture(Quick Capture) --> I
        I -- "Triage & Link" --> S
        S -- "Develop In" --> B
    end

    %% --- Relationships (The core of the system) ---

    %% An Idea is the starting point for a Song
    I -- "Can become part of a" --> S

    %% A Song is made of Bars
    S -- "Contains" --> B

    %% A Bar is made of Words
    B -- "Is composed of" --> W

    %% A Word belongs to a Rhyme Group (manually assigned)
    W -- "Belongs to" --> RG

    %% Bars can be associated with a primary Rhyme Group (for discoverability)
    B -- "Primary Rhyme" --> RG

    %% A Song can be associated with multiple Rhyme Groups (for high-level view)
    S -- "Uses Rhymes From" --> RG


    %% --- Styling ---
    style S fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style B fill:#c5e8b7,stroke:#a5c897,color:black
    style W fill:#a8d5ff,stroke:#88b5e0,color:black

    style RG fill:#f9d77e,stroke:#d9b95c,color:black
```

### Explanation of Relationships

This unified schema establishes a powerful, interconnected web for creative development:

*   **Ideas -> Songs (Many-to-Many)**: The `Ideas` database is the central inbox. Any idea can be linked to one or more `Songs` as inspiration or a starting point. A `Song` can be born from multiple `Ideas`.

*   **Songs -> Bars (One-to-Many)**: A `Song` is the primary container for `Bars`. Each Bar belongs to a single `Song`, creating the song's structure.

*   **Bars -> Words (Many-to-Many)**: A `Bar` is composed of multiple `Words`. This allows you to track which words are used in which lines, enabling powerful analysis later (e.g., "show me all the bars where I used the word 'love'").

*   **Words -> Rhyme Groups (Many-to-One)**: This is the core of the rhyme engine. Every `Word` you add to your dictionary is manually assigned to a single `Rhyme Group`. This gives you full creative control. For example, you decide that "כאב", "לבלב", and "חלב" belong to the same group, even if their spelling differs.

*   **Bars -> Rhyme Groups (Many-to-One, "Primary Rhyme")**: To make finding rhymes easier, each `Bar` can be linked to the main `Rhyme Group` it represents (usually based on the last word). This lets you quickly find other bars that could follow it.

*   **Songs -> Rhyme Groups (Many-to-Many)**: At a high level, you can tag a `Song` with all the `Rhyme Groups` used within it. This gives you a quick overview of the song's rhyme palette. 