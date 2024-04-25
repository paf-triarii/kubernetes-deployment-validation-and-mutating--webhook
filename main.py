import yaml, os
from fastapi import Body, FastAPI
from pydantic import ValidationError
from m_utils.pretty_print import pretty_print
from m_models.admission_request import AdmissionReview
from m_validations.pods import validate_pod
from m_validations.deployments import validate_deployment
from m_validations.statefulsets import validate_statefulset

app = FastAPI()


def read_config():
    with open("/app/uvicorn_config/config.yaml", 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)

@app.get("/")
def read_root():
    return [{"validate_endpoint": "/validate"}, {"mutate_endpoint": "/mutate"}]

@app.post("/validate")
async def validate(admission_review: AdmissionReview = Body(...)):
    config = read_config()
    pretty_print(config)
    success = {"apiVersion": "admission.k8s.io/v1", "kind": "AdmissionReview", "response": {"uid": admission_review.request.uid, "allowed": True}}

    try:
        pretty_print(admission_review.model_dump_json(exclude_none=True, by_alias=True))
        # Example validation logic
        validation_functions = {
            'pod': validate_pod,
            'deployment': validate_deployment,
            'statefulset': validate_statefulset,
        }

        kind = admission_review.request.object.kind
        if kind in validation_functions:
            result = validation_functions[kind](admission_review.request.object, config)
            if not result['result']:
                return {"apiVersion": "admission.k8s.io/v1", "kind": "AdmissionReview", "response": {"uid": admission_review.request.uid, "allowed": False, "status": {"message": result['message']}}}
            else:
                return success
        else:
            return success

    except ValidationError as e:
        return {"apiVersion": "admission.k8s.io/v1", "kind": "AdmissionReview", "response": {"uid": "uid", "allowed": False, "status": {"message": str(e)}}}