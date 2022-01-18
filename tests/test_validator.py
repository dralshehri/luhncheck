import pytest

from luhn_validator import validate


@pytest.mark.parametrize(
    "actual, expected",
    [
        (1101798278, True),
        ("1101798278", True),
        (1102544794, False),
        (4146274478407735, True),
        ("4146 2744 7840 7735", True),
        (4458274470454207, False),
        ("010551021098314", True),
        ("01-055102-109831-4", True),
        ("01-055102-109831", False),
    ],
)
def test_number_validation(actual, expected):
    assert validate(actual) == expected


@pytest.mark.parametrize(
    "actual, expected",
    [
        ({"number": 1101798278, "length": 10}, True),
        ({"number": "1-1017-9827-8", "length": 10}, True),
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
        ({"number": 4146274478407735, "length": 16}, True),
        ({"number": "4146 2744 7840 7735", "length": 16}, True),
        ({"number": 4146274478407735, "length": 15}, False),
        ({"number": 4146274478407735, "prefix": 41}, True),
        ({"number": 4146274478407735, "prefix": 44}, False),
        ({"number": 4146274478407735, "prefix": [44, 41]}, True),
        ({"number": 4146274478407735, "prefix": [5, 6]}, False),
        ({"number": 4146274478407735, "length": 16, "prefix": 41}, True),
        ({"number": 4146274478407735, "length": 16, "prefix": 44}, False),
        ({"number": 4146274478407735, "length": 15, "prefix": 41}, False),
        ({"number": 4146274478407735, "length": 15, "prefix": 44}, False),
        ({"number": 4146274478407735, "length": 16, "prefix": [44, 41]}, True),
        ({"number": 4146274478407735, "length": 16, "prefix": [5, 6]}, False),
        ({"number": 4146274478407735, "length": 15, "prefix": [44, 41]}, False),
        ({"number": 4146274478407735, "length": 15, "prefix": [5, 6]}, False),
        ({"number": "33-168941-274558-0", "length": 15}, True),
        ({"number": "33-168941-274558-0", "length": 18}, False),
        ({"number": "01-055102-109831-4", "length": 15}, True),
    ],
)
def test_number_validation_with_keyword_args(actual, expected):
    assert validate(**actual) == expected


@pytest.mark.parametrize(
    "actual, expected",
    [
        ((1101798278, 10), True),
        (("1-1017-9827-8", 10), True),
        ((1101798278, 9), False),
        ((1101798278, None, 1), True),
        ((1101798278, None, [1]), True),
        ((1101798278, None, 2), False),
        ((1101798278, None, [2]), False),
        ((1101798278, None, [1, 2]), True),
        ((1101798278, None, [3, 4]), False),
        ((1101798278, 10, 1), True),
        ((1101798278, 10, [1]), True),
        ((1101798278, 10, 2), False),
        ((1101798278, 10, [2]), False),
        ((1101798278, 9, 1), False),
        ((1101798278, 9, 2), False),
        ((1101798278, 10, [1, 2]), True),
        ((1101798278, 10, [3, 4]), False),
        ((1101798278, 9, [1, 2]), False),
        ((1101798278, 9, [3, 4]), False),
        ((4146274478407735, 16), True),
        (("4146 2744 7840 7735", 16), True),
        ((4146274478407735, 15), False),
        ((4146274478407735, None, 41), True),
        ((4146274478407735, None, 44), False),
        ((4146274478407735, None, [44, 41]), True),
        ((4146274478407735, None, [5, 6]), False),
        ((4146274478407735, 16, 41), True),
        ((4146274478407735, 16, 44), False),
        ((4146274478407735, 15, 41), False),
        ((4146274478407735, 15, 44), False),
        ((4146274478407735, 16, [44, 41]), True),
        ((4146274478407735, 16, [5, 6]), False),
        ((4146274478407735, 15, [44, 41]), False),
        ((4146274478407735, 15, [5, 6]), False),
        (("33-168941-274558-0", 15), True),
        (("33-168941-274558-0", 18), False),
        (("01-055102-109831-4", 15), True),
    ],
)
def test_number_validation_with_positional_args(actual, expected):
    assert validate(*actual) == expected
