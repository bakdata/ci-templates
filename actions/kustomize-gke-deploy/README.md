# Kustomize-gke-deploy

This action will deploy resources with Kustomize on a Google Kubernetes Engine cluster.

## Prerequisites

Create a `kustomization.yaml` file for your deployment.

## Input Parameters

| Name               | Required | Default Value |  Type  | Description                                        |
| ------------------ | :------: | :-----------: | :----: | -------------------------------------------------- |
| kustomization-path |    ✅    |       -       | string | Path to the root directory of the kustomization    |
| timeout            |    ❌    |      60       | string | Time out(in seconds) for CustomResourceDefinitions |

## Usage

```yaml
steps:
  - name: Deploy crds and app
        uses: bakdata/ci-templates/actions/kustomize-gke-deploy@main
        with:
          kustomization-path: "my-kustomization-path" #directory containing my kustomization file
          timeout: "60" #optional
```
