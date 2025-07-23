# Description of docker-build-and-publish reusable Workflow

This workflow will use a Dockerfile to build and push images to any container registry.

## Prerequisites

This workflow requires a Dockerfile located in the repository.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [docker-build](https://github.com/bakdata/ci-templates/tree/main/actions/docker-build)
- [docker-publish](https://github.com/bakdata/ci-templates/tree/main/actions/docker-publish)

## Calling the workflow

```yaml
name: Docker build and publish

on:
  workflow_dispatch:

jobs:
  call-workflow-passing-data:
    name: Build and push Docker image
    uses: bakdata/ci-templates/.github/workflows/docker-build-and-publish.yaml@main
    with:
      # with these settings image would be pushed to my-registry.com/my-namespace/my-image:my-tag
      docker-context: "./docker-dir/"
      dockerfile-path: "./path/to/my/Dockerfile"
      docker-registry: "my-registry.com"
      image-namespace: "my-namespace"
      image-name: "my-image"
      image-tag: "my-tag"
      ref: "feat/foo"
      retention-days: 2
      image-artifact-name: "my-image-artifact"
      working-directory: "."
    secrets:
      docker-user: "${{ secrets.DOCKER_USER }}"
      docker-password: "${{ secrets.DOCKER_PWD }}"
      github-token: ${{ secrets.GH_TOKEN }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE    | REQUIRED | DEFAULT                                         | DESCRIPTION                                                                                                                              |
| ------------------- | ------- | -------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| checkout-lfs-files  | boolean | false    | `false`                                         | Whether the Git checkout action should resolve LFS files or not. (Default is false)                                                      |
| checkout-submodules | string  | false    | `"false"`                                       | Whether to checkout submodules: `true` to checkout submodules or `recursive` to recursively checkout submodules.                         |
| docker-build-args   | string  | false    |                                                 | List of build-time variables (see https://github.com/docker/build-push-action?tab=readme-ov-file#inputs)                                 |
| docker-context      | string  | false    | `"."`                                           | The docker context.                                                                                                                      |
| docker-registry     | string  | false    | `"docker.io"`                                   | Host where the image should be pushed to.                                                                                                |
| dockerfile-path     | string  | false    | `"./Dockerfile"`                                | Path to the Dockerfile.                                                                                                                  |
| image-name          | string  | false    | `"${{ github.event.repository.name }}"`         | Name of Docker image.                                                                                                                    |
| image-namespace     | string  | false    | `"bakdata"`                                     | Namespace of Docker image.                                                                                                               |
| image-tag           | string  | false    | `"pipeline-${{ github.run_id }}-git-{{ sha }}"` | Tag of Docker image.                                                                                                                     |
| image-tag-flavor    | string  | false    |                                                 | Flavor of Docker image tags. See [docs of metadata-action](https://github.com/docker/metadata-action/blob/v5.6.1/README.md#flavor-input) |
| ref                 | string  | false    |                                                 | Ref name to checkout                                                                                                                     |

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

<!-- AUTO-DOC-SECRETS:END -->
