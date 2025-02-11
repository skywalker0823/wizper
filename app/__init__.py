from flask import Flask
from pathlib import Path

from .routes import main

def create_app():
    app = Flask(__name__, static_url_path='/',
                static_folder = Path(__file__).parent.parent / 'static',
                template_folder = Path(__file__).parent.parent / 'templates')
    
    # Blueprint
    app.register_blueprint(main)

    return app