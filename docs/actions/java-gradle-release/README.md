<h1>Description java-gradle-release composite action</h1>

This action releases Java Gradle artifacts by createing a tag on GitHub.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release@main
    with:
      release-type: "patch"
      github-email: ${{ secrets.github-email }}
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      gradle-cache: false # (Optional)
      working-directory: "." # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |     DEFAULT      |                         DESCRIPTION                         |
|-------------------|--------|----------|------------------|-------------------------------------------------------------|
|  changelog-file   | string |  false   | <code>"CHANGELOG.md"</code> |     Path to the changelog file in the GitHub repository     |
|   github-email    | string |   true   |                  |        GitHub email for requesting changes from API.        |
|   github-token    | string |   true   |                  |        GitHub token for requesting changes from API.        |
|  github-username  | string |   true   |                  |      GitHub username for requesting changes from API.       |
|   gradle-cache    | string |  false   |     <code>"true"</code>     | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string |  false   |   <code>"wrapper"</code>    |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string |  false   |  <code>"microsoft"</code>   |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string |  false   |      <code>"11"</code>      |        Java version to be installed. (Default is 11)        |
|   release-type    | string |   true   |                  |                    Scope of the release                     |
| working-directory | string |  false   |      <code>"."</code>       | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |  TYPE  |             DESCRIPTION             |
|-----------------|--------|-------------------------------------|
| release-version | string | The bumped version of your release. |

<!-- AUTO-DOC-OUTPUT:END -->
