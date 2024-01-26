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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                                 |
| ----------------- | ------ | -------- | ------------- | ----------------------------------------------------------- |
| gradle-cache      | string | false    | `"true"`      | Whether Gradle caching is enabled or not. (Default is true) |
| gradle-version    | string | false    | `"wrapper"`   | Gradle version to be installed. (Default is wrapper)        |
| java-distribution | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft)   |
| java-version      | string | false    | `"11"`        | Java version to be installed. (Default is 11)               |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
