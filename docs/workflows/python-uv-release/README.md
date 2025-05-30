# Description of python-uv-release reusable Workflow

This workflow will bump the version of your Python project, create a Git tag, and make a release of your project on GitHub. Moreover, this workflow allows you to add a CHANGELOG.md automatically if you wish to do so.
In the following, you will first find the necessary prerequisites to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

## Prerequisites

Your Python project needs to be set up with uv and contain a `pyproject.toml` file to use this workflow.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [setup-uv](https://github.com/astral-sh/setup-uv)
- [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
- [tag-and-release](https://github.com/bakdata/ci-templates/tree/main/actions/tag-and-release)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)
- [changelog-generate](https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate)

## Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/python-uv-release.yaml@main
    with:
      release-type: patch # (Required)
      ref: my-awesome-ref # (Optional) if not set the ${{ github.event.repository.default_branch }} will fill the value. In this case the changes will be pushed to my-awesome-ref
      python-version: 3.11 # (Optional) Default value is 3.13. In this case uv is installed with Python 3.11
      uv-version: "0.5.11" # (Optional) Default value is 0.6.13. In this case uv version 0.5.11 is installed
      working-directory: "./my-awesome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
      changelog: false # (Optional) Default to true.
      changelog-config: ./my-changelog-config.json # (Optional) Set only if changelog is set to true. More information about it here https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate
    secrets:
      github-email: ${{ secrets.GH_EMAIL }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}

  use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT          | DESCRIPTION                                                     |
| ----------------- | ------- | -------- | ---------------- | --------------------------------------------------------------- |
| changelog         | boolean | false    | `true`           | Create changelog for release.                                   |
| changelog-config  | string  | false    |                  | Changelog config path.                                          |
| changelog-file    | string  | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository             |
| python-version    | string  | false    | `"3.13"`         | The Python version for setting up uv. (Default is 3.13)         |
| release-type      | string  | true     |                  | Scope of the release (major, minor or patch).                   |
| uv-version        | string  | false    | `"0.6.13"`       | The uv version to be installed. (Default is 0.6.13)             |
| working-directory | string  | false    | `"."`            | Working directory containing `.bumpversion.cfg`. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                                      |
| --------------- | ----------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
