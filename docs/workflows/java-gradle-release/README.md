<h1>Description of java-gradle-release reusable Workflow</h1>

This workflow will release your Java Gradle project. That means it will bump the version according to
your <code>release-type</code>, push the bumped version to the default branch and a tag branch, push a new SNAPSHOT version to commit to the default branch and generate and push a changelog to the default branch.

<h2>Prerequisites</h2>

Your Java project needs to be set up with Gradle and either needs to contain a <code>build.gradle</code> or a <code>build.gradle.kts</code>
file that uses the <a href="https://plugins.gradle.org/plugin/net.researchgate.release">Researchgate Release</a> plugin. Moreover, prepare a <code>github-username</code>, a <code>github-email</code> and a <code>github-token</code> to push to GitHub.

<h2>Dependencies</h2>

This workflow is built from another composite action listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-setup">java-gradle-setup</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "The scope of the release (major, minor or patch)."
        default: "patch"
        required: false

jobs:
  call-workflow-passing-data:
    name: Java Gradle Release
    uses: bakdata/ci-templates/.github/workflows/java-gradle-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}"
      java-distribution: "microsoft" # (Optional) Default is microsoft
      java-version: "11" # (Optional) Default is 11
      gradle-version: "wrapper" # (Optional) Default is wrapper
      gradle-cache: false # (Optional) Default is true
      working-directory: "." # (Optional) Default is .
    secrets:
      github-username: "${{ secrets.GH<em>USERNAME }}"
      github-email: "${{ secrets.GH</em>EMAIL }}"
      github-token: "${{ secrets.GH_TOKEN }}"

use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE   | REQUIRED |     DEFAULT      |                         DESCRIPTION                         |
|-------------------|---------|----------|------------------|-------------------------------------------------------------|
|  changelog-file   | string  |  false   | <code>"CHANGELOG.md"</code> |     Path to the changelog file in the GitHub repository     |
|   gradle-cache    | boolean |  false   |      <code>true</code>      | Whether Gradle caching is enabled or not. (Default is true) |
|  gradle-version   | string  |  false   |   <code>"wrapper"</code>    |    Gradle version to be installed. (Default is wrapper)     |
| java-distribution | string  |  false   |  <code>"microsoft"</code>   |  Java distribution to be installed. (Default is microsoft)  |
|   java-version    | string  |  false   |      <code>"11"</code>      |        Java version to be installed. (Default is 11)        |
|   release-type    | string  |   true   |                  |        Scope of the release (major, minor or patch).        |
| working-directory | string  |  false   |      <code>"."</code>       | Working directory of your Gradle artifacts. (Default is .)  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |                      VALUE                      |           DESCRIPTION           |
|-----------------|-------------------------------------------------|---------------------------------|
| release-version | <code>"${{ jobs.release.outputs.release-version }}"</code> | Bumped version of your project. |

<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|     SECRET      | REQUIRED |                 DESCRIPTION                 |
|-----------------|----------|---------------------------------------------|
|  github-email   |   true   |  GitHub email for committing the changes.   |
|  github-token   |   true   |  GitHub token for committing the changes.   |
| github-username |   true   | GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
