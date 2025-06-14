import os
import logging
from notion_client import Client
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_notion_connection():
    """
    Tests the connection to Notion and to each specific database.
    """
    logging.info("--- Starting Notion Connection Health Check ---")
    
    # Load environment variables from .env file in the current directory
    load_dotenv()

    notion_api_key = os.environ.get("NOTION_API_KEY")
    if not notion_api_key or notion_api_key == "YOUR_SECRET_API_KEY_HERE":
        logging.error("CRITICAL: NOTION_API_KEY is not set in the .env file.")
        return

    logging.info("Notion API Key found.")
    
    try:
        notion = Client(auth=notion_api_key)
        logging.info("Notion client initialized successfully.")
    except Exception as e:
        logging.error(f"CRITICAL: Failed to initialize Notion client: {e}")
        return

    databases = {
        "Rhyme Groups": os.environ.get("RHYME_GROUPS_DB_ID"),
        "Words": os.environ.get("WORDS_DB_ID"),
        "Ideas": os.environ.get("IDEAS_DB_ID"),
        "Bars": os.environ.get("BARS_DB_ID"),
        "Songs": os.environ.get("SONGS_DB_ID"),
    }

    all_dbs_ok = True
    for name, db_id in databases.items():
        if not db_id or "YOUR_" in db_id:
            logging.error(f"Database '{name}' FAILED: ID is not set in the .env file.")
            all_dbs_ok = False
            continue
        try:
            notion.databases.retrieve(database_id=db_id)
            logging.info(f"Database '{name}' connection... SUCCESS.")
        except Exception as e:
            logging.error(f"Database '{name}' connection... FAILED. Error: {e}")
            all_dbs_ok = False
    
    if not all_dbs_ok:
        logging.error("One or more database connection tests failed. Aborting further tests.")
        return

    logging.info("--- All databases are connected. Now testing data fetching... ---")
    
    # Import and test the service function
    try:
        from rhyme_app.notion_service import get_all_rhyme_groups
        logging.info("Attempting to fetch rhyme groups using notion_service...")
        rhyme_groups = get_all_rhyme_groups()
        if rhyme_groups is not None:
             logging.info(f"SUCCESS: Fetched {len(rhyme_groups)} rhyme groups.")
             # print(rhyme_groups) # Uncomment for detailed output
        else:
             logging.error("FAILURE: The function get_all_rhyme_groups returned None.")
    except Exception as e:
        logging.error(f"FAILURE: An error occurred while testing get_all_rhyme_groups: {e}")

    logging.info("--- Health Check Complete ---")


if __name__ == "__main__":
    test_notion_connection() 