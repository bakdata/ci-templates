# Description python-poetry-publish composite action

This composite action uses Poetry to build and publish your Python packages to a package index.

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

    # Other steps in your workflow

  - name: Publish to package index
    uses: bakdata/ci-templates/actions/python-poetry-publish@main
    with:
      index-name: index
      index-url: example.org/simple/
      index-username: user123
      index-password: supersecret
      working-directory: ${{ inputs.working-directory }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                  | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                                                |
| ---------------------- | ------ | -------- | ------- | -------------------------------------------------------------------------- |
| index-name             | string | true     |         | The package index name for publishing packages.                            |
| index-password         | string | true     |         | The package index password for publishing packages.                        |
| index-url              | string | true     |         | The package index url for publishing packages.                             |
| index-username         | string | true     |         | The package index username for publishing packages.                        |
| peotry-request-timeout | string | false    | `"120"` | Poetry's HTTP request timeout in seconds. (Default is 120 seconds)         |
| working-directory      | string | false    | `"./"`  | The working directory of your Python packages. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
