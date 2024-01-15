<h1>Description of python-poetry-publish-pypi reusable Workflow</h1>

This workflow will publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

<h2>Prerequisites</h2>

Your Python project needs to be set up with Poetry and contain a <code>pyproject.toml</code> file to use this workflow.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry">python-setup-poetry</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-publish-pypi">python-poetry-publish-pypi</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Publish

on:
  push:
    tags:
      - "*"

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/python-poetry-publish-pypi.yaml@main
    with:
      publish-to-test: false # (Optional) By default the packages are published to TestPyPI. In this case the packages are published to PyPI
      python-version: 3.8 # (Optional) Default value is 3.10. In this case Poetry is installed with Python 3.8
      poetry-version: "1.1.11" # (Optional) Default value is 1.5.1. In this case Poetry version 1.1.11 is installed
      working-directory: "./my-awesome-python-project" # (Optional) Default value is the root directory of your repository. In this case all the files to the given path are published
    secrets:
      pypi-token: ${{ secrets.PYPI_TOKEN }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED |  DEFAULT  |                                DESCRIPTION                                 |
|-------------------|---------|----------|-----------|----------------------------------------------------------------------------|
|  poetry-version   | string  |  false   | <code>"1.5.1"</code> |           The Poetry version to be installed. (Default is 1.5.1)           |
|  publish-to-test  | boolean |  false   |  <code>true</code>   |   If set to false, the packages are published to PyPI. (Default is true)   |
|  python-version   | string  |  false   | <code>"3.10"</code>  |  The Python version for the Poetry virtual environment. (Default is 3.10)  |
| working-directory | string  |  false   |  <code>"./"</code>   | The working directory of your Python packages. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|   SECRET   | REQUIRED | DESCRIPTION |
|------------|----------|-------------|
| pypi-token |   true   | PyPI token  |

<!-- AUTO-DOC-SECRETS:END -->
