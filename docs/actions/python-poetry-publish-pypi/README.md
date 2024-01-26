# Description python-poetry-publish-pypi composite action

This composite action uses Poetry to build and publish your Python packages either on TestPyPI or PyPI.

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

    # Other steps in your workflow

  - name: Publish to (Test)PyPI
    uses: bakdata/ci-templates/actions/python-poetry-publish-pypi@main
    with:
      pypi-token: ${{ secrets.pypi-token }}
      publish-to-test: ${{ inputs.publish-to-test }}
      working-directory: ${{ inputs.working-directory }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT  | DESCRIPTION                                                                |
| ----------------- | ------ | -------- | -------- | -------------------------------------------------------------------------- |
| publish-to-test   | string | false    | `"true"` | If set to false, the packages are published to PyPI. (Default is true)     |
| pypi-token        | string | true     |          | The PyPI token for publishing packages.                                    |
| working-directory | string | false    | `"./"`   | The working directory of your Python packages. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
