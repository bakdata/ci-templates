# Refenrences helm-lint composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                                                                               |
| ---------------- | ------ | -------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| helm-version     | string | false    | `"v3.10.1"`                  | The Helm version.                                                                                                                         |
| lint-config-path | string | false    | `".github/lint-config.yaml"` | The path to the lint configuration file (For an example see https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| ref              | string | false    | `"${{ github.ref_name }}"`   | The ref name to checkout the repository.                                                                                                  |
<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
