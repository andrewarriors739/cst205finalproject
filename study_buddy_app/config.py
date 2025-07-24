# ----
# Study Buddy App - Configuration
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

class Config:
    """Application configuration class"""
    SECRET_KEY = 'super_secret_key_12345'  # TODO: Use environment variable for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///studybuddy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # TODO: Consider environment variables for debug/production mode
