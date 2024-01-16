<h1>Description of helm-release reusable Workflow</h1>

This workflow will lint a Helm chart, bump its version according to the <code>.bumpversion.cfg</code> file, package the chart, update the Helm index, and deploy it on GitHub pages.

<h2>Prerequisites</h2>

Your Helm chart and <code>.bumpversion.cfg</code> need to be located inside the <code>charts-dir</code> folder of your repository (repository root by default) to use this workflow. A minimal configuration with <code>charts-dir=charts</code> could look like this:

```cfg
[bumpversion]
current_version = 0.0.1

[bumpversion:file:charts/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

Additionally, you need to create the lint configuration file <code>.github/lint-config.yaml</code> and configure it to your liking.
A minimal configuration could look like this:

```yaml

<h1>check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations</h1>

target-branch: "main"
```

Moreover, choose a GitHub user who will commit and push the changes. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch
even if there is a protection rule in place.

Finally, set up GitHub pages for your repository in Settings → Pages → Build and deployment source → GitHub Actions. A special <code>gh-pages</code> branch is not needed, since we will use GitHub actions to deploy a Pages artifact.
Currently, it is not possible to download a previously created Pages artifact as they quickly expire after deploying it. When releasing an update to a Helm chart, we want to keep all previous versions of the Helm chart available. Therefore, as a workaround, we download the <code>index.yaml</code> file from Pages, parse all referenced releases and download these .tgz packages from Pages as well. Then we package the new version and update the index. Afterward, a new Pages artifact is created from these files and finally deployed.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/helm-lint">helm-lint</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/bump-version">bump-version</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/helm-package">helm-package</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a>
</ul>

<h2>Calling the workflow</h2>

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

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT       |  TYPE   | REQUIRED |                      DEFAULT                      |                                                        DESCRIPTION                                                         |
|------------------|---------|----------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|   artifact-dir   | string  |  false   |                   <code>"artifact"</code>                    |                        Directory inside <code>charts-dir</code> for preparation of the GitHub pages artifact.                         |
|    charts-dir    | string  |  false   |                       <code>"."</code>                       |                            The directory containing the Helm chart and <code>.bumpversion.cfg</code> file.                            |
|   helm-version   | string  |  false   |                    <code>"v3.10.1"</code>                    |                                                     The Helm version.                                                      |
| lint-config-path | string  |  false   |           <code>".github/lint-config.yaml"</code>            | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
|     page-url     | string  |   true   |                                                   |                                     URL to the GitHub pages website of the repository.                                     |
|       ref        | string  |  false   | <code>"${{ github.event.repository.default_branch }}"</code> |                                          The ref name to checkout the repository.                                          |
|   release-type   | string  |   true   |                                                   |                                       Scope of the release (major, minor or patch).                                        |
|  skip-download   | boolean |  false   |                      <code>false</code>                      |   Skip downloading index.yaml and previous Chart versions from GitHub pages. (To be used during setup of this workflow)    |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                        VALUE                         |                   DESCRIPTION                    |
|-----------------|------------------------------------------------------|--------------------------------------------------|
|   old-version   |   <code>"${{ jobs.helm-release.outputs.old-version }}"</code>   | The old version in your <code>.bumpversion.cfg</code> file. |
| release-version | <code>"${{ jobs.helm-release.outputs.release-version }}"</code> |               The bumped version.                |

<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                   DESCRIPTION                   |
|-----------------|----------|-------------------------------------------------|
|  github-email   |   true   |  The GitHub email for committing the changes.   |
|  github-token   |   true   |  The GitHub token for committing the changes.   |
| github-username |   true   | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
