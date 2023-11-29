# Refenrences python-poetry-publish-snapshot reusable Workflow
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                                DESCRIPTION                                |
|-------------------|--------|----------|-----------|---------------------------------------------------------------------------|
|  poetry-version   | string |  false   | `"1.5.1"` |          The Poetry version to be installed. (Default is 1.5.1)           |
|  python-version   | string |  false   | `"3.10"`  |        The Python version for setting up Poetry. (Default is 3.10)        |
| working-directory | string |  false   |  `"./"`   | The working directory of your Python package. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                          VALUE                           |            DESCRIPTION             |
|-----------------|----------------------------------------------------------|------------------------------------|
|   old-version   |   `"${{ jobs.publish-snapshot.outputs.old-version }}"`   |  The old version of the package.   |
| release-version | `"${{ jobs.publish-snapshot.outputs.release-version }}"` | The bumped version of the package. |

<!-- AUTO-DOC-OUTPUT:END -->
## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|   SECRET   | REQUIRED |  DESCRIPTION   |
|------------|----------|----------------|
| pypi-token |   true   | TestPyPI token |

<!-- AUTO-DOC-SECRETS:END -->
