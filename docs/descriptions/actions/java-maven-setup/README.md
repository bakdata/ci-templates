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
