<h1>Description of java-gradle-base reusable Workflow</h1>

This workflow will build, test and publish a Java Gradle project.

<h2>Prerequisites</h2>

Your Java project needs to be set up with Gradle and either needs to contain a <code>build.gradle</code> or a <code>build.gradle.kts</code>
file that uses the <a href="https://github.com/bakdata/gradle-plugins/tree/master/sonar">Sonar</a>, <a href="https://github.com/bakdata/gradle-plugins/tree/master/sonatype">Sonatype</a> and <a href="https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin">Jib</a> plugins. Moreover, prepare credentials for Sonarcloud, Sonatype, GitHub and Docker.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-build">java-gradle-build</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-test">java-gradle-test</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-assess-code-quality">java-gradle-assess-code-quality</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Call this reusable workflow

on:
  push:
    branches: [main]

jobs:
  call-workflow-passing-data:
    name: Java Gradle Docker
    uses: bakdata/ci-templates/.github/workflows/java-gradle-base.yaml@main
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
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE   | REQUIRED |    DEFAULT    |                                     DESCRIPTION                                     |
|--------------------|---------|----------|---------------|-------------------------------------------------------------------------------------|
| download-lfs-files | boolean |  false   |    <code>false</code>    | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
|    gradle-cache    | boolean |  false   |    <code>true</code>     |             Whether Gradle caching is enabled or not. (Default is true)             |
|   gradle-version   | string  |  false   |  <code>"wrapper"</code>  |                Gradle version to be installed. (Default is wrapper)                 |
| java-distribution  | string  |  false   | <code>"microsoft"</code> |              Java distribution to be installed. (Default is microsoft)              |
|    java-version    | string  |  false   |    <code>"11"</code>     |                    Java version to be installed. (Default is 11)                    |
| working-directory  | string  |  false   |     <code>"."</code>     |             Working directory of your Gradle artifacts. (Default is .)              |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|         SECRET          | REQUIRED |                           DESCRIPTION                           |
|-------------------------|----------|-----------------------------------------------------------------|
|     signing-key-id      |   true   |          Key id for signing the Sonatype publication.           |
|    signing-password     |   true   |         Password for signing the Sonatype publication.          |
| signing-secret-key-ring |   true   | Key ring (base64 encoded) for signing the Sonatype publication. |
|   sonar-organization    |   true   |                   Organization for Sonarcloud                   |
|       sonar-token       |   true   |                      Token for Sonarcloud.                      |

<!-- AUTO-DOC-SECRETS:END -->
