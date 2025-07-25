# ----
# Study Buddy App - Routes
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from .models import User
from .services import UserService, TaskService, MatchingService
from .image_service import ImageService

# Create blueprint for routes
main = Blueprint('main', __name__)

# ---- Routes (Minimal, some unimplemented features) ----
@main.route('/')
def upstart_home():
    return render_template('index.html')

@main.route('/signup', methods=['GET', 'POST'])
def unique_signup():
    if request.method == 'POST':
        chosen_username = request.form['username']
        fav_course = request.form['course']
        friend_style = request.form['study_style']

        # Handle profile picture upload
        profile_picture_data = None
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and ImageService.is_valid_image(file):
                profile_picture_data = ImageService.process_profile_picture(file)
                if not profile_picture_data:
                    flash('Error processing image. Please try a different file.', 'error')
                    return render_template('signup.html')

        # Create user in DB if not existing (for task persistence)
        user = UserService.create_or_get_user(chosen_username)
        
        # Update user with profile picture if provided
        if profile_picture_data and user:
            UserService.update_profile_picture(user, profile_picture_data)
        
        # Store user details in memory for matching (existing logic)
        UserService.store_user_data(chosen_username, fav_course, friend_style)
        
        session['username'] = chosen_username
        return redirect(url_for('main.dashboard_view'))
    return render_template('signup.html')

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard_view():
    if 'username' not in session:
        return redirect(url_for('main.unique_signup'))
    current_username = session['username']

    # Use existing in-memory storage for matching logic
    dashboard_matches = MatchingService.get_matches_for_user(current_username)

    # Get DB user object for task actions
    current_user = User.query.filter_by(username=current_username).first()
    if not current_user:
        return redirect(url_for('main.unique_signup'))

    if request.method == 'POST':
        fresh_task = request.form['task_entry']
        TaskService.create_task(fresh_task, current_user)
        return redirect(url_for('main.dashboard_view'))

    # Retrieve persistent tasks for logged-in user
    user_tasks = TaskService.get_user_tasks(current_user.id)
    
    # Get user's profile picture
    profile_picture = UserService.get_user_profile_picture(current_username)

    return render_template(
        'dashboard.html',
        learner=current_username,
        match_suggestions=dashboard_matches,
        task_list=user_tasks,
        profile_picture=profile_picture
    )

# Add routes to remove and complete tasks

@main.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('main.unique_signup'))
    
    current_user = User.query.filter_by(username=session['username']).first()
    TaskService.delete_task(task_id, current_user.id)
    
    return redirect(url_for('main.dashboard_view'))

@main.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('main.unique_signup'))
    
    current_user = User.query.filter_by(username=session['username']).first()
    TaskService.toggle_task_completion(task_id, current_user.id)
    
    return redirect(url_for('main.dashboard_view'))

@main.route('/pomodoro')
def pomodoro_page():
    return render_template('pomodoro.html')

@main.route('/logout')
def session_logout():
    session.clear()
    return redirect(url_for('main.upstart_home'))