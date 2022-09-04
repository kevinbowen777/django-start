## django_start

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_start.svg)](https://github.com/kevinbowen777/django_start/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>


- Django framework reference repository

 - A basic demonstration of Django functionality.
 - A reference template of "best practices" & standards to be employed in [my other Django projects](https://github.com/kevinbowen777/web-project-index).  See the [Features](#Features) section for details on the functionality provided.

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

### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`


---
## Features
 - User registration with email verification & social(GitHub) login
 - Bootstrap4 & crispy-forms decorations
 - Customizable user profile pages with bio, profile pic, & country flags
 - image carousel
 - pagination template
 - basic module testing templates
 - Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

### Live Demo on Heroku:
 - [django-start](https://kbowen-django-start.herokuapp.com/)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_start/issues)
      to view currently open bug reports or open a new issue.
