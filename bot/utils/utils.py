def convert_to_number(data: str) -> int | float | bool:
    """The convert_to_number function converts the input to a number.

    Args:
        data (str): the string input
    Returns:
        int or floar, bool if `data` does not represents a number
    """
    try:
        return int(data)
    except ValueError:
        pass

    try:
        return float(data)
    except ValueError:
        pass

    return False
