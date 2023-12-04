# Refenrences helm-release reusable Workflow

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE    | REQUIRED | DEFAULT                                           | DESCRIPTION                                                                                                                |
| ---------------- | ------- | -------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| artifact-dir     | string  | false    | `"artifact"`                                      | Directory inside `charts-dir` for preparation of the GitHub pages artifact.                                                |
| charts-dir       | string  | false    | `"."`                                             | The directory containing the Helm chart and `.bumpversion.cfg` file.                                                       |
| helm-version     | string  | false    | `"v3.10.1"`                                       | The Helm version.                                                                                                          |
| lint-config-path | string  | false    | `".github/lint-config.yaml"`                      | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| page-url         | string  | true     |                                                   | URL to the GitHub pages website of the repository.                                                                         |
| ref              | string  | false    | `"${{ github.event.repository.default_branch }}"` | The ref name to checkout the repository.                                                                                   |
| release-type     | string  | true     |                                                   | Scope of the release (major, minor or patch).                                                                              |
| skip-download    | boolean | false    | `false`                                           | Skip downloading index.yaml and previous Chart versions from GitHub pages. (To be used during setup of this workflow)      |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

## Secrets

TART - Do not remove or modify this section -->

| INPUT            | TYPE    | REQUIRED | DEFAULT                                           | DESCRIPTION                                                                                                                |
| ---------------- | ------- | -------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| artifact-dir     | string  | false    | `"artifact"`                                      | Directory inside `charts-dir` for preparation of the GitHub pages artifact.                                                |
| charts-dir       | string  | false    | `"."`                                             | The directory containing the Helm chart and `.bumpversion.cfg` file.                                                       |
| helm-version     | string  | false    | `"v3.10.1"`                                       | The Helm version.                                                                                                          |
| lint-config-path | string  | false    | `".github/lint-config.yaml"`                      | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| page-url         | string  | true     |                                                   | URL to the GitHub pages website of the repository.                                                                         |
| ref              | string  | false    | `"${{ github.event.repository.default_branch }}"` | The ref name to checkout the repository.                                                                                   |
| release-type     | string  | true     |                                                   | Scope of the release (major, minor or patch).                                                                              |
| skip-download    | boolean | false    | `false`                                           | Skip downloading index.yaml and previous Chart versions from GitHub pages. (To be used during setup of this workflow)      |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                                | DESCRIPTION                                      |
| --------------- | ---------------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.helm-release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.helm-release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
