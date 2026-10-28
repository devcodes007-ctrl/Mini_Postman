# Mini Postman

A beginner-friendly API testing project built with Django and Python.

## Overview

Mini Postman is a web-based project inspired by Postman. It demonstrates how to create HTTP endpoints and return structured JSON responses using Django.

## Current Features

- Welcome API endpoint
- API information endpoint
- API health-check endpoint
- JSON responses
- Django URL routing
- Git version control

## Technology Stack

- Python 3
- Django 5.2
- SQLite
- Git and GitHub

## Project Structure

```text
Mini_Postman/
├── api_tester/
│   ├── migrations/
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone or download the project

Open a terminal in the project directory.

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python3 manage.py migrate
```

### 5. Start the development server

```bash
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/` | Welcome response |
| GET | `/api/info/` | Project information |
| GET | `/api/health/` | API health status |

## Database

The current development configuration uses SQLite. XAMPP/MariaDB integration is planned as a future enhancement.

## Current Limitations

This is an early-stage project. A full API testing interface, custom request builder, saved requests, request history, and response analysis are not implemented yet.

## Future Improvements

- Support GET, POST, PUT, PATCH, and DELETE requests
- Add request headers and JSON body inputs
- Display status codes, response headers, and response times
- Save requests and view request history
- Build a user-friendly frontend
- Integrate a compatible database
- Add automated tests

## Author

Developed as a learning project to practice Python, Django, HTTP APIs, databases, and Git.
