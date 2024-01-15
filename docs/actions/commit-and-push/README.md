<h1>Description commit-and-push composite action</h1>

This composite action commits the changes of your repository with an arbitrary commit message and then pushes them using an authenticated GitHub user. The GitHub user is set by passing the username, email, and a valid GitHub token to the composite action.

<blockquote>
  <strong>Note</strong>
  Pushing to protected branches requires any <code>checkout</code> actions to specify the <code>persist-credentials: false</code> option. Additionally, the configured GitHub user needs to be added as an exclusion in Settings → Branches → Branch protection rule → <strong>Allow specified actors to bypass required pull requests</strong> &amp; <strong>Restrict who can push to matching branches</strong>
</blockquote>

<h2>Usage</h2>

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0
    with:
      persist-credentials: false # required for pushing to protected branch later

<h1>Other Steps ...</h1>

<h1>Imagine that the previous steps change some files and the changes need to be committed</h1>

<ul>
name: Commit and push changes
  uses: bakdata/ci-templates/actions/commit-and-push@main
  with:
    ref: "my-awesome-ref-name" # (Optional) if not set the ${{ github.event.repository.default_branch }} will fill the value
    commit-message: "Committing all the awesome changes in my repository!"
    add-untracked: "true" # (Optional) if not set, only tracked files will be committed
    pass-empty-commit: "true" # (Optional) if not set, fail upon nothing to commit
    github-username: ${{ secrets.github-username }}
    github-email: ${{ secrets.github-email }}
    github-token: ${{ secrets.github-token }}

  # Rest of the workflow steps

```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |                      DEFAULT                      |                     DESCRIPTION                     |
|-------------------|--------|----------|---------------------------------------------------|-----------------------------------------------------|
|   add-untracked   | string |  false   |                     <code>"false"</code>                     |      Whether to add untracked files to commit.      |
|  commit-message   | string |   true   |                                                   |                 The commit message.                 |
|   github-email    | string |   true   |                                                   |    The GitHub email for committing the changes.     |
|   github-token    | string |   true   |                                                   |    The GitHub token for committing the changes.     |
|  github-username  | string |   true   |                                                   |   The GitHub username for committing the changes.   |
| pass-empty-commit | string |  false   |                     <code>"false"</code>                     | Whether to exit with code 0 when nothing to commit. |
|        ref        | string |  false   | <code>"${{ github.event.repository.default_branch }}"</code> |    The ref name to commit and push the files on.    |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
