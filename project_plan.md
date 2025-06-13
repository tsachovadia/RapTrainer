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

## New Direction: The "Freestyle Capture" Tool

This section outlines a potential new direction for the RapTrainer project, based on our discussion. The core idea is to pivot from a generic rhyme assistant to a specialized tool that captures the creative moments during a live freestyle session.

### The User Story

The user (a rap artist) has a specific creative setup:
- **Music Source:** A YouTube playlist (Jazz, Lo-fi) playing in the background.
- **DAW:** Ableton Live with a microphone channel set up with various effects (Compressor, EQ, Autotune, Reverb, Delay).
- **Control:** A MIDI controller mapped to manipulate these effects in real-time (e.g., toggle autotune, adjust delay feedback/mix).

The user's most creative moments happen in this setup. The problem is that valuable ideas (melodies, lyrics, flows, effect settings) are lost because there's no easy way to capture them without breaking the creative flow.

The goal is to create a system that allows the user to press a single button on their MIDI controller to instantly save a "snapshot" of their last 30-60 seconds of creativity.

### The "Snapshot" Data
A complete snapshot would capture three types of context:
1.  **Audio Context:** The user's vocals.
2.  **Musical Context:** The YouTube track and the precise timestamp.
3.  **Performance Context:** The real-time MIDI controller settings (reverb amount, delay time, etc.).

This snapshot would be saved as a new "Idea" in Notion for later review and development.

### Technical Approach & Phased Rollout

The implementation is complex and should be approached in phases to validate the core concept first.

*   **Phase 1: The Core Audio Capture (MVP)**
    *   **Goal:** Test the fundamental value of in-flow audio capture.
    *   **Implementation:** A simple, lightweight background application that:
        1.  Listens for a specific, designated MIDI trigger (e.g., an unused pad).
        2.  Constantly records a "rolling buffer" of the last 30-60 seconds of audio from the primary microphone input.
        3.  When triggered, it saves the audio buffer to a local folder as an MP3 file.
    *   **Workflow:** The user would manually upload these audio snippets to Notion.

*   **Phase 2: Full Notion Integration**
    *   **Goal:** Remove the manual workflow and automate the Notion entry.
    *   **Implementation:** Enhance the background app to:
        1.  Use the Notion API.
        2.  When triggered, automatically create a new page in a "Freestyle Ideas" database.
        3.  Upload the captured audio file directly to that new page.

*   **Phase 3: Adding Musical & Performance Context**
    *   **Goal:** Capture the full context of the creative moment.
    *   **Implementation:** This is the most complex part.
        *   **MIDI Data:** The app would also log the last known values for the specified MIDI CC messages and save them as properties in the Notion page.
        *   **YouTube Data (The Challenge):**
            *   **Option A (Most Robust):** A custom browser extension that communicates with the background app to provide the current URL and timestamp. (High complexity).
            *   **Option B (Best Balance):** An in-app YouTube player. The user would play their beats through the RapTrainer app itself, giving us full control and knowledge of the musical context. (Medium complexity).
            *   **Option C (Manual MVP):** The app only saves a timestamp. The user manually cross-references their YouTube history to find the beat. (Low complexity, poor UX).
    *   **Recommendation:** Start with Option B for the best balance of feasibility and user experience.

This new direction transforms RapTrainer from a simple utility into a powerful, integrated creative partner that solves a very specific and high-value problem for the artist.

This plan provides a clear, phased approach to building the RAP Brain system from the ground up, ensuring the final product is both powerful and a joy to use. 