from dataclasses import dataclass, field
from typing import Set

from .BaseNodeType import BaseNodeType, NodeType
from .BaseOption import BaseOption


@dataclass
class TypeOR(BaseNodeType):  # type: ignore
    nodes: Set[NodeType]

    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(TypeOR) \
               + hash(frozenset(self.nodes)) \
               + 0
