from typing import Optional, Any


def object_or_id(obj, obj_class):
    if isinstance(obj, obj_class):
        obj_id = obj.id
    elif isinstance(obj, str):
        obj_id = obj
    else:
        raise TypeError(" Argument must be either {obj_class} or string (id)")
    return obj_id
