# Refenrences java-gradle-test composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                                         |
| ------------------ | ------ | -------- | ------------- | ----------------------------------------------------------------------------------- |
| download-lfs-files | string | false    | `"false"`     | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| gradle-cache       | string | false    | `"true"`      | Whether Gradle caching is enabled or not. (Default is true)                         |
| gradle-version     | string | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)                                |
| java-distribution  | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)                           |
| java-version       | string | false    | `"11"`        | Java version to be installed. (Default is 11)                                       |
| working-directory  | string | false    | `"."`         | Working directory of your Gradle artifacts. (Default is .)                          |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
