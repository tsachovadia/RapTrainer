# RapTrainer: Creative Management System

Welcome to RapTrainer, a custom-built tool to manage your creative workflow for songwriting. This application provides a simple web interface to interact with a powerful Notion database backend, allowing you to easily organize songs, ideas, bars, words, and rhyme groups.

## Project Structure

The project is a monorepo containing two main parts:

-   `backend_flask/`: A Python Flask server that acts as an API layer. It handles all business logic and communication with the Notion API.
-   `frontend_vue/`: A modern web application built with Vue.js and PrimeVue for a rich, interactive user experience.

## Tech Stack

-   **Backend:** Python, Flask, `python-dotenv`, `notion-client`
-   **Frontend:** Vue.js, Vite, PrimeVue (UI Components)
-   **Database:** Notion
-   **Development:** `concurrently` (for running both servers simultaneously)

---

## Getting Started

Follow these instructions to get the development environment up and running.

### 1. Prerequisites

-   Python 3.8+ and `pip`
-   Node.js 16+ and `npm`
-   A Notion account and API key

### 2. Backend Setup

1.  **Create an Environment File:**
    -   Navigate to the `backend_flask` directory.
    -   Create a file named `.env`.
    -   Add your Notion API Key and Database IDs to this file. It should look like this:
        ```
        NOTION_API_KEY="secret_..."
        RHYME_GROUPS_DB_ID="..."
        WORDS_DB_ID="..."
        SONGS_DB_ID="..."
        IDEAS_DB_ID="..."
        BARS_DB_ID="..."
        ```

2.  **Install Python Dependencies:**
    -   From the `backend_flask` directory, create a virtual environment and install the required packages:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        ```

### 3. Frontend Setup

1.  **Install Node Modules:**
    -   From the `frontend_vue` directory, run:
        ```bash
        npm install
        ```

### 4. Running the Application

The project is configured to run both the backend and frontend servers with a single command.

-   From the `frontend_vue` directory, run:
    ```bash
    npm run dev
    ```
-   This will start the Flask server on port `5000` and the Vite frontend server on port `5173`.
-   Open your browser and navigate to `http://localhost:5173` to use the application.

---

## Development Plan (Current Tasks)

This is the current focus of development, migrated from `tasks.md`.

### Phase 2: Build the Rhyme Group List

-   [ ] **2.1:** Create a new component `RhymeGroupList.vue` responsible for displaying the list.
-   [ ] **2.2:** Create a `RhymeGroupItem.vue` component for each item in the list, which will display the group name, word count, and action buttons (initially inactive).
-   [ ] **2.3:** Add a simple form (above the list) to create a new rhyme group.
-   [ ] **2.4:** Implement the logic to send a `POST` request to the server when the form is submitted and refresh the list upon a successful response.

### Phase 3: Word Management within a Rhyme Group

-   [ ] **3.1:** Make each `RhymeGroupItem.vue` clickable. Clicking will show the words associated with that group.
-   [ ] **3.2:** Implement the API call to get the details of a specific group (`/api/rhyme-groups/<id>`).
-   [ ] **3.3:** Create `WordList.vue` and `WordItem.vue` components to display the words.
-   [ ] **3.4:** Add a form to add a new word to the selected group.
-   [ ] **3.5:** Implement the ability to update and delete existing words. 