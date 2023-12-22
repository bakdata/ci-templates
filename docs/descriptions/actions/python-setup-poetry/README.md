# Description python-setup-poetry composite action

This composite action sets up Poetry for the given input version. It supports caching the Python virtualenv between workflow runs.

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
