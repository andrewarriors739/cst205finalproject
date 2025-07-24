# cst205finalproject

# Study Buddy App

## Overview
**Study Buddy** is a student-focused web application designed to help college students stay organized, manage study sessions, and connect with peers who share similar academic goals. Built as part of the CST 205 Design Project, this app blends task tracking, Pomodoro time management, and a study partner matching system into a clean, intuitive interface.

## Project Team
- Alexis Chavarria
- Anthony Jordan Lagura
- James Lindfors
- Andre Gutierrez

## Features
- **Sign-Up Form**: Students create a simple profile with their course and study style preferences.
- **Study Buddy Matching**: Automatically pairs users with other students who share similar course and study style preferences.
- **Task Management**: A dashboard that allows users to create and view personal to-do lists.
- **Pomodoro Timer**: A focused work session tool with a 25-minute countdown and start/reset controls.

## Design Principles
- **Clean UI**: All pages follow a consistent visual style defined in a shared `style.css` file.
- **Accessibility**: Inputs and displays are stacked vertically for clarity and mobile-friendliness.
- **Session-Based**: Users stay logged in through session cookies with a secret key.

## Technologies
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (external stylesheet)

## Updates Since Initial Setup
- Unified styling across all HTML files using `static/css/style.css`
- Replaced inline styles with a shared layout and button design
- Updated dashboard to display match info in a spaced, stacked format
- Centered and enlarged the Pomodoro timer for better visibility
- Added navigation button to return from Pomodoro page to dashboard

## Notes
- Currently uses in-memory storage (non-persistent).
- Future improvements could include persistent storage (JSON/SQLite), chat integration, and calendar syncing.
