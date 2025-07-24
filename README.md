# Study Buddy App
> CST205 - Summer 2025 Final Project

Last Updated 7/24/2025

## Overview
**Study Buddy** is a student-focused web application designed to help college students stay organized, manage study sessions, and connect with peers who share similar academic goals. Built as part of the CST 205 Design Project, this app blends task tracking, Pomodoro time management, and a study partner matching system into a clean, intuitive interface.

## Project Team
- Alexis Chavarria
- Anthony Jordan Lagura
- James Lindfors
- Andre Gutierrez

## Technologies
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (external stylesheet)

## Features
- **Sign-Up Form**: Students create a simple profile with their course and study style preferences.
- **Study Buddy Matching**: Automatically pairs users with other students who share similar course and study style preferences.
- **Task Management**: A dashboard that allows users to create and view personal to-do lists.
- **Pomodoro Timer**: A focused work session tool with a 25-minute countdown and start/reset controls.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/andrewarriors739/cst205finalproject 
   ```
2. Navigate to the project directory:
   ```bash
    cd cst205finalproject
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    Optionally, you can create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Run the Flask application:
    ```bash
    python -m study_buddy_app
    ```

5. Open your web browser and go to `http://localhost:5000` to access the app.

## Project Structure
```
study_buddy_app/
├── __init__.py          # Application factory
├── __main__.py          # Module entry point
├── config.py            # Configuration settings
├── models.py            # Database models
├── routes.py            # Route handlers
├── services.py          # Business logic
├── data.py              # Data storage and placeholders
├── studyapp.py          # Alternative entry point
├── static/              # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
└── templates/           # HTML templates
    ├── dashboard.html
    ├── index.html
    ├── pomodoro.html
    └── signup.html
```

## Design Principles
- **Clean UI**: All pages follow a consistent visual style defined in a shared `style.css` file.
- **Accessibility**: Inputs and displays are stacked vertically for clarity and mobile-friendliness.
- **Session-Based**: Users stay logged in through session cookies with a secret key.

## Future Enhancements
- Implement chat functionality for real-time communication between study buddies.
- Add calendar integration to sync study sessions and deadlines.