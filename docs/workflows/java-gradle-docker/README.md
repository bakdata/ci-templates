# Description of java-gradle-docker reusable Workflow

This workflow will build, test and publish a Java Gradle project including a tarball image. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Sonar](https://github.com/bakdata/gradle-plugins/tree/master/sonar), [Sonatype](https://github.com/bakdata/gradle-plugins/tree/master/sonatype) and [Jib](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub and Docker.

## Dependencies

This workflow is built from multiple composite actions and workflows listed below:

- [java-gradle-base](https://github.com/bakdata/ci-templates/tree/main/.github/workflows/java-gradle-base.yaml)
- [java-gradle-build-jib](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build-jib)
- [java-gradle-publish](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish)
- [docker-publish](https://github.com/bakdata/ci-templates/tree/main/actions/docker-publish)
- [java-gradle-release-github](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github)

## Calling the workflow

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Docker
    uses: bakdata/ci-templates/.github/workflows/java-gradle-docker.yaml@main
    with:
      docker-publisher: "my-publisher" # (Required)
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
      docker-username: ${{ secrets.DOCKERHUB_USERNAME }}
      docker-password: ${{ secrets.DOCKERHUB_TOKEN }}
      github-username: ${{ secrets.GH_USERNAME }}
      github-token: ${{ secrets.GH_TOKEN }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                       | TYPE    | REQUIRED | DEFAULT                     | DESCRIPTION                                                                                       |
| --------------------------- | ------- | -------- | --------------------------- | ------------------------------------------------------------------------------------------------- |
| docker-publisher            | string  | true     |                             | Publisher to prefix Docker image.                                                                 |
| docker-registry             | string  | false    | `"docker.io"`               | Host where the image should be pushed to.                                                         |
| gradle-cache                | boolean | false    | `true`                      | Whether Gradle caching is enabled or not. (Default is true)                                       |
| gradle-cache-read-only      | boolean | false    | `false`                     | Whether Gradle caching should be read-only. Only used for build and test jobs. (Default is false) |
| gradle-refresh-dependencies | boolean | false    | `false`                     | Whether Gradle should refresh dependencies. (Default is false)                                    |
| gradle-version              | string  | false    | `"wrapper"`                 | Gradle version to be installed. (Default is wrapper)                                              |
| java-distribution           | string  | false    | `"microsoft"`               | Java distribution to be installed. (Default is microsoft)                                         |
| java-version                | string  | false    | `"11"`                      | Java version to be installed. (Default is 11)                                                     |
| platforms                   | string  | false    | `"linux/amd64,linux/arm64"` | Architectures for the created image (comma separated)                                             |
| working-directory           | string  | false    | `"."`                       | Working directory of your Gradle artifacts. (Default is .)                                        |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
