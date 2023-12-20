# Description kustomize-destroy composite action

This action will destroy a `kustomization.yaml` file on a Kubernetes cluster.

## Usage

```yaml
steps:
  - name: Destroy Kustomize app
    uses: bakdata/ci-templates/actions/kustomize-destroy@main
    with:
      kustomization-path: "my-kustomization-path" #directory containing my kustomization file
```
