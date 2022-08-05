# java-gradle-test

This action sets up Java and Gradle.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                     |
|-------------------|:--------:|:-------------:|:------:|-------------------------------------------------|
| java-distribution |    ❌     |   microsoft   | string | Java distribution to be installed               |
| java-version      |    ❌     |      11       | string | Java version to be installed                    |
| gradle-version    |    ❌     |    wrapper    | string | Gradle version to be installed                  |
| working-directory |    ❌     |     "./"      | string | Working directory of your Gradle artifacts      |

## Usage

```yaml
...
steps:
  - name: Set up Gradle
    uses: bakdata/ci-templates/actions/java-gradle-setup@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "./" # (Optional)
...
```
