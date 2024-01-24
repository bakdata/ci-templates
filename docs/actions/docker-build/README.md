# Description docker-build composite action

This action uses a Dockerfile to build an `image.tar` file and upload it to GitHub artifacts.

## Prerequisites

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

## Usage

```yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/docker-build@main
    with:
      docker-context: "./docker-dir/"
      dockerfile-path: "./path/to/my/Dockerfile"
      image-artifact-name: "my-image-artifact"
      image-name: "my-image"
      retention-days: 2
      working-directory: "./tarball"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                                 | DESCRIPTION                                                                                                                                         |
| ------------------- | ------ | -------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| docker-context      | string | false    | `"."`                                   | The docker context.                                                                                                                                 |
| dockerfile-path     | string | false    | `"Dockerfile"`                          | Path to the Dockerfile.                                                                                                                             |
| image-artifact-name | string | false    | `"image-artifact"`                      | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact'). |
| image-name          | string | false    | `"${{ github.event.repository.name }}"` | Name of Docker image.                                                                                                                               |
| retention-days      | string | false    | `"1"`                                   | Number of days the image artifact should be stored on GitHub.                                                                                       |
| working-directory   | string | false    | `"."`                                   | Working directory for your Docker artifacts.                                                                                                        |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
