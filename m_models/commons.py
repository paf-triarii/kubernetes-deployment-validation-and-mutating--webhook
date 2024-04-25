from pydantic import BaseModel, Field
from typing import Dict, List, Optional

class BaseModelConfig(BaseModel):
    class Config:
        orm_mode = True
        exclude_none = True

class Metadata(BaseModelConfig):
    name: str
    namespace: Optional[str] = None
    annotations: Optional[Dict[str, str]] = Field(default_factory=dict)
    labels: Optional[Dict[str, str]] = Field(default_factory=dict)
    creationTimestamp: Optional[str] = None
    generation: Optional[int] = None
    resourceVersion: Optional[str] = None
    uid: Optional[str] = None