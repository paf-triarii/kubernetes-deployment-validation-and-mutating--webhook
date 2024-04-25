from pydantic import BaseModel, Field, field_validator
from typing import Dict, List, Optional

class BaseModelConfig(BaseModel):
    class Config:
        from_attributes = True
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

class KubernetesObject(BaseModelConfig):
    apiVersion: str = Field(..., alias='apiVersion')
    kind: str
    metadata: Metadata

    # This will be the discriminator field
    @field_validator('kind')
    def set_kind(cls, v):
        return v.lower()