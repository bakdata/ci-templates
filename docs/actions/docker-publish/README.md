# Description docker-publish composite action

This action downloads an `image.tar` file from an artifact and publishes it into a Docker registry. When this action is used on a tag branch, the image is tagged with `latest` and the tag version of the branch (e.g. `1.2.3`). For all other branches, the tag `pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}` is used as an image tag.

## Prerequisites

Create an action that [uploads a tarball image as an artifact](https://github.com/actions/upload-artifact). A [Gradle Jib](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) example can be found [here](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib).

## Usage

```yaml
steps:
  - name: Publish tarball image
    uses: bakdata/ci-templates/actions/docker-publish@main
    with:
      # publishing image registry.hub.docker.com/my-namespace/my-image:v1.1.0
      docker-registry: "registry.hub.docker.com"
      image-namespace: "my-namespace"
      image-name: "my-image"
      image-tag: "v1.1.0"
      image-artifact-name: "tarball"
      working-directory: "./tarball"
```

## Dependencies

- [actions/download-artifact@v3](https://github.com/actions/download-artifact/tree/v3)
- [docker/setup-buildx-action@v2.2.1](https://github.com/docker/setup-buildx-action/tree/v2.2.1)
- [bakdata/ci-templates/actions/docker-push@1.30.0](https://github.com/bakdata/ci-templates/blob/1.30.0/actions/docker-push)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                                                | DESCRIPTION                                                                                                           |
| ------------------- | ------ | -------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| docker-registry     | string | false    |                                                        | Host where the image should be pushed to.                                                                             |
| image-artifact-name | string | false    | `"image-artifact"`                                     | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact. |
| image-name          | string | false    | `"${{ github.event.repository.name }}"`                | Name of Docker image.                                                                                                 |
| image-namespace     | string | false    |                                                        | Namespace of Docker image.                                                                                            |
| image-tag           | string | false    | `"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"` | Tag of Docker image.                                                                                                  |
| working-directory   | string | false    | `"."`                                                  | Working directory for your Docker artifacts.                                                                          |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
