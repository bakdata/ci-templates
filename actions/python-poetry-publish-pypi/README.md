# python-poetry-publish-pypi

This composite action uses Poetry to build and publish your Python packages either on TestPyPI or PyPI.

## Input Parameters

| Name              | Required | Default Value | Description                                                                                          |
| ----------------- | :------: | :-----------: | ---------------------------------------------------------------------------------------------------- |
| pypi-token        |    ✅    |       -       | The (Test)PyPI API token for publishing packages                                                     |
| publish-to-test   |    ❌    |     true      | If set to true, the packages are published to TestPyPI other wise the packages are published to PyPI |
| working-directory |    ❌    |     "./"      | The working directory of your Python package.                                                        |

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
