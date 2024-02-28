# Description java-gradle-setup composite action

This action sets up Java and Gradle.

## Usage

```yaml
steps:
  - name: Set up Gradle
    uses: bakdata/ci-templates/actions/java-gradle-setup@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
```

## Dependencies

- [actions/setup-java@v3](https://github.com/actions/setup-java/tree/v3)
- [gradle/gradle-build-action@v2](https://github.com/gradle/gradle-build-action/tree/v2)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                  | TYPE   | REQUIRED | DEFAULT                                                                                                 | DESCRIPTION                                                                                                                                                         |
| ---------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gradle-cache           | string | false    | `"true"`                                                                                                | Whether Gradle caching is enabled or not. (Default is true)                                                                                                         |
| gradle-cache-read-only | string | false    | `"${{ github.event.repository != null && github.ref_name != github.event.repository.default_branch }}"` | Whether Gradle caching should be read-only. By default this value is 'false' for workflows on the GitHub default branch and 'true' for workflows on other branches. |
| gradle-version         | string | false    | `"wrapper"`                                                                                             | Gradle version to be installed. (Default is wrapper)                                                                                                                |
| java-distribution      | string | false    | `"microsoft"`                                                                                           | Java distribution to be installed. (Default is microsoft)                                                                                                           |
| java-version           | string | false    | `"11"`                                                                                                  | Java version to be installed. (Default is 11)                                                                                                                       |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
