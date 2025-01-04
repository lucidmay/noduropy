from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from noduro.entity.utils import Thing
import json


# @dataclass
# class Id:
#     String: str

# @dataclass
# class Thing:
#     tb: str
#     id: Id

#     @classmethod
#     def from_str(cls, tb: str, id: str):
#         return cls(tb=tb, id=Id(String=id))

#     def to_json(self) -> str:
#         return json.dumps(self, default=lambda o: o.__dict__, indent=4)


@dataclass
class NodeProperty:
    value: Optional[str]  # Assuming PropertyType is a string; adjust as necessary
    editable: bool

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

class PublishStatus(Enum):
    Draft = "Draft"
    Published = "Published"
    Unpublished = "Unpublished"

@dataclass
class Publish:
    id: Thing
    node_id: Thing
    timestamp: str
    userid: Optional[Thing] = None
    comment: Optional[str] = None
    entries: Dict[str, Thing] = field(default_factory=dict)
    status: Optional['PublishStatus'] = None  # Forward declaration
    version: Optional[int] = None
    software: Optional[str] = None
    thumbnail: Optional[str] = None
    metadata: Optional[dict] = None  # Using dict to represent Value

class NodeType(Enum):
    Crate = "Crate"
    Assembly = "Assembly"
    Component = "Component"
    Dev = "Dev"
    Temp = "Temp"

class ComponentType(Enum):
    Version = "Version"
    InVersion = "InVersion"
    Gallery = "Gallery"
    Assembly = "Assembly"

@dataclass
class NodeProperty:
    value: Optional['PropertyType']  # Forward declaration
    editable: bool

class PropertyType:
    def __init__(self, value: Union[str, int, float, bool, List[str], dict]):
        if isinstance(value, str):
            self.type = 'String'
            self.value = value
        elif isinstance(value, int):
            self.type = 'Integer'
            self.value = value
        elif isinstance(value, float):
            self.type = 'Float'
            self.value = value
        elif isinstance(value, bool):
            self.type = 'Boolean'
            self.value = value
        elif isinstance(value, list) and all(isinstance(item, str) for item in value):
            self.type = 'Array'
            self.value = value
        elif isinstance(value, dict):
            self.type = 'Object'
            self.value = value
        else:
            raise ValueError("Invalid type for PropertyType")

    def to_json(self) -> str:
        """Serialize the PropertyType instance to a JSON string."""
        return json.dumps({"type": self.type, "value": self.value}, indent=4)


@dataclass
class VersionProperties:
    properties: Dict[str, 'NodeProperty']  # Forward declaration
    atop: Optional[str] = None
    versions: Dict[str, Thing] = field(default_factory=dict)
    latest: Optional[str] = None

@dataclass
class InVersionProperties:
    properties: Dict[str, 'NodeProperty']  # Forward declaration

@dataclass
class GalleryProperties:
    properties: Dict[str, 'NodeProperty']  # Forward declaration

@dataclass
class AssemblyProperties:
    properties: Dict[str, 'NodeProperty']  # Forward declaration

class InputType:
    def __init__(self, value: Union[str, None], input_type: str):
        if input_type == "User":
            self.type = "User"
            self.value = value
        elif input_type == "Derive":
            self.type = "Derive"
            self.value = value
        else:
            raise ValueError("Invalid input type")

@dataclass
class Str:
    value: Optional['InputType'] = None  # Forward declaration
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    capitalize: Optional[bool] = None

class Expression(Enum):
    Str = "Str"
    Int = "Int"
    Ext = "Ext"

@dataclass
class Name:
    id: Optional[Thing] = None
    patterns: Dict[str, 'Expression'] = field(default_factory=dict)  # Forward declaration
    order: List[str] = field(default_factory=list)
    delimiter: Optional[str] = None


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

