# object est le nom du parametre recu
# any veut dire que on peut recevoir tout et nimporte quoi
# -> int veut dire que la fonction renvoie un int
def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List : " + str(type(object)))
    elif isinstance(object, tuple):
        print("Tuple : " + str(type(object)))
    elif isinstance(object, set):
        print("Set : " + str(type(object)))
    elif isinstance(object, dict):
        print("Dict : " + str(type(object)))
    elif isinstance(object, str):
        print(object + " is in the kitchen : " + str(type(object)))
    else:
        print("Type not found")
    return 42
