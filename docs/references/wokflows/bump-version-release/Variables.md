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
