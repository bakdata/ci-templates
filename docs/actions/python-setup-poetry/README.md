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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT   | DESCRIPTION                                                  |
| ----------------- | ------ | -------- | --------- | ------------------------------------------------------------ |
| install-pipx      | string | false    | `"false"` | Whether to ensure that pipx is installed before invoking it. |
| poetry-version    | string | false    | `"1.2.2"` | The Poetry version to be installed.                          |
| python-version    | string | false    | `"3.10"`  | The Python version for the Poetry virtual environment.       |
| working-directory | string | false    | `"."`     | The root directory of the Poetry project.                    |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
