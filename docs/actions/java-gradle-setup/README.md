<h1>Description java-gradle-setup composite action</h1>

This action sets up Java and Gradle.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Set up Gradle
    uses: bakdata/ci-templates/actions/java-gradle-setup@main
    with:
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |    DEFAULT    |                         DESCRIPTION                         |
|-------------------|--------|----------|---------------|-------------------------------------------------------------|
|   gradle-cache    | string |  false   |   <code>"true"</code>    | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string |  false   |  <code>"wrapper"</code>  |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string |  false   | <code>"microsoft"</code> |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string |  false   |    <code>"11"</code>     |        Java version to be installed. (Default is 11)        |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
