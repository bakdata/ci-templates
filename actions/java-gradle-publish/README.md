# java-gradle-publish

This action uses Gradle to publish Java artifacts to Sonatype Nexus and Java plugins to the Gradle Plugin Portal.

## Input Parameters

| Name                    | Required | Default Value |  Type  | Description                                                                                         |
| ----------------------- | :------: | :-----------: | :----: | --------------------------------------------------------------------------------------------------- |
| signing-secret-key-ring |    ✅    |       -       | string | Key ring (base64 encoded) for signing the Sonatype publication                                      |
| signing-key-id          |    ✅    |       -       | string | Key id for signing the Sonatype publication                                                         |
| signing-password        |    ✅    |       -       | string | Password for signing the Sonatype publication                                                       |
| ossrh-username          |    ✅    |       -       | string | Username for signing into Sonatype repository                                                       |
| ossrh-password          |    ✅    |       -       | string | Password for signing into Sonatype repository                                                       |
| gradle-publish-key      |    ❌    |       -       | string | Key for publishing to Gradle Plugin Portal. Optional because it is only used for plugin projects    |
| gradle-publish-secret   |    ❌    |       -       | string | Secret for publishing to Gradle Plugin Portal. Optional because it is only used for plugin projects |
| java-distribution       |    ❌    |   microsoft   | string | Java distribution to be installed                                                                   |
| java-version            |    ❌    |      11       | string | Java version to be installed                                                                        |
| gradle-version          |    ❌    |    wrapper    | string | Gradle version to be installed                                                                      |
| working-directory       |    ❌    |     "./"      | string | Working directory of your Gradle artifacts                                                          |

## Usage

```yaml

---
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      ossrh-username: ${{ secrets.ossrh-username }}
      ossrh-password: ${{ secrets.ossrh-password }}
      gradle-publish-key: ${{ secrets.gradle-publish-key }} # (Optional)
      gradle-publish-secret: ${{ secrets.gradle-publish-secret }} # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "./" # (Optional)
```
