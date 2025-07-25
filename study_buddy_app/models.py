# ----
# Study Buddy App - Database Models
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from . import db

class User(db.Model):
    """User model for task persistence"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile_picture = db.Column(db.Text, nullable=True)  # Base64 encoded image

class Task(db.Model):
    """Task model for user task management"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))
