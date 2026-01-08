"""Simple validator for identification numbers based on the Luhn algorithm.

https://github.com/dralshehri/luhncheck
"""

__all__ = ["is_luhn"]


def is_luhn(
    number: str,
    length: int | None = None,
    prefix: str | list[str] | None = None,
) -> bool:
    """Validate checksum and format of an identification number.

    Uses the Luhn algorithm to validate identification numbers.

    Args:
        number: Identification number to validate.
        length: How many digits the number must contain. (The default is
            ``None``, which implies skipping the length check).
        prefix: Exact digit(s) the number must start with. When a list of digits
            is provided, one of the values must match. (The default is ``None``,
            which implies skipping the prefix check).

    Returns:
        ``True`` when the number is valid, otherwise ``False``.
    """
    # Strip hyphens and spaces
    number = number.replace("-", "").replace(" ", "")

    # Check if digits
    if not number.isdigit():
        return False

    # Check length
    if length is not None and len(number) != length:
        return False

    # Check prefix
    if prefix is not None:
        prefix = [prefix] if isinstance(prefix, str) else prefix
        if not number.startswith(tuple(map(str, prefix))):
            return False

    # Validate checksum
    digits = [*map(int, number)]
    digits[-2::-2] = [sum(divmod(2 * d, 10)) for d in digits[-2::-2]]
    return sum(digits) % 10 == 0
