from pydantic import Field
from typing import Dict, List, Optional, Union
from m_models.commons import Metadata, BaseModelConfig, KubernetesObject
from m_models.pods import TemplateSpec

class Selector(BaseModelConfig):
    matchLabels: Dict[str, str] = Field(default_factory=dict)

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
    replicas: Optional[int] = 1
    progressDeadlineSeconds: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    strategy: Optional[Strategy] = None

##############
# Main Model #
##############

class Deployment(KubernetesObject):
    spec: Spec