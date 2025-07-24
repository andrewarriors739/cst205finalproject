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
- **Frontend**: HTML, CSS (external stylesheet), JavaScript
- **Multimedia**: Audio files (WAV format), Confetti animations, Image upload/processing
- **External Libraries**: TSParticles Confetti, Pillow (PIL) for image processing

## Features
- **Enhanced Sign-Up Form**: Students create a profile with their course, study style preferences, and optional profile picture upload
- **Profile Pictures**: Upload and display custom profile pictures with automatic resizing and base64 storage
- **Study Buddy Matching**: Automatically pairs users with other students who share similar course and study style preferences.
- **Task Management**: A dashboard that allows users to create and view personal to-do lists.
- **Enhanced Pomodoro Timer**: A focused work session tool with:
  - 25-minute countdown with start/reset controls
  - **Audio feedback**: Click sounds for button interactions and bell sound for timer completion
  - **Visual celebration**: Confetti animation when timer completes
  - **Professional UI**: Clean, responsive design

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

## Environment Configuration

The application uses environment variables for configuration. A `.env.example` file is provided as a template.

### Setting up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your desired configuration.

### Environment Variables Description

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `ENV` | Application environment (development/production) | `development` |
| `PORT` | Port number for the Flask application | `5000` |
| `DEBUG` | Enable/disable debug mode | `True` |
| `SECRET_KEY` | Secret key for session management | `super_secret_key_12345` |
| `DATABASE_URI` | Database connection string | `sqlite:///instance/studybuddy.db` |

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
├── image_service.py     # Image processing utilities
├── static/              # Static files (CSS, JS, images, audio)
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   ├── js/
│   │   └── pomodoro.js  # Pomodoro timer functionality with confetti
│   └── audio/
│       ├── bell.wav     # Timer completion sound
│       └── click.wav    # Button interaction sound
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
- **Multimedia Enhancement**: Audio feedback and visual animations provide engaging user experience.
- **Modular JavaScript**: External JS files keep code organized and maintainable.

## Future Enhancements
- Implement chat functionality for real-time communication between study buddies.
- Add calendar integration to sync study sessions and deadlines.