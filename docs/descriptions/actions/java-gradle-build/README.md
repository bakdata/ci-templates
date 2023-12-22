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
