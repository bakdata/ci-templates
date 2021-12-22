# python-poetry-release

This composite action uses poetry to build and push your Python packages either to TestPyPI or PyPI.

## Dependencies

This action uses another composite action listed below:

* [python-setup-poetry](https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry)

## Input Parameters

| Name              | Required | Default Value | Description                                                                                          |
|-------------------|:--------:|:-------------:|------------------------------------------------------------------------------------------------------|
| pypi-token        |    ✅     |       -       | The (test) PyPI api token for publishing packages                                                    |
| publish-to-test   |    ❌     |     true      | If set to true, the packages are published to TestPyPI other wise the packages are published to PyPI |
| python-version    |    ❌     |     3.10      | The python version for setting up poetry.                                                            |
| poetry-version    |    ❌     |    1.1.12     | The poetry version to be installed.                                                                  |
| working-directory |    ❌     |     "./"      | The working directory of your Python package.                                                        |

## Usage

```yaml
steps:
  # Other steps in your workflow

  - name: Release to (Test)PyPI
    uses: bakdata/ci-templates/actions/python-poetry-release@main
    with:
      pypi-token: ${{ secrets.pypi-token }}
      publish-to-test: ${{ inputs.publish-to-test }}
      working-directory: ${{ inputs.working-directory }}
      python-version: ${{ inputs.python-version }}
      poetry-version: ${{ inputs.poetry-version }}
```
