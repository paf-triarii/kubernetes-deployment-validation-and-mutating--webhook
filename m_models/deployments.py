from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union
from m_models.commons import Metadata, BaseModelConfig
from m_models.pods import TemplateSpec

class MatchLabels(BaseModelConfig):
    labels: Dict[str, str] = Field(default_factory=dict)

class Selector(BaseModelConfig):
    matchLabels: MatchLabels

class RollingUpdate(BaseModelConfig):
    maxSurge: Optional[str] = None
    maxUnavailable: Optional[str] = None

class Strategy(BaseModelConfig):
    rollingUpdate: Optional[RollingUpdate] = None
    type: Optional[str] = None

class TemplateMetadata(BaseModelConfig):
    creationTimestamp: Optional[str]
    labels: Dict[str, str] = Field(default_factory=dict)

class Template(BaseModelConfig):
    metadata: TemplateMetadata
    spec: TemplateSpec

class Spec(BaseModelConfig):
    selector: Selector
    template: Template
    replicas: int
    progressDeadlineSeconds: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    strategy: Optional[Strategy] = None

##############
# Main Model #
##############

class Deployment(BaseModelConfig):
    apiVersion: str = Field(..., alias="apiVersion")
    kind: str
    metadata: Metadata
    spec: Spec