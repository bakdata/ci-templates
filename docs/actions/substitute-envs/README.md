# Description substitute-envs composite action

This action will recursively substitute environment variables in a given directory.

## Usage

```yaml
---
steps:
  - name: Substitute env variables
    id: substitute
    uses: bakdata/ci-templates/actions/substitute-envs@main
    with:
      path: "path/to/directory"

  - name: Use substitute output
    run: echo "${{ steps.substitute.outputs.path }}"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                                  |
| ----- | ------ | -------- | ------- | ------------------------------------------------------------ |
| path  | string | true     |         | Path to the directory to substitute environment variables in |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT | TYPE   | DESCRIPTION                                        |
| ------ | ------ | -------------------------------------------------- |
| path   | string | Path to the temporary directory after substitution |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
