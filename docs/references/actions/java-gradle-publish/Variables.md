# Refenrences java-gradle-publish composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                   | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                     |
| ----------------------- | ------ | -------- | ------------- | --------------------------------------------------------------- |
| gradle-cache            | string | false    | `"true"`      | Whether Gradle caching is enabled or not. (Default is true)     |
| gradle-version          | string | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)            |
| java-distribution       | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)       |
| java-version            | string | false    | `"11"`        | Java version to be installed. (Default is 11)                   |
| ossrh-password          | string | true     |               | Password for signing into Sonatype repository.                  |
| ossrh-username          | string | true     |               | Username for signing into Sonatype repository.                  |
| signing-key-id          | string | true     |               | Key id for signing the Sonatype publication.                    |
| signing-password        | string | true     |               | Password for signing the Sonatype publication.                  |
| signing-secret-key-ring | string | true     |               | Key ring (base64 encoded) for signing the Sonatype publication. |
| working-directory       | string | false    | `"."`         | Working directory of your Gradle artifacts. (Default is .)      |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->