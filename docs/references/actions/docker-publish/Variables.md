# Refenrences docker-publish composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                                                | DESCRIPTION                                                                                                           |
| ------------------- | ------ | -------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
e    | `"image-artifact"`                                     | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact. |
| image-name          | string | false    | `"${{ github.event.repository.name }}"`                | Name of Docker image.                                                                                                 |
| image-namespace     | string | false    |                                                        | Namespace of Docker image.                                                                                            |
| image-tag           | string | false    | `"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"` | Tag of Docker image.                                                                                                  |
| working-directory   | string | false    | `"."`                                                  | Working directory for your Docker artifacts.                                                                          |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
