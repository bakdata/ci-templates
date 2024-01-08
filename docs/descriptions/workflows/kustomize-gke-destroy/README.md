# Description of kustomize-gke-destroy reusable Workflow

This workflow will uninstall deployments using Kustomize.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-setup](https://github.com/bakdata/ci-templates/tree/main/actions/helm-setup)
- [kustomize-gke-destroy](https://github.com/bakdata/ci-templates/tree/main/actions/kustomize-gke-destroy)

## Calling the workflow

```yaml
name: Call this reusable workflow

on:
  workflow_dispatch:
    inputs:
      kustomization-path:
        description: "Path to the root directory of the kustomization"
        default: "kustomization-path"
        required: false
      timeout:
        description: "Time out(in seconds) for CustomResourceDefinitions"
        default: "60"
        required: false

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/kustomize-gke-destroy.yaml@main
    with:
      kustomization-path: ${{ inputs.kustomization-path }}
      gcloud-sdk-version: "376.0.0" #optional
      kubectl-version: "v1.23.0" #optional
      helm-version: "v3.8.1" #optional
    secrets:
      gke-service-account: ${{ secrets.GKE_DEV_SERVICE_ACCOUNT }}
      gke-project: ${{ secrets.GKE_DEV_PROJECT }}
      gke-region: ${{ secrets.GKE_DEV_REGION }}
      gke-cluster: ${{ secrets.GKE_DEV_CLUSTER }}
```