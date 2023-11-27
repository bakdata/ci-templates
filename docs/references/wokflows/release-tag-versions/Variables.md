# Refenrences release-tag-versions reusable Workflow

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                   | TYPE   | REQUIRED | DEFAULT      | DESCRIPTION                                                                                                |
| ----------------------- | ------ | -------- | ------------ | ---------------------------------------------------------------------------------------------------------- |
| next-dev-release-suffix | string | false    | `"SNAPSHOT"` | The suffix to add for the developer version                                                                |
| next-dev-release-type   | string | true     |              | Scope of the next release (minor or patch) for developers                                                  |
| release-type            | string | true     |              | Scope of the release (major, minor or patch).                                                              |
| version-configs-dir     | string | true     |              | The Path to the directory containing the file where the versioning is defined and `.bumpversion.cfg` file. |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

## Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
