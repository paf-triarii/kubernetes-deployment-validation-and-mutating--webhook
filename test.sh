#!/bin/bash

kubectl create deployment nginx --image=nginx --dry-run=client -o json > nginx-deployment.json
curl -X POST -H "Content-Type: application/json" -d @nginx-deployment.json http://127.0.0.1:8000/validate | jq .
