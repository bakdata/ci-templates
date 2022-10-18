# python-setup-poetry

This composite action sets up Poetry for the given input version. It supports caching the Python virtualenv between workflow runs.

## Input Parameters

| Name              | Required | Default Value | Description                               |
| ----------------- | :------: | :-----------: | ----------------------------------------- |
| python-version    |    ❌    |     3.10      | The Python version for setting up Poetry. |
| poetry-version    |    ❌    |     1.2.2     | The Poetry version to be installed.       |
| working-directory |    ❌    |       .       | The root directory of the Poetry project. |

## Usage

```yaml
steps:
  # Other Steps in your workflow

  - name: Set up Poetry ${{ inputs.poetry-version }}
    uses: bakdata/ci-templates/actions/python-setup-poetry@main
    with:
      python-version: ${{ inputs.python-version }}
      poetry-version: ${{ inputs.poetry-version }}
      working-directory: ${{ inputs.working-directory }}

  # Rest of your workflow
```
