from typing import Optional, Dict
from dataclasses import dataclass, field
from noduro.entity.properties import NodeProperty
from noduro.entity.utils import Thing
from enum import Enum
import json
from datetime import datetime

class VersionStatus(Enum):
    Active = "Active"
    Draft = "Draft"
    Pruned = "Pruned"
    Preserve = "Preserve"

@dataclass
class Version:
    version: int
    properties: Dict[str, NodeProperty] = field(default_factory=dict)
    comment: Optional[str] = None
    userid: Optional[Thing] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    status: Optional['VersionStatus'] = None  # Forward declaration
    software: Optional[str] = None
    thumbnail: Optional[str] = None
    metadata: Optional[dict] = None  # Using dict to represent Value
    entries: Dict[str, str] = field(default_factory=dict)  # file format and path < USD, "./assembly.usda" >

    
    def to_json(self) -> dict:
        return {
            "version": self.version,
            "properties": {k: v.to_json() for k, v in self.properties.items()} if self.properties else {},  # Change None to {}
            "comment": self.comment,
            "userid": {
                "tb": self.userid.tb,
                "id": {"String": self.userid.id.String}
            } if self.userid else None,
            "timestamp": self.timestamp,
            "status": self.status.value if self.status else None,
            "software": self.software,
            "thumbnail": self.thumbnail,
            "metadata": self.metadata,
            "entries": self.entries
        }
    
    @classmethod
    def new(cls, 
            version: int,
            userid: Optional[Thing] = None,
            comment: Optional[str] = None,
            entries: Optional[Dict[str, str]] = None,
            status: Optional[VersionStatus] = None,
            software: Optional[str] = None,
            thumbnail: Optional[str] = None,
            metadata: Optional[dict] = None,
            properties: Optional[Dict[str, NodeProperty]] = None,
            ):

            return cls(
                timestamp=datetime.now().isoformat(),
                userid=userid,
                comment=comment,
                entries=entries,
                status=status,
                version=version,
                software=software,
                thumbnail=thumbnail,
                metadata=metadata,
                properties=properties
            )

    @classmethod
    def from_json(cls, json_str: str) -> 'Version':
        data = json.loads(json_str)
        return cls(**data)



