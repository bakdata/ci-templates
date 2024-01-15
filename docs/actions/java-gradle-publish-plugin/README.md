<h1>Description java-gradle-publish-plugin composite action</h1>

This action uses Gradle to publish Java plugins to the Gradle Plugin Portal.

<h2>Usage</h2>

<code>yaml
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
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|          INPUT          |  TYPE  | REQUIRED |    DEFAULT    |                           DESCRIPTION                           |
|-------------------------|--------|----------|---------------|-----------------------------------------------------------------|
|      gradle-cache       | string |  false   |   <code>"true"</code>    |   Whether Gradle caching is enabled or not. (Default is true)   |
|   gradle-publish-key    | string |   true   |               |           Key for publishing to Gradle Plugin Portal.           |
|  gradle-publish-secret  | string |   true   |               |         Secret for publishing to Gradle Plugin Portal.          |
|     gradle-version      | string |  false   |  <code>"wrapper"</code>  |      Gradle version to be installed. (Default is wrapper)       |
|    java-distribution    | string |  false   | <code>"microsoft"</code> |    Java distribution to be installed. (Default is microsoft)    |
|      java-version       | string |  false   |    <code>"11"</code>     |          Java version to be installed. (Default is 11)          |
|     signing-key-id      | string |   true   |               |          Key id for signing the Sonatype publication.           |
|    signing-password     | string |   true   |               |         Password for signing the Sonatype publication.          |
| signing-secret-key-ring | string |   true   |               | Key ring (base64 encoded) for signing the Sonatype publication. |
|    working-directory    | string |  false   |     <code>"."</code>     |   Working directory of your Gradle artifacts. (Default is .)    |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
