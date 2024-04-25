from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union
from m_models.commons import Metadata

class MatchLabels(BaseModel):
    labels: Dict[str, str] = Field(default_factory=dict)

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

class LabelSelectorRequirement(BaseModel):
    key: str
    operator: str
    values: Optional[List[str]]

class LabelSelector(BaseModel):
    matchLabels: Optional[Dict[str, str]]
    matchExpressions: Optional[List[LabelSelectorRequirement]] = None

class AffinityTerm(BaseModel):
    labelSelector: LabelSelector
    topologyKey: str

class PodAffinity(BaseModel):
    preferredDuringSchedulingIgnoredDuringExecution: Optional[List[Dict[str, Union[AffinityTerm, int]]]] = None


class Affinity(BaseModel):
    podAntiAffinity: Optional[PodAffinity] = None

class ProbeHTTPGet(BaseModel):
    path: str
    port: Union[int, str]
    scheme: str

class Probe(BaseModel):
    failureThreshold: int
    httpGet: ProbeHTTPGet
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    timeoutSeconds: int

class Port(BaseModel):
    containerPort: int
    name: str
    protocol: str = 'TCP'

class VolumeMount(BaseModel):
    mountPath: str
    name: str
    readOnly: Optional[bool] = True

class VolumeConfigMapItem(BaseModel):
    key: str
    path: str

class VolumeConfigMap(BaseModel):
    name: str
    defaultMode: Optional[int] = '0600'
    items: Optional[List[VolumeConfigMapItem]] = None

class Volume(BaseModel):
    name: str
    configMap: VolumeConfigMap = None

class Toleration(BaseModel):
    key: Optional[str] = None
    operator: Optional[str] = None
    effect: Optional[str] = None

class Container(BaseModel):
    name: str
    image: str
    args: Optional[List[str]] = None
    imagePullPolicy: Optional[str] = 'Always'
    ports: Optional[List[Port]] = None
    livenessProbe: Optional[Probe] = None
    readinessProbe: Optional[Probe] = None
    resources: Optional[dict] = None
    securityContext: Optional[dict] = None
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None
    volumeMounts: Optional[List[VolumeMount]] = None

class TemplateSpec(BaseModel):
    containers: List[Container]
    affinity: Optional[Affinity] = None
    dnsPolicy: Optional[str] = None
    nodeSelector: Optional[Dict[str, str]] = None
    priorityClassName: Optional[str] = None
    restartPolicy: Optional[str] = None
    schedulerName: Optional[str] = None
    securityContext: Optional[dict] = None
    serviceAccount: Optional[str] = None
    serviceAccountName: Optional[str] = None
    terminationGracePeriodSeconds: Optional[int] = None
    tolerations: Optional[List[Toleration]] = None
    volumes: Optional[List[Volume]] = None

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