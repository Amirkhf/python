import sys
from ft_filter import ft_filter


def main():
    """Print the words longer than N characters."""
    try:
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        n = int(sys.argv[2])
        # ca prend la chaine de char et ca remplit notre liste mot par mot
        words = [word for word in sys.argv[1].split()]
        resultat = ft_filter(lambda word: len(word) > n, words)
        print(resultat)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
