

def check_len_family(family: list) -> bool:
    """verifie que chaque ligne est une liste et qu'elles
    ont toutes la meme taille"""
    if len(family) == 0:
        return False
    for ligne in family:
        if not isinstance(ligne, list):
            return False
    first_size = len(family[0])
    for ligne in family:
        if first_size != len(ligne):
            return False
    return True


def check_type_and_size(family: list, start: int, end: int) -> bool:
    if not isinstance(start, int):
        return False
    if not isinstance(end, int):
        return False
    if not isinstance(family, list):
        return False
    size_family = len(family)
    if start >= size_family or end > size_family or size_family == 0:
        return False
    return True


def check_data(family: list, start: int, end: int) -> bool:
    """cette fonction verifie les donnees que le main
    nous envoie : start et end doivent etre des int,
    family une liste de listes de meme taille,
    et chaque valeur un int ou un float"""
    if not check_type_and_size(family, start, end):
        return False
    if not check_len_family(family):
        return False
    for ligne in family:
        for valeur in ligne:
            if not isinstance(valeur, (int, float)):
                return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    if not check_data(family, start, end):
        return []
    largeur = len(family[0])
    print(f"My shape is : ({len(family)}, {largeur})")
    new_family = family[start:end]
    print(f"My new shape is : ({len(new_family)}, {largeur})")
    return new_family


def main():
    famille = [[1.87, 80],
               [1.65, 90],
               [1.90, 32],
               [1.76, 85]]
    print(slice_me(famille, 1, 3))


if __name__ == "__main__":
    main()
