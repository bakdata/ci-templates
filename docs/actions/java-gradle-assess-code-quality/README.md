# Description java-gradle-assess-code-quality composite action

This action assesses code quality and tests signing for Sonatype.

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
      sonar-token: ${{ secrets.sonar-token }} # (Optional) If not set, code quality tests are skipped
      sonar-organization: ${{ secrets.sonar-organization }} # (Optional) If not set, code quality tests are skipped
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }} # (Optional) If not set, signing for Sonatype is not tested
      signing-key-id: ${{ secrets.signing-key-id }} # (Optional) If not set, signing for Sonatype is not tested
      signing-password: ${{ secrets.signing-password }} # (Optional) If not set, signing for Sonatype is not tested
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

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
| signing-key-id              | string | false    |                                                                                                         | Key id for signing the Sonatype publication.                                                                                                                        |
| signing-password            | string | false    |                                                                                                         | Password for signing the Sonatype publication.                                                                                                                      |
| signing-secret-key-ring     | string | false    |                                                                                                         | Key ring (base64 encoded) for signing the Sonatype publication.                                                                                                     |
| sonar-organization          | string | false    |                                                                                                         | Organization for Sonarcloud.                                                                                                                                        |
| sonar-token                 | string | false    |                                                                                                         | Token for Sonarcloud.                                                                                                                                               |
| working-directory           | string | false    | `"."`                                                                                                   | Working directory of your Gradle artifacts. (Default is .)                                                                                                          |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
