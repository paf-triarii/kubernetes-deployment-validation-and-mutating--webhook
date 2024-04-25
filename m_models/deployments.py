from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from m_models.commons import Metadata

class MatchLabels(BaseModel):
    app: str

class Selector(BaseModel):
    matchLabels: MatchLabels

class RollingUpdate(BaseModel):
    maxSurge: Optional[str] = None
    maxUnavailable: Optional[str] = None

class Strategy(BaseModel):
    rollingUpdate: Optional[RollingUpdate] = None
    type: Optional[str] = None

class Container(BaseModel):
    image: str
    name: str
    imagePullPolicy: Optional[str] = None
    resources: Optional[dict] = None
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None

class TemplateSpec(BaseModel):
    containers: List[Container]
    dnsPolicy: Optional[str] = None
    restartPolicy: Optional[str] = None
    schedulerName: Optional[str] = None
    securityContext: Optional[dict] = None
    terminationGracePeriodSeconds: Optional[int] = None

class TemplateMetadata(BaseModel):
    creationTimestamp: Optional[str]
    labels: Dict[str, str] = Field(default_factory=dict)

class Template(BaseModel):
    metadata: TemplateMetadata
    spec: TemplateSpec

class Spec(BaseModel):
    selector: Selector
    template: Template
    replicas: int
    progressDeadlineSeconds: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    strategy: Optional[Strategy] = None

##############
# Main Model #
##############

class Deployment(BaseModel):
    apiVersion: str = Field(..., alias="apiVersion")
    kind: str
    metadata: Metadata
    spec: Spec