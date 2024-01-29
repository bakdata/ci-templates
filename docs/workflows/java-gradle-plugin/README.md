# Description of java-gradle-plugin reusable Workflow

This workflow will build, test and publish a Java Gradle plugin project to the Gradle Plugin Portal. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar), [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) and [Plugin Publish](https://plugins.gradle.org/plugin/com.gradle.plugin-publish) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub
and Gradle Plugin Portal.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT       | DESCRIPTION                                                 |
| ----------------- | ------- | -------- | ------------- | ----------------------------------------------------------- |
| gradle-cache      | boolean | false    | `true`        | Whether Gradle caching is enabled or not. (Default is true) |
| gradle-version    | string  | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)        |
| java-distribution | string  | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)   |
| java-version      | string  | false    | `"11"`        | Java version to be installed. (Default is 11)               |
| working-directory | string  | false    | `"."`         | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                  | REQUIRED | DESCRIPTION                                                     |
| ----------------------- | -------- | --------------------------------------------------------------- |
| github-token            | true     | GitHub token for requesting changes from API.                   |
| github-username         | true     | GitHub username for requesting changes from API.                |
| gradle-publish-key      | true     | Key for publishing to Gradle Plugin Portal.                     |
| gradle-publish-secret   | true     | Secret for publishing to Gradle Plugin Portal.                  |
| ossrh-password          | true     | Password for signing into Sonatype repository.                  |
| ossrh-username          | true     | Username for signing into Sonatype repository.                  |
| signing-key-id          | true     | Key id for signing the Sonatype publication.                    |
| signing-password        | true     | Password for signing the Sonatype publication.                  |
| signing-secret-key-ring | true     | Key ring (base64 encoded) for signing the Sonatype publication. |
| sonar-organization      | true     | Organization for Sonarcloud                                     |
| sonar-token             | true     | Token for Sonarcloud.                                           |

<!-- AUTO-DOC-SECRETS:END -->
