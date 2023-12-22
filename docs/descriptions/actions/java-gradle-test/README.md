# Description java-gradle-test composite action

This action runs Junit tests, publishes the test results and tests signing for Sonatype.

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
