# Description java-gradle-build composite action

This action builds Java artifacts using Gradle and uploads `.jar` files as an artifact.

## Usage

```yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-gradle-build@main
    with:
      build-artifact-name: "build-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT            | DESCRIPTION                                                                                                                           |
| ------------------- | ------ | -------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| build-artifact-name | string | false    | `"build-artifact"` | Artifact name that is used for uploading build artifacts, see https://github.com/actions/upload-artifact (Default is build-artifact). |
| gradle-cache        | string | false    | `"true"`           | Whether Gradle caching is enabled or not. (Default is true)                                                                           |
| gradle-version      | string | false    | `"wrapper"`        | Gradle version to be installed. (Default is wrapper)                                                                                  |
| java-distribution   | string | false    | `"microsoft"`      | Java distribution to be installed. (Default is microsoft)                                                                             |
| java-version        | string | false    | `"11"`             | Java version to be installed. (Default is 11)                                                                                         |
| working-directory   | string | false    | `"."`              | Working directory of your Gradle artifacts. (Default is .)                                                                            |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
