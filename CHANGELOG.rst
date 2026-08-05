.. _`changelog`:

=========
Changelog
=========

``django-start`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-start/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-start 0.3.6 (2026-08-05)
===============================

Improved documentation
----------------------

-  (`#613 <https://github.com/kevinbowen777/django-start/issues/613>`_): Add towncrier 25.8.0.

django-start 0.3.5 (2026-07-21)
===============================

Contributor-facing changes
--------------------------

-  (`#628 <https://github.com/kevinbowen777/django-start/issues/628>`_): Update with Python 3.14.6 & 3.13.14.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#624 <https://github.com/kevinbowen777/django-start/issues/624>`_): Drop support for Python 3.11.


New features
------------

-  (`#595 <https://github.com/kevinbowen777/django-start/issues/595>`_): Upgrade to Django 6.0.

django-start 0.3.4 (2025-11-17)
===============================

Contributor-facing changes
--------------------------

-  (`#570 <https://github.com/kevinbowen777/django-start/issues/570>`_): Bump Poetry version to 2.1.4.

-  (`#580 <https://github.com/kevinbowen777/django-start/issues/580>`_): Add Python 3.14 support.


New features
------------

-  (`#527 <https://github.com/kevinbowen777/django-start/issues/527>`_): Upgrade Django to 5.2.7.

-  (`#584 <https://github.com/kevinbowen777/django-start/issues/584>`_): Upgrade Django to 5.2.8.

django-start 0.3.3 (2025-04-29)
===============================

Contributor-facing changes
--------------------------

-  (`#522 <https://github.com/kevinbowen777/django-start/issues/522>`_): Upgrade PostgreSQL to 15.11.

-  (`#532 <https://github.com/kevinbowen777/django-start/issues/532>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#530 <https://github.com/kevinbowen777/django-start/issues/530>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#528 <https://github.com/kevinbowen777/django-start/issues/528>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#467 <https://github.com/kevinbowen777/django-start/issues/467>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#534 <https://github.com/kevinbowen777/django-start/issues/534>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#537 <https://github.com/kevinbowen777/django-start/issues/537>`_): Replace safety package with pip-audit.

django-start 0.3.2 (2025-01-06)
===============================

Contributor-facing changes
--------------------------

-  (`#457 <https://github.com/kevinbowen777/django-start/issues/457>`_): Upgrade to psycopg 3.

-  (`#463 <https://github.com/kevinbowen777/django-start/issues/463>`_): Add support for Python 3.13

-  (`#505 <https://github.com/kevinbowen777/django-start/issues/505>`_): Update pyproject for Poetry 2.0.


New features
------------

-  (`#497 <https://github.com/kevinbowen777/django-start/issues/497>`_): Upgrade Django to 5.1.4

django-start 0.3.0 (2023-12-21)
===============================

Contributor-facing changes
--------------------------

-  (`#167 <https://github.com/kevinbowen777/django-start/issues/167>`_): Add docker no venv template.

-  (`#300 <https://github.com/kevinbowen777/django-start/issues/300>`_): Bump Safety version to 2.4.0.

-  (`#334 <https://github.com/kevinbowen777/django-start/issues/334>`_): Upggrade Poetry to 1.7.0.


New features
------------

-  (`#350 <https://github.com/kevinbowen777/django-start/issues/350>`_): Upgrade to Django 5.0.

django-start 0.2.0 (2023-05-13)
===============================

Contributor-facing changes
--------------------------

-  (`#203 <https://github.com/kevinbowen777/django-start/issues/203>`_): Install ruff. Drop flake8 packages.


New features
------------

-  (`#202 <https://github.com/kevinbowen777/django-start/issues/202>`_): Upgrade Django to 4.2.1.

django-start 0.1.0 (2023-05-02)
===============================

Contributor-facing changes
--------------------------

- : Drop pipenv for project management. Add Poetry.

- : Migrate PostgreSQL to 15.2

-  (`#176 <https://github.com/kevinbowen777/django-start/issues/176>`_): Add support for Python 3.12.

-  (`#182 <https://github.com/kevinbowen777/django-start/issues/182>`_): Update Poetry to 1.4.1.


New features
------------

-  (`#162 <https://github.com/kevinbowen777/django-start/issues/162>`_): Upgrade to Django 4.1.7

-  (`#184 <https://github.com/kevinbowen777/django-start/issues/184>`_): Upgrade to Django 4.2.

django-start 0.0.1 (2023-02-23)
===============================

New features
------------

- : Build Docker support for Heroku deployment.

- : Support Django 4.0.3, Python 3.9.12.


Miscellaneous internal changes
------------------------------

- : Initial commit
