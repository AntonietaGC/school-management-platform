#!/usr/bin/env bash

set -euo pipefail

VERSION="${1:-dev}"
IMAGE="school-management-platform:${VERSION}"
NAMESPACE="school-dev"
DEPLOYMENT="school-platform-dev"
CONTAINER="school-platform"

echo " 1. AUTOMATED TESTS "
.venv/bin/python -m pytest tests -v

echo " 2. ANSIBLE VALIDATION "
ansible-playbook \
  -i ansible/inventory.ini \
  ansible/setup-server.yml

echo " 3. TERRAFORM VALIDATION "
terraform -chdir=terraform init -input=false
terraform -chdir=terraform validate
terraform -chdir=terraform apply -auto-approve -input=false

echo " 4. DOCKER BUILD "
docker build -t "${IMAGE}" .

echo " 5. LOAD IMAGE INTO MINIKUBE "
minikube image load "${IMAGE}"

echo " 6. KUBERNETES DEPLOYMENT "
kubectl apply -f kubernetes/dev/deployment.yaml
kubectl apply -f kubernetes/dev/service.yaml

kubectl set image \
  deployment/"${DEPLOYMENT}" \
  "${CONTAINER}"="${IMAGE}" \
  -n "${NAMESPACE}"

echo " 7. WAIT FOR ROLLOUT "
kubectl rollout status \
  deployment/"${DEPLOYMENT}" \
  -n "${NAMESPACE}" \
  --timeout=180s

echo " 8. VALIDATION "
kubectl get deployment,pods,service \
  -n "${NAMESPACE}" \
  -o wide

echo "Deployed image: ${IMAGE}"
