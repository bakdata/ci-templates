# Description helm-package composite action

This composite action packages a Helm chart. Afterwards, it creates an index file for the chart repository. If `index.yaml` exists, it is merged in the new index.

## Usage

```yaml
steps:
  # ...

  - name: Helm package
    uses: bakdata/ci-templates/actions/helm-package@main
    with:
      helm-version: "v3.10.1" # (Optional)
      charts-dir: "helm-chart" # (Optional) if not set the repository root will be used


  # Rest of the workflow steps
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT        | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                              |
| ------------ | ------ | -------- | ----------- | ---------------------------------------- |
| charts-dir   | string | false    | `"."`       | The directory containing the Helm chart. |
| helm-version | string | false    | `"v3.10.1"` | The Helm version.                        |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
