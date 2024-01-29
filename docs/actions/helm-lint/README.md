# Description helm-lint composite action

This action will lint Helm charts inside the `charts` folder of your repository.

## Prerequisites

You need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:

```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

## Usage

```yaml
steps:
  - name: Lint helm charts
    uses: bakdata/ci-templates/actions/helm-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-config.yaml" # (Optional)
      helm-version: "v3.10.1" # (Optional)
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [azure/setup-helm@v3](https://github.com/azure/setup-helm/tree/v3)
- [helm/chart-testing-action@v2.0.1](https://github.com/helm/chart-testing-action/tree/v2.0.1)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                                                                               |
| ---------------- | ------ | -------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| helm-version     | string | false    | `"v3.10.1"`                  | The Helm version.                                                                                                                         |
| lint-config-path | string | false    | `".github/lint-config.yaml"` | The path to the lint configuration file (For an example see https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| ref              | string | false    | `"${{ github.ref_name }}"`   | The ref name to checkout the repository.                                                                                                  |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
