import os
import logging
from notion_client import Client

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Notion Client
notion = Client(auth=os.environ.get("NOTION_API_KEY"))

# Get Database IDs from environment variables
rhyme_groups_db_id = os.environ.get("RHYME_GROUPS_DB_ID")
words_db_id = os.environ.get("WORDS_DB_ID")
ideas_db_id = os.environ.get("IDEAS_DB_ID")
bars_db_id = os.environ.get("BARS_DB_ID")
songs_db_id = os.environ.get("SONGS_DB_ID")


def get_all_rhyme_groups():
    """
    Fetches all pages from the Rhyme Groups database.
    Returns a simplified list of rhyme group objects.
    """
    logging.info("Attempting to fetch all rhyme groups...")
    try:
        response = notion.databases.query(database_id=rhyme_groups_db_id)
        results = response.get("results")
        logging.info(f"Successfully received {len(results)} items from Notion.")

        rhyme_groups = []
        for page in results:
            try:
                # Extract the title from the page properties
                title_property = page.get("properties", {}).get("Name", {})
                title_list = title_property.get("title", [])
                if title_list:
                    group_name = title_list[0].get("plain_text")
                    rhyme_groups.append({
                        "id": page.get("id"),
                        "name": group_name
                    })
                else:
                    logging.warning(f"Page with ID {page.get('id')} has no title text.")
            except Exception as e:
                logging.error(f"Error processing page {page.get('id')}: {e}")
                
        logging.info(f"Successfully processed {len(rhyme_groups)} rhyme groups.")
        return rhyme_groups
    except Exception as e:
        logging.error(f"An error occurred while querying the database: {e}")
        return []

# --- We will add more functions below as we build out the app --- 