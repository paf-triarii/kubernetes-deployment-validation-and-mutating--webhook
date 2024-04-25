from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union
from m_models.commons import Metadata, BaseModelConfig

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

class Container(BaseModelConfig):
    image: str
    name: str
    imagePullPolicy: Optional[str] = None
    resources: Optional[dict] = None
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None

class LabelSelectorRequirement(BaseModelConfig):
    key: str
    operator: str
    values: Optional[List[str]]

class LabelSelector(BaseModelConfig):
    matchLabels: Optional[Dict[str, str]]
    matchExpressions: Optional[List[LabelSelectorRequirement]] = None

class AffinityTerm(BaseModelConfig):
    labelSelector: LabelSelector
    topologyKey: str

class PodAffinity(BaseModelConfig):
    preferredDuringSchedulingIgnoredDuringExecution: Optional[List[Dict[str, Union[AffinityTerm, int]]]] = None


class Affinity(BaseModelConfig):
    podAntiAffinity: Optional[PodAffinity] = None

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

class Port(BaseModelConfig):
    containerPort: int
    name: str
    protocol: str = 'TCP'

class VolumeMount(BaseModelConfig):
    mountPath: str
    name: str
    readOnly: Optional[bool] = True

class VolumeConfigMapItem(BaseModelConfig):
    key: str
    path: str

class VolumeConfigMap(BaseModelConfig):
    name: str
    defaultMode: Optional[int] = '0600'
    items: Optional[List[VolumeConfigMapItem]] = None

class Volume(BaseModelConfig):
    name: str
    configMap: VolumeConfigMap = None

class Toleration(BaseModelConfig):
    key: Optional[str] = None
    operator: Optional[str] = None
    effect: Optional[str] = None

class ResourcesDetails(BaseModelConfig):
  cpu: Optional[str] = '250m'
  memory: Optional[str] = '200Mi'

class Resources(BaseModelConfig):
    limits: Optional[ResourcesDetails] = ResourcesDetails()
    requests: Optional[ResourcesDetails] = ResourcesDetails()

class SecurityContextPod(BaseModelConfig):
    runAsUser: Optional[int] = 1000
    runAsGroup: Optional[int] = 1000
    fsGroup: Optional[int] = 2000

class SecurityContextContainer(BaseModelConfig):
    runAsUser: Optional[int] = 1000
    runAsGroup: Optional[int] = 1000
    allowPrivilegeEscalation: Optional[bool] = False

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

class TemplateSpec(BaseModelConfig):
    containers: List[Container]
    affinity: Optional[Affinity] = None
    dnsPolicy: Optional[str] = None
    nodeSelector: Optional[Dict[str, str]] = None
    priorityClassName: Optional[str] = None
    restartPolicy: Optional[str] = None
    schedulerName: Optional[str] = None
    securityContext: Optional[SecurityContextPod] = SecurityContextPod()
    serviceAccount: Optional[str] = None
    serviceAccountName: Optional[str] = None
    terminationGracePeriodSeconds: Optional[int] = None
    tolerations: Optional[List[Toleration]] = None
    volumes: Optional[List[Volume]] = None

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