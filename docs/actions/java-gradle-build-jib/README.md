<h1>Description java-gradle-build-jib composite action</h1>

This action builds an image tarball using <a href="https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin">Jib Gradle</a> and uploads an <code>image.tar</code> file as an artifact.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Build tarball image
    uses: bakdata/ci-templates/actions/java-gradle-build-jib@main
    with:
      image-artifact-name: "image-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |                 DEFAULT                 |                                                               DESCRIPTION                                                                |
|---------------------|--------|----------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| download-lfs-files  | string |  false   |                <code>"false"</code>                |                           Whether the Git checkout action should resolve LFS files or not. (Default is false)                            |
|    gradle-cache     | string |  false   |                <code>"true"</code>                 |                                       Whether Gradle caching is enabled or not. (Default is true)                                        |
|   gradle-version    | string |  false   |               <code>"wrapper"</code>               |                                           Gradle version to be installed. (Default is wrapper)                                           |
| image-artifact-name | string |  false   |           <code>"image-artifact"</code>            |                          Artifact name to upload tarball image, see https://github.com/actions/upload-artifact                           |
|     image-name      | string |  false   | <code>"${{ github.event.repository.name }}"</code> |                                                          Name of Docker image.                                                           |
|  java-distribution  | string |  false   |              <code>"microsoft"</code>              |                                        Java distribution to be installed. (Default is microsoft)                                         |
|    java-version     | string |  false   |                 <code>"11"</code>                  |                                              Java version to be installed. (Default is 11)                                               |
|   jib-from-image    | string |  false   |                                         |                                                        The Jib base image to use                                                         |
|     subproject      | string |  false   |                                         | The Gradle subproject for which the tarball image should be built (If not specified, a tarball image for the root project will be built) |
|  working-directory  | string |  false   |                  <code>"."</code>                  |                                        Working directory of your Gradle artifacts. (Default is .)                                        |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
