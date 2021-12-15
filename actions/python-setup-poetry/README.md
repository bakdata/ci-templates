# python-setup-poetry

This composite action setups poetry. First, it installs Python for the given version and then Poetry for the given input
version.

## Input Parameters

| Name           | Required | Default Value | Description                               |
|----------------|:--------:|:-------------:|-------------------------------------------|
| python-version |    ❌     |      3.7      | The python version for setting up poetry. |
| poetry-version |    ❌     |    1.1.12     | The poetry version to be installed.       |

## Usage

```yaml
  steps:

    # Other Steps in your workflow

    - name: Set up Poetry version ${{ inputs.poetry-version }}
      uses: ./ci-templates/actions/python-setup-poetry
      with:
        python-version: ${{ inputs.python-version }}
        poetry-version: ${{ inputs.poetry-version }}

    # Rest of your workflow
```