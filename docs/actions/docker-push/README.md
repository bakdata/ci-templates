# Description docker-push composite action

This action publishes a Docker image to a Docker registry. When this action is used on a tag branch, the image is tagged with `latest` and the tag version of the branch (e.g. `1.2.3`). For all other branches, the tag `pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}` is used as an image tag.

## Prerequisites

Have a Docker image with name `${{ image-name }}` available in the Docker context.

## Usage

```yaml
steps:
  - name: Push Docker image
    uses: bakdata/ci-templates/actions/docker-push@main
    with:
      # publishing image registry.hub.docker.com/my-namespace/my-image:v1.1.0
      docker-registry: "registry.hub.docker.com"
      image-namespace: "my-namespace"
      image-name: "my-image"
      image-tag: "v1.1.0"
      working-directory: "./tarball"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT                                                | DESCRIPTION                                  |
| ----------------- | ------ | -------- | ------------------------------------------------------ | -------------------------------------------- |
| docker-registry   | string | false    |                                                        | Host where the image should be pushed to.    |
| image-name        | string | false    | `"${{ github.event.repository.name }}"`                | Name of Docker image.                        |
| image-namespace   | string | false    |                                                        | Namespace of Docker image.                   |
| image-tag         | string | false    | `"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"` | Tag of Docker image.                         |
| working-directory | string | false    | `"."`                                                  | Working directory for your Docker artifacts. |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
