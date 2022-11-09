## django-start

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django-start.svg)](https://github.com/kevinbowen777/django-start/issues)
  [![Coverage Status](https://coveralls.io/repos/github/kevinbowen777/django-start/badge.svg?branch=master)](https://coveralls.io/github/kevinbowen777/django-start?branch=master)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- django_start - A Django framework reference repository

 - A reference template of "best practices" & standards used in my collection
   of [Web Framework
   Projects](https://github.com/kevinbowen777/web-project-index). This
   repository runs a Django 4.1.x web application demonstrating some of this
   functionality.

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - User registration with email verification & social(GitHub) login using [django-allauth](https://pypi.org/project/django-allauth/)
     - [Bootstrap4](https://pypi.org/project/django-bootstrap4/) & [crispy-forms](https://pypi.org/project/django-crispy-forms/) decorations
     - Customizable user profile pages with bio, profile pic, & [country flags](https://pypi.python.org/pypi/django-countries)
     - Image carousel
     - Pagination template
     - Centered account templates(login, registration, verification, etc.)
 - Dev/testing
     - Basic module testing templates
     - [Coverage](https://pypi.org/project/coverage/) reports in `htmlcov` directory
     - [Debug-toolbar](https://pypi.org/project/django-debug-toolbar/) available. See notes in `config/settings.py` for enabling.
     - Examples of using [Factories](https://pypi.org/project/factory-boy/) & [pytest](https://pypi.org/project/pytest/) fixtures in account app testing
     - [shell_plus](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) with [IPython](https://pypi.org/project/ipython/) via [django-extensions](https://pypi.python.org/pypi/django-extensions/) package
     - [Nox](https://pypi.org/project/nox/) testing sessions for latest Python 3.9, 3.10, and 3.11
         - [black](https://pypi.org/project/black/)
         - [Sphinx](https://pypi.org/project/Sphinx/) documentaion generation
         - linting
             - [flake8](https://pypi.org/project/flake8/)
             - [flake8-bandit](https://pypi.org/project/flake8-bandit/)
             - [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
             - [flake8-import-order](https://pypi.org/project/flake8-import-order/)
         - [safety](https://pypi.org/project/safety/)(python package vulnerability testing)
         - [pytest](https://docs.pytest.org/en/latest/) sessions with [pytest-cov](https://pypi.org/project/pytest-cov/) & [pytest-django](https://pypi.org/project/pytest-django/)
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

---

### Installation
 - `git clone https://github.com/kevinbowen777/django-start.git`
 - `cd django_start`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### Application Demo
A live application demonstration hosted at Heroku
 - [django-start](https://kbowen-django-start.herokuapp.com/)

---

### Screenshots

### Home
![Home](https://github.com/kevinbowen777/django-start/blob/master/images/django-start_home.png)

### Login Page
![Login Page](https://github.com/kevinbowen777/django-start/blob/master/images/django-start_login.png)

### Logged in user with dropdown
![Dropdown detail](https://github.com/kevinbowen777/django-start/blob/master/images/django-start_logged_dropdown.png)

### Profile Page
![Profile Page](https://github.com/kevinbowen777/django-start/blob/master/images/django-start_profile-page.png)

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django-start/issues)
      to view currently open bug reports or open a new issue.
