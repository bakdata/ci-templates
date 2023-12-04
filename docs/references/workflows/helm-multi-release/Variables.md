# Refenrences helm-multi-release reusable Workflow

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                                                                |
| ---------------- | ------ | -------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| artifact-dir     | string | false    | `"artifacts"`                | Directory next to `charts-path` for preparation of the GitHub pages artifact.                                              |
| charts-path      | string | true     |                              | The directory containing the Helm chart(s).                                                                                |
| gh-pages-branch  | string | false    | `"gh-pages"`                 | Name of branch containing the artifacts                                                                                    |
| helm-version     | string | false    | `"v3.10.1"`                  | The Helm version.                                                                                                          |
| lint-config-path | string | false    | `".github/lint-config.yaml"` | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| subdirs          | string | true     |                              | List of subdir to consider                                                                                                 |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
