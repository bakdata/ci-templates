# Description of java-gradle-release reusable Workflow

This workflow will release your Java Gradle project. That means it will bump the version according to
your `release-type`, push the bumped version to the default branch and a tag branch, push a new SNAPSHOT version to commit to the default branch and generate and push a changelog to the default branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Researchgate Release](https://plugins.gradle.org/plugin/net.researchgate.release) plugin. Moreover, prepare a `github-username`, a `github-email` and a `github-token` to push to GitHub.

## Dependencies

This workflow is built from another composite action listed below:

- [java-gradle-setup](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-setup)

## Calling the workflow

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "The scope of the release (major, minor or patch)."
        default: "patch"
        required: false

jobs:
  call-workflow-passing-data:
    name: Java Gradle Release
    uses: bakdata/ci-templates/.github/workflows/java-gradle-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}"
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      gradle-cache: false # (Optional) Default is true
      working-directory: "." # (Optional) Default is .
    secrets:
      github-username: "${{ secrets.GH_USERNAME }}"
      github-email: "${{ secrets.GH_EMAIL }}"
      github-token: "${{ secrets.GH_TOKEN }}"

  use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```

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

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
