# Refenrences python-poetry-publish composite action

## Inputs

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

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
