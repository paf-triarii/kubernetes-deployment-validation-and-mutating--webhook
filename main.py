import json
from fastapi import Body, FastAPI
from pydantic import ValidationError
from m_utils.pretty_print import pretty_print
from m_models.deployments import Deployment

app = FastAPI()

def process_request(allowed: bool, uid: str, message: str):
    allowed_str = "allowed" if allowed else "denied"
    return {"response": {"allowed": allowed_str, "uid": uid, "status": {"message": message}}}

@app.get("/")
def read_root():
    return [{"validate_endpoint": "/validate"}, {"mutate_endpoint": "/mutate"}]

@app.post("/validate")
async def validate(deployment: Deployment = Body(...)):
    try:
        pretty_print(type(deployment), "Request Type")
        pretty_print(deployment, "Request JSON")
        return process_request(True, "uid", deployment.metadata.name)
    except ValidationError as e:
        return process_request(False, "uid", str(e))