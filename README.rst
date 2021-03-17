Saudi ID Validator
==================

A Python package to validate ID numbers of Saudi Arabian identity cards for
both citizens and residents.

|travis| |codecov| |supported| |version| |license|

.. |travis|
   image:: https://img.shields.io/travis/com/dralshehri/saudi-id-validator.svg
   :alt: Build Status
   :target: https://travis-ci.com/dralshehri/saudi-id-validator

.. |codecov|
   image:: https://img.shields.io/codecov/c/github/dralshehri/saudi-id-validator.svg
   :alt: Coverage Status
   :target: https://codecov.io/github/dralshehri/saudi-id-validator

.. |supported|
   image:: https://img.shields.io/pypi/pyversions/saudi-id-validator.svg
   :alt: Supported versions
   :target: https://pypi.python.org/pypi/saudi-id-validator

.. |version|
   image:: https://img.shields.io/pypi/v/saudi-id-validator.svg
   :alt: PyPI Package version
   :target: https://pypi.python.org/pypi/saudi-id-validator

.. |license|
   image:: https://img.shields.io/github/license/dralshehri/saudi-id-validator.svg
   :alt: License
   :target: https://github.com/dralshehri/saudi-id-validator/blob/master/LICENSE

The validation formula is based on `Luhn algorithm`_ which is in wide use
today by many governments to distinguish valid numbers from mistyped or
otherwise incorrect numbers.

.. _`Luhn algorithm`: https://en.wikipedia.org/wiki/Luhn_algorithm

Installation
------------

.. code-block:: bash

    $ pip install -U saudi-id-validator

Basic Usage
-----------

To validate an ID:

.. code:: python

    from saudi_id_validator import validate

    is_valid = validate('1071724369')  # could also be an integer
    print(is_valid)
    # False

The `validate` method will return a boolean (``True`` or ``False``) indicating
whether ID is valid or not.

License
-------

This package is distributed under an MIT license. See `LICENSE`_ file.

.. _LICENSE: https://github.com/dralshehri/saudi-id-validator/blob/master/LICENSE

Change Log
----------

**v1.0.6**

- Fixed the package homepage URL (Thanks to `@ddimmich <https://github.com/ddimmich>`_).
- Updated CI tests to include recent python versions.

**v1.0.5**

- Added params to docstrings.
- Fixed a typo in README.

**v1.0.4**

- Updated README.

**v1.0.3**

- Updated usage example.
- Updated README badges.
- Removed LICENSE file extension.

**v1.0.2**

- Improved README content.

**v1.0.1**

- Fixed some typos in README file.

**v1.0.0**

- First release.
