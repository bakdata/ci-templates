# Refenrences java-maven-build composite action
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |    DEFAULT    |                        DESCRIPTION                        |
|-------------------|--------|----------|---------------|-----------------------------------------------------------|
|      command      | string |  false   |  `"compile"`  |      Command to run build with. (Default is compile)      |
| java-distribution | string |  false   | `"microsoft"` | Java distribution to be installed. (Default is microsoft) |
|   java-version    | string |  false   |    `"11"`     |       Java version to be installed. (Default is 11)       |
|   maven-version   | string |   true   |               |              Maven version to be installed.               |
| working-directory | string |  false   |     `"."`     | Working directory of your Maven artifacts. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |    DEFAULT    |                        DESCRIPTION                        |
|-------------------|--------|----------|---------------|-----------------------------------------------------------|
|      command      | string |  false   |  `"compile"`  |      Command to run build with. (Default is compile)      |
| java-distribution | string 