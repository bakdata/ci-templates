# Description of helm-release reusable Workflow

This workflow will lint a Helm chart, bump its version according to the `.bumpversion.cfg` file, package the chart, update the Helm index, and deploy it on GitHub pages.

## Prerequisites

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
Currently, it is not possible to download a previously created Pages artifact as they quickly expire after deploying it. When releasing an update to a Helm chart, we want to keep all previous versions of the Helm chart available. Therefore, as a workaround, we download the `index.yaml` file from Pages, parse all referenced releases and download these .tgz packages from Pages as well. Then we package the new version and update the index. Afterward, a new Pages artifact is created from these files and finally deployed.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-lint](https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint)
- [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
- [helm-package](https://github.com/bakdata/ci-templates/tree/main/actions/helm-package)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

## Calling the workflow

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

## References

### Inputs

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

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                                | DESCRIPTION                                      |
| --------------- | ---------------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.helm-release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.helm-release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
