<h1>Description of python-poetry-release reusable Workflow</h1>

This workflow will bump the version of your Python project, create a Git tag, and make a release of your project on GitHub. Moreover, this workflow allows you to add a CHANGELOG.md automatically if you wish to do so.
In the following, you will first find the necessary prerequisites to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

<h2>Prerequisites</h2>

Your Python project needs to be set up with Poetry and contain a <code>pyproject.toml</code> file to use this workflow. Moreover,
choose a GitHub user who will change, commit, and push the version in your <code>pyproject.toml</code> file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version">python-poetry-bump-version</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/tag-and-release">tag-and-release</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate">changelog-generate</a>
</ul>

<h2>Calling the workflow</h2>

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
      ref: my-awesome-ref # (Optional) if not set the ${{ github.event.repository.default<em>branch }} will fill the value. In this case the changes will be pushed to my-awesome-ref
      python-version: 3.8 # (Optional) Default value is 3.10. In this case Poetry is installed with Python 3.8
      poetry-version: "1.1.11" # (Optional) Default value is 1.5.1. In this case Poetry version 1.1.11 is installed
      working-directory: "./my-awesome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
      changelog: false # (Optional) Default to true.
      changelog-config: ./my-changelog-config.json # (Optional) Set only if changelog is set to true. More information about it here https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate
    secrets:
      github-email: ${{ secrets.GH</em>EMAIL }}
      github-username: ${{ secrets.GH<em>USERNAME }}
      github-token: ${{ secrets.GH</em>TOKEN }}

use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED |                      DEFAULT                      |                                DESCRIPTION                                |
|-------------------|---------|----------|---------------------------------------------------|---------------------------------------------------------------------------|
|     changelog     | boolean |  false   |                      <code>true</code>                       |                       Create changelog for release.                       |
| changelog-config  | string  |  false   |                                                   |                          Changelog config path.                           |
|  poetry-version   | string  |  false   |                     <code>"1.5.1"</code>                     |          The Poetry version to be installed. (Default is 1.5.1)           |
|  python-version   | string  |  false   |                     <code>"3.10"</code>                      |        The Python version for setting up Poetry. (Default is 3.10)        |
|        ref        | string  |  false   | <code>"${{ github.event.repository.default_branch }}"</code> |                 The ref name to checkout the repository.                  |
|   release-type    | string  |   true   |                                                   |  Scope of the release; See: https://python-poetry.org/docs/cli/#version   |
| working-directory | string  |  false   |                      <code>"./"</code>                       | The working directory of your Python package. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                         VALUE                          |            DESCRIPTION             |
|-----------------|--------------------------------------------------------|------------------------------------|
|   old-version   |   <code>"${{ jobs.create-release.outputs.old-version }}"</code>   |  The old version of the package.   |
| release-version | <code>"${{ jobs.create-release.outputs.release-version }}"</code> | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                   DESCRIPTION                   |
|-----------------|----------|-------------------------------------------------|
|  github-email   |   true   |  The GitHub email for committing the changes.   |
|  github-token   |   true   |  The GitHub token for committing the changes.   |
| github-username |   true   | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
