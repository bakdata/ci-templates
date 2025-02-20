# Description java-gradle-release composite action

This action releases Java Gradle artifacts by creating a tag on GitHub.

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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                                |
| ----------------- | ------ | -------- | ------- | ---------------------------------------------------------- |
| github-email      | string | true     |         | GitHub email for requesting changes from API.              |
| github-token      | string | true     |         | GitHub token for requesting changes from API.              |
| github-username   | string | true     |         | GitHub username for requesting changes from API.           |
| release-type      | string | true     |         | Scope of the release                                       |
| working-directory | string | false    | `"."`   | Working directory of your Gradle artifacts. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                         |
| --------------- | ------ | ----------------------------------- |
| release-version | string | The bumped version of your release. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
