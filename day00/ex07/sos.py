import sys
import string


def check_input(text) -> bool:
    """verifie que text ne contient que des lettres chiffres et espaces"""
    for c in text:
        if c not in string.ascii_letters + string.digits + ' ':
            return False
    return True


def convertion_mors(str_input) -> str:
    """convertit str_input en code morse lettres separees par un espace"""
    valide_input = str_input.upper()
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
    }
    result = ''

    for i, c in enumerate(valide_input):
        one = morse_dict[c]
        result += one
        if i < len(valide_input) - 1:
            result += ' '
    return result


def main():
    """verifie le nombre darguments puis le contenu enfin convertit"""
    argc = len(sys.argv)
    if argc != 2:
        print('AssertionError: the arguments are bad')
        return
    elif not check_input(sys.argv[1]):
        print('AssertionError: the arguments are bad')
        return
    result = convertion_mors(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()
