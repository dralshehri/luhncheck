# Changelog

The versioning scheme is compliant with the [PEP 440] specification.

[PEP 440]: https://peps.python.org/pep-0440/#public-version-identifiers

## 2.1.0 (2023-12-18)

- Dropped support for Python 3.7 and added support for Python 3.12.

## 2.0.0 (2023-04-24)

- Renamed the package to `luhncheck` and deprecated the old name.
- Renamed the `validate` function to `is_luhn`.
- Dropped support for Python 3.6 and added support for Python 3.11.
- Fixed location of type-checking marker file.
- Improved performance by using a generator for `sum` function.
- Removed badges from the package description.
- Updated development configurations and GitHub actions.
- Changed GitHub username back to @dralshehri and updated related links.

## 1.1.4 (2022-02-05)

- Fixed some typos.
- Updated linting configurations.

## 1.1.3 (2022-02-02)

- Changed type hints for `number` and `prefix` arguments to prefer strings.
- Changed GitHub username to @mhalshehri and updated related links.
- Updated development workflows and configurations.

## 1.1.2 (2022-01-19)

- Improved type hints for `number` and `prefix` arguments.
- Improved handling of numbers containing hyphens or spaces.
- Updated documentation, tests, and usage examples.

## 1.1.1 (2021-10-29)

- Improved docstrings and package metadata.
- Improved usage examples.

## 1.1.0 (2021-10-20)

- Renamed the project to `luhncheck` for more generic use.
- Changed `number` parameter of `validate` function to accept integers only.
- Added `length` and `prefix` parameters to `validate` function.
- Updated documentation and tests.
- Updated packaging configuration files and local development workflow.

## 1.0.7 (2021-10-18)

- Deprecated `saudi-id-validator` in favor of the new name.

## 1.0.6 (2021-03-18)

- Fixed the package homepage URL. ([#2])
- Updated CI tests to include recent Python versions.

[#2]: https://github.com/dralshehri/luhncheck/pull/2

## 1.0.5 (2019-06-05)

- Added params to docstrings.
- Fixed a typo in README.

## 1.0.4 (2019-05-27)

- Updated README.

## 1.0.3 (2019-05-22)

- Updated usage example.
- Updated README badges.
- Removed LICENSE file extension.

## 1.0.2 (2018-12-06)

- Improved README content.

## 1.0.1 (2018-11-18)

- Fixed some typos in README file.

## 1.0.0 (2018-11-18)

- First release.
