# RAP Brain - Project Plan (Phoenix Version)

This document outlines the ground-up rebuild of the RAP Brain project, focusing on a product-first approach, a sophisticated Hebrew rhyme engine, and a song-centric data model, as per the user's "מחשבות שלי" file.

---

### Core Principles

1.  **Creativity First**: The system must be intuitive and adapt to the creative workflow, not dictate it.
2.  **Authentic Hebrew Rhyming**: Rhyme detection will be based on phonetics (sound, nikud, stress), not just spelling.
3.  **Song as the Core**: The central entity is the "Song," to which all other elements (ideas, bars, rhymes) connect.
4.  **Frictionless Capture**: There must be a simple, immediate way to capture fleeting ideas and thoughts.
5.  **No Premature AI**: The rhyme engine will be rule-based. AI can be integrated later if needed.

---

### Phase 1: Foundational Database Schema

*Goal: Build a robust, interconnected database structure in Notion that reflects the new model.*

- [ ] **Task 1.1: Create `Songs` Database**
  - **Purpose**: The master container for each musical piece.
  - **Fields**: `Title` (Title), `Status` (Select: Idea, Drafting, Complete), `Theme` (Text).

- [ ] **Task 1.2: Create `Ideas` Database**
  - **Purpose**: A flexible "inbox" for all raw thoughts, lines, and concepts.
  - **Fields**: `Content` (Title), `Timestamp` (Created Time), `Type` (Select: Lyric Idea, Melody Idea, Concept).

- [ ] **Task 1.3: Create `Rhyme Groups` Database**
  - **Purpose**: To group words based on their *phonetic* sound.
  - **Fields**: `Phonetic Key` (Title - e.g., "ev", "ax"), `Description` (Text).

- [ ] **Task 1.4: Create `Words` Database**
  - **Purpose**: A dictionary of all unique words used.
  - **Fields**: `Word` (Title), `Phonetic Key` (Text - Auto-generated).

- [ ] **Task 1.5: Create `Bars` Database**
  - **Purpose**: To store individual lines or couplets.
  - **Fields**: `Bar` (Title).

- [ ] **Task 1.6: Establish All Relations**
  - [ ] `Songs` <-> `Ideas` (Many-to-Many)
  - [ ] `Songs` <-> `Bars` (Many-to-Many)
  - [ ] `Songs` <-> `Rhyme Groups` (Many-to-Many)
  - [ ] `Bars` <-> `Words` (Many-to-Many)
  - [ ] `Words` <-> `Rhyme Groups` (Many-to-One, a word belongs to one phonetic group)

---

### Phase 2: The Phonetic Rhyme Engine

*Goal: Develop a rule-based Python script to analyze Hebrew words and generate a phonetic key for accurate rhyme grouping.*

- [ ] **Task 2.1: Research Hebrew Morphology Tools**
  - **Action**: Find a Python-friendly library or data source for Hebrew nikud and stress (e.g., `hebrew-tokenizer`, MILA, custom dictionaries).

- [ ] **Task 2.2: Develop `phonetic_engine.py`**
  - **Action**: Create a standalone Python script with a function `get_phonetic_key(word)`.
  - **Logic**:
    1.  Input: A Hebrew word string.
    2.  Process: Use the chosen library to get nikud/stress info.
    3.  Algorithm: Determine the sound of the final stressed syllable (e.g., "כְּאֵב" -> "ev", "שָלָיו" -> "av").
    4.  Output: A consistent phonetic key string.

- [ ] **Task 2.3: Integrate with Notion**
  - **Action**: Create a script (`update_notion_words.py`) that reads from the `Words` database, uses the `phonetic_engine` to generate keys, and updates the `Phonetic Key` and `Rhyme Group` relation for each word in Notion.

---

### Phase 3: The Creative Workflow

*Goal: Design and implement the user-facing workflow for capturing and organizing ideas within Notion.*

- [ ] **Task 3.1: Create "INBOX" Dashboard**
  - **Action**: Design the main project page in Notion.
  - **Features**:
    -   A prominent view of the `Ideas` database, acting as a digital inbox.
    -   Buttons or templates for quickly adding a new `Idea` or a new `Song`.

- [ ] **Task 3.2: Define the "Idea to Song" Funnel**
  - **Workflow**:
    1.  **Capture**: User quickly adds a thought to the `Ideas` database.
    2.  **Triage**: From the INBOX, the user processes ideas. They can be linked to an existing `Song` or used to create a new one.
    3.  **Develop**: Within a `Song` page, the user develops the idea into `Bars`, linking words and rhymes as they go.

- [ ] **Task 3.3: (Future) Frictionless Mobile Capture**
  - **Action**: Plan for a simplified capture method (e.g., iOS Shortcut, a super-simple bot) that does one thing only: adds text to the `Ideas` INBOX.

---
This plan provides a clear, phased approach to building the RAP Brain system from the ground up, ensuring the final product is both powerful and a joy to use. 