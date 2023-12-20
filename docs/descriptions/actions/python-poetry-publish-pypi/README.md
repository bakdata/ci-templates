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
