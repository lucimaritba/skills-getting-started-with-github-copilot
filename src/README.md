# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

From the project root, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python -m uvicorn app:app --app-dir src --reload
```

Open the site at http://localhost:8000, or view the API documentation at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Running Tests

From the project root, run:

```bash
python -m pytest -q
```

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/participants/{email}`               | Remove a participant from an activity                               |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
