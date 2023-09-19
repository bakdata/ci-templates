# java-maven-test

This action runs Junit tests.

## Input Parameters

If you do not set input parameters for publishing code quality test results on Sonarcloud or for testing the signing for
Sonatype, then these steps are skipped.

| Name               | Required | Default Value |  Type   | Description                                                                                        |
| ------------------ | :------: | :-----------: | :-----: | -------------------------------------------------------------------------------------------------- |
| java-distribution  |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version       |    ❌    |      11       | string  | Java version to be installed                                                                       |
| working-directory  |    ❌    |      "."      | string  | Working directory of your Maven artifacts                                                          |
| download-lfs-files |    ❌    |     false     | boolean | Whether the Git checkout action should resolve LFS files or not                                    |

## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-maven-test@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
```
