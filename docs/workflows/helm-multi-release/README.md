<h1>Description of helm-multi-release reusable Workflow</h1>

This workflow is for projects with one or multiple Helm charts. The workflow will lint all Helm charts, use the tag to bump the version, package the charts, update/create the Helm index, and deploy it on GitHub pages.

<h2>Prerequisites</h2>

All Helm charts need to be located in a corresponding subdir inside the <code>charts-path</code> folder of your repository. In case there is just one Helm chart, then pass the path to the directory containing the <code>Chart.yaml</code> to <code>charts-path</code>. Then give an empty subdir by setting <code>subdir</code> as follows: <code>subdirs: "['.']"</code>

Additionally, you need to create the lint configuration file <code>.github/lint-config.yaml</code> and configure it to your liking.
A minimal configuration could look like this:

```yaml

<h1>check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations</h1>

target-branch: "main"
```

Moreover, choose a GitHub user who will commit and push the changes. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch
even if there is a protection rule in place.

Finally, create a special <code>gh-pages</code> branch then set up GitHub pages for your repository in Settings → Pages → Build and deployment source → Deploy from a branch.

For each run we use the tag to bump the version and package new artifacts. We then check out the <code>gh-pages</code> branch, add the newly created artifacts and generate a new <code>index.yaml</code> file.
We upload the newly created artifacts as well as the <code>index.yaml</code> file to <code>gh-pages</code>. The index is then made available thanks to a GitHub pipeline that automatically builds and deploys pages.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint">helm-lint</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a>
</ul>

<h2>Calling the workflow</h2>

<h3>Multi-chart</h3>

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release &amp; Publish Helm chart
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

<h3>Single chart</h3>

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Release &amp; Publish Helm chart
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

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT       |  TYPE  | REQUIRED |           DEFAULT            |                                                        DESCRIPTION                                                         |
|------------------|--------|----------|------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|   artifact-dir   | string |  false   |        <code>"artifacts"</code>         |                       Directory next to <code>charts-path</code> for preparation of the GitHub pages artifact.                        |
|   charts-path    | string |   true   |                              |                                        The directory containing the Helm chart(s).                                         |
| gh-pages-branch  | string |  false   |         <code>"gh-pages"</code>         |                                          Name of branch containing the artifacts                                           |
|   helm-version   | string |  false   |         <code>"v3.10.1"</code>          |                                                     The Helm version.                                                      |
| lint-config-path | string |  false   | <code>".github/lint-config.yaml"</code> | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
|     subdirs      | string |   true   |                              |                                                 List of subdir to consider                                                 |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                   DESCRIPTION                   |
|-----------------|----------|-------------------------------------------------|
|  github-email   |   true   |  The GitHub email for committing the changes.   |
|  github-token   |   true   |  The GitHub token for committing the changes.   |
| github-username |   true   | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
