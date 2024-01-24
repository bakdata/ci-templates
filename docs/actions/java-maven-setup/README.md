# Description java-maven-setup composite action

This action sets up Java and Maven.

## Usage

```yaml
steps:
  - name: Set up Maven
    uses: bakdata/ci-templates/actions/java-maven-setup@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                               |
| ----------------- | ------ | -------- | ------------- | --------------------------------------------------------- |
| java-distribution | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft) |
| java-version      | string | false    | `"11"`        | Java version to be installed. (Default is 11)             |
| maven-version     | string | true     |               | Maven version to be installed.                            |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
