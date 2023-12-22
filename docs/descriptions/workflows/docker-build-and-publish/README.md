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
