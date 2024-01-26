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

This workflow is built from multiple composite actions listed below:

- [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
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
    uses: bakdata/ci-templates/.github/workflows/python-poetry-release.yaml@main
    with:
      release-type: patch # (Required) See more values at: https://python-poetry.org/docs/cli/#version
      ref: my-awesome-ref # (Optional) if not set the ${{ github.event.repository.default_branch }} will fill the value. In this case the changes will be pushed to my-awesome-ref
      python-version: 3.8 # (Optional) Default value is 3.10. In this case Poetry is installed with Python 3.8
      poetry-version: "1.1.11" # (Optional) Default value is 1.5.1. In this case Poetry version 1.1.11 is installed
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

|       INPUT       |  TYPE   | REQUIRED |                      DEFAULT                      |                                DESCRIPTION                                |
|-------------------|---------|----------|---------------------------------------------------|---------------------------------------------------------------------------|
|     changelog     | boolean |  false   |                      `true`                       |                       Create changelog for release.                       |
| changelog-config  | string  |  false   |                                                   |                          Changelog config path.                           |
|  changelog-file   | string  |  false   |                 `"CHANGELOG.md"`                  |            Path to the changelog file in the GitHub repository            |
|  poetry-version   | string  |  false   |                     `"1.5.1"`                     |          The Poetry version to be installed. (Default is 1.5.1)           |
|  python-version   | string  |  false   |                     `"3.10"`                      |        The Python version for setting up Poetry. (Default is 3.10)        |
|        ref        | string  |  false   | `"${{ github.event.repository.default_branch }}"` |                 The ref name to checkout the repository.                  |
|   release-type    | string  |   true   |                                                   |  Scope of the release; See: https://python-poetry.org/docs/cli/#version   |
| working-directory | string  |  false   |                      `"./"`                       | The working directory of your Python package. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->


### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                         VALUE                          |            DESCRIPTION             |
|-----------------|--------------------------------------------------------|------------------------------------|
|   old-version   |   `"${{ jobs.create-release.outputs.old-version }}"`   |  The old version of the package.   |
| release-version | `"${{ jobs.create-release.outputs.release-version }}"` | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->


### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                   DESCRIPTION                   |
|-----------------|----------|-------------------------------------------------|
|  github-email   |   true   |  The GitHub email for committing the changes.   |
|  github-token   |   true   |  The GitHub token for committing the changes.   |
| github-username |   true   | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
