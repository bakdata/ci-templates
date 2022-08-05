# java-gradle-build

This action builds java artifacts using gradle and uploads `.jar` files as a pipeline artifact.

## Input Parameters

| Name                | Required | Default Value  |  Type  | Description                                                                                                         |
|---------------------|:--------:|:--------------:|:------:|---------------------------------------------------------------------------------------------------------------------|
| build-artifact-name |    ❌     | build-artifact | string | Pipeline artifact name that is used for uploading build artifacts, see <https://github.com/actions/upload-artifact> |
| java-distribution   |    ❌     |   microsoft    | string | Java distribution to be installed                                                                                   |
| java-version        |    ❌     |       11       | string | Java version to be installed                                                                                        |
| gradle-version      |    ❌     |    wrapper     | string | Gradle version to be installed                                                                                      |
| working-directory   |    ❌     |      "./"      | string | Working directory of your Gradle artifacts                                                                          |

## Usage

```yaml
...
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-gradle-build@main
    with:
      build-artifact-name: "build-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "./" # (Optional)
...
```
