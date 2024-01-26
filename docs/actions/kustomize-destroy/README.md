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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                     |
| ------------------ | ------ | -------- | ------- | ----------------------------------------------- |
| kustomization-path | string | true     |         | Path to the root directory of the kustomization |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
