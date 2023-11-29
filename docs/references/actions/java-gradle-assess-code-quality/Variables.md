# Refenrences java-gradle-assess-code-quality composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                   | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                                         |
| ----------------------- | ------ | -------- | ------------- | ----------------------------------------------------------------------------------- |
| download-lfs-files      | string | false    | `"false"`     | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| gradle-cache            | string | false    | `"true"`      | Whether Gradle caching is enabled or not. (Default is true)                         |
| gradle-version          | string | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)                                |
| java-distribution       | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)                           |
| java-version            | string | false    | `"11"`        | Java version to be installed. (Default is 11)                                       |
| signing-key-id          | string | false    |               | Key id for signing the Sonatype publication.                                        |
| signing-password        | string | false    |               | Password for signing the Sonatype publication.                                      |
| signing-secret-key-ring | string | false    |               | Key ring (base64 encoded) for signing the Sonatype publication.                     |
| sonar-organization      | string | false    |               | Organization for Sonarcloud.                                                        |
| sonar-token             | string | false    |               | Token for Sonarcloud.                                                               |
| working-directory       | string | false    | `"."`         | Working directory of your Gradle artifacts. (Default is .)                          |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                   | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                                         |
| ----------------------- | ------ | -------- | ------------- | ----------------------------------------------------------------------------------- |
| download-lfs-files      | string | false    | `"false"`     | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| gradle-cache            | string | false    | `"true"`      | Whether Gradle caching is enabled or not. (Default is true)                         |
| gradle-version          | string | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)                                |
| java-distribution       | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)                           |
| java-version            | string | false    | `"11"`        | Java version to be installed. (Default is 11)                                       |
| signing-key-id          | string | false    |               | Key id for signing the Sonatype publication.                                        |
| signing-password        | string | false    |               | Password for signing the Sonatype publication.                                      |
| signing-secret-key-ring | string | false    |               | Key ring (base64 encoded) for signing the Sonatype publication.                     |
| sonar-organization      | string | false    |               | Organization for Sonarcloud.                                                        |
| sonar-token             | string | false    |               | Token for Sonarcloud.                                                               |
| working-directory       | string | false    | `"."`         | Working directory of your Gradle artifacts. (Default is .)                          |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
