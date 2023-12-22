# Description bump-version-release reusable Workflow

This workflow will release your Bump Version project. That means it will bump the version according to your `release-type`, create a Git tag, and create a GitHub release with an optional changelog.

## Prerequisites

A `.bumpversion.cfg` needs to be located inside `working-directory` (repository root by default) to use this workflow.
Moreover, prepare a `github-username`, a `github-email` and a `github-token` to push to GitHub.

## Dependencies

This workflow is built from other composite actions listed below:

- [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
- [changelog-generate](https://github.com/bakdata/ci-templates/tree/main/actions/changelog-generate)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)
- [tag-and-release](https://github.com/bakdata/ci-templates/tree/main/actions/tag-and-release)

## Calling the workflow

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "Scope of the release."
        type: choice
        required: true
        default: patch
        options:
          - patch
          - minor
          - major

jobs:
  call-workflow-passing-data:
    name: Release
    uses: bakdata/ci-templates/.github/workflows/bump-version-release.yaml@main
    with:
      release-type: "${{ github.event.inputs.release-type }}"
      changelog: false # (Optional) Default is true
      changelog-config: "./.github/changelog-config.json" # (Optional)
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
