# luhn-validator

A Python package to validate a variety of identification numbers using Luhn algorithm.

[![Checks Status](https://img.shields.io/github/workflow/status/dralshehri/luhn-validator/Checks/main?event=push&label=checks)][checks]
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage]
[![Code Quality](https://img.shields.io/codefactor/grade/github/dralshehri/luhn-validator/main?&label=codefactor)][quality]
[![PyPI Version](https://img.shields.io/pypi/v/luhn-validator)][pypi-version]
[![Package License](https://img.shields.io/github/license/dralshehri/luhn-validator)][license]

[checks]: https://github.com/dralshehri/luhn-validator/actions/workflows/checks.yml
[coverage]: https://github.com/dralshehri/luhn-validator/actions/workflows/checks.yml
[quality]: https://www.codefactor.io/repository/github/dralshehri/luhn-validator/overview/main
[pypi-version]: https://pypi.python.org/pypi/luhn-validator
[license]: https://github.com/dralshehri/luhn-validator/blob/main/LICENSE

## Overview

The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm,
named after its creator, IBM scientist Hans Peter Luhn, is a simple checksum formula used
to validate a variety of identification numbers, such as:

- US National Provider Identifier numbers.
- Canadian Social Insurance Numbers.
- Saudi Arabia National and Resident ID numbers.
- South African ID numbers.
- Swedish National identification numbers.
- Swedish Corporate Identity Numbers (OrgNr).
- Greek Social Security Numbers (ΑΜΚΑ).
- Credit card numbers.
- IMEI numbers.

The algorithm is in the public domain and is in wide use today. It was designed to
protect against accidental errors. Most credit cards and many government identification
numbers use the algorithm as a simple method of distinguishing valid numbers from
mistyped or otherwise incorrect numbers.

## Features

- Simple API to validate numbers based on Luhn algorithm.
- Extended validation to cover number length and/or prefix(es).
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested with 100% test coverage.

## Installation

To install using `pip`, run:
```shell
pip install luhn-validator
```

## Usage Examples

```pycon
>>> from luhn_validator import validate

>>> # Simple validation
>>> validate(1101798278)
True

>>> # Validate number and check length
>>> validate(1101798278, 9)
False

>>> # Validate number and check if length is 10 and starts with either 1 or 2
>>> validate(1101798278, 10, [1, 2])
True
```

## API Reference

### <kbd>function</kbd> `validate`

```python
validate(
    number: int,
    length: Optional[int] = None,
    prefix: Optional[Union[int, List[int]]] = None,
) -> bool
```

Validate format and checksum of an identification number based on Luhn algorithm.

**Args:**

- **`number`**: Identification number to validate.
- **`length`**: How many digits the number must contain. (The default is `None`,
  which implies skipping the length check).
- **`prefix`**: Exact digit(s) the number must start with. When a list of digits is
  provided, one of the values must match. (The default is `None`, which implies
  skipping the prefix check).

**Returns:**

- `True` when the number is valid, otherwise `False`.

## License

This project is licensed under the terms of the MIT license.
