import math  # for math.nan (Not a Number)


def NULL_not_found(object: any) -> int:
    type_names = {None: "Nothing", math.nan: "Cheese", '0': "Zero", '': "Empty", False: "Fake"}

    type_name = type_names.get(object, "Type not Found")
    if type_name != "Type not Found":
        print(f"{type(object)}: {object}")
    elif object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object == 0 and isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {object} {type(object)}")
    elif not object and isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
    return 1 if type_name == "Type not Found" else 0
