# Description helm-destroy composite action

This action will destroy a Helm chart on a Kubernetes cluster.

## Usage

```yaml
steps:
  - name: Destroy Helm chart
    uses: bakdata/ci-templates/actions/helm-destroy@main
    with:
      release-name: "my-release"
      namespace: "my-namespace"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT        | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                 |
| ------------ | ------ | -------- | ------- | --------------------------- |
| namespace    | string | true     |         | K8s namespace to destroy in |
| release-name | string | true     |         | Helm release name           |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
