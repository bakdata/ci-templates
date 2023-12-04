# Refenrences java-maven-test composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                                         |
| ------------------ | ------ | -------- | ------------- | ----------------------------------------------------------------------------------- |
| command            | string | false    | `"test"`      | Command to run tests with. (Default is test)                                        |
| download-lfs-files | string | false    | `"false"`     | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| java-distribution  | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)                           |
| java-version       | string | false    | `"11"`        | Java version to be installed. (Default is 11)                                       |
| maven-version      | string | true     |               | Maven version to be installed.                                                      |
| working-directory  | string | false    | `"."`         | Working directory of your Maven artifacts. (Default is .)                           |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                                         |
| ------------------ | ------ | -------- | ------------- | ----------------------------------------------------------------------------------- |
| command            | string | false    | `"test"`      | Command to run tests with. (Default is test)                                        |
| download-lfs-files | string | false    | `"false"`     | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| java-distribution  | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)                           |
| java-version       | string | false    | `"11"`        | Java version to be installed. (Default is 11)                                       |
| maven-version      | string | true     |               | Maven version to be installed.                                                      |
| working-directory  | string | false    | `"."`         | Working directory of your Maven artifacts. (Default is .)                           |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
