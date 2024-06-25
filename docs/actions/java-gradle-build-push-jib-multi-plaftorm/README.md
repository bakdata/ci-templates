# Description java-gradle-build-push-jib-multi-platform composite action

This action builds and pushes a multi-plaform image using [Jib Gradle](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) to a private image registry.

## Usage

```yaml
steps:
  - name: Build multi-plaform image
    uses: bakdata/ci-templates/actions/java-gradle-build-push-jib-multi-platform@main
    with:
      full-image-name: "registry/image-name" # (Optional)
      registry-password: "registry-password" # (Optional)
      image-tag: "tag" # (Optional)
      image-artifact-name: "image-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                       | TYPE   | REQUIRED | DEFAULT                                                                                                 | DESCRIPTION                                                                                                                                                             |
| --------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| additional-tags             | string | false    |                                                                                                         | Additional tags to be pushed to the registry. Comma seperated list.                                                                                                     |
| allow-insecure-registries   | string | false    | `"false"`                                                                                               | Whether to allow insecure registries or not. (Default is false)                                                                                                         |
| class                       | string | false    |                                                                                                         | The entrypoint class to be used for the image                                                                                                                           |
| download-lfs-files          | string | false    | `"false"`                                                                                               | Whether the Git checkout action should resolve LFS files or not. (Default is false)                                                                                     |
| full-image-name             | string | true     |                                                                                                         | Full name of image (registry/image:tag) If an image name is provided without a tag, 'latest' will be used. Be careful with registries that dont allow overwriting tags. |
| gradle-cache                | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                             |
| gradle-cache-read-only      | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches.     |
| gradle-refresh-dependencies | string | false    | `"false"`                                                                                               | Whether Gradle should refresh dependencies. (Default is false)                                                                                                          |
| gradle-version              | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                    |
| java-distribution           | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                               |
| java-version                | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                           |
| jib-from-image              | string | false    |                                                                                                         | The Jib base image to use                                                                                                                                               |
| subproject                  | string | false    |                                                                                                         | The Gradle subproject for which the tarball image should be built (If not specified, a tarball image for the root project will be built)                                |
| working-directory           | string | false    | `"."`                                                                                                   | Working directory of your Gradle artifacts. (Default is .)                                                                                                              |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
