## django-start

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django-start.svg)](https://github.com/kevinbowen777/django-start/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
  [![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kevinbowen777/261b3eac2838cf0bc3b365335c8323df/raw/covbadge.json)](https://kevinbowen777.github.io/django-start/)

</div>

- django-start - A Django framework reference repository

 - A reference template of "best practices" & standards used in my collection
   of [Web Framework
   Projects](https://github.com/kevinbowen777/web-project-index). This
   repository runs a Django 5.1.x web application demonstrating some of this
   functionality.

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Contributions](#contributions)
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
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)
 - Dev/testing
     - Basic module testing templates
     - [Coverage](https://kevinbowen777.github.io/django-start/) reports on web
     - [Debug-toolbar](https://pypi.org/project/django-debug-toolbar/) available. See notes in `config/settings.py` for enabling.
     - Examples of using [Factories](https://pypi.org/project/factory-boy/) & [pytest](https://pypi.org/project/pytest/) fixtures in account app testing
     - [shell_plus](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) via [django-extensions](https://pypi.python.org/pypi/django-extensions/) package
     - [Pre-commit](https://github.com/pre-commit/pre-commit)
     - [Nox](https://pypi.org/project/nox/) testing sessions for latest Python 3.10, 3.11, 3.12, and 3.13.
         - [Sphinx](https://pypi.org/project/Sphinx/) documentation generation (`nox -s docs`)
         - Generate [Coverage](https://pypi.org/project/coverage/) reports in `htmlcov` directory (`nox -s coverage`)
         - linting (`nox -s lint`)
             - [ruff](https://pypi.org/project/ruff/)
             - [djlint](https://pypi.org/project/djlint/)
         - [safety](https://pypi.org/project/safety/)(python package vulnerability testing) (`nox -s safety`)
         - [pytest](https://docs.pytest.org/en/latest/) sessions with
           [pytest-cov](https://pypi.org/project/pytest-cov/)
           [pytest-django](https://pypi.org/project/pytest-django/) (`coverage run -m pytest`)
  - `run` and `drun` command menus

    A collection of command shortcuts/aliases for frequently used Docker,
    Django, and Nox commands. For a local installation, use the `run` command
    file. For Docker installations, use the `drun` command file.
    (adapted from Nick Janetakis' helpful [docker-django-example](https://github.com/nickjj/docker-django-example)) repository.

    You can run `./run` to get a list of commands and each command has documentation in the run file itself. This comes in handy to run various Docker commands because sometimes these commands can be a bit long to type. 

    *If you get tired of typing `./run` you can always create a shell alias with `alias run=./run` in your `~/.bash_aliases` or equivalent file. Then you'll be able to run `run` instead of `./run`.*

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
     - `docker compose build --build-arg "ENV=DEV"` (include testing/dev dependencies)
     - `docker compose build --build-arg "ENV=PROD"`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/resources/
 - Pre-commit:
     - To add the hook, run the following command in the poetry shell:
         - `pre-commit install`
     - To update the pre-commit hooks, run the following command:
         - `pre-commit autoupdate`

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for coverage, lint, safety, tests)
     - testing supported for Python 3.10, 3.11, 3.12, 3.13
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`
       - `nox`
       - `nox -s coverage-3.12`
       - `nox -s docs-3.11`
       - `nox -rs lint-3.10` (Use the 'r' flag to reuse existing session)
       - `nox -s safety` (will run tests against all Python versions)
       - `nox -s tests`

---

### Application Demo

 - TBD

---

### Screenshots

### Home
![Home](images/django-start_home.png)

### Login Page
![Login Page](images/django-start_login.png)

### Logged in user with dropdown
![Dropdown detail](images/django-start_logged_dropdown.png)

### Profile Page
![Profile Page](images/django-start_profile-page.png)

---

### Contributions

At this time, this project is not accepting pull-requests. You are free to fork
this repository and modify as you see fit.

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django-start/issues)
      to view currently open bug reports or open a new issue.
