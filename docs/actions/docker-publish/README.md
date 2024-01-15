<h1>Description docker-publish composite action</h1>

This action downloads an <code>image.tar</code> file from an artifact and publishes it into a Docker registry. When this action is used on a tag branch, the image is tagged with <code>latest</code> and the tag version of the branch (e.g. <code>1.2.3</code>). For all other branches, the tag <code>pipeline-${{ github.run<em>id }}-git-${GITHUB</em>SHA::8}</code> is used as an image tag.

<h2>Prerequisites</h2>

Create an action that <a href="https://github.com/actions/upload-artifact">uploads a tarball image as an artifact</a>. A <a href="https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin">Gradle Jib</a> example can be found <a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib">here</a>.

<h2>Usage</h2>

<code>yaml
steps:

<ul>
<li>name: Publish tarball image
uses: bakdata/ci-templates/actions/docker-publish@main
with: # publishing image registry.hub.docker.com/my-namespace/my-image:v1.1.0
docker-registry: "registry.hub.docker.com"
image-namespace: "my-namespace"
image-name: "my-image"
image-tag: "v1.1.0"
image-artifact-name: "tarball"
working-directory: "./tarball"
</code></li>
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |                        DEFAULT                         |                                                      DESCRIPTION                                                      |
|---------------------|--------|----------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|   docker-registry   | string |  false   |                                                        |                                       Host where the image should be pushed to.                                       |
| image-artifact-name | string |  false   |                   <code>"image-artifact"</code>                   | Name of the artifact that contains the Docker image.tar file to push, see https://github.com/actions/upload-artifact. |
|     image-name      | string |  false   |        <code>"${{ github.event.repository.name }}"</code>         |                                                 Name of Docker image.                                                 |
|   image-namespace   | string |  false   |                                                        |                                              Namespace of Docker image.                                               |
|      image-tag      | string |  false   | <code>"pipeline-${{ github.run_id }}-git-${GITHUB_SHA::8}"</code> |                                                 Tag of Docker image.                                                  |
|  working-directory  | string |  false   |                         <code>"."</code>                          |                                     Working directory for your Docker artifacts.                                      |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
