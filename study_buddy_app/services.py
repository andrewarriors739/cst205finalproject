# ----
# Study Buddy App - Services Layer
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from .models import User, Task
from .data import users_data_storage, study_buddy_matches
from . import db

class UserService:
    """Service class for user-related operations"""
    
    @staticmethod
    def create_or_get_user(username):
        """Create user in DB if not existing, return user object"""
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        return user
    
    @staticmethod
    def store_user_data(username, course, study_style):
        """Store user details in memory for matching (existing logic)"""
        users_data_storage[username] = {
            'course': course,
            'study_style': study_style,
        }
    
    @staticmethod
    def update_profile_picture(user, profile_picture_data):
        """Update user's profile picture"""
        user.profile_picture = profile_picture_data
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_profile_picture(username):
        """Get user's profile picture data"""
        user = User.query.filter_by(username=username).first()
        return user.profile_picture if user else None

class TaskService:
    """Service class for task-related operations"""
    
    @staticmethod
    def create_task(description, user):
        """Create a new task for a user"""
        if description.strip():
            new_task = Task(description=description.strip(), user=user)
            db.session.add(new_task)
            db.session.commit()
            return new_task
        return None
    
    @staticmethod
    def get_user_tasks(user_id):
        """Get all tasks for a user"""
        return Task.query.filter_by(user_id=user_id).order_by(Task.id.desc()).all()
    
    @staticmethod
    def delete_task(task_id, user_id):
        """Delete a task if it belongs to the user"""
        task = Task.query.get_or_404(task_id)
        if task.user_id == user_id:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def toggle_task_completion(task_id, user_id):
        """Toggle task completion status if it belongs to the user"""
        task = Task.query.get_or_404(task_id)
        if task.user_id == user_id:
            task.complete = not task.complete
            db.session.commit()
            return True
        return False

class MatchingService:
    """Service class for study buddy matching operations"""
    
    @staticmethod
    def get_matches_for_user(username):
        """Get study buddy matches for a user based on course"""
        user_course = users_data_storage.get(username, {}).get('course')
        return [
            buddy for buddy in study_buddy_matches
            if user_course == buddy['course']
        ]
