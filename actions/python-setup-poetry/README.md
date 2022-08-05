# python-setup-poetry

This composite action sets up poetry. First, it installs Python for the given version and then Poetry for the given input
version.

## Input Parameters

| Name              | Required | Default Value | Description                               |
|-------------------|:--------:|:-------------:|-------------------------------------------|
| python-version    |    ❌     |     3.10      | The python version for setting up poetry. |
| poetry-version    |    ❌     |    1.1.12     | The poetry version to be installed.       |
| working-directory |    ❌     |       .       | The root directory of the poetry project. |

## Usage

```yaml
  steps:

    # Other Steps in your workflow

    - name: Set up Poetry version ${{ inputs.poetry-version }}
      uses: bakdata/ci-templates/actions/python-setup-poetry@main
      with:
        python-version: ${{ inputs.python-version }}
        poetry-version: ${{ inputs.poetry-version }}
        working-directory: ${{ inputs.working-directory }}

    # Rest of your workflow
```
