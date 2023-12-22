# Description kustomize-deploy composite action

This action will deploy resources with Kustomize on a Kubernetes cluster.

## Prerequisites

Create a `kustomization.yaml` file for your deployment.

## Usage

```yaml
steps:
  - name: Deploy Kustomize app
    uses: bakdata/ci-templates/actions/kustomize-deploy@main
    with:
      kustomization-path: "my-kustomization-path" #directory containing my kustomization file
      timeout: "60" #optional
```
