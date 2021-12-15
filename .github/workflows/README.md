# python-poetry-release

This action will bump the version of your python project and publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters documentation. In the end, you find a small example of how to
use this workflow.

## Prerequisite

Your Python project needs to be set up with poetry and contains a `pyproject.toml` file to use this workflow. Moreover,
choose a GitHub user who will change, commit, and push the version in your `pyproject.toml` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

## Dependencies

This workflow is build from multiple composite actions listed bellow:

* [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
* [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)
* [python-poetry-release](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-release)

## Input Parameters

| Name              | Required | Default Value  |  Type   | Description                                                                                                                        |
|-------------------|:--------:|:--------------:|:-------:|------------------------------------------------------------------------------------------------------------------------------------|
| release-type      |    ✅     |       -        | string  | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values  |
| ref               |    ✅     |       -        | string  | The ref name to checkout the repository                                                                                            |
| publish-to-test   |    ❌     |      true      | boolean | If set to true, the packages are published to test.pypi.org other wise the packages are published to pypi.org                      |
| python-version    |    ❌     |     "3.7"      | string  | The python version for setting up poetry.                                                                                          |
| poetry-version    |    ❌     |    "1.1.12"    | string  | The poetry version to be installed.                                                                                                |
| working-directory |    ❌     |      "./"      | string  | The working directory of your Python package.                                                                                      |

## Secret Parameters

These secrets define the GitHub user that pushes the changes of your `pyproject.toml` file to the repository. Create a
repository secret for the GitHub username (`GH_USERNAME`), the GitHub Email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the
email: `[username]@users.noreply.github.com`.

| Name            |  Required  | Description                                    |
|-----------------|:----------:|------------------------------------------------|
| github-username |     ✅      | The GitHub username for pushing                |
| github-email    |     ✅      | The GitHub email for pushing                   |
| github-token    |     ✅      | The GitHub token for pushing                   |
| pypi-token      |     ✅      | The (test) pypi api token for pushing packages |

## Outputs

This workflow outputs two variables: The `old-tag` and the `release-tag`. These variables can be used in the future
jobs (e.g., using the `release-tag` to create GitHub release).

| Name        | Description                                         |
|-------------|-----------------------------------------------------|
| old-tag     | Defines the old version in your pyproject.toml file |
| release-tag | The bumped version of your project                  |

## Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [ main ]

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-template/python-poetry-release.yaml@main
    with:
      release-type: patch # (Required) See more values at: https://python-poetry.org/docs/cli/#version
      ref: main # (Required) Some repositories still use master as a ref
      publish-to-test: false # (Optional) Default value true. In this case the packages are pushed to PyPI
      python-version: 3.8 # (Optional) Default value is 3.7. In this case poetry is installed with Python 3.8
      poetry-version: 1.1.11 # (Optional) Default value is 1.1.12. In this case poetry version 1.1.11 is installed
      working-directory: "./my-awsome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
    secrets:
      github-email: ${{ secrets.GH_EMAIL }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
      pypi-token: ${{ secrets.PYPI_API_TOKEN }}

  use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-tag }} to ${{ needs.call-workflow-passing-data.outputs.release-tag }}
```

