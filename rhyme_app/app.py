from flask import Flask, render_template, request, jsonify
from flask_dotenv import DotEnv
import os

app = Flask(__name__)
# Use flask-dotenv to find and load the .env file
env = DotEnv()
env.init_app(app, env_file=".env", verbose_mode=True)

# Import our notion_service
from notion_service import get_all_rhyme_groups

@app.route('/')
def home():
    """
    Render the home page for quick capture.
    """
    return render_template('index.html')

@app.route('/rhyme-groups')
def rhyme_groups_page():
    """
    Render the page that displays all rhyme groups.
    """
    groups = get_all_rhyme_groups()
    return render_template('rhyme_groups.html', groups=groups)

if __name__ == '__main__':
    app.run(debug=True) 