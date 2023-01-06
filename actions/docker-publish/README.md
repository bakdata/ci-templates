# docker-publish

This action uses a Dockerfile to publish an image to a Registry of your choice. The action requires you to specify a Tag. The image has then both the given and a `latest` Tags.

## Prerequisites

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

## Input Parameters

| Name                | Required |        Default Value         |  Type  | Description                                                                                                                                         |
| ------------------- | :------: | :--------------------------: | :----: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| docker-registry     |    ✅    |              -               | string | Host where the image should be pushed to.                                                                                                           |
| github-token        |    ✅    |              -               | string | Github token to use for checkout.                                                                                                                   |
| password            |    ✅    |              -               | string | Password for the Docker registry login                                                                                                              |
| publisher           |    ✅    |              -               | string | Publisher to prefix Docker image (e.g. 'my-publisher')                                                                                              |
| username            |    ✅    |              -               | string | Username for the Docker registry login                                                                                                              |
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
