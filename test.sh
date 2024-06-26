#!/bin/bash

# kubectl create deployment nginx --image=nginx --dry-run=client -o json > nginx-deployment.json
curl -X POST -H "Content-Type: application/json" --insecure -d @admission_request_real.json https://127.0.0.1:443/validate?timeout=5s | jq .
