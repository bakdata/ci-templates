# docker-build

This action uses a Dockerfile to build an `image.tar` file and upload it to GitHub artifacts.

## Prerequisites

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

## Input Parameters

| Name                | Required |        Default Value         |                                                                             Description                                                                              |
| ------------------- | :------: | :--------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| dockerfile-context  |    ❌    |             "."              |                                                                         The docker context.                                                                          |
| dockerfile-path     |    ❌    |         "Dockerfile"         |                                                                       Path to the Dockerfile.                                                                        |
| github-token        |    ❌    |         github.token         | Github token to use for checkout(important when this action should be automatically triggerd by another action: https://github.com/orgs/community/discussions/27028) |
| image-artifact-name |    ❌    |       "image-artifact"       |         Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact').          |
| image-name          |    ❌    | github.event.repository.name |                                                                  Name of Docker image on Dockerhub                                                                   |
| ref                 |    ❌    |       github.ref_name        |                                                                   Branch to use for the checkout.                                                                    |

## Usage

```yaml
steps:
  - name: Build tarball image
    uses: bakdata/ci-templates/actions/docker-build@main
    with:
      dockerfile-context: "./docker-dir/"
      dockerfile-path: "docker-dir/Dockerfile"
      image-artifact-name: "${{ inputs.image-artifact-name }}"
      image-name: "tarball"
      github-token: "${{ secrets.GITHUB_TOKEN }}"
```
