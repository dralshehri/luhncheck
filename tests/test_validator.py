import pytest

from luhn_validator import validate


@pytest.mark.parametrize(
    "actual, expected",
    [
        (1101798278, True),
        (1102544794, False),
        (4146274478407735, True),
        (4458274470454207, False),
    ],
)
def test_number_validation(actual, expected):
    assert validate(actual) == expected


@pytest.mark.parametrize(
    "actual, expected",
    [
        ({"number": 1101798278, "length": 10}, True),
        ({"number": 1101798278, "length": 9}, False),
        ({"number": 1101798278, "prefix": 1}, True),
        ({"number": 1101798278, "prefix": [1]}, True),
        ({"number": 1101798278, "prefix": 2}, False),
        ({"number": 1101798278, "prefix": [2]}, False),
        ({"number": 1101798278, "prefix": [1, 2]}, True),
        ({"number": 1101798278, "prefix": [3, 4]}, False),
        ({"number": 1101798278, "length": 10, "prefix": 1}, True),
        ({"number": 1101798278, "length": 10, "prefix": [1]}, True),
        ({"number": 1101798278, "length": 10, "prefix": 2}, False),
        ({"number": 1101798278, "length": 10, "prefix": [2]}, False),
        ({"number": 1101798278, "length": 9, "prefix": 1}, False),
        ({"number": 1101798278, "length": 9, "prefix": 2}, False),
        ({"number": 1101798278, "length": 10, "prefix": [1, 2]}, True),
        ({"number": 1101798278, "length": 10, "prefix": [3, 4]}, False),
        ({"number": 1101798278, "length": 9, "prefix": [1, 2]}, False),
        ({"number": 1101798278, "length": 9, "prefix": [3, 4]}, False),
        ({"number": 4458274470454207, "length": 16}, False),
        ({"number": 4458274470454207, "length": 15}, False),
        ({"number": 4458274470454207, "prefix": 44}, False),
        ({"number": 4458274470454207, "prefix": 41}, False),
        ({"number": 4458274470454207, "prefix": [44, 41]}, False),
        ({"number": 4458274470454207, "prefix": [5, 6]}, False),
        ({"number": 4458274470454207, "length": 16, "prefix": 44}, False),
        ({"number": 4458274470454207, "length": 16, "prefix": 41}, False),
        ({"number": 4458274470454207, "length": 15, "prefix": 44}, False),
        ({"number": 4458274470454207, "length": 15, "prefix": 41}, False),
        ({"number": 4458274470454207, "length": 16, "prefix": [44, 41]}, False),
        ({"number": 4458274470454207, "length": 16, "prefix": [5, 6]}, False),
        ({"number": 4458274470454207, "length": 15, "prefix": [44, 41]}, False),
        ({"number": 4458274470454207, "length": 15, "prefix": [5, 6]}, False),
    ],
)
def test_number_validation_with_keyword_args(actual, expected):
    assert validate(**actual) == expected


@pytest.mark.parametrize(
    "actual, expected",
    [
        ((1101798278, 10), True),
        ((1101798278, 9), False),
        ((1101798278, None, 1), True),
        ((1101798278, None, 2), False),
        ((1101798278, None, [1, 2]), True),
        ((1101798278, None, [3, 4]), False),
        ((1101798278, 10, 1), True),
        ((1101798278, 10, 2), False),
        ((1101798278, 9, 1), False),
        ((1101798278, 9, 2), False),
        ((1101798278, 10, [1, 2]), True),
        ((1101798278, 10, [3, 4]), False),
        ((1101798278, 9, [1, 2]), False),
        ((1101798278, 9, [3, 4]), False),
        ((4458274470454207, 16), False),
        ((4458274470454207, 15), False),
        ((4458274470454207, None, 44), False),
        ((4458274470454207, None, 41), False),
        ((4458274470454207, None, [44, 41]), False),
        ((4458274470454207, None, [5, 6]), False),
        ((4458274470454207, 16, 44), False),
        ((4458274470454207, 16, 41), False),
        ((4458274470454207, 15, 44), False),
        ((4458274470454207, 15, 41), False),
        ((4458274470454207, 16, [44, 41]), False),
        ((4458274470454207, 16, [5, 6]), False),
        ((4458274470454207, 15, [44, 41]), False),
        ((4458274470454207, 15, [5, 6]), False),
    ],
)
def test_number_validation_with_positional_args(actual, expected):
    assert validate(*actual) == expected
