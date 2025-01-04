from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from noduro.entity.utils import Thing
import json
from datetime import datetime

class PublishStatus(Enum):
    Active = "Active"
    Draft = "Draft"
    Pruned = "Pruned"

@dataclass
class Publish:
    id: Thing
    timestamp: str
    userid: Optional[Thing] = None
    comment: Optional[str] = None
    entries: Dict[str, str] = field(default_factory=dict)
    status: Optional['PublishStatus'] = None  # Forward declaration
    version: Optional[int] = None
    software: Optional[str] = None
    thumbnail: Optional[str] = None
    metadata: Optional[dict] = None  # Using dict to represent Value

    def to_json(self) -> dict:
        return {
            "id": {
                "tb": self.id.tb,
                "id": {"String": self.id.id.String}
            } if self.id else None,
            "timestamp": self.timestamp,
            "userid": {
                "tb": self.userid.tb,
                "id": {"String": self.userid.id.String}
            } if self.userid else None,
            "comment": self.comment,
            "entries": self.entries,
            "status": self.status.value if self.status else None,
            "version": self.version,
            "software": self.software,
            "thumbnail": self.thumbnail,
            "metadata": self.metadata
        }


    def from_json(self, json_str: str) -> 'Publish':
        return json.loads(json_str, object_hook=lambda d: Publish(**d))

    
    @classmethod
    def new(
            cls,
            userid: Optional[Thing] = None,
            comment: Optional[str] = None,
            entries: Optional[Dict[str, str]] = None,
            status: Optional[PublishStatus] = None,
            version: Optional[int] = None,
            software: Optional[str] = None,
            thumbnail: Optional[str] = None,
            metadata: Optional[dict] = None,
            ) -> 'Publish':
        return cls(
            id=Thing.from_str("temp", "temp"),
            timestamp=datetime.now().isoformat(),
            userid=userid,
            comment=comment,
            entries=entries,
            status=status,
            version=version,
            software=software,
            thumbnail=thumbnail,
            metadata=metadata
        )


