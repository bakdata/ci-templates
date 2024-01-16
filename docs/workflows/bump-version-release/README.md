<h1>Description bump-version-release reusable Workflow</h1>

This workflow will release your Bump Version project. That means it will bump the version according to your <code>release-type</code>, create a Git tag, and create a GitHub release with an optional changelog.

<h2>Prerequisites</h2>

A <code>.bumpversion.cfg</code> needs to be located inside <code>working-directory</code> (repository root by default) to use this workflow.
Moreover, prepare a <code>github-username</code>, a <code>github-email</code> and a <code>github-token</code> to push to GitHub.

<h2>Dependencies</h2>

This workflow is built from other composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/bump-version">bump-version</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate">changelog-generate</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/tag-and-release">tag-and-release</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "Scope of the release."
        type: choice
        required: true
        default: patch
        options:
          - patch
          - minor
          - major

jobs:
  call-workflow-passing-data:
    name: Release
    uses: bakdata/ci-templates/.github/workflows/bump-version-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}"
      changelog: false # (Optional) Default is true
      changelog-config: "./.github/changelog-config.json" # (Optional)
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

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED | DEFAULT |                           DESCRIPTION                           |
|-------------------|---------|----------|---------|-----------------------------------------------------------------|
|     changelog     | boolean |  false   | <code>true</code>  |                  Create changelog for release.                  |
| changelog-config  | string  |  false   |         |                     Changelog config path.                      |
|   release-type    | string  |   true   |         |          Scope of the release (major, minor or patch).          |
| working-directory | string  |  false   |  <code>"."</code>  | Working directory containing <code>.bumpversion.cfg</code>. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                      VALUE                      |                   DESCRIPTION                    |
|-----------------|-------------------------------------------------|--------------------------------------------------|
|   old-version   |   <code>"${{ jobs.release.outputs.old-version }}"</code>   | The old version in your <code>.bumpversion.cfg</code> file. |
| release-version | <code>"${{ jobs.release.outputs.release-version }}"</code> |               The bumped version.                |

<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                   DESCRIPTION                   |
|-----------------|----------|-------------------------------------------------|
|  github-email   |   true   |  The GitHub email for committing the changes.   |
|  github-token   |   true   |  The GitHub token for committing the changes.   |
| github-username |   true   | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
