# Description java-gradle-release-github composite action

This action releases Java Gradle Artifacts and a generated changelog on Github.

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release-github@main
    with:
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT          | TYPE   | REQUIRED | DEFAULT          | DESCRIPTION                                         |
| -------------- | ------ | -------- | ---------------- | --------------------------------------------------- |
| changelog-file | string | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository |
| github-token   | string | true     |                  | GitHub token for requesting changes from API.       |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
