# Description python-poetry-bump-version composite action

This composite action bumps the Python package version depending on the release type. The [`poetry version`](https://python-poetry.org/docs/cli/#version) command is used to bump the version and change it in the `pyproject.toml` file. It will output the old and new bumped versions.

## Dependencies

This action uses another composite action listed below:

- [python-setup-poetry](https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry)

## Usage

```yaml
steps:
  # Other steps in your workflow
  - name: Bump version
    id: bump-version
    uses: bakdata/ci-templates/actions/python-poetry-bump-version@main
    with:
      release-type: ${{ inputs.release-type }}
      python-version: ${{ inputs.python-version }}
      poetry-version: ${{ inputs.poetry-version }}

  - name: Use bump version output
    run: echo Bumped version from ${{ steps.bump-version.outputs.old-version }} to ${{ steps.bump-version.outputs.release-version }}
```
