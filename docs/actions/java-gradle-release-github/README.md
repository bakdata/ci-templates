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

| INPUT                       | TYPE   | REQUIRED | DEFAULT                                                                                                 | DESCRIPTION                                                                                                                                                         |
| --------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| github-token                | string | true     |                                                                                                         | GitHub token for requesting changes from API.                                                                                                                       |
| gradle-cache                | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                         |
| gradle-cache-read-only      | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches. |
| gradle-refresh-dependencies | string | false    | `"false"`                                                                                               | Whether Gradle should refresh dependencies. (Default is false)                                                                                                      |
| gradle-version              | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                |
| java-distribution           | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                           |
| java-version                | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                       |
| working-directory           | string | false    | `"."`                                                                                                   | Working directory of your Gradle artifacts. (Default is .)                                                                                                          |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
