# python-poetry-bump-version

This composite action bumps the python package version depending on the release type. The [poetry version](https://python-poetry.org/docs/cli/#version) command is used to bump the version and change it
in the `pyproject.toml` file. It will output the old and new bumped versions.

## Dependencies

This action uses another composite action listed below:

- [python-setup-poetry](https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry)

## Input Parameters

| Name              | Required | Default Value |                   Type                    | Description                                                                                                                       |
| ----------------- | :------: | :-----------: | :---------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------- |
| release-type      |    ✅     |       -       |                  string                   | Scope of the release, see the official [documentation of poetry](https://python-poetry.org/docs/cli/#version) for possible values |
| python-version    |    ❌     |     3.10      |                  number                   | The python version for setting up poetry.                                                                                         |
| poetry-version    |    ❌     |    1.1.14     |                  number                   | The poetry version to be installed.                                                                                               |
| working-directory |    ❌     |       .       | The root directory of the poetry project. |                                                                                                                                   |

## Output Parameters

| Name        | Description                                         |
| ----------- | --------------------------------------------------- |
| old-tag     | Defines the old version in your pyproject.toml file |
| release-tag | The bumped version of your project                  |

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
    run: echo Bumped Version from ${{ steps.bump-version.outputs.old-tag }} to ${{ steps.bump-version.outputs.release-tag }}
```
