# Flask Quiz Application

This repository contains a Flask-based web application for a quiz. Users can register, log in, take a quiz, and view results.

## Project Structure

    quiz - This directory contains the main application code.
        routes.py - The Flask application's main code.
        models.py - Includes database models for User and Question.
        forms.py - Contains form classes for registration, login, and quiz.
        templates/ - HTML templates for different pages (home, registration, login, quiz, results).
        __init__.py- . Package initialization code.
    run.py - File for running application
    instance - Directory, where db is stored.
    README.md  - Description of project

## Functionality

    Home Page: Accessible at / or /home. From here, users can start the quiz.
    Registration: Users can sign up for an account at /register.
    Login: Registered users can log in at /login.
    Quiz: Users can take the quiz at /quiz/<id>, where <id> represents the question number.
    Results: Upon completion, users can view the results at /results.
    Logout: Users can log out at /logout.

## Routes

    / or /home: Home page
    /register: User registration
    /login: User login
    /quiz/<id>: Quiz page for a specific question
    /results: Results page
    /logout: Logout

