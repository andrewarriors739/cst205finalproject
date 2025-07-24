# ----
# Study Buddy App TEST
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

from flask import Flask, render_template, request, redirect, session, url_for

portal_flask_app = Flask(__name__)
portal_flask_app.secret_key = 'super_secret_key_12345'

# ---- Data Models (Placeholders) ----

users_data_storage = {}  # TODO: Implement a persistent storage solution

study_buddy_matches = [
    # TODO: Replace with real matching algorithm/data models
    {'username': 'aliceK', 'course': 'CS101', 'study_style': 'Morning', 'contact': 'alice@email.com'},
    {'username': 'bobQ',   'course': 'CS205', 'study_style': 'Night',   'contact': 'bobq@email.com'},
    {'username': 'cathyJ', 'course': 'MATH330','study_style': 'Evening','contact': 'cj@email.com'},
]

tasks_data = []  # TODO: Link each user's tasks persistently

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
    current_user = session['username']
    dashboard_matches = [
        buddy for buddy in study_buddy_matches
        if users_data_storage[current_user]['course'] == buddy['course']
    ]
    if request.method == 'POST':
        # TODO: Add ability to remove tasks, mark complete, etc.
        fresh_task = request.form['task_entry']
        tasks_data.append({'user': current_user, 'desc': fresh_task})
    # TODO: Design dashboard template with study buddy matches and tasks
    return render_template(
        'dashboard.html',
        learner=current_user,
        match_suggestions=dashboard_matches,
        task_list=tasks_data
    )

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
