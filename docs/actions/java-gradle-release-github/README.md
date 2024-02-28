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

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [actions/download-artifact@v3](https://github.com/actions/download-artifact/tree/v3)
- [bakdata/ci-templates/actions/changelog-generate@1.38.0](https://github.com/bakdata/ci-templates/blob/1.38.0/actions/changelog-generate)
- [softprops/action-gh-release@v1](https://github.com/softprops/action-gh-release/tree/v1)

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
