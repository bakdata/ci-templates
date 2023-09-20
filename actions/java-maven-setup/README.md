# java-maven-setup

This action sets up Java and Maven.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                        |
| ----------------- | :------: | :-----------: | :----: | -------------------------------------------------------------------------------------------------- |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                       |
| maven-version     |    ✅    |       -       | string | Maven version to be installed                                                                      |

## Usage

```yaml
steps:
  - name: Set up Maven
    uses: bakdata/ci-templates/actions/java-maven-setup@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      maven-version: "3.8.2"
```
