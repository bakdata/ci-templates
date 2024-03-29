# Description java-gradle-publish composite action

This action uses Gradle to publish Java artifacts to Sonatype Nexus.

## Usage

```yaml
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      ossrh-username: ${{ secrets.ossrh-username }}
      ossrh-password: ${{ secrets.ossrh-password }}
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
| gradle-cache                | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                         |
| gradle-cache-read-only      | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches. |
| gradle-refresh-dependencies | string | false    | `"false"`                                                                                               | Whether Gradle should refresh dependencies. (Default is false)                                                                                                      |
| gradle-version              | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                |
| java-distribution           | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                           |
| java-version                | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                       |
| ossrh-password              | string | true     |                                                                                                         | Password for signing into Sonatype repository.                                                                                                                      |
| ossrh-username              | string | true     |                                                                                                         | Username for signing into Sonatype repository.                                                                                                                      |
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
