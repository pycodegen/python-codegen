from typing import List, Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args, remove_temp_options
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.ListFound import ListFound


def list_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    child_options = remove_temp_options(options)
    typ_origin = get_typ_origin(typ)
    if typ_origin is not list and typ_origin is not List:
        return
    typ_args = get_typ_args(typ)
    processed_typ = type_extractor.rawtype_to_node(typ_args[0], child_options)
    return ListFound(typ=processed_typ)
