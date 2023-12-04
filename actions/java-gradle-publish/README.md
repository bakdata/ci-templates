# java-gradle-publish

This action uses Gradle to publish Java artifacts to Sonatype Nexus.

## Input Parameters

| Name                    | Required | Default Value |  Type   | Description                                                                                                   |
| ----------------------- | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| signing-secret-key-ring |    ✅    |       -       | string  | Key ring (base64 encoded) for signing the Sonatype publication                                                |
| signing-key-id          |    ✅    |       -       | string  | Key id for signing the Sonatype publication                                                                   |
| signing-password        |    ✅    |       -       | string  | Password for signing the Sonatype publication                                                                 |
| ossrh-username          |    ✅    |       -       | string  | Username for signing into Sonatype repository                                                                 |
| ossrh-password          |    ✅    |       -       | string  | Password for signing into Sonatype repository                                                                 |
| java-distribution       |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version            |    ❌    |      11       | string  | Java version to be installed                                                                                  |
| gradle-version          |    ❌    |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| gradle-cache            |    ❌    |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| working-directory       |    ❌    |      "."      | string  | Working directory of your Gradle artifacts                                                                    |

## Usage

```yaml
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      ossrh-username: ${{ secrets.ossrh-username }}
      ossrh-password: ${{ secrets.ossrh-password }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
