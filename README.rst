Saudi ID Validator
==================

This package has been **deprecated** and should be replaced by
`luhn-validator <https://pypi.org/project/luhn-validator/>`_.

To get the same result with **luhn-validator**, see this example:

.. code:: python

    from luhn_validator import validate

    # add length and prefixes
    validate(10717243691, 10, [1, 2])
