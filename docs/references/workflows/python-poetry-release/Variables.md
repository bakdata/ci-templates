# Refenrences python-poetry-release reusable Workflow

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT                                           | DESCRIPTION                                                               |
| ----------------- | ------- | -------- | ------------------------------------------------- | ------------------------------------------------------------------------- |
| changelog         | boolean | false    | `true`                                            | Create changelog for release.                                             |
| changelog-config  | string  | false    |                                                   | Changelog config path.                                                    |
| changelog-file    | string  | false    | `"CHANGELOG.md"`                                  | Path to the changelog file in the GitHub repository                       |
| poetry-version    | string  | false    | `"1.5.1"`                                         | The Poetry version to be installed. (Default is 1.5.1)                    |
| python-version    | string  | false    | `"3.10"`                                          | The Python version for setting up Poetry. (Default is 3.10)               |
| ref               | string  | false    | `"${{ github.event.repository.default_branch }}"` | The ref name to checkout the repository.                                  |
| release-type      | string  | true     |                                                   | Scope of the release; See: https://python-poetry.org/docs/cli/#version    |
| working-directory | string  | false    | `"./"`                                            | The working directory of your Python package. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                                  | DESCRIPTION                        |
| --------------- | ------------------------------------------------------ | ---------------------------------- |
| old-version     | `"${{ jobs.create-release.outputs.old-version }}"`     | The old version of the package.    |
| release-version | `"${{ jobs.create-release.outputs.release-version }}"` | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
