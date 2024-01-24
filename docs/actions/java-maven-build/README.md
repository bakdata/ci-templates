# Description java-maven-build composite action

This action builds Java artifacts using Maven.

## Usage

```yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-maven-build@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
      command: "compile" # (Optional)
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT       | DESCRIPTION                                               |
| ----------------- | ------ | -------- | ------------- | --------------------------------------------------------- |
| command           | string | false    | `"compile"`   | Command to run build with. (Default is compile)           |
| java-distribution | string | false    | `"microsoft"` | Java distribution to be installed. (Default is microsoft) |
| java-version      | string | false    | `"11"`        | Java version to be installed. (Default is 11)             |
| maven-version     | string | true     |               | Maven version to be installed.                            |
| working-directory | string | false    | `"."`         | Working directory of your Maven artifacts. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
