# docker-build

This action uses a Dockerfile to build an `image.tar` file and upload it to GitHub artifacts.

## Prerequisites

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

## Input Parameters

| Name                | Required |        Default Value         | Description                                                                                                          |
| ------------------- | :------: | :--------------------------: | -------------------------------------------------------------------------------------------------------------------- |
| docker-context      |    ❌    |             "."              | The docker context.                                                                                                  |
| dockerfile-path     |    ❌    |         "Dockerfile"         | Path to the Dockerfile.                                                                                              |
| image-name          |    ❌    | github.event.repository.name | Name of Docker image on Dockerhub                                                                                    |
| image-artifact-name |    ❌    |       "image-artifact"       | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact |
| retention-days      |    ❌    |             "1"              | Number of days the image artifact should be stored on GitHub                                                         |
| working-directory   |    ❌    |             "."              | Working directory for your Docker artifacts                                                                          |

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
      retention-days: "2"
      working-directory: "./tarball"
```
