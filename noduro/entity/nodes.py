from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from noduro.entity.utils import Thing
from noduro.entity.expression import Name
from noduro.entity.properties import NodeProperty
import json


@dataclass
class Crate:
    # Define the fields for Crate as needed
    pass

@dataclass
class Assembly:
    # Define the fields for Assembly as needed
    pass

@dataclass
class Dev:
    # Define the fields for Dev as needed
    pass

@dataclass
class Temp:
    # Define the fields for Temp as needed
    pass

@dataclass
class Component:
    state: str
    component_type: 'ComponentType'  # Forward declaration

class NodeType(Enum):
    Crate = "Crate"
    Assembly = "Assembly"
    Component = "Component"
    Dev = "Dev"
    Temp = "Temp"

class ComponentType(Enum):
    Version = "Version"
    Gallery = "Gallery"
    Assembly = "Assembly"





@dataclass
class Node:
    id: Thing
    name: str
    segments: List[Thing] = field(default_factory=list)
    metadata: json = field(default_factory=dict)
    properties: Dict[str, NodeProperty] = field(default_factory=dict)
    dependencies: List[Thing] = field(default_factory=list)
    node_type: NodeType = field(default=NodeType.Crate)
    name_pattern: Optional[Name] = None

    def __post_init__(self):
        pass

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)
    


if __name__ == "__main__":
    node = Node(id="1", name="Root", type="Group")
    node_json = node.to_json()
    print(node_json)
    node_from_json = Node.from_json(node_json)
    print(node_from_json)

