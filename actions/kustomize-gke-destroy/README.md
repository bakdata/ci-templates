# Kustomize-gke-deploy

This action will destroy a `kustomization.yaml` file on a Google Kubernetes Engine cluster.

## Input Parameters

| Name            | Required | Default Value |  Type  | Description                                                                                       |
| --------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------- |
| kustomization-path    |    ✅    |       -       | string | Path to the root directory of the kustomization                                                           |

## Usage

```yaml
steps:
  - name: Destroy Kustomize
    uses: bakdata/ci-templates/actions/kustomize-gke-destroy@main
    with:
      kustomization-path: "my-kustomization-path" #directory containing my kustomization file
```
