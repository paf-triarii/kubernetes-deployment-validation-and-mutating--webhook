from typing import List, Optional, Union
from m_models.commons import  BaseModelConfig

class ResourcesDetails(BaseModelConfig):
  cpu: Optional[str] = '250m'
  memory: Optional[str] = '200Mi'

class Resources(BaseModelConfig):
    limits: Optional[ResourcesDetails] = ResourcesDetails()
    requests: Optional[ResourcesDetails] = ResourcesDetails()

class SecurityContextContainer(BaseModelConfig):
    runAsUser: Optional[int] = 1000
    runAsGroup: Optional[int] = 1000
    allowPrivilegeEscalation: Optional[bool] = False

class Port(BaseModelConfig):
    containerPort: int
    name: str
    protocol: str = 'TCP'

class VolumeMount(BaseModelConfig):
    mountPath: str
    name: str
    readOnly: Optional[bool] = True

class ProbeHTTPGet(BaseModelConfig):
    path: str
    port: Union[int, str]
    scheme: str

class Probe(BaseModelConfig):
    failureThreshold: int
    httpGet: ProbeHTTPGet
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    timeoutSeconds: int

class Container(BaseModelConfig):
    name: str
    image: str
    args: Optional[List[str]] = None
    imagePullPolicy: Optional[str] = 'Always'
    ports: Optional[List[Port]] = None
    livenessProbe: Optional[Probe] = None
    readinessProbe: Optional[Probe] = None
    resources: Optional[Resources] = None
    securityContext: Optional[SecurityContextContainer] = SecurityContextContainer()
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None
    volumeMounts: Optional[List[VolumeMount]] = None