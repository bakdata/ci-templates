# Refenrences java-gradle-release reusable Workflow

## Inputs

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

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                     |
| --------------- | ----------------------------------------------- | ------------------------------- |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | Bumped version of your project. |

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                 |
| --------------- | -------- | ------------------------------------------- |
| github-email    | true     | GitHub email for committing the changes.    |
| github-token    | true     | GitHub token for committing the changes.    |
| github-username | true     | GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->

## Inputs

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

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                     |
| --------------- | ----------------------------------------------- | ------------------------------- |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | Bumped version of your project. |

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                 |
| --------------- | -------- | ------------------------------------------- |
| github-email    | true     | GitHub email for committing the changes.    |
| github-token    | true     | GitHub token for committing the changes.    |
| github-username | true     | GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
