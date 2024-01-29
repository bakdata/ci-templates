# Description java-gradle-build-jib composite action

This action builds an image tarball using [Jib Gradle](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) and uploads an `image.tar` file as an artifact.

## Usage

```yaml
steps:
  - name: Build tarball image
    uses: bakdata/ci-templates/actions/java-gradle-build-jib@main
    with:
      image-artifact-name: "image-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)
- [actions/upload-artifact@v3](https://github.com/actions/upload-artifact/tree/v3)

## References

### Inputs

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

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
