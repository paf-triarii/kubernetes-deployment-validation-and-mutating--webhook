from pydantic import Field
from typing import Optional, Union, List, Dict
from m_models.pods import Pod
from m_models.commons import Metadata, BaseModelConfig
from m_models.deployments import Deployment

class UserInfo(BaseModelConfig):
    username: str
    uid: str
    groups: List[str]
    extra: Optional[Dict[str, List[str]]]

class StatefulSetSpec(BaseModelConfig):
    # Placeholder for the statefulset spec properties
    serviceName: str
    replicas: int

class StatefulSet(BaseModelConfig):
    apiVersion: str = Field(..., alias="apiVersion")
    kind: str
    metadata: Metadata
    spec: StatefulSetSpec

class Request(BaseModelConfig):
    uid: str
    kind: Dict[str, str]
    resource: Dict[str, str]
    namespace: str
    operation: str
    userInfo: UserInfo
    object: Union[Pod, Deployment, StatefulSet]
    oldObject: Optional[Union[Pod, Deployment, StatefulSet]]
    dryRun: bool

class AdmissionReview(BaseModelConfig):
    apiVersion: str = Field(..., alias="apiVersion")
    kind: str
    request: Request
