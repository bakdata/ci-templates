# docker-publish

This action downloads an `image.tar` file from an artifact and publishes it into a Docker registry. When this action is used on a tag branch, the image is tagged with `latest` and the tag version of the branch (e.g. `1.2.3`). For all other branches, the tag `pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}` is used as an image tag.

## Prerequisites

Create an action that [uploads a tarball image as an artifact](https://github.com/actions/upload-artifact). A [Gradle Jib](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) example can be found [here](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib).

## Input Parameters

| Name                | Required |                   Default Value                    | Description                                                                                                          |
| ------------------- | :------: | :------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------- |
| docker-registry     |    ❌    |                         ""                         | Host where the image should be pushed to                                                                             |
| image-repository    |    ❌    |                         ""                         | Repository of Docker image                                                                                           |
| image-name          |    ❌    |            github.event.repository.name            | Name of Docker image                                                                                                 |
| image-tag           |    ❌    | pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8} | Tag of Docker image                                                                                                  |
| image-artifact-name |    ❌    |                  "image-artifact"                  | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact |
| working-directory   |    ❌    |                        "."                         | Working directory for your Docker artifacts                                                                          |

## Usage

```yaml
steps:
  - name: Publish tarball image
    uses: bakdata/ci-templates/actions/docker-publish@main
    with:
      # publishing image registry.hub.docker.com/my-repo/my-image:v1.1.0
      docker-registry: "registry.hub.docker.com"
      image-repository: "my-repo"
      image-name: "my-image"
      image-tag: "v1.1.0"
      image-artifact-name: "tarball"
      working-directory: "./tarball"
```
