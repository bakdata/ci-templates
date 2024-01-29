# Description of java-gradle-release reusable Workflow

This workflow will release your Java Gradle project. That means it will bump the version according to
your `release-type`, push the bumped version to the default branch and a tag branch, push a new SNAPSHOT version to commit to the default branch and generate and push a changelog to the default branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Researchgate Release](https://plugins.gradle.org/plugin/net.researchgate.release) plugin. Moreover, prepare a `github-username`, a `github-email` and a `github-token` to push to GitHub.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT          | DESCRIPTION                                                 |
| ----------------- | ------- | -------- | ---------------- | ----------------------------------------------------------- |
| changelog-file    | string  | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository         |
| gradle-cache      | boolean | false    | `true`           | Whether Gradle caching is enabled or not. (Default is true) |
| gradle-version    | string  | false    | `"wrapper"`      | Gradle version to be installed. (Default is wrapper)        |
| java-distribution | string  | false    | `"microsoft"`    | Java distribution to be installed. (Default is microsoft)   |
| java-version      | string  | false    | `"11"`           | Java version to be installed. (Default is 11)               |
| release-type      | string  | true     |                  | Scope of the release (major, minor or patch).               |
| working-directory | string  | false    | `"."`            | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                     |
| --------------- | ----------------------------------------------- | ------------------------------- |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | Bumped version of your project. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                 |
| --------------- | -------- | ------------------------------------------- |
| github-email    | true     | GitHub email for committing the changes.    |
| github-token    | true     | GitHub token for committing the changes.    |
| github-username | true     | GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
