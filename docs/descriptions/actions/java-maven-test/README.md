# Description java-maven-test composite action

This action runs Junit tests and publishes the test results.

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-maven-test@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
      command: "test" # (Optional)
```
