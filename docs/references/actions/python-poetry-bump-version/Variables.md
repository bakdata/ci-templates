# Refenrences python-poetry-bump-version composite action
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                                                      DESCRIPTION                                                       |
|-------------------|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------|
|  poetry-version   | string |  false   | `"1.2.2"` |                                          The Poetry version to be installed.                                           |
|  python-version   | string |  false   | `"3.10"`  |                                 The Python version for the Poetry virtual environment.                                 |
|   release-type    | string |   true   |           | Scope of the release: patch, minor, major, or snapshot. See https://python-poetry.org/docs/cli/#version for reference. |
| working-directory | string |  false   |   `"."`   |                                       The root directory of the Poetry project.                                        |

<!-- AUTO-DOC-INPUT:END -->
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                                                      DESCRIPTION                                                       |
|-------------------|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------|
|  poetry-version   | string |  false   | `"1.2.2"` |                                          The Poetry version to be installed.                                           |
|  python-version   | string |  false   | `"3.10"`  |                                 The Python version for the Poetry virtual environment.                                 |
|   release-type    | string |   true   |           | Scope of the release: patch, minor, major, or snapshot. See https://python-poetry.org/docs/cli/#version for reference. |
| working-directory | string |  false   |   `"."`   |                                       The root directory of the Poetry project.                                        |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |  TYPE  |             DESCRIPTION             |
|-----------------|--------|-------------------------------------|
|   old-version   | string |  The old version of your package.   |
| release-version | string | The bumped version of your package. |

<!-- AUTO-DOC-OUTPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |  TYPE  |             DESCRIPTION             |
|-----------------|--------|-------------------------------------|
|   old-version   | string |  The old version of your package.   |
| release-version | string | The bumped version of your package. |

<!-- AUTO-DOC-OUTPUT:END -->
