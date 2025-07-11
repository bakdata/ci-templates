# Description of helm-multi-release reusable Workflow

This workflow is for projects with one or multiple Helm charts. The workflow will lint all Helm charts, use the tag to bump the version, package the charts, update/create the Helm index, and deploy it on GitHub pages.

## Prerequisites

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

## Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-lint](https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

## Calling the workflow

### Multi-chart

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release & Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/helm-multi-release.yaml@main
    with:
      charts-path: "./charts"
      subdirs: "['subdir1', 'subdir2', 'subdir3']"
      gh-pages-branch: gh-pages
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```

### Single chart

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release & Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/helm-multi-release.yaml@main
    with:
      charts-path: "./helm-chart"
      subdirs: "['.']"
      gh-pages-branch: gh-pages
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                                                                |
| ---------------- | ------ | -------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| artifact-dir     | string | false    | `"artifacts"`                | Directory next to `charts-path` for preparation of the GitHub pages artifact.                                              |
| charts-dir       | string | true     |                              | The directory containing the Helm chart(s).                                                                                |
| gh-pages-branch  | string | false    | `"gh-pages"`                 | Name of branch containing the artifacts                                                                                    |
| helm-version     | string | false    | `"v3.10.1"`                  | The Helm version.                                                                                                          |
| lint-config-path | string | false    | `".github/lint-config.yaml"` | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| subdirs          | string | true     |                              | List of subdir to consider                                                                                                 |
| version          | string | true     |                              | version to publish                                                                                                         |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
