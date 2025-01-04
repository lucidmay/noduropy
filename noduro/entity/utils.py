from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
import json


@dataclass
class Id:
    String: str

@dataclass
class Thing:
    tb: str
    id: Id

    @classmethod
    def from_str(cls, tb: str, id: str):
        return cls(tb=tb, id=Id(String=id))

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)


if __name__ == "__main__":
    thing = Thing.from_str("nodes-1b64faa8-ed3a-48cd-98ab-ffbbeb9d9bde", "@root/show:triplets")
    print(thing.to_json())

