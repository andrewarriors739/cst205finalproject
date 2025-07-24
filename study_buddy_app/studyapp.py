# ----
# Study Buddy App
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

portal_flask_app = Flask(__name__)
portal_flask_app.secret_key = 'super_secret_key_12345'

# ---- Data Models (Placeholders, except for tasks persistence) ----

users_data_storage = {}  # TODO: Implement a persistent storage solution

study_buddy_matches = [
    # TODO: Replace with real matching algorithm/data models
    {'username': 'aliceK', 'course': 'CS101', 'study_style': 'Morning', 'contact': 'alice@email.com'},
    {'username': 'bobQ',   'course': 'CS205', 'study_style': 'Night',   'contact': 'bobq@email.com'},
    {'username': 'cathyJ', 'course': 'MATH330','study_style': 'Evening','contact': 'cj@email.com'},
]

tasks_data = []  # TODO: Link each user's tasks persistently (Removed for task persistence via DB)

# ---- Persistent Storage Setup for Tasks ----
portal_flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studybuddy.db'
portal_flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(portal_flask_app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

with portal_flask_app.app_context():
    db.create_all()

# ---- Routes (Minimal, some unimplemented features) ----

@portal_flask_app.route('/')
def upstart_home():
    return render_template('index.html')

@portal_flask_app.route('/signup', methods=['GET', 'POST'])
def unique_signup():
    if request.method == 'POST':
        chosen_username = request.form['username']
        fav_course = request.form['course']
        friend_style = request.form['study_style']

        # Create user in DB if not existing (for task persistence)
        user = User.query.filter_by(username=chosen_username).first()
        if not user:
            user = User(username=chosen_username)
            db.session.add(user)
            db.session.commit()

        # Store user details in memory for matching (existing logic)
        users_data_storage[chosen_username] = {
            'course': fav_course,
            'study_style': friend_style,
        }
        session['username'] = chosen_username
        return redirect(url_for('dashboard_view'))
    return render_template('signup.html')

@portal_flask_app.route('/dashboard', methods=['GET', 'POST'])
def dashboard_view():
    if 'username' not in session:
        return redirect(url_for('unique_signup'))
    current_username = session['username']

    # Use existing in-memory storage for matching logic
    dashboard_matches = [
        buddy for buddy in study_buddy_matches
        if users_data_storage.get(current_username, {}).get('course') == buddy['course']
    ]

    # Get DB user object for task actions
    current_user = User.query.filter_by(username=current_username).first()
    if not current_user:
        return redirect(url_for('unique_signup'))

    if request.method == 'POST':
        fresh_task = request.form['task_entry']
        if fresh_task.strip():
            new_task = Task(description=fresh_task.strip(), user=current_user)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('dashboard_view'))

    # Retrieve persistent tasks for logged-in user
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.id.desc()).all()

    # Pass persistent tasks instead of in-memory tasks_data
    return render_template(
        'dashboard.html',
        learner=current_username,
        match_suggestions=dashboard_matches,
        task_list=user_tasks
    )

# Add routes to remove and complete tasks

@portal_flask_app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('unique_signup'))
    task = Task.query.get_or_404(task_id)
    current_user = User.query.filter_by(username=session['username']).first()
    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard_view'))

@portal_flask_app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('unique_signup'))
    task = Task.query.get_or_404(task_id)
    current_user = User.query.filter_by(username=session['username']).first()
    if task.user_id == current_user.id:
        task.complete = not task.complete
        db.session.commit()
    return redirect(url_for('dashboard_view'))

@portal_flask_app.route('/pomodoro')
def pomodoro_page():
    return render_template('pomodoro.html')

@portal_flask_app.route('/logout')
def session_logout():
    session.clear()
    return redirect(url_for('upstart_home'))

if __name__ == '__main__':
    # TODO: Consider environment variables for debug/production mode
    portal_flask_app.run(debug=True)
