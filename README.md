## django_start

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_start.svg)](https://github.com/kevinbowen777/django_start/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- django_start - A Django framework reference repository

 - A reference template of "best practices" & standards used in my collection
   of [Web Framework
   Projects](https://github.com/kevinbowen777/web-project-index). This
   repository runs a Django 4.1.1 web application demonstrating some of this
   functionality.

##### Table of Contents
 - [Features](#Features)
 - [Installation](#Installation)
 - [Testing](#Testing)
 - [Application Demo](#Application Demo)
 - [Screenshots](#Screenshots)
 - [Reporting Bugs](#Reporting Bugs)

---
<a name="Features"/>
## Features
 - Application
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
     - image carousel
     - pagination template
 - Dev/testing
     - basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generation
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage

---
<a name="Installation"/>
### Installation
 - `git clone https://github.com/kevinbowen777/django_start.git`
 - `cd django_start`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---
<a name="Testing"/>
### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---
<a name="Application Demo"/>
### Application Demo:
A live application demonstration hosted at Heroku
 - [django-start](https://kbowen-django-start.herokuapp.com/)

---
<a name="Screenshots"/>
### Screenshots

---
<a name="Reporting Bugs"/>
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_start/issues)
      to view currently open bug reports or open a new issue.
