from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from noduro.entity.utils import Thing
import json

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
