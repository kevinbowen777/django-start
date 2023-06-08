*******
Testing
*******

Running the Tests
=================

.. code-block:: console

   $ python manage.py runserver
   $ docker compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -s black-3.12 
   $ nox -s docs-3.11 
   $ nox -rs lint-3.9  (Use the 'r' flag to reuse existing session)
   $ nox -s safety  (will run tests against all Python versions)
   $ nox -s tests 
