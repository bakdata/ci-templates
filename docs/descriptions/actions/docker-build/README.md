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
