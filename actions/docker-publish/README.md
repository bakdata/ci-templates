# docker-publish

This action downloads an `image.tar` file from a pipeline artifact and publishes it on Dockerhub.

## Prerequisites

Create an action that uploads an `image.tar` file as pipeline artifact (see <https://github.com/actions/upload-artifact>).

## Input Parameters

| Name                | Required |        Default Value         |  Type  | Description                                                                                                                     |
|---------------------|:--------:|:----------------------------:|:------:|---------------------------------------------------------------------------------------------------------------------------------|
| image-name          |    ✅     | github.event.repository.name | string | Name of Docker image on Dockerhub                                                                                               |
| image-artifact-name |    ✅     |       "image-artifact"       | string | Name of the pipeline artifact that contains the Docker image.tar file to push, see <https://github.com/actions/upload-artifact> |
| username            |    ✅     |              -               | string | Username for the Docker registry login                                                                                          |
| password            |    ✅     |              -               | string | Password for the Docker registry login                                                                                          |
| publisher           |    ❌     |              -               | string | Publisher to prefix Docker image (e.g. 'my-publisher')                                                                          |
| working-directory   |    ❌     |             "./"             | string | Working directory for your docker artifacts                                                                                     |

## Usage

```yaml
...
steps:
  - name: Publish Jib image
    uses: bakdata/ci-templates/actions/docker-publish@main
    with:
      image-artifact-name: "image-artifact"
      image-name: "my-image" # published image name will be 'my-image'
      publisher: "my-publisher" # (Optional) published image will called be 'my-publisher/my-image'      
      username: ${{ secrets.docker-user }}
      password: ${{ secrets.docker-password }}
      working-directory: "./" # (Optional)
...
```
