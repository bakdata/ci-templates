# Refenrences commit-and-push composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT                                           | DESCRIPTION                                         |
| ----------------- | ------ | -------- | ------------------------------------------------- | --------------------------------------------------- |
| add-untracked     | string | false    | `"false"`                                         | Whether to add untracked files to commit.           |
| commit-message    | string | true     |                                                   | The commit message.                                 |
| github-email      | string | true     |                                                   | The GitHub email for committing the changes.        |
| github-token      | string | true     |                                                   | The GitHub token for committing the changes.        |
| github-username   | string | true     |                                                   | The GitHub username for committing the changes.     |
| pass-empty-commit | string | false    | `"false"`                                         | Whether to exit with code 0 when nothing to commit. |
| ref               | string | false    | `"${{ github.event.repository.default_branch }}"` | The ref name to commit and push the files on.       |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
