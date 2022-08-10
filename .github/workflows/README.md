# Workflow Templates

The following workflows can be found here:

* [Helm Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#helm-release)
* [Python Poetry Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#python-poetry-release)

## Helm Release

This workflow will lint all charts, bump the project version according to the `.bumpversion.cfg` file, create releases
for all changed charts and provide an `index.yaml` for all packaged charts as a GitHub web page.

### Prerequisites

Your helm charts need to be located inside the `charts` folder of your repository to use this workflow and you need
a `.bumpversion.cfg` file in your root directory. Make sure to set the correct path for the `Chart.yaml` file. A minimal
configuration could look like this:

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

Moreover, choose a GitHub user who will change, commit, and push the version in your `.bumpversion.cfg` file. Make sure
to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

Finally, add an empty branch `gh-pages` for the `index.yaml` to be hosted publicly:

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

| Name             | Required |             Default Value             |  Type  | Description                                                                                                                                |
|------------------|:--------:|:-------------------------------------:|:------:|--------------------------------------------------------------------------------------------------------------------------------------------|
| release-type     |    ✅     |                   -                   | string | The scope of the release (major, minor or patch)                                                                                           |
| ref              |    ❌     | The default branch of your repository | string | The ref name to checkout the repository                                                                                                    |
| lint-config-path |    ❌     |      ".github/lint-config.yaml"       | string | The path to the lint configuration file (For an example see <https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml>) |
| python-version   |    ❌     |                "3.10"                 | string | The python version for bump2version                                                                                                        |
| helm-version     |    ❌     |               "v3.4.0"                | string | The helm version                                                                                                                           |

### Secret Parameters

These secrets define the GitHub user that pushes the changes of your `.bumpversion.cfg` file to the repository. Create a
repository secret for the GitHub username (`GH_USERNAME`), the GitHub Email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the
email: `[username]@users.noreply.github.com`.

| Name            | Required | Description                                    |
|-----------------|:--------:|------------------------------------------------|
| github-username |    ✅     | The GitHub username for committing the changes |
| github-email    |    ✅     | The GitHub email for committing the changes    |
| github-token    |    ✅     | The GitHub token for committing the changes    |

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

| Name              | Required |             Default Value             |  Type   | Description                                                                                                                       |
|-------------------|:--------:|:-------------------------------------:|:-------:|-----------------------------------------------------------------------------------------------------------------------------------|
| release-type      |    ✅     |                   -                   | string  | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values |
| ref               |    ❌     | The default branch of your repository | string  | The ref name to checkout the repository                                                                                           |
| publish-to-test   |    ❌     |                 true                  | boolean | If set to true, the packages are published to test.pypi.org other wise the packages are published to pypi.org                     |
| python-version    |    ❌     |                "3.10"                 | string  | The python version for setting up poetry                                                                                          |
| poetry-version    |    ❌     |               "1.1.12"                | string  | The poetry version to be installed                                                                                                |
| working-directory |    ❌     |                 "./"                  | string  | The working directory of your Python package                                                                                      |

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

## Java Gradle Docker

This workflow will build, test and publish a Java Gradle project including a Jib image. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

### Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses Jib. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub and Docker.

### Dependencies

This workflow is built from multiple composite actions listed below:

* [java-gradle-build](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build)
* [java-gradle-test](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test)
* [java-gradle-build-jib-image](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib-image)
* [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
* [docker-publish](https://github.com/bakdata/ci-templates/tree/main/actions/docker-publish)
* [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                |
|-------------------|:--------:|:-------------:|:------:|--------------------------------------------|
| docker-publisher  |    ✅     |       -       | string | Publisher to prefix Docker image           |
| java-distribution |    ❌     |   microsoft   | string | Java distribution to be installed          |
| java-version      |    ❌     |      11       | string | Java version to be installed               |
| gradle-version    |    ❌     |    wrapper    | string | Gradle version to be installed             |
| working-directory |    ❌     |       .       | string | Working directory of your Gradle artifacts |

### Secret Parameters

For Sonarcloud you need to provide a `sonar-token` to publish code quality results. In case of Sonatype, the action
requires you to have a `signing-secret-key-ring` (base64 encoded), a `signing-key-id`, a `signing-password` to sign your
build artifacts and additionally a `ossrh-username` and a `ossrh-password` to publish the signed artifacts to Nexus. To
publish the docker image to DockerHub you need to provide a `docker-username` and a `docker-password`.
The `github-username` and `github-token` is required to query the GitHub API for generating a changelog when running on
a tag branch.

| Name                    | Required | Description                                        |
|-------------------------|:--------:|----------------------------------------------------|
| sonar-token             |    ✅     | Token for Sonarcloud                               |
| signing-secret-key-ring |    ✅     | Key ring file for signing the Sonatype publication |
| signing-key-id          |    ✅     | Key id for signing the Sonatype publication        |
| signing-password        |    ✅     | Password for signing the Sonatype publication      |
| ossrh-username          |    ✅     | Username for signing into Sonatype repository      |
| ossrh-password          |    ✅     | Password for signing into Sonatype repository      |
| docker-username         |    ✅     | Username for publishing to Dockerhub               |
| docker-password         |    ✅     | Password for publishing to Dockerhub               |
| github-username         |    ✅     | GitHub username for requesting changes from API    |
| github-token            |    ✅     | GitHub token for requesting changes from API       |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [ main ]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Docker
    uses: bakdata/ci-templates/.github/workflows/java-gradle-docker.yaml@main
    with:
      docker-publisher: "my-publisher" # (Required)
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "./" # (Optional) Default is ./      
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      signing-secret-key-ring: ${{ secrets.SIGNING_SECRET_KEY_RING }}
      signing-key-id: ${{ secrets.SIGNING_KEY_ID }}
      signing-password: ${{ secrets.SIGNING_PASSWORD }}
      ossrh-username: ${{ secrets.OSSHR_USERNAME }}
      ossrh-password: ${{ secrets.OSSHR_PASSWORD }}
      docker-username: ${{ secrets.DOCKERHUB_USERNAME }}
      docker-password: ${{ secrets.DOCKERHUB_TOKEN }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
```

## Java Gradle Library

This workflow will build, test and publish a Java Gradle library project. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

### Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the `plugin-publish-plugin` dependency. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub
and Gradle
Plugin Portal.

### Dependencies

This workflow is built from multiple composite actions listed below:

* [java-gradle-build](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build)
* [java-gradle-test](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test)
* [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
* [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                |
|-------------------|:--------:|:-------------:|:------:|--------------------------------------------|
| java-distribution |    ❌     |   microsoft   | string | Java distribution to be installed          |
| java-version      |    ❌     |      11       | string | Java version to be installed               |
| gradle-version    |    ❌     |    wrapper    | string | Gradle version to be installed             |
| working-directory |    ❌     |       .       | string | Working directory of your Gradle artifacts |

### Secret Parameters

For Sonarcloud you need to provide a `sonar-token` to publish code quality results. In case of Sonatype, the action
requires you to have a `signing-secret-key-ring` (base64 encoded), a `signing-key-id`, a `signing-password` to sign your
build artifacts and additionally a `ossrh-username` and a `ossrh-password` to publish the signed artifacts to Nexus. To
publish the gradle plugin to the Gradle Plugin Portal you need to provide a `gradle-publish-key` and
a `gradle-publish-secret`. The `github-username` and `github-token` is required to query the GitHub API for generating a
changelog when running on a tag branch.

| Name                    | Required | Description                                        |
|-------------------------|:--------:|----------------------------------------------------|
| sonar-token             |    ✅     | Token for Sonarcloud                               |
| signing-secret-key-ring |    ✅     | Key ring file for signing the Sonatype publication |
| signing-key-id          |    ✅     | Key id for signing the Sonatype publication        |
| signing-password        |    ✅     | Password for signing the Sonatype publication      |
| ossrh-username          |    ✅     | Username for signing into Sonatype repository      |
| ossrh-password          |    ✅     | Password for signing into Sonatype repository      |
| gradle-publish-key      |    ✅     | Key for publishing to Gradle Plugin Portal         |
| gradle-publish-secret   |    ✅     | Secret for publishing to Gradle Plugin Portal      |
| github-username         |    ✅     | GitHub username for requesting changes from API    |
| github-token            |    ✅     | GitHub token for requesting changes from API       |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [ main ]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Library
    uses: bakdata/ci-templates/.github/workflows/java-gradle-library.yaml@main
    with:
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "./" # (Optional) Default is ./
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      signing-secret-key-ring: ${{ secrets.SIGNING_SECRET_KEY_RING }}
      signing-key-id: ${{ secrets.SIGNING_KEY_ID }}
      signing-password: ${{ secrets.SIGNING_PASSWORD }}
      ossrh-username: ${{ secrets.OSSHR_USERNAME }}
      ossrh-password: ${{ secrets.OSSHR_PASSWORD }}
      gradle-publish-key: ${{ secrets.GRADLE_PUBLISH_KEY }}
      gradle-publish-secret: ${{ secrets.GRADLE_PUBLISH_SECRET }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
```

## Java Gradle Release

This workflow will release your Java Gradle project. That means it will bump the version according to
your `release-type`, push the bumped version to the default branch and a tag branch, push a new SNAPSHOT version commit
to the default branch and generate and push a changelog to the default branch.

### Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the `net.researchgate.release` dependency. Moreover, prepare credentials for pushing to GitHub.

### Dependencies

This workflow is built from another composite action listed below:

* [java-gradle-setup](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-setup)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                  |
|-------------------|:--------:|:-------------:|:------:|----------------------------------------------|
| release-type      |    ✅     |     patch     | string | Scope of the release (major, minor or patch) |
| java-distribution |    ❌     |   microsoft   | string | Java distribution to be installed            |
| java-version      |    ❌     |      11       | string | Java version to be installed                 |
| gradle-version    |    ❌     |    wrapper    | string | Gradle version to be installed               |
| working-directory |    ❌     |       .       | string | Working directory of your Gradle artifacts   |

### Secret Parameters

For committing and pushing the changes to GitHub you need to define a `github-username`, a `github-email` and
a `github-password`.

| Name            | Required | Description                                |
|-----------------|:--------:|--------------------------------------------|
| github-username |    ✅     | GitHub username for committing the changes |
| github-email    |    ✅     | GitHub email for committing the changes    |
| github-token    |    ✅     | GitHub token for committing the changes    |

### Outputs

This workflow outputs two variables: The `old-version` and the `release-version`. These variables can be used in the
future jobs (e.g., using the `release-version` to create GitHub release).

| Name            | Description                                            |
|-----------------|--------------------------------------------------------|
| old-version     | Defines the old version in your gradle.properties file |
| release-version | The bumped version of your project                     |

### Calling the workflow

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "The scope of the release (major, minor or patch)."
        default: "patch"
        required: false

jobs:
  call-workflow-passing-data:
    name: Java Gradle Release
    uses: bakdata/ci-templates/.github/workflows/java-gradle-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}" # (Optional) Default is patch
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "./" # (Optional) Default is ./
    secrets:
      github-username: "${{ secrets.GH_USERNAME }}"
      github-email: "${{ secrets.GH_EMAIL }}"
      github-token: "${{ secrets.GH_TOKEN }}"

  use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```
