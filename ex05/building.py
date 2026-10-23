import sys
import string


def main():
    lower = upper = spaces = digits = punctuation = 0
    argc = len(sys.argv)
    phrase = ""

    if argc == 1:
        phrase = input("Entrez une phrase à analyser : ")
        if phrase == "" or phrase == '\n':
            return
    elif argc > 2:
        print("AssertionError: more than one argument is provided")
        return

    if argc == 2:
        phrase = sys.argv[1]
    for i in phrase:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        elif i in string.punctuation:
            punctuation += 1

    result = (
        f"What is the text to count?\n"
        f"{phrase}\n"
        f"The text contains {len(phrase)} characters:\n"
        f"{upper} upper letters\n"
        f"{lower} lower letters\n"
        f"{punctuation} punctuation marks\n"
        f"{spaces} spaces\n"
        f"{digits} digits"
    )
    print(result)


if __name__ == "__main__":
    main()
