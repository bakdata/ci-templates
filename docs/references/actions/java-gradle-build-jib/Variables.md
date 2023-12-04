# Refenrences java-gradle-build-jib composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                                 | DESCRIPTION                                                                                                                              |
| ------------------- | ------ | -------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| download-lfs-files  | string | false    | `"false"`                               | Whether the Git checkout action should resolve LFS files or not. (Default is false)                                                      |
| gradle-cache        | string | false    | `"true"`                                | Whether Gradle caching is enabled or not. (Default is true)                                                                              |
| gradle-version      | string | false    | `"wrapper"`                             | Gradle version to be installed. (Default is wrapper)                                                                                     |
| image-artifact-name | string | false    | `"image-artifact"`                      | Artifact name to upload tarball image, see https://github.com/actions/upload-artifact                                                    |
| image-name          | string | false    | `"${{ github.event.repository.name }}"` | Name of Docker image.                                                                                                                    |
| java-distribution   | string | false    | `"microsoft"`                           | Java distribution to be installed. (Default is microsoft)                                                                                |
| java-version        | string | false    | `"11"`                                  | Java version to be installed. (Default is 11)                                                                                            |
| jib-from-image      | string | false    |                                         | The Jib base image to use                                                                                                                |
| subproject          | string | false    |                                         | The Gradle subproject for which the tarball image should be built (If not specified, a tarball image for the root project will be built) |
| working-directory   | string | false    | `"."`                                   | Working directory of your Gradle artifacts. (Default is .)                                                                               |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
