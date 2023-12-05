# Refenrences docker-build composite action
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |                 DEFAULT                 |                                                                     DESCRIPTION                                                                     |
|---------------------|--------|----------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|   docker-context    | string |  false   |                  `"."`                  |                                                                 The docker context.                                                                 |
|   dockerfile-path   | string |  false   |             `"Dockerfile"`              |                                                               Path to the Dockerfile.                                                               |
| image-artifact-name | string |  false   |           `"image-artifact"`            | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact'). |
|     image-name      | string |  false   | `"${{ github.event.repository.name }}"` |                                                                Name of Docker image.                                                                |
|   retention-days    | string |  false   |                  `"1"`                  |                                            Number of days the image artifact should be stored on GitHub.                                            |
|  working-directory  | string |  false   |                  `"."`                  |                                                    Working directory for your Docker artifacts.                                                     |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
