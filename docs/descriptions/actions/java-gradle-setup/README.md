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
