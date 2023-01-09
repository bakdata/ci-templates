# docker-build

This action uses a Dockerfile to build an `image.tar` file and upload it to GitHub artifacts.

## Prerequisites

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

## Input Parameters

| Name                | Required |        Default Value         |  Type  | Description                                                                                                                                           |
| ------------------- | :------: | :--------------------------: | :----: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| dockerfile-path     |    ✅    |              -               | string | Path to the Dockerfile.                                                                                                                               |
| github-token        |    ✅    |              -               | string | Github token to use for checkout.                                                                                                                     |
| image-artifact-name |    ❌    |              -               | string | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact'). |
| image-name          |    ❌    | github.event.repository.name | string | Name of Docker image on Dockerhub                                                                                                                     |
| ref                 |    ❌    |       github.ref_name        | string | Branch to use for the checkout.                                                                                                                       |

## Usage

```yaml
steps:
  - name: Build tarball image
    uses: bakdata/ci-templates/actions/docker-build@main
    with:
      image-artifact-name: "${{ inputs.image-artifact-name }}"
      dockerfile-path: "./docker-dir"
      image-name: "tarball"
      github-token: "${{ secrets.GITHUB_TOKEN }}"
```
