def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
function(item) is true.  If function is None, return the items that
are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    """Test ft_filter with a few examples."""
    def is_even(number):
        """Return True if number is even."""
        return number % 2 == 0

    def starts_with_a(word):
        """Return True if word starts with 'A'."""
        return word.startswith("A")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_names = ["Alice", "Bob", "Anna", "Charlie"]

    even_numbers = ft_filter(is_even, numbers)
    names_starting_with_a = ft_filter(starts_with_a, first_names)

    print("Even numbers:", even_numbers)
    print("Names starting with A:", names_starting_with_a)
    print("Truthy values:", ft_filter(None, [0, 1, "", "a", None, []]))


if __name__ == "__main__":
    main()
