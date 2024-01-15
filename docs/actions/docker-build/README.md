<h1>Description docker-build composite action</h1>

This action uses a Dockerfile to build an <code>image.tar</code> file and upload it to GitHub artifacts.

<h2>Prerequisites</h2>

Ensure that your Dockerfile is uploaded to the repository you want to use this action from.

<h2>Usage</h2>

<code>yaml
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
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |                 DEFAULT                 |                                                                     DESCRIPTION                                                                     |
|---------------------|--------|----------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|   docker-context    | string |  false   |                  <code>"."</code>                  |                                                                 The docker context.                                                                 |
|   dockerfile-path   | string |  false   |             <code>"Dockerfile"</code>              |                                                               Path to the Dockerfile.                                                               |
| image-artifact-name | string |  false   |           <code>"image-artifact"</code>            | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact (Default is 'image-artifact'). |
|     image-name      | string |  false   | <code>"${{ github.event.repository.name }}"</code> |                                                                Name of Docker image.                                                                |
|   retention-days    | string |  false   |                  <code>"1"</code>                  |                                            Number of days the image artifact should be stored on GitHub.                                            |
|  working-directory  | string |  false   |                  <code>"."</code>                  |                                                    Working directory for your Docker artifacts.                                                     |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
