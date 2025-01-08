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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT          | DESCRIPTION                                                     |
| ----------------- | ------- | -------- | ---------------- | --------------------------------------------------------------- |
| changelog         | boolean | false    | `true`           | Create changelog for release.                                   |
| changelog-config  | string  | false    |                  | Changelog config path.                                          |
| changelog-file    | string  | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository             |
| release-type      | string  | true     |                  | Scope of the release (major, minor or patch).                   |
| working-directory | string  | false    | `"."`            | Working directory containing `.bumpversion.cfg`. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                                      |
| --------------- | ----------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
