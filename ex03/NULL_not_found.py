def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: " + str(object) + " " + str(type(object)))
    elif isinstance(object, float) and object != object:
        print("Cheese: " + str(object) + " " + str(type(object)))
    elif isinstance(object, bool) and object is False:
        print("Fake: " + str(object) + " " + str(type(object)))
    elif isinstance(object, int) and object == 0:
        print("Zero: " + str(object) + " " + str(type(object)))
    elif isinstance(object, str) and object == "":
        print("Empty: " + str(type(object)))
    else:
        print("Type not Found")
        return 1
    return 0