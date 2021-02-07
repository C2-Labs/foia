# FOIA Demo Site

This site is used for customer demonstration of a Django-based architecture for re-imagining the Freedom of Information Act (FOIA) application hosted by the Environmental Protection Agency (EPA).

# Pre-Requisites

- Python 3.8 or greater
- Django - `pipenv install django~=3.1.6`
- pipenv
- git

# Design

- [Leverages the US Web Design System (USWDS)](https://designsystem.digital.gov/)

# Managing the Virtual Environment

- Start the virtual environment shell with `pipenv shell`
- Run the application/server with  `python manage.py runserver`
- Stop the application with CTRL + C
- Exit the virtual environment with `exit`

# Database Migrations

- Create a migration with `python manage.py makemigrations app_name`
- Apply a migration with `python manage.py migrate`

# Create the God Mode Account

- `python manage.py createsuperuser`