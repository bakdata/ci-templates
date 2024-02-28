# Description of python-poetry-publish-pypi reusable Workflow

This workflow will publish the built project to either TestPyPI or PyPI. In
the following, you will first find the necessary prerequisite to set up the workflow. Next, you will find the
documentation of the input, secret, and output parameters. In the end, you find a small example of how to use this
workflow.

## Prerequisites

Your Python project needs to be set up with Poetry and contain a `pyproject.toml` file to use this workflow.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

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

| SECRET     | REQUIRED | DESCRIPTION |
| ---------- | -------- | ----------- |
| pypi-token | true     | PyPI token  |

<!-- AUTO-DOC-SECRETS:END -->
