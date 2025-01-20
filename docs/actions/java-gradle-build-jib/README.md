## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                       | TYPE   | REQUIRED | DEFAULT                                                                                                 | DESCRIPTION                                                                                                                                                         |
| --------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| allow-insecure-registries   | string | false    | `"false"`                                                                                               | Whether to allow insecure registries or not. (Default is false)                                                                                                     |
| class                       | string | false    |                                                                                                         | The entrypoint class to be used for the image                                                                                                                       |
| download-lfs-files          | string | false    | `"false"`                                                                                               | Whether the Git checkout action should resolve LFS files or not. (Default is false)                                                                                 |
| gradle-cache                | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                         |
| gradle-cache-read-only      | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches. |
| gradle-refresh-dependencies | string | false    | `"false"`                                                                                               | Whether Gradle should refresh dependencies. (Default is false)                                                                                                      |
| gradle-version              | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                |
| java-distribution           | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                           |
| java-version                | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                       |
| jib-from-image              | string | false    |                                                                                                         | The Jib base image to use                                                                                                                                           |
| platforms                   | string | false    | `"linux/amd64,linux/arm64"`                                                                             | Architectures for the created image (comma separated)                                                                                                               |
| repository                  | string | false    |                                                                                                         | The repository to push the image to                                                                                                                                 |
| working-directory           | string | false    | `"."`                                                                                                   | Working directory of your Gradle artifacts. (Default is .)                                                                                                          |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT    | TYPE   | DESCRIPTION                  |
| --------- | ------ | ---------------------------- |
| image-tag | string | The tag of the docker image. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
