# Refenrences java-gradle-plugin reusable Workflow
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED |    DEFAULT    |                         DESCRIPTION                         |
|-------------------|---------|----------|---------------|-------------------------------------------------------------|
|   gradle-cache    | boolean |  false   |    `true`     | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string  |  false   |  `"wrapper"`  |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string  |  false   | `"microsoft"` |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string  |  false   |    `"11"`     |        Java version to be installed. (Default is 11)        |
| working-directory | string  |  false   |     `"."`     | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|         SECRET          | REQUIRED |                           DESCRIPTION                           |
|-------------------------|----------|-----------------------------------------------------------------|
|      github-token       |   true   |          GitHub token for requesting changes from API.          |
|     github-username     |   true   |        GitHub username for requesting changes from API.         |
|   gradle-publish-key    |   true   |           Key for publishing to Gradle Plugin Portal.           |
|  gradle-publish-secret  |   true   |         Secret for publishing to Gradle Plugin Portal.          |
|     ossrh-password      |   true   |         Password for signing into Sonatype repository.          |
|     ossrh-username      |   true   |         Username for signing into Sonatype repository.          |
|     signing-key-id      |   true   |          Key id for signing the Sonatype publication.           |
|    signing-password     |   true   |         Password for signing the Sonatype publication.          |
| signing-secret-key-ring |   true   | Key ring (base64 encoded) for signing the Sonatype publication. |
|   sonar-organization    |   true   |                   Organization for Sonarcloud                   |
|       sonar-token       |   true   |                      Token for Sonarcloud.                      |

<!-- AUTO-DOC-SECRETS:END -->
