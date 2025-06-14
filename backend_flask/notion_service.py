import os
import logging
import json # Import the json library
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
        
        # --- DEBUG LOGGING ---
        if results:
            logging.info("--- Raw Properties for First Rhyme Group ---")
            logging.info(json.dumps(results[0].get("properties"), indent=2, ensure_ascii=False))
            logging.info("-------------------------------------------")
        # --- END DEBUG LOGGING ---
            
        logging.info(f"Successfully received {len(results)} items from Notion.")

        rhyme_groups = []
        for page in results:
            try:
                properties = page.get("properties", {})
                # Extract the title from the page properties
                title_property = properties.get("Name", {})
                title_list = title_property.get("title", [])
                
                # Extract the word count from the rollup property using the correct name
                word_count_property = properties.get("Word Count", {})
                word_count = 0 # Default to 0
                if 'rollup' in word_count_property and 'number' in word_count_property['rollup']:
                    word_count = word_count_property['rollup']['number']

                if title_list:
                    group_name = title_list[0].get("plain_text")
                    rhyme_groups.append({
                        "id": page.get("id"),
                        "name": group_name,
                        "word_count": word_count
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

def get_rhyme_group_details(group_id):
    """
    Fetches the details for a single rhyme group, including its words and related bars.
    """
    logging.info(f"--- Fetching details for group_id: {group_id} ---")
    try:
        # 1. Get the group's name
        logging.info("Step 1: Retrieving group page by ID...")
        group_page = notion.pages.retrieve(page_id=group_id)
        group_name_property = group_page.get("properties", {}).get("Name", {}).get("title", [])
        group_name = group_name_property[0].get("plain_text", "Unknown Group") if group_name_property else "Unknown Group"
        logging.info(f"Successfully retrieved group name: {group_name}")

        # 2. Get all words in this group
        logging.info("Step 2: Querying 'Words' database...")
        words_in_group = []
        words_response = notion.databases.query(
            database_id=words_db_id,
            filter={"property": "\"Rhyme Group\"", "relation": {"contains": group_id}}
        )
        logging.info(f"Found {len(words_response.get('results', []))} related words.")
        for word_page in words_response.get("results", []):
            word_title_property = word_page.get("properties", {}).get("Word", {}).get("title", [])
            if word_title_property:
                word_text = word_title_property[0].get("plain_text")
                words_in_group.append({"id": word_page.get("id"), "text": word_text})

        logging.info("--- Successfully fetched all details ---")
        return {
            "id": group_id,
            "name": group_name,
            "words": words_in_group
        }

    except Exception as e:
        logging.error(f"CRITICAL ERROR in get_rhyme_group_details for group {group_id}: {e}", exc_info=True)
        return None

def create_rhyme_group(name):
    """
    Creates a new page in the Rhyme Groups database.
    """
    logging.info(f"Attempting to create new rhyme group with name: {name}")
    try:
        new_page = notion.pages.create(
            parent={"database_id": rhyme_groups_db_id},
            properties={
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ]
                }
            }
        )
        logging.info(f"Successfully created page with ID: {new_page['id']}")
        return new_page
    except Exception as e:
        logging.error(f"Failed to create page with name {name}: {e}", exc_info=True)
        return None

def update_rhyme_group_name(group_id, new_name):
    """
    Updates the name of a rhyme group page in Notion.
    """
    logging.info(f"Attempting to update name for group ID: {group_id} to '{new_name}'")
    try:
        notion.pages.update(
            page_id=group_id,
            properties={
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": new_name
                            }
                        }
                    ]
                }
            }
        )
        logging.info(f"Successfully updated page name for ID: {group_id}")
        return True
    except Exception as e:
        logging.error(f"Failed to update page name for ID {group_id}: {e}", exc_info=True)
        return False

def delete_rhyme_group(group_id):
    """
    Archives a rhyme group page in Notion (effectively deleting it).
    """
    logging.info(f"Attempting to archive (delete) rhyme group with ID: {group_id}")
    try:
        notion.pages.update(page_id=group_id, archived=True)
        logging.info(f"Successfully archived page with ID: {group_id}")
        return True
    except Exception as e:
        logging.error(f"Failed to archive page with ID {group_id}: {e}", exc_info=True)
        return False

def add_word_to_group(word_text, group_id):
    """
    Creates a new word page and links it to a rhyme group.
    """
    logging.info(f"Attempting to add word '{word_text}' to group {group_id}")
    try:
        new_word_page = notion.pages.create(
            parent={"database_id": words_db_id},
            properties={
                "Word": {"title": [{"text": {"content": word_text}}]},
                "\"Rhyme Group\"": {"relation": [{"id": group_id}]}
            }
        )
        logging.info(f"Successfully created word page with ID: {new_word_page['id']}")
        return new_word_page
    except Exception as e:
        logging.error(f"Failed to create word '{word_text}': {e}", exc_info=True)
        return None

def update_word(word_id, new_text):
    """
    Updates the text of an existing word page.
    """
    logging.info(f"Attempting to update word {word_id} to '{new_text}'")
    try:
        notion.pages.update(
            page_id=word_id,
            properties={
                "Word": {"title": [{"text": {"content": new_text}}]}
            }
        )
        logging.info(f"Successfully updated word {word_id}")
        return True
    except Exception as e:
        logging.error(f"Failed to update word {word_id}: {e}", exc_info=True)
        return False

def delete_word(word_id):
    """
    Archives a word page in Notion.
    """
    logging.info(f"Attempting to archive (delete) word with ID: {word_id}")
    try:
        notion.pages.update(page_id=word_id, archived=True)
        logging.info(f"Successfully archived word {word_id}")
        return True
    except Exception as e:
        logging.error(f"Failed to archive word {word_id}: {e}", exc_info=True)
        return False

# --- We will add more functions below as we build out the app --- 