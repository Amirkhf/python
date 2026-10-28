import sys


# recupere les arguments du main
# et verifie si ce sont des nombres pairs ou impairs
def main():
    argc = len(sys.argv)
    if argc == 1:
        return
    elif argc > 2:
        print("AssertionError: more than one argument is provided")
        return
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    if value % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")


# si on a execute ce fichier alors on execute le main
# sinon ca nous donne juste acces aux fonctions du fichier
if __name__ == "__main__":
    main()