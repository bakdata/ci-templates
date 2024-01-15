<h1>Description java-gradle-test composite action</h1>

This action runs Junit tests, publishes the test results and tests signing for Sonatype.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED |    DEFAULT    |                                     DESCRIPTION                                     |
|--------------------|--------|----------|---------------|-------------------------------------------------------------------------------------|
| download-lfs-files | string |  false   |   <code>"false"</code>   | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
|    gradle-cache    | string |  false   |   <code>"true"</code>    |             Whether Gradle caching is enabled or not. (Default is true)             |
|   gradle-version   | string |  false   |  <code>"wrapper"</code>  |                Gradle version to be installed. (Default is wrapper)                 |
| java-distribution  | string |  false   | <code>"microsoft"</code> |              Java distribution to be installed. (Default is microsoft)              |
|    java-version    | string |  false   |    <code>"11"</code>     |                    Java version to be installed. (Default is 11)                    |
| working-directory  | string |  false   |     <code>"."</code>     |             Working directory of your Gradle artifacts. (Default is .)              |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
