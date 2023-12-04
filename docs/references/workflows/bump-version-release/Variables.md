# Refenrences bump-version-release reusable Workflow

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE    | REQUIRED | DEFAULT | DESCRIPTION                                                     |
| ----------------- | ------- | -------- | ------- | --------------------------------------------------------------- |
| changelog         | boolean | false    | `true`  | Create changelog for release.                                   |
| changelog-config  | string  | false    |         | Changelog config path.                                          |
| release-type      | string  | true     |         | Scope of the release (major, minor or patch).                   |
| working-directory | string  | false    | `"."`   | Working directory containing `.bumpversion.cfg`. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                           | DESCRIPTION                                      |
| --------------- | ----------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
