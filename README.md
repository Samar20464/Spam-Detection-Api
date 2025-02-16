# Spam Detecttion Api

## Table of Contents

1. Introduction
2. Installation
3. Usage
4. Features

## Introduction

This Spam Detection API project is built using Django and Django REST Framework, providing RESTful endpoints for user registration, contact management, spam reporting, and contact searches. It allows users to register, add contacts, report spam numbers, and search for contact details. The API helps in identifying potential spam callers based on sourced reports.

## Installation 

1. Create a virtual environment and activate 

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate
```

2. Install dependencies:

```bash 
pip install -r requirements.txt

```
3. Apply database migrations:

```bash 
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser for the admin panel:

``` bash
python manage.py createsuperuser
```

5. Run the server:

``` bash
python manage.py runserver
```

7. Open the application:

Admin panel: http://127.0.0.1:8000/admin/

API endpoints: http://127.0.0.1:8000/api

## Usage


### API Endpoints

| Endpoint             | Method | Description                         |
|---------------------|--------|-------------------------------------|
| `/api/users/register/` | POST   | Register a new user                |
| `/api/token/`          | POST   | Obtain access token for authentication |
| `/api/contacts/`       | GET    | View the list of contacts           |
| `/api/spam/`           | POST   | Report a spam contact                |

## Features

- **User Authentication:** Registration and login with JWT tokens.
- **Contact Management:** Add and view contact details.
- **Spam Reporting:** Report spam conact to warn other users.
- **Search Functionality:** Look up contact details by name or number.
- **Admin Dashboard:** Manage users and contacts via the admin panel.

