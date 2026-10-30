def parsing_for_give_bmi(height: list[int | float],
                         weight: list[int | float]) -> bool:
    """Vérifie les types et tailles des listes."""
    if not isinstance(height, list):
        print("Erreur : height n'est pas une liste")
        return False
    elif not isinstance(weight, list):
        print("Erreur : weight n'est pas une liste")
        return False
    elif len(height) != len(weight):
        print("Erreur : tailles différentes")
        return False
    for tailles, poids in zip(height, weight):
        if not isinstance(tailles, (float, int)):
            print(f"Erreur : {tailles!r} invalide")
            return False
        elif tailles <= 0:
            print("Erreur : height doit être > 0")
            return False
        elif not isinstance(poids, (float, int)):
            print(f"Erreur : {poids!r} invalide")
            return False
        elif poids <= 0:
            print("Erreur : weight doit être > 0")
            return False
    return True


def parsing_for_apply_limit(bmi: list[int | float], limit: int) -> bool:
    """Vérifie les types de bmi et limit."""
    if not isinstance(bmi, list):
        print("Erreur : bmi n'est pas une liste")
        return False
    if not isinstance(limit, int):
        print("Erreur : limit doit être un int")
        return False
    for imc in bmi:
        if not isinstance(imc, (float, int)):
            print(f"Erreur : {imc!r} invalide")
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Renvoie la liste des IMC."""
    imc = []
    if not parsing_for_give_bmi(height, weight):
        return imc
    for tailles, poids in zip(height, weight):
        imc.append(poids / (tailles ** 2))
    return imc


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Renvoie True si l'IMC dépasse limit."""
    result = []
    if not parsing_for_apply_limit(bmi, limit):
        return result
    for imc in bmi:
        if imc > limit:
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    """Teste give_bmi et apply_limit."""
    height = [2.1, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
