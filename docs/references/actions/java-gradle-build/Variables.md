# Refenrences java-gradle-build composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT            | DESCRIPTION                                                                                                                           |
| ------------------- | ------ | -------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| build-artifact-name | string | false    | `"build-artifact"` | Artifact name that is used for uploading build artifacts, see https://github.com/actions/upload-artifact (Default is build-artifact). |
| gradle-cache        | string | false    | `"true"`           | Whether Gradle caching is enabled or not. (Default is true)                                                                           |
| gradle-version      | string | false    | `"wrapper"`        | Gradle version to be installed. (Default is wrapper)                                                                                  |
| java-distribution   | string | false    | `"microsoft"`      | Java distribution to be installed. (Default is microsoft)                                                                             |
| java-version        | string | false    | `"11"`             | Java version to be installed. (Default is 11)                                                                                         |
| working-directory   | string | false    | `"."`              | Working directory of your Gradle artifacts. (Default is .)                                                                            |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT            | DESCRIPTION                                                                                                                           |
| ------------------- | ------ | -------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| build-artifact-name | string | false    | `"build-artifact"` | Artifact name that is used for uploading build artifacts, see https://github.com/actions/upload-artifact (Default is build-artifact). |
| gradle-cache        | string | false    | `"true"`           | Whether Gradle caching is enabled or not. (Default is true)                                                                           |
| gradle-version      | string | false    | `"wrapper"`        | Gradle version to be installed. (Default is wrapper)                                                                                  |
| java-distribution   | string | false    | `"microsoft"`      | Java distribution to be installed. (Default is microsoft)                                                                             |
| java-version        | string | false    | `"11"`             | Java version to be installed. (Default is 11)                                                                                         |
| working-directory   | string | false    | `"."`              | Working directory of your Gradle artifacts. (Default is .)                                                                            |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
