# java-gradle-publish-plugin

This action uses Gradle to publish Java plugins to the Gradle Plugin Portal.

## Input Parameters

| Name                    | Required | Default Value |  Type   | Description                                                                                                   |
| ----------------------- | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| signing-secret-key-ring |    ✅     |       -       | string  | Key ring (base64 encoded) for signing the Sonatype publication                                                |
| signing-key-id          |    ✅     |       -       | string  | Key id for signing the Sonatype publication                                                                   |
| signing-password        |    ✅     |       -       | string  | Password for signing the Sonatype publication                                                                 |
| gradle-publish-key      |    ✅     |       -       | string  | Key for publishing to Gradle Plugin Portal                                                                    |
| gradle-publish-secret   |    ✅     |       -       | string  | Secret for publishing to Gradle Plugin Portal                                                                 |
| java-distribution       |    ❌     |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version            |    ❌     |      11       | string  | Java version to be installed                                                                                  |
| gradle-version          |    ❌     |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| gradle-cache            |    ❌     |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| working-directory       |    ❌     |      "."      | string  | Working directory of your Gradle artifacts                                                                    |

## Usage

```yaml
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish-plugin@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      gradle-publish-key: ${{ secrets.gradle-publish-key }}
      gradle-publish-secret: ${{ secrets.gradle-publish-secret }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
