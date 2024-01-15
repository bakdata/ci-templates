<h1>Description java-gradle-assess-code-quality composite action</h1>

This action assesses code quality and tests signing for Sonatype.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
      sonar-token: ${{ secrets.sonar-token }} # (Optional) If not set, code quality tests are skipped
      sonar-organization: ${{ secrets.sonar-organization }} # (Optional) If not set, code quality tests are skipped
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }} # (Optional) If not set, signing for Sonatype is not tested
      signing-key-id: ${{ secrets.signing-key-id }} # (Optional) If not set, signing for Sonatype is not tested
      signing-password: ${{ secrets.signing-password }} # (Optional) If not set, signing for Sonatype is not tested
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|          INPUT          |  TYPE  | REQUIRED |    DEFAULT    |                                     DESCRIPTION                                     |
|-------------------------|--------|----------|---------------|-------------------------------------------------------------------------------------|
|   download-lfs-files    | string |  false   |   <code>"false"</code>   | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
|      gradle-cache       | string |  false   |   <code>"true"</code>    |             Whether Gradle caching is enabled or not. (Default is true)             |
|     gradle-version      | string |  false   |  <code>"wrapper"</code>  |                Gradle version to be installed. (Default is wrapper)                 |
|    java-distribution    | string |  false   | <code>"microsoft"</code> |              Java distribution to be installed. (Default is microsoft)              |
|      java-version       | string |  false   |    <code>"11"</code>     |                    Java version to be installed. (Default is 11)                    |
|     signing-key-id      | string |  false   |               |                    Key id for signing the Sonatype publication.                     |
|    signing-password     | string |  false   |               |                   Password for signing the Sonatype publication.                    |
| signing-secret-key-ring | string |  false   |               |           Key ring (base64 encoded) for signing the Sonatype publication.           |
|   sonar-organization    | string |  false   |               |                            Organization for Sonarcloud.                             |
|       sonar-token       | string |  false   |               |                                Token for Sonarcloud.                                |
|    working-directory    | string |  false   |     <code>"."</code>     |             Working directory of your Gradle artifacts. (Default is .)              |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
