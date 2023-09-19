# java-maven-build

This action builds Java artifacts using Maven.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                        |
| ----------------- | :------: | :-----------: | :----: | -------------------------------------------------------------------------------------------------- |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                       |
| working-directory |    ❌    |      "."      | string | Working directory of your Maven artifacts                                                          |
| command           |    ❌    |    compile    | string | Command to run build with                                                                          |

## Usage

```yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-maven-build@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
      command: "compile" # (Optional)
```
