# ----
# Study Buddy App - Flask Application Factory
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Import and apply configuration
    from .config import Config
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    # Create database tables
    with app.app_context():
        from . import models  # Models imported to ensure they're registered
        db.create_all()
    
    return app
