# java-gradle-test

This action runs Junit tests, publishes the test results and tests signing for Sonatype.

## Input Parameters

| Name               | Required | Default Value |  Type   | Description                                                                                                   |
| ------------------ | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| download-lfs-files |    ❌    |     false     | boolean | Whether the Git checkout action should resolve LFS files or not                                               |
| java-distribution  |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version       |    ❌    |      11       | string  | Java version to be installed                                                                                  |
| gradle-cache       |    ❌    |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| gradle-version     |    ❌    |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory  |    ❌    |      "."      | string  | Working directory of your Gradle artifacts                                                                    |

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
