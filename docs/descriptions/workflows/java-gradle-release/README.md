# Description of java-gradle-release reusable Workflow

This workflow will release your Java Gradle project. That means it will bump the version according to
your `release-type`, push the bumped version to the default branch and a tag branch, push a new SNAPSHOT version to commit to the default branch and generate and push a changelog to the default branch.

## Prerequisites

Your Java project needs to be set up with Gradle and either needs to contain a `build.gradle` or a `build.gradle.kts`
file that uses the [Researchgate Release](https://plugins.gradle.org/plugin/net.researchgate.release) plugin. Moreover, prepare a `github-username`, a `github-email` and a `github-token` to push to GitHub.

## Dependencies

This workflow is built from another composite action listed below:

- [java-gradle-setup](https://github.com/bakdata/ci-templates/tree/main/actions/java-gradle-setup)

## Calling the workflow

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
      github-username: "${{ secrets.GH_USERNAME }}"
      github-email: "${{ secrets.GH_EMAIL }}"
      github-token: "${{ secrets.GH_TOKEN }}"

  use-output-of-workflow:
    runs-on: ubuntu-latest
    needs: call-workflow-passing-data
    steps:
      - run: echo Bumped Version from ${{ needs.call-workflow-passing-data.outputs.old-version }} to ${{ needs.call-workflow-passing-data.outputs.release-version }}
```
