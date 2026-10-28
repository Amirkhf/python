def parsing(height: list[int | float],
             weight: list[int | float]) -> bool:
    """Envoie les bonnes valeurs."""
    if not isinstance(height, list):
        print("1 : envoie les bonnes valeurs")
        return False
    elif not isinstance(weight, list):
        print("2 : envoie les bonnes valeurs")
        return False
    elif len(height) != len(weight):
        return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Vérifie le type des données que l'on reçoit,
    puis ensuite vérifie leur taille,
    et enfin remplit la liste.
    Note pour moi : trouver un moyen d'enlever le i là.
    """
    imc = []
    if not parsing(height, weight):
        return
    for tailles, poids in zip(height, weight):
        imc.append(poids / tailles)
    return imc


def main():
    print(give_bmi([10, 20, 30], [19, 89, 98]))


if __name__ == "__main__":
    main()
