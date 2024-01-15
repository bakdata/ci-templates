<h1>Description of release-tag-versions reusable Workflow</h1>

This workflow enables the release of tag versions as well as the creation of a new snapshot version for developers to work on the next release. The workflow allows you to choose the sort of release that will be performed as well as how to generate the snapshot version.

<h2>Prerequisites</h2>

Create, and configure your <code>.bumpversion.cfg</code> file and make sure it's in the <code>version-configs-dir</code> directory. A minimal configuration with <code>Chart.yaml</code> being the versioning file could look like this:

```cfg
[bumpversion]
current_version = 1.0.1-SNAPSHOT
parse = (?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(-(?P<suffix>\w+))?
serialize =
  {major}.{minor}.{patch}-{suffix}
  {major}.{minor}.{patch}

[bumpversion:file:path/to/Chart.yaml]
search =
  version: {current<em>version}
  appVersion: {current</em>version}
replace =
  version: {new<em>version}
  appVersion: {new</em>version}
```

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/bump-version">bump-version</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a>
</ul>

<h2>Calling the workflow</h2>

<code>yaml
name: Release multiple Helm Charts
on:
  workflow<em>dispatch:
    inputs:
      release-type:
        description: "Scope of the release (major, minor or patch)."
        required: true
        type: string
      next-dev-release-type:
        description: "Scope of the next release (minor or patch) for developers"
        required: true
        type: string
jobs:
  call-workflow-passing-data:
    name: Release &amp; Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/release-tag-versions.yaml@main
    with:
      version-configs-dir: "."
      release-type: "${{ inputs.release-type }}"
      next-dev-release-type: "${{ inputs.next-dev-release-type }}"
      next-dev-release-suffix: "SNAPSHOT"
    secrets:
      github-email: "${{ secrets.GH</em>EMAIL }}"
      github-username: "${{ secrets.GH<em>USERNAME }}"
      github-token: "${{ secrets.GH</em>TOKEN }}"
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|          INPUT          |  TYPE  | REQUIRED |   DEFAULT    |                                                DESCRIPTION                                                 |
|-------------------------|--------|----------|--------------|------------------------------------------------------------------------------------------------------------|
| next-dev-release-suffix | string |  false   | <code>"SNAPSHOT"</code> |                                The suffix to add for the developer version                                 |
|  next-dev-release-type  | string |   true   |              |                         Scope of the next release (minor or patch) for developers                          |
|      release-type       | string |   true   |              |                               Scope of the release (major, minor or patch).                                |
|   version-configs-dir   | string |   true   |              | The Path to the directory containing the file where the versioning is defined and <code>.bumpversion.cfg</code> file. |

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
