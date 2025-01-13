def divide_by_three(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")
    return num / 3