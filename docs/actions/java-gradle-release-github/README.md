<h1>Description java-gradle-release-github composite action</h1>

This action releases Java Gradle Artifacts and a generated changelog on Github.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release-github@main
    with:
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |     DEFAULT      |                         DESCRIPTION                         |
|-------------------|--------|----------|------------------|-------------------------------------------------------------|
|  changelog-file   | string |  false   | <code>"CHANGELOG.md"</code> |     Path to the changelog file in the GitHub repository     |
|   github-token    | string |   true   |                  |        GitHub token for requesting changes from API.        |
|  github-username  | string |   true   |                  |      GitHub username for requesting changes from API.       |
|   gradle-cache    | string |  false   |     <code>"true"</code>     | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string |  false   |   <code>"wrapper"</code>    |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string |  false   |  <code>"microsoft"</code>   |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string |  false   |      <code>"11"</code>      |        Java version to be installed. (Default is 11)        |
| working-directory | string |  false   |      <code>"."</code>       | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
