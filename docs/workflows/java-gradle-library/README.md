<h1>Description of java-gradle-library reusable Workflow</h1>

This workflow will build, test and publish a Java Gradle library project. Additionally,
the workflow creates a GitHub Release when running on a tag branch.

<h2>Prerequisites</h2>

Your Java project needs to be set up with Gradle and either needs to contain a <code>build.gradle</code> or a <code>build.gradle.kts</code>
file that uses the <a href="https://github.com/bakdata/gradle-plugins/tree/master/sonar">Sonar</a> and <a href="https://github.com/bakdata/gradle-plugins/tree/master/sonatype">Sonatype</a> plugins. Moreover, prepare credentials for Sonarcloud, Sonatype and GitHub.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions and workflows listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/.github/workflows/java-gradle-base.yaml">java-gradle-base</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-publish">java-gradle-publish</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-release-github">java-gradle-release-github</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Library
    uses: bakdata/ci-templates/.github/workflows/java-gradle-library.yaml@main
    with:
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      gradle-cache: false # (Optional) Default is true
      working-directory: "." # (Optional) Default is .
    secrets:
      sonar-token: ${{ secrets.SONARCLOUD<em>TOKEN }}
      sonar-organization: ${{ secrets.SONARCLOUD</em>ORGANIZATION }}
      signing-secret-key-ring: ${{ secrets.SIGNING<em>SECRET</em>KEY<em>RING }}
      signing-key-id: ${{ secrets.SIGNING</em>KEY<em>ID }}
      signing-password: ${{ secrets.SIGNING</em>PASSWORD }}
      ossrh-username: ${{ secrets.OSSHR<em>USERNAME }}
      ossrh-password: ${{ secrets.OSSHR</em>PASSWORD }}
      github-username: ${{ secrets.GH<em>USERNAME }}
      github-token: ${{ secrets.GH</em>TOKEN }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED |    DEFAULT    |                         DESCRIPTION                         |
|-------------------|---------|----------|---------------|-------------------------------------------------------------|
|   gradle-cache    | boolean |  false   |    <code>true</code>     | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string  |  false   |  <code>"wrapper"</code>  |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string  |  false   | <code>"microsoft"</code> |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string  |  false   |    <code>"11"</code>     |        Java version to be installed. (Default is 11)        |
| working-directory | string  |  false   |     <code>"."</code>     | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|         SECRET          | REQUIRED |                           DESCRIPTION                           |
|-------------------------|----------|-----------------------------------------------------------------|
|      github-token       |   true   |          GitHub token for requesting changes from API.          |
|     github-username     |   true   |        GitHub username for requesting changes from API.         |
|     ossrh-password      |   true   |         Password for signing into Sonatype repository.          |
|     ossrh-username      |   true   |         Username for signing into Sonatype repository.          |
|     signing-key-id      |   true   |          Key id for signing the Sonatype publication.           |
|    signing-password     |   true   |         Password for signing the Sonatype publication.          |
| signing-secret-key-ring |   true   | Key ring (base64 encoded) for signing the Sonatype publication. |
|   sonar-organization    |   true   |                   Organization for Sonarcloud                   |
|       sonar-token       |   true   |                      Token for Sonarcloud.                      |

<!-- AUTO-DOC-SECRETS:END -->
