from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_dotenv import DotEnv
import os

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Use flask-dotenv to find and load the .env file
env = DotEnv()
env.init_app(app, env_file=".env", verbose_mode=True)

# Import our notion_service
from notion_service import (
    get_all_rhyme_groups, 
    get_rhyme_group_details, 
    delete_rhyme_group,
    create_rhyme_group,
    update_rhyme_group_name,
    add_word_to_group,
    update_word,
    delete_word
)

@app.route('/api/rhyme-groups', methods=['GET'])
def get_rhyme_groups_json():
    """
    Return a JSON list of all rhyme groups.
    """
    groups = get_all_rhyme_groups()
    return jsonify(groups)

@app.route('/api/rhyme-groups', methods=['POST'])
def create_rhyme_group_route():
    """
    Create a new rhyme group.
    """
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"message": "Name is required"}), 400
    
    new_group = create_rhyme_group(name)
    if new_group:
        return jsonify({"message": "Group created successfully", "group": new_group}), 201
    return jsonify({"message": "Failed to create group"}), 500

@app.route('/api/rhyme-groups/<group_id>', methods=['PUT'])
def update_rhyme_group_route(group_id):
    """
    Update a rhyme group's name.
    """
    data = request.get_json()
    new_name = data.get('name')
    if not new_name:
        return jsonify({"message": "Name is required"}), 400

    success = update_rhyme_group_name(group_id, new_name)
    if success:
        return jsonify({"message": "Group updated successfully"}), 200
    return jsonify({"message": "Failed to update group"}), 500

@app.route('/api/rhyme-groups/<group_id>', methods=['DELETE'])
def delete_rhyme_group_route(group_id):
    """
    Delete (archive) a rhyme group.
    """
    success = delete_rhyme_group(group_id)
    if success:
        return jsonify({"message": "Group deleted successfully"}), 200
    return jsonify({"message": "Failed to delete group"}), 500

@app.route('/api/rhyme-groups/<group_id>', methods=['GET'])
def get_rhyme_group_detail_json(group_id):
    """
    Return a JSON object with details for a single rhyme group, including words.
    """
    group_details = get_rhyme_group_details(group_id)
    if group_details:
        return jsonify(group_details)
    return jsonify({"message": "Group not found"}), 404

@app.route('/api/rhyme-groups/<group_id>/words', methods=['POST'])
def add_word_to_group_route(group_id):
    """
    Add a new word to a specific rhyme group.
    """
    data = request.get_json()
    word_text = data.get('text')
    if not word_text:
        return jsonify({"message": "Word text is required"}), 400

    new_word = add_word_to_group(word_text, group_id)
    if new_word:
        return jsonify({"message": "Word added successfully", "word": new_word}), 201
    return jsonify({"message": "Failed to add word"}), 500

@app.route('/api/words/<word_id>', methods=['PUT'])
def update_word_route(word_id):
    """
    Update an existing word.
    """
    data = request.get_json()
    new_text = data.get('text')
    if not new_text:
        return jsonify({"message": "New text is required"}), 400
    
    success = update_word(word_id, new_text)
    if success:
        return jsonify({"message": "Word updated successfully"}), 200
    return jsonify({"message": "Failed to update word"}), 500

@app.route('/api/words/<word_id>', methods=['DELETE'])
def delete_word_route(word_id):
    """
    Delete (archive) an existing word.
    """
    success = delete_word(word_id)
    if success:
        return jsonify({"message": "Word deleted successfully"}), 200
    return jsonify({"message": "Failed to delete word"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 