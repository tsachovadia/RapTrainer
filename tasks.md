# Project Tasks: RapTrainer

## Phase 0: Core Notion Database Setup (Completed)
*Goal: Build the foundational, interconnected set of Notion databases.*
- [x] **Task 0.1: Create the Five Core Databases in Notion**
- [x] **Task 0.2: Establish All Database Relations**
- [ ] **Task 0.3: Manually Configure Rollup Properties**

---
## Phase 1: Web Application MVP (High Priority)
*Goal: Build a simple web application to serve as a complete, user-friendly interface for the Notion database system.*

- [ ] **Task 1.1: High-Level Design & Architecture**
    - [x] Define the multi-page application structure (Home, Rhyme Groups, Bars, Ideas).
    - [x] Specify the user flow for viewing, adding, and linking data.
    - [x] Document the Notion API communication strategy.

- [x] **Task 1.2: Set Up Web Application Environment**
    - [x] Create directory structure (`rhyme_app`, `templates`, `static`).
    - [x] Initialize Flask application.
    - [x] Create `.env` to store Notion API Key and Database IDs.
    - [x] Add dependencies (`flask`, `python-dotenv`, `notion-client`) to `requirements.txt`.

- [ ] **Task 1.3: Backend - Core Notion Service**
    - [x] Create a `notion_service.py` to encapsulate all communication with the Notion API.
    - [x] Implement functions to fetch all items from each database (get_rhyme_groups).
    - [ ] Implement functions to fetch detailed data for a single rhyme group (words, bars).
    - [ ] Implement the `check_word` and `add_word` logic.
    - [ ] Implement a function to add new `Ideas`.

- [ ] **Task 1.4: Backend - Flask Routes**
    - [x] Create routes for each page (`/`, `/rhyme-groups`).
    - [ ] Create a new route for the rhyme group detail page (`/rhyme-groups/<group_id>`).
    - [ ] Create API endpoints for the frontend to call (`/api/add_word`, etc.).

- [ ] **Task 1.5: Frontend - HTML Templates**
    - [x] Create a base template (`base.html`) with navigation.
    - [x] Create HTML files for the main pages (`index.html`, `rhyme_groups.html`).
    - [ ] Create the HTML file for the rhyme group detail page.
    - [ ] Update the rhyme groups list to include word counts and links.

- [ ] **Task 1.6: Frontend - Dynamic Behavior (JavaScript)**
    - [ ] Write JavaScript to handle the interactive form submissions without full page reloads.
    - [ ] Implement logic to dynamically display suggestions and success/error messages.

- [ ] **Task 2.1**: Implement editing and deleting of items.
- [ ] **Task 2.2**: Add search and filtering capabilities to the pages.

## Future Phases (On Hold)
*These ideas will be revisited after the core system is built and validated.*
- [ ] **Freestyle Capture Tool**
- [ ] **Advanced Song Analytics** 