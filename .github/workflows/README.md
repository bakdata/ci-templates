# Workflow Templates

The following workflows can be found here:

- [Helm Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#helm-release)
- [Helm Multi Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#helm-multi-release)
- [Kustomize GKE Deploy](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#kustomize-gke-deploy)
- [Kustomize GKE Destroy](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#kustomize-gke-destroy)
- [Python Poetry Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#python-poetry-release)
- [Java Gradle Docker](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#java-gradle-docker)
- [Java Gradle Library](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#java-gradle-library)
- [Java Gradle Plugin](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#java-gradle-plugin)
- [Java Gradle Release](https://github.com/bakdata/ci-templates/tree/main/.github/workflows#java-gradle-release)

## Helm Release

This workflow will lint a Helm chart, bump its version according to the `.bumpversion.cfg` file, package the chart, update the Helm index, and deploy it on GitHub pages.

### Prerequisites

Your Helm chart and `.bumpversion.cfg` need to be located inside the `charts-dir` folder of your repository (repository root by default) to use this workflow. A minimal configuration with `charts-dir=charts` could look like this:

```cfg
[bumpversion]
current_version = 0.0.1

[bumpversion:file:charts/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

Additionally, you need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:

```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

Moreover, choose a GitHub user who will commit and push the changes. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch
even if there is a protection rule in place.

Finally, set up GitHub pages for your repository in Settings → Pages → Build and deployment source → GitHub Actions. A special `gh-pages` branch is not needed, since we will use GitHub actions to deploy a Pages artifact.

Currently it is not possible to download a previously created Pages artifact as they quickly expire after deploying it. When releasing an update to a Helm chart, we want to keep all previous versions of the Helm chart available. Therefore, as a workaround, we download the index.yaml file from Pages, parse all referenced releases, and download these .tgz packages from Pages as well. Then we package the new version and update the index. Afterwards, a new Pages artifact is created from these files and finally deployed.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-lint](https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint)
- [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
- [helm-package](https://github.com/bakdata/ci-templates/tree/main/actions/helm-package)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

### Input Parameters

| Name             | Required |             Default Value             |  Type  | Description                                                                                                                                |
| ---------------- | :------: | :-----------------------------------: | :----: | ------------------------------------------------------------------------------------------------------------------------------------------ |
| page-url         |    ✅    |                                       | string | URL to the GitHub pages website of the repository.                                                                                         |
| release-type     |    ✅    |                   -                   | string | The scope of the release (major, minor or patch)                                                                                           |
| ref              |    ❌    | The default branch of your repository | string | The ref name to checkout the repository                                                                                                    |
| lint-config-path |    ❌    |      ".github/lint-config.yaml"       | string | The path to the lint configuration file (For an example see <https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml>) |
| helm-version     |    ❌    |               "v3.10.1"               | string | The Helm version                                                                                                                           |
| charts-dir       |    ❌    |                  "."                  | string | The directory containing the Helm chart and `.bumpversion.cfg` file                                                                        |
| skip-download    |    ❌    |                "false"                | string | Skip downloading index.yaml and previous Chart versions from GitHub pages. (To be used during setup of this workflow)                      |
| artifact-dir     |    ❌    |              "artifact"               | string | Directory inside `charts-dir` for preparation of the GitHub pages artifact.                                                                |

### Secret Parameters

These secrets define the GitHub user that pushes the changes of your `.bumpversion.cfg` and `Chart.yaml` file to the repository. Create a repository secret for the GitHub username (`GH_USERNAME`), the GitHub email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the email: `[username]@users.noreply.github.com`.

| Name            | Required | Description                                    |
| --------------- | :------: | ---------------------------------------------- |
| github-username |    ✅    | The GitHub username for committing the changes |
| github-email    |    ✅    | The GitHub email for committing the changes    |
| github-token    |    ✅    | The GitHub token for committing the changes    |

### Outputs

This workflow outputs two variables: The `old-tag` and the `release-tag`. These variables can be used in subsequent jobs (e.g., using the `release-tag` to create GitHub release).

| Name        | Description                                           |
| ----------- | ----------------------------------------------------- |
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
      page-url: https://example.github.io/your-repository
      release-type: ${{ inputs.release-type }}
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-config.yaml" # (Optional)
      helm-version: "v3.10.1" # (Optional)
      charts-dir: charts # (Optional)
      skip-download: "false" # (Optional)
      artifact-dir: "artifact" # (Optional)
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```

## Helm Multi Release

This workflow is for projects with one or multiple Helm charts. The workflow will lint all Helm charts, use the tag to bump the version, package the charts, update/create the Helm index, and deploy it on GitHub pages.

### Prerequisites

All Helm charts need to be located in a corresponding subdir inside the `charts-path` folder of your repository. In case there is just one Helm chart, then pass the path to the directory containing the `Chart.yaml` to `charts-path`. Then give an empty subdir by setting `subdir` as follows: `subdirs: "['.']"`

Additionally, you need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:

```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

Moreover, choose a GitHub user who will commit and push the changes. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch
even if there is a protection rule in place.

Finally, create a special `gh-pages` branch then set up GitHub pages for your repository in Settings → Pages → Build and deployment source → Deploy from a branch. 

For each run we use the tag to bump the version and package new artifacts. We then check out the `gh-pages` branch, add the newly created artifacts and generate a new `index.yaml` file.
We upload the newly created artifacts as well as the `index.yaml` file to `gh-pages`. The index is then made available thanks to a GitHub pipeline that automatically builds and deploys pages.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-lint](https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

### Input Parameters

| Name             | Required |             Default Value             |  Type  | Description                                                                                                                                |
| ---------------- | :------: |:-------------------------------------:| :----: |--------------------------------------------------------------------------------------------------------------------------------------------|
| charts-path       |    ✅     |                                       | string | The path to the directory containing the Helm charts                                                                                                   |
| subdirs              |    ✅   |  | string | List of subdir to consider" Format:  "['subdir1', 'subdir2', 'subdir3']"                                                                   |
| artifact-dir     |    ❌    |              "artifacts"              | string | Directory inside `charts-dir` for preparation of the GitHub pages artifact.                                                                |
| gh-pages-branch    |    ❌    |              "gh-pages"               | string | The branch containing all the artifacts                                                                                                    |
| root-branch              |    ❌   |                 "main                      | string | The main branch where the changes in the Helm Charts should be stored repository                                                                                                    |
| helm-version     |    ❌    |               "v3.10.1"               | string | The Helm version                                                                                                                           |
| lint-config-path |    ❌    |      ".github/lint-config.yaml"       | string | The path to the lint configuration file (For an example see <https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml>) |

### Secret Parameters

These secrets define the GitHub user that pushes our changes to the repository. Create a repository secret for the GitHub username (`GH_USERNAME`), the GitHub email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the email: `[username]@users.noreply.github.com`.

| Name            | Required | Description                                    |
| --------------- | :------: | ---------------------------------------------- |
| github-username |    ✅    | The GitHub username for committing the changes |
| github-email    |    ✅    | The GitHub email for committing the changes    |
| github-token    |    ✅    | The GitHub token for committing the changes    |


### Calling the workflow

#### Multi chart

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release & Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/helm-multi-release.yaml@multi-release
    with:
      charts-path: "./charts"
      subdirs: "['subdir1', 'subdir2', 'subdir3']"
      gh-pages-branch: gh-pages
      root-branch: main
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```

#### Single chart

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release & Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/helm-multi-release.yaml@multi-release
    with:
      root-branch: main
      charts-path: "./helm-chart"
      subdirs: "['.']"
      gh-pages-branch: gh-pages
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"

```

## Kustomize GKE Deploy

This workflow will deploy to GKE using a Kustomize root directory.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-setup](https://github.com/bakdata/ci-templates/tree/main/actions/helm-gke-setup)
- [kustomize-gke-deploy](https://github.com/bakdata/ci-templates/tree/main/actions/kustomize-gke-deploy)

### Input Parameters

| Name               | Required | Default Value |  Type  | Description                                         |
| ------------------ | :------: | :-----------: | :----: | --------------------------------------------------- |
| kustomization-path |    ✅    |       -       | string | Path to the root directory of the kustomization     |
| timeout            |    ❌    |      60       | string | Time out(in seconds) for CustomResourceDefinitions |
| python-version     |    ❌    |    "3.10"     | string |  Python version                                  |
| gcloud-sdk-version |    ❌    |   "376.0.0"   | string | GCloud-SDK version                              |
| kubectl-version    |    ❌    |   "v1.23.0"   | string | Kubectl version                                 |
| helm-version       |    ❌    |   "v3.8.1"    | string | Helm version                                    |

### Secret Parameters

The GKE cluster that will be used for the deployment is defined by these secrets. Create those secrets so that the pipeline has the necessary access to the targeted cluster.

| Name                | Required | Description                                |
| ------------------- | :------: | ------------------------------------------ |
| gke-service-account |    ✅    | GKE service account key for authentication |
| gke-project         |    ✅    | GKE project id for authentication          |
| gke-region          |    ✅    | GKE region for authentication              |
| gke-cluster         |    ✅    | GKE cluster for authentication             |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  workflow_dispatch:
    inputs:
      kustomization-path:
        description: "Path to the root directory of the kustomization"
        default: "kustomization-path"
        required: false
      timeout:
        description: "Time out(in seconds) for CustomResourceDefinitions"
        default: "60"
        required: false

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/kustomize-gke-deploy.yaml@main
    with:
      kustomization-path: ${{ inputs.kustomization-path }}
      timeout: ${{ inputs.timeout }} #optional
      python-version: "3.10" #optional
      gcloud-sdk-version: "376.0.0" #optional
      kubectl-version: "v1.23.0" #optional
      helm-version: "v3.8.1"
    secrets:
      gke-service-account: ${{ secrets.GKE_DEV_SERVICE_ACCOUNT }}
      gke-project: ${{ secrets.GKE_DEV_PROJECT }}
      gke-region: ${{ secrets.GKE_DEV_REGION }}
      gke-cluster: ${{ secrets.GKE_DEV_CLUSTER }}
```

## Kustomize GKE Destroy

This workflow will uninstall deployments using Kustomize.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-setup](https://github.com/bakdata/ci-templates/tree/main/actions/helm-gke-setup)
- [kustomize-gke-destroy](https://github.com/bakdata/ci-templates/tree/main/actions/kustomize-gke-destroy)

### Input Parameters

| Name               | Required | Default Value |  Type  | Description                                     |
| ------------------ | :------: | :-----------: | :----: | ----------------------------------------------- |
| kustomization-path |    ✅    |       -       | string | Path to the root directory of the kustomization |
|  python-version     |    ❌    |    "3.10"     | string |  The Python version                              |
| gcloud-sdk-version |    ❌    |   "376.0.0"   | string | GCloud-SDK version                          |
| kubectl-version    |    ❌    |   "v1.23.0"   | string | Kubectl version                             |
| helm-version       |    ❌    |   "v3.8.1"    | string | Helm version                                |

### Secret Parameters

The GKE cluster that will be used for the deployment is defined by these secrets. Create those secrets so that the pipeline has the necessary access to the targeted cluster.

| Name                | Required | Description                                |
| ------------------- | :------: | ------------------------------------------ |
| gke-service-account |    ✅    | GKE service account key for authentication |
| gke-project         |    ✅    | GKE project id for authentication          |
| gke-region          |    ✅    | GKE region for authentication              |
| gke-cluster         |    ✅    | GKE cluster for authentication             |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  workflow_dispatch:
    inputs:
      kustomization-path:
        description: "Path to the root directory of the kustomization"
        default: "kustomization-path"
        required: false
      timeout:
        description: "Time out(in seconds) for CustomResourceDefinitions"
        default: "60"
        required: false

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/kustomize-gke-destroy.yaml@main
    with:
      kustomization-path: ${{ inputs.kustomization-path }}
      python-version: "3.10" #optional
      gcloud-sdk-version: "376.0.0" #optional
      kubectl-version: "v1.23.0" #optional
      helm-version: "v3.8.1" #optional
    secrets:
      gke-service-account: ${{ secrets.GKE_DEV_SERVICE_ACCOUNT }}
      gke-project: ${{ secrets.GKE_DEV_PROJECT }}
      gke-region: ${{ secrets.GKE_DEV_REGION }}
      gke-cluster: ${{ secrets.GKE_DEV_CLUSTER }}
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

- [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
- [python-poetry-release](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-release)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

### Input Parameters

| Name              | Required |             Default Value             |  Type   | Description                                                                                                                       |
| ----------------- | :------: | :-----------------------------------: | :-----: | --------------------------------------------------------------------------------------------------------------------------------- |
| release-type      |    ✅    |                   -                   | string  | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values |
| ref               |    ❌    | The default branch of your repository | string  | ref name to checkout the repository                                                                                           |
| publish-to-test   |    ❌    |                 true                  | boolean | If set to true, the packages are published to test.pypi.org other wise the packages are published to pypi.org                     |
| python-version    |    ❌    |                "3.10"                 | string  |  Python version for setting up poetry                                                                                          |
| poetry-version    |    ❌    |               "1.1.12"                | string  | Poetry version to be installed                                                                                                |
| working-directory |    ❌    |                 "./"                  | string  | Working directory of your Python package                                                                                      |

### Secret Parameters

These secrets define the GitHub user that pushes the changes of your `pyproject.toml` file to the repository. Create a
repository secret for the GitHub username (`GH_USERNAME`), the GitHub Email (`GH_EMAIL`), and a personal access
token (`GH_TOKEN`) of the user. You can use the no reply GitHub email for the
email: `[username]@users.noreply.github.com`.

| Name            | Required | Description                                       |
| --------------- | :------: | ------------------------------------------------- |
| github-username |    ✅    | The GitHub username for committing the changes    |
| github-email    |    ✅    | The GitHub email for committing the changes       |
| github-token    |    ✅    | The GitHub token for committing the changes       |
| pypi-token      |    ✅    | The (test) PyPI api token for publishing packages |

### Outputs

This workflow outputs two variables: The `old-tag` and the `release-tag`. These variables can be used in the future
jobs (e.g., using the `release-tag` to create GitHub release).

| Name        | Description                                         |
| ----------- | --------------------------------------------------- |
| old-tag     | Defines the old version in your pyproject.toml file |
| release-tag | The bumped version of your project                  |

### Calling the workflow

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

This workflow will build, test and publish a Java Gradle project including a tarball image. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

### Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar), [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) and [Jib](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub and Docker.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [java-gradle-build](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build)
- [java-gradle-test](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test)
- [java-gradle-build-jib](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib)
- [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
- [docker-publish](https://github.com/bakdata/ci-templates/tree/main/actions/docker-publish)
- [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| docker-publisher  |    ✅    |       -       | string | Publisher to prefix Docker image                                                                              |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory |    ❌    |       .       | string | Working directory of your Gradle artifacts                                                                    |

### Secret Parameters

For Sonarcloud you need to provide a `sonar-token` and a `sonar-organization` to publish code quality results. In case of Sonatype, the action
requires you to have a `signing-secret-key-ring` (base64 encoded), a `signing-key-id` and a `signing-password` to sign
your build artifacts and additionally an `ossrh-username` and an `ossrh-password` to publish the signed artifacts to
Nexus. To publish the Docker image to DockerHub you need to provide a `docker-username` and a `docker-password`.
The `github-username` and `github-token` is required to query the GitHub API for generating a changelog when running on
a tag branch.

| Name                    | Required | Description                                                    |
| ----------------------- | :------: | -------------------------------------------------------------- |
| sonar-token             |    ✅    | Token for Sonarcloud                                           |
| sonar-organization      |    ✅    | Organization for Sonarcloud                                    |
| signing-secret-key-ring |    ✅    | Key ring (base64 encoded) for signing the Sonatype publication |
| signing-key-id          |    ✅    | Key id for signing the Sonatype publication                    |
| signing-password        |    ✅    | Password for signing the Sonatype publication                  |
| ossrh-username          |    ✅    | Username for signing into Sonatype repository                  |
| ossrh-password          |    ✅    | Password for signing into Sonatype repository                  |
| docker-username         |    ✅    | Username for publishing to Dockerhub                           |
| docker-password         |    ✅    | Password for publishing to Dockerhub                           |
| github-username         |    ✅    | GitHub username for requesting changes from API                |
| github-token            |    ✅    | GitHub token for requesting changes from API                   |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Docker
    uses: bakdata/ci-templates/.github/workflows/java-gradle-docker.yaml@main
    with:
      docker-publisher: "my-publisher" # (Required)
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "." # (Optional) Default is .
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      sonar-organization: ${{ secrets.SONARCLOUD_ORGANIZATION }}
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
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar) and [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype and GitHub.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [java-gradle-build](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build)
- [java-gradle-test](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test)
- [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
- [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory |    ❌    |       .       | string | Working directory of your Gradle artifacts                                                                    |

### Secret Parameters

For Sonarcloud you need to provide a `sonar-token` and a `sonar-organization` to publish code quality results. In case of Sonatype, the action
requires you to have a `signing-secret-key-ring` (base64 encoded), a `signing-key-id` and a `signing-password` to sign
your build artifacts and additionally an `ossrh-username` and an `ossrh-password` to publish the signed artifacts to
Nexus. The `github-username` and `github-token` are required to query the GitHub API for generating a
changelog when running on a tag branch.

| Name                    | Required | Description                                                    |
| ----------------------- | :------: | -------------------------------------------------------------- |
| sonar-token             |    ✅    | Token for Sonarcloud                                           |
| sonar-organization      |    ✅    | Organization for Sonarcloud                                    |
| signing-secret-key-ring |    ✅    | Key ring (base64 encoded) for signing the Sonatype publication |
| signing-key-id          |    ✅    | Key id for signing the Sonatype publication                    |
| signing-password        |    ✅    | Password for signing the Sonatype publication                  |
| ossrh-username          |    ✅    | Username for signing into Sonatype repository                  |
| ossrh-password          |    ✅    | Password for signing into Sonatype repository                  |
| github-username         |    ✅    | GitHub username for requesting changes from API                |
| github-token            |    ✅    | GitHub token for requesting changes from API                   |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Library
    uses: bakdata/ci-templates/.github/workflows/java-gradle-library.yaml@main
    with:
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "." # (Optional) Default is .
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      sonar-organization: ${{ secrets.SONARCLOUD_ORGANIZATION }}
      signing-secret-key-ring: ${{ secrets.SIGNING_SECRET_KEY_RING }}
      signing-key-id: ${{ secrets.SIGNING_KEY_ID }}
      signing-password: ${{ secrets.SIGNING_PASSWORD }}
      ossrh-username: ${{ secrets.OSSHR_USERNAME }}
      ossrh-password: ${{ secrets.OSSHR_PASSWORD }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
```

## Java Gradle Plugin

This workflow will build, test and publish a Java Gradle plugin project to the Gradle Plugin Portal. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

### Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar), [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) and [Plugin Publish](https://plugins.gradle.org/plugin/com.gradle.plugin-publish) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub
and Gradle Plugin Portal.

### Dependencies

This workflow is built from multiple composite actions listed below:

- [java-gradle-build](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build)
- [java-gradle-test](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test)
- [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
- [java-gradle-publish-plugin](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish-plugin)
- [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory |    ❌    |       .       | string | Working directory of your Gradle artifacts                                                                    |

### Secret Parameters

For Sonarcloud you need to provide a `sonar-token` and a `sonar-organization` to publish code quality results. In case of Sonatype, the action
requires you to have a `signing-secret-key-ring` (base64 encoded), a `signing-key-id` and a `signing-password` to sign
your build artifacts and additionally an `ossrh-username` and an `ossrh-password` to publish the signed artifacts to
Nexus. To publish the Gradle plugin to the Gradle Plugin Portal you need to provide a `gradle-publish-key` and
a `gradle-publish-secret`. The `github-username` and `github-token` are required to query the GitHub API for generating a
changelog when running on a tag branch.

| Name                    | Required | Description                                                    |
| ----------------------- | :------: | -------------------------------------------------------------- |
| sonar-token             |    ✅    | Token for Sonarcloud                                           |
| sonar-organization      |    ✅    | Organization for Sonarcloud                                    |
| signing-secret-key-ring |    ✅    | Key ring (base64 encoded) for signing the Sonatype publication |
| signing-key-id          |    ✅    | Key id for signing the Sonatype publication                    |
| signing-password        |    ✅    | Password for signing the Sonatype publication                  |
| ossrh-username          |    ✅    | Username for signing into Sonatype repository                  |
| ossrh-password          |    ✅    | Password for signing into Sonatype repository                  |
| gradle-publish-key      |    ✅    | Key for publishing to Gradle Plugin Portal                     |
| gradle-publish-secret   |    ✅    | Secret for publishing to Gradle Plugin Portal                  |
| github-username         |    ✅    | GitHub username for requesting changes from API                |
| github-token            |    ✅    | GitHub token for requesting changes from API                   |

### Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Library
    uses: bakdata/ci-templates/.github/workflows/java-gradle-library.yaml@main
    with:
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      working-directory: "." # (Optional) Default is .
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      sonar-organization: ${{ secrets.SONARCLOUD_ORGANIZATION }}
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
file that uses the [Researchgate Release](https://plugins.gradle.org/plugin/net.researchgate.release) plugin. Moreover, prepare a `github-username`, a `github-email` and a `github-token` to push to GitHub.

### Dependencies

This workflow is built from another composite action listed below:

- [java-gradle-setup](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-setup)

### Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| release-type      |    ✅    |     patch     | string | Scope of the release (major, minor or patch)                                                                  |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory |    ❌    |       .       | string | Working directory of your Gradle artifacts                                                                    |

### Secret Parameters

For committing and pushing the changes to GitHub you need to define a `github-username`, a `github-email` and
a `github-token`.

| Name            | Required | Description                                |
| --------------- | :------: | ------------------------------------------ |
| github-username |    ✅    | GitHub username for committing the changes |
| github-email    |    ✅    | GitHub email for committing the changes    |
| github-token    |    ✅    | GitHub token for committing the changes    |

### Outputs

This workflow outputs two variables: The `old-version` and the `release-version`. These variables can be used in the
future jobs (e.g., using the `release-version` to create a GitHub release).

| Name            | Description                                  |
| --------------- | -------------------------------------------- |
| old-version     | Old version from your gradle.properties file |
| release-version | Bumped version of your project               |

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
      working-directory: "." # (Optional) Default is .
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
