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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT   | DESCRIPTION                                                                                                            |
| ----------------- | ------ | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| poetry-version    | string | false    | `"1.2.2"` | The Poetry version to be installed.                                                                                    |
| python-version    | string | false    | `"3.10"`  | The Python version for the Poetry virtual environment.                                                                 |
| release-type      | string | true     |           | Scope of the release: patch, minor, major, or snapshot. See https://python-poetry.org/docs/cli/#version for reference. |
| working-directory | string | false    | `"."`     | The root directory of the Poetry project.                                                                              |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                         |
| --------------- | ------ | ----------------------------------- |
| old-version     | string | The old version of your package.    |
| release-version | string | The bumped version of your package. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
