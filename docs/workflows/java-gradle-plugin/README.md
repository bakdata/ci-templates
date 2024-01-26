# Description of java-gradle-plugin reusable Workflow

This workflow will build, test and publish a Java Gradle plugin project to the Gradle Plugin Portal. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar), [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) and [Plugin Publish](https://plugins.gradle.org/plugin/com.gradle.plugin-publish) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub
and Gradle Plugin Portal.

## Dependencies

This workflow is built from multiple composite actions and workflows listed below:

- [java-gradle-base](https://github.com/bakdata/ci-templates/tree/main/.github/workflows/java-gradle-base.yaml)
- [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
- [java-gradle-publish-plugin](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish-plugin)
- [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

## Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Library
    uses: bakdata/ci-templates/.github/workflows/java-gradle-pluglin.yaml@main
    with:
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      gradle-cache: false # (Optional) Default is true
      working-directory: "." # (Optional) Default is .
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD_TOKEN }}
      sonar-organization: ${{ secrets.SONARCLOUD_ORGANIZATION }}
      signing-secret-key-ring: ${{ secrets.SIGNING_SECRET_KEY_RING }}
      signing-key-id: ${{ secrets.SIGNING_KEY_ID }}
      signing-password: ${{ secrets.SIGNING_PASSWORD }}
      ossrh-username: ${{ secrets.OSSHR_USERNAME }}
      ossrh-password: ${{ secrets.OSSHR_PASSWORD }}
      gradle-publish-key: ${{ secrets.GRADLE_PUBLISH_KEY }}
      gradle-publish-secret: ${{ secrets.GRADLE_PUBLISH_SECRET }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
```

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
