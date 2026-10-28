def count_in_list(lst: list, value: any) -> int:
    """Return the number of occurrences of value in lst."""
    count = 0
    for word in lst:
        if word == value:
            count += 1
    return count
