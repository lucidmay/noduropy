from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from noduro.entity.utils import Thing
import json

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

