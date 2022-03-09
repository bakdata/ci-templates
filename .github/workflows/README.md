# Workflow Templates
The following workflows can be found here:
* [Helm Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#helm-release)
* [Python Poetry Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#python-poetry-release)

## Helm Release
This workflow will lint all charts, bump the project version according to the `.bumpversion.cfg` file, create releases for all changed charts
and provide an `index.yaml` for all packaged charts as a Github web page.

### Prerequisites
Your helm charts need to be located inside the `charts` folder of your repository to use this workflow and
you need a `.bumpversion.cfg` file in your root directory. Make sure to set the correct path for the `Chart.yaml` file.
A minimal configuration could look like this:
```cfg
[bumpversion]
current_version = 0.0.1
commit = True
tag = False

[bumpversion:file:charts/my-chart/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

Additionally, you need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

Moreover, choose a GitHub user who will change, commit, and push the version in your `.bumpversion.cfg` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

Finally, add an empty branch `gh-pages` for the `index.yaml` to be hosted publically:
```sh
git checkout --orphan gh-pages
git rm --cached .
git commit -m "Initial commit" --allow-empty
git push --set-upstream origin gh-pages
```

### Dependencies
This workflow is built from multiple composite actions listed below:

* [helm-lint](https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint)
* [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
* [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

### Input Parameters
| Name              | Required  |             Default Value             |  Type   | Description                                                                                                                              |
|-------------------|:---------:|:-------------------------------------:|:-------:|------------------------------------------------------------------------------------------------------------------------------------------|
| release-type      |    ✅     |                  -                    | string  | The scope of the release (major, minor or patch)                                                                                         |
| ref               |    ❌     | The default branch of your repository | string  | The ref name to checkout the repository                                                                                                  |
| lint-config-path  |    ❌     |      ".github/lint-config.yaml"       | string  | The path to the lint configuration file (For an example see https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml) |
| python-version    |    ❌     |                "3.10"                 | string  | The python version for bump2version                                                                                                      |
| helm-version      |    ❌     |               "v3.4.0"                | string  | The helm version                                                                                                                         |

### Secret Parameters
These secrets define the GitHub user that pushes the changes of your `.bumpversion.cfg` file to the repository. Create a
repository secret for the GitHub username (`GH_USERNAME`), the GitHub Email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the
email: `[username]@users.noreply.github.com`.

| Name            | Required  | Description                                       |
|-----------------|:---------:|---------------------------------------------------|
| github-username |    ✅     | The GitHub username for committing the changes    |
| github-email    |    ✅     | The GitHub email for committing the changes       |
| github-token    |    ✅     | The GitHub token for committing the changes       |

### Outputs
This workflow outputs two variables: The `old-tag` and the `release-tag`. These variables can be used in the future
jobs (e.g., using the `release-tag` to create GitHub release).

| Name        | Description                                           |
|-------------|-------------------------------------------------------|
| old-tag     | Defines the old version in your .bumpversion.cfg file |
| release-tag | The bumped version of your project                    |

### Calling the workflow
```yaml
name: Call this reusable workflow

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "The scope of the release (major, minor or patch)."
        default: "patch"
        required: false

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/helm-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}"
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-config.yaml" # (Optional)
      helm-version: "v3.4.0" # (Optional)
      python-version: "3.8" # (Optional)
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```


## Python Poetry Release
This workflow will bump the version of your python project and publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

### Prerequisites
Your Python project needs to be set up with poetry and contain a `pyproject.toml` file to use this workflow. Moreover,
choose a GitHub user who will change, commit, and push the version in your `pyproject.toml` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

### Dependencies
This workflow is built from multiple composite actions listed below:

* [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
* [python-poetry-release](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-release)
* [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

### Input Parameters
| Name              | Required  |             Default Value             |  Type   | Description                                                                                                                        |
|-------------------|:---------:|:-------------------------------------:|:-------:|------------------------------------------------------------------------------------------------------------------------------------|
| release-type      |    ✅     |                   -                   | string  | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values  |
| ref               |    ❌     | The default branch of your repository | string  | The ref name to checkout the repository                                                                                            |
| publish-to-test   |    ❌     |                 true                  | boolean | If set to true, the packages are published to test.pypi.org other wise the packages are published to pypi.org                      |
| python-version    |    ❌     |                "3.10"                 | string  | The python version for setting up poetry                                                                                           |
| poetry-version    |    ❌     |               "1.1.12"                | string  | The poetry version to be installed                                                                                                 |
| working-directory |    ❌     |                 "./"                  | string  | The working directory of your Python package                                                                                       |

### Secret Parameters
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

### Outputs
This workflow outputs two variables: The `old-tag` and the `release-tag`. These variables can be used in the future
jobs (e.g., using the `release-tag` to create GitHub release).

| Name        | Description                                         |
|-------------|-----------------------------------------------------|
| old-tag     | Defines the old version in your pyproject.toml file |
| release-tag | The bumped version of your project                  |

### Calling the workflow
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
