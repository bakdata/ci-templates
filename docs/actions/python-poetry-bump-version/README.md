# Description python-poetry-bump-version composite action

This composite action bumps the Python package version depending on the release type. The [`poetry version`](https://python-poetry.org/docs/cli/#version) command is used to bump the version and change it in the `pyproject.toml` file. It will output the old and new bumped versions.

## Dependencies

- [bakdata/ci-templates/actions/python-setup-poetry@v1.5.3](https://github.com/bakdata/ci-templates/blob/v1.5.3/actions/python-setup-poetry)

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
