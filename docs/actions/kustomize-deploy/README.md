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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                        |
| ------------------ | ------ | -------- | ------- | -------------------------------------------------- |
| kustomization-path | string | true     |         | Path to the root directory of the kustomization    |
| timeout            | string | false    | `"60"`  | Time out(in seconds) for CustomResourceDefinitions |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
