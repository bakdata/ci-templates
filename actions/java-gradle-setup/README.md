# java-gradle-setup

This action sets up Java and Gradle.

## Input Parameters

| Name              | Required | Default Value |  Type   | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| java-distribution |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string  | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| gradle-cache      |    ❌    |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |

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
