# Description java-gradle-release composite action

This action releases Java Gradle artifacts by createing a tag on GitHub.

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release@main
    with:
      release-type: "patch"
      github-email: ${{ secrets.github-email }}
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      gradle-cache: false # (Optional)
      working-directory: "." # (Optional)
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)
- [bakdata/ci-templates/actions/changelog-generate@1.38.0](https://github.com/bakdata/ci-templates/blob/1.38.0/actions/changelog-generate)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT          | DESCRIPTION                                                 |
| ----------------- | ------ | -------- | ---------------- | ----------------------------------------------------------- |
| changelog-file    | string | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository         |
| github-email      | string | true     |                  | GitHub email for requesting changes from API.               |
| github-token      | string | true     |                  | GitHub token for requesting changes from API.               |
| github-username   | string | true     |                  | GitHub username for requesting changes from API.            |
| gradle-cache      | string | false    | `"true"`         | Whether Gradle caching is enabled or not. (Default is true) |
| gradle-version    | string | false    | `"wrapper"`      | Gradle version to be installed. (Default is wrapper)        |
| java-distribution | string | false    | `"microsoft"`    | Java distribution to be installed. (Default is microsoft)   |
| java-version      | string | false    | `"11"`           | Java version to be installed. (Default is 11)               |
| release-type      | string | true     |                  | Scope of the release                                        |
| working-directory | string | false    | `"."`            | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                         |
| --------------- | ------ | ----------------------------------- |
| release-version | string | The bumped version of your release. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
