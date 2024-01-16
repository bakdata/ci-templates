<h1>Description of docker-build-and-publish reusable Workflow</h1>

This workflow will use a Dockerfile to build and push images to any container registry.

<h2>Prerequisites</h2>

This workflow requires a Dockerfile located in the repository.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/docker-build">docker-build</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/docker-publish">docker-publish</a>
</ul>

<h2>Calling the workflow</h2>

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

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |                        DEFAULT                         |                                                      DESCRIPTION                                                      |
|---------------------|--------|----------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|   docker-context    | string |  false   |                         <code>"."</code>                          |                                                  The docker context.                                                  |
|   docker-registry   | string |  false   |                                                        |                                       Host where the image should be pushed to.                                       |
|   dockerfile-path   | string |  false   |                     <code>"Dockerfile"</code>                     |                                                Path to the Dockerfile.                                                |
| image-artifact-name | string |  false   |                   <code>"image-artifact"</code>                   | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact. |
|     image-name      | string |  false   |        <code>"${{ github.event.repository.name }}"</code>         |                                                 Name of Docker image.                                                 |
|   image-namespace   | string |  false   |                                                        |                                              Namespace of Docker image.                                               |
|      image-tag      | string |  false   | <code>"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"</code> |                                                 Tag of Docker image.                                                  |
|         ref         | string |  false   |                                                        |                                                 Ref name to checkout                                                  |
|   retention-days    | number |  false   |                          <code>1</code>                           |                             Number of days the image artifact should be stored on GitHub.                             |
|  working-directory  | string |  false   |                         <code>"."</code>                          |                              Working directory for your Docker artifacts. (Default is .)                              |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |               DESCRIPTION               |
|-----------------|----------|-----------------------------------------|
| docker-password |   true   | Password for the Docker registry login. |
|   docker-user   |   true   | Username for the Docker registry login. |
|  github-token   |  false   |              GitHub token.              |

<!-- AUTO-DOC-SECRETS:END -->
