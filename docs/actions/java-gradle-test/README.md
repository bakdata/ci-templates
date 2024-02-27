# Description java-gradle-test composite action

This action runs Junit tests, publishes the test results and tests signing for Sonatype.

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
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
| download-lfs-files          | string | false    | `"false"`                                                                                               | Whether the Git checkout action should resolve LFS files or not. (Default is false)                                                                                 |
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
