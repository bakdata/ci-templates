# docker-publish

This action downloads an `image.tar` file from an artifact and publishes it on Dockerhub. When this action is used on a tag branch, the image is tagged with latest and the tag version of the branch (e.g. 1.2.3). For all other branches the github.run_id is used as an image tag.

## Prerequisites

Create an action that [uploads a tarball image as artifact](https://github.com/actions/upload-artifact). A [Gradle Jib](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) example can be found [here](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib).

## Input Parameters

| Name                | Required |        Default Value         |  Type  | Description                                                                                                                                         |
| ------------------- | :------: | :--------------------------: | :----: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| password            |    ✅    |              -               | string | Password for the Docker registry login                                                                                                              |
| publisher           |    ✅    |              -               | string | Publisher to prefix Docker image (e.g. 'my-publisher')                                                                                              |
| username            |    ✅    |              -               | string | Username for the Docker registry login                                                                                                              |
| docker-registry     |    ❌    |       "hub.docker.com"       | string | Host where the image should be pushed to.                                                                                                           |
| image-artifact-name |    ❌    |       "image-artifact"       | string | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact'). |
| image-name          |    ❌    | github.event.repository.name | string | Name of Docker image on Dockerhub                                                                                                                   |
| ref                 |    ❌    |       github.ref_name        | string | Branch to use for the checkout.                                                                                                                     |
| working-directory   |    ❌    |              -               | string | Working directory for your Docker artifacts                                                                                                         |

## Usage

```yaml
steps:
  - name: Publish tarball image
    uses: bakdata/ci-templates/actions/docker-publish@main
    with:
      image-tag: "v.1.0"
      image-name: "tarball"
      publisher: "my-publisher"
      username: "${{ secrets.docker-user }}"
      password: "${{ secrets.docker-password }}"
      working-directory: "./tarball"
      docker-registry: "hub.docker.com"
      github-token: "${{ secrets.GITHUB_TOKEN }}"
      ref: "master" # (Optional)
```
