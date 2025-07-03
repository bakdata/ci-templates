# Description of python-poetry-publish-pypi reusable Workflow

This workflow will publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

## Prerequisites

Your Python project needs to be set up with Poetry and contain a `pyproject.toml` file to use this workflow.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [python-setup-poetry](https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry)
- [python-poetry-publish-pypi](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-publish-pypi)

## Calling the workflow

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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT   | DESCRIPTION                                                                |
| ----------------- | ------- | -------- | --------- | -------------------------------------------------------------------------- |
| poetry-version    | string  | false    | `"1.5.1"` | The Poetry version to be installed. (Default is 1.5.1)                     |
| publish-to-test   | boolean | false    | `true`    | If set to false, the packages are published to PyPI. (Default is true)     |
| python-version    | string  | false    | `"3.10"`  | The Python version for the Poetry virtual environment. (Default is 3.10)   |
| working-directory | string  | false    | `"./"`    | The working directory of your Python packages. (Default is root directory) |

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
