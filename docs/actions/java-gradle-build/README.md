<h1>Description java-gradle-build composite action</h1>

This action builds Java artifacts using Gradle and uploads <code>.jar</code> files as an artifact.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-gradle-build@main
    with:
      build-artifact-name: "build-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |      DEFAULT       |                                                              DESCRIPTION                                                              |
|---------------------|--------|----------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| build-artifact-name | string |  false   | <code>"build-artifact"</code> | Artifact name that is used for uploading build artifacts, see https://github.com/actions/upload-artifact (Default is build-artifact). |
|    gradle-cache     | string |  false   |      <code>"true"</code>      |                                      Whether Gradle caching is enabled or not. (Default is true)                                      |
|   gradle-version    | string |  false   |    <code>"wrapper"</code>     |                                         Gradle version to be installed. (Default is wrapper)                                          |
|  java-distribution  | string |  false   |   <code>"microsoft"</code>    |                                       Java distribution to be installed. (Default is microsoft)                                       |
|    java-version     | string |  false   |       <code>"11"</code>       |                                             Java version to be installed. (Default is 11)                                             |
|  working-directory  | string |  false   |       <code>"."</code>        |                                      Working directory of your Gradle artifacts. (Default is .)                                       |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
