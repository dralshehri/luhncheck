def validate(id_number: int) -> bool:
    """Validate the format and checksum of an SA identity number."""

    digits = [int(d) for d in str(id_number)]

    if len(digits) != 10 or digits[0] not in [1, 2]:
        return False

    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    checksum = (odd_sum + even_sum) % 10

    return bool(checksum == 0)
