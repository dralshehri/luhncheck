Saudi Arabian ID Validator
==========================

|travis| |codecov| |supported-versions| |version|

.. |travis| image:: https://travis-ci.org/dralshehri/sa-id-validator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/dralshehri/saudi-id-validator

.. |codecov| image:: https://codecov.io/github/dralshehri/sa-id-validator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/dralshehri/saudi-id-validator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/saudi-id-validator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/saudi-id-validator

.. |version| image:: https://img.shields.io/pypi/v/saudi-id-validator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/saudi-id-validator

A Python package to validate ID numbers of Saudi Arabian identity cards for
both citizens and residents.

The validation formula is based on `Luhn algorithm`_ which is in wide use
today by many governments to distinguish valid numbers from mistyped or
otherwise incorrect numbers.

.. _`Luhn algorithm`: https://en.wikipedia.org/wiki/Luhn_algorithm

Installation
------------

.. code-block:: bash

    $ pip install saudi-id-validator

Basic Usage
-----------

To validate an ID:

.. code:: python

    from saudi_id_validator import validate

    validate(1071724369)
    # Returns False

The `validate` method will return a boolean (``True`` or ``False``) indicating whether
ID is valid or not.

License
-------

This package is distributed under an MIT licence. See ``LICENSE.rst`` file.

Change Log
----------

**1.0.0 (2018-11-18)**

- First release.
