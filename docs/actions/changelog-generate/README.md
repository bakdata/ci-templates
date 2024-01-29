# Description generate-changelog composite action

This action will enable the automated creation of a changelog.
The changelog template needs to be configured using a `changelog-config.json`.
If there is a global changelog managed by the repository this will be updated.
The action generates a new release changelog and an updated version of
the changelog file in the repository (if there is any).
The default setting updates the repo changelog.
If your current repository does not have any global changelog file,
then pass an empty string to the variable `changelog-file`.
The action returns both the new tag's changelog and the global changelog.

When generating the changelog, the action evaluates two factors to decide which PRs to consider:
`old-tag`
(lower bound defining the 'start' from where the changelog will consider merged pull requests)
and `new-tag`
(upper bound defining until which tag the changelog will consider merged pull requests).

The upper bound might be either existing or new.
If the new tag does not yet exist, the action will
nevertheless create the changelog so that it may be included in the release.

## Dependencies

- [mikepenz/release-changelog-builder-action@v4](https://github.com/mikepenz/release-changelog-builder-action/tree/v4)

## References

### Inputs

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

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT           | TYPE   | DESCRIPTION                                           |
| ---------------- | ------ | ----------------------------------------------------- |
| merged-changelog | string | Changelog containing listing of all single changelogs |
| single-changelog | string | Changelog containing changes of the latest tag        |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
