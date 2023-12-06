# Refenrences docker-push composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT                                                | DESCRIPTION                                  |
| ----------------- | ------ | -------- | ------------------------------------------------------ | -------------------------------------------- |
| docker-registry4   | string | false    |                                                        | Host where the image should be pushed to.    |
| image-name        | string | false    | `"${{ github.event.repository.name }}"`                | Name of Docker image.                        |
| image-namespace   | string | false    |                                                        | Namespace of Docker image.                   |
| image-tag         | string | false    | `"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"` | Tag of Docker image.                         |
| working-directory | string | false    | `"."`                                                  | Working directory for your Docker artifacts. |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
