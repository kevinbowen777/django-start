## django_start - Django framework reference repository

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_start.svg)](https://github.com/kevinbowen777/django_start/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

The purpose of this repository is twofold:

 - A basic demonstration of Django functionality.
 - A reference template of "best practices" & standards to be employed in
    all of my other Django projects. See [Features][#Features].

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


---
## Features
 - User registration with email verification & social(GitHub) login
 - image carousel
 - pagination
 - test examples

### Live Demo on Heroku:
 - [django-start](https://kbowen-django-start.herokuapp.com/)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_start/issues)
      to view currently open bug reports or open a new issue.
