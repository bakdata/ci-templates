# Description java-gradle-publish-plugin composite action

This action uses Gradle to publish Java plugins to the Gradle Plugin Portal.

## Usage

```yaml
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish-plugin@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      gradle-publish-key: ${{ secrets.gradle-publish-key }}
      gradle-publish-secret: ${{ secrets.gradle-publish-secret }}
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
| gradle-cache                | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                         |
| gradle-cache-read-only      | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches. |
| gradle-publish-key          | string | true     |                                                                                                         | Key for publishing to Gradle Plugin Portal.                                                                                                                         |
| gradle-publish-secret       | string | true     |                                                                                                         | Secret for publishing to Gradle Plugin Portal.                                                                                                                      |
| gradle-refresh-dependencies | string | false    | `"false"`                                                                                               | Whether Gradle should refresh dependencies. (Default is false)                                                                                                      |
| gradle-version              | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                |
| java-distribution           | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                           |
| java-version                | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                       |
| signing-key-id              | string | true     |                                                                                                         | Key id for signing the Sonatype publication.                                                                                                                        |
| signing-password            | string | true     |                                                                                                         | Password for signing the Sonatype publication.                                                                                                                      |
| signing-secret-key-ring     | string | true     |                                                                                                         | Key ring (base64 encoded) for signing the Sonatype publication.                                                                                                     |
| working-directory           | string | false    | `"."`                                                                                                   | Working directory of your Gradle artifacts. (Default is .)                                                                                                          |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
