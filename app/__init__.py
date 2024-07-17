# app/__init__.py

from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Configuration for PostgreSQL
    app.config['POSTGRES_HOST'] = os.getenv('DB_HOST')
    app.config['POSTGRES_USER'] = os.getenv('DB_USER')
    app.config['POSTGRES_PASSWORD'] = os.getenv('DB_PASSWORD')
    app.config['POSTGRES_DB'] = os.getenv('DB_NAME')

    # Importing routes (adjust as per your routes structure)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
