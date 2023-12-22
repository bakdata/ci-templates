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
