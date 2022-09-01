Django Start - A Django web framework template project
======================================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

The template repository for the
`Web Framework Projects <https://github.com/kevinbowen777/web-project-index>`_
assembled by Kevin Bowen.
This repository runs a Django 4.1 application demonstrating some of its
basic functionality.

Features
--------

 * User registration with email verification & social(GitHub) login
 * Bootstrap4 & crispy-forms decorations
 * Customizable user profiles with bio, profile picture & country flags
 * image carousel
 * pagination template
 * basic module testing templates
 * Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation

Installation
------------

To install the django_start project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/django_start.git
   $ cd django_start

Local install:
--------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser
   

Docker install:
---------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run django_start, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Live Application Demonstration on Heroku
----------------------------------------
`kbowen-django-start <https://kbowen-django-start.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the django_start `Issues page <https://github.com/kevinbowen777/django_start/issues>`_ on GitHub.
