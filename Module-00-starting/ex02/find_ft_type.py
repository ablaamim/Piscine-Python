def all_thing_is_obj(obj: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    object_type = type(obj)
    type_name = type_names.get(object_type, "Type not found")

    if object_type == str:
        print(f"{obj} is in the kitchen : {object_type}")
    else:
        print(f"{type_name} : {object_type}")

    return 42
