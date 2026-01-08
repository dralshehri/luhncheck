# LuhnCheck

A Python package to validate identification numbers using the Luhn algorithm with additional optional checks.

<!-- start badges -->

[![Release Status](https://img.shields.io/badge/release-pass-success)][release] [![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage] [![PyPI Downloads](https://static.pepy.tech/badge/luhncheck)][downloads] [![PyPI Version](https://img.shields.io/pypi/v/luhncheck)][pypi-version] [![Package License](https://img.shields.io/github/license/dralshehri/luhncheck)][license]

[release]: https://github.com/dralshehri/luhncheck/releases/latest
[coverage]: https://github.com/dralshehri/luhncheck/releases/latest
[downloads]: https://pepy.tech/project/luhncheck
[pypi-version]: https://pypi.python.org/pypi/luhncheck
[license]: https://github.com/dralshehri/luhncheck/blob/main/LICENSE

<!-- end badges -->

## 📖 Overview

The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, named after its creator, IBM scientist Hans Peter Luhn, is a simple checksum formula used to validate a variety of identification numbers, such as:

- US National Provider Identifier numbers
- Canadian Social Insurance Numbers
- Saudi Arabia National and Resident ID numbers
- South African ID numbers
- Swedish National identification numbers
- Swedish Corporate Identity Numbers (OrgNr)
- Greek Social Security Numbers (ΑΜΚΑ)
- Credit card numbers
- IMEI numbers

The algorithm is in the public domain and is in wide use today. It was designed to protect against accidental errors. Most credit cards and many government identification numbers use the algorithm to distinguish valid numbers from mistyped or otherwise incorrect numbers.

## ✨ Features

- Simple API to validate numbers based on the Luhn algorithm
- Extended validation to cover number length and prefix(es)
- Can validate numbers containing hyphens or spaces
- Full type annotations and 100% test coverage
- Zero runtime dependencies

## 📦 Installation

To install using `uv`, run:

```shell
uv add luhncheck
```

To install using `pip`, run:

```shell
pip install luhncheck
```

## 🚀 Basic Usage

```python
from luhncheck import is_luhn

# Simple checksum validation
print(is_luhn("1101798278"))  # True

# Additional check for length (9 digits)
print(is_luhn("1101798278", 9))  # False

# Additional checks for prefix (either 1 or 2)
print(is_luhn("1101798278", 10, ["1", "2"]))  # True

# Validate numbers containing hyphens
print(is_luhn("01-055102-109831-4", None, "01"))  # True
```

## 📚 API Reference

### <kbd>function</kbd> `is_luhn`

```python
is_luhn(
    number: str,
    length: int | None = None,
    prefix: str | list[str] | None = None
) -> bool
```

Validate checksum and format of an identification number based on the Luhn algorithm.

**Args:**

- **`number`**: Identification number to validate.
- **`length`**: How many digits the number must contain. (The default is `None`, which implies skipping the length check).
- **`prefix`**: Exact digit(s) the number must start with. When a list of digits is provided, one of the values must match. (The default is `None`, which implies skipping the prefix check).

**Returns:**

- `True` when the number is valid; otherwise, `False`.

## 🤝 Contributing

If you're interested in contributing, please check out the [Contributing](https://github.com/dralshehri/luhncheck/blob/main/CONTRIBUTING.md) guide for more information on how you can help!

## 📄 License

This project is licensed under the terms of the MIT license.