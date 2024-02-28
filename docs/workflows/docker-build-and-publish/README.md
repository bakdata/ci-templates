# Description of docker-build-and-publish reusable Workflow

This workflow will use a Dockerfile to build and push images to any container registry.

## Prerequisites

This workflow requires a Dockerfile located in the repository.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                                                | DESCRIPTION                                                                                                           |
| ------------------- | ------ | -------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| docker-context      | string | false    | `"."`                                                  | The docker context.                                                                                                   |
| docker-registry     | string | false    |                                                        | Host where the image should be pushed to.                                                                             |
| dockerfile-path     | string | false    | `"Dockerfile"`                                         | Path to the Dockerfile.                                                                                               |
| image-artifact-name | string | false    | `"image-artifact"`                                     | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact. |
| image-name          | string | false    | `"${{ github.event.repository.name }}"`                | Name of Docker image.                                                                                                 |
| image-namespace     | string | false    |                                                        | Namespace of Docker image.                                                                                            |
| image-tag           | string | false    | `"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"` | Tag of Docker image.                                                                                                  |
| ref                 | string | false    |                                                        | Ref name to checkout                                                                                                  |
| retention-days      | number | false    | `1`                                                    | Number of days the image artifact should be stored on GitHub.                                                         |
| working-directory   | string | false    | `"."`                                                  | Working directory for your Docker artifacts. (Default is .)                                                           |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                             |
| --------------- | -------- | --------------------------------------- |
| docker-password | true     | Password for the Docker registry login. |
| docker-user     | true     | Username for the Docker registry login. |
| github-token    | false    | GitHub token.                           |

<!-- AUTO-DOC-SECRETS:END -->
