# Description of python-poetry-publish-snapshot reusable Workflow

This workflow will publish a dev snapshot of the package to TestPyPI using Poetry.

## Prerequisites

Your Python project needs to be set up with Poetry and contain a `pyproject.toml` file to use this workflow.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [python-poetry-bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-bump-version)
- [python-poetry-publish-pypi](https://github.com/bakdata/ci-templates/tree/main/actions/python-poetry-publish-pypi)

## Calling the workflow

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
