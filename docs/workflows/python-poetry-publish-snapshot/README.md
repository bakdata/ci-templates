<h1>Description of python-poetry-publish-snapshot reusable Workflow</h1>

This workflow will publish a dev snapshot of the package to TestPyPI using Poetry.

<h2>Prerequisites</h2>

Your Python project needs to be set up with Poetry and contain a <code>pyproject.toml</code> file to use this workflow.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version">python-poetry-bump-version</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-publish-pypi">python-poetry-publish-pypi</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Publish snapshot

on:
  push:

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/python-poetry-publish-snapshot.yaml@main
    with:
      python-version: 3.8 # (Optional) Default value is 3.10. In this case Poetry is installed with Python 3.8
      poetry-version: "1.1.11" # (Optional) Default value is 1.5.1. In this case Poetry version 1.1.11 is installed
      working-directory: "./my-awesome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
    secrets:
      pypi-token: ${{ secrets.TEST_PYPI_TOKEN }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                                DESCRIPTION                                |
|-------------------|--------|----------|-----------|---------------------------------------------------------------------------|
|  poetry-version   | string |  false   | <code>"1.5.1"</code> |          The Poetry version to be installed. (Default is 1.5.1)           |
|  python-version   | string |  false   | <code>"3.10"</code>  |        The Python version for setting up Poetry. (Default is 3.10)        |
| working-directory | string |  false   |  <code>"./"</code>   | The working directory of your Python package. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                          VALUE                           |            DESCRIPTION             |
|-----------------|----------------------------------------------------------|------------------------------------|
|   old-version   |   <code>"${{ jobs.publish-snapshot.outputs.old-version }}"</code>   |  The old version of the package.   |
| release-version | <code>"${{ jobs.publish-snapshot.outputs.release-version }}"</code> | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|   SECRET   | REQUIRED |  DESCRIPTION   |
|------------|----------|----------------|
| pypi-token |   true   | TestPyPI token |

<!-- AUTO-DOC-SECRETS:END -->
