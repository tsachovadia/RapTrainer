# System Design: RapTrainer

This document outlines the high-level architecture of the RapTrainer application.

## Frontend

The frontend is a single-page application (SPA) built with vanilla JavaScript.

-   **View**: `rhyme_app/templates/rhyme_groups.html`
-   **Logic**: `rhyme_app/static/app.js`

### Features:

-   **CRUD for Rhyme Groups**:
    -   **Create**: Add new rhyme groups via a form.
    -   **Read**: Displays a list of all rhyme groups on page load.
    -   **Update**: Inline editing of rhyme group names.
    -   **Delete**: Remove rhyme groups.
-   **Live Communication Log**: A panel at the bottom of the page shows real-time logs of requests and responses between the frontend and the backend, aiding in debugging.

## Backend (Flask)

The backend is a Flask application serving a RESTful API.

-   **Main Application**: `rhyme_app/app.py`
-   **Notion Service Layer**: `rhyme_app/notion_service.py`

### API Endpoints:

-   `GET /`: Redirects to the main rhyme groups page.
-   `GET /rhyme-groups-page`: Renders the HTML for the single-page application.
-   `GET /rhyme-groups`: Returns a JSON list of all rhyme groups.
-   `POST /rhyme-groups`: Creates a new rhyme group.
-   `PUT /rhyme-groups/<group_id>`: Updates the name of a specific rhyme group.
-   `DELETE /rhyme-groups/<group_id>`: Deletes (archives) a specific rhyme group.
-   `GET /rhyme-groups/<group_id>`: Returns a JSON object with details for a single rhyme group, including its associated words.

## Database (Notion)

Notion is used as the backend database. All data operations (Create, Read, Update, Delete) are performed via the Notion API, abstracted through the `notion_service.py` module. 