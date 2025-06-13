```mermaid
graph TD
    subgraph "Core Entities"
        S[Songs]
        I[Ideas]
        B[Bars]
        W[Words]
        RG[Rhyme Groups]
    end

    subgraph "Creative Workflow"
        direction LR
        Capture(Quick Capture) --> Triage(INBOX / Triage)
        Triage --> Develop(Song Development)
    end

    %% --- Relationships ---
    S ---|"has"| B
    S ---|"can start from"| I
    S ---|"uses"| RG

    B ---|"contains"| W
    I ---|"can evolve into"| B

    W ---|"belongs to"| RG

    %% --- Workflow Connections ---
    Capture --> I
    Triage --- S
    Develop --- B

    %% --- Styling ---
    style S fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style RG fill:#cfc,stroke:#333,stroke-width:2px

    linkStyle 0 stroke-width:2px,fill:none,stroke:orange;
    linkStyle 1 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 2 stroke-width:2px,fill:none,stroke:green;
    linkStyle 3 stroke-width:2px,fill:none,stroke:purple;
    linkStyle 4 stroke-width:2px,fill:none,stroke:red;
    linkStyle 5 stroke-width:2px,fill:none,stroke:teal;
```

### Explanation

*   **Songs**: This is the central hub. A song is composed of `Bars` and `Ideas`, and it utilizes `Rhyme Groups`.
*   **Ideas**: The starting point. A raw thought or concept that can be developed into `Bars` or linked to a `Song`. This is your "inbox".
*   **Bars**: The actual lines of a song. They are made up of `Words`.
*   **Words**: The building blocks. Each word belongs to a phonetic `Rhyme Group`.
*   **Rhyme Groups**: Groups of words that *sound* alike, based on a phonetic key, not just spelling.

This structure supports the desired workflow:
1.  **Capture** an `Idea`.
2.  **Triage** the idea, possibly assigning it to a `Song`.
3.  **Develop** the idea into `Bars` within the context of that `Song`.
4.  The system helps you find rhymes by connecting `Words` to `Rhyme Groups` automatically. 