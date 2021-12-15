# commit-and-push

This composite action commits the changes of your repository with an arbitrary commit message and then pushes
them using an authenticated GitHub user. The GitHub user is set by passing the username, email, and a valid GitHub token to the composite
action.

## Input Parameters

| Name            | Required | Description                                   |
|-----------------|:--------:|-----------------------------------------------|
| ref             |    ✅     | The ref name to commit and push the files on  |
| commit-message  |    ✅     | The commit message                            |
| github-username |    ✅     | The GitHub username for pushing               |
| github-email    |    ✅     | The GitHub email for pushing                  |
| github-token    |    ✅     | The GitHub token for pushing                  |

## Usage

```yaml

    steps:
      # Other Steps ...
      # Imagine that the previous steps bumped the version and changed wrote it to the pyproject.toml file

      - name: Commit and push pyproject.toml file
        uses: bakdata/ci-templates/actions/commit-and-push
        with:
          ref: ${{ inputs.ref }}
          commit-message: "Bump version ${{ steps.release-tag.outputs.old-tag }} → ${{ steps.release-tag.outputs.release-tag }}"
          github-username: ${{ secrets.github-username }}
          github-email: ${{ secrets.github-email }}
          github-token: ${{ secrets.github-token }}

      # Rest of the workflow steps
```