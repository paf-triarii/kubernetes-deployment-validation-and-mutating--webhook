import json
from fastapi import Body, FastAPI
from pydantic import ValidationError
from m_utils.pretty_print import pretty_print
from m_models.admission_request import AdmissionReview

app = FastAPI()

@app.get("/")
def read_root():
    return [{"validate_endpoint": "/validate"}, {"mutate_endpoint": "/mutate"}]

@app.post("/validate")
async def validate(admission_review: AdmissionReview = Body(...)):
    try:
        # Use Pydantic's json() method to serialize the review for logging/debugging
        print(admission_review.model_dump_json(exclude_none=True, by_alias=True))
        # Example validation logic
        if admission_review.request.object.kind == 'pod':
            # Perform specific validation for Pod
            pass
        elif admission_review.request.object.kind == 'deployment':
            # Perform specific validation for Deployment
            pass
        elif admission_review.request.object.kind == 'statefulset':
            # Perform specific validation for StatefulSet
            pass
        
        return {"apiVersion": "admission.k8s.io/v1", "kind": "AdmissionReview", "response": {"uid": admission_review.request.uid, "allowed": True}}
    except ValidationError as e:
        return {"apiVersion": "admission.k8s.io/v1", "kind": "AdmissionReview", "response": {"uid": "uid", "allowed": False, "status": {"message": str(e)}}}