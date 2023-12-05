# Refenrences bump-version composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                           |
| ----------------- | ------ | -------- | ------- | ----------------------------------------------------- |
| new-version       | string | false    |         |                                                       |
| release-type      | string | true     |         | The type of the release (major, minor or patch).      |
| working-directory | string | false    | `"."`   | The directory containing the `.bumpversion.cfg` file. |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                                      |
| --------------- | ------ | ------------------------------------------------ |
| old-version     | string | The old version in your `.bumpversion.cfg` file. |
| release-version | string | The bumped version of your project.                 |

<!-- AUTO-DOC-OUTPUT:END -->
