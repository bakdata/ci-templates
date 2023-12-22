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
