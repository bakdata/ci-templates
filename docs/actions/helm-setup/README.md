# Description helm-setup composite action

This action will set up everything necessary to deploy or destroy Helm charts.

## Usage

```yaml
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/helm-setup@main
    with:
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.10.1" # optional
```

## Dependencies

- [azure/setup-kubectl@v3](https://github.com/azure/setup-kubectl/tree/v3)
- [azure/setup-helm@v3](https://github.com/azure/setup-helm/tree/v3)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT           | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION     |
| --------------- | ------ | -------- | ----------- | --------------- |
| helm-version    | string | false    | `"v3.10.1"` | Helm version    |
| kubectl-version | string | false    | `"v1.23.0"` | Kubectl version |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
