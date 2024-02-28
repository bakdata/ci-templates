# Description of python-poetry-release reusable Workflow

This workflow will bump the version of your Python project, create a Git tag, and make a release of your project on GitHub. Moreover, this workflow allows you to add a CHANGELOG.md automatically if you wish to do so.
In the following, you will first find the necessary prerequisites to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

## Prerequisites

Your Python project needs to be set up with Poetry and contain a `pyproject.toml` file to use this workflow. Moreover,
choose a GitHub user who will change, commit, and push the version in your `pyproject.toml` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

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

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                                  | DESCRIPTION                        |
| --------------- | ------------------------------------------------------ | ---------------------------------- |
| old-version     | `"${{ jobs.create-release.outputs.old-version }}"`     | The old version of the package.    |
| release-version | `"${{ jobs.create-release.outputs.release-version }}"` | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
