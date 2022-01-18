"""Simple validator for identification numbers based on the Luhn algorithm.

https://github.com/dralshehri/luhn-validator
"""

__version__ = "1.1.2"

from typing import List, Optional, Union


def validate(
    number: Union[str, int],
    length: Optional[int] = None,
    prefix: Optional[Union[Union[str, int], List[Union[str, int]]]] = None,
) -> bool:
    """Validate checksum and format of an identification number based on the Luhn algorithm.

    Args:
        number: Identification number to validate.
        length: How many digits the number must contain. (The default is ``None``,
            which implies skipping the length check).
        prefix: Exact digit(s) the number must start with. When a list of
            digits is provided, one of the values must match. (The default is ``None``,
            which implies skipping the prefix check).

    Returns:
        ``True`` when the number is valid, otherwise ``False``.
    """

    if isinstance(number, int):
        number = str(number)

    # Strip hyphens and spaces
    number = number.replace("-", "").replace(" ", "")

    # Check length
    if length is not None:
        if len(number) != length:
            return False

    # Check prefix
    if prefix is not None:
        if not isinstance(prefix, list):
            prefix = [prefix]
        prefix_tuple = tuple(map(str, prefix))
        if not number.startswith(prefix_tuple):
            return False

    # Validate checksum
    digits = list(map(int, number))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    checksum = (odd_sum + even_sum) % 10
    result = bool(checksum == 0)

    return result
