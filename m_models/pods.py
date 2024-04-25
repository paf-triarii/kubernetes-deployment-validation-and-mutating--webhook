from m_models.commons import BaseModelConfig, Metadata, KubernetesObject
from m_models.containers import Container
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

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

class SecurityContextPod(BaseModelConfig):
    runAsUser: Optional[int] = 1000
    runAsGroup: Optional[int] = 1000
    fsGroup: Optional[int] = 2000

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

class Pod(KubernetesObject):
    spec: TemplateSpec