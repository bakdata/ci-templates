# Refenrences changelog-generate composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                     | TYPE   | REQUIRED | DEFAULT          | DESCRIPTION                                                    |
| ------------------------- | ------ | -------- | ---------------- | -------------------------------------------------------------- |
| changelog-file            | string | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository            |
| commit-mode               | string | false    | `"false"`        | Special configuration for projects which work without PRs.     |
| config                    | string | false    |                  | Path to the changelog config JSON file                         |
| fetch-release-information | string | false    | `"false"`        | Will enable fetching additional release information from tags. |
| fetch-reviewers           | string | false    | `"false"`        | Will enable fetching the users/reviewers who approved the PR   |
| github-token              | string | true     |                  | The GitHub token for committing the changes.                   |
| new-tag                   | string | true     |                  | Version after bump                                             |
| old-tag                   | string | false    |                  | Previous version. Let empty for releases                       |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT           | TYPE   | DESCRIPTION                                           |
| ---------------- | ------ | ----------------------------------------------------- |
| merged-changelog | string | Changelog containing listing of all single changelogs |
| single-changelog | string | Changelog containing changes of the latest tag        |

<!-- AUTO-DOC-OUTPUT:END -->
