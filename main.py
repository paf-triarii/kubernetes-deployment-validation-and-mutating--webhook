from fastapi import FastAPI
import json
from m_utils.pretty_print import pretty_print
from m_models.deployments import Deployment

app = FastAPI()

@app.get("/")
def read_root():
    return [{"validate_endpoint": "/validate"}, {"mutate_endpoint": "/mutate"}]

@app.post("/validate")
async def validate(deployment: Deployment):
    pretty_print(type(deployment), "Request Type")
    pretty_print(deployment, "Request JSON")
    return {"validate": "success"}