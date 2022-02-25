# helm-lint
To use this action you need to have a few things setup in the repository:

1. Add a `./github/lint-config.yaml` file with the following content and set the target branch to the default branch of your repository:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

2. Add the following steps to your workflow:
```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2
    with:
      # this is only needed if your workflow runs on pull_requests
      fetch-depth: 0

  # check out ci-templates into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
  
  # lint all charts
  - name: Lint helm charts
    uses: ./ci-templates/helm-lint
```

# helm release
This action will lint all charts, bump the version according to the `.bumpversion.cfg` file and create releases for all changed charts. To use this action you need to have a few things setup in the repository:

1. Add a `./github/lint-config.yaml` file with the following content and set `target-branch` to the default branch of your repository:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

2. Add an empty branch `gh-pages` for the index.yaml to be hosted publically:
```
git checkout --orphan gh-pages
git rm --cached .
git commit -m "Initial commit" --allow-empty
git push --set-upstream origin gh-pages
```

3. Add a `.bumpversion.cfg` file in the root directory of your repository with the following content. Make sure to replace the `CHART_NAME` with the folder name to your chart and `CHART_VERSION` with the current version of your chart found in the `Chart.yaml` file. If you have multiple charts in the same repository just copy the second block multiple times, but be aware that all charts in the same repository need to have the same version:
```cfg
[bumpversion]
current_version = CHART_VERSION
commit = True
tag = False

[bumpversion:file:charts/CHART_NAME/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

4. Choose a Github user that is going to push the tags and version updates. Create a repository secret for the Github username (`GH_USERNAME`), the Github Email (`GH_EMAIL`) and a personal access token (`GH_TOKEN`) of the user. For the email you can use the no reply github email: `[username]@users.noreply.github.com`. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch even if there is a protection rule in place.

6. Add the following steps to your workflow:
```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2
    with:
      # needed because the releaser scans for chart changes in multiple commits
      fetch-depth: 0
      # needed to push the bumped charts
      persist-credentials: false

  # check out ci-templates repository into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
  
  # lint, bump version and release all changed charts
  - name: Release charts
      uses: ./ci-templates/helm-release
      with:
        githubToken: "${{ secrets.GH_TOKEN }}"
        githubUsername: "${{ secrets.GH_USERNAME }}"
        githubEmail: "${{ secrets.GH_EMAIL }}"
```

## Optional parameters
You can optionally set the `releaseType` to `major`, `minor` or `patch`. This can also be done via a workflow input:
```yaml
name: release

on:
  workflow_dispatch:
    inputs:
      releaseType:
        description: "The type of the release."
        default: "patch"
        required: false

jobs:
  release:
    runs-on: ubuntu-20.04
    steps:
      # check out current repository
      - uses: actions/checkout@v2
        with:
          # needed because the releaser scans for chart changes in multiple commits
          fetch-depth: 0
          # needed to push the bumped charts
          persist-credentials: false

      # check out ci-templates repository into ./ci-templates
      - uses: actions/checkout@v2
        with:
          repository: "bakdata/ci-templates"
          path: "ci-templates"
      
      # lint, bump version and release all changed charts
      - name: Release charts
          uses: ./ci-templates/helm-release
          with:
            githubToken: "${{ secrets.GH_TOKEN }}"
            githubUsername: "${{ secrets.GH_USERNAME }}"
            githubEmail: "${{ secrets.GH_EMAIL }}"
            releaseType: "${{ github.event.inputs.releaseType }}"
```

# python-poetry-release

This workflow will bump the version of your python project and publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

## Prerequisite

Your Python project needs to be set up with poetry and contain a `pyproject.toml` file to use this workflow. Moreover,
choose a GitHub user who will change, commit, and push the version in your `pyproject.toml` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

## Dependencies

This workflow is built from multiple composite actions listed below:

* [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
* [python-poetry-release](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-release)
* [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

## Input Parameters

| Name              | Required |             Default Value             |  Type   | Description                                                                                                                        |
|-------------------|:--------:|:-------------------------------------:|:-------:|------------------------------------------------------------------------------------------------------------------------------------|
| release-type      |    ✅     |                   -                   | string  | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values  |
| ref               |    ❌     | The default branch of your repository | string  | The ref name to checkout the repository                                                                                            |
| publish-to-test   |    ❌     |                 true                  | boolean | If set to true, the packages are published to test.pypi.org other wise the packages are published to pypi.org                      |
| python-version    |    ❌     |                "3.10"                 | string  | The python version for setting up poetry.                                                                                          |
| poetry-version    |    ❌     |               "1.1.12"                | string  | The poetry version to be installed.                                                                                                |
| working-directory |    ❌     |                 "./"                  | string  | The working directory of your Python package.                                                                                      |

## Secret Parameters

These secrets define the GitHub user that pushes the changes of your `pyproject.toml` file to the repository. Create a
repository secret for the GitHub username (`GH_USERNAME`), the GitHub Email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the
email: `[username]@users.noreply.github.com`.

| Name            | Required | Description                                       |
|-----------------|:--------:|---------------------------------------------------|
| github-username |    ✅     | The GitHub username for committing the changes    |
| github-email    |    ✅     | The GitHub email for committing the changes       |
| github-token    |    ✅     | The GitHub token for committing the changes       |
| pypi-token      |    ✅     | The (test) PyPI api token for publishing packages |

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
    uses: bakdata/ci-templates/.github/workflows/python-poetry-release.yaml@main
    with:
      release-type: patch # (Required) See more values at: https://python-poetry.org/docs/cli/#version
      ref: my-awesome-ref # (Optional) if not set the ${{ github.event.repository.default_branch }} will fill the value. In this case the changes will be pushed to my-awesome-ref
      publish-to-test: false # (Optional) By default the packages are published to TestPyPI. In this case the packages are published to PyPI
      python-version: 3.8 # (Optional) Default value is 3.10. In this case poetry is installed with Python 3.8
      poetry-version: 1.1.11 # (Optional) Default value is 1.1.12. In this case poetry version 1.1.11 is installed
      working-directory: "./my-awesome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
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

