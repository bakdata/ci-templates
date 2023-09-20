# java-maven-test

This action runs Junit tests and publishes the test results.

## Input Parameters

| Name               | Required | Default Value |  Type   | Description                                                                                        |
| ------------------ | :------: | :-----------: | :-----: | -------------------------------------------------------------------------------------------------- |
| java-distribution  |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version       |    ❌    |      11       | string  | Java version to be installed                                                                       |
| maven-version      |    ✅    |       -       | string  | Maven version to be installed                                                                      |
| working-directory  |    ❌    |      "."      | string  | Working directory of your Maven artifacts                                                          |
| download-lfs-files |    ❌    |     false     | boolean | Whether the Git checkout action should resolve LFS files or not                                    |
| command            |    ❌    |     test      | string  | Command to run tests with                                                                          |

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-maven-test@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      maven-version: "3.8.2"
      working-directory: "." # (Optional)
      command: "test" # (Optional)
```
